"""Servidor MCP (stdio, SSE e Streamable HTTP) para busca semântica na documentação HighBond.

Compatível com VS Code (GitHub Copilot), Claude Desktop/Web, ChatGPT e Antigravity.
Pode rodar como processo independente (stdio ou HTTP) ou montado dentro do FastAPI (api.py).

Uso:
    rag-mcp                        # modo stdio (padrão local)
    rag-mcp --transporte http      # modo Streamable HTTP em http://0.0.0.0:8000/mcp
    rag-mcp --transporte sse       # modo SSE em http://0.0.0.0:8000/sse
"""

import argparse
import logging

from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

from .ollama import iniciar_ollama_se_necessario
from .store import IndiceBusca

# Em servidores stdio, logs vão para stderr para não poluir o protocolo.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    handlers=[logging.StreamHandler(__import__("sys").stderr)],
)
logger = logging.getLogger(__name__)

mcp = FastMCP(
    "rag-highbond",
    instructions=(
        "Busca semântica na documentação oficial da API HighBond (Diligent). "
        "Use buscar_highbond para encontrar endpoints relevantes e "
        "obter_chunk para ler o conteúdo completo de um endpoint."
    ),
    stateless_http=True,
    transport_security=TransportSecuritySettings(enable_dns_rebinding_protection=False),
)

_indice: IndiceBusca | None = None


def definir_indice(indice: IndiceBusca | None) -> None:
    """Permite compartilhar a instância já carregada pelo FastAPI."""
    global _indice
    _indice = indice


def obter_indice() -> IndiceBusca:
    """Carrega o índice de forma preguiçosa (na primeira tool chamada)."""
    global _indice
    if _indice is None:
        iniciar_ollama_se_necessario()
        _indice = IndiceBusca()
    return _indice


@mcp.tool()
def buscar_highbond(
    pergunta: str,
    quantidade: int = 5,
    similaridade_minima: float = 0.6,
) -> list[dict]:
    """Busca os chunks de documentação da API HighBond mais relevantes
    para uma pergunta. A pergunta pode ser em português ou inglês.

    Retorna id, título, similaridade e um trecho de cada chunk.
    Use obter_chunk com o id para ler o conteúdo completo.
    """
    resultados = obter_indice().buscar(
        pergunta=pergunta,
        quantidade=quantidade,
        similaridade_minima=similaridade_minima,
    )
    return [
        {
            "posicao": r.posicao,
            "similaridade": r.similaridade,
            "id": r.id,
            "title": r.title,
            "trecho": r.trecho,
        }
        for r in resultados
    ]


@mcp.tool()
def obter_chunk(chunk_id: str) -> dict:
    """Retorna o conteúdo completo de um chunk de documentação pelo id
    (obtido previamente com buscar_highbond).
    """
    documento = obter_indice().obter_chunk(chunk_id)
    if documento is None:
        return {"erro": f"Chunk não encontrado: {chunk_id}"}
    return {
        "id": documento.id,
        "title": documento.title,
        "tags": documento.tags,
        "conteudo": documento.conteudo,
    }


def main():
    parser = argparse.ArgumentParser(description="Servidor MCP do RAG HighBond")
    parser.add_argument(
        "--transporte",
        choices=["stdio", "http", "sse"],
        default="stdio",
        help="Protocolo de transporte: stdio (local), http (Streamable HTTP) ou sse",
    )
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--porta", "--port", type=int, default=8000, dest="porta")
    args = parser.parse_args()

    mcp.settings.host = args.host
    mcp.settings.port = args.porta

    transporte_map = {
        "stdio": "stdio",
        "http": "streamable-http",
        "sse": "sse",
    }
    modo = transporte_map[args.transporte]
    logger.info("Iniciando servidor MCP rag-highbond (%s)...", modo)
    mcp.run(transport=modo)


if __name__ == "__main__":
    main()
