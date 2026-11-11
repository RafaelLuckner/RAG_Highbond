# RAG HighBond — API REST + Servidor MCP (Local e Cloud Run)

Serviço de busca semântica (RAG) sobre a documentação oficial da **API HighBond (Diligent)**, utilizando embeddings **`qwen3-embedding:0.6b`** (cross-lingual Português ↔ Inglês) com **FastAPI** e **FastMCP**.

Exposto simultaneamente em dois formatos no mesmo servidor:
- **API REST + OpenAPI (`/buscar`, `/chunks/{id}`, `/openapi.json`):** Compatível com **ChatGPT (Custom GPT Actions)**, scripts Python, n8n e automações HTTP.
- **Servidor MCP (`/mcp` via Streamable HTTP, `/sse` e `stdio`):** Compatível com **Antigravity**, **VS Code (GitHub Copilot)**, **Claude Desktop/Web**, **Cursor** e **ChatGPT Connectors**.

---

## Recursos de Produção Integrados

- **Autenticação por API Key (`RAG_API_KEY`):** Aceita `Authorization: Bearer <chave>`, cabeçalho `X-API-Key` ou `?api_key=`.
- **Rate Limiting por Usuário/IP (`RAG_RATE_LIMIT_PER_MIN`):** Janela deslizante (padrão: 30 req/min) com retorno `HTTP 429` e cabeçalho `Retry-After`.
- **Controle de Concorrência (`RAG_MAX_CONCURRENT`):** Semáforo para proteger o serviço de embeddings contra sobrecarga de CPU.
- **Cache LRU em Memória (`RAG_EMBEDDING_CACHE_SIZE`):** Buscas repetidas respondem em `< 1 ms` sem acionar o modelo novamente.
- **Métrica de Tempo (`X-Process-Time-Ms`):** Cabeçalho HTTP em todas as respostas informando a latência exata no servidor.

---

## 1. Como Rodar Localmente

### Pré-requisitos
1. Python 3.10+
2. [Ollama](https://ollama.com/download) instalado com o modelo:
   ```powershell
   ollama pull qwen3-embedding:0.6b
   ```

### Instalação e Execução
```powershell
pip install -e .[dev]

# Subir API REST + MCP HTTP em http://127.0.0.1:8000
rag-api

# Rodar testes automatizados
pytest -v
```

---

## 2. Como Configurar como MCP

### Modo Local (`stdio` — Antigravity / Claude Desktop / VS Code)
No arquivo `~/.gemini/config/mcp_config.json` (Antigravity) ou `.vscode/mcp.json`:
```json
{
  "mcpServers": {
    "rag-highbond": {
      "command": "C:\\caminho\\para\\.venv\\Scripts\\python.exe",
      "args": ["-m", "rag_highbond.mcp_server"]
    }
  }
}
```

### Modo Remoto (`Streamable HTTP` — Cloud Run / Servidor)
```json
{
  "mcpServers": {
    "rag-highbond-cloud": {
      "url": "https://SUA-URL-CLOUD-RUN.a.run.app/mcp",
      "headers": {
        "Authorization": "Bearer hb-rag-secreto-2026"
      }
    }
  }
}
```

---

## 3. Deploy no Google Cloud Run (Free Tier com Ollama Embutido)

No **Google Cloud Shell**, execute:

```bash
git clone https://github.com/RafaelLuckner/RAG_Highbond.git
cd RAG_Highbond

gcloud run deploy rag-highbond \
  --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --execution-environment gen2 \
  --cpu-boost \
  --memory 2Gi \
  --cpu 2 \
  --min-instances 0 \
  --max-instances 2 \
  --timeout 120 \
  --set-env-vars="RAG_API_KEY=hb-rag-secreto-2026,RAG_RATE_LIMIT_PER_MIN=30"
```

---

## 4. Conectando ao ChatGPT (Custom GPT Actions)

1. No ChatGPT, acesse **Explore GPTs ➔ Create ➔ Configure ➔ Create new action**.
2. Em **Authentication**, selecione **API Key (Bearer)** e informe o valor configurado em `RAG_API_KEY`.
3. Em **Schema ➔ Import from URL**, informe:
   ```text
   https://SUA-URL-CLOUD-RUN.a.run.app/openapi.json
   ```

