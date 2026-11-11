#!/bin/sh
set -e

echo "[STARTUP] Iniciando Ollama em background..."
ollama serve &
OLLAMA_PID=$!

echo "[STARTUP] Aguardando Ollama responder..."
for i in $(seq 1 30); do
    if curl -s http://127.0.0.1:11434/api/tags > /dev/null 2>&1; then
        echo "[STARTUP] Ollama pronto em ${i}s!"
        break
    fi
    sleep 1
done

PORT_NUM="${PORT:-8080}"
echo "[STARTUP] Iniciando rag-api na porta ${PORT_NUM}..."
exec rag-api --host 0.0.0.0 --porta "${PORT_NUM}"
