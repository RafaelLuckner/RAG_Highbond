FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    OLLAMA_KEEP_ALIVE=24h \
    OLLAMA_NUM_PARALLEL=2 \
    RAG_PROJECT_ROOT=/app \
    HOST=0.0.0.0 \
    PORT=8080

WORKDIR /app

# 1. Instala o binário oficial do Ollama e remove os ~4 GB de drivers GPU (CUDA/ROCm)
# que não são usados em CPU no Cloud Run, reduzindo a imagem de ~4.5 GB para ~700 MB!
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    zstd \
    && curl -fsSL https://ollama.com/install.sh | sh \
    && rm -rf /usr/local/lib/ollama/cuda* /usr/local/lib/ollama/rocm* \
              /usr/lib/ollama/cuda* /usr/lib/ollama/rocm* \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 2. Baixa o modelo qwen3-embedding:0.6b durante o BUILD (fica em cache nas camadas do Docker)
RUN ollama serve & \
    SERVER_PID=$! && \
    sleep 3 && \
    ollama pull qwen3-embedding:0.6b && \
    kill $SERVER_PID

# 3. Copia a base de chunks e o índice de embeddings (.npy) pré-calculado
COPY rag_doc_api/indice ./rag_doc_api/indice
COPY rag_doc_api/raw_info/chunks ./rag_doc_api/raw_info/chunks

# 4. Instala dependências e o pacote Python
COPY pyproject.toml ./
COPY src ./src
RUN pip install --no-cache-dir -e .

EXPOSE 8080

# 5. Inicia diretamente o rag-api (que abre a porta $PORT imediatamente e sobe o Ollama em background)
CMD ["rag-api"]
