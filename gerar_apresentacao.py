"""Gera uma apresentação moderna e editável focada no RAG HighBond, documentação e resultados nos LLMs."""

from collections import Counter
import json
from pathlib import Path

import numpy as np
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt


ROOT = Path(__file__).resolve().parent
OPENAPI = ROOT / "rag_doc_api" / "openapi.json"
CHUNKS = ROOT / "rag_doc_api" / "raw_info" / "chunks"
EMBEDDINGS = ROOT / "rag_doc_api" / "indice" / "embeddings_qwen3_06b.npy"
OUTPUT = ROOT / "apresentacao_rag_highbond.pptx"

# Caso salve os prints com estes nomes, o script insere automaticamente nos slides 8, 9 e 10:
PRINT_GPT = [ROOT / "docs" / "print_gpt.png", ROOT / "print_gpt.png"]
PRINT_GEMINI = [ROOT / "docs" / "print_gemini.png", ROOT / "print_gemini.png"]
PRINT_COLAB = [
    ROOT / "docs" / "print_colab.png",
    ROOT / "print_colab.png",
    ROOT / "docs" / "print_api.png",
    ROOT / "print_api.png",
]

# Paleta Moderna e Intuitiva
NAVY = RGBColor(20, 38, 63)
DARK_SLATE = RGBColor(28, 49, 78)
CARD_DARK = RGBColor(30, 45, 59)
BLUE = RGBColor(0, 116, 217)
TEAL = RGBColor(0, 156, 166)
ORANGE = RGBColor(238, 123, 45)
PURPLE = RGBColor(103, 92, 168)
GREEN = RGBColor(16, 163, 127)
INK = RGBColor(29, 39, 51)
MUTED = RGBColor(91, 105, 120)
PAPER = RGBColor(248, 250, 252)
SOFT_BG = RGBColor(239, 244, 249)
WHITE = RGBColor(255, 255, 255)
LINE = RGBColor(217, 225, 233)


def add_text(
    slide,
    text,
    x,
    y,
    w,
    h,
    size=18,
    color=INK,
    bold=False,
    font="Aptos",
    align=PP_ALIGN.LEFT,
    valign=MSO_ANCHOR.TOP,
):
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


def add_rect(slide, x, y, w, h, fill, radius=False, line=None, line_width=1.0):
    shape_type = MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE
    shape = slide.shapes.add_shape(shape_type, Inches(x), Inches(y), Inches(w), Inches(h))
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    shape.line.color.rgb = line or fill
    shape.line.width = Pt(line_width)
    return shape


def add_badge(slide, text, x, y, w, h=0.32, bg=TEAL, fg=WHITE, size=10):
    add_rect(slide, x, y, w, h, bg, radius=True)
    add_text(slide, text, x, y + 0.03, w, h - 0.03, size, fg, True, align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE)


def add_header(slide, title, subtitle, number, total=11):
    add_rect(slide, 0, 0, 13.333, 7.5, PAPER)
    add_rect(slide, 0, 0, 13.333, 0.07, TEAL)
    add_text(slide, title, 0.72, 0.38, 10.4, 0.48, 25, NAVY, True, "Aptos Display")
    add_text(slide, subtitle, 0.74, 0.88, 10.8, 0.3, 11, MUTED)
    add_badge(slide, f"{number:02d} / {total:02d}", 11.78, 0.44, 0.85, 0.3, DARK_SLATE, WHITE, 9.5)
    add_rect(slide, 0.72, 1.28, 11.9, 0.015, LINE)


def add_footer(slide):
    add_rect(slide, 0.72, 7.08, 11.9, 0.01, LINE)
    add_text(slide, "RAG HighBond | Documentação técnica com busca semântica para LLMs", 0.72, 7.14, 8.5, 0.2, 8.5, MUTED)
    add_text(slide, "Rafael Luckner", 11.0, 7.14, 1.6, 0.2, 8.5, NAVY, True, align=PP_ALIGN.RIGHT)


def add_bullet_list(slide, items, x, y, w, size=14.5, color=INK, gap=0.12, bullet_color=TEAL, row_h=0.42):
    current_y = y
    for item in items:
        add_text(slide, "•", x, current_y, 0.22, 0.28, size, bullet_color, True)
        add_text(slide, item, x + 0.26, current_y, w - 0.26, row_h, size, color)
        current_y += row_h + gap


def add_metric(slide, value, label, x, y, w, accent=TEAL):
    add_rect(slide, x, y, w, 1.25, WHITE, True, LINE)
    add_rect(slide, x, y, 0.08, 1.25, accent)
    add_text(slide, str(value), x + 0.25, y + 0.18, w - 0.4, 0.42, 25, NAVY, True, "Aptos Display")
    add_text(slide, label, x + 0.25, y + 0.74, w - 0.35, 0.32, 10.5, MUTED)


def add_step(slide, label, detail, x, color):
    add_rect(slide, x, 2.55, 1.9, 1.55, WHITE, True, LINE)
    add_rect(slide, x, 2.55, 1.9, 0.12, color, True)
    add_text(slide, label, x + 0.16, 2.88, 1.58, 0.32, 15, NAVY, True)
    add_text(slide, detail, x + 0.16, 3.32, 1.58, 0.55, 10.5, MUTED)


def add_screenshot_box(slide, x, y, w, h, window_title, placeholder_label, hint_text, candidate_paths, accent=TEAL):
    """Cria uma moldura visual limpa para colar o print (ou carrega a imagem se existir)."""
    add_rect(slide, x, y, w, h, WHITE, True, LINE, line_width=1.2)
    add_rect(slide, x, y, w, 0.38, DARK_SLATE, True)
    add_rect(slide, x + 0.16, y + 0.13, 0.11, 0.11, RGBColor(239, 68, 68), True)
    add_rect(slide, x + 0.32, y + 0.13, 0.11, 0.11, RGBColor(245, 158, 11), True)
    add_rect(slide, x + 0.48, y + 0.13, 0.11, 0.11, RGBColor(16, 185, 129), True)
    add_text(slide, window_title, x + 0.72, y + 0.08, w - 0.85, 0.22, 10, WHITE, True, "Consolas")

    img_path = next((p for p in candidate_paths if p.exists()), None)
    ix, iy, iw, ih = x + 0.12, y + 0.48, w - 0.24, h - 0.6

    if img_path is not None:
        slide.shapes.add_picture(str(img_path), Inches(ix), Inches(iy), width=Inches(iw))
    else:
        add_rect(slide, ix, iy, iw, ih, SOFT_BG, True, accent, line_width=1.2)
        add_badge(slide, placeholder_label, ix + iw / 2 - 1.35, iy + ih / 2 - 0.52, 2.7, 0.34, accent, WHITE, 9.5)
        add_text(slide, hint_text, ix + 0.25, iy + ih / 2 - 0.05, iw - 0.5, 0.75, 11, MUTED, align=PP_ALIGN.CENTER)


def add_mini_table(slide, headers, rows, x, y, col_widths, accent=TEAL, row_h=0.29, font_size=9.5):
    """Desenha uma tabela compacta e moderna para mostrar os resultados do RAG."""
    total_w = sum(col_widths)
    add_rect(slide, x, y, total_w, row_h, accent, radius=False)
    curr_x = x
    for h_text, cw in zip(headers, col_widths):
        add_text(slide, h_text, curr_x + 0.06, y + 0.04, cw - 0.12, row_h - 0.04, font_size, WHITE, True)
        curr_x += cw

    curr_y = y + row_h
    for r_idx, row in enumerate(rows):
        bg = WHITE if r_idx % 2 == 0 else SOFT_BG
        add_rect(slide, x, curr_y, total_w, row_h, bg, line=LINE, line_width=0.5)
        curr_x = x
        for c_idx, (cell_text, cw) in enumerate(zip(row, col_widths)):
            is_code = c_idx in (1, 2)
            font_name = "Consolas" if is_code else "Aptos"
            color = TEAL if c_idx == 1 else INK
            bold = c_idx in (0, 1)
            add_text(slide, str(cell_text), curr_x + 0.06, curr_y + 0.04, cw - 0.1, row_h - 0.04, font_size - 0.5, color, bold, font_name)
            curr_x += cw
        curr_y += row_h


def _carregar_metricas():
    total_chunks = len(list(CHUNKS.glob("*.md")))
    indexed_chunks = sum(
        chunk.read_text(encoding="utf-8").startswith("---")
        for chunk in CHUNKS.glob("*.md")
    )
    vector_count, vector_dimensions = np.load(EMBEDDINGS).shape

    if OPENAPI.exists():
        specification = json.loads(OPENAPI.read_text(encoding="utf-8"))
        paths = specification["paths"]
        methods = ("get", "post", "put", "patch", "delete")
        operations = [method for path in paths.values() for method in path if method in methods]
        method_counts = Counter(operations)
        num_paths = len(paths)
        num_ops = len(operations)
        num_tags = len(specification.get("tags", []))
        schemas = len(specification.get("components", {}).get("schemas", {}))
        security_schemes = len(specification.get("components", {}).get("securitySchemes", {}))
        size_mb = OPENAPI.stat().st_size / 1024 / 1024
    else:
        num_paths = 201
        num_ops = 369
        num_tags = 55
        schemas = 290
        security_schemes = 1
        size_mb = 3.2
        method_counts = Counter({"get": 162, "post": 85, "patch": 54, "delete": 52, "put": 16})

    return {
        "total_chunks": total_chunks,
        "indexed_chunks": indexed_chunks,
        "vector_count": vector_count,
        "vector_dimensions": vector_dimensions,
        "num_paths": num_paths,
        "num_ops": num_ops,
        "num_tags": num_tags,
        "schemas": schemas,
        "security_schemes": security_schemes,
        "size_mb": size_mb,
        "method_counts": method_counts,
    }


def build_presentation(output_path: Path = OUTPUT):
    m = _carregar_metricas()
    total_slides = 11

    presentation = Presentation()
    presentation.slide_width = Inches(13.333)
    presentation.slide_height = Inches(7.5)
    blank = presentation.slide_layouts[6]

    # =========================================================================
    # SLIDE 1 — CAPA
    # =========================================================================
    slide = presentation.slides.add_slide(blank)
    add_rect(slide, 0, 0, 13.333, 7.5, NAVY)
    add_rect(slide, 0, 0, 0.22, 7.5, TEAL)
    add_rect(slide, 9.0, 0, 4.333, 7.5, RGBColor(17, 54, 84))

    add_badge(slide, "CONTEXTO PARA LLMs  •  BUSCA SEMÂNTICA  •  MCP", 0.88, 1.0, 4.2, 0.34, TEAL, WHITE, 10)
    add_text(slide, "RAG HighBond", 0.88, 1.52, 7.4, 0.85, 42, WHITE, True, "Aptos Display")
    add_text(
        slide,
        "Da especificação OpenAPI à consulta inteligente\nda documentação técnica com LLMs",
        0.9,
        2.48,
        7.4,
        0.95,
        22,
        RGBColor(215, 231, 244),
    )
    add_text(
        slide,
        "Recuperação Aumentada por Geração (RAG) aplicada à API HighBond / Diligent,\nintegrada ao ChatGPT, Gemini e Google Colab.",
        0.9,
        3.72,
        7.1,
        0.7,
        14.5,
        RGBColor(184, 207, 224),
    )

    add_rect(slide, 9.75, 1.35, 2.8, 1.5, TEAL, True)
    add_text(slide, f"{m['num_paths']}\nrotas OpenAPI", 9.9, 1.58, 2.5, 0.95, 24, WHITE, True, "Aptos Display", PP_ALIGN.CENTER)

    add_rect(slide, 9.75, 3.15, 2.8, 1.35, BLUE, True)
    add_text(slide, f"{m['indexed_chunks']} chunks\nindexados", 9.9, 3.38, 2.5, 0.85, 20, WHITE, True, "Aptos Display", PP_ALIGN.CENTER)

    add_rect(slide, 9.75, 4.78, 2.8, 1.15, ORANGE, True)
    add_text(slide, "ChatGPT • Gemini • Colab", 9.85, 5.18, 2.6, 0.35, 13, WHITE, True, align=PP_ALIGN.CENTER)

    add_text(slide, "Rafael Luckner  •  2026", 0.9, 6.72, 3.5, 0.25, 11, RGBColor(184, 207, 224), True)

    # =========================================================================
    # SLIDE 2 — O DESAFIO
    # =========================================================================
    slide = presentation.slides.add_slide(blank)
    add_header(slide, "O desafio", "Tornar uma referência extensa de API consultável em linguagem natural pelos LLMs", 2, total_slides)
    add_text(slide, "Pergunta de partida", 0.75, 1.75, 3.2, 0.36, 15, TEAL, True)
    add_text(
        slide,
        "Como localizar rapidamente os endpoints, payloads e gatilhos certos em uma API ampla, sem percorrer manualmente o JSON?",
        0.75,
        2.18,
        5.5,
        1.4,
        24,
        NAVY,
        True,
        "Aptos Display",
    )
    add_text(
        slide,
        "Enviar o arquivo OpenAPI inteiro no prompt estoura o limite de tokens e reduz a precisão do modelo. O RAG entrega apenas os trechos relevantes para a pergunta.",
        0.75,
        3.95,
        5.4,
        1.1,
        14,
        MUTED,
    )

    add_rect(slide, 6.75, 1.72, 5.85, 4.85, WHITE, True, LINE)
    add_rect(slide, 6.75, 1.72, 5.85, 0.1, TEAL, True)
    add_text(slide, "Critérios da solução", 7.15, 2.08, 4.5, 0.35, 18, NAVY, True, "Aptos Display")
    add_bullet_list(
        slide,
        [
            "Preservar 100% da fidelidade técnica da documentação de origem (OpenAPI).",
            "Aceitar perguntas em português e buscar na documentação em inglês (Cross-Lingual).",
            "Recuperar tanto a visão geral (ranking de endpoints) quanto o schema completo.",
            "Expor a base como ferramenta (MCP / API) para uso direto no ChatGPT, Gemini e Colab.",
        ],
        7.15,
        2.68,
        5.1,
        14.5,
        INK,
        gap=0.22,
        row_h=0.52,
    )
    add_footer(slide)

    # =========================================================================
    # SLIDE 3 — A DOCUMENTAÇÃO DE ORIGEM
    # =========================================================================
    slide = presentation.slides.add_slide(blank)
    add_header(slide, "A documentação de origem", "A especificação oficial da API HighBond como fonte de verdade", 3, total_slides)
    add_metric(slide, f"{m['num_paths']}", "caminhos (paths) OpenAPI", 0.75, 1.72, 2.75, TEAL)
    add_metric(slide, f"{m['num_ops']}", "operações HTTP documentadas", 3.78, 1.72, 2.75, BLUE)
    add_metric(slide, f"{m['num_tags']}", "domínios / tags funcionais", 6.81, 1.72, 2.75, ORANGE)
    add_metric(slide, f"{m['schemas']}", "schemas reutilizáveis", 9.84, 1.72, 2.75, PURPLE)

    add_rect(slide, 0.75, 3.38, 11.85, 3.2, WHITE, True, LINE)
    add_text(slide, "openapi.json — HighBond API Reference", 1.1, 3.72, 6.5, 0.35, 18, NAVY, True, "Aptos Display")
    add_text(slide, "OpenAPI 3.0.2  |  HighBond API v1.1.0  |  Padrão JSON:API v1.0  |  OAuth 2.0", 1.1, 4.18, 9.8, 0.28, 14, TEAL, True)
    add_bullet_list(
        slide,
        [
            f"Arquivo bruto de {m['size_mb']:.1f} MB contendo todas as rotas de Projects, Controls, Results (Events/Handlers), Strategy e Robots.",
            "Estrutura rica com parâmetros de rota/query, schemas aninhados ($refs), atributos de payload e exemplos de resposta.",
            "Transformado em documentos independentes para que o LLM consulte apenas os endpoints necessários a cada pergunta.",
        ],
        1.1,
        4.68,
        11.0,
        14,
        INK,
        gap=0.14,
    )
    add_footer(slide)

    # =========================================================================
    # SLIDE 4 — COBERTURA DA API
    # =========================================================================
    slide = presentation.slides.add_slide(blank)
    add_header(slide, "Cobertura da API", "Distribuição das 369 operações presentes na documentação", 4, total_slides)
    mc = m["method_counts"]
    labels = [
        ("GET", mc["get"], TEAL),
        ("POST", mc["post"], BLUE),
        ("PATCH", mc["patch"], ORANGE),
        ("DELETE", mc["delete"], RGBColor(201, 74, 74)),
        ("PUT", mc["put"], PURPLE),
    ]
    max_count = max(count for _, count, _ in labels)
    for index, (label, count, color) in enumerate(labels):
        y = 1.85 + index * 0.82
        add_badge(slide, label, 0.85, y + 0.02, 1.0, 0.38, color, WHITE, 12)
        add_rect(slide, 2.05, y + 0.02, 7.3, 0.38, RGBColor(231, 236, 241), True)
        add_rect(slide, 2.05, y + 0.02, max(0.35, 7.3 * count / max_count), 0.38, color, True)
        add_text(slide, str(count), 9.55, y + 0.04, 0.65, 0.3, 14.5, NAVY, True, align=PP_ALIGN.RIGHT)

    add_rect(slide, 10.55, 1.78, 2.05, 4.45, WHITE, True, LINE)
    add_rect(slide, 10.55, 1.78, 2.05, 0.1, TEAL, True)
    add_text(slide, "Cada endpoint preserva", 10.72, 2.05, 1.7, 0.5, 13.5, NAVY, True, align=PP_ALIGN.CENTER)
    add_text(
        slide,
        "• Método e Rota\n• operationId\n• Domínio (Tag)\n• Parâmetros\n• Request Body\n• Schemas JSON\n• Respostas HTTP",
        10.75,
        2.72,
        1.7,
        3.1,
        12.5,
        MUTED,
    )
    add_footer(slide)

    # =========================================================================
    # SLIDE 5 — PROCESSO EXECUTADO (PIPELINE RAG)
    # =========================================================================
    slide = presentation.slides.add_slide(blank)
    add_header(slide, "Processo executado", "Pipeline que converte a especificação OpenAPI em uma base semântica consultável", 5, total_slides)
    steps = [
        ("1. Extrair", "Leitura do OpenAPI JSON e resolução de referências", 0.72, TEAL),
        ("2. Estruturar", "Geração de 369 chunks em Markdown + YAML", 3.16, BLUE),
        ("3. Vetorizar", "Embeddings com Ollama (qwen3-embedding:0.6b)", 5.60, ORANGE),
        ("4. Indexar", "Matriz NumPy (.npy) normalizada em disco", 8.04, PURPLE),
        ("5. Consultar", "Busca em 2 etapas via MCP e API nos LLMs", 10.48, TEAL),
    ]
    for label, detail, x, color in steps:
        add_step(slide, label, detail, x, color)
    for x in (2.72, 5.16, 7.60, 10.04):
        add_text(slide, "→", x, 3.12, 0.34, 0.3, 18, MUTED, True, align=PP_ALIGN.CENTER)

    add_rect(slide, 0.72, 4.65, 11.9, 1.85, WHITE, True, LINE)
    add_text(slide, "Alinhamento e Rastreabilidade", 1.05, 4.88, 5.0, 0.3, 15.5, NAVY, True)
    add_text(
        slide,
        "• A ordem alfabética dos arquivos Markdown é preservada para manter cada chunk exatamente alinhado à sua linha na matriz de embeddings (.npy).\n"
        "• A consulta é dividida em duas operações complementares: buscar_highbond (localiza os endpoints mais relevantes por similaridade) e obter_chunk (recupera a documentação completa do endpoint escolhido).",
        1.05,
        5.28,
        11.2,
        1.0,
        13.5,
        INK,
    )
    add_footer(slide)

    # =========================================================================
    # SLIDE 6 — COMO A DOCUMENTAÇÃO FOI PREPARADA (CHUNKS)
    # =========================================================================
    slide = presentation.slides.add_slide(blank)
    add_header(slide, "Como a documentação foi preparada", "Cada operação da API vira uma unidade de contexto auto-contida em Markdown", 6, total_slides)
    add_rect(slide, 0.75, 1.72, 5.95, 4.85, CARD_DARK, True)
    add_badge(slide, "Exemplo de Chunk Markdown com Front Matter YAML", 1.05, 1.95, 4.3, 0.3, TEAL, WHITE, 9.5)
    code = (
        "---\n"
        "id: endpoint-post-orgs-org-id-events-createevent\n"
        'title: "Events: Create an event"\n'
        "tags: [Events]\n"
        "source: openapi.json\n"
        "---\n\n"
        "### `POST /orgs/{org_id}/events` — Create an event\n"
        "- **operationId:** `createEvent`\n"
        "- **Domínio(s):** Events\n\n"
        "#### Request Body / Parâmetros / Triggers\n"
        "Atributos: title, target, triggers (fieldUpdated,\n"
        "questionnaireResponded)..."
    )
    add_text(slide, code, 1.05, 2.42, 5.35, 3.9, 13.5, RGBColor(220, 233, 242), False, "Consolas")

    add_metric(slide, str(m["total_chunks"]), "arquivos Markdown na coleção", 7.1, 1.75, 5.5, BLUE)
    add_metric(slide, str(m["indexed_chunks"]), "chunks de endpoints com Front Matter YAML", 7.1, 3.18, 5.5, TEAL)
    add_text(slide, "Vantagens desse formato para LLMs", 7.12, 4.72, 4.5, 0.3, 16, NAVY, True)
    add_bullet_list(
        slide,
        [
            "Front Matter YAML isola id, título e tags para indexação limpa.",
            "Um endpoint inteiro por chunk evita cortar schemas JSON ao meio.",
            "Markdown estruturado é o formato nativo de melhor leitura para GPT e Gemini.",
        ],
        7.1,
        5.12,
        5.4,
        13.5,
        INK,
        gap=0.1,
    )
    add_footer(slide)

    # =========================================================================
    # SLIDE 7 — ÍNDICE SEMÂNTICO E BUSCA CROSS-LINGUAL
    # =========================================================================
    slide = presentation.slides.add_slide(blank)
    add_header(slide, "Índice semântico e busca multilíngue", "Embeddings permitem buscar por intenção em português na documentação em inglês", 7, total_slides)
    add_metric(slide, str(m["vector_count"]), "vetores armazenados (.npy)", 0.75, 1.75, 3.7, TEAL)
    add_metric(slide, str(m["vector_dimensions"]), "dimensões (qwen3-embedding:0.6b)", 4.8, 1.75, 3.7, BLUE)
    add_metric(slide, "0,55 – 0,60", "limiar de similaridade configurável", 8.85, 1.75, 3.75, ORANGE)

    add_rect(slide, 0.75, 3.42, 11.85, 1.65, WHITE, True, LINE)
    flow_items = [
        ("Pergunta em PT-BR", "Ex: 'Como criar Events e configurar triggers?'", 0.95, 2.55),
        ("Prompt c/ Instrução", "Instruct: Retrieve HighBond API...\nQuery: <pergunta>", 3.9, 2.65),
        ("Produto Escalar", "Matriz (369×1024) @ Vetor (1024)\n= Similaridade do Cosseno", 6.95, 2.65),
        ("Top-K + Conteúdo", "1º buscar_highbond (ranking)\n2º obter_chunk ( texto integral )", 10.0, 2.4),
    ]
    for f_title, f_sub, fx, fw in flow_items:
        add_text(slide, f_title, fx, 3.65, fw, 0.3, 14, NAVY, True)
        add_text(slide, f_sub, fx, 4.02, fw, 0.85, 11, MUTED)
    for ax in (3.52, 6.58, 9.64):
        add_text(slide, "→", ax, 3.85, 0.32, 0.3, 20, TEAL, True, align=PP_ALIGN.CENTER)

    add_rect(slide, 0.75, 5.38, 11.85, 1.25, SOFT_BG, True, LINE)
    add_text(
        slide,
        "Por que buscar em 2 etapas (buscar_highbond → obter_chunk)?\n"
        "Na 1ª chamada o LLM recebe os 5 a 10 candidatos mais próximos com score de similaridade e resumo. Em seguida, ele chama obter_chunk apenas para os IDs que realmente respondem à pergunta, mantendo o contexto enxuto e preciso.",
        1.05,
        5.55,
        11.2,
        0.95,
        13,
        INK,
    )
    add_footer(slide)

    # =========================================================================
    # SLIDE 8 — RESULTADO 1: CHATGPT (CASO REAL EVENTS & HANDLERS)
    # =========================================================================
    slide = presentation.slides.add_slide(blank)
    add_header(
        slide,
        "Resultado no ChatGPT: Consulta via MCP",
        "O modelo dividiu o problema em 2 requisições semânticas (Events e Handlers) e recuperou os chunks exatos",
        8,
        total_slides,
    )

    # Coluna Esquerda: Os dados reais retornados pelo ChatGPT
    add_rect(slide, 0.72, 1.52, 6.85, 5.32, WHITE, True, LINE)

    # Bloco Requisição 1
    add_badge(slide, "REQUISIÇÃO 1 — EVENTS (similaridade_minima: 0.55 | top 10)", 0.92, 1.68, 4.6, 0.28, GREEN, WHITE, 9)
    add_text(
        slide,
        'Pergunta: "Quais são os endpoints da API HighBond para listar, consultar, criar, atualizar e excluir Events (gatilhos/eventos) no módulo Resultados? Inclua métodos HTTP, rotas, payloads e atributos triggers."',
        0.92,
        2.02,
        6.45,
        0.52,
        9.5,
        INK,
        True,
    )
    add_mini_table(
        slide,
        headers=["Pos", "Simil.", "ID do Documento (Chunk)", "Endpoint Encontrado"],
        rows=[
            ["1", "0.7455", "endpoint-get-orgs-org-id-events-id-getevent", "GET evento"],
            ["2", "0.7287", "endpoint-get-orgs-org-id-events-getevents", "GET eventos"],
            ["3", "0.7041", "endpoint-post-orgs-org-id-events-createevent", "POST evento"],
            ["4", "0.7032", "endpoint-patch-orgs-org-id-events-id-updateevent", "PATCH evento"],
            ["10", "0.6749", "endpoint-delete-orgs-org-id-events-id-deleteevent", "DELETE evento"],
        ],
        x=0.92,
        y=2.56,
        col_widths=[0.45, 0.68, 3.85, 1.45],
        accent=GREEN,
        row_h=0.25,
        font_size=8.8,
    )

    # Bloco Requisição 2
    add_badge(slide, "REQUISIÇÃO 2 — HANDLERS E CONFIGURAÇÃO DE GATILHOS", 0.92, 4.22, 4.6, 0.28, TEAL, WHITE, 9)
    add_text(
        slide,
        'Pergunta: "Quais são os endpoints da API HighBond para obter, criar, atualizar e excluir Handlers? Preciso do schema/payload de conditions e actions e da relação entre Events e Handlers (fieldUpdated e questionnaireResponded)."',
        0.92,
        4.56,
        6.45,
        0.52,
        9.5,
        INK,
        True,
    )
    add_mini_table(
        slide,
        headers=["Pos", "Simil.", "ID do Documento (Chunk)", "Endpoint Encontrado"],
        rows=[
            ["1", "0.7759", "endpoint-post-orgs-org-id-handlers-createhandler", "POST Handler"],
            ["2", "0.7703", "endpoint-get-orgs-org-id-handlers-id-gethandler", "GET Handler individual"],
            ["3", "0.7621", "endpoint-patch-orgs-org-id-handlers-id-updatehandler", "PATCH Handler"],
        ],
        x=0.92,
        y=5.12,
        col_widths=[0.45, 0.68, 3.85, 1.45],
        accent=TEAL,
        row_h=0.26,
        font_size=8.8,
    )
    add_text(
        slide,
        "✓ Após o buscar_highbond, o ChatGPT acionou obter_chunk para ler os schemas completos de cada operação.",
        0.92,
        6.28,
        6.45,
        0.35,
        9.5,
        NAVY,
        True,
    )

    # Coluna Direita: Espaço para o Print do ChatGPT
    add_screenshot_box(
        slide,
        x=7.78,
        y=1.52,
        w=4.82,
        h=5.32,
        window_title="ChatGPT — MCP rag---highbond-api",
        placeholder_label="PRINT DO CHATGPT AQUI",
        hint_text="Cole aqui o print da resposta do ChatGPT\n(ou salve como docs/print_gpt.png)",
        candidate_paths=PRINT_GPT,
        accent=GREEN,
    )
    add_footer(slide)

    # =========================================================================
    # SLIDE 9 — RESULTADO 2: GEMINI (VIA MCP)
    # =========================================================================
    slide = presentation.slides.add_slide(blank)
    add_header(
        slide,
        "Resultado no Gemini: Consulta via MCP",
        "Descoberta automática das tools buscar_highbond e obter_chunk para responder dúvidas da API",
        9,
        total_slides,
    )

    add_rect(slide, 0.72, 1.55, 5.55, 5.25, WHITE, True, LINE)
    add_badge(slide, "FLUXO EXECUTADO PELO GEMINI", 0.98, 1.8, 2.8, 0.3, BLUE, WHITE, 9.5)
    add_text(slide, "Consulta Contextual sem Alucinação de Endpoints", 0.98, 2.22, 5.0, 0.4, 17, NAVY, True, "Aptos Display")
    add_bullet_list(
        slide,
        [
            "O Gemini recebe a pergunta em português e aciona a ferramenta buscar_highbond do servidor MCP.",
            "Identifica com alta similaridade os endpoints de criação de projetos (0.7018) e importação (0.6892).",
            "Chama obter_chunk com o ID selecionado para inspecionar os parâmetros obrigatórios e estados ('active', 'archive').",
            "Entrega a explicação técnica e o exemplo de requisição fiéis à documentação oficial.",
        ],
        0.98,
        2.78,
        5.05,
        12.5,
        INK,
        gap=0.14,
        bullet_color=BLUE,
        row_h=0.48,
    )

    add_mini_table(
        slide,
        headers=["Pos", "Simil.", "ID Retornado ao Gemini", "Título"],
        rows=[
            ["1", "0.7018", "endpoint-post-orgs-org-id-projects-createproject", "Create a project"],
            ["2", "0.6892", "endpoint-post-orgs-org-id-import-data-createimport", "Create import"],
        ],
        x=0.98,
        y=5.45,
        col_widths=[0.42, 0.65, 2.65, 1.3],
        accent=BLUE,
        row_h=0.28,
        font_size=8.8,
    )

    add_screenshot_box(
        slide,
        x=6.5,
        y=1.55,
        w=6.1,
        h=5.25,
        window_title="Gemini — Uso da Ferramenta MCP rag-highbond",
        placeholder_label="PRINT DO GEMINI AQUI",
        hint_text="Cole aqui o print do Gemini utilizando o MCP rag-highbond\n(ou salve como docs/print_gemini.png)",
        candidate_paths=PRINT_GEMINI,
        accent=BLUE,
    )
    add_footer(slide)

    # =========================================================================
    # SLIDE 10 — RESULTADO 3: GOOGLE COLAB / NOTEBOOK
    # =========================================================================
    slide = presentation.slides.add_slide(blank)
    add_header(
        slide,
        "Resultado no Google Colab: Experimentação e Busca",
        "Validação direta das consultas semânticas, scores de similaridade e inspeção dos chunks em Python",
        10,
        total_slides,
    )

    add_rect(slide, 0.72, 1.55, 5.55, 5.25, CARD_DARK, True)
    add_badge(slide, "EXECUÇÃO NO GOOGLE COLAB / JUPYTER", 0.98, 1.8, 3.2, 0.3, ORANGE, WHITE, 9.5)
    colab_code = (
        "# Consulta semântica direta no notebook\n"
        "res = requests.post(\n"
        '    f"{BASE_URL}/buscar",\n'
        "    json={\n"
        '        "pergunta": "Como atualizar um control test?",\n'
        '        "quantidade": 5,\n'
        '        "similaridade_minima": 0.55\n'
        "    }\n"
        ").json()\n\n"
        "for r in res:\n"
        '    print(r["posicao"], r["similaridade"], r["id"])\n\n'
        "# Recupera o Markdown completo do 1º resultado\n"
        'chunk = requests.get(f"{BASE_URL}/chunks/{res[0][\'id\']}").json()\n'
        'print(chunk["conteudo"])'
    )
    add_text(slide, colab_code, 0.98, 2.28, 5.05, 3.1, 11.5, RGBColor(220, 235, 245), False, "Consolas")

    add_rect(slide, 0.98, 5.45, 5.05, 1.1, RGBColor(39, 58, 77), True, ORANGE, 1.0)
    add_text(
        slide,
        "Permite testar lotes de perguntas em português, calibrar o limiar de similaridade (0.55–0.60) e auditar os trechos retornados pelo índice.",
        1.15,
        5.6,
        4.7,
        0.8,
        11.5,
        WHITE,
    )

    add_screenshot_box(
        slide,
        x=6.5,
        y=1.55,
        w=6.1,
        h=5.25,
        window_title="Google Colab — Notebook de Testes e Validação do RAG",
        placeholder_label="PRINT DO GOOGLE COLAB AQUI",
        hint_text="Cole aqui o print do Google Colab executando as buscas\n(ou salve como docs/print_colab.png)",
        candidate_paths=PRINT_COLAB,
        accent=ORANGE,
    )
    add_footer(slide)

    # =========================================================================
    # SLIDE 11 — CONCLUSÃO E PRÓXIMOS PASSOS
    # =========================================================================
    slide = presentation.slides.add_slide(blank)
    add_header(slide, "Síntese dos Resultados e Próximos Passos", "Uma base semântica precisa, rastreável e validada em múltiplos LLMs", 11, total_slides)

    add_rect(slide, 0.75, 1.72, 5.7, 4.9, WHITE, True, TEAL, 1.5)
    add_badge(slide, "RESULTADOS COMPROVADOS", 1.05, 2.0, 2.45, 0.3, TEAL, WHITE, 9.5)
    add_bullet_list(
        slide,
        [
            "Documentação OpenAPI integral convertida em 369 unidades de contexto.",
            "Alta precisão semântica PT-BR → EN (scores entre 0.67 e 0.78 para endpoints exatos).",
            "Recuperação completa de CRUD (GET, POST, PATCH, DELETE) como visto em Events e Handlers.",
            "Funcionamento validado na prática no ChatGPT, no Gemini e no Google Colab.",
            "Eliminação de alucinações sobre rotas, payloads e atributos da API HighBond.",
        ],
        1.05,
        2.55,
        5.1,
        13.5,
        INK,
        gap=0.18,
        bullet_color=TEAL,
        row_h=0.48,
    )

    add_rect(slide, 6.8, 1.72, 5.8, 4.9, WHITE, True, LINE)
    add_badge(slide, "EVOLUÇÕES FUTURAS", 7.1, 2.0, 2.1, 0.3, PURPLE, WHITE, 9.5)
    add_bullet_list(
        slide,
        [
            "Expandir a base para novas coleções (ex: documentação do Diligent Robots).",
            "Combinar busca semântica com filtros explícitos por tag/domínio e verbo HTTP.",
            "Automatizar a regeneração de chunks e embeddings a novas versões do OpenAPI.",
            "Avaliar métricas de recuperação (Recall@K / MRR) em um conjunto expandido de perguntas.",
        ],
        7.1,
        2.55,
        5.15,
        13.5,
        INK,
        gap=0.18,
        bullet_color=PURPLE,
        row_h=0.48,
    )

    add_footer(slide)

    try:
        presentation.save(output_path)
        return output_path
    except PermissionError:
        alt_path = ROOT / "apresentacao_rag_highbond_v2.pptx"
        presentation.save(alt_path)
        return alt_path


if __name__ == "__main__":
    caminho = build_presentation()
    print(f"Apresentação gerada em: {caminho}")
