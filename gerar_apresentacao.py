"""Gera uma apresentação moderna e editável do projeto RAG HighBond (Local + Cloud Run + MCP + GPT + Gemini)."""

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

# Opcional: se o usuário salvar os prints com esses nomes na pasta docs/ ou raiz, o script já insere automaticamente!
PRINT_GEMINI = [ROOT / "docs" / "print_gemini.png", ROOT / "print_gemini.png"]
PRINT_GPT = [ROOT / "docs" / "print_gpt.png", ROOT / "print_gpt.png"]
PRINT_API = [ROOT / "docs" / "print_api.png", ROOT / "print_api.png"]

# Paleta Moderna High-Contrast
NAVY = RGBColor(15, 29, 50)
DARK_SLATE = RGBColor(24, 43, 73)
CARD_DARK = RGBColor(30, 41, 59)
BLUE = RGBColor(0, 116, 217)
TEAL = RGBColor(0, 163, 173)
ORANGE = RGBColor(242, 125, 42)
PURPLE = RGBColor(108, 92, 231)
GREEN = RGBColor(16, 185, 129)
INK = RGBColor(29, 39, 51)
MUTED = RGBColor(95, 109, 126)
PAPER = RGBColor(246, 249, 252)
SOFT_BLUE = RGBColor(235, 245, 255)
SOFT_TEAL = RGBColor(232, 250, 250)
WHITE = RGBColor(255, 255, 255)
LINE = RGBColor(214, 223, 233)


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


def add_badge(slide, text, x, y, w, h=0.34, bg=TEAL, fg=WHITE, size=10.5):
    add_rect(slide, x, y, w, h, bg, radius=True)
    add_text(slide, text, x, y + 0.04, w, h - 0.04, size, fg, True, align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE)


def add_header(slide, title, subtitle, number, total=12):
    add_rect(slide, 0, 0, 13.333, 7.5, PAPER)
    add_rect(slide, 0, 0, 13.333, 0.08, TEAL)
    add_text(slide, title, 0.72, 0.38, 10.2, 0.48, 25, NAVY, True, "Aptos Display")
    add_text(slide, subtitle, 0.74, 0.88, 10.7, 0.3, 11, MUTED)
    add_badge(slide, f"{number:02d} / {total:02d}", 11.75, 0.44, 0.88, 0.32, DARK_SLATE, WHITE, 10)
    add_rect(slide, 0.72, 1.28, 11.9, 0.015, LINE)


def add_footer(slide):
    add_rect(slide, 0.72, 7.05, 11.9, 0.01, LINE)
    add_text(
        slide,
        "RAG HighBond | Busca Semântica + Servidor MCP + API Cloud Run (https://rag-highbond-764415736.us-central1.run.app)",
        0.72,
        7.12,
        10.5,
        0.22,
        8.5,
        MUTED,
    )
    add_text(slide, "Rafael Luckner", 11.2, 7.12, 1.4, 0.22, 8.5, NAVY, True, align=PP_ALIGN.RIGHT)


def add_bullet_list(slide, items, x, y, w, size=14.5, color=INK, gap=0.11, bullet_color=TEAL, row_h=0.42):
    current_y = y
    for item in items:
        add_text(slide, "▸", x, current_y, 0.24, 0.28, size, bullet_color, True)
        add_text(slide, item, x + 0.26, current_y, w - 0.26, row_h, size, color)
        current_y += row_h + gap


def add_metric(slide, value, label, x, y, w, accent=TEAL, sublabel=None):
    h = 1.32 if sublabel else 1.2
    add_rect(slide, x, y, w, h, WHITE, True, LINE)
    add_rect(slide, x, y, 0.09, h, accent)
    add_text(slide, str(value), x + 0.25, y + 0.14, w - 0.35, 0.44, 25, NAVY, True, "Aptos Display")
    add_text(slide, label, x + 0.25, y + 0.68, w - 0.32, 0.28, 11, INK, True)
    if sublabel:
        add_text(slide, sublabel, x + 0.25, y + 0.95, w - 0.32, 0.24, 9.5, MUTED)


def add_step(slide, number_str, label, detail, x, y, w, color):
    add_rect(slide, x, y, w, 1.65, WHITE, True, LINE)
    add_rect(slide, x, y, w, 0.11, color, True)
    add_badge(slide, number_str, x + 0.16, y + 0.24, 0.42, 0.28, color, WHITE, 10)
    add_text(slide, label, x + 0.16, y + 0.62, w - 0.32, 0.32, 14.5, NAVY, True)
    add_text(slide, detail, x + 0.16, y + 1.0, w - 0.32, 0.52, 10.5, MUTED)


def add_screenshot_frame(slide, x, y, w, h, title_window, instruction_text, candidate_paths, accent=TEAL):
    """Cria uma moldura de janela moderna para o print (ou insere a imagem automaticamente se existir)."""
    # Sombra/borda externa da janela
    add_rect(slide, x, y, w, h, WHITE, True, LINE, line_width=1.5)
    # Barra de título estilo navegador/app escuro
    add_rect(slide, x, y, w, 0.42, DARK_SLATE, True)
    # Bolinhas da janela (macOS/modern window controls)
    add_rect(slide, x + 0.18, y + 0.14, 0.12, 0.12, RGBColor(239, 68, 68), True)
    add_rect(slide, x + 0.36, y + 0.14, 0.12, 0.12, RGBColor(245, 158, 11), True)
    add_rect(slide, x + 0.54, y + 0.14, 0.12, 0.12, RGBColor(16, 185, 129), True)
    add_text(slide, title_window, x + 0.8, y + 0.09, w - 1.0, 0.24, 10.5, WHITE, True, "Consolas")

    img_path = next((p for p in candidate_paths if p.exists()), None)
    inner_x, inner_y, inner_w, inner_h = x + 0.14, y + 0.54, w - 0.28, h - 0.68

    if img_path is not None:
        slide.shapes.add_picture(str(img_path), Inches(inner_x), Inches(inner_y), width=Inches(inner_w))
    else:
        # Área tracejada/estilizada pronta para colar o print no PowerPoint
        add_rect(slide, inner_x, inner_y, inner_w, inner_h, PAPER, True, accent, line_width=1.5)
        add_badge(slide, "ESPAÇO PARA PRINT / SCREENSHOT", inner_x + inner_w / 2 - 1.45, inner_y + inner_h / 2 - 0.65, 2.9, 0.36, accent, WHITE, 10)
        add_text(
            slide,
            instruction_text,
            inner_x + 0.4,
            inner_y + inner_h / 2 - 0.15,
            inner_w - 0.8,
            0.9,
            12,
            MUTED,
            False,
            align=PP_ALIGN.CENTER,
        )


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
    total_slides = 12

    presentation = Presentation()
    presentation.slide_width = Inches(13.333)
    presentation.slide_height = Inches(7.5)
    blank = presentation.slide_layouts[6]

    # =========================================================================
    # SLIDE 1 — CAPA
    # =========================================================================
    slide = presentation.slides.add_slide(blank)
    add_rect(slide, 0, 0, 13.333, 7.5, NAVY)
    add_rect(slide, 0, 0, 0.24, 7.5, TEAL)
    add_rect(slide, 8.75, 0, 4.583, 7.5, DARK_SLATE)

    add_badge(slide, "RAG • MODEL CONTEXT PROTOCOL (MCP) • GOOGLE CLOUD RUN", 0.88, 0.92, 4.65, 0.34, TEAL, WHITE, 10)
    add_text(slide, "RAG HighBond", 0.88, 1.48, 7.5, 0.85, 42, WHITE, True, "Aptos Display")
    add_text(
        slide,
        "Da especificação OpenAPI a um Serviço Cloud & MCP\nacessível no Gemini, ChatGPT, IDEs e via API REST",
        0.9,
        2.42,
        7.5,
        0.95,
        20,
        RGBColor(210, 228, 245),
    )
    add_text(
        slide,
        "Busca semântica cross-lingual (PT ↔ EN) com Qwen3-Embedding 0.6B,\nhospedada em container Serverless com cache LRU, autenticação e controle de taxa.",
        0.9,
        3.68,
        7.3,
        0.75,
        13.5,
        RGBColor(175, 198, 220),
    )

    # Cards de destaque na direita da capa
    add_rect(slide, 9.25, 1.15, 3.45, 1.45, CARD_DARK, True, TEAL, 1.5)
    add_text(slide, f"{m['indexed_chunks']} Endpoints", 9.5, 1.35, 3.0, 0.4, 24, TEAL, True, "Aptos Display")
    add_text(slide, f"Indexados a partir de {m['num_paths']} rotas da documentação oficial HighBond", 9.5, 1.85, 3.0, 0.5, 10.5, WHITE)

    add_rect(slide, 9.25, 2.85, 3.45, 1.45, CARD_DARK, True, BLUE, 1.5)
    add_text(slide, "MCP + REST API", 9.5, 3.05, 3.0, 0.4, 24, RGBColor(96, 178, 255), True, "Aptos Display")
    add_text(slide, "Conectado ao Gemini/Antigravity, VS Code, Claude e App do ChatGPT", 9.5, 3.55, 3.0, 0.5, 10.5, WHITE)

    add_rect(slide, 9.25, 4.55, 3.45, 1.45, CARD_DARK, True, ORANGE, 1.5)
    add_text(slide, "Cloud Run Live", 9.5, 4.75, 3.0, 0.4, 24, ORANGE, True, "Aptos Display")
    add_text(slide, "Deploy em produção com resposta em ~650 ms (e ~2 ms via Cache LRU)", 9.5, 5.25, 3.0, 0.5, 10.5, WHITE)

    add_text(slide, "Rafael Luckner  •  2026", 0.9, 6.68, 4.5, 0.3, 11, RGBColor(184, 207, 224), True)

    # =========================================================================
    # SLIDE 2 — O DESAFIO & EVOLUÇÃO
    # =========================================================================
    slide = presentation.slides.add_slide(blank)
    add_header(slide, "O desafio e a visão do serviço", "Transformar uma especificação extensa em uma ferramenta viva para qualquer LLM", 2, total_slides)

    add_rect(slide, 0.75, 1.65, 5.65, 4.95, WHITE, True, LINE)
    add_badge(slide, "PROBLEMA INICIAL", 1.05, 1.95, 1.75, 0.3, ORANGE, WHITE, 9.5)
    add_text(
        slide,
        "Como encontrar rapidamente o endpoint exato em uma API com 369 operações sem estourar o contexto da LLM?",
        1.05,
        2.42,
        5.05,
        1.15,
        20,
        NAVY,
        True,
        "Aptos Display",
    )
    add_bullet_list(
        slide,
        [
            "O arquivo openapi.json bruto tem mais de 3 MB (inviável enviar inteiro no prompt).",
            "A documentação original é 100% em inglês, enquanto as perguntas vêm em português.",
            "Desenvolvedores e agentes precisam tanto de busca rápida quanto do schema completo.",
        ],
        1.05,
        3.85,
        5.0,
        13.5,
        MUTED,
        gap=0.18,
        bullet_color=ORANGE,
    )

    add_rect(slide, 6.72, 1.65, 5.88, 4.95, WHITE, True, TEAL, 1.5)
    add_badge(slide, "SOLUÇÃO IMPLEMENTADA", 7.05, 1.95, 2.15, 0.3, TEAL, WHITE, 9.5)
    add_text(slide, "Arquitetura RAG como Serviço Universal", 7.05, 2.42, 5.2, 0.4, 20, NAVY, True, "Aptos Display")
    add_bullet_list(
        slide,
        [
            "Segmentação inteligente em 369 chunks Markdown com metadados YAML.",
            "Busca semântica bilíngue (PT ↔ EN) com Qwen3-Embedding (0.6B).",
            "Dupla exposição: Protocolo MCP (stdio/HTTP/SSE) + API REST (OpenAPI 3.1).",
            "Proteção de produção: API Key Bearer, Rate Limit (30/min) e Semáforo de CPU.",
            "Hospedado gratuitamente no Google Cloud Run com modelo embarcado na imagem.",
        ],
        7.05,
        3.05,
        5.25,
        13.5,
        INK,
        gap=0.14,
        bullet_color=TEAL,
    )
    add_footer(slide)

    # =========================================================================
    # SLIDE 3 — A DOCUMENTAÇÃO DE ORIGEM
    # =========================================================================
    slide = presentation.slides.add_slide(blank)
    add_header(slide, "A documentação de origem", "A especificação oficial OpenAPI serve como fonte única de verdade", 3, total_slides)
    add_metric(slide, f"{m['num_paths']}", "Rotas (Paths) OpenAPI", 0.75, 1.72, 2.8, TEAL, "Endpoints RESTful mapeados")
    add_metric(slide, f"{m['num_ops']}", "Operações HTTP", 3.78, 1.72, 2.8, BLUE, "GET, POST, PATCH, PUT, DELETE")
    add_metric(slide, f"{m['num_tags']}", "Domínios Funcionais", 6.81, 1.72, 2.8, ORANGE, "Projects, Controls, Strategy, etc.")
    add_metric(slide, f"{m['schemas']}", "Schemas de Dados", 9.84, 1.72, 2.78, PURPLE, "Payloads e modelos JSON:API")

    add_rect(slide, 0.75, 3.42, 11.87, 3.2, WHITE, True, LINE)
    add_text(slide, "Especificação Técnica: HighBond API Reference (Diligent)", 1.1, 3.75, 8.5, 0.35, 18, NAVY, True, "Aptos Display")
    add_text(slide, "OpenAPI 3.0.2  •  Padrão JSON:API v1.0  •  Autenticação Bearer / OAuth 2.0", 1.1, 4.18, 9.8, 0.28, 14, TEAL, True)
    add_bullet_list(
        slide,
        [
            f"Base bruta de {m['size_mb']:.1f} MB processada e higienizada (remoção de tokens de exemplo e resolução de $refs).",
            "Cobre todos os módulos da plataforma: Auditoria, Controles, Riscos Estratégicos, Robots, Storyboards e Questionários.",
            "Cada operação foi isolada mantendo parâmetros de rota/query, schemas de corpo e códigos de resposta HTTP.",
        ],
        1.1,
        4.68,
        11.0,
        13.5,
        INK,
        gap=0.1,
    )
    add_footer(slide)

    # =========================================================================
    # SLIDE 4 — COBERTURA DA API
    # =========================================================================
    slide = presentation.slides.add_slide(blank)
    add_header(slide, "Cobertura da API por Método HTTP", "Distribuição das 369 operações indexadas na base vetorial", 4, total_slides)
    mc = m["method_counts"]
    labels = [
        ("GET", mc["get"], TEAL, "Consultas e listagens paginadas"),
        ("POST", mc["post"], BLUE, "Criação de recursos e uploads"),
        ("PATCH", mc["patch"], ORANGE, "Atualizações parciais de estado"),
        ("DELETE", mc["delete"], RGBColor(214, 69, 69), "Remoção de registros e vínculos"),
        ("PUT", mc["put"], PURPLE, "Substituição integral de recursos"),
    ]
    max_count = max(count for _, count, _, _ in labels)
    for index, (label, count, color, desc) in enumerate(labels):
        y = 1.78 + index * 0.92
        add_badge(slide, label, 0.82, y + 0.04, 1.05, 0.38, color, WHITE, 12)
        add_rect(slide, 2.05, y + 0.04, 6.8, 0.38, RGBColor(231, 236, 241), True)
        add_rect(slide, 2.05, y + 0.04, max(0.4, 6.8 * count / max_count), 0.38, color, True)
        add_text(slide, str(count), 9.0, y + 0.06, 0.65, 0.3, 15, NAVY, True, align=PP_ALIGN.RIGHT)
        add_text(slide, desc, 9.85, y + 0.08, 2.8, 0.3, 11.5, MUTED)

    add_footer(slide)

    # =========================================================================
    # SLIDE 5 — PIPELINE DE ENGENHARIA RAG
    # =========================================================================
    slide = presentation.slides.add_slide(blank)
    add_header(slide, "Pipeline de Engenharia RAG", "Do arquivo OpenAPI bruto ao serviço em nuvem de baixa latência", 5, total_slides)
    steps = [
        ("01", "Extrair", "Parsing do OpenAPI JSON e resolução de schemas", 0.72, TEAL),
        ("02", "Estruturar", "369 arquivos Markdown com Front Matter YAML", 3.16, BLUE),
        ("03", "Vetorizar", "Qwen3-Embedding 0.6B (1024 dimensões)", 5.60, ORANGE),
        ("04", "Indexar", "Matriz NumPy (.npy) normalizada + Dict O(1)", 8.04, PURPLE),
        ("05", "Servir", "FastAPI + FastMCP no Google Cloud Run", 10.48, GREEN),
    ]
    for num_s, label, detail, x, color in steps:
        add_step(slide, num_s, label, detail, x, 2.15, 2.12, color)
    for x in (2.88, 5.32, 7.76, 10.20):
        add_text(slide, "→", x, 2.78, 0.26, 0.3, 18, MUTED, True, align=PP_ALIGN.CENTER)

    add_rect(slide, 0.72, 4.35, 11.88, 2.15, WHITE, True, LINE)
    add_text(slide, "Destaques de Engenharia do Pipeline", 1.05, 4.55, 6.0, 0.32, 16, NAVY, True)
    add_bullet_list(
        slide,
        [
            "Alinhamento determinístico: ordenação alfabética garante correspondência exata entre cada chunk .md e sua linha na matriz .npy.",
            "Instruction-Aware Retrieval: perguntas recebem o prefixo 'Instruct: Retrieve the most relevant HighBond API documentation...' para máxima precisão PT→EN.",
            "Imagem Docker enxuta (~700 MB): remoção das bibliotecas pesadas de GPU (CUDA/ROCm) do Ollama, mantendo apenas o motor CPU + modelo pré-carregado.",
        ],
        1.05,
        4.98,
        11.2,
        13,
        INK,
        gap=0.08,
    )
    add_footer(slide)

    # =========================================================================
    # SLIDE 6 — ESTRUTURA DOS CHUNKS MARKDOWN
    # =========================================================================
    slide = presentation.slides.add_slide(blank)
    add_header(slide, "Unidade de Contexto (Chunking Semântico)", "Cada endpoint é isolado em um documento Markdown auto-contido", 6, total_slides)
    add_rect(slide, 0.75, 1.68, 6.1, 4.95, CARD_DARK, True)
    add_badge(slide, "endpoint-post-orgs-org-id-projects-createproject.md", 1.05, 1.92, 4.6, 0.3, TEAL, WHITE, 9.5)
    code = (
        "---\n"
        'id: "endpoint-post-orgs-org-id-projects-createproject"\n'
        'title: "Projects: Create a project"\n'
        "tags:\n"
        "  - Projects\n"
        'source: "openapi.json"\n'
        "---\n\n"
        "### `POST /orgs/{org_id}/projects` — Create a project\n"
        "- **operationId:** `createProject`\n"
        "- **Domínio(s):** Projects\n\n"
        "#### Parâmetros, Request Body e Respostas (201 Created)..."
    )
    add_text(slide, code, 1.05, 2.42, 5.55, 3.9, 13, RGBColor(220, 235, 245), False, "Consolas")

    add_metric(slide, str(m["indexed_chunks"]), "Chunks válidos indexados", 7.2, 1.72, 5.4, BLUE, "1 chunk = 1 endpoint completo (sem quebrar tabelas JSON)")
    add_rect(slide, 7.2, 3.28, 5.4, 3.35, WHITE, True, LINE)
    add_text(slide, "Busca em 2 Etapas (Economia de Tokens)", 7.5, 3.55, 4.8, 0.32, 16, NAVY, True)
    add_bullet_list(
        slide,
        [
            "Etapa 1 (buscar_highbond / POST /buscar): Retorna apenas o Top-K com ID, título, score de similaridade e um resumo de 500 caracteres.",
            "Etapa 2 (obter_chunk / GET /chunks/{id}): O LLM solicita o Markdown completo apenas do endpoint que realmente vai utilizar.",
            "Busca de Chunk O(1): Dicionário em memória indexado por ID entrega o documento completo instantaneamente.",
        ],
        7.5,
        4.05,
        4.85,
        13,
        INK,
        gap=0.18,
    )
    add_footer(slide)

    # =========================================================================
    # SLIDE 7 — MOTOR SEMÂNTICO, CACHE E CONTROLE DE TAXA
    # =========================================================================
    slide = presentation.slides.add_slide(blank)
    add_header(slide, "Performance, Cache LRU e Proteção do Serviço", "Arquitetura desenhada para responder rápido e suportar múltiplos usuários", 7, total_slides)

    add_metric(slide, f"{m['vector_count']} × {m['vector_dimensions']}", "Matriz de Embeddings (.npy)", 0.75, 1.68, 2.8, TEAL, "Apenas 1,5 MB em memória RAM")
    add_metric(slide, "~650 ms", "Latência de Busca (Warm)", 3.78, 1.68, 2.8, BLUE, "Vetorização Qwen3 em CPU + NumPy")
    add_metric(slide, "~2,0 ms", "Latência em Cache Hit (LRU)", 6.81, 1.68, 2.8, GREEN, "Até 256 perguntas recentes em RAM")
    add_metric(slide, "30 req/min", "Rate Limit por Usuário/IP", 9.84, 1.68, 2.78, ORANGE, "Sliding window + Semáforo CPU (4)")

    add_rect(slide, 0.75, 3.35, 11.87, 3.3, WHITE, True, LINE)
    add_text(slide, "Camadas de Proteção e Estabilidade Implementadas (api.py & ollama.py)", 1.1, 3.62, 10.5, 0.32, 16, NAVY, True)

    cards = [
        ("Autenticação Flexível", "Aceita Authorization: Bearer, header X-API-Key ou query ?api_key= em tempo constante (secrets.compare_digest).", TEAL, 1.1),
        ("Rate Limiting (HTTP 429)", "Janela deslizante por chave ou IP real (CF-Connecting-IP / X-Forwarded-For) com retorno do cabeçalho Retry-After.", ORANGE, 4.95),
        ("Semáforo + Cache LRU", "BoundedSemaphore impede sobrecarga simultânea de CPU no Ollama, enquanto o lru_cache responde buscas repetidas em 2 ms.", BLUE, 8.8),
    ]
    for c_title, c_desc, c_color, c_x in cards:
        add_rect(slide, c_x, 4.18, 3.55, 2.15, PAPER, True, LINE)
        add_rect(slide, c_x, 4.18, 3.55, 0.09, c_color, True)
        add_text(slide, c_title, c_x + 0.2, 4.42, 3.15, 0.3, 14, NAVY, True)
        add_text(slide, c_desc, c_x + 0.2, 4.82, 3.15, 1.3, 11.5, MUTED)

    add_footer(slide)

    # =========================================================================
    # SLIDE 8 — ARQUITETURA EM PRODUÇÃO (GOOGLE CLOUD RUN)
    # =========================================================================
    slide = presentation.slides.add_slide(blank)
    add_header(slide, "Arquitetura em Produção no Google Cloud Run", "Um único serviço servindo Agentes MCP, ChatGPT Actions e Requisições HTTP", 8, total_slides)

    # Coluna Esquerda: Clientes
    add_rect(slide, 0.75, 1.72, 3.4, 4.9, WHITE, True, LINE)
    add_badge(slide, "CLIENTES CONECTADOS", 1.0, 1.95, 2.9, 0.32, DARK_SLATE, WHITE, 10)

    clientes = [
        ("Gemini / Antigravity / IDEs", "Via MCP Local (stdio) ou Remoto (/mcp)", TEAL, 2.52),
        ("App do ChatGPT (Web & Mobile)", "Via Custom GPT Actions (/openapi.json) e @menção", GREEN, 3.88),
        ("Scripts Python / Notebooks / n8n", "Via Requisição HTTP REST (POST /buscar)", BLUE, 5.24),
    ]
    for cl_title, cl_sub, cl_col, cl_y in clientes:
        add_rect(slide, 1.0, cl_y, 2.9, 1.1, PAPER, True, cl_col, 1.2)
        add_text(slide, cl_title, 1.15, cl_y + 0.16, 2.6, 0.3, 12.5, NAVY, True)
        add_text(slide, cl_sub, 1.15, cl_y + 0.52, 2.6, 0.45, 10.5, MUTED)

    add_text(slide, "HTTPS\nBearer", 4.25, 3.85, 0.85, 0.6, 11, TEAL, True, align=PP_ALIGN.CENTER)
    add_text(slide, "⇄", 4.35, 4.35, 0.65, 0.4, 24, TEAL, True, align=PP_ALIGN.CENTER)

    # Coluna Direita: Container Cloud Run
    add_rect(slide, 5.2, 1.72, 7.42, 4.9, CARD_DARK, True, TEAL, 1.5)
    add_badge(slide, "GOOGLE CLOUD RUN (us-central1 • Gen2 • 2 GiB RAM • Scale-to-Zero)", 5.5, 1.95, 6.8, 0.34, TEAL, WHITE, 10)
    add_text(slide, "https://rag-highbond-764415736.us-central1.run.app", 5.5, 2.42, 6.8, 0.3, 13, RGBColor(139, 233, 253), True, "Consolas")

    add_rect(slide, 5.5, 2.92, 3.25, 3.35, RGBColor(39, 55, 77), True, BLUE, 1.2)
    add_text(slide, "FastAPI + FastMCP (api.py)", 5.7, 3.12, 2.85, 0.3, 13.5, WHITE, True)
    add_text(
        slide,
        "• POST /buscar\n• GET /chunks/{id}\n• GET /openapi.json\n• GET /health\n• POST /mcp (Streamable HTTP)\n• GET /sse (Server-Sent Events)",
        5.7,
        3.55,
        2.85,
        2.4,
        11.5,
        RGBColor(210, 228, 245),
        False,
        "Consolas",
    )

    add_rect(slide, 9.05, 2.92, 3.25, 3.35, RGBColor(39, 55, 77), True, ORANGE, 1.2)
    add_text(slide, "Motor Interno Embarcado", 9.25, 3.12, 2.85, 0.3, 13.5, WHITE, True)
    add_text(
        slide,
        "• Ollama Server (127.0.0.1:11434)\n• Modelo qwen3-embedding:0.6b\n  pré-baixado em /app/.ollama\n• IndiceBusca (NumPy .npy)\n• 369 Chunks Markdown\n• Cache LRU (256 queries)",
        9.25,
        3.55,
        2.85,
        2.4,
        11.5,
        RGBColor(210, 228, 245),
    )

    add_footer(slide)

    # =========================================================================
    # SLIDE 9 — DEMONSTRAÇÃO 1: FUNCIONANDO NO GEMINI / ANTIGRAVITY (MCP)
    # =========================================================================
    slide = presentation.slides.add_slide(blank)
    add_header(slide, "Na Prática 1: Funcionando no Gemini / Antigravity (MCP)", "O agente aciona autonomamente as ferramentas buscar_highbond e obter_chunk", 9, total_slides)

    add_rect(slide, 0.75, 1.68, 4.35, 4.95, WHITE, True, LINE)
    add_badge(slide, "INTEGRAÇÃO VIA MCP", 1.0, 1.95, 2.1, 0.3, TEAL, WHITE, 9.5)
    add_text(slide, "Descoberta e Execução Nativa de Tools", 1.0, 2.4, 3.85, 0.55, 17, NAVY, True, "Aptos Display")
    add_bullet_list(
        slide,
        [
            "Configurado em mcp_config.json (local via stdio ou remoto via /mcp).",
            "O modelo identifica a dúvida sobre HighBond e chama buscar_highbond.",
            "Com o ID retornado (score 0.7018), lê o Markdown exato via obter_chunk.",
            "Gera código e explicações sem alucinar rotas ou parâmetros.",
        ],
        1.0,
        3.15,
        3.85,
        12.5,
        INK,
        gap=0.18,
        bullet_color=TEAL,
    )

    add_screenshot_frame(
        slide,
        x=5.35,
        y=1.68,
        w=7.25,
        h=4.95,
        title_window="Antigravity / Gemini — MCP Tool Call: rag-highbond (buscar_highbond)",
        instruction_text="Cole aqui o print do Gemini / Antigravity chamando a tool buscar_highbond\n(ou salve a imagem como docs/print_gemini.png e rode gerar_apresentacao.py)",
        candidate_paths=PRINT_GEMINI,
        accent=TEAL,
    )
    add_footer(slide)

    # =========================================================================
    # SLIDE 10 — DEMONSTRAÇÃO 2: FUNCIONANDO NO APP DO CHATGPT
    # =========================================================================
    slide = presentation.slides.add_slide(blank)
    add_header(slide, "Na Prática 2: Funcionando no App do ChatGPT (Web & Mobile)", "Integrado via Custom GPT Actions (OpenAPI 3.1) e Conector MCP", 10, total_slides)

    add_rect(slide, 0.75, 1.68, 4.35, 4.95, WHITE, True, LINE)
    add_badge(slide, "CHATGPT ACTIONS & @PLUGIN", 1.0, 1.95, 2.5, 0.3, GREEN, WHITE, 9.5)
    add_text(slide, "Especialista HighBond no PC e no Celular", 1.0, 2.4, 3.85, 0.55, 17, NAVY, True, "Aptos Display")
    add_bullet_list(
        slide,
        [
            "Importação automática via URL: .../openapi.json com autenticação Bearer.",
            "Pode ser acionado em qualquer conversa digitando @Especialista HighBond.",
            "Funciona no navegador, no App Desktop e no App de Celular (Android/iOS).",
            "Encadeia automaticamente a busca semântica e a leitura do chunk.",
        ],
        1.0,
        3.15,
        3.85,
        12.5,
        INK,
        gap=0.18,
        bullet_color=GREEN,
    )

    add_screenshot_frame(
        slide,
        x=5.35,
        y=1.68,
        w=7.25,
        h=4.95,
        title_window="ChatGPT App — Talking to rag-highbond-764415736.us-central1.run.app",
        instruction_text="Cole aqui o print do ChatGPT consultando a Action do servidor Cloud Run\n(ou salve a imagem como docs/print_gpt.png e rode gerar_apresentacao.py)",
        candidate_paths=PRINT_GPT,
        accent=GREEN,
    )
    add_footer(slide)

    # =========================================================================
    # SLIDE 11 — DEMONSTRAÇÃO 3: FUNCIONANDO VIA REQUISIÇÃO API / NOTEBOOK
    # =========================================================================
    slide = presentation.slides.add_slide(blank)
    add_header(slide, "Na Prática 3: Requisição Direta via API REST & MCP HTTP", "Consumo direto por scripts Python, Jupyter Notebook (testes.ipynb) e automações", 11, total_slides)

    add_rect(slide, 0.75, 1.68, 4.35, 4.95, CARD_DARK, True)
    add_badge(slide, "EXEMPLO DE REQUISIÇÃO HTTP", 1.0, 1.95, 2.6, 0.3, BLUE, WHITE, 9.5)
    req_code = (
        "POST /buscar HTTP/1.1\n"
        "Host: rag-highbond-764415736\n"
        "      .us-central1.run.app\n"
        "Authorization: Bearer hb-rag-***\n\n"
        "{\n"
        '  "pergunta": "como criar projeto?",\n'
        '  "quantidade": 2\n'
        "}\n\n"
        "# Header de Resposta:\n"
        "HTTP/1.1 200 OK\n"
        "X-Process-Time-Ms: 2.02"
    )
    add_text(slide, req_code, 1.0, 2.42, 3.9, 3.9, 12, RGBColor(215, 232, 248), False, "Consolas")

    add_screenshot_frame(
        slide,
        x=5.35,
        y=1.68,
        w=7.25,
        h=4.95,
        title_window="Jupyter Notebook (testes.ipynb) / Postman — POST /buscar & GET /chunks/{id}",
        instruction_text="Cole aqui o print da requisição via API / Notebook testes.ipynb retornando JSON\n(ou salve a imagem como docs/print_api.png e rode gerar_apresentacao.py)",
        candidate_paths=PRINT_API,
        accent=BLUE,
    )
    add_footer(slide)

    # =========================================================================
    # SLIDE 12 — ENTREGÁVEIS CONCLUÍDOS & PRÓXIMOS PASSOS
    # =========================================================================
    slide = presentation.slides.add_slide(blank)
    add_header(slide, "Resultados Alcançados e Próximos Passos", "Um ecossistema RAG completo, seguro e em produção na nuvem", 12, total_slides)

    add_rect(slide, 0.75, 1.68, 5.75, 4.95, WHITE, True, TEAL, 1.5)
    add_badge(slide, "ENTREGÁVEIS EM PRODUÇÃO", 1.05, 1.95, 2.4, 0.3, TEAL, WHITE, 9.5)
    add_bullet_list(
        slide,
        [
            "369 chunks Markdown estruturados + Índice NumPy (1024d).",
            "Pacote Python modular (rag_highbond) com suíte de testes Pytest.",
            "Servidor Híbrido: API REST (OpenAPI 3.1) + MCP (stdio, /mcp e /sse).",
            "Segurança: Autenticação por API Key, Rate Limiting (30/min) e Cache LRU.",
            "Deploy Serverless ativo no Google Cloud Run com Ollama embarcado.",
        ],
        1.05,
        2.5,
        5.15,
        13.5,
        INK,
        gap=0.16,
        bullet_color=TEAL,
    )

    add_rect(slide, 6.82, 1.68, 5.78, 4.95, WHITE, True, LINE)
    add_badge(slide, "EVOLUÇÕES FUTURAS", 7.12, 1.95, 2.0, 0.3, PURPLE, WHITE, 9.5)
    add_bullet_list(
        slide,
        [
            "Expandir para novas coleções (ex: documentação do Diligent Robots).",
            "Adicionar filtros combinados por domínio/tag e verbo HTTP na busca.",
            "Reindexação incremental automatizada via CI/CD quando o OpenAPI mudar.",
            "Dashboard de telemetria das dúvidas mais frequentes dos usuários.",
        ],
        7.12,
        2.5,
        5.15,
        13.5,
        INK,
        gap=0.16,
        bullet_color=PURPLE,
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
    caminho_gerado = build_presentation()
    print(f"Apresentação gerada em: {caminho_gerado}")
