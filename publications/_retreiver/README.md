# publications/_retreiver/

Ferramentas que mantêm a lista de publicações e as fotos de autores do
site atualizadas automaticamente a partir do Google Scholar. Nada nesta
pasta é renderizado pelo site — o `_` no nome faz o Quarto ignorá-la
inteiramente, a mesma convenção usada em `publications/_external/` (ver
abaixo).

Requer Playwright (`.venv/` aqui já tem `playwright` + `beautifulsoup4`;
recriar com `pip install playwright && playwright install chromium` se
necessário).

## Princípios de projeto

- **Sem estágio de revisão manual.** Um paper em que o dono do site é
  autor é escrito direto em `publications/` (oficial, visível no site)
  assim que o scraper o encontra — não existe pasta de rascunho pra
  promover depois. Ajustes (abstract truncado, nome de autor na forma
  abreviada da citação) são feitos editando o arquivo já publicado.
- **Sem página de perfil por coautor externo.** Um autor que não é da
  equipe nunca ganha um `.qmd` próprio. Em vez disso, autores externos são
  resolvidos contra um cache compartilhado de foto/ID (`coauthors/`, ver
  "Resolução de autores" abaixo) ou caem num ícone genérico.
- **Google Scholar é a fonte de dados principal**, acessado via uma sessão
  normal de navegador com Playwright — sem proxy, VPN ou rotação de IP. O
  Scholar não tem API pública, então isso significa carregar as páginas
  HTML dele como um usuário comum carregaria, o que traz o risco real e
  inerente de bloqueio/CAPTCHA temporário. `fetch_semantic_scholar.py` (a
  API oficial do Semantic Scholar) fica disponível como alternativa de
  menor risco pra conferir/comparar dados.
- **Minimizar requisições repetidas ao Scholar.** Uma vez que um dado é
  conhecido (o Scholar ID de um autor, o veículo de um paper), ele é
  guardado em disco e nunca re-buscado, a não ser que haja um motivo
  específico pra esperar que tenha mudado (ver "Atualizando um preprint
  depois de publicado").

## Pastas

| Pasta | Conteúdo | Aparece no site? |
|---|---|---|
| `publications/group/*.qmd` | a lista **oficial** com 2+ autores registrados no site (arquivos de verdade, não symlink) | Sim — página de Publications, home, e o listing de cada coautor |
| `publications/<solo>/*.qmd` (ex.: `mraimundo/`, ver `SOLO_AUTHOR_FOLDERS` em `sync_symlinks.py`) | a lista **oficial** de autoria solo dessa pessoa (arquivos de verdade, não symlink) | Sim — mesmos três lugares acima |
| `publications/_external/<username>/` | o resto das publicações de uma pessoa específica (sem o dono do site) | Não diretamente (prefixo `_`), mas ver `publications/<username>/` abaixo |
| `publications/<username>/` (uma por pessoa SEM publicação solo, gerada automaticamente) | links simbólicos pras publicações dessa pessoa (`group/` + as próprias de `_external/<username>/`) | **Sim** — é isso que faz o listing nativo do perfil dela funcionar |
| `publications/<solo>-external/` (ex.: `mraimundo-external/`) | o equivalente de `publications/<username>/` acima, mas pra quem tem pasta canônica solo — só os links das externas, nunca dos oficiais (que já vivem nativamente em `<solo>/` e `group/`) | **Sim** — só no perfil dessa pessoa, que soma as três pastas (ver `person_bibliography.py`) |
| `coauthors/` | `coauthors.json` (scholar_id → foto em cache), os arquivos de foto, e `not_found.json` (nomes buscados sem resultado) | Não é uma pasta do site — um cache de dados/imagens lido por `render_authors_block` |

`publications/*.qmd` deixou de ser um monte flat: um `contents:` de
listing com glob cruza diretório mesmo sem `**` explícito (testado ao
vivo), então uma pasta oficial compartilhada com as pastas de symlink por
pessoa arriscava sempre listar cada publicação em grupo mais de uma vez
nas duas páginas principais. As duas pastas canônicas acima (`group/` e
`<solo>/`) resolvem isso: `publications/index.qmd` e a home apontam
direto pra elas com um glob estático (`publications/group/*.qmd` +
`publications/<solo>/*.qmd`), sem precisar de uma lista `contents:`
regenerada a cada render.

`username` é o padrão usado em todo `people/*.qmd`: iniciais de cada parte
do nome exceto a última, mais o sobrenome, minúsculo, sem separador (ex.:
"Giovani Valdrighi" → `gvaldrighi`). O dono do site é a única exceção
deliberada, `mraimundo` (só a inicial do primeiro nome + sobrenome) em vez
da forma de duas iniciais que a regra normalmente produziria.

## Pipeline

1. **`extract_scholar_links.py`** — só leitura local, sem rede. Varre
   `people/*.qmd` e devolve `{username: {name, scholar_id, scholar_url}}`
   pra quem tem Google Scholar cadastrado no perfil (campo `scholar-id:`
   no front matter, com fallback pra ler o link dentro de
   `.profile-links` em perfis anteriores a esse campo existir).

2. **`google_scholar_scraper.py`** — as funções de raspagem de fato
   (Playwright + BeautifulSoup):
   - `scrape_author_profile` — publicações recentes de um perfil e a
     caixa "Coautores" da barra lateral.
   - `scrape_paper_details` — resumo, autores, data, veículo a partir da
     página de citação de um artigo.
   - `search_coauthor` — busca ancorada pra um coautor sem confirmação
     prévia (ver "Resolução de autores" abaixo).
   - `human_delay` — pausas aleatórias entre requisições.

3. **`sync_from_google_scholar.py`** — orquestração de ponta a ponta:

       python3 sync_from_google_scholar.py --person gvaldrighi

   `--person` é sempre um **username** (nome de arquivo em `people/`).
   Abre o perfil dessa pessoa, pula publicações já cadastradas (oficiais
   ou externas, por título — ainda que `scholar-ids:` do arquivo existente
   seja atualizado, ver abaixo), e para cada uma nova: escreve direto em
   `publications/group/<slug>.qmd` (2+ autores registrados) ou
   `publications/<solo>/<slug>.qmd` (autoria solo, ver
   `_canonical_folder_for` em `render_publication.py`) se o dono do site é
   coautor, senão em `publications/_external/<username>/<slug>.qmd`.

4. **`resolve_authors.py`** — resolve cada autor de um paper oficial pra
   um link + imagem e mantém o cache em `coauthors/`. O único acesso à
   rede aqui é baixar a foto de um coautor confirmado; autores sem
   confirmação ganham um ícone genérico sem nenhuma requisição. A
   correspondência de nomes usa sobrenome + iniciais (`_name_key`), não
   string exata, porque citações abreviam nomes de formas inconsistentes
   — incluindo iniciais grudadas sem ponto ("SB" → {s, b}) e partículas
   comuns ("de", "da"...) excluídas do conjunto de iniciais.
   `_KNOWN_ALIASES` cobre os poucos casos que a heurística não resolve
   sozinha (sobrenome truncado ou expandido entre a citação e o perfil
   real).

5. **`render_publication.py`** — preenche `TEMPLATE.qmd`, compartilhado
   pelos dois fetchers. Define `PUBLICATIONS_DIR` e `CANONICAL_SUBDIRS`
   (`group/` + `SOLO_AUTHOR_FOLDERS`, ver `sync_symlinks.py`) e
   `EXTERNAL_DIR` (`_external/`). `_canonical_folder_for` decide em qual
   das duas pastas canônicas uma publicação nova é escrita, a partir do
   `author-ids:` já preenchido no texto renderizado. Também tem
   `backfill_scholar_ids`/`find_existing_publication` (atualiza
   `scholar-ids:` num arquivo já existente sem reabrir a página de
   citação) e `looks_like_preprint`/`update_venue_if_published` (ver
   "Atualizando um preprint" abaixo).

6. **`sync_symlinks.py`** — a fonte única da verdade de "quais
   publicações são de quem": varre `publications/group/*.qmd` +
   `publications/<solo>/*.qmd` (`author-ids:`) e
   `publications/_external/<username>/*.qmd`, e cria/atualiza
   `publications/<username>/` (ou, pra quem está em
   `SOLO_AUTHOR_FOLDERS`, só `publications/<username>-external/`, já que a
   pasta homônima é canônica e nunca ganha symlink) com um link simbólico
   pra cada correspondência, removendo os que não valem mais. Roda
   sozinho, sem precisar de um `quarto render` completo:

       python3 sync_symlinks.py

7. **`refresh_coauthors.py`** — pré-popula o cache de coautores pra todo
   perfil cadastrado de uma vez, sem tocar em publicações (ver abaixo).

8. **`fetch_semantic_scholar.py`** — a alternativa via API do Semantic
   Scholar.

9. **`TEMPLATE.qmd`** — o template que `render_publication.py` preenche.

## Resolução de autores

Um autor de um paper oficial que **não** é da equipe é resolvido por
`resolve_authors.resolve_author_ids` para um de três resultados:

1. **Confirmado pela caixa "Coautores"** — o Google Scholar já lista essa
   pessoa na barra lateral de um perfil sincronizado nesta rodada
   (`id="gsc_rsb_co"`, extraído por
   `google_scholar_scraper.scrape_author_profile`). É a única parte do
   Scholar que liga um nome a um ID de perfil **e** uma foto real — a
   lista de autores de uma página de citação, em contraste, é texto puro,
   sem nenhum dos dois.
2. **Achado por busca ancorada** — se não veio pela caixa "Coautores",
   `sync_from_google_scholar.py` chama `search_coauthor`, que consulta a
   busca geral de artigos do Scholar
   (`/scholar?q=author:"Alvo" author:"Âncora"`) por um paper coautorado
   pelos dois nomes, e lê o link do nome abreviado do autor alvo (ex.: "J
   Poco") pra extrair o ID de perfil. A **âncora** — a pessoa cujo perfil
   está sendo sincronizado — é o que torna isso seguro: como ela é uma
   coautora confirmada de verdade do artigo, exigir os dois nomes na busca
   praticamente elimina o risco de achar um homônimo. Uma busca solta,
   sem âncora, não tem essa garantia (ver nota abaixo) e por isso não é
   usada.
3. **Sem confirmação nenhuma** — um ícone de pessoa genérico
   (`bi-person-circle`, igual pra todo mundo nesse caso) cujo cartão linka
   pra uma busca comum do Google pelo nome da pessoa. Nomes sem resultado
   ficam registrados em `coauthors/not_found.json` pra a busca não se
   repetir a cada sincronização seguinte.

Nos casos 1 e 2, a foto real é baixada uma vez pra
`coauthors/<scholar_id>.jpg` e registrada em `coauthors/coauthors.json`
como `{scholar_id: {"name", "photo"}}`; o cartão da pessoa na seção
"## Authors" linka direto pro Scholar dela.

**Por que a busca precisa ser ancorada:** a própria página de busca de
autor do Scholar (`view_op=search_authors`) redireciona pra uma tela de
login do Google mesmo com uma sessão "aquecida", tornando-a inutilizável
sem autenticação real. Uma busca comum do Google
(`"<nome>" google scholar`) evita essa tela, mas não é confiável — um
teste de controle contra um caso conhecido ("Jorge Poco", cujo ID real
`S_88vX4AAAAJ` já estava confirmado pela caixa de coautores) trouxe o ID
de uma pessoa diferente no primeiro resultado. Exigir um segundo nome já
conhecido na busca (o operador `author:` do próprio Scholar aceita
múltiplas cláusulas) resolveu esse caso específico corretamente, já que
exige um artigo que as duas pessoas realmente escreveram juntas. Não é
infalível — duas duplas de coautoria que sejam *ambas* homônimas uma da
outra ainda colidiriam — mas elimina a ambiguidade de nome único ao custo
de uma requisição a mais ao Scholar por autor sem confirmação.

**`refresh_coauthors.py`** coleta só a caixa "Coautores" (sem raspar
publicações, sem busca ancorada) de todo perfil com `scholar-id`
cadastrado, de uma vez — mais barato que uma sincronização completa
quando o objetivo é só manter `coauthors.json` populado, inclusive pra
quem ainda não teve as próprias publicações sincronizadas:

    python3 refresh_coauthors.py

## Campo `scholar-ids:`

Toda publicação (oficial ou externa) tem um campo `scholar-ids: [...]` no
front matter com os IDs de Scholar conhecidos dos seus autores, vindos da
mesma caixa "Coautores" descrita acima.

- Um membro da equipe (`people/`) sem `scholar-id:` ainda ganha o campo
  automaticamente na primeira vez que aparece na caixa de coautores de um
  perfil sincronizado (nunca sobrescrevendo um valor já existente).
- Pra um paper já existente (encontrado por título), `sync_from_google_scholar.py`
  não reabre a página de citação — chama `backfill_scholar_ids`, que
  atualiza `scholar-ids:` usando o campo `author:` já salvo no arquivo
  mais o que foi resolvido nesta rodada.

**Limitação conhecida:** a caixa "Coautores" só lista quem o próprio
Scholar já considera colaborador frequente/confirmado, não todo coautor
de todo artigo — `scholar-ids:` costuma ficar parcial em papers com muitos
autores, preenchido aos poucos conforme mais perfis são sincronizados ou
buscados.

## Atualizando um preprint depois de publicado

Um paper já cadastrado nunca é re-raspado por padrão — é isso que evita
requisições repetidas pro mesmo artigo. A única exceção: se um arquivo
ainda "parece um preprint" (`render_publication.looks_like_preprint`, que
procura as palavras "preprint"/"arxiv" em qualquer lugar do arquivo), a
sincronização seguinte reabre a página de citação dele
(`scrape_paper_details`) especificamente pra conferir se o veículo já
mudou pra algo definitivo. Se mudou, `update_venue_if_published` atualiza
só `date:` e `description:` — abstract e lista de autores ficam intocados,
já que não se espera que mudem nessa transição. Uma vez que o veículo de
um arquivo deixa de parecer preprint, ele nunca mais é reaberto; só quem
ainda está pendente de publicação paga a requisição extra por
sincronização.

O que essa política não cobre: uma mudança de título entre a versão
preprint e a publicada (seria tratada como um artigo novo pelo dedup por
título, possivelmente duplicando), e mudanças de abstract/autores depois
de publicado. Ambos exigem ajuste manual — editar o `.qmd` diretamente, ou
apagá-lo e deixar a próxima sincronização recriá-lo se o título mudou o
suficiente pra não bater mais.

## Manutenção automática do listing

`../generate_person_bibliographies.py` (em `publications/`, chamado pelo
`project.pre-render` em `_quarto.yml`) chama `sync_symlinks.py` e depois
atualiza o front matter de cada `people/<username>.qmd` (o bloco
`listing:` delimitado) — a cada `quarto render`/`quarto preview`, sem
nenhum passo manual além de rodar um dos fetchers acima. As duas páginas
de listing principais (Publications e home) não são mais tocadas por
esse script: apontam direto, como glob estático, pras pastas canônicas
(`publications/group/*.qmd` + `publications/<solo>/*.qmd`), então uma
publicação nova já aparece sozinha ali assim que cai numa dessas pastas.

## Depois de rodar um fetcher

Como nada fica retido pra revisão, vale conferir rapidamente depois:

1. Confirmar que qualquer `categories:` bate com valores já usados em vez
   de introduzir categorias novas.
2. Checar os campos que o Google Scholar trouxe (ano, veículo, coautores,
   às vezes um abstract truncado) — ele não estrutura isso com a mesma
   limpeza da API do Semantic Scholar.
3. Corrigir o que estiver errado editando o `.qmd` já em `publications/`
   diretamente — não há arquivo intermediário pra mexer.

O `quarto render`/`quarto preview` seguinte recalcula sozinho o listing de
cada coautor e das duas páginas principais.
