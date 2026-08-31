"""Lógica compartilhada para gerar um .qmd de publicação a partir de
TEMPLATE.qmd, usada tanto por fetch_semantic_scholar.py quanto por
sync_from_google_scholar.py — a fonte dos dados muda, o formato de saída
(e a regra de quando incluir fotos de autores) é sempre o mesmo.
"""

import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from resolve_authors import (  # noqa: E402
    _name_key,
    backfill_scholar_id_if_person,
    find_known_scholar_id,
    render_authors_block,
    resolve_author_ids,
)
from sync_symlinks import SOLO_AUTHOR_FOLDERS  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent.parent
PUBLICATIONS_DIR = ROOT / "publications"
# "_external" com underscore: convenção do próprio Quarto pra ignorar
# arquivos/pastas inteiramente (nunca renderizados, nunca aparecem em
# nenhum listing) — exatamente o que se quer pro estoque bruto de
# publicações sem o dono do site (ver render_publication(), ramo
# involves_owner=False). O listing de cada pessoa não lê daqui diretamente
# — ver generate_person_bibliographies.py, que cria links simbólicos em
# publications/<username>/ apontando pra cá, já que só um arquivo dentro
# de uma pasta SEM underscore é de fato renderizado pelo Quarto.
#
# Por decisão de Marcos, papers com ele como autor NÃO passam por um
# estágio de rascunho — vão direto pra publications/ (PUBLICATIONS_DIR)
# assim que o scraper os encontra, sem revisão manual antes de ficarem
# visíveis no site.
EXTERNAL_DIR = PUBLICATIONS_DIR / "_external"

# As duas pastas canônicas do acervo oficial (ver SOLO_AUTHOR_FOLDERS em
# sync_symlinks.py para o porquê): group/ pra publicação com 2+ autores
# registrados no site, <solo>/ pra autoria solo dessa pessoa.
CANONICAL_SUBDIRS = ("group", *SOLO_AUTHOR_FOLDERS)

TEMPLATE = (Path(__file__).parent / "TEMPLATE.qmd").read_text(encoding="utf-8")


def slugify(text: str) -> str:
    n = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    n = n.lower().replace(".", "").replace("'", "")
    n = re.sub(r"[^a-z0-9]+", "-", n)
    return n.strip("-")[:60].rstrip("-")


def existing_titles() -> set[str]:
    """Títulos (minúsculos) já presentes no acervo oficial (ver
    CANONICAL_SUBDIRS) — usado para não recriar um artigo que já foi
    migrado/cadastrado manualmente."""
    titles = set()
    for sub in CANONICAL_SUBDIRS:
        folder = PUBLICATIONS_DIR / sub
        if not folder.exists():
            continue
        for path in folder.glob("*.qmd"):
            match = re.search(r'^title:\s*"([^"]+)"', path.read_text(encoding="utf-8"), re.MULTILINE)
            if match:
                titles.add(match.group(1).strip().lower())
    return titles


def render_publication(
    title: str,
    authors: list[str],
    date_iso: str,
    year: str,
    venue: str,
    abstract: str | None,
    source_url: str | None,
    owner_name: str | None = "M. M. Raimundo",
    coauthor_scholar_map: dict | None = None,
) -> str:
    """Preenche TEMPLATE.qmd com os dados de um artigo, independente da
    fonte (Semantic Scholar, Google Scholar, ou preenchido manualmente).

    owner_name: só decide se a seção "## Authors" (com fotos) é incluída —
    por pedido explícito, só pra papers em que o dono do site (Marcos)
    está envolvido (ver resolve_authors.py pra como cada autor vira
    perfil da equipe, coautor confirmado pelo Scholar, ou ícone genérico).

    coauthor_scholar_map: {_name_key(nome): {"scholar_id", "photo_url"}},
    vindo da caixa "Coautores" do perfil sincronizado nesta rodada (ver
    google_scholar_scraper.scrape_author_profile) — usado pra popular
    scholar-ids: [...] em TODA publicação (oficial ou externa), pedido
    explícito pra sempre ter esse vínculo registrado e nunca precisar
    "baixar o paper de novo" só pra redescobrir quem é quem.
    """
    authors_str = ", ".join(authors)
    coauthor_scholar_map = coauthor_scholar_map or {}

    text = TEMPLATE
    text = text.replace('title: "{{TITLE}}"', f'title: "{title}"')
    text = text.replace('date: "{{DATE_ISO}}"', f'date: "{date_iso}"')
    text = text.replace("{{AUTHORS_COMMA_SEPARATED}}", authors_str)
    text = text.replace("{{YEAR}}", year)
    text = text.replace("{{VENUE}}", venue)
    # categorias não vêm de nenhuma das fontes automáticas — omitir a linha
    # inteira em vez de adivinhar
    text = re.sub(r"\ncategories: \[.*?\]\n", "\n", text)

    # Comparação por sobrenome+iniciais (_name_key), não substring exata —
    # citações abreviam nomes de formas diferentes por fonte ("M. M.
    # Raimundo" no Semantic Scholar, "Marcos Medeiros Raimundo" no Google
    # Scholar), e substring simples deixa passar praticamente todo mundo.
    owner_key = _name_key(owner_name) if owner_name else None
    involves_owner = owner_key is not None and any(_name_key(a) == owner_key for a in authors)

    if involves_owner:
        author_tuples = [
            (name, *(
                (coauthor_scholar_map[_name_key(name)]["scholar_id"], coauthor_scholar_map[_name_key(name)]["photo_url"])
                if _name_key(name) in coauthor_scholar_map else (None, None)
            ))
            for name in authors
        ]
        resolved = resolve_author_ids(author_tuples)
        # só "people" tem slug de verdade no site — "coauthor" (scholar_id,
        # sem página local) e "unknown" (sem identidade nenhuma) ficam de
        # fora de author-ids, que é usado por sync_symlinks.py pra saber em
        # qual publications/<username>/ colocar o link simbólico
        author_ids = ", ".join(p["id"] for p in resolved if p["source"] == "people")
        authors_block = render_authors_block(resolved)
        text = text.replace("{{AUTHOR_ID_1}}, {{AUTHOR_ID_2}}", author_ids)
        text = text.replace("{{AUTHORS_WITH_PHOTOS}}", authors_block)
        scholar_ids = [p["scholar_id"] for p in resolved if p.get("scholar_id")]
    else:
        # sem o dono do site no paper: nada de author-ids/fotos — mas
        # ainda registra os scholar-ids que já conhecemos
        text = re.sub(r"\nauthor-ids: \[.*?\]\n", "\n", text)
        text = re.sub(r"\n## Authors\n\n\{\{AUTHORS_WITH_PHOTOS\}\}\n", "\n", text)
        scholar_ids = []
        for name in authors:
            fresh = coauthor_scholar_map.get(_name_key(name), {}).get("scholar_id")
            if fresh:
                backfill_scholar_id_if_person(name, fresh)
            found = fresh or find_known_scholar_id(name)
            if found:
                scholar_ids.append(found)

    if scholar_ids:
        text = text.replace("{{SCHOLAR_ID_1}}, {{SCHOLAR_ID_2}}", ", ".join(dict.fromkeys(scholar_ids)))
    else:
        text = re.sub(r"\nscholar-ids: \[.*?\]\n", "\n", text)

    abstract = (abstract or "").strip()
    if abstract:
        text = text.replace("{{ABSTRACT}}", abstract)
    else:
        text = re.sub(r"\n## Abstract\n\n\{\{ABSTRACT\}\}\n", "\n", text)

    if source_url:
        text = text.replace("{{SOURCE_URL}}", source_url)
    else:
        # sem URL nenhuma pra linkar: remove o item da lista e o
        # placeholder inteiros, não só o valor (links.lua é global — ver
        # _quarto.yml — não precisa remover nenhum filters: aqui)
        text = re.sub(r'\n  - scholar: "\{\{SOURCE_URL\}\}"', "", text)
        text = re.sub(r"\nlinks:\n\n", "\n", text)
        text = re.sub(r"\n::: \{#links\}\n:::\n", "\n", text)

    return text


def find_existing_publication(title_key: str, person_slug: str) -> Path | None:
    """Acha o arquivo (oficial ou externo dessa pessoa) cujo título bate
    com title_key (já em minúsculas) — usado por backfill_scholar_ids pra
    atualizar um arquivo já existente sem precisar re-raspar nada dele."""
    for sub in CANONICAL_SUBDIRS:
        folder = PUBLICATIONS_DIR / sub
        if not folder.exists():
            continue
        for path in folder.glob("*.qmd"):
            match = re.search(r'^title:\s*"([^"]+)"', path.read_text(encoding="utf-8"), re.MULTILINE)
            if match and match.group(1).strip().lower() == title_key:
                return path
    directory = EXTERNAL_DIR / person_slug
    if directory.exists():
        for path in directory.glob("*.qmd"):
            match = re.search(r'^title:\s*"([^"]+)"', path.read_text(encoding="utf-8"), re.MULTILINE)
            if match and match.group(1).strip().lower() == title_key:
                return path
    return None


AUTHOR_FIELD_RE = re.compile(r'^author:\s*"([^"]*)"', re.MULTILINE)
SCHOLAR_IDS_FIELD_RE = re.compile(r"^scholar-ids:\s*\[(.*?)\]", re.MULTILINE)
_ANCHOR_FOR_SCHOLAR_IDS_RE = re.compile(r"(^author-ids:\s*\[.*?\]\n|^author:\s*\".*?\"\n)", re.MULTILINE)
DATE_FIELD_RE = re.compile(r'^date:\s*"[^"]*"', re.MULTILINE)
DESCRIPTION_FIELD_RE = re.compile(r'^description:\s*"[^"]*"', re.MULTILINE)


def looks_like_preprint(path: Path) -> bool:
    """Heurística simples: título/veículo ainda mencionam "preprint" ou
    "arxiv" em algum lugar do arquivo — usado pra decidir se vale a pena
    conferir de novo se o artigo já foi publicado de verdade (ver
    update_venue_if_published). Papers com veículo "definitivo" (revista,
    conferência) nunca são reabertos de novo, só os que ainda parecem
    provisórios."""
    text = path.read_text(encoding="utf-8").lower()
    return "preprint" in text or "arxiv" in text


def update_venue_if_published(path: Path, details: dict) -> bool:
    """Pra um paper que looks_like_preprint(): se os detalhes frescos
    trouxerem um veículo que não é mais preprint/arXiv, atualiza date: e
    description: no arquivo (o caso de "publicou no periódico depois").
    Não mexe em mais nada (abstract, autores) — só os dois campos que
    mudam quando um preprint vira publicação de verdade. Retorna True se
    atualizou algo."""
    new_venue = details.get("venue")
    if not new_venue or re.search(r"preprint|arxiv", new_venue, re.IGNORECASE):
        return False

    text = path.read_text(encoding="utf-8")
    author_match = AUTHOR_FIELD_RE.search(text)
    if not author_match:
        return False

    year = details.get("year") or ""
    new_description = f"{author_match.group(1)} ({year}). {new_venue}."

    new_text = text
    if details.get("date_iso"):
        new_text = DATE_FIELD_RE.sub(lambda _m: f'date: "{details["date_iso"]}"', new_text, count=1)
    new_text = DESCRIPTION_FIELD_RE.sub(lambda _m: f'description: "{new_description}"', new_text, count=1)

    if new_text == text:
        return False
    path.write_text(new_text, encoding="utf-8")
    return True


def backfill_scholar_ids(path: Path, coauthor_scholar_map: dict) -> bool:
    """Atualiza/cria scholar-ids: num arquivo JÁ existente usando só o que
    já está nele (author:) + o mapa de coautores desta rodada — sem
    reabrir a página de citação no Scholar. Retorna True se mudou algo."""
    text = path.read_text(encoding="utf-8")
    author_match = AUTHOR_FIELD_RE.search(text)
    if not author_match:
        return False
    authors = [a.strip() for a in author_match.group(1).split(",") if a.strip()]

    existing_match = SCHOLAR_IDS_FIELD_RE.search(text)
    existing_ids = [i.strip() for i in existing_match.group(1).split(",") if i.strip()] if existing_match else []

    new_ids = list(existing_ids)
    for name in authors:
        found = coauthor_scholar_map.get(_name_key(name), {}).get("scholar_id") or find_known_scholar_id(name)
        if found and found not in new_ids:
            new_ids.append(found)

    if new_ids == existing_ids:
        return False

    ids_line = f"scholar-ids: [{', '.join(new_ids)}]\n"
    if existing_match:
        new_text = SCHOLAR_IDS_FIELD_RE.sub(lambda _m: ids_line.rstrip("\n"), text, count=1)
    else:
        anchor = _ANCHOR_FOR_SCHOLAR_IDS_RE.search(text)
        if not anchor:
            return False
        new_text = text[:anchor.end()] + ids_line + text[anchor.end():]

    path.write_text(new_text, encoding="utf-8")
    return True


AUTHOR_IDS_LINE_RE = re.compile(r"^author-ids:\s*\[(.*?)\]", re.MULTILINE)


def _canonical_folder_for(rendered_text: str) -> Path:
    """group/ pra publicação com 2+ autores registrados no site, ou a
    pasta homônima da pessoa se ela for a única autora registrada (ver
    SOLO_AUTHOR_FOLDERS) — senão (nenhum author-ids, ou o único autor não
    está na lista de quem já tem publicação solo) cai em group/ também,
    já que toda publicação oficial envolve o dono do site."""
    match = AUTHOR_IDS_LINE_RE.search(rendered_text)
    author_ids = [a.strip() for a in match.group(1).split(",") if a.strip()] if match else []
    if len(author_ids) == 1 and author_ids[0] in SOLO_AUTHOR_FOLDERS:
        return PUBLICATIONS_DIR / author_ids[0]
    return PUBLICATIONS_DIR / "group"


def write_publication(slug: str, rendered_text: str) -> Path:
    folder = _canonical_folder_for(rendered_text)
    folder.mkdir(parents=True, exist_ok=True)
    out_path = folder / f"{slug}.qmd"
    out_path.write_text(rendered_text, encoding="utf-8")
    return out_path


def existing_external_titles(person_slug: str) -> set[str]:
    """Títulos já presentes em publications/_external/<person_slug>/*.qmd —
    usado pra não reprocessar/reescrever um artigo sem o dono do site que já
    foi encontrado numa rodada anterior do scraper para essa pessoa."""
    titles = set()
    directory = EXTERNAL_DIR / person_slug
    if not directory.exists():
        return titles
    for path in directory.glob("*.qmd"):
        match = re.search(r'^title:\s*"([^"]+)"', path.read_text(encoding="utf-8"), re.MULTILINE)
        if match:
            titles.add(match.group(1).strip().lower())
    return titles


def write_external_publication(person_slug: str, slug: str, rendered_text: str) -> Path:
    directory = EXTERNAL_DIR / person_slug
    directory.mkdir(parents=True, exist_ok=True)
    out_path = directory / f"{slug}.qmd"
    out_path.write_text(rendered_text, encoding="utf-8")
    return out_path
