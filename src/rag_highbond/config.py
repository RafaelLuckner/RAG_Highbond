"""Configuração central do pacote.

Caminhos são resolvidos a partir da raiz do projeto (local deste arquivo),
nunca do diretório de trabalho corrente. Valores de conexão podem ser
sobrescritos por variáveis de ambiente:

- OLLAMA_URL: URL da API de embeddings do Ollama
- EMBEDDING_MODEL: modelo de embedding a utilizar
"""

import os
from pathlib import Path

# src/rag_highbond/config.py -> raiz do projeto está 3 níveis acima
RAIZ_PROJETO = Path(__file__).resolve().parents[2]

PASTA_RAG_API = RAIZ_PROJETO / "rag_doc_api"
PASTA_CHUNKS = PASTA_RAG_API / "raw_info" / "chunks"
PASTA_INDICE = PASTA_RAG_API / "indice"
ARQUIVO_EMBEDDINGS = PASTA_INDICE / "embeddings_qwen3_06b.npy"
ARQUIVO_IDS = PASTA_INDICE / "documentos_ids.json"

URL_OLLAMA = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/embed")
URL_OLLAMA_TAGS = os.environ.get("OLLAMA_TAGS_URL", "http://localhost:11434/api/tags")
MODELO_EMBEDDING = os.environ.get("EMBEDDING_MODEL", "qwen3-embedding:0.6b")

# Provedor de embedding opcional para nuvem leve (Render/Koyeb 512MB sem Ollama local):
# Opções de EMBEDDING_PROVIDER: "ollama" (padrão) ou "openai_compatible" (ex: HuggingFace/DeepInfra/OpenRouter rodando Qwen3-Embedding-0.6B)
PROVEDOR_EMBEDDING = os.environ.get("EMBEDDING_PROVIDER", "ollama").strip().lower()
EMBEDDING_API_URL = os.environ.get(
    "EMBEDDING_API_URL",
    "https://router.huggingface.co/hf-inference/models/Qwen/Qwen3-Embedding-0.6B/pipeline/feature-extraction",
).strip()
EMBEDDING_API_KEY = os.environ.get("EMBEDDING_API_KEY", "").strip()
EMBEDDING_API_MODEL = os.environ.get("EMBEDDING_API_MODEL", "Qwen/Qwen3-Embedding-0.6B").strip()

# Timeout de requisição ao Ollama (segundos). Padrão reduzido para evitar travar workers HTTP.
TIMEOUT_OLLAMA = float(os.environ.get("OLLAMA_TIMEOUT", "15"))

# Segurança e Limites (Rate Limiting / Concorrência / Cache)
# Se RAG_API_KEY estiver vazia, a API aceita requisições sem chave (útil em dev local).
RAG_API_KEY = os.environ.get("RAG_API_KEY", "").strip()
RATE_LIMIT_POR_MINUTO = int(os.environ.get("RAG_RATE_LIMIT_PER_MIN", "30"))
MAX_REQUISICOES_SIMULTANEAS = int(os.environ.get("RAG_MAX_CONCURRENT", "4"))
TAMANHO_CACHE_EMBEDDINGS = int(os.environ.get("RAG_EMBEDDING_CACHE_SIZE", "256"))
URL_PUBLICA_SERVIDOR = os.environ.get("RAG_PUBLIC_URL", "").strip()

INSTRUCAO_BUSCA = (
    "Retrieve the most relevant HighBond API documentation for the question. "
    "The question may be in Portuguese or English and the documentation is in English."
)

# Preparado para futuras coleções (ex.: Diligent Robots)
COLECAO_PADRAO = "highbond"
