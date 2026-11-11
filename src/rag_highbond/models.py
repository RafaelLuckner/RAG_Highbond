"""Modelos de dados do domínio."""

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Documento:
    """Chunk de documentação carregado de um arquivo Markdown com front matter."""

    arquivo: str
    id: str
    title: str
    conteudo: str
    tags: list[str] = field(default_factory=list)
    source: str | None = None

    @property
    def caracteres(self) -> int:
        return len(self.conteudo)

    @property
    def palavras(self) -> int:
        return len(self.conteudo.split())

    @property
    def tokens_estimados(self) -> int:
        return round(len(self.conteudo) / 4)

    def texto_para_embedding(self) -> str:
        """Formato usado na geração dos embeddings (deve bater com o notebook)."""
        tags = ", ".join(self.tags)
        return (
            f"HighBond API documentation\n"
            f"Title: {self.title}\n"
            f"Tags: {tags}\n\n"
            f"{self.conteudo}"
        )


@dataclass
class ResultadoBusca:
    """Um resultado de busca semântica."""

    posicao: int
    similaridade: float
    id: str
    title: str
    trecho: str
    arquivo: str | None = None
