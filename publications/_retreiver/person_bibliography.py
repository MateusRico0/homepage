"""Mantém a seção "## Publications" no perfil de uma pessoa (people/<username>.qmd)
como um único listing NATIVO do Quarto (cards, igual ::: {#teaching} ::: da
home), apontando pra publications/<username>/ — uma pasta cheia de links
simbólicos que generate_person_bibliographies.py mantém (ver aquele módulo
para o que entra nela: oficiais + externas).

Como o `contents:` só precisa apontar pra essa pasta (o conteúdo dela é que
muda a cada render, não o caminho), o item do listing no front matter é
praticamente estático — só aparece ou desaparece conforme a pessoa tem ou
não pelo menos uma publicação. Tem que ser um glob com `*.qmd` no fim
(`"../publications/username/*.qmd"`), não a pasta pura — o Quarto não
segue links simbólicos ao escanear um `contents:` de pasta, só quando o
padrão tem um glob explícito.

Front matter da pessoa (bloco marcado por comentário YAML, seguro de
atualizar de novo sem mexer no resto do front matter escrito à mão). A
chave `listing:` é COMPARTILHADA com projects/generate_project_pages.py
(uma pessoa pode ter "## Publications" e "## Projects" ao mesmo tempo, e o
Quarto só aceita uma chave `listing:` por página — cada um é um item da
mesma lista, ver publications/_retreiver/listing_blocks.py):

    ---
    title: "..."
    group: "..."
    listing:
      # publications-listing:start (gerado por generate_person_bibliographies.py — não editar)
      - id: publications
        contents: "../publications/username/*.qmd"
        type: default
        sort: "date desc"
        fields: [title, description]
      # publications-listing:end
    filters:
      - ../band-sections.lua
    ---

Corpo da pessoa (heading + div que o Quarto preenche com o listing acima):

    ## Publications

    ::: {#publications}
    :::

Se a pessoa não tem nenhuma publicação, a seção inteira — incluindo o item
em `listing:` (e a própria chave, se não sobrar mais nenhum item) — é
removida.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
PEOPLE_DIR = ROOT / "people"

sys.path.insert(0, str(Path(__file__).parent))
from listing_blocks import set_listing_item  # noqa: E402
from sync_symlinks import SOLO_AUTHOR_FOLDERS  # noqa: E402

LISTING_START = "# publications-listing:start (gerado por generate_person_bibliographies.py — não editar)"
LISTING_END = "# publications-listing:end"

FRONTMATTER_RE = re.compile(r"\A(---\n.*?\n---\n)", re.DOTALL)

SECTION_RE = re.compile(r"\n## Publications\n.*?(?=\n## |\Z)", re.DOTALL)

SECTION_BODY = "## Publications\n\n::: {#publications}\n:::\n"

_MISSING_BLANK_LINE_RE = re.compile(r"([^\n])\n(## )")


def _ensure_blank_line_before_headings(text: str) -> str:
    """section_re.sub() só troca o trecho casado — o "\\n## " que marca onde
    a seção termina (lookahead, não consumido) nunca é tocado, então se essa
    fronteira já estiver sem uma linha em branco (por qualquer motivo:
    edição manual, outra seção gerada por outro script), a falta persiste a
    cada substituição seguinte. Normaliza "texto\\n## " para "texto\\n\\n## "
    sem mexer em quem já está correto."""
    return _MISSING_BLANK_LINE_RE.sub(r"\1\n\n\2", text)


def _listing_item(person_slug: str) -> str:
    if person_slug in SOLO_AUTHOR_FOLDERS:
        # Pra quem tem publicação solo, a própria pasta homônima só guarda
        # o acervo canônico nativo (solo) + externas — as publicações em
        # grupo (group/) e as externas (numa pasta irmã, ver
        # sync_symlinks.py) ficam de fora dela de propósito, pra não
        # duplicar entradas na listagem principal (publications/index.qmd
        # e a home, que somam group/ + <solo>/). O perfil da pessoa soma
        # as três pastas pra mostrar tudo.
        contents = (
            f'["../publications/{person_slug}/*.qmd", '
            '"../publications/group/*.qmd", '
            f'"../publications/{person_slug}-external/*.qmd"]'
        )
    else:
        contents = f'"../publications/{person_slug}/*.qmd"'
    return (
        f"  {LISTING_START}\n"
        "  - id: publications\n"
        f"    contents: {contents}\n"
        "    type: default\n"
        '    sort: "date desc"\n'
        "    fields: [title, description]\n"
        f"  {LISTING_END}\n"
    )


def _set_listing_block(text: str, person_slug: str, has_publications: bool) -> str:
    """Front matter é YAML, não o corpo — tratado à parte, sempre dentro do
    trecho isolado por FRONTMATTER_RE, pra nunca arriscar mexer num "---"
    que seja na verdade um separador horizontal escrito à mão no corpo."""
    fm_match = FRONTMATTER_RE.match(text)
    if not fm_match:
        return text
    frontmatter = fm_match.group(1)
    rest = text[fm_match.end():]

    item = _listing_item(person_slug) if has_publications else None
    new_frontmatter = set_listing_item(frontmatter, LISTING_START, LISTING_END, item)

    return new_frontmatter + rest


def set_person_publications(person_slug: str, has_publications: bool) -> Path:
    """has_publications: se publications/<person_slug>/ (mantida por
    generate_person_bibliographies.py) tem pelo menos um link simbólico."""
    path = PEOPLE_DIR / f"{person_slug}.qmd"
    if not path.exists():
        raise FileNotFoundError(f"Perfil não encontrado: {path}")

    original = path.read_text(encoding="utf-8")
    text = original

    if not has_publications:
        text = SECTION_RE.sub("", text) if SECTION_RE.search(text) else text
        text = _set_listing_block(text, person_slug, False)
        text = _ensure_blank_line_before_headings(text)
        if text != original:
            path.write_text(text, encoding="utf-8")
        return path

    section = "\n" + SECTION_BODY
    if SECTION_RE.search(text):
        text = SECTION_RE.sub(lambda _m: section.rstrip("\n"), text, count=1)
    else:
        text = text.rstrip("\n") + "\n" + section

    text = _set_listing_block(text, person_slug, True)
    text = _ensure_blank_line_before_headings(text)
    # Escrever só quando o conteúdo muda de verdade (não a cada render,
    # incondicionalmente) é essencial, não só uma otimização: um
    # pre-render script que sempre grava (mesmo com o mesmo conteúdo)
    # muda o mtime de todo people/*.qmd em TODO render — e qualquer
    # coisa que observe o projeto por mtime (ex.: preview-watch.py) vê
    # isso como "mudança", dispara outro render, que grava de novo, que
    # dispara outro... Foi exatamente essa a causa de um loop infinito
    # real (~4h30 rerenderizando sozinho) já visto em produção aqui.
    if text != original:
        path.write_text(text, encoding="utf-8")
    return path
