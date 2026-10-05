# Fluxo de trabalho — geração de aulas

`teaching/` contém várias disciplinas, uma por subpasta (`supervised-learning/`, `unsupervised-learning/`, `optimization-linear-algebra/`, `computing-and-society/`, ...). Este arquivo vale para todas.

**Checkpoints por aula, com aprovação humana em cada etapa.** Nunca pule etapa nem gere a seguinte sem aprovação explícita ("pode seguir", "ok", "próxima etapa"). Depois do planejamento, pergunte se o usuário quer ir direto à aula completa ou conferir etapa a etapa.

Detalhes de formato consultados só na etapa que os usa (templates, glifos, exercícios, datasets, YAML): [`_ref-conteudo.md`](_ref-conteudo.md).

---

## Estrutura de pastas

```
teaching/
├── CLAUDE.md, _ref-conteudo.md
├── lesson-theme.scss, logos-footer.html, lesson-toc-accordion.html, UNICAMP.png, IC.png
└── <disciplina>/
    ├── index.qmd              # página pública do curso + planejamento do semestre
    ├── _fontes/               # PDFs de referência (symlinks relativos — nunca copiar o PDF)
    ├── _progresso.md          # estado aprovado + dicionário de notações
    ├── src/                   # opcional: módulo Python compartilhado entre aulas
    └── aulaNN/
        ├── index.qmd          # a aula (HTML + RevealJS), sem exercícios embutidos
        ├── exercicios.qmd     # público
        ├── soluções.qmd       # público — gabarito dos V/F
        ├── _00-plano-aula.md  # plano + fontes citadas (oculto)
        └── _02-respostas-pausas.md  # gabarito das Pausas Ativas (oculto)
```

O Quarto nunca publica arquivos/pastas com prefixo `_` (link para eles dá 404) — é assim que material de apoio e PDFs com direitos autorais ficam fora do site. Aulas antigas podem ter nomes legados (`_00-planejamento.md`, `_01-respostas.md`, `_03-respostas-pausas.md`); leia-os normalmente, mas crie arquivos novos só com os nomes acima.

O `index.qmd` da disciplina: só acrescente/atualize a entrada da aula em questão, salvo aprovação explícita.

---

## Etapa 0 — Identificar a disciplina (toda sessão)

- Declarada na mensagem → usar e confirmar em uma linha.
- Não declarada e há mais de uma disciplina → **perguntar** antes de qualquer ação (não adivinhar pela sessão anterior).
- Workspace aberto numa única disciplina → é ela.

Caminhos abaixo são relativos à subpasta da disciplina.

## Continuidade entre aulas (sem esgotar o contexto)

1. `_progresso.md` primeiro — estado + dicionário de notações (é a fonte para saber se um símbolo já existe).
2. O resumo do plano da aula N-1 — onde parou e qual foi a Ponte prometida.
3. O `index.qmd` de uma aula anterior só **sob demanda**, para uma dúvida concreta (como uma fórmula foi apresentada, que exemplo-fio foi usado). Prefira `grep` a ler o arquivo inteiro.

---

## Estrutura da aula

**Estratégia** (escolhida no planejamento):
- **A — Outside-In** (modelos/algoritmos: árvores, SVM, boosting, regressão logística, K-Means): modelo mental → necessidade teórica → teoria formal → síntese e limitações.
- **B — Inside-Out com Problema-Fio** (fundamentação matemática: matrizes, gradiente, espaços vetoriais, SVD): problema-fio → mecanismo/operação → diagnóstico teórico → ponte/limitação.

**Esqueleto de seções** (títulos `#` do `index.qmd`; ver template em `_ref-conteudo.md#esqueleto`):

1. **`# Revisão e Introdução`** (~10 min):
   - *Revisão* da aula anterior e conexão com a aula atual. Explique brevemente os conceitos principais (da aula anterior, e outros) para a aula atual, não dê de novo a aula, mas não seja exageradamente superficial.
   - *Ideia Central* (Ausubel): a ponte entre o que já se sabe e o novo.
   - *Roteiro*: quais são os principais conceitos que vão ser aprendidos e qual a conexão com os conceitos anteriores.
   - *Problema Motivador*: um resultado concreto (de preferência numérico/gráfico, no dataset-fio) que provoca antes do formalismo.
   - Pausa Ativa.
2. **`# Intuição — ...`** (~10 min; quase sempre em A, quando couber em B): o algoritmo/modelo em linhas gerais, com gráfico/diagrama, sem matemática pesada.
3. **`# Bloco N: ...`** — blocos de 10–15 min, cada um com um único ponto de aterrissagem e uma Pausa Ativa ao final. Sinalize hierarquia ("este é o resultado central", "esta hipótese vamos relaxar depois"). Depois da Intuição o rigor sobe: anuncie as premissas, depois derive passo a passo (ver "Precisão de conteúdo técnico").
4. **`# Fechamento`** (~5 min): *Retomando as N Perguntas* (uma resposta curta por pergunta do Roteiro) → *O Que Fica em Aberto* → *Ponte para a Aula N+1* → links de Exercícios/Soluções.

**Pausa Ativa (~3 min, nas notas e nos slides)** — duas caixas no mesmo slide:
1. uma **pergunta aberta** provocadora (com dica para conduzir);
2. um **bloco de V/F (4 itens)** que ajuda o raciocínio da pergunta aberta sem ser intrinsecamente ligado a ela — outros ângulos do mesmo conteúdo, não a resposta da aberta fatiada em itens.

A resposta aparece **só nos slides**, num slide seguinte (itens resolvidos com `✔`/`✗` + justificativa curta, e um fragmento "**Voltando à pergunta:** ..." respondendo a aberta). Nas notas, a resposta vai para `_02-respostas-pausas.md`, nunca para o `index.qmd`. Template e glifos: `_ref-conteudo.md#pausa-ativa`. **Nunca** `- [ ]`, `☐` ou `☒` (o Pandoc os transforma em checkbox clicável); use `□`.

Técnicas micro, quando couberem: exemplo resolvido antes do exercício; contraexemplo deliberado ("onde falha?"); duplo registro (intuição → formalismo → intuição); distratores plausíveis; não ler o slide em voz alta (Mayer); explicitar a estrutura argumentativa.

**Registro:** sem metáforas comerciais ("o que X compra/custa"), seja mais acadêmico. Nomeie direto: vantagens e limitações, custo computacional, o que se ganha e o que se perde.

---

## Formato do arquivo de aula

Um único `aulaNN/index.qmd` com saída dupla via `::: {.content-visible when-format="html" unless-format="revealjs"}` / `::: {.content-visible when-format="revealjs"}`. Copie o YAML de uma aula recente (`output-file: notas.html` / `slides.html` são obrigatórios — o rodapé dos slides linka `notas.html`). **Nunca mova configurações de formato para o `_quarto.yml`** (um `format: revealjs:` global já quebrou o build inteiro, silenciosamente).

**Notas e slides diferem na organização, não na profundidade.** Notas = prosa corrida com derivações por extenso, citações de página e avisos de leitura. Slides = a mesma história em fragmentos, sustentando a aula sozinhos. Teste: "um aluno que só visse o slide perderia algo que está na prosa?" Se sim, o slide está simplificado demais. Isso inclui o significado das variáveis do dataset, o porquê das escolhas e o contraste com o que veio antes.

Regras de slide (detalhes e exemplos em `_ref-conteudo.md#slides`):
- Revelação progressiva com `::: {.fragment}` (a conclusão/alerta do slide pode ser `::: {.fragment .callout-important}`); fórmulas e listas em itens, não em parágrafo denso.
- No máximo uma caixa por slide, exceto no slide da Pausa Ativa.
- Nenhum slide vazio ou picotado: depois de cada bloco, releia a sequência de `##` e funda os slides que são fração da mesma ideia; figura e comentário ficam juntos.
- Blocos HTML e RevealJS intercalados; um chunk de figura compartilhado vem depois dos dois textos (evita rodar o código duas vezes).

**Código:** um único chunk de setup global no topo (imports, paleta `COR_*` consistente com as aulas anteriores, dataset-fio, e todo cálculo cujo número aparece no texto). Todo número citado na prosa ou nos slides sai do código executado, com vírgula decimal (`$0{,}451$`). Chunks de figura: `#| echo: false`, envolvidos em `::: {.fig-resize style="width: XX%; margin: 0 auto;"}` (em chunks Python, `out-width`/`fig-width`/`fig-height` são ignorados; o tamanho vem do `figsize` e da largura do `.fig-resize`).

**Diagramas:** proponha TikZ (```` ```{.tikz} ````) sem esperar pedido quando houver sequência, árvore de decisão, ramificação ou caminhos alternativos. Use as cores de `lesson-theme.scss` e envolva também em `.fig-resize` (`fig-align` não tem efeito sem `fig-cap`).

**Dados:** o exemplo-fio vem de um dataset real (lista testada no Hugging Face Hub em `_ref-conteudo.md#datasets`), nunca Iris. Dados sintéticos só para isolar um ponto matemático (contraexemplo controlado, verificação numérica).

**Citações:** no `_00-plano-aula.md`, o trecho vai literal, na língua original, extraído do PDF (nunca de memória). No `index.qmd`, vai traduzido, marcado como "tradução livre", com seção e página. Termos sem tradução estável (*prima facie*) ficam no original, explicados na primeira aparição.

---

## Exercícios (toda aula)

Ficam fora do `index.qmd`, em `exercicios.qmd` + `soluções.qmd` (públicos): **2–3 questões discursivas** e **6–10 testes de V/F de 4 itens** cobrindo a aula de ponta a ponta. **Autocontidos**: servem de banco de prova, então nada pode depender de contexto que só existe na aula; use uma seção `## Contexto e notação` no topo. Os itens seguem heurísticas de construção (contrafactual, caso limite, transferência *dentro de ML*, falsa equivalência). Formato completo, YAML e classes dos links: `_ref-conteudo.md#exercicios`.

No `index.qmd`, os links `[Exercícios](exercicios.qmd){.see-all .exercicios-link} [Soluções](soluções.qmd){.see-all .solucoes-link}` ficam uma vez no Fechamento das notas e uma vez no dos slides. Não os repita no bloco de links do topo: o `toc-accordion.js` já move todo `a.see-all` das notas para o cabeçalho, e a repetição duplica os ícones.

Provas e avaliações (≠ exercícios de aula) ficam só no submódulo `evals/`.

---

## Ciclo por aula

1. **Contexto** — ler o `index.qmd` da disciplina, `_progresso.md` e a Ponte/resumo da aula N-1; confirmar tema, objetivos e carga horária. **Parar.**
2. **`_00-plano-aula.md`** — resumo (5–10 linhas: cobertura, objetivos, pré-requisitos, dataset-fio), estratégia A/B com justificativa em 1 linha, blocos com tempo e transição, e fontes (referência + uso + trecho literal). Template: `_ref-conteudo.md#plano-de-aula`. **Parar.**
3. **`index.qmd`** — seguir o plano e o esqueleto; revisar o picotamento a cada bloco de slides. **Parar.**
4. **`exercicios.qmd`, `soluções.qmd`, `_02-respostas-pausas.md`.** **Parar.**
5. **Registro** — mostrar o trecho exato da entrada no `index.qmd` da disciplina e aplicar só após confirmação; atualizar `_progresso.md` no formato de `_ref-conteudo.md#progresso` (uma linha na tabela de estado, 1–2 linhas de fio condutor, notações novas; **nunca um diário de correções**, que fica no git). Se o conteúdo desta aula desmentir a Ponte da aula N-1, propor a correção dessa Ponte (notas e slides).
6. **Avançar** só quando o usuário pedir ("próxima aula", "continuar").

---

## Precisão de conteúdo técnico

- Sinalize quando algo é inferido/generalizado a partir do livro, não copiado fielmente (provas, propriedades estatísticas, otimalidade).
- Definições, teoremas e provas são formais nas notas **e nos slides**: toda igualdade escrita, nenhum passo telescopado ("Passos 2–3: mesma mecânica" é proibido), nenhuma notação inventada (`(X^T)^T`, nunca `X^{TT}`), cada propriedade atribuída à entidade certa (simetria → matriz; ortogonalidade → conjunto de vetores), teoremas com hipótese e tese completas. Use callouts `callout-note icon=false` com título `Definição (...)` / `Teorema (...; fonte)`.
- **Derivações nos slides:** um fragmento por passo (`**Passo k — regra usada:**` + a equação completa). Quando a derivação continua em outro slide, reescreva a equação de onde parou. Abra os blocos que ficaram "fechados" num passo anterior quando é neles que o ponto da aula aparece (ex.: fatorar $p(\mathbf{Z},\pi\mid\phi)$ para mostrar onde a priori entra).
- Todo resultado não óbvio vem com nome do teorema e fonte (seção/página) ou com demonstração. Em cadeias de equivalências, cada elo precisa da sua justificativa. Um resultado de curso anterior não provado nem citado no material não pode ser usado como disponível.
- Quando um conceito abstrato tiver uma forma visual (o que a priori "acredita", a forma de uma densidade), mostre-a num gráfico antes de usar.
