# Progresso — Optimization and Linear Algebra for Machine Learning

Estrutura conforme `CLAUDE.md`: `index.md` é o planejamento do semestre
(formatado para Hugo, com link de cada aula pronta); cada aula é
`aulaNN/` com `00-plano-aula.md`, `01-fontes.md`, `02-aula.qmd`. Fontes em
`fontes/`: `mathml.pdf` (Deisenroth, Faisal & Ong — *Mathematics for
Machine Learning*, 2024), `copt.pdf` (Boyd & Vandenberghe — *Convex
Optimization*), `optml.pdf` (Wright & Recht — *Optimization for Data
Analysis*) — os dois últimos reservados para a Parte 2/3 do curso
(Aulas 6+), ainda não usados.

## Aula 1 — Vector Spaces, Norms, Inner Products, and Metrics

O `02-aula.qmd` já vinha pronto ("já está boa", nas palavras do usuário) —
esta sessão construiu a estrutura de apoio em volta dele, não reescreveu o
conteúdo, exceto por uma correção matemática pontual.

- [x] `00-plano-aula.md` — reconstruído a partir do `plan.md` anterior
      (que era uma colagem de conversa de chat, não um plano de aula) mais
      leitura completa do `.qmd` real. 6 blocos, ~125 min (acima da
      estimativa original de 90–120 min do `plan.md`, por causa de conteúdo
      que o plano não previa: prova da métrica do cosseno, Swiss Roll,
      duas luas, fechamento com RAG).
- [x] `01-fontes.md` — 7 fontes do `mathml.pdf`, todas com trecho literal
      já extraído (offset confirmado: **+6** entre página impressa e PDF,
      diferente do +20 usado nos livros de `supervised`). $k$-NN,
      variedades/manifolds e RAG não têm lastro no MathML — são
      contribuições de ML da própria aula, sinalizado explicitamente no
      arquivo, não fabricado como citação.
- [x] `02-aula.qmd` — **um erro matemático real corrigido nesta sessão**:
      a prova de que a distância do cosseno ($d_{\cos}=1-\cos\theta$)
      satisfaz a desigualdade triangular tinha um passo inválido (elevar
      ao quadrado uma desigualdade de raízes e concluir a versão não
      elevada). Contraexemplo verificado numericamente (vetores a
      $0°,90°,135°$): a desigualdade falha de fato. Corrigido para a
      conclusão certa — $\sqrt{2\,d_{\cos}}$ (distância cordal) é métrica;
      $d_{\cos}$ em si não é, em geral. Também removido um artefato de
      geração (`[cite: 3]` solto no texto). YAML corrigido: tinha
      `output-dir: "aula1"` por formato, que conflitava com a convenção do
      projeto (`_quarto.yml` já define `output-dir`/`output-file` no nível
      do projeto) — removido, mais `date`/`lang` adicionados para
      consistência com `supervised`. Validado com `quarto render --to html`
      e `--to revealjs`, sem erro.

**Pendências registradas em `01-fontes.md`** (não bloqueiam a aprovação,
mas valem revisão): produto interno usado no Bloco 5 sem definição formal
prévia no Bloco 4 (a Fonte 5, MathML §3.2.2, cobre isso mas ainda não foi
citada no texto); $L_\infty$ sem exemplo nomeado localizado no MathML.

**Reavaliada em 2026-08-19** para se ajustar ao novo paradigma de aula do
`CLAUDE.md` (o mesmo já aplicado a `supervised` Aulas 1–3 e a
`unsupervised` Aula 1): roteiro explícito de 4 perguntas logo na
abertura (o arquivo não tinha uma seção de abertura separada — o roteiro
foi inserido como a primeira caixa do Bloco 1), 3 pausas ativas
(pergunta-título entre blocos: hipótese de suavidade antes do $k$-NN;
fechamento sob adição de uma esfera antes de introduzir variedades;
por que $L_1$/$L_2$/$L_\infty$ discordam sobre o "tamanho" de um vetor),
3 testes V/F nos slides — cada um com slide de resposta separado
(hipótese de suavidade e $k$-NN; espaços vetoriais/subespaços/variedades;
métricas/alta dimensão/cosseno) —, uma seção "Retomando as perguntas de
abertura" no fechamento, e a seção de Exercícios nas notas HTML (3
discursivas + 12 blocos de V/F, 48 itens, cobrindo os 6 blocos de ponta a
ponta). Diferente da reavaliação de `unsupervised`, este `.qmd` usa
`---` como separador explícito de slide dentro de um mesmo bloco
`content-visible` (convenção própria deste arquivo, não usada nos
outros); todo callout-tip novo foi conferido para não ficar "solto" (sem
`content-visible` restringindo o formato), que causaria slide duplicado
no Reveal.js — mesmo bug já corrigido antes na Aula 3 de `supervised`.
Conteúdo técnico não mudou (nem a correção da prova do cosseno feita
antes); só a estrutura pedagógica e os exercícios foram adicionados.
Revalidado com `quarto render --to html` e `--to revealjs` (mesmo
detalhe de ambiente `.venv` já registrado em `supervised/progresso.md`).

**Dados sintéticos trocados por dados reais em 2026-08-19** (aplicação
da diretriz "Dados: prefira exemplos reais a sintéticos" do
`CLAUDE.md`), em dois blocos:

- **Bloco 1** (espaço de características): a tabela fake de 5 imóveis
  virou uma amostra real de 5 bairros do **California Housing Dataset**
  (`gvlassis/california_housing` no Hugging Face Hub) — renda mediana
  vs. valor mediano do imóvel, com a ressalva explícita no texto de que
  cada ponto é um grupo de setores censitários, não um imóvel
  individual.
- **Bloco 2** (ilustração do $k$-NN): as duas nuvens gaussianas
  sintéticas viraram dados reais do **Breast Cancer Wisconsin Dataset**
  (`scikit-learn/breast-cancer-wisconsin`) — raio médio vs. textura
  média do núcleo celular, diagnóstico real (benigno/maligno). A
  paciente de consulta também é real (removida da vizinhança); achado
  ao explorar os dados: para essa paciente (diagnóstico real benigno),
  o voto por $k=3$ erra (maioria maligno, 2 a 1) — mantido no texto como
  lembrete honesto de que a escolha de $k$ não é neutra, com ponte
  explícita para a Aula 4 de `supervised` (seleção de modelo).

**Correção de padrão de slide em 2026-08-19**: as pausas ativas e os
testes V/F desta aula usavam a pergunta/tema inteiro como título real
do slide (heading hoisted para fora da caixa), com a caixa `callout-tip`
carregando só uma dica curta. O padrão correto — confirmado
explicitamente pelo usuário e agora documentado no `CLAUDE.md` — é
diferente: o título real do slide deve ser o rótulo genérico `Pergunta`
(e, no slide de resposta, `Resposta`), com a pergunta/tema específico
sendo o título do `callout-tip`, dentro da caixa. Havia uma inconsistência
real neste arquivo: 2 das 3 pausas ativas já seguiam esse padrão
`Pergunta`/`Resposta` corretamente, mas a terceira (L1/L2/L∞) e os 3
testes V/F ainda usavam o padrão antigo — todos corrigidos agora para o
mesmo padrão `Pergunta`/`Resposta`. Revalidado com `quarto render --to
html` e `--to revealjs`; confirmado via extração de `<section id=...>`
do `slides.html` renderizado que todo slide `Pergunta`/`Resposta` tem a
caixa correta por baixo, sem heading duplicado ou solto.

Deixados sintéticos, por decisão consciente (são contraexemplos/provas
específicas, não o problema-fio de um bloco): o *Swiss Roll* (Bloco 3,
ilustração geométrica de variedade curva), as bolas unitárias das
normas $L_1/L_2/L_\infty$ (Bloco 4, pura geometria, não há "dado" por
trás), o contraexemplo dos três vetores a $0°/90°/135°$ (Bloco 5, prova
da desigualdade triangular), e as duas luas (Bloco 6, ilustração
geométrica de fronteira não-linear). Adicionadas `datasets` e
`huggingface_hub` como dependências do projeto (`pyproject.toml`).
Verificado que o aviso "unauthenticated requests" e a barra de
progresso do download não vazam para a saída renderizada. Revalidado
com `quarto render --to html` e `--to revealjs`, sem erro.

**Pequenos ajustes de conteúdo em 2026-08-19** (pedidos pontuais do
usuário):

- **Dados categóricos** adicionados à Motivação (Bloco 1) — *one-hot
  encoding* explicado com exemplo (cor de um carro), avisando por que
  codificar categorias com números arbitrários introduz ordem falsa.
- **Continuidade de Lipschitz** citada (não aprofundada) logo após a
  Hipótese de Suavidade (Bloco 2), com a fórmula
  $|f(\mathbf{x})-f(\mathbf{y})|\le L\cdot d(\mathbf{x},\mathbf{y})$ e
  ponte explícita para convergência de otimização, tema futuro do
  curso.
- **Gráfico de limiar de decisão** adicionado depois da Ilustração
  Prática do $k$-NN (Bloco 2) — região de decisão do $k$-NN ($k=3$)
  sobre as $569$ pacientes reais do Breast Cancer Wisconsin, mostrando
  a fronteira irregular exatamente na região onde a paciente de
  consulta está posicionada.
- **Demonstração concreta de $A\mathbf{x}=\mathbf{0}$** (Bloco 3) — a
  prova abstrata de 3 passos ganhou um exemplo numérico
  ($A=[1,1,1]$, $\mathbf{x}=[1,-1,0]^T$, $\mathbf{y}=[0,1,-1]^T$),
  verificado antes via script Python, tirando a prova "do papel".
- **Mapeamento não-linear + fronteira do $k$-NN** (Bloco 3, depois da
  Hipótese da Variedade) — dois círculos concêntricos mapeados para
  coordenadas polares $(r,\theta)$: fronteira curva no espaço original
  vira uma fronteira quase plana em $(r,\theta)$ (verificado
  numericamente: $r$ sozinho separa as classes com acurácia $1{,}0$),
  ilustração direta e concreta do "desamassar o manifold".

Todas as figuras novas usam a paleta preferencial do IC
(`#0085CA`/`#FF5E00`/`#E03C31`). Revalidado com `quarto render --to
html` e `--to revealjs`, sem erro.

**Pergunta separada do usuário, respondida só no chat (não incorporada
à aula):** vantagens práticas de usar distância cordal/angular em vez
de $1-\cos\theta$ em sistemas reais de busca vetorial — ver a
conversa; resumo: para *ranking*/ordenação as três são equivalentes
(transformações monótonas umas das outras), então a maioria dos
sistemas usa a versão mais barata ($1-\cos\theta$ ou o produto interno
puro); a distância cordal importa na prática porque equivale à
distância Euclidiana entre vetores normalizados — permite reusar
índices ANN que só suportam L2 nativamente; métricas de verdade
(cordal/angular) só são estritamente necessárias para estruturas de
indexação métrica clássicas (M-trees, VP-trees) que podam candidatos
via desigualdade triangular.

## Aula 2 — Matrix Representations, Linear Systems, and Independence

Construída do zero em 2026-08-21, já seguindo o novo paradigma de aula
desde o início (não precisou de reavaliação posterior como as Aulas 1
de `supervised`/`unsupervised`/`algebra_opt`).

- [x] `00-plano-aula.md` — 6 blocos, ~115 min. Fio condutor: mesmo
      dataset real da Aula 1 (California Housing, via Hugging Face) —
      continuidade de dataset entre aulas. Conexão explícita com a Aula 1
      no Bloco 3: o resultado "solução de $A\mathbf{x}=\mathbf{0}$ é
      subespaço" é generalizado para $A\mathbf{x}=\mathbf{b}$. Correlação
      real AveRooms/AveBedrms ($0{,}865$) verificada por script antes de
      citá-la no plano, usada no Bloco 5 como exemplo de
      quase-multicolinearidade.
- [x] `01-fontes.md` — 5 fontes do MathML (§2.1 sistemas lineares, §2.2
      matrizes, §2.4 ponte com subespaços da Aula 1, §2.5 independência
      linear, §2.6.2 posto), offset +6 confirmado de novo. A leitura de
      $A\mathbf{x}$ como combinação linear de colunas (usada no Bloco 2)
      é sinalizada explicitamente como exposição nossa, não citação — o
      MathML não enuncia nesses termos.
- [x] `02-aula.qmd` — escrito com o dataset real (California Housing)
      em quase todos os blocos: amostra de 6 bairros como matriz de
      design (Bloco 1), previsões via $X\mathbf{w}$ com pesos
      ilustrativos (Bloco 2), posto da matriz de design completa
      ($16.640\times 4$, posto $4$) mais uma coluna redundante fabricada
      deliberadamente ($2\times$ `AveRooms`, posto continua $4$) para
      ilustrar multicolinearidade exata (Bloco 5), e o scatter real
      `AveRooms`/`AveBedrms` para quase-multicolinearidade. Contraexemplo
      do Bloco 4 (3 vetores em $\mathbb{R}^2$ são sempre dependentes)
      verificado numericamente antes de escrever ($\mathbf{v}_3 =
      0{,}6\mathbf{v}_1+2{,}8\mathbf{v}_2$, confirmado por
      `np.linalg.lstsq`). As três formas de solução de um sistema
      (nenhuma/uma/infinitas) ilustradas geometricamente com equações
      próprias, não copiadas do MathML. 2 pausas ativas + 3 testes V/F,
      padrão `Pergunta`/`Resposta` desde a primeira escrita. Um diagrama
      TikZ (roteiro da aula) — testado renderizando o SVG gerado antes
      de confiar no resultado (aviso do Inkscape sobre parsing de PDF
      UTF16 se mostrou inofensivo; diagrama renderizou corretamente,
      inclusive acentuação). Validado com `quarto render --to html` e
      `--to revealjs`, sem erro; Exercícios com 3 discursivas + 12
      blocos de V/F (48 itens) confirmados por contagem no HTML
      renderizado.

## Etapa 5 — index.md

Link da Aula 1 corrigido: apontava para `../../algebra/aula1/livro.html`
(disciplina, pasta e nome de arquivo antigos/errados) — agora
`../../algebra_opt/aula01/notas.html` (+ Slides), mesmo padrão do
`supervised`. Mostrado no chat antes de aplicar.

## Aula 2 — Matrizes, Sistemas Lineares e Independência

Nota: esta seção não havia sido criada quando a Aula 2 foi originalmente
escrita (o registro de progresso ficou desatualizado) — preenchida agora
retroativamente, junto com o trabalho desta sessão.

**Auditoria e reescrita completa dos itens de V/F (2026-08-26)**, a
pedido do usuário ("Reescreva os vf da aula dois de algebra"), depois de
uma auditoria (agente dedicado) que encontrou: de 48 itens nas notas e
12 nos slides, só ~8 satisfaziam de fato uma das quatro heurísticas
exigidas pelo `CLAUDE.md` (Contrafactual/Caso limite/Transferência de
domínio/Falsa dicotomia) — a grande maioria era paráfrase literal ou
recall de uma frase já dada no texto (padrão "proibido"), incluindo 2
pares de itens duplicados quase palavra-por-palavra entre slides e
notas. `_02-solucoes.md` (obrigatório) nunca havia sido criado.

- **Todos os 48 itens das notas (12 blocos) e os 12 itens dos 3
  *checkpoints* de slides foram reescritos** — mesmos temas/títulos de
  bloco, itens novos, cada um checado individualmente contra sua
  heurística antes de fixar a resposta (evitando repetir o erro de
  assumir a resposta sem verificar a mecânica, ex.: o item sobre "$AB$
  e $BA$ nunca definidos simultaneamente" foi corrigido para citar o
  contraexemplo de matriz quadrada, e o item sobre "reduzir $N$ abaixo
  de $d$ garante solução exata" foi descartado por, na verificação,
  também ser tecnicamente verdadeiro no caso genérico — não servia como
  armadilha).
- **`_02-solucoes.md` criado do zero**, com heurística nomeada e
  justificativa por item, mesmo formato já padronizado nas outras
  disciplinas.
- Duplicações entre slides e notas eliminadas — nenhum item dos 3
  *checkpoints* de slides repete um item das 12 questões de notas,
  mesmo cobrindo temas próximos.
- Revalidado com `quarto render --to html` e `--to revealjs`, sem
  erro; contagem de `id="pergunta*"`/`id="resposta*"` no `slides.html`
  renderizado confirma a mesma estrutura de antes (5 `Pergunta`/3
  `Resposta` — só o conteúdo dos itens mudou, não a estrutura de
  slides).
- **Pendências não resolvidas nesta rodada** (fora do escopo do pedido,
  que foi só sobre os V/F — sinalizadas para o usuário, não corrigidas
  sem confirmação): 2 das 5 pausas ativas ainda não têm um bloco de V/F
  + slide de `Resposta` (só a pergunta discursiva); nenhuma figura ou
  bloco `{.tikz}` está envolvido em `.fig-resize`; dois avisos de
  leitura naturais (interpretação por coluna do MathML sendo exposição
  nossa; resultado de posto citado sem prova) continuam como texto
  simples, não em `callout-note`/`callout-warning`.

## Aula 2 revisada por completo contra a política atual do CLAUDE.md (2026-08-26)

Feedback do usuário: "não está bom" + fonte grande demais nos slides —
pediu para varrer o `../CLAUDE.md` em detalhe e refazer a aula. O
CLAUDE.md evoluiu bastante desde a última passada nesta aula (aula
construída antes de várias convenções mais recentes serem
estabelecidas em `unsupervised-learning`), então vários pontos da
política atual não estavam sendo seguidos aqui. Corrigido:

- **Bug de fonte grande identificado e corrigido:** o YAML do
  `revealjs` desta aula não tinha `smaller: true`/`scrollable: true` —
  presentes em toda aula mais recente (`unsupervised-learning`,
  `supervised-learning`), ausentes aqui e em `aula01` (não mexido,
  fora do pedido desta vez). Confirmado no HTML renderizado:
  `'smaller': true` agora aparece na config JS do Reveal.
- **Exercícios (12 blocos de V/F) reescritos no formato correto:**
  usavam `a. ( )` (parênteses, não clicável mas fora do padrão
  estabelecido) dentro de `callout-tip`; convertidos para `- □`
  (bullets) dentro de `callout-note icon=false`, igual ao padrão de
  toda outra disciplina.
- **Todas as 5 pausas ativas de bloco convertidas para o glifo
  `□`/`✔`/`✗`:** os blocos 2, 4 e 5 já tinham V/F + Resposta, mas no
  formato antigo `a. **Verdadeiro** — texto` (pré-data a descoberta do
  glifo seguro); convertidos para `- ✔`/`- ✗`. Os blocos 1 ("Definindo
  a Matriz de Design") e 3 ("Sistemas Lineares") só tinham uma pergunta
  aberta de reflexão, sem V/F nem slide de Resposta — reescritos do
  zero com 4 itens por heurística (contrafactual, limite, transferência
  de domínio, falsa dicotomia) e slide de Resposta completo.
- **Gap de "o que a variável significa" nos slides (mesmo padrão do
  `radius_mean` em `unsupervised-learning`):** o slide RevealJS "Da
  Tabela de Dados à Matriz" seguia direto para a tabela de 6 bairros
  sem nunca dizer o que `MedInc`/`HouseAge`/`AveRooms`/`AveBedrms`
  significam fisicamente (as notas diziam, o slide não). Also esse
  slide estava vazio (só um título, "Dataset - California Housing
  Dataset", sem nenhum conteúdo antes da figura) — corrigido junto,
  aproveitando a nova regra de "nenhum slide vazio" do CLAUDE.md.
- **Abertura reforçada:** só tinha Roteiro Explícito (4 perguntas) e o
  diagrama TikZ — sem Organizador Prévio, Revisão Rápida da Aula 1, nem
  Problema Motivador distintos, os três elementos que o CLAUDE.md
  também exige na Abertura. Adicionados: uma Revisão Rápida cobrindo
  espaço vetorial/subespaço, normas, produto interno/cosseno e o aviso
  inicial de maldição da dimensionalidade da Aula 1; um Organizador
  Prévio fazendo a ponte "de um vetor para N vetores de uma vez"; e um
  Problema Motivador concreto (prever o preço dos 20.640 bairros de uma
  vez, sem loop) antes de qualquer formalismo.
- **`.fig-resize` ausente em toda figura/diagrama do arquivo** — bug já
  sinalizado como pendência não resolvida numa rodada anterior (ver
  entrada anterior de V/F), agora corrigido: as 7 figuras Python
  (tabela de amostra, gráfico de barras de previsões, 2 versões do
  gráfico de 3 soluções, diagrama de vetores em $\mathbb{R}^2$, 2
  versões do scatter AveRooms/AveBedrms) e o diagrama TikZ da Abertura
  agora saem envolvidos em `.fig-resize`, com o `width=`/`.nostretch`
  inútil removido do bloco `{.tikz}` (não tinha efeito, conforme já
  documentado no CLAUDE.md).
- **`_00-plano-aula.md`:** adicionada a declaração de Estratégia
  Pedagógica que faltava — Estratégia B (Inside-Out com Problema-Fio),
  por ser aula de fundação matemática de representação.

Revalidado com `quarto render --to html` e `--to revealjs`: sem erro,
sem warning de div (`:::` balanceado), sem `<input type="checkbox">`
real, 5 pares `pergunta`/`resposta` confirmados (um por bloco).

**Pendência sinalizada, não resolvida nesta rodada** (fora do escopo
explícito do pedido — mudança mais invasiva, melhor com aprovação
antes): o Bloco 1 ainda apresenta a definição formal de matriz (Def.
2.1, MathML) antes do exemplo concreto dos 6 bairros — na ordem
inversa da fase "Intuição" (concreto antes do formalismo) que
`unsupervised-learning/aula02` já adota. Inverter essa ordem exigiria
reestruturar o bloco inteiro; sinalizado para decisão do usuário antes
de mexer.

## Slide "Combinações Lineares e Independência" separado em definição + exemplo (2026-08-26)

Feedback do usuário: o slide misturava a definição formal com a
explicação intuitiva ("sem redundância") — pediu para deixar a
definição mais formal nesse slide e mover qualquer exemplo/explicação
intuitiva para o slide seguinte.

- **"Combinações Lineares e Independência"** ficou só com as duas
  definições formais, com notação de somatório explícita
  ($\sum_{i=1}^k\lambda_i\mathbf{x}_i$) e separação clara de LD/LI
  (tradução nossa, MathML, Def. 2.11–2.12) — nada de intuição ou
  exemplo.
- **Novo slide "O Que Essa Definição Quer Dizer, na Prática"** reúne a
  explicação intuitiva ("sem redundância", MathML §2.5) e a introdução
  do contraexemplo (3 vetores em $\mathbb{R}^2$ nunca são LI) — a ponte
  entre a definição formal e o código que verifica o contraexemplo,
  que continua logo em seguida sem mudança.

Revalidado com `quarto render --to html` e `--to revealjs`: sem erro,
sem warning de div, sem `<input type="checkbox">` real, 5 pares
`pergunta`/`resposta` confirmados intactos.

## Duas explicações aprofundadas, a pedido do usuário (2026-08-26)

**1. "Da Independência à Multicolinearidade" ganhou um gráfico.**
Faltava um exemplo visual concreto. Adicionado: um gráfico de dispersão
de `AveRooms` (original) contra $2\times$`AveRooms` (a mesma cópia
fabricada que o Bloco 5 usa para derrubar o posto) — todos os pontos
caem exatamente numa reta, tornando visível que a segunda coluna não
carrega nenhuma informação que a primeira não tivesse. O texto também
passou a conectar explicitamente com a Leitura 2 do Bloco 2 (coluna
redundante = combinação linear das outras = nenhuma direção nova em
$X\mathbf{w}$), em vez de introduzir a ideia solta.

**2. "O Posto de uma Matriz" ganhou a explicação de $\text{rk}(A|\mathbf{b})$
e por que o critério de solvabilidade funciona.** Antes, a aula citava
a fórmula do MathML sem explicar o mecanismo. Adicionado um
desenvolvimento *principled* completo: $[A|\mathbf{b}]$ definida como
matriz aumentada; Premissas (Leitura 2 do Bloco 2: resolver
$A\mathbf{x}=\mathbf{b}$ é perguntar se $\mathbf{b}$ é combinação
linear das colunas de $A$; posto mede quantas direções essas colunas
geram); Passo 1 ($\mathbf{b}$ dentro do espaço-coluna → posto não
muda) e Passo 2 ($\mathbf{b}$ fora → posto sobe 1); conclusão amarrando
tudo. Conferido numericamente reaproveitando o próprio exemplo
"nenhuma solução" do Bloco 3 (retas paralelas): $\text{rk}(A)=1$,
$\text{rk}([A|\mathbf{b}])=2$, confirmado por código
(`np.linalg.matrix_rank`).

Revalidado com `quarto render --to html` e `--to revealjs`: sem erro,
sem warning de div, sem `<input type="checkbox">` real, 5 pares
`pergunta`/`resposta` confirmados intactos.

## Quatro adições de conteúdo para preencher os 100 min reais de aula (2026-08-26)

Feedback do usuário: o conteúdo atual da aula, na prática, se dava em
~50 min — bem abaixo dos 100 min reais da turma. Diagnóstico corrigido
em relação a uma sugestão anterior minha (eu tinha lido a situação ao
contrário, como se faltasse tempo): o problema não era falta de foco,
era falta de profundidade real nos mesmos blocos. Quatro adições,
todas no fio condutor já existente, não conteúdo novo desconectado:

1. **Exemplo resolvido de eliminação de Gauss (Bloco 3).** A aula
   mostrava geometricamente que um sistema pode ter 0/1/∞ soluções, mas
   nunca como descobrir isso na prática. Adicionado um sistema 3×3
   resolvido passo a passo (matriz aumentada → eliminação → forma
   triangular → substituição reversa), verificado com
   `np.linalg.solve` (solução $(1,2,3)$ confirmada), mais uma explicação
   de como reconhecer os casos "sem solução" (linha "$0=$ não-zero") e
   "infinitas soluções" (linha "$0=0$") no mesmo algoritmo — preparando
   o atalho do posto que vem no Bloco 5.

2. **Espaço-coluna visualizado geometricamente, antes da definição
   formal de posto (Bloco 5).** Pedido explícito do usuário: a versão
   anterior desta explicação (do turno passado, sobre
   $\text{rk}(A|\mathbf{b})$) estava fragmentada em slides pequenos
   demais e pouco intuitiva. Reescrita do zero: primeiro um gráfico
   mostrando o espaço-coluna do exemplo do Bloco 3 como uma reta em
   $\mathbb{R}^2$, com $\mathbf{b}=(3,5)$ fora dela (sem solução) e
   $\mathbf{b}'=(4,4)$ sobre ela (com solução) — só depois a definição
   formal do MathML e o critério $\text{rk}(A)=\text{rk}(A|\mathbf{b})$,
   como *formalização* do que o desenho já respondeu, seguindo o
   princípio duplo-registro (intuição → formalismo). Consolidado em
   menos slides, cada um mais completo, em vez de muitos fragmentos
   rasos.

3. **Walkthrough completo com $\mathbf{w}$ conhecido (Bloco 2).**
   Expandido o demo antigo (só um gráfico de barras de previsões) para
   comparar previsão vs. valor real (`MedHouseVal`) dos 6 bairros da
   amostra, introduzindo o **resíduo** $\hat{\mathbf{y}}-\mathbf{y}$
   como antecipação direta da pergunta central da Aula 3.

4. **Demonstração numérica de instabilidade por quase-multicolinearidade
   (Bloco 5).** Em vez de só afirmar "fica instável, assunto da Aula
   4", mostrado com números: ajuste por mínimos quadrados numa amostra
   de 20 bairros com `AveRooms`/`AveBedrms` (correlação 0,865),
   perturbação de apenas 1% em `MedHouseVal` faz o peso de `AveBedrms`
   variar ~30% — contra <1% de variação no par bem condicionado
   `MedInc`/`HouseAge` sob o mesmo ruído. Números verificados
   experimentalmente antes de escrever (`np.linalg.lstsq`,
   `random_state=7` para a amostra, seed 1 para o ruído — reprodutível).

`_00-plano-aula.md` atualizado: cabeçalho trocado de "carga horária
estimada: ~115min" para "carga horária real da turma: 100min", com as
quatro adições anotadas dentro dos blocos 2, 3 e 5.

Revalidado com `quarto render --to html` e `--to revealjs`: sem erro,
sem warning de div, sem `<input type="checkbox">` real, 5 pares
`pergunta`/`resposta` confirmados intactos.

## Aula 3 — Etapa 1–2 (2026-08-30)

Tema confirmado com o usuário: "Orthogonal Projections and Subspaces"
(Lesson 3 do `../index.qmd`, já linkada lá desde antes desta sessão,
mas nunca construída — `_progresso.md` confirmava "Aulas 3–15: não
iniciadas"). `aula03/_00-plano-aula.md` criado — Estratégia B
(Inside-Out com Problema-Fio), carga horária ~100min (mesmo alvo real
recalibrado na Aula 2), 7 blocos (Abertura retomando o sistema
sobredeterminado sem solução da Aula 2 → Intuição geométrica da
"sombra"/projeção em $\mathbb{R}^2$/$\mathbb{R}^3$ → subespaços e
complemento ortogonal → Teorema da Projeção com Premissas + passo a
passo até as Equações Normais → aplicação e verificação no dado real
→ quando a fórmula falha/fica frágil, reconectando com posto e a
instabilidade numérica já demonstradas na Aula 2 → fechamento/ponte
para autovalores na Aula 4). Dataset-fio: California Housing, mesmo
subconjunto de atributos das Aulas 1–2. **PARADO, aguardando aprovação
do plano.**

## Aula 3 — Etapa 3–4: fontes e aula completa (2026-08-30)

Usuário autorizou seguir direto até a aula completa sem parar em cada
checkpoint intermediário ("Vamos continuar as duas aulas 3. Não precisa
da minha permissão para criar a aula ao final.").

- [x] `_01-fontes.md` — 7 fontes do `mathml.pdf`, §3.6 (Complemento
      Ortogonal, p. 79–80) e §3.8 (Projeções Ortogonais, Definição 3.10 e
      §3.8.1–3.8.2, p. 82–88), offset **+6** reconfirmado (cabeçalho
      "79 ... Analytic Geometry" na página 85 do PDF). Extraído via
      `pdftotext -layout` das páginas certas, localizadas primeiro com
      `grep` no texto completo do PDF (não adivinhado por número de
      página). Inclui o trecho do próprio MathML que amarra
      explicitamente "sistema sem solução" (Aula 2) com "projeção como
      melhor aproximação" (Fonte 7, p. 88) — citado na Abertura e no
      Fechamento da aula.
- [x] `index.qmd` — construído a partir do template de `aula02/index.qmd`
      (YAML, `.fig-resize`, intercalação `content-visible`), 7 blocos do
      plano, **6 pausas ativas** (uma por bloco, exceto o Fechamento) e
      Exercícios com 3 discursivas + 12 blocos de V/F (48 itens,
      confirmados por contagem programática, não por inspeção visual).
      Diagramas: 3 TikZ (roteiro da Abertura com ramificação
      invertível/não-invertível; esquema geométrico do Teorema da
      Projeção no Bloco 4; ramificação multicolinearidade
      exata-vs-quase-exata no Bloco 6) e 3 figuras matplotlib de
      geometria conceitual (sombra 2D/3D no Bloco 2; decomposição
      $V=U\oplus U^\perp$ no Bloco 3) — todas envolvidas em
      `.fig-resize`.
- **Números reais calculados antes de escrever** (Python do kernel
  `sensibleml-moo`, `.venv` em
  `~/Documents/Research/sensible-deep-moo/code/.venv`), nunca
  fabricados:
  - $\hat{\mathbf{w}}$ via Equações Normais no California Housing
    completo ($N=16\,640$, 4 atributos):
    $[0{,}48761,\ 0{,}01171,\ -0{,}18809,\ 0{,}78255]$ (`MedInc`,
    `HouseAge`, `AveRooms`, `AveBedrms`) — diferença máxima contra
    `np.linalg.lstsq`: $\approx 1{,}29\times10^{-14}$.
  - Ortogonalidade do resíduo: produto interno com cada coluna entre
    $-5{,}0\times10^{-9}$ e $-2{,}0\times10^{-10}$ (proporção relativa
    $\approx 10^{-14}$ — numericamente zero).
  - $\|\text{resíduo}\|\approx 101{,}49$, $\|\mathbf{y}\|\approx
    298{,}57$, $R^2\approx 0{,}518$.
  - Coluna duplicada ($2\times$`AveRooms`, reaproveitada da Aula 2):
    posto continua $4$; $\det(X^TX_{\text{dup}})=0$;
    `np.linalg.inv` levanta `LinAlgError: Singular matrix`.
  - Número de condição: $\text{cond}(X^TX)\approx 23\,460$ (4 atributos
    completos); $\text{cond}(X^TX)\approx 419{,}8$ (par
    `AveRooms`/`AveBedrms`, amostra de 20) vs. $\approx 169{,}1$ (par
    `MedInc`/`HouseAge`, mesma amostra) — reproduzindo exatamente os
    números já demonstrados na Aula 2 (variação de $\approx 29{,}5\%$ no
    peso de `AveBedrms` sob perturbação de 1%, contra $\approx 0{,}1\%$
    no par bem-condicionado; `random_state=7`, ruído seed `1`).
  - Correlação `AveRooms`/`AveBedrms` no dataset completo:
    $0{,}8652$ (Aula 2 já citava $0{,}865$ — consistente).
- **Um bug encontrado e corrigido durante a validação:** um chunk do
  Bloco 5 (verificação de ortogonalidade) tinha um laço de depuração
  esquecido (`residuo @ np.eye(4)`, incompatível de dimensão —
  $4\ne 16\,640$) que quebrava o render em HTML. Removido antes de
  revalidar.
- **12º bloco de V/F acrescentado durante a auditoria de contagem:** a
  primeira escrita saiu com 11 blocos (44 itens) por causa de um erro
  de contagem manual; acrescentado um 12º bloco ("A matriz de projeção
  $P_\pi$", explorando $P_\pi=X(X^TX)^{-1}X^T$ e $P_\pi^2=P_\pi$, tema
  coberto na aula mas sem bloco próprio) para fechar em 48 itens exatos.
- `_02-solucoes.md` e `_03-respostas-pausas.md` criados do zero, nos
  formatos exigidos pelo `CLAUDE.md` — heurística nomeada + afirmação +
  resposta + justificativa por item (48 itens); discussão em prosa +
  lista `✔`/`✗` por pausa (6 pausas). Um item (Bloco "Posto e
  multicolinearidade exata", item c — Celsius/Fahrenheit) foi projetado
  como armadilha deliberada: a transformação é **afim** ($F=\frac95
  C+32$), não puramente linear/múltiplo escalar, então as duas colunas
  **não** ficam automaticamente dependentes sem uma coluna de intercepto
  já presente — resposta Falso, com a distinção justificada em
  `_02-solucoes.md`.

**Validação (6 itens obrigatórios, todos passados):**

1. `quarto render index.qmd --to html` e `--to revealjs` — ambos sem
   erro após a correção do bug do Bloco 5 (o "NotFound" transitório de
   `notas.html`/`slides.html` apareceu uma vez entre renders
   consecutivos de formatos diferentes, some ao rerenderizar o outro
   formato — mesmo comportamento benigno já descrito na tarefa).
2. Balanceamento de `:::` verificado por script (pilha LIFO): 182
   aberturas, 182 fechamentos, pilha vazia ao final do arquivo, zero
   erros.
3. `grep -n '☐\|☒\|- \[ \]\|- \[x\]'` em `index.qmd`,
   `_02-solucoes.md` e `_03-respostas-pausas.md`: limpo nos três.
4. Exercícios: exatamente 3 discursivas e 12 blocos `callout-note` de 4
   itens (48 itens) confirmados por contagem programática (`grep -c`).
5. YAML confirmado: `output-file: notas.html` (html) e
   `output-file: slides.html` (revealjs).
6. Conteúdo-chave grepado nos HTMLs renderizados: "Equações Normais"
   (23× em `notas.html`, 11× em `slides.html`) e "resíduo" (36× e 23×);
   valores numéricos reais (`0.518`, `23\,460`, os produtos internos do
   resíduo) confirmados presentes no `notas.html` renderizado, não só
   no código-fonte.

`index.qmd` final: 2140 linhas, 11891 palavras.

**Sem desvios não sinalizados do plano** — a única adição em relação ao
`_00-plano-aula.md` original foi o 12º bloco de exercícios (acima do
mínimo, não uma mudança de estrutura) e a correção do bug de depuração;
os 7 blocos, a estratégia pedagógica (B) e o dataset-fio saíram como
planejado. **Etapa 5 (link no `index.qmd` da disciplina) não foi feita
nesta sessão** — fica para o usuário confirmar o trecho antes da
edição, por instrução do `CLAUDE.md`.

**Etapa 5 concluída (2026-08-30):** o link da Aula 3 no `../index.qmd`
já existia desde antes desta sessão (`[**Lesson 3: Orthogonal
Projections and Subspaces**](./aula03/index.qmd)`) — era um artefato de
esqueleto pré-existente, apontando para uma pasta que não existia ainda
quando checado no início desta sessão. Agora que `aula03/` existe e
está validada, o link já está correto sem precisar de edição adicional.
Aula 3 encerrada.

**Verificação independente (2026-08-30, sessão supervisora):** reconferi
os 6 itens acima e encontrei uma lacuna real que o agente não pegou —
os 3 chunks Python que geram figura (linhas ~356, ~584, ~1328 antes da
correção) não estavam envolvidos em `.fig-resize`, só os 3 blocos
`{.tikz}` estavam (contagem `fig-resize`=3 vs. `plt.show()`+`{.tikz}`=6,
deveria ser 1:1). Corrigido — agora 6 divs `.fig-resize` para 6
figuras/diagramas. Reconferido balanceamento LIFO (limpo) e re-renderizado
`--to html` e `--to revealjs` do zero: ambos sem erro. Todo o resto do
relatório do agente (números reais computados, contagem de exercícios,
glifos, YAML) confere.

## Aula 4 — Autovalores, Autovetores e Matrizes Simétricas (2026-09-07)

Construída em uma única sessão a partir de um `_00-planejamento.md` já
completo, escrito por uma sessão anterior que atingiu o limite de taxa
da conta antes de gerar qualquer outro arquivo — esta sessão executou o
plano já pronto (7 blocos, ~100min, Estratégia B/Inside-Out com
Problema-Fio), sem redesenhá-lo. Gancho de abertura: a promessa
explícita deixada pelo Fechamento da Aula 3 ("o número de condição foi
usado aqui de forma empírica [...] a Aula 4 dá a ferramenta exata para
medi-lo diretamente a partir da estrutura de $X^TX$ [...] sem precisar
perturbar nada").

- [x] `_00-planejamento.md` — já existente ao início da sessão; 12
      fontes citadas (10 do `mathml.pdf`, 2 do `copt.pdf`), todas com
      página impressa e trecho literal em inglês já extraídos.
- [x] **Verificação de citações contra os PDFs originais (offset de
      página):** confirmado offset **+6** para `mathml.pdf` (consistente
      com Aulas 1–3) reconferindo 9 trechos distintos (Def. 3.4 p.74→80,
      Def. 4.5 p.104→110, Def./obs. 4.6 p.105→111, Teorema 4.8 p.106→112,
      Exemplo 4.5 p.107→113, Fig. 4.4 p.108→114, Teoremas 4.14/4.15
      p.111→117, Teorema 4.20 p.116→122, Teorema 4.21/Exemplo 4.11
      p.117-118→123-124) — todos batendo exatamente, texto e página.
      Para `copt.pdf` (**primeira vez usado nesta disciplina**),
      descoberto e confirmado offset **+14** (não +6): "lengths of the
      semi-axes" (p.30→44), "Suppose A ∈ Sⁿ" (p.646→660), "largest and
      smallest eigenvalues" (p.647→661), "condition number" (p.649→663)
      — os quatro batendo com o mesmo offset, texto conferido
      literalmente contra o PDF via `pdftotext`. **Novo item no
      dicionário de offsets da disciplina: `copt.pdf` usa +14, diferente
      do +6 do `mathml.pdf`.**
- [x] `index.qmd` — dual HTML/RevealJS, 7 blocos: (1) Revisão/Introdução
      retomando a Aula 3 + Pausa Ativa 1; (2) Intuição visual
      (autovetores como direções que não giram, matriz
      $A=\begin{bmatrix}4&2\\1&3\end{bmatrix}$ do MathML Exemplo 4.5,
      figura de grade de vetores + círculo→elipse) + Pausa Ativa 2; (3)
      polinômio característico, exemplo resolvido à mão (raízes
      $\lambda=2,5$, autovetores $(2,1)$/$(1,-1)$), verificação via
      `numpy.linalg.eig` + Pausa Ativa 3; (4) Teorema Espectral Real —
      prova própria de ortogonalidade entre autovetores de autovalores
      distintos (sinalizada explicitamente como "prova nossa, não da
      fonte"), contraste com $A_{\text{sim}}=\frac12\begin{bmatrix}5&-2\\
      -2&5\end{bmatrix}$ (MathML Exemplo 4.11, autovalores $7/2,3/2$,
      autovetores ortonormais), decomposição espectral geral
      $A=PDP^{-1}$ especializada ao caso simétrico + Pausa Ativa 4; (5)
      definitude positiva via $x^TAx$ (MathML Def./Exemplo 3.4, $A_1$
      PD/$A_2$ indefinida, com figura de contorno tigela-vs-sela),
      caracterização por autovalores (Boyd A.5.2), quociente de Rayleigh,
      número de condição exato fechando o ciclo da Aula 3, ponte breve
      para Hessiana/convexidade (Aula 7) + Pausa Ativa 5; (6) aplicação
      no dado real (ver números abaixo), sem pausa ativa própria (fiel
      ao plano); (7) Fechamento retomando as 4 perguntas + ponte para SVD
      (Aula 5). 5 Pausas Ativas (uma por bloco, Blocos 1–5; Blocos 6–7
      sem pausa, conforme o plano original). 6 elementos visuais, todos
      em `.fig-resize` (2 TikZ: roteiro de abertura, ponte final
      simétrica-vs-retangular para SVD; 4 figuras matplotlib: grade de
      vetores/círculo→elipse do Bloco 2, contraste de ângulo entre
      autovetores simétrica-vs-não-simétrica do Bloco 4, contorno
      tigela-vs-sela do Bloco 5, scatter real `AveRooms`/`AveBedrms` com
      autovetores da covariância do Bloco 6).
- **Números do Bloco 6 — computados via script Python antes de
  escrever, reproduzindo exatamente os valores que o plano já
  antecipava** (mesmo kernel `homepage`, `uv run python`,
  `gvlassis/california_housing`):
  - Autovalores de $X^TX$ (4 atributos completos):
    $[747{,}25;\ 52\,666{,}03;\ 273\,990{,}28;\ 1{,}753\times10^{7}]$;
    $\text{cond}(X^TX)=23\,460{,}5$ — bate com a Aula 3 até a primeira
    casa decimal (era $\approx 23\,460$ via `np.linalg.cond`).
  - Par quase-colinear (`AveRooms`/`AveBedrms`, amostra de 20,
    `random_state=7`): autovalores $[1{,}767;\ 741{,}961]$,
    $\text{cond}=419{,}8$ — idêntico ao $\approx 420$ da Aula 3.
  - Par bem-condicionado (`MedInc`/`HouseAge`, mesma amostra):
    autovalores $[139{,}617;\ 23\,613{,}014]$, $\text{cond}=169{,}1$ —
    idêntico ao $\approx 169$ da Aula 3. **Nenhuma discrepância a
    registrar** — os três números batem, número por número, com o que o
    `_00-planejamento.md` já antecipava (a Aula 3 os havia calculado por
    perturbação/`np.linalg.cond`; ambos os métodos convergem porque, para
    matriz simétrica PSD, `np.linalg.cond` já usa os mesmos autovalores
    por baixo dos panos).
  - Ortogonalidade dos autovetores confirmada (produto interno $=0$,
    até erro de arredondamento) nos três casos e também na covariância.
  - Covariância empírica `AveRooms`/`AveBedrms` (dados completos):
    autovalores $[0{,}0640;\ 7{,}2132]$, autovetor principal
    $\approx(0{,}986;\,0{,}166)$ — quase alinhado ao eixo `AveRooms`
    (variância $\approx7{,}02$ vs. $\approx0{,}26$ de `AveBedrms`,
    quase $27\times$ maior), levemente inclinado pela covariância
    cruzada positiva ($\approx1{,}17$).
  - Covariância dos 4 atributos brutos: variância de `HouseAge`
    ($\approx163{,}8$) mais de $20\times$ maior que qualquer outro
    atributo — maior autovalor da covariância completa
    ($\approx164{,}0$) dominado por essa escala bruta, não pela
    estrutura de correlação — usado como o aviso honesto de
    sensibilidade a escala antes de semear PCA (Aprendizado Não
    Supervisionado), sem desenvolver.
- [x] `_01-respostas.md` — criado do zero, já no formato consolidado
      atual do `CLAUDE.md` (um único arquivo, não mais os três arquivos
      separados `_02-solucoes.md`/`_03-respostas-pausas.md` usados nas
      Aulas 2–3): discussão em prosa + V/F resolvido das 5 Pausas
      Ativas, e heurística nomeada + afirmação + resposta + justificativa
      para os 32 itens de V/F dos Exercícios (8 blocos × 4 itens: "regra
      básica de autovalor/autovetor", "polinômio característico",
      "não-unicidade e autoespaços", "Teorema Espectral Real",
      "definitude positiva", "quociente de Rayleigh/número de condição",
      "$X^TX$: simetria", "covariância empírica/semente de PCA"); mais 3
      questões discursivas, sem solução (trabalho do aluno). **Checagem
      de texto exato entre `index.qmd` e `_01-respostas.md` confirmada
      programaticamente** (32/32 itens idênticos após a correção de dois
      artefatos triviais de quebra de linha) — mesma checagem que já
      pegou bugs reais em aulas anteriores desta disciplina.
- **Um bug de execução encontrado e corrigido durante o render:**
  `numpy.linalg.eig` devolve autovalores/autovetores em `dtype=complex128`
  por padrão para matrizes não-simétricas (mesmo quando os autovalores
  são todos reais, como no exemplo $A=\begin{bmatrix}4&2\\1&3
  \end{bmatrix}$) — isso quebrava tanto uma comparação de ângulo
  (`np.degrees` não aceita complexo) quanto a formatação `:.1f` num
  f-string mais adiante. Corrigido tomando `.real` explicitamente nos
  dois chunks que chamam `np.linalg.eig(A_exemplo)`, com comentário no
  código explicando o motivo — **novo item de atenção para futuras aulas
  desta disciplina**, ao lado dos já registrados (`\le`/`\mathbb`
  proibidos em mathtext do matplotlib; `{,}` literal quebra f-string).

**Validação (itens obrigatórios, todos passados):**

1. Balanceamento de `:::` verificado por script (pilha LIFO): 0 abas
   abertas remanescentes ao final do arquivo, checado antes e depois da
   correção do bug de `dtype`.
2. `quarto render --to html` e `--to revealjs`: ambos sem erro após a
   correção do bug de `dtype` complexo.
3. Glifos: `notas.html` tem 52 `□` (20 das 5 Pausas Ativas + 32 dos 8
   blocos de Exercícios) e zero `✔`/`✗`; `slides.html` tem 20 `□`
   (Pergunta) + 12 `✔` + 8 `✗` (Resposta) das mesmas 5 Pausas Ativas —
   nenhum glifo cruzado entre as duas saídas. Único hit de
   `type="checkbox"` em ambos os arquivos é a regra genérica de CSS do
   tema (`ul.task-list li input[type="checkbox"]`), nunca um checkbox
   real renderizado.
4. Exercícios confirmados por contagem programática: 3 discursivas + 8
   blocos de V/F (32 itens) — densidade calibrada abaixo do teto de 10
   blocos porque a aula tem 5 blocos de conteúdo novo (vs. os 6 da Aula
   3), consistente com a diretriz de não esticar por cota.
5. YAML confirmado: `output-file: notas.html` (html) e
   `output-file: slides.html` (revealjs), mesmo bloco `format:`
   compartilhado das Aulas 1–3.
6. Números reais (`23,460`, `419.8`, `169.1`, autovalores completos)
   confirmados presentes no `notas.html` renderizado, não só no
   código-fonte.

**Etapa 5 concluída nesta sessão:** link da Aula 4 adicionado ao
`../index.qmd` (bullet convertido para link, mesmo formato das Lições
1–3); dicionário de notações abaixo atualizado.

### Dicionário de notações — símbolos novos desta aula

| Símbolo/termo | Significado | Introduzido em |
|---|---|---|
| $\lambda$ | autovalor | Aula 4, Bloco 2 |
| autovetor $\mathbf{x}$ (na equação $A\mathbf{x}=\lambda\mathbf{x}$) | direção que $A$ só estica/encolhe, nunca gira | Aula 4, Bloco 2 |
| $p_A(\lambda)=\det(A-\lambda I)$ | polinômio característico de $A$ | Aula 4, Bloco 3 |
| $E_\lambda$ | autoespaço associado ao autovalor $\lambda$ | Aula 4, Bloco 3 |
| multiplicidade algébrica/geométrica | grau da raiz no polinômio característico / dimensão do autoespaço | Aula 4, Bloco 4 (menção breve) |
| $A=PDP^{-1}$ | decomposição em autovalores (matriz diagonalizável geral) | Aula 4, Bloco 4 |
| $A=Q\Lambda Q^T$ | decomposição espectral (matriz simétrica, $Q$ ortogonal) | Aula 4, Bloco 4 |
| $A\succ 0$ / $A\succeq 0$ | matriz (simétrica) positiva definida / semidefinida | Aula 4, Bloco 5 |
| quociente de Rayleigh $\mathbf{x}^TA\mathbf{x}/\mathbf{x}^T\mathbf{x}$ | média ponderada dos autovalores, limitada por $\lambda_{\min}$/$\lambda_{\max}$ | Aula 4, Bloco 5 |
| $\text{cond}(A)=\lambda_{\max}(A)/\lambda_{\min}(A)$ | número de condição exato (matrizes simétricas PSD) | Aula 4, Bloco 5 |

**Pendência explícita para a Aula 5:** autovalores/autovetores só
existem garantidamente (na forma real do Teorema Espectral) para
matrizes quadradas simétricas — $X$ retangular precisa da Decomposição
em Valores Singulares (SVD), já anunciada no Fechamento desta aula via
a própria definição de número de condição do Boyd (escrita em termos de
valores singulares $\sigma$, não autovalores).

## Aula 5 — Decomposição em Valores Singulares (SVD) e Aproximações de Baixo Posto (2026-09-12)

Construída numa única sessão, ciclo completo (planejamento → aula →
gabarito → link da disciplina → `_progresso.md`) sem parar nos
checkpoints intermediários — autorização explícita do usuário para
seguir direto até o fim das Aulas 5 e 6. Gancho de abertura: a pendência
que a própria Aula 4 deixou registrada neste arquivo ("autovalores e
autovetores reais [...] só existem incondicionalmente para matrizes
quadradas simétricas [...] a resposta é a Decomposição em Valores
Singulares, tema da Aula 5") e o TikZ de fechamento da Aula 4
("$X$ não é quadrada $\to$ Teorema Espectral não se aplica direto
$\to$ SVD (Aula 5)").

- [x] `_00-planejamento.md` — Estratégia B (Inside-Out com
      Problema-Fio), 7 blocos, ~100min. 7 fontes citadas, todas do
      `mathml.pdf` (Cap. 4.5-4.6, SVD e Aproximação de Matrizes),
      offset **+6** reconfirmado (Teorema 4.22 p.119→125; construção
      §4.5.2 p.122-125→128-131; Exemplo 4.13 p.125-126→131-132; Def.
      4.23/Teo. 4.24 p.131→137; Teo. 4.25 Eckart-Young p.131-132→137-138;
      Exemplos 4.14-4.15, notas de filmes, p.127-128 e 132→133-134 e
      138). A Decomposição Polar (Bloco 6) não tem lastro em nenhuma das
      3 fontes da disciplina (buscado explicitamente em `mathml.pdf`,
      `copt.pdf` e `optml.pdf` — zero ocorrências) — sinalizada como
      construção própria, derivada diretamente do Teorema 4.22 já
      demonstrado.
- [x] `index.qmd` — dual HTML/RevealJS, 7 blocos: (1) Revisão/Introdução
      retomando a Aula 4 + explicação formal de por que autovalor é
      **indefinido** (não só "não garantido") para matriz retangular +
      Problema Motivador (matriz de notas de filmes, MathML Exemplo
      4.14, traduzida) + Pausa Ativa 1; (2) Intuição geométrica — matriz
      $2\times2$ não-simétrica de propósito, contrastando vetores
      singulares (sempre ortogonais) com autovetores (não-ortogonais em
      geral, $\approx106{,}9°$ no exemplo) + Pausa Ativa 2; (3)
      Construção formal da SVD a partir do Teorema Espectral — prova
      própria passo a passo (Premissas → vetores singulares à direita
      via autovetores de $A^TA$ → vetores singulares à esquerda como
      imagem normalizada, com prova de ortogonalidade → equação de valor
      singular → montagem $A=U\Sigma V^T$), Teorema 4.22 formal, exemplo
      resolvido à mão (MathML Exemplo 4.13, $2\times3$) verificado com
      `numpy.linalg.svd` + Pausa Ativa 3; (4) SVD do dataset-fio $X$
      (California Housing) — $\sigma_i^2=\lambda_i(X^TX)$ verificado
      numericamente idêntico aos autovalores da Aula 4; Proposição
      própria $\text{cond}(X^TX)=\text{cond}(X)^2$, provada e verificada
      ($153{,}168^2\approx23\,460{,}5$, batendo exato com a Aula 4) +
      Pausa Ativa 4; (5) Aproximação de baixo posto — matrizes de posto
      1 $A_i=\mathbf{u}_i\mathbf{v}_i^T$, SVD truncada, norma espectral
      (Def. 4.23, Teo. 4.24 com prova própria via quociente de Rayleigh
      da Aula 4), Teorema de Eckart-Young-Mirsky (Teo. 4.25) com prova
      completa (tradução/reorganização da prova do MathML, citando o
      Teorema do Núcleo e da Imagem), aplicado a $X$ ($k=1,2,3$,
      erro espectral batendo com $\sigma_{k+1}$ até a 6ª casa decimal) e
      retomando o Problema Motivador (filtragem colaborativa: notas de
      filmes, rank-1 vs. rank-2, heatmaps) + Pausa Ativa 5; (6)
      Decomposição Polar — construção própria $A=QS$ a partir dos
      fatores da SVD, prova de que $Q$ é ortogonal e $S$ é simétrica
      PSD, aplicada de volta à matriz $2\times2$ do Bloco 2 (estica via
      $S$, gira via $Q$), ponte para a Aula 14 (Newton-Schulz,
      Shampoo/Muon); (7) Fechamento retomando as 4 perguntas + ponte
      para a Aula 6 (gradiente/Jacobiano). 5 Pausas Ativas (Blocos 1-5;
      Blocos 6-7 sem pausa, mesmo padrão da Aula 4). 8 elementos visuais
      em `.fig-resize` (2 TikZ: roteiro de abertura, ponte final para a
      Aula 6; 4 figuras matplotlib com imagem: intuição geométrica
      $2\times2$, valores singulares de $X$ + validação $\sigma^2=
      \lambda$, heatmaps de notas de filmes original/posto-1/posto-2,
      decomposição polar circulo→elipse→elipse-girada; 2 chunks
      adicionais de só texto/tabela, também envolvidos em
      `.fig-resize` por consistência de estilo).
- **Números verificados via script Python (`uv run python3`, kernel
  `homepage`) antes de escrever, nunca fabricados:**
  - SVD completa de $X$ (California Housing, $N=16\,640$, 4 atributos):
    $\sigma=[4\,186{,}996;\ 523{,}441;\ 229{,}491;\ 27{,}336]$;
    $\sigma^2$ idêntico, número por número, aos autovalores de $X^TX$
    já calculados na Aula 4.
    $\text{cond}(X)\approx153{,}168$; $\text{cond}(X)^2\approx23\,460{,}5$
    — bate exato com $\text{cond}(X^TX)$ da Aula 4.
  - Eckart-Young-Mirsky verificado exatamente em $X$: para $k=1,2,3$,
    $\|X-\hat X^{(k)}\|_2=\sigma_{k+1}$ até a 6ª casa decimal; erro
    relativo de Frobenius caindo de $\approx13{,}5\%$ ($k=1$) a
    $\approx0{,}6\%$ ($k=3$).
  - Matriz de notas de filmes (MathML Exemplo 4.14): $\sigma=
    [9{,}6438;\ 6{,}3639;\ 0{,}7056]$; rank-1/rank-2 recalculados e
    conferidos contra os valores do próprio livro (rank-2:
    $[[4{,}78,4{,}24,1{,}02],[5{,}23,4{,}75,-0{,}03],[0{,}25,-0{,}27,
    4{,}97],[0{,}75,0{,}28,4{,}03]]$ — bate com o MathML, pequenas
    diferenças de arredondamento de quarta casa decimal). Erro espectral
    de posto-1/posto-2 batendo exato com $\sigma_2,\sigma_3$.
  - Adição de um $4^o$ espectador com nota $(5,5,5,5)$ (usado no
    Exercícios): posto sobe de $3$ para $4$; resíduo fora do
    espaço-coluna $\approx0{,}577$ (não-nulo); $4^o$ valor singular novo
    $\approx0{,}362$ — verificado antes de escrever o item.
  - Decomposição Polar da matriz $2\times2$ do Bloco 2/6: $\det(Q)=1$
    (rotação pura, $\approx7{,}43°$); autovalores de $S=[0{,}645;\,
    1{,}675]$ = valores singulares de $A$; $QS=A$ até erro de ponto
    flutuante.
  - Gradiente de teste (usado só para preparar a ponte com a Aula 6,
    não publicado nesta aula): $\nabla_\beta\|X\beta-\mathbf{y}\|^2=
    2X^T(X\beta-\mathbf{y})$ conferido contra diferença finita central
    (`eps=1e-5`), diferença relativa $\approx10^{-12}$.
- [x] `_01-respostas.md` — discussão em prosa + V/F resolvido das 5
      Pausas Ativas; heurística nomeada + afirmação + resposta +
      justificativa para os 36 itens de V/F dos Exercícios (9 blocos:
      existência/formato da SVD; construção via $A^TA$/$AA^T$; valores
      singulares/norma espectral; aproximação de baixo posto; Eckart-
      Young-Mirsky; Decomposição Polar; SVD vs. decomposição espectral;
      SVD aplicada a $X$; filtragem colaborativa); mais 3 questões
      discursivas, sem solução (trabalho do aluno). **Uma correção real
      feita durante a escrita do gabarito:** o item (b) do bloco "A SVD
      aplicada a $X$" (Pausa Ativa 4) tinha sido rascunhado com uma
      resposta internamente contraditória (marcado ✔ com uma
      justificativa que na verdade demonstrava ✗) — identificado e
      corrigido antes de finalizar, com a Proposição
      $\text{cond}(X^TX)=\text{cond}(X)^2$ usada para justificar a
      resposta certa (✗, o item afirmava o oposto do que a proposição
      garante). Também corrigido um item do bloco "Eckart-Young-Mirsky"
      que, como rascunhado originalmente, testava uma afirmação
      **verdadeira** (a generalização de Mirsky para norma de Frobenius)
      rotulada como armadilha de "falsa dicotomia" — reescrito para
      manter a premissa verdadeira (mesma matriz minimizadora nas duas
      normas) mas testar uma conclusão indevida (mesmo *valor* mínimo
      nas duas normas, que é falsa em geral), verificado numericamente
      antes de fixar a resposta.
- **Um erro de raciocínio pego e corrigido nesta sessão, antes de
  publicar:** ao rascunhar o item (c) do bloco "SVD vs. decomposição
  espectral" dos Exercícios, a primeira tentativa generalizava
  incorretamente a condição do Remark do MathML (SVD = decomposição
  espectral só para matrizes **simétricas semidefinidas positivas**,
  não para qualquer simétrica) — corrigido reescrevendo o item (a) do
  mesmo bloco para testar exatamente esse limite (falso em geral,
  verdadeiro só no caso PSD), com o item (b) construindo a mecânica do
  contraexemplo (autovalor negativo $\Rightarrow$ troca de sinal em
  $U$ ou $V$) e o item (c) confirmando o caso PSD.

**Validação (itens obrigatórios, todos passados):**

1. Balanceamento de `:::` verificado por script (pilha LIFO): 0 abas
   abertas remanescentes; 4 ocorrências de fechamento duplicado
   acidental (bug de cópia do padrão da Aula 4) encontradas e
   corrigidas antes de renderizar.
2. `uv run python3 preview-watch.py --incremental` (nunca `quarto
   render` direto, por instrução do `CLAUDE.md`): `notas.html` e
   `slides.html` gerados sem erro/traceback.
3. Glifos: 76 `□` no total (40 das 5 Pausas Ativas × 2 formatos + 36 dos
   9 blocos de Exercícios), 11 `✔` + 9 `✗` nas 5 Resposta dos slides;
   zero `<input type="checkbox">` real em ambos os arquivos renderizados
   (única ocorrência de `type="checkbox"` é a regra CSS genérica do
   tema).
4. Exercícios confirmados por contagem programática: 3 discursivas + 9
   blocos de V/F (36 itens) — densidade um pouco acima da Aula 4 (8
   blocos), justificada pelos 6 blocos de conteúdo novo desta aula
   (contra 5 da Aula 4).
5. YAML confirmado: `output-file: notas.html` (html) e
   `output-file: slides.html` (revealjs), mesmo bloco `format:`
   compartilhado das Aulas 1-4.
6. Inspeção visual das 4 figuras matplotlib (PNG do `_freeze/`) e dos 2
   diagramas TikZ (SVG convertido via `rsvg-convert`): todas
   consistentes com a matemática pretendida — círculo/elipse com
   `aspect("equal", adjustable="box")` em todos os painéis geométricos;
   TikZ sem sobreposição de caixas, margens generosas.

**Etapa 5 concluída nesta sessão:** link da Aula 5 no `../index.qmd`
convertido de texto em negrito para link (mesmo formato das Lições
1-4); dicionário de notações abaixo atualizado.

### Dicionário de notações — símbolos novos desta aula

| Símbolo/termo | Significado | Introduzido em |
|---|---|---|
| $A=U\Sigma V^T$ | Decomposição em Valores Singulares (SVD) | Aula 5, Bloco 3 |
| $\sigma_i$ | valor singular (sempre real, $\ge0$, ordenado $\sigma_1\ge\dots\ge\sigma_r>0$) | Aula 5, Bloco 3 |
| $\mathbf{u}_i$ (coluna de $U$) | vetor singular à esquerda (autovetor de $AA^T$) | Aula 5, Bloco 3 |
| $\mathbf{v}_i$ (coluna de $V$) | vetor singular à direita (autovetor de $A^TA$) | Aula 5, Bloco 3 |
| SVD completa / reduzida / truncada | $U,V$ quadradas completas / $U$ recortada ao posto / soma dos $k$ primeiros termos | Aula 5, Bloco 3-5 |
| $\hat{A}^{(k)}=\sum_{i=1}^k\sigma_i\mathbf{u}_i\mathbf{v}_i^T$ | aproximação de posto-$k$ (SVD truncada) | Aula 5, Bloco 5 |
| $\|A\|_2$ | norma espectral ($=\sigma_1$, Teo. 4.24) | Aula 5, Bloco 5 |
| Teorema de Eckart-Young-Mirsky | $\hat{A}^{(k)}$ é a melhor aproximação de posto $k$ em norma espectral (e de Frobenius, generalização de Mirsky), erro $=\sigma_{k+1}$ | Aula 5, Bloco 5 |
| $A=QS$ | Decomposição Polar ($Q$ ortogonal, $S$ simétrica semidefinida positiva) | Aula 5, Bloco 6 |
| $\text{cond}(X)=\sigma_{\max}/\sigma_{\min}$ | número de condição via valores singulares (Boyd, já citado na Aula 4); $\text{cond}(X^TX)=\text{cond}(X)^2$ | Aula 5, Bloco 4 |

**Pendência para a Aula 6:** a SVD decompõe uma matriz estática, mas não
diz como encontrar os parâmetros que minimizam uma função de perda — as
Equações Normais (Aula 3) já usaram, implicitamente, a ideia de "a perda
parar de diminuir" sem nunca formalizar o que isso significa em várias
variáveis. A Aula 6 abre a Parte 2 do curso (Cálculo da Otimização
Diferenciável) com exatamente essa ferramenta: gradiente $\nabla f$ e
Jacobiano $J$.

## Aula 6 — Derivadas Parciais, Jacobiano e o Vetor Gradiente (2026-09-13)

Construída na mesma sessão da Aula 5, ciclo completo (planejamento →
aula → gabarito → link da disciplina → `_progresso.md`), sem parar nos
checkpoints intermediários (mesma autorização do usuário que cobriu a
Aula 5). Abre a **Parte 2** do curso ("Cálculo da Otimização
Diferenciável") — mudança de eixo reconhecida explicitamente na
Abertura: as cinco aulas anteriores nunca precisaram definir
"minimizar uma função", mas as Equações Normais (Aula 3) já usaram essa
ideia implicitamente, via um argumento geométrico de projeção.

- [x] `_00-planejamento.md` — Estratégia B (Inside-Out com
      Problema-Fio), 7 blocos, ~100min. 6 fontes originalmente
      planejadas do `mathml.pdf` (Cap. 5, Vector Calculus: Def. 5.5
      Derivada Parcial/Gradiente, Remark convenção linha, §5.2.1 regras
      de derivação, Def. 5.6 Jacobiano, Def. 5.2/§7.1 "subida mais
      íngreme" sem prova), offset **+6** reconfirmado (Def. 5.5 p.
      146→152; Def. 5.6 p. 150→156). **Uma 7ª fonte encontrada durante a
      escrita do Bloco 5** (não antecipada no planejamento original):
      MathML Exemplo 5.11 ("Gradient of a Least-Squares Loss in a
      Linear Model", p. 153-154→159-160) resolve **exatamente** o
      problema desta aula (perda de mínimos quadrados de modelo linear,
      via regra da cadeia com Jacobiano) — substituiu uma nota de
      "construção própria" originalmente planejada por uma citação
      direta e precisa, com tradução/adaptação de notação
      ($\mathbf{e}=\mathbf{y}-\Phi\boldsymbol{\theta}=-\mathbf{r}$).
      Derivada direcional (Bloco 4) permanece **construção nossa**
      — busca confirmou que nenhuma das 3 fontes da disciplina define o
      termo no material coberto (`optml.pdf`/`copt.pdf` definem, mas
      estão reservados para aulas de otimização não-suave, mais
      adiante); a prova de que o gradiente maximiza a derivada
      direcional (via Cauchy-Schwarz, Aula 1) também é prova nossa — o
      MathML só afirma o resultado, nunca prova.
- [x] `index.qmd` — dual HTML/RevealJS, 7 blocos: (1) Revisão/Introdução
      com reconhecimento explícito do corte Álgebra Linear→Cálculo +
      Problema Motivador (direção de redução mais rápida de
      $L(\boldsymbol{\beta})$ sem resolver sistema, cenário de milhões
      de parâmetros) + Pausa Ativa 1; (2) Derivada parcial (Def. 5.5,
      metade) aplicada a um exemplo bivariado concreto (amostra de $5$
      bairros, $2$ atributos), limite numérico vs. fórmula exata + Pausa
      Ativa 2; (3) Gradiente como vetor-linha (Def. 5.5 completa +
      Remark de convenção) e regras de derivação (soma/produto/cadeia,
      §5.2.1), com desenvolvimento *principled* completo do gradiente
      da perda quadrática ($\nabla_{\boldsymbol{\beta}}\|X\boldsymbol{
      \beta}-\mathbf{y}\|^2=2(X\boldsymbol{\beta}-\mathbf{y})^TX$),
      recuperando as Equações Normais como $\nabla L=\mathbf{0}$ + Pausa
      Ativa 3; (4) Derivada direcional (construção própria) + prova
      própria (Cauchy-Schwarz, Aula 1) de que o gradiente maximiza a
      derivada direcional, com verificação numérica/geométrica (contorno
      + curva de cosseno) + Pausa Ativa 4; (5) Jacobiano (Def. 5.6),
      aplicado ao resíduo ($J_{\mathbf{r}}(\boldsymbol{\beta})=X$,
      observação nossa) e à regra da cadeia com Jacobiano (MathML
      Exemplo 5.11, recuperando o resultado do Bloco 3 por rota
      diferente) + Pausa Ativa 5; (6) Verificação numérica —
      compromisso truncamento-vs-arredondamento na escolha de $h$ para
      diferença finita, caso especial honesto (perda quadrática do
      problema-fio tem $f'''\equiv0$, erro de truncamento zero, só
      arredondamento visível), sem pausa ativa (mesmo padrão do bloco
      de "aplicação no dado real" da Aula 4); (7) Fechamento retomando
      as 4 perguntas + ponte para a Aula 7 (Hessiana — $\nabla L=
      \mathbf{0}$ identifica ponto crítico, não garante mínimo). 5
      Pausas Ativas (Blocos 1-5; Blocos 6-7 sem pausa). 7 elementos
      visuais em `.fig-resize` (2 TikZ: roteiro de abertura, ponte final
      para a Aula 7; 2 figuras matplotlib com imagem — contorno +
      derivada direcional em função do ângulo (Bloco 4), erro da
      diferença finita em função de $h$ (Bloco 6); 3 chunks adicionais
      de só texto/verificação numérica, também em `.fig-resize` por
      consistência de estilo).
- **Um bug real de visualização encontrado e corrigido durante a
  verificação visual:** a primeira versão da figura do Bloco 4
  desenhava a seta do gradiente com uma escala fixa em unidades de
  dado (`0.08/norma`), que — como os eixos $\beta_1$ (faixa $0,6$) e
  $\beta_2$ (faixa $0,04$) têm escalas muito diferentes — jogava a
  ponta da seta muito além dos limites visíveis do eixo $\beta_2$,
  tornando a seta **invisível** no gráfico renderizado (só o ponto
  vermelho aparecia). Corrigido escalando o vetor como fração do
  próprio intervalo visível do eixo dominante, e a prosa ao redor da
  figura foi ajustada para não alegar ortogonalidade **visual** exata
  às curvas de nível (só visível com eixos de mesma escala, que aqui
  distorceria a legibilidade das curvas) — o fato matemático em si
  (provado via Cauchy-Schwarz) não depende da escolha de desenho, e
  continua correto e citado em prosa.
- **Números verificados via script Python (`uv run python3`, kernel
  `homepage`) antes de escrever, nunca fabricados:**
  - Gradiente de $L(\boldsymbol{\beta})=\|X\boldsymbol{\beta}-
    \mathbf{y}\|^2$ em $\boldsymbol{\beta}_0=(0{,}4;\,0{,}02;\,
    -0{,}15;\,0{,}7)$: $\nabla L=[-5\,846{,}13;\ 71\,951{,}88;\
    4\,014{,}13;\ 1\,643{,}72]$ (forma coluna $2X^T\mathbf{r}$),
    conferido contra diferença finita central ($h=10^{-5}$), diferença
    relativa $\approx10^{-12}$.
  - Derivada direcional: para $5$ direções testadas em
    $\boldsymbol{\beta}_0$, $D_{\mathbf{v}}L$ bate exatamente com
    $\nabla L\cdot\mathbf{v}$ em todos os casos; máximo
    ($\approx72\,319{,}19=\|\nabla L\|$) na direção do gradiente
    normalizado, mínimo na direção oposta.
  - Exemplo bivariado (amostra de $5$ bairros, `MedInc`/`HouseAge`):
    em $(\beta_1,\beta_2)=(0{,}5;\,0{,}02)$, $\partial L/
    \partial\beta_1\approx5{,}637$, $\partial L/\partial\beta_2\approx
    95{,}040$; gradiente ângulo $\approx86{,}6°$, norma
    $\approx95{,}207$; máximo de $D_{\mathbf{v}}L$ sobre a grade de
    ângulos confirmado exatamente nesse ângulo.
  - Jacobiano do resíduo $J_{\mathbf{r}}(\boldsymbol{\beta})=X$
    confirmado coluna a coluna por diferença finita, erro máximo
    $\sim10^{-10}$ nas $4$ colunas.
  - Compromisso de $h$: erro de diferença finita central medido para
    $h$ de $10^{-2}$ a $10^{-13}$ — confirmado **monotonicamente
    crescente** conforme $h\to0$ (sem "U"), consistente com
    $f'''\equiv0$ para a perda quadrática do problema-fio.
- [x] `_01-respostas.md` — discussão em prosa + V/F resolvido das 5
      Pausas Ativas; heurística nomeada + afirmação + resposta +
      justificativa para os 32 itens de V/F dos Exercícios (8 blocos:
      derivada parcial; convenção linha/coluna do gradiente; regras de
      derivação e gradiente da perda quadrática; derivada direcional;
      direção de subida mais íngreme; Jacobiano; regra da cadeia com
      Jacobiano; verificação numérica); mais 3 questões discursivas,
      sem solução (trabalho do aluno).

**Validação (itens obrigatórios, todos passados):**

1. Balanceamento de `:::` verificado por script (pilha LIFO) desde a
   primeira escrita — zero erros (lição aprendida da Aula 5, onde um
   bug de fechamento duplicado só foi pego depois de escrever; desta
   vez verificado a cada bloco).
2. `uv run python3 preview-watch.py --incremental`: `notas.html` e
   `slides.html` sem erro/traceback, incluindo depois da correção do
   bug de visualização do Bloco 4.
3. Glifos: 72 `□` no total (40 das 5 Pausas Ativas × 2 formatos + 32 dos
   8 blocos de Exercícios), 12 `✔` + 8 `✗` nas 5 Resposta dos slides;
   zero `<input type="checkbox">` real em ambos os arquivos.
4. Exercícios confirmados por contagem programática: 3 discursivas + 8
   blocos de V/F (32 itens) — mesma densidade da Aula 4 (5 blocos de
   conteúdo novo, Blocos 2-6).
5. YAML confirmado: `output-file: notas.html` (html) e
   `output-file: slides.html` (revealjs), mesmo bloco `format:`
   compartilhado das Aulas 1-5.
6. Inspeção visual das 2 figuras matplotlib (PNG do `_freeze/`, incluindo
   re-inspeção depois da correção do bug de escala) e dos 2 diagramas
   TikZ (SVG convertido via `rsvg-convert`): consistentes com a
   matemática pretendida; TikZ sem sobreposição, margens generosas.

**Etapa 5 concluída nesta sessão:** link da Aula 6 no `../index.qmd`
convertido de texto em negrito para link (mesmo formato das Lições
1-5); dicionário de notações abaixo atualizado.

### Dicionário de notações — símbolos novos desta aula

| Símbolo/termo | Significado | Introduzido em |
|---|---|---|
| $\partial f/\partial x_i$ | derivada parcial de $f$ em relação a $x_i$ (demais variáveis fixas) | Aula 6, Bloco 2 |
| $\nabla f$, $\nabla_{\mathbf{x}}f$, $df/d\mathbf{x}$ | gradiente de $f$ (vetor-**linha**, convenção MathML) | Aula 6, Bloco 3 |
| $D_{\mathbf{v}}f(\mathbf{x})$ | derivada direcional de $f$ em $\mathbf{x}$, na direção unitária $\mathbf{v}$ | Aula 6, Bloco 4 |
| $J$, $J_f(\mathbf{x})$ | Jacobiano de $f:\mathbb{R}^n\to\mathbb{R}^m$ (matriz $m\times n$, *numerator layout*; gradiente = caso $m=1$) | Aula 6, Bloco 5 |
| $\mathbf{r}(\boldsymbol{\beta})=X\boldsymbol{\beta}-\mathbf{y}$ | resíduo como função vetorial de $\boldsymbol{\beta}$; $J_{\mathbf{r}}(\boldsymbol{\beta})=X$ | Aula 6, Bloco 5 |
| regra da cadeia com Jacobiano | $\nabla_{\boldsymbol{\beta}}(g\circ\mathbf{r})=\nabla_{\mathbf{r}}g\cdot J_{\mathbf{r}}(\boldsymbol{\beta})$ | Aula 6, Bloco 5 |
| ponto crítico | ponto onde $\nabla f=\mathbf{0}$ — não garante mínimo/máximo sem informação adicional | Aula 6, Fechamento |

**Pendência para a Aula 7:** $\nabla L=\mathbf{0}$ identifica um ponto
crítico, mas não diz se é mínimo, máximo ou sela — para a perda
quadrática do problema-fio isso funciona porque $X^TX$ é semidefinida
positiva (Aula 4), mas essa garantia não vem do gradiente sozinho.
Tema da Aula 7 (Convexidade e a Hessiana, syllabus): a segunda derivada
em várias variáveis decide essa questão em geral.

## Migração para `exercicios.qmd`/`soluções.qmd` públicos por aula (2026-09-14)

Retomada de uma migração interrompida por rate limit (agentes paralelos
anteriores morreram no meio do trabalho). Executada sequencialmente,
sem sub-agentes, seguindo a convenção descrita em `../CLAUDE.md` (seção
"Exercícios"): a seção "Exercícios" embutida em cada `aulaNN/index.qmd`
(HTML + RevealJS) foi removida e substituída por dois arquivos-irmãos
publicados, `aulaNN/exercicios.qmd` (questões, autocontidas) e
`aulaNN/soluções.qmd` (gabarito, agora público) — mais um link de
navegação simples perto do Fechamento (`[Exercícios](exercicios.qmd)
[Soluções](soluções.qmd)`, nas duas saídas). As Pausas Ativas não foram
afetadas — continuam embutidas em `index.qmd`, com gabarito oculto em
`_0N-respostas*.md`.

**Por aula:**

- **Aula 1 — caso especial, exige registro explícito.** Ao contrário do
  que a tarefa original supunha, `aula01/index.qmd` **nunca teve** uma
  seção de Exercícios — verificado em todo o histórico do git (`git log
  --all -p`), a seção nunca existiu em nenhum commit. O arquivo-raiz
  antigo `exercicios.qmd` (já removido, ver abaixo) também não tinha
  nenhuma seção "Aula 01"/"Aula 1" — começava direto em "Aula 02". Ou
  seja: não havia gabarito para recuperar porque **também não havia
  pergunta** para recuperar. Em vez de só escrever um gabarito para
  itens inexistentes, foi necessário **autorar do zero** tanto as
  perguntas quanto o gabarito — 3 questões discursivas e 8 blocos de
  V/F (32 itens), cobrindo vetores/operações, Hipótese de Suavidade/
  $k$-NN, subespaços, Hipótese da Variedade, normas, métrica formal,
  maldição da dimensionalidade e distância do cosseno — seguindo a
  metodologia de heurísticas (contrafactual/limite/transferência/falsa
  dicotomia) e a Heurística 3 restrita a outro cenário de ML, como
  exigido pelo `CLAUDE.md`. Conteúdo original, não uma recuperação;
  revisar com atenção redobrada na próxima leitura humana.
- **Aula 2 — já estava pronta** de uma sessão anterior; só confirmada
  (balanceamento de `:::`, ausência de glifos de checkbox clicável).
- **Aula 3 — migração direta.** Perguntas extraídas de `index.qmd`,
  gabarito de `_02-solucoes.md` (12 blocos de V/F, 48 itens — acima da
  faixa de 6–10 blocos do `CLAUDE.md`, preservado como estava por ser
  conteúdo já produzido; sinalizar para eventual revisão futura, não
  cortado nesta sessão). `_02-solucoes.md` apagado.
- **Aulas 4–6 — convenção antiga (`_01-respostas.md` misto).** Cada
  arquivo consolidava Pausas Ativas + Exercícios num só lugar; a parte
  de Exercícios foi extraída para `soluções.qmd`, e `_01-respostas.md`
  foi *trimado* (não apagado) para conter só a parte de Pausas Ativas,
  mantendo o mesmo nome de arquivo (convenção antiga desta disciplina,
  não renomeado para `_0N-respostas-pausas.md`).
- **Reescrita de autocontenção (todas as aulas migradas).** Vários
  itens de V/F e questões discursivas, herdados de `index.qmd`,
  dependiam de referências internas invisíveis fora da aula —
  `"Bloco N"`, `"Aula N"`, `"nesta aula"`, `"Definição X.Y"`,
  `"MathML"`, números de página do livro-texto. Cada `exercicios.qmd`
  ganhou uma caixa **Convenções** no topo, restaurando inline toda
  notação/definição necessária (equações normais, projeção, subespaço,
  norma, métrica, autovalor/autovetor, SVD, gradiente/Jacobiano,
  exemplos numéricos concretos como o dataset California Housing e a
  matriz de notas de filmes), e cada item problemático foi reescrito
  para apontar para essa caixa em vez de para a estrutura interna da
  aula. Os `soluções.qmd` receberam o mesmo tratamento nas
  justificativas (com menos rigor, já que o requisito formal do
  `CLAUDE.md` é só sobre `exercicios.qmd`, mas a leitura ficaria confusa
  sem isso). Depois de cada reescrita, o texto de cada afirmação em
  `exercicios.qmd` foi comparado programaticamente (script Python) com
  o campo **Afirmação** correspondente em `soluções.qmd`, byte a byte
  após normalização de espaço em branco — zero divergência final em
  todas as aulas migradas nesta sessão (3, 4, 5, 6).

**Limpeza em nível de disciplina:**

- `exercicios.qmd` da raiz (arquivo consolidado antigo, misturando
  todas as aulas — o gatilho desta migração por estar com conteúdo
  desatualizado/quebrado em partes) **apagado**.
- `index.qmd` da disciplina: removida a linha de link
  `[Exercícios de todas as aulas](./exercicios.qmd)`, que apontava para
  o arquivo apagado. `styles.css` da raiz não foi tocado (ainda usado
  por `computing-and-society`, fora do escopo desta migração).

**Validação (todas as 6 aulas, itens obrigatórios):**

1. Balanceamento de `:::` (pilha LIFO) verificado por script em
   `index.qmd`, `exercicios.qmd` e `soluções.qmd` de cada aula — zero
   erros.
2. `grep` por `- [ ]`, `- [x]`, `☐`, `☒` nos três arquivos de cada
   aula — zero ocorrências em todas.
3. Contagem de itens `- □` em cada `exercicios.qmd` comparada com a
   contagem de blocos `**Afirmação:**` no `soluções.qmd`
   correspondente — igual em todas as 6 aulas (32, 32, 48, 32, 36, 32
   itens nas Aulas 1–6, respectivamente).
4. Releitura completa de cada `exercicios.qmd` publicado, confirmando
   que nenhum item depende de "nesta aula"/"Bloco N"/notação não
   redefinida na própria caixa de Convenções.
5. `uv run python3 preview-watch.py --incremental` executado da raiz do
   projeto — ver seção de render abaixo para o resultado.

**Correção pós-migração (2026-09-14, mesma sessão):** uma varredura
manual por palavras-chave (`sensor`, `físico`, `sinal`, `satélite`,
`elétrica`, `epidemiologia`, etc.) encontrou **12 itens de V/F** com
`Heurística: Transferência` que violavam a regra já estabelecida no
`CLAUDE.md` ("a heurística 3 deve migrar para outro cenário de
Aprendizado de Máquina, nunca para um domínio estapafúrdio ou
decorativo") — a migração automática, ao reescrever itens para
autocontenção, reintroduziu exemplos de física/engenharia/sinais em
vez de manter o domínio de ML. Todos os 12 foram reescritos (em
`exercicios.qmd` **e** `soluções.qmd`, mantendo a mesma resposta e
mecânica matemática testada):

- **Aula 2:** "imagens de satélite/modelo físico" → reconhecimento
  facial; "sensor sempre desligado" → atributo binário nunca ativado
  num dataset.
- **Aula 3 (6 itens):** previsão de demanda de energia/modelo físico →
  risco de crédito (German Credit); processamento de sinal de áudio →
  sistema de recomendação por fatoração de matrizes; compressão de
  vídeo por frequência → compressão de embeddings via PCA; termômetro/
  temperatura → anotações redundantes de rotulação por crowdsourcing;
  reconstrução de sinais → regressão com atributos linearmente
  dependentes; experimento de física → regressão financeira sobre
  outro dataset; sensores IoT Celsius/Fahrenheit → mantido (Celsius/
  Fahrenheit), mas recontextualizado como atributo de um dataset de
  previsão de demanda de energia (ML), não mais "sensores IoT".
- **Aula 4 (4 itens):** modelo de epidemiologia → cadeia de Markov em
  aprendizado por reforço; rede elétrica/matriz de admitância → matriz
  Laplaciana de grafo em *clustering* espectral; sensores redundantes
  removidos fisicamente → atributos redundantes removidos de um
  dataset; sensores industriais Celsius/Pascal → dataset com atributos
  em escalas heterogêneas (German Credit).

Justificativas correspondentes também revisadas para remover menções
remanescentes aos domínios antigos (ex.: "epidemiologia, ecologia" e
"redes elétricas" apareciam nas justificativas mesmo depois da
Afirmação já ter sido corrigida numa primeira passada). Rerenderizado
e confirmado nos HTMLs publicados. **Nota para revisão futura:** o
mesmo tipo de varredura não foi feito ainda nas disciplinas
`supervised-learning` (2 itens já corrigidos à parte) e
`unsupervised-learning` (ainda não verificada) além do que já constava
nos relatórios de verificação de cada uma.

## Aulas 7–15

Não iniciadas.
