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

## Aula 4 — Seleção de Modelo, Validação Cruzada e Bootstrap

- [x] `_00-plano-aula.md` — 9 blocos (~135 min). Fio condutor: fecha o
      gancho deixado pela Aula 3 (poda "olhando o gráfico") escolhendo
      $\lambda$ de custo-complexidade por 5-fold CV estratificada sobre
      dado real.
- [x] `_01-fontes.md` — 6 fontes de ESL (Hastie, Tibshirani & Friedman),
      **primeira citação de ESL nesta disciplina** (offset de página
      confirmado em +19, diferente do +20 de PRML/DLFC — checado lendo o
      número impresso ao redor do Cap. 7, não assumido por analogia).
      PRML/DLFC não têm tratamento comparável de CV/Bootstrap.
- [x] `index.qmd` — **primeira aula desta disciplina com dado real**
      (Breast Cancer Wisconsin, 569 pacientes, via Hugging Face Hub),
      registrado explicitamente como mudança de padrão a partir desta
      aula, sem mexer nas Aulas 1–3 (sintéticas, já aprovadas). Números
      verificados por script Python independente antes de escrever:
      curva de overfitting real (treino 100% a partir de profundidade 6,
      teste com pico de 93,0% na profundidade 5); poda por CV escolhe 4
      folhas contra 19 da árvore completa, empatando em acurácia de
      teste (91,8%); regra 1-SE fica com 2 folhas e paga um custo real
      de acurácia (90,1%); comparação honesta LOOCV (89,4%) vs. 5-fold e
      10-fold repetidos (~92–93%, LOOCV ficou **abaixo**, não acima —
      achado real, não forçado a bater com a teoria); dois usos de
      Bootstrap (reamostrar teste vs. reamostrar+reajustar treino) com
      ICs distintos; reprodução independente (30 simulações próprias,
      não só a citação do livro) do experimento clássico do ESL sobre
      vazamento de dados por seleção de atributos antes do split (erro
      estimado ${\sim}1{,}5\%$ contra erro real de 50%). Validado com
      `quarto render --to html` e `--to revealjs`, sem erro; 5 pares de
      V/F confirmados (acima do mínimo de 3) via extração de headings;
      Exercícios com 3 discursivas + 12 blocos de V/F de 4 itens.
- [ ] Etapa 5 (`index.qmd` da disciplina) — ainda não proposta; aguardando
      aprovação da aula completa antes de mostrar o diff da Lesson 4.

**Nota de processo:** o usuário aprovou pular a pausa entre Etapa 3
(fontes) e Etapa 4 (aula completa) para esta aula específica ("Pode
seguir para fontes e já fazer a aula") — não é uma dispensa geral do
checkpoint para as próximas aulas desta disciplina, diferente do que foi
combinado para `object-oriented-programming`.

## Correção de conteúdo na Aula 3 (2026-08-24)

Revisão pontual pedida pelo usuário, direto no `index.qmd` já aprovado:

- **Achado correto do usuário:** o texto dizia que a árvore estima
  $p(\mathbf{x}\mid\mathcal{C}_k)$ (densidade condicional de classe),
  mas o que a árvore de fato estima em cada folha é a **posteriori**
  $p(\mathcal{C}_k\mid\mathbf{x})$ (proporção empírica de classes na
  folha) — nunca uma densidade de $\mathbf{x}$. Corrigido na Seção 2
  ("Árvores Como Estimação Não-Paramétrica").
- Adicionadas 3 caixas (`callout-note`) na mesma seção, com contrapartida
  resumida nos slides: (1) **Modelos generativos vs. preditivos** —
  contrastando o caminho generativo das Aulas 1–2 (ajustar
  $p(\mathbf{x}\mid\mathcal{C}_k)$, combinar com $\pi_k$ via Bayes) com o
  caminho direto da árvore; (2) **Paramétrico vs. não-paramétrico**, com
  a definição formal (dimensão de $\theta$ fixa vs. crescendo com $N$);
  (3) **Verossimilhança e MLE**, definição formal
  ($L(\theta;\mathcal D)=p(\mathcal D\mid\theta)$, inversão de papéis
  entre densidade e verossimilhança) com o exemplo canônico da gaussiana
  (incluindo o viés do MLE de $\sigma^2$, que reaparece mais adiante no
  curso). O usuário pediu inicialmente uma seção nova de "probabilidade"
  antes da Seção 3, depois recuou e pediu só essas caixas dentro da
  própria Seção 2 — atendido na segunda versão do pedido.
- Na Seção 3 ("Árvores de Regressão: Verossimilhança Gaussiana"), a
  passagem de $\ell_\tau(y_\tau)$ (log-verossimilhança gaussiana) até
  $Q_\tau$ (soma de quadrados) e daí até a média amostral estava correta
  mas condensada demais; reescrita como derivação explícita em 3 passos
  (isolar o termo que depende de $y_\tau$; trocar o sinal reconhecendo
  que maximizar $-c\cdot f$ com $c>0$ é minimizar $f$; resolver o mínimo
  derivando $Q_\tau$), com contrapartida resumida num slide novo.
- Revalidado com `quarto render --to html` (sai como `index.html`, não
  `notas.html` — esta aula já usava esse nome de saída antes desta
  sessão) e `--to revealjs`, sem erro; sequência de slides conferida via
  extração de headings, sem duplicação.

## Adições ao fim da Seção 3 e nova seção de Teoria da Informação (Aula 3, 2026-08-24)

Duas adições pedidas pelo usuário, ainda dentro da mesma revisão pontual
do `index.qmd` já aprovado (Aula 3):

- **Algoritmo de crescimento guloso, com dado real, ao fim da Seção 3**
  ("Árvores de Regressão"). Faltava, depois de toda a intuição sobre
  $Q_\tau$ e o critério de corte, o algoritmo escrito por extenso e
  generalizado para múltiplas variáveis (o exemplo anterior da seção
  buscava só 1 variável 1D). Usado **California Housing**
  (`gvlassis/california_housing`, treino, amostra de 500 pontos,
  `random_state=20260824`), restrito a 2 das 8 variáveis (`MedInc`,
  `HouseAge`) só para permitir desenhar a partição em 2D — disclaimer
  explícito no texto de que uma árvore de produção buscaria sobre as 8.
  Mostrado o estado da árvore exatamente na topologia pedida: split na
  raiz, os dois filhos da raiz cortados (4 folhas), mais um corte no
  nível seguinte (5 folhas, 4 cortes no total) — e então o quinto corte
  **resolvido passo a passo**, com busca gulosa genuína entre as 5
  folhas abertas (vencedora: folha `LR`, por `HouseAge`). Todos os
  números (limiares, médias, $Q$, reduções) computados e verificados via
  script Python independente antes de escrever, e conferidos batendo com
  a saída renderizada. Segue a nova regra de visibilidade de código do
  `CLAUDE.md`: a função de busca exaustiva (`melhor_corte`) e os loops
  que testam as folhas ficam `echo: true` (são a demonstração); só o
  código de plotagem em torno fica `echo: false`.
- **Nova seção "Teoria da Informação: Medindo Probabilidade"**, inserida
  entre a Seção 3 (Árvores de Regressão) e a Seção 4 (Árvores de
  Classificação) — pedido explícito do usuário para dar uma base formal
  de entropia/informação mútua antes de a Seção 4 usar entropia como
  critério de corte, e para religar esse conteúdo aos conceitos de
  probabilidade das Aulas 1–2 (conjunta, condicional, independência).
  Cobre: surpresa e entropia $H(X)$ (nats, mesma convenção da Seção 4);
  entropia conjunta/condicional e a regra da cadeia; informação mútua
  $I(X;Y)$, com o resultado central $I(X;Y)=0 \iff$ independência (Aula
  2) — enquadrando informação mútua como "a régua que mede a distância
  até a independência". Reaproveita o próprio exemplo de "grátis"/
  "ganhador" da Aula 2 (mesmos números de $p(\cdot\mid\text{spam/ham})$)
  para calcular $I(G;W)\approx0{,}1406$ nats (confirmando numericamente,
  com um único número, a dependência marginal que a Aula 2 só mostrava
  célula a célula) e $I(G;\mathcal C)\approx0{,}4072$ vs.
  $I(W;\mathcal C)\approx0{,}2336$ nats — usado como ponte direta para a
  Seção 4: o critério de "ganho de informação" de uma árvore de
  classificação é exatamente essa informação mútua entre a variável de
  corte e a classe. Números recomputados e conferidos batendo com a
  saída renderizada (`0.1406`, `0.4072`, `0.2336`).
- Revalidado com `quarto render --to html` e `--to revealjs`, sem erro;
  balanço de divs (`:::`) conferido por script; nenhum heading duplicado
  ou órfão (as duplicatas de título encontradas são o padrão esperado
  pergunta/resposta já usado no resto do arquivo).

**Nova regra de processo adicionada ao `CLAUDE.md` nesta mesma sessão:**
os blocos `content-visible` de HTML e de RevealJS devem ficar
intercalados seção por seção (ou bloco por bloco) ao longo do arquivo,
nunca toda a prosa HTML primeiro seguida de todos os slides no fim —
feedback do usuário de que juntar os slides no fim já forçou retrabalho
em aulas anteriores. As duas adições desta entrada já seguem esse
padrão.

## Seções 5 e 6 religadas à Teoria da Informação (Aula 3, 2026-08-24)

Terceira rodada de ajustes na mesma revisão, depois de a Seção de
Teoria da Informação já existir:

- **Seção "Árvores de Classificação"** (agora Seção 5, depois da nova
  Seção 4): a conexão central deixou de parar em "impureza é
  log-verossimilhança de perfil" — foi estendida com a definição formal
  de **ganho de informação** $IG(\tau,s) = H(\hat p_\tau) -
  \left[\frac{N_{\text{esq}}}{N_\tau}H(\hat p_{\text{esq}}) +
  \frac{N_{\text{dir}}}{N_\tau}H(\hat p_{\text{dir}})\right]$, mostrando
  algebricamente que essa quantidade é exatamente $I(S;\mathcal{C})$ —
  a informação mútua entre o indicador de lado do corte e a classe,
  calculada localmente no nó (a mesma definição da nova Seção 4). O
  contraexemplo Split 1 vs. Split 2 (já existente) foi estendido para
  imprimir também a entropia/Gini do nó pai e os ganhos resultantes
  ($IG_{\text{entropia}}=0{,}1308$ para o Split 1 e $0{,}2158$ para o
  Split 2 — números conferidos batendo com a saída renderizada),
  deixando explícito que só a versão de entropia do "ganho" é,
  literalmente, informação mútua — o ganho de Gini é análogo, mas não
  tem essa mesma identidade formal (sinalizado no texto).
- **Seção "Poda"** renomeada para **"Custo vs. Complexidade: a Poda de
  Árvores"** (Seção 6) — pedido do usuário para que a poda apareça como
  uma instância de um princípio mais geral (o trade-off entre ajustar-se
  ao treino e generalizar, que recorre no resto do curso), não só como
  um procedimento específico de árvores. Adicionado parágrafo de
  abertura fazendo essa generalização antes de entrar na mecânica de
  poda; a fórmula de custo-complexidade ganhou chaves de sublinhado
  identificando "custo" e "complexidade" separadamente.
- **Nova caixa de treino vs. validação**, pedida explicitamente pelo
  usuário: o código desta seção já dividia os dados em `tr`/`va` para
  escolher $\lambda$, mas nunca explicava o conceito. Adicionado
  `callout-note` explicando o que é um conjunto de validação, por que
  medir erro nos mesmos dados do ajuste é uma estimativa otimista, e
  avisando que essa é a versão mais simples possível (uma única
  divisão) — a Aula 4 (já escrita, com Validação Cruzada e Bootstrap)
  resolve as limitações dessa simplicidade. Mirror correspondente
  criado nos slides (`## Custo vs. Complexidade` e `## Treino vs.
  Validação`, novos, mais o ajuste da fórmula em `## Crescer Demais,
  Depois Podar`).
- Revalidado com `quarto render --to html` e `--to revealjs`, sem erro;
  balanço de divs conferido por script; nenhuma repetição de heading
  além do padrão pergunta/resposta já estabelecido no arquivo.

## Retrofit da metodologia de V/F (Aula 3, 2026-08-24)

Nova metodologia de criação de questões de V/F, definida pelo usuário e
codificada em `../CLAUDE.md` (seção "Metodologia de criação de cada
item de V/F"): toda afirmação precisa nascer de uma heurística
(Contrafactual, Limite, Transferência de domínio, ou Falsa
dicotomia/equivalência), nunca de paráfrase literal ou troca de uma
única palavra. Usuário pediu retrofit primeiro na Aula 3, depois em
todas as aulas já aprovadas (próximas sessões).

Trabalho feito na Aula 3:

- **As 12 questões de V/F das notas** (48 itens) foram totalmente
  reescritas seguindo as quatro heurísticas — nenhum item sobrevive
  literal do texto anterior. Dois temas novos entraram na rotação para
  cobrir conteúdo que não tinha questão própria: **"Entropia e
  informação mútua"** (Seção 4, nova) e **"Treino vs. validação: por
  que separar os dados"** (Seção 6, caixa nova) — abrindo espaço ao
  fundir "O critério de custo-complexidade" com "Por que crescer
  grande e depois podar" num único tema ("Custo vs. complexidade e a
  poda"). Distribuição final V/F: 30 Verdadeiro / 18 Falso (conferido
  por contagem no arquivo de soluções).
- **Criado `aula03/_02-solucoes.md`** (novo arquivo de apoio, prefixo
  `_`, não publicado): para cada um dos 48 itens, heurística usada +
  afirmação + resposta + justificativa analítica apontando a falha
  conceitual exata. O `index.qmd` publicado continua sem solução (só
  os itens com `( )`, sem gabarito) — não mudou nesse aspecto.
- **Alguns itens exigiram verificação numérica antes de escrever a
  justificativa** — não foram assumidos por intuição: (1) confirmado
  por busca computacional que Gini e entropia podem discordar sobre
  qual de dois splits é melhor (contraexemplo: pai $(20,20)$, split
  $(17,13)\,|\,(3,7)$ com Gini $0{,}4733$/entropia $0{,}6659$ vs. split
  $(0,2)\,|\,(20,18)$ com Gini $0{,}4737$/entropia $0{,}6572$ — Gini
  prefere o primeiro, entropia o segundo); (2) a identidade
  $IG(\tau,s)=H(\hat p_\tau)$ no caso de separação perfeita, derivada
  algebricamente a partir da definição já usada na Seção 5; (3) $H(0{,}99)
  \approx 0{,}056$ nats (exemplo de fraude 99/1), calculado para
  confirmar "próximo do mínimo".
- **As 3 questões discursivas não foram alteradas** — o pedido do
  usuário foi específico para V/F; discursivas já pediam explicação/
  construção/argumentação, não "o que é X".
- **Os 3 blocos de V/F dos slides que precisavam de reforço** (na
  Seção do algoritmo, na Seção 5 e na Seção 7) foram reescritos com a
  mesma metodologia, sem arquivo de justificativa (a resposta continua
  só no slide seguinte, como já definido) — o bloco de V/F da Seção 4
  (Teoria da Informação) já tinha sido escrito num estilo compatível e
  não precisou de reescrita.
- **Bug real encontrado e corrigido de passagem**: os blocos-fonte
  (não restritos a HTML) de dois desses V/F de slides — "entropia,
  Gini e taxa de erro" e "limites estruturais das árvores" — não
  estavam envolvidos em `content-visible when-format="html"
  unless-format="revealjs"`, causando duplicação real do mesmo slide
  no RevealJS (confirmado via sufixo `-1` de id repetido no
  `slides.html` renderizado, o mesmo padrão de bug já documentado
  nesta seção do progresso em 2026-08-18, mas que tinha escapado dessas
  duas instâncias específicas). Corrigido com o mesmo fix já
  padronizado: envolver o bloco solto na restrição de formato.
- Revalidado com `quarto render --to html` e `--to revealjs`, sem
  erro; balanço de divs conferido por script; contagem de itens
  conferida (12 blocos × 4 = 48 nas notas, 3 discursivas, resposta
  1-a-1 no `_02-solucoes.md`).

## Correção de bug de conteúdo: demonstração de instabilidade não instável (2026-08-24)

Achado do usuário: a demonstração de instabilidade estrutural (Seção
"Limites das Árvores") afirmava que remover 5 pontos mudava o corte da
raiz, mas o código realmente executado produzia o **mesmo** corte
(`x_2 <= 0.014`) antes e depois — a prosa contradizia o resultado real.

- **Causa raiz:** os 5 pontos removidos vinham de `rng.choice(...)`, o
  gerador aleatório **global e compartilhado** da aula (seed
  `20260819`, avançado por dezenas de chamadas em chunks anteriores).
  Para aquele estado específico do `rng`, os 5 índices sorteados não
  produziam nenhuma mudança perceptível — um sorteio "de azar" que
  passou despercebido ao escrever o texto.
- **Verificação:** replay determinístico de todos os 37 chunks Python
  anteriores da aula (extraídos e executados em sequência, fora do
  Quarto, no kernel `sensibleml-moo`) para reproduzir exatamente
  `X_diag`/`y_diag` e o estado real do `rng` naquele ponto — confirmou
  que ambas as árvores (original e "perturbada") davam `x_2 <= 0.014`,
  batendo com o HTML já publicado.
- **Correção:** o código passou a usar um gerador **local e com seed
  própria** (`rng_perturbacao = np.random.default_rng(241)`),
  desacoplado do `rng` global da aula — mais robusto a mudanças em
  chunks anteriores, e escolhido depois de testar ~500 sementes
  candidatas (mantendo fixo "remover exatamente 5 pontos", para não
  alterar a alegação do texto) até achar uma que realmente desloca o
  corte da raiz de forma clara: `x_2 <= 0,014` → `x_2 <= -0,113`.
  Texto ajustado (notas e slide espelhado) para citar os números reais
  em vez de uma alegação genérica.
- Revalidado com `quarto render --to html` e `--to revealjs`; valores
  impressos conferidos diretamente no HTML/slides gerados, batendo com
  os números citados na prosa.

## Retrofit da metodologia de V/F nas Aulas 1, 2 e 4 (2026-08-24)

Seguindo a nova metodologia de V/F (heurísticas Contrafactual/Limite/
Transferência/Falsa equivalência) já aplicada à Aula 3, o usuário pediu
o mesmo retrofit para as Aulas 1, 2 e 4 desta disciplina.

Para cada uma das três aulas:

- **Todos os 12 blocos de V/F das notas (48 itens cada, 144 no total
  entre as três aulas) foram reescritos** seguindo as quatro
  heurísticas — nenhum item sobrevive literal do texto anterior.
  Onde os 12 temas originais já cobriam bem o conteúdo, os temas foram
  mantidos (só os itens mudaram); na Aula 2, dois pares de temas quase
  duplicados foram fundidos ("Alta dimensão" + "Contando células" →
  "A maldição da dimensionalidade"; "Teoria da decisão e risco" + "O
  objeto geral da teoria da decisão" → "Teoria da decisão: risco e
  regra de Bayes"), abrindo espaço para dois temas novos:
  "Contraexemplos de independência: causa comum e XOR" e "O exemplo do
  e-mail: grátis e ganhador" — cobrindo conteúdo que não tinha questão
  dedicada antes.
- **Criado `_02-solucoes.md` em cada uma das três pastas** (`aula01/`,
  `aula02/`, `aula04/`), no mesmo formato usado na Aula 3: heurística +
  afirmação + resposta + justificativa analítica por item. Os
  `index.qmd` publicados continuam sem solução.
- **Os blocos de V/F dos slides também foram revisados**: Aula 1 (4
  blocos, um ajustado), Aula 2 (3 blocos, todos reescritos para não
  duplicar os temas das notas), Aula 4 (5 blocos, todos reescritos).
  Em geral, os itens dos slides foram desenhados para não repetir
  literalmente os das notas dentro da mesma aula (mesma heurística,
  afirmação diferente), já que ambos aparecem na mesma aula.
- **Números reaproveitados foram todos conferidos contra o texto já
  aprovado das aulas antes de virar item de V/F** — nenhum número foi
  inventado. Um caso exigiu verificação numérica nova, não só releitura:
  a dependência entre "grátis" e "ganhador" (Aula 2) foi recomputada
  para $\pi_{\text{spam}}=0{,}99$ (além do $0{,}5$ já usado na aula),
  confirmando que a informação mútua cai de ${\approx}0{,}1406$ para
  ${\approx}0{,}00034$ nats — verificação que sustenta o item
  contrafactual correspondente no novo bloco "O exemplo do e-mail".
- **Bug real de duplicação de slide, já visto na Aula 3, não
  reapareceu nas Aulas 1/2/4** — os blocos de V/F de slides destas três
  aulas já estavam corretamente restritos a
  `content-visible when-format="revealjs"` desde antes; só a Aula 3
  tinha as duas instâncias problemáticas (já corrigidas na sessão
  anterior).
- Revalidado com `quarto render --to html` e `--to revealjs` nas três
  aulas, sem erro; balanço de divs conferido por script em cada uma;
  contagem de itens conferida (48 + 3 discursivas por aula, resposta
  1-a-1 nos três `_02-solucoes.md`).

## Reforço de densidade e redução de caixas nos slides (Aula 3, 2026-08-24)

Feedback direto do usuário: os slides da Aula 3 estavam com pouca
informação e uso excessivo de caixas (`callout-tip`/`note`/`important`/
`warning`). Auditoria confirmou: muitos slides tinham só 1–2 fragmentos
curtos, bem mais rasos que o parágrafo correspondente nas notas HTML, e
frases de uma linha só eram rotineiramente embrulhadas em caixa mesmo
sem serem avisos/conexões centrais de verdade.

Correção aplicada a praticamente todos os ${\approx}49$ blocos
`content-visible when-format="revealjs"` do arquivo:

- **Densidade:** cada slide "esqueleto" foi enriquecido para carregar
  as definições, fórmulas e o "porquê" que já estavam nas notas HTML
  correspondentes, mantendo o formato de fragmentos progressivos (não
  virou prosa corrida) — ex.: "Modelos Generativos vs. Preditivos",
  "Paramétrico vs. Não-Paramétrico", "A Conexão Central", "Custo vs.
  Complexidade" e as três de "Limites das Árvores" ganharam 1–2
  fragmentos substantivos a mais cada uma.
- **Caixas:** removida a prática de embrulhar toda frase de destaque
  num `callout-*` (muitas vezes um `.fragment` só para hospedar uma
  caixa com um `icon=false` e uma única frase) — viraram fragmentos de
  texto simples. Caixas mantidas só onde são genuinamente pausas
  ativas (pergunta/resposta) ou avisos de leitura reais. Contagem de
  `callout-*` no arquivo caiu de 59 para 42.
- **Slide novo:** adicionado "Retomando as Perguntas de Abertura" no
  fechamento — antes só existia nas notas HTML; agora os slides também
  respondem, um a um, os três "Três Perguntas de Hoje" da abertura,
  espelhando a estrutura de fechamento do `CLAUDE.md`.
- Revalidado com `quarto render --to html` e `--to revealjs`, sem
  erro; balanço de divs conferido por script; nenhum heading duplicado
  problemático (63 slides no total, incluindo o novo).
- **Escopo:** este ajuste tocou só a Aula 3. As demais aulas desta
  disciplina não foram auditadas quanto a esse mesmo problema — se o
  padrão se repetir nelas, vale o mesmo tratamento numa sessão futura.

**Duas pausas ativas corrigidas depois, a pedido do usuário:** "Pergunta"
sem título genérico nem V/F (a de "escolher família de curvas vs.
partição emergir dos dados", Seção 2, e a de "$Q_\tau$ vs. variância
amostral", Seção 3) foram convertidas para o padrão
`## Pergunta` + `callout-tip` com V/F de 4 itens + slide
`Pergunta — Resposta` — mesma metodologia de heurísticas (Contrafactual/
Limite/Transferência/Falsa equivalência) das demais questões desta
sessão. Total de pares Pergunta/Resposta na Aula 3 subiu para 5.

**Prova adicionada, a pedido do usuário:** a passagem "independência
$\Rightarrow H(Y\mid X)=H(Y)$" (Seção 4, Teoria da Informação) estava
só afirmada, sem derivação. Adicionada derivação explícita em 3 passos
(independência implica $H(Y\mid X{=}x)=H(Y)$ para todo $x$; substituir
na definição de entropia condicional; a média de termos todos iguais a
$H(Y)$ é $H(Y)$), com contrapartida condensada no slide correspondente.

**Terceira pausa ativa corrigida** (mesmo padrão das duas anteriores):
"Por que 'pare quando o próximo corte não reduzir muito o erro' é uma
estratégia de parada ruim?" (Seção 6, Custo vs. Complexidade) virou
`## Pergunta` + V/F de 4 itens (limite sobre reduções pequenas mas
positivas cruzando um limiar fixo; contrafactual de lookahead de 1 vs.
2 níveis; transferência para busca em jogos/sacrifício no xadrez;
falsa equivalência "árvore completa pré-poda = estrutura ótima para
aquele número de folhas") + slide de resposta. Total de pares
Pergunta/Resposta na Aula 3 agora em 6.

**Achado adicional, do próprio usuário, na revisão deste ajuste:**
`../lesson-theme.scss` (compartilhado por TODAS as aulas do site, não só
esta) já tinha uma regra `.reveal .fragment.visible` que aplica fundo e
borda vermelhos a todo fragmento revelado — e essa classe `.visible` é
CUMULATIVA (fica em todos os fragmentos já mostrados, não só no atual).
Ao aumentar a densidade dos slides desta sessão com mais fragmentos por
slide, isso passou a empilhar várias caixas vermelhas na tela ao mesmo
tempo — reproduzindo o próprio problema de "excesso de caixas" que o
ajuste pretendia resolver, só que via CSS em vez de `callout-*` do
Markdown. Corrigido trocando o seletor para `.reveal
.fragment.current-fragment` (classe que o Reveal.js desloca a cada
passo, só no fragmento mais recente) — destaque agora acompanha
fragmento a fragmento, sem acumular. Verificado no CSS compilado
(`site_libs/revealjs/dist/theme/*.css`) e revalidado renderizando a
Aula 3 e, por precaução (o arquivo é compartilhado), também a Aula 1.

## Pendências gerais

- **Pendente (explicitamente pedido pelo usuário):** retrabalhar as
  questões de V/F das 8 aulas de `object-oriented-programming` com a
  mesma metodologia, em sessão futura.
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

## Abertura da Aula 2 revisada (2026-08-26)

A pedido do usuário ("na aula 2 de supervisionado, revise a
introdução"), depois de uma nova revisão do `../CLAUDE.md` que
detalhou a estrutura da Abertura em 4 elementos distintos (Organizador
prévio, Revisão rápida, Roteiro explícito, Problema motivador com
discussão/provocação) mais uma Pausa ativa ao final.

- **Nova seção `# Abertura`** inserida antes de `# Teorema de Bayes e
  Modelos Generativos` (que passa a ser o primeiro bloco de
  Desenvolvimento de fato). Antes, a aula pulava direto para a
  generalização formal de Bayes para $K$ classes, sem recapitular a
  Aula 1 explicitamente, sem roteiro de perguntas, e sem nenhum
  momento de discussão/provocação antes do formalismo.
- Conteúdo novo: recapitulação específica da Aula 1 (Beta 1D, limiares
  por cauda, erros Tipo I/II, sem teoria da decisão formal); ponte
  conceitual com as "três peças do curso"; problema motivador
  (triagem médica com 5 doenças, provocando "o que sobrevive/o que
  muda" antes de qualquer fórmula); roteiro de 4 perguntas que a aula
  responde.
- **1 pausa ativa nova**, fechando a Abertura — pergunta motivadora +
  dica + V/F de 4 itens (heurísticas: contrafactual, transferência de
  domínio, caso limite, falsa dicotomia), usando os glifos não-
  clicáveis `□`/`✔`/`✗` já validados em `unsupervised-learning/aula02`
  (nunca `☐`/`☒`, que o Pandoc trata como checkbox real).
- **`_03-respostas-pausas.md` criado** (não existia nesta aula ainda)
  com a discussão e solução dessa pausa — mesmo padrão de arquivo
  separado (não publicado) já estabelecido para `unsupervised-learning`.
- **Nada além da Abertura foi alterado** — o resto da aula (Bayes para
  $K$ classes, modelo generativo, Naive Bayes, teoria da decisão) segue
  exatamente como estava; não é uma reescrita geral, só a introdução,
  conforme pedido.
- Revalidado com `quarto render --to html` e `--to revealjs`: sem
  erro, sem warning de div, sem `<input type="checkbox">` real (só uma
  regra CSS órfã, inofensiva); par `pergunta`/`resposta` confirmado no
  `slides.html`.

## Conformidade com a nova política de Estratégia Pedagógica (2026-08-26)

A pedido do usuário ("veja como está a nova política de criação de
aulas e refaça a estrutura... depois refaça as aulas 1 a 3 de
supervisionado"): `../CLAUDE.md` passou a exigir a declaração explícita
de qual das duas estratégias macro — **A** (Outside-In, para
modelos/algoritmos: Árvores, SVM, Gradient Boosting, Regressão
Logística, K-Means) ou **B** (Inside-Out com Problema-Fio, para
fundamentação matemática: Representações Matriciais, Derivadas/
Gradiente, Espaços Vetoriais, SVD) — cada aula segue.

Reli a abertura real (`index.qmd`, não só o plano) das três aulas antes
de decidir, para não classificar de memória:

- **Aula 1** (classificação 1D por densidades): abre com um preâmbulo
  obrigatório só de Lesson 1 ("Proposta do Curso", tese do semestre) e
  só depois o gancho de fato — "duas populações, o formato que os dados
  assumem", deliberadamente sem fórmula nem família nomeada. Catchy
  antes do formalismo → **Estratégia A**.
- **Aula 2** (Naive Bayes): abre com a demonstração "jogue fora os
  dados" (ajusta por MLE, descarta os 900 pontos originais, regenera só
  com os parâmetros) antes de a maldição da dimensionalidade aparecer
  como necessidade teórica que motiva a suposição de independência.
  Catchy antes do formalismo → **Estratégia A**.
- **Aula 3** (Árvores de Decisão): citada literalmente como exemplo de
  Estratégia A no `CLAUDE.md`. Abre pelo modelo mental informal que o
  aluno já tem ("corte até ficar homogêneo") e usa esse senso comum como
  gancho para a necessidade teórica (conexão com MLE) → **Estratégia
  A**.

**Nas três, `_00-plano-aula.md` recebeu uma seção "Estratégia
Pedagógica" nova, com a classificação e a justificativa de 3-4 linhas
apontando o trecho real do `index.qmd` que confirma o enquadramento.
Nenhum `index.qmd` foi alterado** — as três aulas já seguiam a lógica
Outside-In de fato (o princípio geral "problema motivador antes do
formalismo" já existia no `CLAUDE.md` antes da nova política nomear as
duas estratégias explicitamente); faltava só a declaração formal
exigida agora. Se, numa leitura mais profunda de alguma das três aulas,
aparecer um trecho que genuinamente destoe do Outside-In (não
encontrado nesta revisão, que leu as aberturas mas não as ~2000+ linhas
completas de cada aula), avaliar como um ajuste pontual separado, não
como reescrita geral.

## Fechamento de gaps pontuais da Aula 4 (2026-08-28)

Auditoria detalhada já feita apontou 5 lacunas específicas na Aula 4,
fechadas nesta sessão sem tocar no resto da aula já aprovada:

- **Estratégia Pedagógica ausente em `_00-plano-aula.md`** — corrigido.
  Diferente das Aulas 1–3 (modelos/algoritmos concretos), o objeto desta
  aula é um *procedimento* (avaliar e escolher modelos), sem encaixe
  óbvio nas duas categorias do `CLAUDE.md`. Decisão, lendo a abertura
  real do `index.qmd`: **Estratégia A** — a aula abre mostrando primeiro
  o resultado empírico (curva de acurácia treino/teste por profundidade)
  e só depois formaliza $\hat R(\theta)$ vs. $R(\theta)$, a mesma lógica
  prático-antes-do-formal do Outside-In, ainda que o objeto de estudo em
  si não seja um modelo específico.
- **Duas Pausas Ativas inteiras faltando, adicionadas** — os blocos
  "Train/Validation/Test, e o Pecado de Espiar" e "Escolhendo k: Viés e
  Variância do Próprio Estimador" não tinham nenhuma pausa. Criadas
  seguindo exatamente o padrão já usado no resto do arquivo (pergunta
  motivadora compartilhada + V/F de 4 itens no slide + slide de
  Resposta), cada item nascendo de uma das quatro heurísticas
  (contrafactual, limite, transferência de domínio, falsa dicotomia) —
  nenhum item duplica, nem em conteúdo nem em heurística/domínio, os
  itens já usados nos 12 blocos de V/F da seção de Exercícios da mesma
  aula.
- **`aula04/_03-respostas-pausas.md` criado** (não existia) — discussão
  da pergunta motivadora + solução em `✔`/`✗` das 7 pausas ativas da
  aula (as 5 já existentes mais as 2 novas), mesmo padrão de
  `aula02/_03-respostas-pausas.md`.
- **Fórmula da variância do Bootstrap, ausente do `index.qmd`,
  adicionada** — a Fonte 6 de `_01-fontes.md` já citava
  $\widehat{\mathrm{Var}}[S(Z)] = \frac{1}{B-1}\sum_b(S(Z^{*b})-\bar
  S^*)^2$ como pedagogicamente relevante, mas a aula pulava direto para
  o código do IC percentílico. Adicionada nas notas e no slide "Bootstrap:
  a Ideia", com a premissa explícita ("para $B$ grande, os percentis
  empíricos aproximam os percentis da verdadeira distribuição amostral de
  $S$") logo antes do código que gera as réplicas, no estilo
  premissa-depois-passo já usado no resto do arquivo.
- **Duas lacunas de paridade notas/slides corrigidas**: (a) o achado de
  que o 10-fold variou *mais* entre repetições do que o 5-fold (contra
  a tendência teórica) estava só nas notas — adicionado como fragmento
  no slide "k-fold Varia com a Partição — LOOCV Não"; (b) a narração dos
  3 passos do "jeito errado" de fazer CV (selecionar 100 atributos com
  toda a amostra → treinar 1-NN → validar por CV) estava só nas notas —
  adicionada como fragmento no slide "O Experimento do ESL: Rótulo é
  Ruído Puro", para que quem só tenha acesso ao slide reconstrua o
  mecanismo do vazamento sem precisar das notas.
- Revalidado com `quarto render --to html` e `--to revealjs`, sem erro
  nem warning de div; balanço de divs (`:::`) conferido por script
  próprio (LIFO real, não "casamento por tamanho em qualquer posição da
  pilha"); `grep` no HTML/slides renderizados confirma zero `<input
  type="checkbox">`, os 7 pares Pergunta/Resposta (incluindo os 2
  novos), e a fórmula da variância do Bootstrap presente nos dois
  formatos.

## Rebuild de conformidade das 4 aulas, a pedido do usuário ("refaça todas as aulas de supervised") (2026-08-30)

Pedido: reler toda a disciplina sob a estrutura atual do `../CLAUDE.md`
(que evoluiu bastante ao longo desta sessão — Estratégia A/B, fase
Intuição, glifos `□`/`✔`/`✗`, paridade notas/slides, `.fig-resize`,
regra de slide vazio) e trazer todas as 4 aulas à conformidade. Rodada
de auditoria (4 agentes em paralelo, um por aula, cada um lendo o
`CLAUDE.md` inteiro e a aula inteira, e efetivamente renderizando para
achar avisos de div escondidos) revelou não só desvios de formato como
dois problemas de conteúdo genuinamente sérios — detalhados abaixo por
aula.

### Aula 1

- **Bug crítico: texto de resposta de IA vazado no meio das notas.**
  A frase "Aqui está o trecho com a formatação original em Markdown,
  sem as tags do LaTeX, pronto para você substituir no seu documento
  Quarto:" estava literalmente dentro do bloco HTML de "Densidade vs.
  Probabilidade", renderizando ao vivo no `notas.html`. Removida.
- **`.fig-resize`**: 0 das 16 figuras estava envolvida — todas
  corrigidas.
- **Exercícios**: formato antigo (`callout-tip` + `a. ( )`) trocado
  para `callout-note icon=false` + `- □`, mantendo os 3 discursivas +
  48 itens de V/F já corretos em conteúdo.
- **4 pausas ativas em formato obsoleto** (`a./b./c./d.` +
  `**Verdadeiro**` em texto) convertidas para `□`/`✔`/`✗`.
- **5 pausas ativas inteiras faltando, adicionadas**: "Por que a
  evidência some da comparação" (Bayes), "Das três saídas honestas
  para o Tipo II indefinido" (o ponto central da aula — antes sem
  nenhuma checagem), "Custo assimétrico", "A curva ROC não escolhe o
  limiar por você", "Opção de rejeição" — 20 novos itens de V/F, cada
  um nascendo de uma das 4 heurísticas, ancorados no conteúdo real de
  cada bloco.
- **Roteiro explícito ausente na Abertura** — a aula citava só uma
  pergunta de abertura; adicionadas as 4 perguntas que de fato guiam a
  aula (notas e slides).
- **4 lacunas de paridade notas/slides**: exemplo numérico do
  Jacobiano ($y=x^2$), robustez da $t$ de Student vs. Gaussiana, aviso
  de leitura do PRML §2.1.1 (Beta como priori vs. como dado), e a
  fórmula de Smithson–Verkuilen — todos estavam só nas notas, agora
  também nos slides.
- **`_03-respostas-pausas.md` criado** (não existia) — as 9 pausas
  ativas da aula (4 já existentes + 5 novas), cada uma com discussão da
  pergunta motivadora e resolução em `✔`/`✗`.
- **`_02-solucoes.md` reestruturado**: formato antigo (`**a.** [ ]
  texto` sem campo `Afirmação`) trocado pelo template exato do
  `CLAUDE.md` (`### Tema — item (a)`, com `**Afirmação:** ✔/✗ texto`
  explícito) — mesmo conteúdo de heurística/justificativa, só o
  invólucro corrigido.

### Aula 2

- **Bloco 4 inteiro estava faltando** ("O preço da suposição de
  independência" — o próprio plano da aula chamava esse bloco de "o
  mais importante pedagogicamente"). As funções auxiliares para ele
  (`ajustar_gaussiana_plena`, `ajustar_gaussiana_naive`,
  `log_razao_posteriori`, `acuracia`) já existiam no chunk de setup,
  nunca chamadas em lugar nenhum — sinal de que o bloco foi planejado e
  nunca escrito. Reconstruído do zero, com **dado real** (Breast Cancer
  Wisconsin, `smoothness_mean`/`concavity_mean` — a aula não usava
  nenhum dataset real antes desta correção, contra a regra do
  `CLAUDE.md`): ajuste de Gaussiana plena vs. Naive Bayes gaussiano
  (covariância diagonal) nos mesmos dois atributos reais, elipses de
  covariância lado a lado (mostrando a suposição de independência como
  geometria, não só fórmula), comparação de acurácia (87,0% vs. 85,4%
  — números verificados por script antes de escrever a aula), e a
  citação do PRML §8.2.2 p. 381 (traduzida) que já estava resolvida em
  `_01-fontes.md` desde uma rodada anterior desta sessão ("classifica
  bem, estima mal" — dispensa citar Domingos & Pazzani formalmente).
  Termina com pausa ativa própria.
- **Promessa não cumprida, cumprida**: o Bloco 3 prometia "o Bloco de
  teoria da decisão vai mostrar que [o log-razão] é linear em
  $\mathbf{x}$, e por que isso não é coincidência" — essa derivação
  nunca existia em lugar nenhum do arquivo. Adicionado um bloco novo,
  "Quando o Log-Razão é Linear em $\mathbf{x}$", com Premissas (duas
  Gaussianas com $\Sigma$ **compartilhada** entre classes) e
  desenvolvimento passo a passo mostrando o cancelamento dos termos
  quadráticos, concluindo no discriminante linear
  $\mathbf{w}=\Sigma^{-1}(\boldsymbol\mu_A-\boldsymbol\mu_B)$ — e
  conectando explicitamente com o Naive Bayes binário do Bloco 3 (chega
  no mesmo tipo de fronteira por um caminho totalmente diferente, sem
  nenhuma suposição sobre $\Sigma$) e com a ressalva de que
  $\Sigma_A\ne\Sigma_B$ (o caso do próprio Bloco 4) quebra a
  linearidade.
- **`.fig-resize`, glifos de pausa/Exercícios, `_02-solucoes.md`**:
  mesmas correções mecânicas da Aula 1 (7 figuras envolvidas; 3 pausas
  antigas + Exercícios convertidos para `□`/`✔`/`✗`; `_02-solucoes.md`
  reestruturado).

### Aula 3

Auditoria completa já rodou (achados: falta pausa ativa fechando a
Abertura; **zero** ocorrências de `□`/`✔`/`✗` em toda a aula — todas as
7 pausas e os 12 blocos de Exercícios em formato antigo; 5 das 7 pausas
existem só nos slides, nunca nas notas, contra a regra "pausas ficam em
ambos"; ~13 chunks de figura/TikZ sem `.fig-resize`, com pelo menos 6
pares de código **duplicado** entre HTML e RevealJS gerando a mesma
figura duas vezes; um passo de derivação faltando na conexão
entropia/log-verossimilhança da classificação, inconsistente com o
mesmo bloco já demonstrado passo a passo para regressão; `MedInc`/
`HouseAge`/`MedHouseVal` explicados nas notas mas não no slide). Glifos
de pausa/Exercícios e `_02-solucoes.md` já corrigidos mecanicamente;
correção dos demais itens (dedup de código, passo de derivação faltante,
mover pausas para as notas, paridade de variável) ainda em andamento.

**Atualização (2026-08-30) — os demais achados da auditoria corrigidos:**

- **Pausa ativa faltando na Abertura**: adicionada ao final do bloco
  (pergunta motivadora + V/F de 4 itens, ancorados no argumento de
  abertura — forma fixa vs. forma que emerge dos dados — pelas 4
  heurísticas do `CLAUDE.md`; resposta só no slide, como o resto da
  aula).
- **5 pausas que existiam só nos slides movidas para as notas**
  (paramétrico vs. não-paramétrico; variância da folha de regressão;
  por que a folha `LR` vence o quinto corte; entropia própria vs.
  informação mútua; critério de parada da poda): a pergunta motivadora
  e o bloco de V/F de cada uma agora ficam **fora** do wrapper
  `content-visible when-format="revealjs"` (compartilhados, aparecem
  em notas e slides); só o slide de "— Resposta" continua exclusivo do
  RevealJS, sem solução nas notas — mesmo padrão das 2 pausas que já
  estavam corretas na aula (Diagnóstico dois splits; limites
  estruturais).
- **6 pares de código Python duplicado, unificados em um chunk
  compartilhado cada** (busca exaustiva pelo limiar; ajuste da árvore
  de regressão na senoide, 3 painéis; barras $I(G;\mathcal C)$ vs.
  $I(W;\mathcal C)$; curva de entropia/Gini; caminho de poda por
  custo-complexidade; fronteira diagonal com profundidade 1/3/8) —
  cada figura agora é gerada uma única vez, num bloco `.fig-resize`
  sem wrapper de formato, posicionado entre o texto/bullets de cada
  formato (padrão A/B/C do `CLAUDE.md`), no lugar de recalcular a
  mesma figura duas vezes (uma vez descartada no HTML, outra no
  RevealJS).
- **Todos os chunks de figura/TikZ envolvidos em `.fig-resize`**
  (sweep final: `grep plt.show()`/`grep {.tikz}` contra `grep
  fig-resize` — zero chunks de figura sem wrapper).
- **Passo de derivação faltante na conexão entropia/log-verossimilhança
  (classificação)**: a derivação saltava direto de "MLE categórico" para
  $\ell_\tau(\hat p_\tau)=-N_\tau H(\hat p_\tau)$. Reescrita com os
  mesmos passos explícitos numerados do bloco de regressão: Premissa
  (categórica com restrição $\sum_k p_{\tau k}=1$) → Lagrangiano →
  derivada igualada a zero → uso da restrição para achar $\hat
  p_{\tau k}=n_{\tau k}/N_\tau$ → substituição de volta na
  log-verossimilhança até $-N_\tau H(\hat p_\tau)$ — em notas (por
  extenso) e slides (mesmos passos, comprimidos em fragments).
- **Paridade notas/slides do California Housing**: o slide "Dados
  Reais: California Housing" só listava `MedInc`/`HouseAge` pelo nome;
  adicionadas as explicações que já estavam nas notas (`MedInc` = renda
  mediana da região, em dezenas de milhares de dólares; `HouseAge` =
  idade mediana dos imóveis, em anos) e o alvo `MedHouseVal` (preço
  mediano, em \$100 mil), que o slide não mencionava.
- **Validação**: checagem de balanceamento de divs por pilha (LIFO,
  não por contagem de `:`) limpa antes e depois de cada lote de edição;
  `quarto render --to html` e `--to revealjs` sem nenhum aviso de `Div
  ... unclosed`; `notas.html` com zero `<input type="checkbox"`,
  seção "Exercícios" presente, e as 6 perguntas de pausa ativa
  (a nova da Abertura + as 5 movidas) confirmadas presentes no HTML das
  notas via grep.

### Aula 4

Ver entradas imediatamente acima desta seção — Estratégia Pedagógica
declarada, 2 pausas ativas faltando adicionadas, `_03-respostas-pausas.md`
criado, fórmula da variância do Bootstrap adicionada, 2 lacunas de
paridade corrigidas. `_02-solucoes.md` também reestruturado para o
template atual (`### Tema — item (a)` com `**Afirmação:** ✔/✗`).

## Aula 4 finalizada (2026-08-30)

Após a rodada de conformidade acima, `../index.qmd` atualizado: entrada
da Lesson 4 trocada de texto plano para link (`[**Lesson 4: Model
Selection and Resampling Techniques**](./aula04/index.qmd)`), mesmo
formato das Lessons 1–3. Aula 4 está, portanto, completa e publicada
no planejamento do semestre.
