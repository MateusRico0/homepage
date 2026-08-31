"""Gera automaticamente a seção "## Publications" (listing nativo do
Quarto) de cada perfil em people/, a partir de publications/<username>/ —
pasta de links simbólicos mantida por publications/_retreiver/sync_symlinks.py
(ver aquele módulo pro que entra nela: oficiais + externas). Esta etapa só
decide SE a seção existe (a pessoa tem ou não pelo menos uma publicação) —
o conteúdo em si é o próprio listing lendo a(s) pasta(s) (ver
person_bibliography.py — pra quem tem publicação solo, o listing soma três
pastas em vez de uma só).

Efeito colateral aceito: uma publicação oficial com N coautores
cadastrados no site acaba renderizada N+1 vezes (a página "oficial" em
publications/group|<solo>/<slug>.html, mais uma cópia via link simbólico
em cada publications/<username>/<slug>.html) — mesmo conteúdo, URLs
diferentes. É o preço de ter um listing nativo por pessoa sem mexer em
texto à mão.

As listagens de Publications na página de Publications
(publications/index.qmd) e na home (index.qmd) NÃO são mais geradas por
este script — apontam direto, como glob estático, pra
publications/group/*.qmd + publications/<solo>/*.qmd (ver
SOLO_AUTHOR_FOLDERS em sync_symlinks.py), então qualquer publicação nova
naquelas duas pastas já aparece sozinha, sem precisar regenerar nada aqui.

Sem rede, sem scraping — só lê o que já está no disco. Roda automaticamente
antes de cada `quarto render`/`quarto preview` via project.pre-render em
_quarto.yml.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "_retreiver"))
from person_bibliography import set_person_publications  # noqa: E402
from sync_symlinks import official_files, sync_all_symlinks  # noqa: E402


def main() -> None:
    has_publications = sync_all_symlinks()
    for username, has_pubs in has_publications.items():
        set_person_publications(username, has_pubs)
    updated = sum(1 for v in has_publications.values() if v)
    total_official = len(official_files())

    print(f"[✔] Listing de publicações atualizado para {updated} pessoa(s), "
          f"{total_official} publicação(ões) oficial(is).")


if __name__ == "__main__":
    main()
