"""Carregamento de chunks Markdown com front matter YAML."""

import logging
from pathlib import Path

import yaml

from .models import Documento

logger = logging.getLogger(__name__)


class ErroCarregamento(Exception):
    """Falha ao carregar ou interpretar um chunk Markdown."""


def carregar_markdown(caminho: Path) -> Documento:
    """Carrega um arquivo .md com front matter YAML e retorna um Documento.

    Levanta ErroCarregamento se o front matter estiver ausente ou inválido.
    """
    texto = caminho.read_text(encoding="utf-8")

    if not texto.startswith("---"):
        raise ErroCarregamento(f"Front matter não encontrado: {caminho.name}")

    partes = texto.split("---", 2)

    if len(partes) < 3:
        raise ErroCarregamento(f"Front matter inválido: {caminho.name}")

    metadados = yaml.safe_load(partes[1]) or {}
    conteudo = partes[2].strip()

    return Documento(
        arquivo=caminho.name,
        id=metadados.get("id"),
        title=metadados.get("title"),
        tags=metadados.get("tags", []) or [],
        source=metadados.get("source"),
        conteudo=conteudo,
    )


def carregar_colecao(pasta_chunks: Path) -> list[Documento]:
    """Carrega todos os chunks .md de uma pasta, na ordem alfabética.

    A ordem é determinística para manter alinhamento com a matriz de
    embeddings salva (índice por posição). Arquivos com erro são ignorados
    com aviso no log.
    """
    arquivos = sorted(pasta_chunks.glob("*.md"))
    documentos: list[Documento] = []

    for caminho in arquivos:
        try:
            documentos.append(carregar_markdown(caminho))
        except ErroCarregamento as erro:
            logger.warning("Chunk ignorado: %s", erro)

    logger.info("Carregados %d chunks de %s", len(documentos), pasta_chunks)
    return documentos
