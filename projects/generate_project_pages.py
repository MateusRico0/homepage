"""Gera automaticamente, a partir de projects/*.qmd e publications/*.qmd:

  1. A seção "## Related Publications" de cada projeto (listing nativo do
     Quarto), a partir de projects/pubs-by-project/<slug>/ — pasta de
     links simbólicos mantida por _retreiver/sync_symlinks.py, para toda
     publicação cujo campo `projects:` inclua esse slug.

  2. A seção "## Projects" no perfil de cada pessoa em people/ (listing
     nativo do Quarto), a partir de projects/<username>/ — mesma pasta de
     links simbólicos, para toda pessoa que apareça em `participants:` de
     algum projeto.

Os cartões de "## Participants" de cada projeto NÃO são gerados por este
script — são preenchidos em tempo de render por ../participants.lua, a
partir do campo `participants:` do próprio projeto, do mesmo jeito que
../links.lua preenche ::: {#links} ::: nos perfis de people/: o HTML só
existe no documento renderizado, nunca é escrito de volta no .qmd (ver
participants.lua para a lógica de resolução people/coauthor).

Sem rede, sem scraping — só lê o que já está no disco. Roda
automaticamente antes de cada `quarto render`/`quarto preview` via
project.pre-render em _quarto.yml (uma segunda entrada, depois de
publications/generate_person_bibliographies.py).

Um scholar-id em `participants:` que ainda não foi registrado em
coauthors/coauthors.json aparece com ícone genérico e sem nome — rode
_retreiver/fetch_participant_names.py (esse sim acessa a rede) para
resolver.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "_retreiver"))
from sync_project_symlinks import (  # noqa: E402
    project_files,
    sync_person_project_symlinks,
    sync_project_publication_symlinks,
)

sys.path.insert(0, str(Path(__file__).parent.parent / "publications" / "_retreiver"))
from listing_blocks import set_listing_item  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PEOPLE_DIR = ROOT / "people"

FRONTMATTER_RE = re.compile(r"\A(---\n.*?\n---\n)", re.DOTALL)
RELATED_PUBS_SECTION_RE = re.compile(r"\n## Related Publications\n.*?(?=\n## |\Z)", re.DOTALL)
PROJECTS_SECTION_RE = re.compile(r"\n## Projects\n.*?(?=\n## |\Z)", re.DOTALL)

RELATED_PUBS_LISTING_START = "# related-publications-listing:start (gerado por generate_project_pages.py — não editar)"
RELATED_PUBS_LISTING_END = "# related-publications-listing:end"

PROJECTS_LISTING_START = "# projects-listing:start (gerado por generate_project_pages.py — não editar)"
PROJECTS_LISTING_END = "# projects-listing:end"


def _set_listing_frontmatter(text: str, marker_start: str, marker_end: str, item_yaml: str | None) -> str:
    """A chave `listing:` só pode existir uma vez por página — uma pessoa
    pode ter tanto "## Publications" quanto "## Projects", cada um o seu
    próprio item dentro da MESMA lista (ver listing_blocks.py)."""
    fm_match = FRONTMATTER_RE.match(text)
    if not fm_match:
        return text
    frontmatter = fm_match.group(1)
    rest = text[fm_match.end():]
    new_frontmatter = set_listing_item(frontmatter, marker_start, marker_end, item_yaml)
    return new_frontmatter + rest


_MISSING_BLANK_LINE_RE = re.compile(r"([^\n])\n(## )")


def _ensure_blank_line_before_headings(text: str) -> str:
    """Uma seção substituída por section_re.sub() só troca o próprio trecho
    casado — o "\\n## " de two zero-width lookahead que marca onde ela
    termina nunca é tocado, então se uma seção qualquer (gerada por este
    script ou por person_bibliography.py) tiver sido colada sem uma linha
    em branco antes do "## " seguinte, essa falta persiste (e se
    perpetua: a próxima substituição também só mexe até esse mesmo ponto).
    Normaliza qualquer "texto\\n## " (uma linha só) para "texto\\n\\n## "
    (linha em branco), sem mexer em quem já está correto."""
    return _MISSING_BLANK_LINE_RE.sub(r"\1\n\n\2", text)


def _set_body_section(text: str, section_re: re.Pattern, body: str | None) -> str:
    if body is None:
        new_text = section_re.sub("", text) if section_re.search(text) else text
    elif section_re.search(text):
        new_text = section_re.sub(lambda _m: "\n" + body.rstrip("\n"), text, count=1)
    else:
        new_text = text.rstrip("\n") + "\n\n" + body
    return _ensure_blank_line_before_headings(new_text)


def update_project_related_publications(path: Path, has_publications: bool) -> None:
    slug = path.stem
    text = path.read_text(encoding="utf-8")

    if not has_publications:
        text = _set_body_section(text, RELATED_PUBS_SECTION_RE, None)
        new_text = _set_listing_frontmatter(text, RELATED_PUBS_LISTING_START, RELATED_PUBS_LISTING_END, None)
    else:
        body = "## Related Publications\n\n::: {#related-publications}\n:::\n"
        text = _set_body_section(text, RELATED_PUBS_SECTION_RE, body)
        item = (
            f"  {RELATED_PUBS_LISTING_START}\n"
            "  - id: related-publications\n"
            # Dois globs: o primeiro resolve a partir de projects/<slug>.qmd; o segundo
            # a partir do symlink em projects/<username>/<slug>.qmd (Quarto resolve
            # caminhos relativos à pasta do symlink, não do arquivo original).
            "    contents:\n"
            f'      - "pubs-by-project/{slug}/*.qmd"\n'
            f'      - "../pubs-by-project/{slug}/*.qmd"\n'
            "    type: default\n"
            '    sort: "date desc"\n'
            "    fields: [title, description]\n"
            f"  {RELATED_PUBS_LISTING_END}\n"
        )
        new_text = _set_listing_frontmatter(text, RELATED_PUBS_LISTING_START, RELATED_PUBS_LISTING_END, item)

    if new_text != text:
        path.write_text(new_text, encoding="utf-8")


def update_person_projects(username: str, has_projects: bool) -> None:
    path = PEOPLE_DIR / f"{username}.qmd"
    text = path.read_text(encoding="utf-8")

    if not has_projects:
        text = _set_body_section(text, PROJECTS_SECTION_RE, None)
        new_text = _set_listing_frontmatter(text, PROJECTS_LISTING_START, PROJECTS_LISTING_END, None)
    else:
        body = "## Projects\n\n::: {#projects}\n:::\n"
        text = _set_body_section(text, PROJECTS_SECTION_RE, body)
        item = (
            f"  {PROJECTS_LISTING_START}\n"
            "  - id: projects\n"
            f'    contents: "../projects/{username}/*.qmd"\n'
            "    type: default\n"
            '    sort: "date desc"\n'
            "    fields: [title, description]\n"
            f"  {PROJECTS_LISTING_END}\n"
        )
        new_text = _set_listing_frontmatter(text, PROJECTS_LISTING_START, PROJECTS_LISTING_END, item)

    if new_text != text:
        path.write_text(new_text, encoding="utf-8")


def main() -> None:
    has_pubs_by_project = sync_project_publication_symlinks()
    for path in project_files():
        update_project_related_publications(path, has_pubs_by_project.get(path.stem, False))

    has_projects_by_person = sync_person_project_symlinks()
    for username, has_projects in has_projects_by_person.items():
        update_person_projects(username, has_projects)

    n_people_with_projects = sum(1 for v in has_projects_by_person.values() if v)
    n_projects_with_pubs = sum(1 for v in has_pubs_by_project.values() if v)
    print(
        f"[✔] Páginas de projetos atualizadas: {n_people_with_projects} pessoa(s) com projetos no perfil, "
        f"{n_projects_with_pubs} projeto(s) com publicações relacionadas."
    )


if __name__ == "__main__":
    main()
