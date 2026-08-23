# Progresso — Supervised Learning

Estrutura conforme o `CLAUDE.md` atualizado em 2026-08-09: `index.md` é o
planejamento do semestre (formatado para Hugo); cada aula é `aulaNN/` com
`00-plano-aula.md` (resumo + plano de blocos), `01-fontes.md` (fontes com
trecho citado literalmente) e `02-aula.qmd` (aula final, dupla saída
HTML/RevealJS via `_quarto.yml`, que já define `output-file: notas.html` /
`slides.html` no nível do projeto). Fontes bibliográficas em `fontes/`:
`prml.pdf`, `dlfc.pdf`, `esl.pdf` (links simbólicos, já colocados pelo
usuário), mais `exemplos-estilo/exemplo.qmd` (symlink para `aula01/02-aula.qmd`,
aprovada, como referência de tom/estilo para novas aulas).

**Aprovado pelo usuário:** aulas podem ser mais longas que os 100 min de
referência — não é mais um item pendente de decisão, é o padrão aceito.

## Aula 1 — Data, Distributions, and Anomaly Detection

- [x] `00-plano-aula.md` — funde o antigo `resumo.md` + `plan.md`. Duas
      rodadas de ajuste já incorporadas (catálogo cortado, Beta
      simplificada, Blocos 6–7 fundidos, decisão ampliada). ~130 min.
- [x] `01-fontes.md` — 10 fontes, **todos os trechos preenchidos** com
      citação literal extraída de `prml.pdf`/`dlfc.pdf` (offset página
      impressa → PDF: **+20** para os dois livros, confirmado nos
      capítulos usados).
- [x] `02-aula.qmd` — revisado em 2026-08-09 (3 correções: texto vazado da
      geração, referência errada à Aula 4, mistura linear/quadrático no
      gradiente do outlier); depois reescrito para bater com o plano
      reconciliado. Validado com `quarto render --to html` e `--to
      revealjs`, sem erro. Backup do estado pré-revisão em `aula01/backup.md`.
- [x] Servindo de `fontes/exemplos-estilo/exemplo.qmd` (symlink).

## Aula 2 — Conditional Distributions and Generative Models

Reiniciada do zero nesta rodada (`02-aula.qmd`, `00-plano-aula.md` e
`01-fontes.md` anteriores descartados a pedido do usuário; o `index.qmd`
antigo continua recuperável do histórico do git, commit `a66e239`, se algum
dia necessário — não foi restaurado).

- [x] `00-plano-aula.md` — resumo + plano num único arquivo (formato pedido
      pelo usuário para esta aula). Blocos 5+6 do rascunho original foram
      fundidos durante o planejamento (razão de verossimilhanças e teoria
      da decisão são o mesmo objeto — percebido pelo usuário). ~130 min
      final (estimativa original de ~105 min não se sustentou).
- [x] `01-fontes.md` — 10 fontes obrigatórias + 1 opcional (grafo Naive
      Bayes), **todos os trechos preenchidos**. Achado não planejado: a
      Fonte 11 (PRML §8.2.2, p. 381) contém uma frase do próprio PRML que
      sustenta o argumento "classifica bem, estima mal" do Bloco 4 — a
      fonte externa Domingos & Pazzani (1997), que tinha sido descartada,
      acabou substituída por uma citação literal do PRML — **já inserida**
      no `02-aula.qmd`, ao final do Bloco 4.
- [x] `02-aula.qmd` — escrito nesta sessão. Matemática do Bloco 4 (condição
      de coincidência de fronteiras naive/plena) verificada numericamente
      antes de escrever o texto (cos exato = 1.0 no caso alinhado, ≈0.68
      no genérico; acurácia 0.8455 vs. 0.8443 vs. 0.993 vs. 0.892). Validado
      com `quarto render --to html` e `--to revealjs`, sem erro.

## Aula 3 — Decision Trees — Greedy Partitioning

- [x] `00-plano-aula.md` — reescrito a pedido do usuário ("não use os
      livros tanto assim e tente de novo"): removidas quase todas as
      citações inline de página/equação da prosa dos blocos, deixando a
      exposição pedagógica original e reservando citação literal só para
      `01-fontes.md`. 6 blocos (~110–120 min).
- [x] `01-fontes.md` — deliberadamente enxuto: só 6 fontes (vs. 10+ nas
      Aulas 1–2), cobrindo apenas definição/fórmulas/limitações
      essenciais do PRML §14.4 (offset +20 confirmado de novo). Inclui
      nota de precisão sobre a inconsistência de sinal na eq. 14.32
      (cross-entropy impressa sem o sinal negativo padrão, mas descrita
      em prosa como tendo máximo em p=0,5 — achado nosso, não errata
      externa confirmada). ESL segue disponível como leitura opcional,
      não citado nesta aula.
- [x] `02-aula.qmd` — escrito com scikit-learn (`DecisionTreeRegressor`/
      `DecisionTreeClassifier`/`cost_complexity_pruning_path`, v1.9.0).
      Núcleo estatístico verificado numericamente antes de escrever:
      MLE gaussiano numa folha = média amostral (regressão); MLE
      categórico numa folha = proporção empírica, e maximizar essa
      log-verossimilhança ≡ minimizar a entropia (classificação);
      contraexemplo original mostrando que a taxa de erro bruta é cega
      a uma diferença de qualidade entre dois splits (ambos com erro
      ponderado 0,2500) que Gini/entropia corretamente distinguem.
      Segue o novo paradigma de aula do `CLAUDE.md` (pausas ativas como
      pergunta-título, 3 testes V/F nos slides cada um com slide de
      resposta separado, 3 discursivas + 12 blocos de V/F nas notas).
      Validado com `quarto render --to html` e `--to revealjs`
      (precisa ativar `../../.venv` antes — o kernel jupyter "python3"
      padrão do sistema não tem numpy/sklearn instalados).

## Reformulação de pedagogia (Aulas 1–3, `CLAUDE.md` atualizado em 2026-08-18)

As três aulas foram reescritas (ou, no caso da Aula 3, escritas desde o
início) dentro do novo paradigma de `CLAUDE.md`: abertura com organizador
prévio e roteiro explícito, desenvolvimento segmentado com pausas ativas
entre blocos, exercícios de checagem intercalados nos slides (não só ao
final), e fechamento retomando as perguntas de abertura.

- **Quotas de exercícios corrigidas:** o `CLAUDE.md` foi ajustado para
  deixar explícito que são **12 blocos de V/F** (4 itens cada, 48 itens
  ao todo) nas notas, não 12 itens soltos — a primeira leitura da regra
  levou a só 3 blocos nas Aulas 1–2, corrigido depois do usuário apontar.
- **Achado técnico recorrente (Reveal.js):** um `##` usado como título de
  um `callout-tip` vira `<div class="callout-title">`, não um heading
  real — por isso é invisível para o corte de slides do Reveal.js, e o
  conteúdo gruda no slide anterior. Fix: para o bloco `revealjs`, o `##`
  fica **fora** da caixa, como heading real; para as notas HTML, o
  título continua dentro da caixa (cosmético, sem esse problema).
- **Segundo achado, mais sutil, encontrado na Aula 3:** se a mesma
  pergunta/V-ou-F aparece tanto num bloco `html-only` (título dentro da
  caixa) quanto num bloco `revealjs`-only (título hoisted fora da caixa)
  *sem* que o primeiro esteja explicitamente restrito a
  `unless-format="revealjs"`, ele também é renderizado no Reveal.js —
  criando um slide duplicado da mesma pergunta. Verificado via extração
  de `<section id=...>` do `slides.html` renderizado (sufixos `-1`
  automáticos do pandoc para ids repetidos foram o sinal). Fix: todo
  bloco de pergunta/V-ou-F que existe também em versão hoisted para
  `revealjs` precisa estar explicitamente dentro de
  `::: {.content-visible when-format="html" unless-format="revealjs"}`,
  nunca solto sem essa restrição.
- Aula 1 e Aula 2 já tinham passado por essa reescrita antes da Aula 3;
  ambas revalidadas (balanço de divs + render duplo) depois dos ajustes
  de quotas e do fix de heading-hoisting.

**Correção de padrão de slide em 2026-08-19** (aplicada às Aulas 1, 2 e
3, seguindo a mesma correção já feita em `unsupervised` e `algebra_opt`):
as pausas ativas e os testes V/F nos slides RevealJS usavam a
pergunta/tema inteiro como título real do slide, com a caixa
`callout-tip` carregando só uma dica curta (ou, nos testes V/F, um
título "— Resposta" repetido). O padrão correto, confirmado pelo
usuário e documentado no `CLAUDE.md`, usa o rótulo genérico `Pergunta`
(e `Resposta` no slide seguinte) como título real do slide, com a
pergunta/tema específico como título do `callout-tip` dentro da caixa.
Corrigidas 8 instâncias na Aula 1, 9 na Aula 2 e 13 na Aula 3 (30 no
total), via um script Python que localiza, por rastreamento de
aninhamento de divs, cada `callout-tip` dentro de um bloco
`revealjs`-only sem heading interno, e faz a transformação de forma
determinística — verificado antes num arquivo de teste, não direto nos
originais.

Um segundo bug, mais sério, apareceu no caminho: as Aulas 1 e 2 tinham
3 `callout-tip` cada (das *pausas ativas* mais antigas dessas aulas,
escritas antes mesmo da convenção `Pergunta`/`Resposta` existir) que
não estavam restritos a `unless-format="revealjs"` — ou seja,
renderizavam em **todos** os formatos, inclusive no RevealJS, onde já
havia uma versão dedicada da mesma pergunta. Isso duplicava a pausa
ativa no RevealJS (mesmo bug de fundo já visto antes na Aula 3, mas
não pego nas Aulas 1–2 porque elas foram escritas antes desse
achado). Corrigido envolvendo essas 6 caixas em
`::: {.content-visible when-format="html" unless-format="revealjs"}`.

Revalidado com `quarto render --to html` e `--to revealjs` nas três
aulas; confirmado via extração de `<section id=...>` dos `slides.html`
renderizados que todo slide `Pergunta` tem sua caixa logo abaixo, e
que os V/F têm o `Resposta` correspondente imediatamente depois — sem
nenhum id de slide duplicado ou vazio.

## Pendências gerais

## Auditoria do planejamento (2026-08-23)

Pedido do usuário: conferir se o `index.qmd` da disciplina (planejamento do
semestre) bate com o que as Aulas 1–3 realmente entregam. Achados:

- **Bug real, corrigido:** o `_00-plano-aula.md` da Aula 1 definia um
  **Bloco 7 (~35 min, o maior bloco da aula)** — "Teoria da decisão: custo,
  avaliação e rejeição" (matriz de perda sob custo assimétrico, matriz de
  confusão, precisão/recall, curva ROC, opção de rejeição/regra de Chow) —
  que **nunca chegou a ser escrito** no `aula01/index.qmd` final, apesar de
  o arquivo constar como "validado" várias vezes nas rodadas anteriores
  deste progresso. Os Exercícios já citavam "custo assimétrico" e "falso
  positivo" (Questão discursiva 3) como se o conteúdo tivesse sido dado —
  ficou órfão até agora. Reescrito nesta sessão como a seção
  "Teoria da Decisão: Custo, Avaliação e Rejeição" (4 subblocos: custo
  assimétrico, matriz de confusão/precisão/recall, curva ROC, rejeição),
  reaproveitando a mesma população `xA`/`xB` e o mesmo `T_CONJ` dos Blocos
  1–4 (nenhum dado novo, nenhuma suposição nova — só a ferramenta de
  decisão fica mais rica). Números verificados por script Python
  independente antes de escrever (kernel `sensibleml-moo`, seed
  `20260806`): em $t=T_{CONJ}\approx0{,}72$, acurácia $95{,}6\%$ contra
  $95\%$ do classificador ingênuo "sempre A" (o paradoxo da acurácia,
  usado como pausa ativa), recall só $34\%$; com custo 10:1 (mesmo número
  do Exercício 3), o corte desloca para $T_{custo}\approx0{,}53$, recall
  sobe a $72\%$ às custas de acurácia menor ($89{,}4\%$) — usado para
  mostrar que minimizar custo esperado não é o mesmo que minimizar erro
  bruto. ROC reaproveita literalmente os arrays `ts`/`tipo1`/`tipo2` já
  calculados no Bloco 1 (AUC${}\approx0{,}94$). Rejeição com $\theta=0{,}6$
  cobre ${\approx}2{,}1\%$ da população. Um bug de mathtext do matplotlib
  encontrado e corrigido durante a validação: `%` cru dentro de `$...$` em
  título de figura quebra o parser (`ValueError: Expected end of text`) —
  precisa ficar fora do modo matemático ou escapado como `\%`; diferente
  de MathJax (usado no corpo do texto via `\%`), que aceita normalmente.
  Revalidado com `quarto render --to html` e `--to revealjs` (kernel do
  `.venv` em `~/Documents/Research/sensible-deep-moo/code/.venv`, não o
  `.venv` da raiz do site, que não tem scipy) — sem erro, numeração de
  seções e sequência de slides conferidas (nenhum heading duplicado ou
  órfão).
- **Achado leve, corrigido:** a entrada da **Lesson 2** no `index.qmd` da
  disciplina não mencionava teoria da decisão geral (risco posterior,
  regra de Bayes, opção de rejeição para $K$ classes), que é o Bloco 5 da
  Aula 2 — o maior bloco dela (38 min). Descrição da Lesson 2 atualizada
  (ML Concept/Statistical Concept/Objectives/Expected Competencies) para
  refletir isso; trecho mostrado no chat antes de aplicar. Título da
  Lesson 2 mantido como estava (não foi pedido trocar).
- **Não verificado no mesmo nível para Aulas 2–3** — a auditoria focou no
  que o usuário sinalizou; não foi feita uma varredura heading-a-heading
  dessas duas aulas contra seus respectivos planos.

## Pendências gerais

- **Resolvido:** Etapa 5 feita para as Aulas 1, 2 e 3 — `index.md` linka
  `../supervised/aulaNN/notas.html` (+ Slides), um único `../` (não
  `../../`) — path corrigido pelo usuário na Aula 3; Aulas 1–2 já
  estavam certas com essa mesma profundidade. Trecho mostrado no chat
  antes de aplicar, em cada caso.
- **Resolvido:** pastas órfãs removidas — `content/teaching/supervised/aula1/`,
  `aula2/` (nomes antigos, pré-rename) e `static/supervised/aula1/`,
  `aula2/` (output antigo, incluindo um diretório `aula2/` com arquivos
  nunca rastreados pelo git). O output atual vive em
  `static/supervised/aula01/` e `aula02/`, cada um com `02-aula_files/`
  (nome derivado de `02-aula.qmd`, não mais `index_files/`).
- **Resolvido:** citação do PRML p. 381 adicionada ao final do Bloco 4 de
  `aula02/02-aula.qmd`; ambas as aulas re-renderizadas (`--to html` e
  `--to revealjs`) depois da mudança, sem erro.
- Formato do `00-plano-aula.md`: mantido mais elaborado que o esqueleto
  mínimo do `CLAUDE.md` (subseções, notas de reconciliação), por decisão
  explícita do usuário — não é uma divergência a corrigir.
- `fontes/exemplos-estilo/` resolvido com um symlink para `aula01/02-aula.qmd`
  — se a Aula 1 for revisada de novo, o exemplo atualiza automaticamente
  (é link, não cópia).
