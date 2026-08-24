"""Gera, para cada aulaNN/ de cada disciplina em teaching/, um parcial
`_lesson-nav.html` injetado no HTML da aula via `include-after-body`
(configurado no front matter de cada aulaNN/index.qmd).

Esse parcial sempre referencia teaching/toc-accordion.js, que
transforma o sumário nativo do Quarto (#TOC, "Nesta página") num painel
de acordeão ("Nesta aula", aberto por padrão). Quando a disciplina tem
2 ou mais aulas, o parcial também inclui um <template> com a lista de
aulas da disciplina (a atual marcada) e teaching/lesson-nav.js, que
move esse <template> para dentro da barra lateral do TOC
(#quarto-margin-sidebar) — toc-accordion.js então também transforma
esse bloco num segundo painel ("Outras aulas", fechado por padrão),
onde abrir um painel fecha o outro.

Roda automaticamente antes de cada `quarto render`/`quarto preview` via
project.pre-render em _quarto.yml. Os `_lesson-nav.html` gerados são
sobrescritos a cada render — não editar à mão.
"""

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TEACHING = ROOT / "teaching"

MARKER = "<!-- gerado por teaching/generate_lesson_nav.py — não editar à mão -->"

AULA_RE = re.compile(r"aula(\d+)$")

# Algumas aulas já escrevem "Aula N" (ou "Aula N:", "Aula N —") como
# prefixo do próprio título (ex.: computing-and-society), outras não
# (ex.: supervised-learning). Removido antes de montar o rótulo da
# navegação, que sempre prepõe "Aula N:" por conta própria — sem isso
# ficaria duplicado ("Aula 1: Aula 1: ...") nas disciplinas que já
# prefixam.
TITLE_AULA_PREFIX_RE = re.compile(r"^\s*aula\s*\d+\s*[:\-—]?\s*", re.IGNORECASE)

TOC_ACCORDION_SCRIPT = '<script src="../../toc-accordion.js"></script>\n'


def strip_aula_prefix(title: str) -> str:
    return TITLE_AULA_PREFIX_RE.sub("", title).strip()


def read_front_matter(qmd_path: Path) -> dict:
    text = qmd_path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    return yaml.safe_load(parts[1]) or {}


def html_output_file(front_matter: dict) -> str:
    fmt = front_matter.get("format")
    if isinstance(fmt, dict):
        html_fmt = fmt.get("html")
        if isinstance(html_fmt, dict) and html_fmt.get("output-file"):
            return html_fmt["output-file"]
    return "index.html"


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def build_lesson_nav_html(lessons, current_index: int) -> str:
    items = []
    for i, (num, title, href) in enumerate(lessons):
        attrs = ' class="active" aria-current="page"' if i == current_index else ""
        items.append(f'<li><a href="{href}"{attrs}>Aula {num}: {esc(title)}</a></li>')
    items_html = "\n      ".join(items)
    return f"""{MARKER}
<template id="lesson-nav-data">
  <nav class="lesson-nav" aria-label="Aulas da disciplina">
    <h5 class="lesson-nav-title">Outras aulas</h5>
    <ol>
      {items_html}
    </ol>
  </nav>
</template>
<script src="../../lesson-nav.js"></script>
{TOC_ACCORDION_SCRIPT}"""


def build_toc_only_html() -> str:
    return f"{MARKER}\n{TOC_ACCORDION_SCRIPT}"


def process_discipline(discipline_dir: Path) -> int:
    aula_dirs = sorted(
        (
            p
            for p in discipline_dir.iterdir()
            if p.is_dir() and AULA_RE.fullmatch(p.name) and (p / "index.qmd").exists()
        ),
        key=lambda p: int(AULA_RE.fullmatch(p.name).group(1)),
    )
    if not aula_dirs:
        return 0

    if len(aula_dirs) == 1:
        (aula_dirs[0] / "_lesson-nav.html").write_text(
            build_toc_only_html(), encoding="utf-8"
        )
        return 1

    lessons = []
    for aula_dir in aula_dirs:
        num = int(AULA_RE.fullmatch(aula_dir.name).group(1))
        fm = read_front_matter(aula_dir / "index.qmd")
        title = strip_aula_prefix(str(fm.get("title") or aula_dir.name))
        href = f"../{aula_dir.name}/{html_output_file(fm)}"
        lessons.append((num, title, href))

    for i, aula_dir in enumerate(aula_dirs):
        nav_html = build_lesson_nav_html(lessons, i)
        (aula_dir / "_lesson-nav.html").write_text(nav_html, encoding="utf-8")

    return len(aula_dirs)


def main():
    disciplines_done = 0
    aulas_done = 0
    for discipline_dir in sorted(TEACHING.iterdir()):
        if not discipline_dir.is_dir() or not (discipline_dir / "index.qmd").exists():
            continue
        n = process_discipline(discipline_dir)
        if n:
            disciplines_done += 1
            aulas_done += n
    print(
        f"[OK] Navegação/acordeão do TOC gerado: {disciplines_done} disciplina(s), "
        f"{aulas_done} aula(s)."
    )


if __name__ == "__main__":
    main()
