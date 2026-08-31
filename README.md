# 🎓 Guia de Colaboração do Laboratório

Este guia explica como você, aluno(a) do grupo (ou qualquer colaborador
externo), pode atualizar o site (perfil, projetos, publicações e aulas)
sem precisar pedir para o Marcos mexer em nada manualmente. O site é feito
em [Quarto](https://quarto.org/) — não é mais o site antigo em Hugo, então
algumas coisas mudaram de lugar.

**Toda mudança entra pelo GitHub, via Pull Request — nunca por push
direto.** A branch `main` é protegida: ninguém (nem o Marcos) dá push
direto nela. O fluxo é sempre fork (ou branch, se você já tem acesso de
escrita ao repositório) → commit → `git push` → abrir um Pull Request →
revisão → merge pela própria interface do GitHub. As seções abaixo
mostram esse fluxo passo a passo.

## 1. Fork e ambiente de trabalho

1. Acesse o repositório: https://github.com/marcosmrai/webpage
2. Clique em **Fork** (canto superior direito) para criar uma cópia sua do
   repositório.
3. No **seu fork**, clique em **Code → Codespaces → Create codespace on
   main**. Isso abre um VS Code completo no navegador, já com o Quarto
   instalado automaticamente (pode levar 1–2 minutos na primeira vez).
   - Se preferir trabalhar na sua própria máquina em vez de Codespaces,
     clone o seu fork normalmente e instale o Quarto
     (https://quarto.org/docs/get-started/).

## 2. Rodando o site localmente

Dentro do Codespace (ou do seu terminal local), na raiz do projeto, rode:

```bash
quarto preview --port 2222
```

- No Codespaces, uma notificação vai aparecer no canto inferior direito
  oferecendo para abrir a porta `2222` no navegador — clique em **Open in
  Browser**. Se a notificação não aparecer, abra a aba **PORTS** no painel
  inferior do VS Code e clique no ícone de globo ao lado da porta `2222`.
- Localmente, o próprio `quarto preview` já abre o navegador sozinho.
- O preview atualiza automaticamente sempre que você salva um arquivo
  (`Ctrl+S` / `Cmd+S`) — não precisa parar e rodar de novo.
- Para parar o preview, `Ctrl+C` no terminal.
- Esse é o fluxo recomendado para quem está contribuindo de fora. O
  mantenedor do site usa uma variante própria (`preview-watch.py`, rodando
  como serviço em segundo plano) para renderizar só o que muda em
  projetos grandes — não é necessário reproduzir isso para enviar um PR,
  `quarto preview` é suficiente.

## 3. Editando seu perfil

Cada pessoa do grupo tem **um único arquivo** em `people/`, no formato
`people/<usuario>.qmd` (não é mais uma pasta como no site antigo).

### Nome de usuário (nome do arquivo)

O nome do arquivo segue um padrão de "nome de autor de artigo": iniciais
minúsculas de todos os nomes, exceto o último, seguidas do último
sobrenome por extenso, sem espaços nem hífens. Exemplos:

| Nome completo          | Usuário      |
|-------------------------|--------------|
| Giovani Valdrighi        | `gvaldrighi` |
| Caio Prado               | `cprado`     |
| Kento Tiago Tamashiro    | `kttamashiro`|

Partículas como "de", "da", "dos" não entram na inicial (ex.: "Ian Loron de
Almeida" → `ilalmeida`).

### Criando seu perfil do zero

1. Adicione sua foto em `people/<usuario>.jpg` (ou `.png`/`.webp`) — de
   preferência quadrada.
2. Crie `people/<usuario>.qmd` com este conteúdo como ponto de partida,
   trocando os valores pelos seus:

   ```yaml
   ---
   title: "Seu Nome Completo"
   subtitle: "Undergraduate Research Assistant"
   image: <usuario>.jpg
   description: "Sua área de interesse principal"
   about:
     template: jolla
     image-shape: round
   group: "Undergrad Research Assistants"
   filters:
     - ../band-sections.lua
   ---

   [Institute of Computing - University of Campinas](https://ic.unicamp.br/)

   ::: {#links}
   :::

   ## Interests

   - Sua área de interesse

   ## Education

   **Curso**, ano previsto de conclusão
   University of Campinas
   ```

3. `group:` deve ser um destes valores (define em qual seção da página de
   pessoas você aparece): `"Principal Investigator"`, `"Ph.D. Students"`,
   `"Master Students"`, `"Undergrad Research Assistants"`,
   `"Former Researchers"`.
4. Seções de texto livre (Interests, Education, Experience, etc.) você
   escreve à mão, em Markdown normal.

### Links (Scholar, GitHub, LinkedIn, etc.)

**Nunca escreva `<a href=...>` na mão.** Os ícones de contato são gerados
automaticamente a partir de uma lista `links:` no cabeçalho do arquivo.
Adicione (ou edite) assim:

```yaml
links:
  - scholar-id: "SEU_ID_DO_GOOGLE_SCHOLAR"
  - github: seu-usuario-github
  - linkedin: seu-usuario-linkedin
  - lattes: "seu-id-numerico-do-lattes"
  - website: "https://seu-site.com"
  - email: "voce@dominio.com"
```

A ordem em que você lista os campos é a ordem em que os ícones aparecem.
Use só os campos que fizerem sentido para você — não precisa preencher
todos. (Esses campos são interpretados por `links.lua` — ver seção 7.)

### ⚠️ Não edite à mão

Se o seu perfil já tiver um bloco assim no cabeçalho:

```yaml
listing:
  # projects-listing:start (gerado por generate_project_pages.py — não editar)
  ...
  # projects-listing:end
```

ou uma seção `## Projects` / `## Publications` com `::: {#projects} :::` /
`::: {#publications} :::` no corpo do texto, **não mexa nisso**. Esses
blocos são recalculados automaticamente toda vez que o site é renderizado,
a partir dos arquivos em `projects/` e `publications/` — qualquer edição
manual ali é sobrescrita.

## 4. Participando de um projeto

Projetos ficam em `projects/<slug-do-projeto>.qmd`. Se você já tem seu
perfil criado (passo 3) e vai participar de um projeto existente, basta
adicionar seu usuário à lista `participants:` no cabeçalho desse arquivo:

```yaml
participants: [mraimundo, gvaldrighi, seu-usuario]
```

Isso já é suficiente para o seu card (foto + nome, linkando para o seu
perfil) aparecer automaticamente na seção "Participants" da página do
projeto, e para o projeto aparecer na sua própria página de perfil. (Quem
faz esse preenchimento é `participants.lua` — ver seção 7.)

## 5. Publicações

Você **não precisa (e não deve)** criar ou editar arquivos em
`publications/` manualmente. Elas são sincronizadas automaticamente a
partir do Google Scholar. Se notar um artigo seu faltando ou com alguma
informação errada, avise o Marcos em vez de editar o arquivo diretamente.

## 6. Editando aulas (`teaching/`)

Conteúdo de disciplinas e aulas fica em `teaching/<disciplina>/`. Cada
disciplina tem seu próprio `index.qmd` (a página pública do curso — tema,
objetivos, lista de aulas) e uma subpasta `aulaNN/` por aula, cujo
`index.qmd` único gera **duas saídas** a partir do mesmo arquivo: as notas
em HTML (`notas.html`) e os slides em RevealJS (`slides.html`).

Esta é a parte do site com a regra mais detalhada e específica — antes de
editar ou criar uma aula, leia **`teaching/CLAUDE.md`**, que descreve a
estrutura pedagógica esperada (abertura/desenvolvimento/fechamento,
pausas ativas, exercícios obrigatórios), convenções de formatação (nomes
de arquivo de saída, como redimensionar figuras/diagramas, datasets
preferidos) e o processo de checkpoints por aula. Não é opcional pular
essa leitura: um PR que não siga essas convenções provavelmente vai
precisar de retrabalho na revisão.

Algumas disciplinas também têm uma pasta `PDD/` com o Plano de
Desenvolvimento da Disciplina oficial (PDF protocolado na Unicamp) e uma
página `pdd.qmd` que o reproduz — esses PDFs não devem ser editados
diretamente; qualquer atualização deve vir acompanhada da atualização
correspondente em `pdd.qmd`.

## 7. Estrutura do projeto (visão geral)

Um mapa rápido de onde as coisas ficam, útil se seu PR mexe em algo além
de perfil/projeto/aula:

| Caminho | O que é |
|---|---|
| `_quarto.yml` | Configuração global do site: tema, navbar, filtros ativos, formato padrão de saída. |
| `styles.css` / `custom.scss` | Visual do site inteiro (layout, listagens, cabeçalhos, cartão de perfil). `custom.scss` só ajusta variáveis do tema Bootstrap (cor primária, etc.); o grosso das regras está em `styles.css`. |
| `teaching/lesson-theme.scss`, `teaching/toc-accordion.js` | Visual e comportamento específicos das aulas (paleta própria, slides, acordeão do sumário) — carregados só dentro de `teaching/`. |
| `band-sections.lua`, `links.lua`, `participants.lua` | Filtros Pandoc que preenchem automaticamente certas seções (faixas da home, ícones de contato, cards de participantes) a partir do front matter YAML — nunca editam o `.qmd`, e o HTML que geram nunca deve ser escrito à mão. |
| `people/`, `projects/`, `publications/`, `teaching/` | Conteúdo, um por seção do site — ver seções 3–6 acima. |
| `preview-watch.py`, `deploy.sh` | Infraestrutura de build/preview/deploy usada pelo mantenedor do site. Não é necessária para contribuir com conteúdo (use `quarto preview`, seção 2). |
| `_site/`, `_freeze/`, `.quarto/` | Saída renderizada e cache de execução do Quarto. Alguns desses arquivos ficam versionados de propósito (ver comentários em `.gitignore`) e mudam sozinhos quando você roda o preview — normal, não precisa se preocupar em revertê-los; só nunca edite o HTML/SVG gerado ali diretamente, edite sempre a fonte (`.qmd`/`.py`). |

## 8. Enviando suas alterações

Depois de editar e conferir no preview que está tudo certo:

```bash
git add .
git commit -m "Descrição curta do que você mudou"
git push
```

Depois vá até a página do **seu fork** no GitHub — vai aparecer um aviso
"This branch is X commits ahead of marcosmrai:main". Clique em
**Contribute → Open pull request**, escreva uma descrição curta do que
mudou, e envie. O Marcos revisa e faz o merge — lembrando que `main` é
protegida, então mesmo uma mudança pequena e óbvia precisa passar por
esse fluxo de PR, nunca por push direto.

---

Dúvidas ou algo não descrito aqui? Chame o Marcos.
