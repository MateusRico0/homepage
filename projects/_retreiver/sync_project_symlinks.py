"""Varre projects/ e publications/ para manter dois conjuntos de links
simbólicos atualizados — só isso, nada de front matter ou listing (isso é
generate_project_pages.py). Mesma ideia de
publications/_retreiver/sync_symlinks.py, aplicada a projetos:

  1. projects/<username>/ — um link para cada projeto em que essa pessoa
     (alguém de people/) é participante, lido do campo `participants:`
     de cada projects/<slug>.qmd. Usado pela listagem "## Projects" no
     perfil da pessoa.

  2. projects/pubs-by-project/<slug>/ — um link para cada publicação
     (oficial ou externa) cujo campo `projects:` inclui esse slug. SEM "_"
     na frente de propósito: um `listing: contents:` do Quarto ignora
     pastas com "_" na frente do mesmo jeito que o render do projeto
     inteiro ignora — testado ao vivo, a listagem ficava sempre vazia com
     "_pubs-by-project/". Mesma razão pela qual publications/<username>/
     também não tem "_": qualquer pasta usada como fonte de um listing
     precisa estar visível pro Quarto. O efeito colateral aceito é o
     mesmo já documentado para publications/<username>/: cada publicação
     vinculada a um projeto acaba renderizada mais uma vez (cópia via
     link simbólico), mesmo conteúdo em uma URL a mais. Usado pela
     listagem "## Related Publications" na página do projeto.

Uso:
    python3 sync_symlinks.py
"""

import os
import shutil
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
PEOPLE_DIR = ROOT / "people"
PROJECTS_DIR = ROOT / "projects"
PUBLICATIONS_DIR = ROOT / "publications"
PUBS_BY_PROJECT_DIR = PROJECTS_DIR / "pubs-by-project"

PARTICIPANTS_RE = re.compile(r"^participants:\s*\[(.*?)\]", re.MULTILINE)
PROJECTS_FIELD_RE = re.compile(r"^projects:\s*\[(.*?)\]", re.MULTILINE)


def project_files() -> list[Path]:
    return sorted(p for p in PROJECTS_DIR.glob("*.qmd") if p.name != "index.qmd")


def publication_files() -> list[Path]:
    """Oficiais (publications/group/*.qmd + publications/<solo>/*.qmd —
    ver SOLO_AUTHOR_FOLDERS em publications/_retreiver/sync_symlinks.py,
    manter em sincronia com a constante de lá) + externas
    (_external/<username>/*.qmd) — qualquer publicação pode ter um campo
    `projects:`, não só as oficiais."""
    files = []
    for sub in ("group", "mraimundo"):
        folder = PUBLICATIONS_DIR / sub
        if folder.exists():
            files.extend(folder.glob("*.qmd"))
    files += list((PUBLICATIONS_DIR / "_external").glob("*/*.qmd"))
    return sorted(files)


def _field_ids(path: Path, pattern: re.Pattern) -> list[str]:
    match = pattern.search(path.read_text(encoding="utf-8"))
    if not match:
        return []
    return [i.strip() for i in match.group(1).split(",") if i.strip()]


def _sync_folder(folder: Path, targets: list[Path], relative_to: Path) -> bool:
    """Cria/atualiza `folder` com um link simbólico para cada arquivo em
    `targets`, removendo links que não correspondem mais a nada. Retorna
    True se a pasta ficou com pelo menos um link."""
    wanted = {target.name: target for target in targets}

    if not wanted:
        if folder.exists():
            shutil.rmtree(folder)
        return False

    folder.mkdir(parents=True, exist_ok=True)
    for existing in folder.iterdir():
        if existing.name not in wanted:
            # o próprio Quarto pode deixar uma pasta de recursos (ex.:
            # "<slug>_files/") junto da cópia symlinkada ao renderizar —
            # não é só symlink de arquivo que pode sobrar aqui.
            if existing.is_dir() and not existing.is_symlink():
                shutil.rmtree(existing)
            else:
                existing.unlink()

    for name, target in wanted.items():
        link = folder / name
        relative_target = Path(os.path.relpath(target, folder))
        if link.is_symlink() and Path(os.readlink(link)) == relative_target:
            continue
        if link.exists() or link.is_symlink():
            link.unlink()
        link.symlink_to(relative_target)

    return True


def sync_person_project_symlinks() -> dict[str, bool]:
    """projects/<username>/ para cada pessoa de people/ que participa de
    pelo menos um projeto. Retorna {username: tem_projeto}."""
    projects = project_files()
    by_person: dict[str, list[Path]] = {}
    for path in projects:
        for participant_id in _field_ids(path, PARTICIPANTS_RE):
            if (PEOPLE_DIR / f"{participant_id}.qmd").exists():
                by_person.setdefault(participant_id, []).append(path)

    result: dict[str, bool] = {}
    for path in PEOPLE_DIR.glob("*.qmd"):
        username = path.stem
        targets = by_person.get(username, [])
        folder = PROJECTS_DIR / username
        result[username] = _sync_folder(folder, targets, PROJECTS_DIR)
    return result


def sync_project_publication_symlinks() -> dict[str, bool]:
    """projects/pubs-by-project/<slug>/ para cada projeto com pelo menos
    uma publicação vinculada via `projects:`. Retorna {slug: tem_publicacao}."""
    publications = publication_files()
    by_project: dict[str, list[Path]] = {}
    for path in publications:
        for slug in _field_ids(path, PROJECTS_FIELD_RE):
            by_project.setdefault(slug, []).append(path)

    result: dict[str, bool] = {}
    for path in project_files():
        slug = path.stem
        targets = by_project.get(slug, [])
        folder = PUBS_BY_PROJECT_DIR / slug
        result[slug] = _sync_folder(folder, targets, PUBS_BY_PROJECT_DIR)
    return result


if __name__ == "__main__":
    people_result = sync_person_project_symlinks()
    for username, has_projects in sorted(people_result.items()):
        if has_projects:
            n = len(list((PROJECTS_DIR / username).glob("*.qmd")))
            print(f"[✔] {username}: {n} projeto(s) vinculado(s) em projects/{username}/")
    total_people = sum(1 for v in people_result.values() if v)

    project_result = sync_project_publication_symlinks()
    for slug, has_pubs in sorted(project_result.items()):
        if has_pubs:
            n = len(list((PUBS_BY_PROJECT_DIR / slug).glob("*.qmd")))
            print(f"[✔] {slug}: {n} publicação(ões) vinculada(s) em projects/pubs-by-project/{slug}/")
    total_projects = sum(1 for v in project_result.values() if v)

    print(f"\n[✔] {total_people} pessoa(s) com pelo menos um projeto, "
          f"{total_projects} projeto(s) com pelo menos uma publicação vinculada.")
