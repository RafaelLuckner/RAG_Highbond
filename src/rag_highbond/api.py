"""API REST + Servidor MCP Remoto para busca semântica na documentação HighBond.

Inclui:
- Endpoints REST (/buscar, /chunks/{chunk_id}, /health) compatíveis com Custom GPT Actions (OpenAPI)
- Endpoints MCP Remoto (/mcp via Streamable HTTP e /sse) para Claude, ChatGPT, VS Code e Antigravity
- Proteção opcional por API Key (RAG_API_KEY)
- Rate Limiting por IP/usuário (RAG_RATE_LIMIT_PER_MIN)
- Controle de concorrência e cache LRU de embeddings

Uso:
    rag-api                        # sobe em http://127.0.0.1:8000
    rag-api --host 0.0.0.0 --porta 8000
"""

import argparse
from collections import defaultdict, deque
from contextlib import AsyncExitStack, asynccontextmanager
import logging
import secrets
import threading
import time

from fastapi import Depends, FastAPI, HTTPException, Request, Security
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.security import APIKeyHeader, HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel, Field
import uvicorn

from . import config
from .mcp_server import definir_indice, mcp
from .models import ResultadoBusca
from .ollama import (
    OllamaIndisponivel,
    estatisticas_cache_embeddings,
    iniciar_ollama_se_necessario,
    ollama_rodando,
)
from .store import IndiceBusca, IndiceNaoEncontrado

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

# Estado da aplicação: índice carregado uma única vez no startup.
_indice: IndiceBusca | None = None

# Esquemas de segurança documentados no OpenAPI (para Custom GPT Actions e clientes REST)
_bearer_scheme = HTTPBearer(auto_error=False, description="Token Bearer (API Key)")
_api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False, description="Cabeçalho X-API-Key")


class LimitadorTaxa:
    """Rate limiter sliding-window em memória por identificador (IP ou API Key)."""

    def __init__(self, limite_por_minuto: int):
        self.limite = limite_por_minuto
        self.janela = 60.0
        self._historico: dict[str, deque[float]] = defaultdict(deque)
        self._lock = threading.Lock()

    def verificar(self, cliente_id: str) -> tuple[bool, int]:
        """Retorna (permitido, segundos_para_tentar_novamente)."""
        if self.limite <= 0:
            return True, 0

        agora = time.monotonic()
        with self._lock:
            fila = self._historico[cliente_id]
            while fila and (agora - fila[0]) > self.janela:
                fila.popleft()

            if len(fila) >= self.limite:
                retry_after = max(1, int(self.janela - (agora - fila[0])))
                return False, retry_after

            fila.append(agora)
            return True, 0


_limitador = LimitadorTaxa(config.RATE_LIMIT_POR_MINUTO)


def _extrair_chave_request(request: Request) -> str | None:
    """Extrai a chave de API do header Authorization: Bearer, X-API-Key ou query ?api_key=."""
    auth = request.headers.get("authorization", "")
    if auth.lower().startswith("bearer "):
        return auth[7:].strip()
    x_key = request.headers.get("x-api-key")
    if x_key:
        return x_key.strip()
    q_key = request.query_params.get("api_key")
    if q_key:
        return q_key.strip()
    return None


def _chave_valida(chave_recebida: str | None) -> bool:
    """Valida a chave contra config.RAG_API_KEY em tempo constante."""
    if not config.RAG_API_KEY:
        return True
    if not chave_recebida:
        return False
    return secrets.compare_digest(chave_recebida, config.RAG_API_KEY)


def verificar_autenticacao(
    request: Request,
    bearer: HTTPAuthorizationCredentials | None = Security(_bearer_scheme),
    x_api_key: str | None = Security(_api_key_header),
) -> None:
    """Dependência FastAPI que exige API Key quando RAG_API_KEY está configurada."""
    chave = (bearer.credentials if bearer else None) or x_api_key or _extrair_chave_request(request)
    if not _chave_valida(chave):
        raise HTTPException(
            status_code=401,
            detail="Não autorizado. Envie Authorization: Bearer <RAG_API_KEY> ou X-API-Key.",
            headers={"WWW-Authenticate": "Bearer"},
        )


def obter_indice() -> IndiceBusca:
    if _indice is None:
        raise HTTPException(status_code=503, detail="Índice não carregado.")
    return _indice


# Pré-inicializa os sub-apps ASGI do FastMCP (Streamable HTTP em /mcp e SSE em /sse)
_mcp_http_app = mcp.streamable_http_app()
_mcp_sse_app = mcp.sse_app()


@asynccontextmanager
async def lifespan(app: FastAPI):
    global _indice
    iniciar_ollama_se_necessario()
    try:
        _indice = IndiceBusca()
        definir_indice(_indice)
    except IndiceNaoEncontrado as erro:
        logger.error("Falha ao carregar índice: %s", erro)

    async with AsyncExitStack() as stack:
        await stack.enter_async_context(mcp.session_manager.run())
        yield

    _indice = None
    definir_indice(None)


servidores_openapi = (
    [{"url": config.URL_PUBLICA_SERVIDOR, "description": "Servidor Principal"}]
    if config.URL_PUBLICA_SERVIDOR
    else None
)

app = FastAPI(
    title="RAG HighBond",
    version="0.2.0",
    description=(
        "Serviço de busca semântica (RAG) sobre a documentação oficial da API HighBond (Diligent). "
        "Exposto via REST (compatível com OpenAI Custom GPT Actions) e via MCP Remoto (/mcp e /sse)."
    ),
    lifespan=lifespan,
    openapi_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def middleware_seguranca_e_limites(request: Request, call_next):
    """Aplica Rate Limiting por usuário/IP, autenticação nas rotas MCP e cabeçalho de tempo."""
    inicio = time.perf_counter()
    caminho = request.url.path

    # Rotas de documentação e health check não exigem chave
    rota_publica = caminho in {"/health", "/docs", "/redoc", "/openapi.json"}

    # Verifica autenticação para endpoints MCP (/mcp, /sse, /messages) quando RAG_API_KEY estiver ativa
    if not rota_publica and config.RAG_API_KEY:
        chave = _extrair_chave_request(request)
        if not _chave_valida(chave):
            return JSONResponse(
                status_code=401,
                content={"detail": "Não autorizado. Informe Authorization: Bearer <RAG_API_KEY> ou X-API-Key."},
                headers={"WWW-Authenticate": "Bearer"},
            )

    # Rate limit por chave (se autenticada) ou IP do cliente (considerando proxy reverso)
    if caminho != "/health":
        ip_cliente = (
            request.headers.get("cf-connecting-ip")
            or request.headers.get("x-forwarded-for", "").split(",")[0].strip()
            or (request.client.host if request.client else "local")
        )
        identificador = _extrair_chave_request(request) or ip_cliente
        permitido, retry_after = _limitador.verificar(identificador)
        if not permitido:
            return JSONResponse(
                status_code=429,
                content={
                    "detail": (
                        f"Limite de requisições excedido ({config.RATE_LIMIT_POR_MINUTO}/min). "
                        f"Aguarde {retry_after}s."
                    )
                },
                headers={"Retry-After": str(retry_after)},
            )

    resposta = await call_next(request)
    duracao_ms = (time.perf_counter() - inicio) * 1000
    resposta.headers["X-Process-Time-Ms"] = f"{duracao_ms:.2f}"
    return resposta


class RequisicaoBusca(BaseModel):
    pergunta: str = Field(
        ...,
        min_length=1,
        max_length=500,
        description="Pergunta técnica em português ou inglês sobre a API HighBond",
    )
    quantidade: int = Field(5, ge=1, le=20, description="Quantidade máxima de chunks retornados (1 a 20)")
    similaridade_minima: float = Field(0.6, ge=0.0, le=1.0, description="Filtro de similaridade mínima (0.0 a 1.0)")


@app.get("/openapi.json", include_in_schema=False)
def openapi_dinamico(request: Request):
    """Gera o schema OpenAPI preenchendo automaticamente a URL pública do servidor (exigido pelo ChatGPT Actions)."""
    schema = app.openapi()
    if config.URL_PUBLICA_SERVIDOR:
        url_base = config.URL_PUBLICA_SERVIDOR
    else:
        proto = request.headers.get("x-forwarded-proto", request.url.scheme)
        host = request.headers.get("x-forwarded-host") or request.headers.get("host") or request.url.netloc
        url_base = f"{proto}://{host}"
    schema["servers"] = [{"url": url_base, "description": "Servidor RAG HighBond"}]
    return JSONResponse(schema)


@app.get("/health", operation_id="verificarSaude")
def health():
    """Status do serviço, do Ollama, cache de embeddings e limites."""
    return {
        "status": "ok",
        "ollama": ollama_rodando(),
        "modelo_embedding": config.MODELO_EMBEDDING,
        "indice_carregado": _indice is not None,
        "documentos": len(_indice.documentos) if _indice else 0,
        "autenticacao_ativa": bool(config.RAG_API_KEY),
        "rate_limit_por_minuto": config.RATE_LIMIT_POR_MINUTO,
        "max_concorrencia_ollama": config.MAX_REQUISICOES_SIMULTANEAS,
        "cache_embeddings": estatisticas_cache_embeddings(),
    }


@app.post(
    "/buscar",
    response_model=list[ResultadoBusca],
    dependencies=[Depends(verificar_autenticacao)],
    operation_id="buscarDocumentacaoHighbond",
    summary="Busca semântica na documentação da API HighBond",
)
def buscar(requisicao: RequisicaoBusca):
    """Retorna os chunks mais relevantes para a pergunta (em português ou inglês)."""
    indice = obter_indice()
    try:
        return indice.buscar(
            pergunta=requisicao.pergunta,
            quantidade=requisicao.quantidade,
            similaridade_minima=requisicao.similaridade_minima,
        )
    except OllamaIndisponivel as erro:
        raise HTTPException(status_code=503, detail=str(erro)) from erro


@app.get(
    "/chunks/{chunk_id}",
    dependencies=[Depends(verificar_autenticacao)],
    operation_id="obterChunkHighbond",
    summary="Obtém o conteúdo Markdown completo de um endpoint/chunk pelo ID",
)
def obter_chunk(chunk_id: str):
    """Retorna o conteúdo completo de um chunk pelo id retornado em /buscar."""
    indice = obter_indice()
    documento = indice.obter_chunk(chunk_id)
    if documento is None:
        raise HTTPException(status_code=404, detail=f"Chunk não encontrado: {chunk_id}")
    return {
        "id": documento.id,
        "title": documento.title,
        "tags": documento.tags,
        "source": documento.source,
        "arquivo": documento.arquivo,
        "conteudo": documento.conteudo,
    }


# Monta as rotas do MCP Remoto (/mcp para Streamable HTTP e /sse + /messages para SSE)
for rota in _mcp_http_app.routes:
    app.router.routes.append(rota)
for rota in _mcp_sse_app.routes:
    app.router.routes.append(rota)


def main():
    parser = argparse.ArgumentParser(description="API REST + MCP Remoto do RAG HighBond")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--porta", "--port", type=int, default=8000, dest="porta")
    args = parser.parse_args()

    uvicorn.run("rag_highbond.api:app", host=args.host, port=args.porta)


if __name__ == "__main__":
    main()
