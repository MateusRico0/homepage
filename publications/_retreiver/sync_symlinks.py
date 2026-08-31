"""Varre as publicações do site e cria/atualiza publications/<username>/
com um link simbólico para cada uma — só isso, nada de front matter ou
listing. É a única fonte da verdade de "quais publicações são dessa
pessoa", usada tanto pelo pre-render (generate_person_bibliographies.py)
quanto por quem quiser depurar sem rodar `quarto render` inteiro:

    python3 sync_symlinks.py

Duas fontes por pessoa:
  - oficiais: publications/group/*.qmd (2+ autores registrados no site) ou
    publications/<solo>/*.qmd (autoria solo — ver SOLO_AUTHOR_FOLDERS)
    cujo author-ids inclui o username dela. Essas duas pastas são o
    acervo canônico do site (arquivos de verdade, sem symlink) — deixaram
    de ser um monte flat em publications/*.qmd pra permitir um
    `contents:` com glob nas listagens principais (publications/index.qmd
    e a home) sem cruzar pelas pastas de symlink por pessoa abaixo.
  - externas: publications/_external/<username>/*.qmd (ver
    sync_from_google_scholar.py) — sempre dela, a pasta já é a chave.
    Para quem está em SOLO_AUTHOR_FOLDERS, os links das externas vão pra
    uma pasta irmã (<username>-external/), nunca dentro da pasta
    canônica — ver sync_person_folder().

Só author-ids de arquivos que já estão em publications/group/ ou
publications/<solo>/ contam como "oficial" — não há mais estágio de
rascunho intermediário (ver render_publication.py: papers com o dono do
site vão direto pra lá).
"""

import os
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
PEOPLE_DIR = ROOT / "people"
PUBLICATIONS_DIR = ROOT / "publications"
EXTERNAL_DIR = PUBLICATIONS_DIR / "_external"

# publications/*.qmd deixou de ser flat: as duas pastas canônicas abaixo
# guardam o acervo oficial (nada de symlink nelas, são os arquivos de
# verdade) — group/ para publicação com 2+ autores registrados no site,
# e uma pasta por pessoa com pelo menos uma publicação SOLO (hoje, só
# mraimundo). Motivo: um `contents:` de listing com glob (`*.qmd`) cruza
# diretório mesmo sem `**` explícito — testado ao vivo — então uma pasta
# flat compartilhada com as pastas de symlink por pessoa (abaixo) sempre
# arriscava listar cada publicação em grupo mais de uma vez. Adicione o
# username aqui se um dia outra pessoa tiver uma publicação solo.
SOLO_AUTHOR_FOLDERS = {"mraimundo"}

AUTHOR_IDS_RE = re.compile(r"^author-ids:\s*\[(.*?)\]", re.MULTILINE)


def official_files() -> list[Path]:
    """publications/group/*.qmd + publications/<solo>/*.qmd (ver
    SOLO_AUTHOR_FOLDERS) — a lista oficial do site."""
    files = []
    for sub in ("group", *SOLO_AUTHOR_FOLDERS):
        folder = PUBLICATIONS_DIR / sub
        if folder.exists():
            files.extend(folder.glob("*.qmd"))
    return sorted(files)


def official_by_person(files: list[Path]) -> dict[str, list[Path]]:
    """{username: [caminho_do_arquivo_oficial, ...]} a partir de author-ids: [...]."""
    by_person: dict[str, list[Path]] = {}
    for path in files:
        ids_match = AUTHOR_IDS_RE.search(path.read_text(encoding="utf-8"))
        if not ids_match:
            continue
        for person_id in (i.strip() for i in ids_match.group(1).split(",")):
            if person_id and (PEOPLE_DIR / f"{person_id}.qmd").exists():
                by_person.setdefault(person_id, []).append(path)
    return by_person


def sync_person_folder(username: str, targets: list[Path]) -> bool:
    """Cria/atualiza publications/<username>/ com um link simbólico para
    cada arquivo em `targets` (caminhos absolutos), removendo links que não
    correspondem mais a nada. Retorna True se a pasta ficou com pelo menos
    um link/arquivo (então a pessoa tem alguma publicação pra mostrar).

    Caso especial — `username` em SOLO_AUTHOR_FOLDERS: essa pasta também é
    o acervo CANÔNICO das publicações solo dessa pessoa (arquivos de
    verdade, não symlink — ver official_files()). Nunca é apagada mesmo
    com `targets` vazio, e a limpeza abaixo nunca remove um `.qmd` real
    (só symlinks e pastas de recurso do Quarto) — só assim dá pra chamar
    esta função tanto pra popular symlinks de publicações externas nessa
    mesma pasta quanto só pra limpeza, sem arriscar apagar o conteúdo
    nativo."""
    person_dir = PUBLICATIONS_DIR / username
    wanted = {target.name: target for target in targets}
    is_canonical_solo = username in SOLO_AUTHOR_FOLDERS

    if not wanted and not is_canonical_solo:
        if person_dir.exists():
            shutil.rmtree(person_dir)
        return False

    person_dir.mkdir(exist_ok=True)
    for existing in person_dir.iterdir():
        if existing.name in wanted:
            continue
        if existing.is_symlink():
            existing.unlink()
        elif existing.is_dir():
            # o próprio Quarto pode deixar uma pasta de recursos (ex.:
            # "<slug>_files/") junto da cópia symlinkada ao renderizar —
            # não é só symlink de arquivo que pode sobrar aqui.
            shutil.rmtree(existing)
        elif is_canonical_solo:
            # Arquivo .qmd real (não symlink) — conteúdo canônico nativo
            # desta pasta. Nunca apagar.
            continue
        else:
            existing.unlink()

    for name, target in wanted.items():
        link = person_dir / name
        relative_target = Path("..") / target.relative_to(PUBLICATIONS_DIR)
        if link.is_symlink() and Path(os.readlink(link)) == relative_target:
            continue
        if link.exists() and not link.is_symlink():
            # Já é o próprio arquivo canônico (ex.: uma publicação solo
            # cujo alvo é ela mesma) — nada a fazer.
            continue
        if link.exists() or link.is_symlink():
            link.unlink()
        link.symlink_to(relative_target)

    return is_canonical_solo or bool(wanted)


def sync_all_symlinks() -> dict[str, bool]:
    """Roda pra todo mundo em people/. Retorna {username: tem_publicacao}."""
    files = official_files()
    official = official_by_person(files)

    result: dict[str, bool] = {}
    for path in PEOPLE_DIR.glob("*.qmd"):
        username = path.stem
        external_dir = EXTERNAL_DIR / username
        external_targets = sorted(external_dir.glob("*.qmd")) if external_dir.exists() else []

        if username in SOLO_AUTHOR_FOLDERS:
            # publications/<username>/ já É o acervo canônico (nativo) das
            # publicações solo dela — symlinkar aqui também as em grupo
            # (que vivem em group/) duplicaria a entrada na listagem
            # principal, que soma group/ + <solo>/ (ver
            # publications/index.qmd e a home). Só limpa symlinks/pastas
            # de recurso obsoletos, sem tocar no conteúdo nativo (ver
            # sync_person_folder). Publicações externas (fora do acervo
            # oficial) vão pra uma pasta irmã (<username>-external/), só
            # usada no perfil da própria pessoa (ver person_bibliography.py).
            has_native = sync_person_folder(username, [])
            has_external = sync_person_folder(f"{username}-external", external_targets)
            result[username] = has_native or has_external
            continue

        targets = list(official.get(username, [])) + external_targets
        result[username] = sync_person_folder(username, targets)

    return result


if __name__ == "__main__":
    result = sync_all_symlinks()
    for username, has_publications in sorted(result.items()):
        if has_publications:
            n = len(list((PUBLICATIONS_DIR / username).glob("*.qmd")))
            print(f"[✔] {username}: {n} link(s) simbólico(s) em publications/{username}/")
    total = sum(1 for v in result.values() if v)
    print(f"\n[✔] {total} pessoa(s) com pelo menos uma publicação vinculada.")
