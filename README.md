# 🎓 Guia de Colaboração do Laboratório

Este guia explica como você, aluno(a) do grupo, pode atualizar o site
(perfil, projetos e publicações) sem precisar pedir para o Marcos mexer em
nada manualmente. O site é feito em [Quarto](https://quarto.org/) — não é
mais o site antigo em Hugo, então algumas coisas mudaram de lugar.

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
todos.

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
projeto, e para o projeto aparecer na sua própria página de perfil.

## 5. Publicações

Você **não precisa (e não deve)** criar ou editar arquivos em
`publications/` manualmente. Elas são sincronizadas automaticamente a
partir do Google Scholar. Se notar um artigo seu faltando ou com alguma
informação errada, avise o Marcos em vez de editar o arquivo diretamente.

## 6. Enviando suas alterações

Depois de editar e conferir no preview que está tudo certo:

```bash
git add .
git commit -m "Descrição curta do que você mudou"
git push
```

Depois vá até a página do **seu fork** no GitHub — vai aparecer um aviso
"This branch is X commits ahead of marcosmrai:main". Clique em
**Contribute → Open pull request**, escreva uma descrição curta do que
mudou, e envie. O Marcos revisa e faz o merge.

---

Dúvidas ou algo não descrito aqui? Chame o Marcos.
