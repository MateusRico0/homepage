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

## Aulas 4–15

Não iniciadas.
