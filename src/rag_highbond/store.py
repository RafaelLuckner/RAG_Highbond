"""Índice de busca semântica: carrega embeddings e executa a busca."""

import json
import logging
from pathlib import Path

import numpy as np

from . import config
from .loader import carregar_colecao
from .models import Documento, ResultadoBusca
from .ollama import gerar_embedding_pergunta

logger = logging.getLogger(__name__)


class IndiceNaoEncontrado(Exception):
    """Arquivo de índice (embeddings ou ids) não encontrado em disco."""


class IndiceBusca:
    """Mantém a matriz de embeddings e os documentos em memória.

    A busca usa produto escalar sobre vetores normalizados, o que equivale
    à similaridade do cosseno.
    """

    def __init__(
        self,
        pasta_chunks: Path = config.PASTA_CHUNKS,
        arquivo_embeddings: Path = config.ARQUIVO_EMBEDDINGS,
        colecao: str = config.COLECAO_PADRAO,
    ):
        if not arquivo_embeddings.exists():
            raise IndiceNaoEncontrado(
                f"Embeddings não encontrados: {arquivo_embeddings}. "
                "Gere o índice antes de usar a busca."
            )

        self.colecao = colecao
        self.matriz: np.ndarray = np.load(arquivo_embeddings)
        self.documentos: list[Documento] = carregar_colecao(pasta_chunks)
        self._por_id: dict[str, Documento] = {doc.id: doc for doc in self.documentos}

        if len(self.documentos) != self.matriz.shape[0]:
            raise IndiceNaoEncontrado(
                f"Dessincronia: {len(self.documentos)} chunks, mas a matriz tem "
                f"{self.matriz.shape[0]} vetores. Reindexe a coleção."
            )

        logger.info(
            "Índice '%s' carregado: %d documentos, vetores de %d dimensões.",
            colecao, len(self.documentos), self.matriz.shape[1],
        )

    def buscar(
        self,
        pergunta: str,
        quantidade: int = 5,
        similaridade_minima: float = 0.6,
    ) -> list[ResultadoBusca]:
        """Retorna os chunks mais relevantes para a pergunta."""
        vetor_pergunta = gerar_embedding_pergunta(pergunta)
        similaridades = self.matriz @ vetor_pergunta

        # Ordena, filtra pela similaridade mínima e limita à quantidade pedida.
        indices = np.argsort(similaridades)[::-1]
        indices = indices[similaridades[indices] >= similaridade_minima][:quantidade]

        return [
            ResultadoBusca(
                posicao=posicao,
                similaridade=round(float(similaridades[indice]), 4),
                id=self.documentos[indice].id,
                title=self.documentos[indice].title,
                trecho=self.documentos[indice].conteudo.replace("\n", " ")[:500],
                arquivo=self.documentos[indice].arquivo,
            )
            for posicao, indice in enumerate(indices, start=1)
        ]

    def obter_chunk(self, chunk_id: str) -> Documento | None:
        """Retorna o conteúdo completo de um chunk pelo id, ou None."""
        return self._por_id.get(chunk_id)
