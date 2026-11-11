"""Gera uma apresentação editável do projeto RAG HighBond."""

import json
from collections import Counter
from pathlib import Path

import numpy as np
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Inches, Pt


ROOT = Path(__file__).resolve().parent
OPENAPI = ROOT / "rag_doc_api" / "openapi.json"
CHUNKS = ROOT / "rag_doc_api" / "raw_info" / "chunks"
EMBEDDINGS = ROOT / "rag_doc_api" / "indice" / "embeddings_qwen3_06b.npy"
OUTPUT = ROOT / "apresentacao_rag_highbond.pptx"

NAVY = RGBColor(20, 38, 63)
BLUE = RGBColor(0, 116, 217)
TEAL = RGBColor(0, 156, 166)
ORANGE = RGBColor(238, 123, 45)
INK = RGBColor(29, 39, 51)
MUTED = RGBColor(91, 105, 120)
PAPER = RGBColor(248, 250, 252)
WHITE = RGBColor(255, 255, 255)
LINE = RGBColor(217, 225, 233)


def add_text(slide, text, x, y, w, h, size=18, color=INK, bold=False,
             font="Aptos", align=PP_ALIGN.LEFT, valign=MSO_ANCHOR.TOP):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    frame = box.text_frame
    frame.clear()
    frame.word_wrap = True
    frame.vertical_anchor = valign
    paragraph = frame.paragraphs[0]
    paragraph.text = text
    paragraph.alignment = align
    paragraph.font.name = font
    paragraph.font.size = Pt(size)
    paragraph.font.bold = bold
    paragraph.font.color.rgb = color
    return box


def add_rect(slide, x, y, w, h, fill, radius=False, line=None):
    shape_type = MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE
    shape = slide.shapes.add_shape(shape_type, Inches(x), Inches(y), Inches(w), Inches(h))
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    shape.line.color.rgb = line or fill
    return shape


def add_header(slide, title, subtitle, number):
    add_text(slide, title, 0.72, 0.42, 9.8, 0.48, 26, NAVY, True, "Aptos Display")
    add_text(slide, subtitle, 0.74, 0.96, 10.7, 0.3, 10.5, MUTED)
    add_text(slide, f"{number:02d}", 12.0, 0.48, 0.6, 0.3, 11, TEAL, True, align=PP_ALIGN.RIGHT)
    add_rect(slide, 0.72, 1.34, 11.85, 0.015, LINE)


def add_footer(slide):
    add_text(slide, "RAG HighBond | documentação técnica com busca semântica", 0.72, 7.18, 7.0, 0.2, 8.5, MUTED)


def add_bullet_list(slide, items, x, y, w, size=16, color=INK, gap=0.13):
    current_y = y
    for item in items:
        add_text(slide, "•", x, current_y, 0.22, 0.28, size, TEAL, True)
        add_text(slide, item, x + 0.27, current_y, w - 0.27, 0.46, size, color)
        current_y += 0.46 + gap


def add_metric(slide, value, label, x, y, w, accent=TEAL):
    add_rect(slide, x, y, w, 1.25, WHITE, True, LINE)
    add_rect(slide, x, y, 0.08, 1.25, accent)
    add_text(slide, str(value), x + 0.25, y + 0.2, w - 0.4, 0.42, 25, NAVY, True, "Aptos Display")
    add_text(slide, label, x + 0.25, y + 0.76, w - 0.35, 0.28, 10.5, MUTED)


def add_step(slide, label, detail, x, color):
    add_rect(slide, x, 3.1, 1.75, 1.48, WHITE, True, LINE)
    add_rect(slide, x, 3.1, 1.75, 0.12, color, True)
    add_text(slide, label, x + 0.16, 3.42, 1.43, 0.3, 15, NAVY, True)
    add_text(slide, detail, x + 0.16, 3.86, 1.43, 0.42, 10.5, MUTED)


def build_presentation():
    specification = json.loads(OPENAPI.read_text(encoding="utf-8"))
    paths = specification["paths"]
    methods = ("get", "post", "put", "patch", "delete")
    operations = [method for path in paths.values() for method in path if method in methods]
    method_counts = Counter(operations)
    schemas = len(specification.get("components", {}).get("schemas", {}))
    security_schemes = len(specification.get("components", {}).get("securitySchemes", {}))
    total_chunks = len(list(CHUNKS.glob("*.md")))
    indexed_chunks = sum(
        chunk.read_text(encoding="utf-8").startswith("---")
        for chunk in CHUNKS.glob("*.md")
    )
    vector_count, vector_dimensions = np.load(EMBEDDINGS).shape
    size_mb = OPENAPI.stat().st_size / 1024 / 1024

    presentation = Presentation()
    presentation.slide_width = Inches(13.333)
    presentation.slide_height = Inches(7.5)
    blank = presentation.slide_layouts[6]

    slide = presentation.slides.add_slide(blank)
    add_rect(slide, 0, 0, 13.333, 7.5, NAVY)
    add_rect(slide, 0, 0, 0.22, 7.5, TEAL)
    add_rect(slide, 9.2, 0, 4.133, 7.5, RGBColor(17, 54, 84))
    add_text(slide, "RAG HighBond", 0.88, 1.28, 7.4, 0.85, 39, WHITE, True, "Aptos Display")
    add_text(slide, "Da especificação OpenAPI à consulta inteligente\nda documentação técnica", 0.9, 2.28, 7.2, 0.92, 22, RGBColor(215, 231, 244))
    add_text(slide, "Projeto de recuperação aumentada por geração (RAG)\npara a API HighBond / Diligent", 0.9, 3.52, 6.3, 0.6, 15, WHITE)
    add_rect(slide, 9.98, 1.42, 2.3, 2.3, TEAL, True)
    add_text(slide, "201\nroutes", 10.15, 1.88, 1.95, 0.9, 25, WHITE, True, "Aptos Display", PP_ALIGN.CENTER)
    add_rect(slide, 9.58, 4.38, 2.7, 1.0, ORANGE, True)
    add_text(slide, "369 chunks indexados", 9.8, 4.72, 2.25, 0.25, 13, WHITE, True, align=PP_ALIGN.CENTER)
    add_text(slide, "Setembro de 2026", 0.9, 6.72, 2.6, 0.25, 10, RGBColor(184, 207, 224))

    slide = presentation.slides.add_slide(blank)
    add_header(slide, "O desafio", "Tornar uma referência extensa consultável em linguagem natural", 2)
    add_text(slide, "Pergunta de partida", 0.75, 1.82, 3.2, 0.36, 15, TEAL, True)
    add_text(slide, "Como localizar rapidamente o endpoint certo em uma API ampla, sem percorrer manualmente o JSON?", 0.75, 2.25, 5.35, 1.0, 25, NAVY, True, "Aptos Display")
    add_rect(slide, 7.1, 1.76, 5.35, 3.86, PAPER, True, LINE)
    add_text(slide, "Critérios da solução", 7.48, 2.05, 3.7, 0.32, 16, NAVY, True)
    add_bullet_list(slide, [
        "Preservar a documentação técnica de origem.",
        "Aceitar perguntas em português ou inglês.",
        "Retornar contexto relevante, com rastreabilidade.",
        "Integrar com ferramentas de IA via MCP.",
    ], 7.47, 2.62, 4.45, 15)
    add_footer(slide)

    slide = presentation.slides.add_slide(blank)
    add_header(slide, "A documentação de origem", "A especificação inteira permanece disponível como fonte de verdade", 3)
    add_metric(slide, f"{len(paths)}", "caminhos (paths) OpenAPI", 0.75, 1.75, 2.65, TEAL)
    add_metric(slide, f"{len(operations)}", "operações HTTP documentadas", 3.68, 1.75, 2.65, BLUE)
    add_metric(slide, f"{len(specification.get('tags', []))}", "domínios / tags funcionais", 6.61, 1.75, 2.65, ORANGE)
    add_metric(slide, f"{schemas}", "schemas reutilizáveis", 9.54, 1.75, 2.65, TEAL)
    add_rect(slide, 0.75, 3.53, 11.44, 2.4, WHITE, True, LINE)
    add_text(slide, "openapi.json", 1.1, 3.91, 2.2, 0.33, 17, NAVY, True, "Aptos Display")
    add_text(slide, "OpenAPI 3.0.2 | HighBond API Reference v1.1.0 | JSON:API v1.0 | OAuth 2.0", 1.1, 4.42, 9.8, 0.28, 15, INK)
    add_text(slide, f"Arquivo de {size_mb:.1f} MB, mantido integralmente em rag_doc_api/openapi.json.", 1.1, 5.03, 9.8, 0.28, 13, MUTED)
    add_text(slide, f"{security_schemes} esquema de segurança declarado; servidores regionais configuráveis.", 1.1, 5.38, 9.8, 0.28, 13, MUTED)
    add_footer(slide)

    slide = presentation.slides.add_slide(blank)
    add_header(slide, "Cobertura da API", "Distribuição das operações presentes no JSON", 4)
    labels = [("GET", method_counts["get"], TEAL), ("POST", method_counts["post"], BLUE), ("PATCH", method_counts["patch"], ORANGE), ("PUT", method_counts["put"], RGBColor(103, 92, 168)), ("DELETE", method_counts["delete"], RGBColor(201, 74, 74))]
    max_count = max(count for _, count, _ in labels)
    for index, (label, count, color) in enumerate(labels):
        y = 1.85 + index * 0.78
        add_text(slide, label, 0.92, y + 0.07, 1.05, 0.27, 14, NAVY, True)
        add_rect(slide, 2.05, y, 7.4, 0.42, RGBColor(231, 236, 241), True)
        add_rect(slide, 2.05, y, 7.4 * count / max_count, 0.42, color, True)
        add_text(slide, str(count), 9.7, y + 0.04, 0.65, 0.28, 14, INK, True, align=PP_ALIGN.RIGHT)
    add_rect(slide, 10.75, 1.75, 1.43, 4.5, PAPER, True, LINE)
    add_text(slide, "A fonte inclui", 10.93, 2.05, 1.05, 0.5, 13, NAVY, True, align=PP_ALIGN.CENTER)
    add_text(slide, "paths\nparâmetros\ncorpos\nrespostas\nschemas", 10.93, 2.8, 1.05, 1.9, 13, MUTED, align=PP_ALIGN.CENTER)
    add_footer(slide)

    slide = presentation.slides.add_slide(blank)
    add_header(slide, "Processo executado", "Pipeline que converte a referência técnica em uma base semântica", 5)
    steps = [
        ("1. Extrair", "OpenAPI JSON", 0.75, TEAL),
        ("2. Estruturar", "Markdown + YAML", 3.15, BLUE),
        ("3. Vetorizar", "Ollama / Qwen3", 5.55, ORANGE),
        ("4. Indexar", "NumPy .npy", 7.95, RGBColor(103, 92, 168)),
        ("5. Consultar", "MCP e REST", 10.35, TEAL),
    ]
    for label, detail, x, color in steps:
        add_step(slide, label, detail, x, color)
    for x in (2.58, 4.98, 7.38, 9.78):
        add_text(slide, "→", x, 3.61, 0.34, 0.25, 18, MUTED, True, align=PP_ALIGN.CENTER)
    add_text(slide, "A ordem alfabética dos arquivos é preservada para manter cada chunk alinhado ao seu vetor no índice.", 1.05, 5.58, 11.0, 0.35, 14, NAVY, True, align=PP_ALIGN.CENTER)
    add_footer(slide)

    slide = presentation.slides.add_slide(blank)
    add_header(slide, "Como a documentação foi preparada", "Cada endpoint vira uma unidade de contexto rastreável", 6)
    add_rect(slide, 0.75, 1.75, 5.62, 4.62, RGBColor(30, 45, 59), True)
    code = "---\nid: get-orgs-org-id-controls\ntitle: Get controls\ntags: [Controls]\nsource: openapi.json\n---\n\nGET /orgs/{org_id}/controls\n..."
    add_text(slide, code, 1.15, 2.18, 4.75, 3.55, 15, RGBColor(220, 233, 242), False, "Consolas")
    add_text(slide, "Chunk Markdown", 1.15, 5.78, 2.0, 0.25, 11, RGBColor(139, 211, 215), True)
    add_metric(slide, str(total_chunks), "arquivos Markdown gerados", 7.05, 1.88, 4.5, BLUE)
    add_metric(slide, str(indexed_chunks), "chunks válidos com front matter", 7.05, 3.33, 4.5, TEAL)
    add_text(slide, "Campos preservados", 7.07, 5.05, 3.2, 0.28, 15, NAVY, True)
    add_bullet_list(slide, ["id e título", "tags", "origem", "conteúdo do endpoint"], 7.05, 5.43, 4.1, 13.5)
    add_footer(slide)

    slide = presentation.slides.add_slide(blank)
    add_header(slide, "Índice semântico", "Embeddings permitem buscar significado, não somente palavras idênticas", 7)
    add_metric(slide, str(vector_count), "vetores armazenados", 0.75, 1.78, 3.2, TEAL)
    add_metric(slide, str(vector_dimensions), "dimensões por vetor", 4.3, 1.78, 3.2, BLUE)
    add_metric(slide, "0,60", "similaridade mínima padrão", 7.85, 1.78, 3.2, ORANGE)
    add_rect(slide, 0.75, 3.5, 11.43, 1.7, PAPER, True, LINE)
    add_text(slide, "Pergunta em português ou inglês", 1.05, 3.87, 2.55, 0.28, 14, NAVY, True)
    add_text(slide, "→", 3.67, 3.87, 0.38, 0.28, 18, TEAL, True, align=PP_ALIGN.CENTER)
    add_text(slide, "embedding da pergunta", 4.15, 3.87, 2.15, 0.28, 14, NAVY, True)
    add_text(slide, "→", 6.45, 3.87, 0.38, 0.28, 18, TEAL, True, align=PP_ALIGN.CENTER)
    add_text(slide, "produto escalar", 7.0, 3.87, 1.75, 0.28, 14, NAVY, True)
    add_text(slide, "→", 8.86, 3.87, 0.38, 0.28, 18, TEAL, True, align=PP_ALIGN.CENTER)
    add_text(slide, "top-k relevantes", 9.45, 3.87, 1.92, 0.28, 14, NAVY, True)
    add_text(slide, "Os vetores normalizados tornam o produto escalar equivalente à similaridade do cosseno.", 1.05, 5.72, 10.75, 0.3, 14, MUTED, align=PP_ALIGN.CENTER)
    add_footer(slide)

    slide = presentation.slides.add_slide(blank)
    add_header(slide, "Resultado final", "Uma interface de consulta para assistentes e aplicações locais", 8)
    add_rect(slide, 0.75, 1.75, 5.45, 4.65, PAPER, True, LINE)
    add_text(slide, "MCP: rag-highbond", 1.12, 2.12, 3.6, 0.32, 18, NAVY, True, "Aptos Display")
    add_text(slide, "Ferramentas expostas ao Copilot", 1.12, 2.63, 3.6, 0.27, 12, MUTED)
    add_text(slide, "buscar_highbond", 1.12, 3.27, 3.6, 0.3, 16, TEAL, True, "Consolas")
    add_text(slide, "Localiza endpoints relevantes", 1.12, 3.66, 3.6, 0.28, 13, INK)
    add_text(slide, "obter_chunk", 1.12, 4.45, 3.6, 0.3, 16, TEAL, True, "Consolas")
    add_text(slide, "Recupera a documentação completa", 1.12, 4.84, 3.6, 0.28, 13, INK)
    add_rect(slide, 6.72, 1.75, 5.46, 4.65, WHITE, True, LINE)
    add_text(slide, "API REST local", 7.1, 2.12, 3.4, 0.32, 18, NAVY, True, "Aptos Display")
    add_text(slide, "FastAPI em http://localhost:8000", 7.1, 2.63, 3.8, 0.27, 12, MUTED)
    add_text(slide, "POST /buscar", 7.1, 3.27, 3.5, 0.3, 16, BLUE, True, "Consolas")
    add_text(slide, "Retorna ranking, score e trecho", 7.1, 3.66, 3.7, 0.28, 13, INK)
    add_text(slide, "GET /chunks/{chunk_id}", 7.1, 4.45, 4.3, 0.3, 16, BLUE, True, "Consolas")
    add_text(slide, "Retorna o contexto completo", 7.1, 4.84, 3.7, 0.28, 13, INK)
    add_footer(slide)

    slide = presentation.slides.add_slide(blank)
    add_header(slide, "Experiência de consulta", "Fluxo final para responder perguntas sobre a API", 9)
    flow = [
        ("Pergunta", "Como criar um controle?"),
        ("Busca", "buscar_highbond"),
        ("Ranking", "top-k por similaridade"),
        ("Contexto", "obter_chunk"),
        ("Resposta", "com endpoint e detalhes"),
    ]
    for index, (label, detail) in enumerate(flow):
        x = 0.7 + index * 2.5
        color = [TEAL, BLUE, ORANGE, RGBColor(103, 92, 168), TEAL][index]
        add_rect(slide, x, 2.35, 2.02, 1.65, WHITE, True, LINE)
        add_rect(slide, x, 2.35, 2.02, 0.12, color, True)
        add_text(slide, label, x + 0.2, 2.72, 1.62, 0.27, 14, NAVY, True, align=PP_ALIGN.CENTER)
        add_text(slide, detail, x + 0.2, 3.18, 1.62, 0.36, 11, MUTED, align=PP_ALIGN.CENTER)
        if index < 4:
            add_text(slide, "→", x + 2.06, 2.92, 0.32, 0.3, 18, MUTED, True, align=PP_ALIGN.CENTER)
    add_text(slide, "A resposta final pode citar a operação encontrada e, quando necessário, recuperar o conteúdo integral do chunk correspondente.", 1.0, 5.16, 11.2, 0.55, 16, NAVY, True, align=PP_ALIGN.CENTER)
    add_footer(slide)

    slide = presentation.slides.add_slide(blank)
    add_header(slide, "Entregáveis e próximos passos", "Resultado: uma base local, rastreável e pronta para assistência contextual", 10)
    add_rect(slide, 0.75, 1.73, 5.55, 4.85, PAPER, True, LINE)
    add_text(slide, "Entregáveis", 1.1, 2.1, 2.3, 0.32, 18, NAVY, True, "Aptos Display")
    add_bullet_list(slide, [
        "Fonte OpenAPI integral preservada.",
        "369 chunks com metadados estruturados.",
        "Índice vetorial local em NumPy.",
        "Servidor MCP para Copilot e Claude Desktop.",
        "API REST local para integrações.",
    ], 1.08, 2.72, 4.75, 14)
    add_rect(slide, 6.7, 1.73, 5.48, 4.85, WHITE, True, LINE)
    add_text(slide, "Evoluções possíveis", 7.05, 2.1, 3.2, 0.32, 18, NAVY, True, "Aptos Display")
    add_bullet_list(slide, [
        "Avaliar relevância com perguntas reais.",
        "Adicionar filtros por tag e método HTTP.",
        "Atualizar o índice ao receber nova versão do OpenAPI.",
        "Registrar consultas e feedback dos usuários.",
    ], 7.03, 2.72, 4.7, 14)
    add_text(slide, "Obrigado", 0.75, 6.86, 2.2, 0.3, 15, TEAL, True, "Aptos Display")

    presentation.save(OUTPUT)
    return OUTPUT


if __name__ == "__main__":
    print(build_presentation())