import numpy as np
from fastapi.testclient import TestClient

from rag_highbond import api, config, loader, ollama, store
from rag_highbond.models import Documento


def _criar_indice_fake(tmp_path):
    """Cria um índice mínimo temporário para testar store, API e MCP sem precisar do Ollama."""
    pasta_chunks = tmp_path / "chunks"
    pasta_chunks.mkdir()

    chunk_md = (
        "---\n"
        'id: "get-projects"\n'
        'title: "Listar projetos HighBond"\n'
        "tags:\n"
        "  - projects\n"
        'source: "https://docs.highbond.com"\n'
        "---\n"
        "Endpoint GET /orgs/{org_id}/projects para listar projetos."
    )
    (pasta_chunks / "01_projects.md").write_text(chunk_md, encoding="utf-8")

    vetor = np.ones((1, 8), dtype=np.float32)
    vetor /= np.linalg.norm(vetor, axis=1, keepdims=True)
    arq_emb = tmp_path / "embeddings.npy"
    np.save(arq_emb, vetor)

    return store.IndiceBusca(pasta_chunks=pasta_chunks, arquivo_embeddings=arq_emb)


def test_carregar_markdown_e_busca_o1(tmp_path, monkeypatch):
    indice = _criar_indice_fake(tmp_path)
    monkeypatch.setattr(
        store,
        "gerar_embedding_pergunta",
        lambda p: np.ones(8, dtype=np.float32) / np.sqrt(8),
    )

    resultados = indice.buscar("como listar projetos?", quantidade=3, similaridade_minima=0.5)
    assert len(resultados) == 1
    assert resultados[0].id == "get-projects"

    doc = indice.obter_chunk("get-projects")
    assert doc is not None
    assert doc.title == "Listar projetos HighBond"
    assert indice.obter_chunk("nao-existe") is None


def test_api_autenticacao_e_rate_limit(tmp_path, monkeypatch):
    indice = _criar_indice_fake(tmp_path)
    monkeypatch.setattr(
        store,
        "gerar_embedding_pergunta",
        lambda p: np.ones(8, dtype=np.float32) / np.sqrt(8),
    )
    monkeypatch.setattr(api, "_indice", indice)
    monkeypatch.setattr(config, "RAG_API_KEY", "chave-secreta-teste")
    monkeypatch.setattr(api, "_limitador", api.LimitadorTaxa(limite_por_minuto=2))

    client = TestClient(api.app, raise_server_exceptions=False)

    # 1. /health continua público
    r_health = client.get("/health")
    assert r_health.status_code == 200
    assert r_health.json()["autenticacao_ativa"] is True

    # 2. Sem chave -> 401 tanto no REST quanto no MCP
    assert client.post("/buscar", json={"pergunta": "projetos"}).status_code == 401
    assert client.post("/mcp", json={}).status_code == 401

    # 3. Com chave Bearer -> 200 OK e retorna resultado
    headers = {"Authorization": "Bearer chave-secreta-teste"}
    r_ok1 = client.post("/buscar", json={"pergunta": "projetos"}, headers=headers)
    assert r_ok1.status_code == 200
    assert r_ok1.json()[0]["id"] == "get-projects"
    assert "X-Process-Time-Ms" in r_ok1.headers

    # 4. Segunda chamada dentro do limite (2/min) -> 200 OK
    r_ok2 = client.get("/chunks/get-projects", headers={"X-API-Key": "chave-secreta-teste"})
    assert r_ok2.status_code == 200
    assert r_ok2.json()["id"] == "get-projects"

    # 5. Terceira chamada estoura o limite de 2/min -> 429 Too Many Requests
    r_429 = client.get("/chunks/get-projects", headers=headers)
    assert r_429.status_code == 429
    assert "Retry-After" in r_429.headers

