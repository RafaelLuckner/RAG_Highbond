"""Cliente do Ollama: health check, auto-start e geração de embeddings."""

from functools import lru_cache
import logging
import subprocess
import sys
import threading
import time

import numpy as np
import requests

from . import config

logger = logging.getLogger(__name__)

# Semáforo para proteger o Ollama contra sobrecarga de requisições simultâneas em CPU
_semaforo_ollama = threading.BoundedSemaphore(max(1, config.MAX_REQUISICOES_SIMULTANEAS))
_sessao_http = requests.Session()


class OllamaIndisponivel(Exception):
    """O servidor Ollama não está acessível e não pôde ser iniciado."""


def ollama_rodando() -> bool:
    """Verifica se o provedor de embeddings está pronto (Ollama local ou API externa)."""
    if config.PROVEDOR_EMBEDDING != "ollama":
        return bool(config.EMBEDDING_API_KEY or config.EMBEDDING_API_URL)
    try:
        response = requests.get(config.URL_OLLAMA_TAGS, timeout=2)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def iniciar_ollama_se_necessario(timeout_segundos: int = 30) -> bool:
    """Garante que o Ollama está rodando; tenta iniciá-lo se necessário.

    Se PROVEDOR_EMBEDDING != 'ollama', não precisa iniciar processo local.
    """
    if config.PROVEDOR_EMBEDDING != "ollama":
        logger.info("Usando provedor de embedding externo (%s).", config.PROVEDOR_EMBEDDING)
        return True

    if ollama_rodando():
        logger.info("Ollama já está rodando.")
        return True

    logger.info("Ollama não está rodando. Iniciando...")

    try:
        kwargs = {"stdout": subprocess.DEVNULL, "stderr": subprocess.DEVNULL}
        if sys.platform == "win32":
            kwargs["creationflags"] = subprocess.CREATE_NO_WINDOW
        subprocess.Popen(["ollama", "serve"], **kwargs)
    except FileNotFoundError:
        logger.error("'ollama' não encontrado no PATH. Instale: https://ollama.com/download")
        return False

    for tentativa in range(timeout_segundos):
        if ollama_rodando():
            logger.info("Ollama iniciado com sucesso (tentativa %d).", tentativa + 1)
            return True
        time.sleep(1)

    logger.error("Timeout: Ollama não respondeu após %d segundos.", timeout_segundos)
    return False


def _requisitar_vetor_embedding(texto: str) -> list[float]:
    """Solicita o vetor de embedding ao Ollama local ou a uma API externa compatível."""
    headers = {"Content-Type": "application/json"}
    if config.EMBEDDING_API_KEY:
        headers["Authorization"] = f"Bearer {config.EMBEDDING_API_KEY}"

    if config.PROVEDOR_EMBEDDING in {"hf", "huggingface"}:
        response = _sessao_http.post(
            config.EMBEDDING_API_URL,
            headers=headers,
            json={"inputs": texto},
            timeout=config.TIMEOUT_OLLAMA,
        )
        response.raise_for_status()
        dados = response.json()
        return dados[0] if isinstance(dados[0], list) else dados

    if config.PROVEDOR_EMBEDDING in {"openai", "openai_compatible"}:
        response = _sessao_http.post(
            config.EMBEDDING_API_URL,
            headers=headers,
            json={"model": config.EMBEDDING_API_MODEL, "input": texto},
            timeout=config.TIMEOUT_OLLAMA,
        )
        response.raise_for_status()
        return response.json()["data"][0]["embedding"]

    # Padrão: Ollama (/api/embed)
    if not ollama_rodando():
        iniciar_ollama_se_necessario(timeout_segundos=15)

    response = _sessao_http.post(
        config.URL_OLLAMA,
        headers=headers,
        json={"model": config.MODELO_EMBEDDING, "input": texto},
        timeout=config.TIMEOUT_OLLAMA,
    )
    response.raise_for_status()
    return response.json()["embeddings"][0]


@lru_cache(maxsize=max(1, config.TAMANHO_CACHE_EMBEDDINGS))
def _gerar_embedding_pergunta_cached(pergunta_normalizada: str) -> np.ndarray:
    """Gera e mantém em cache LRU o embedding normalizado de uma pergunta."""
    texto = f"Instruct: {config.INSTRUCAO_BUSCA}\nQuery: {pergunta_normalizada}"

    adquirido = _semaforo_ollama.acquire(timeout=config.TIMEOUT_OLLAMA)
    if not adquirido:
        raise OllamaIndisponivel(
            "Servidor ocupado processando outras buscas. Tente novamente em instantes."
        )

    try:
        vetor_lista = _requisitar_vetor_embedding(texto)
    except requests.exceptions.Timeout as exc:
        raise OllamaIndisponivel(
            f"Tempo limite excedido ({config.TIMEOUT_OLLAMA}s) ao aguardar serviço de embeddings."
        ) from exc
    except requests.exceptions.RequestException as exc:
        raise OllamaIndisponivel(
            f"Não foi possível conectar ao serviço de embeddings ({config.PROVEDOR_EMBEDDING}). "
            "Verifique a configuração ou se o Ollama está rodando."
        ) from exc
    finally:
        _semaforo_ollama.release()

    vetor = np.asarray(vetor_lista, dtype=np.float32)
    vetor = vetor / np.linalg.norm(vetor)
    vetor.flags.writeable = False
    return vetor


def gerar_embedding_pergunta(pergunta: str) -> np.ndarray:
    """Gera o embedding normalizado de uma pergunta, com a instrução de busca.

    O formato "Instruct: ... Query: ..." é o esperado pelo modelo
    qwen3-embedding para tarefas de retrieval assimétrico.
    Utiliza cache LRU em memória para respostas instantâneas em buscas repetidas.
    """
    pergunta_normalizada = " ".join(pergunta.strip().split())
    return _gerar_embedding_pergunta_cached(pergunta_normalizada)


def estatisticas_cache_embeddings() -> dict:
    """Retorna métricas de uso do cache de embeddings."""
    info = _gerar_embedding_pergunta_cached.cache_info()
    return {
        "hits": info.hits,
        "misses": info.misses,
        "tamanho_atual": info.currsize,
        "tamanho_maximo": info.maxsize,
    }


def gerar_embeddings_documentos(textos: list[str], tamanho_lote: int = 4) -> np.ndarray:
    """Gera embeddings normalizados para uma lista de textos (reindexação)."""
    embeddings: list[list[float]] = []

    for inicio in range(0, len(textos), tamanho_lote):
        lote = textos[inicio:inicio + tamanho_lote]
        try:
            response = requests.post(
                config.URL_OLLAMA,
                json={"model": config.MODELO_EMBEDDING, "input": lote},
                timeout=config.TIMEOUT_OLLAMA,
            )
            response.raise_for_status()
        except requests.exceptions.ConnectionError as exc:
            raise OllamaIndisponivel(
                f"Não foi possível conectar ao Ollama em {config.URL_OLLAMA}."
            ) from exc

        embeddings.extend(response.json()["embeddings"])
        logger.info("Embeddings: %d/%d", min(inicio + tamanho_lote, len(textos)), len(textos))

    matriz = np.asarray(embeddings, dtype=np.float32)
    # Normaliza para usar produto escalar como similaridade do cosseno.
    matriz /= np.linalg.norm(matriz, axis=1, keepdims=True)
    return matriz
