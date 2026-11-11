FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    OLLAMA_KEEP_ALIVE=24h \
    OLLAMA_NUM_PARALLEL=2 \
    PORT=8080

WORKDIR /app

# 1. Instala o binário oficial do Ollama dentro do container
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    zstd \
    && curl -fsSL https://ollama.com/install.sh | sh \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 2. Instala dependências e o pacote Python
COPY pyproject.toml ./
COPY src ./src
RUN pip install --no-cache-dir .

# 3. Copia a base de chunks e o índice de embeddings (.npy) pré-calculado
COPY rag_doc_api/indice ./rag_doc_api/indice
COPY rag_doc_api/raw_info/chunks ./rag_doc_api/raw_info/chunks

# 4. Baixa o modelo qwen3-embedding:0.6b durante o BUILD da imagem!
# Dessa forma, no Cloud Run o modelo já vem salvo no disco da imagem (sem baixar na hora da requisição).
RUN ollama serve & \
    SERVER_PID=$! && \
    sleep 3 && \
    ollama pull qwen3-embedding:0.6b && \
    kill $SERVER_PID

COPY entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

EXPOSE 8080

CMD ["./entrypoint.sh"]
