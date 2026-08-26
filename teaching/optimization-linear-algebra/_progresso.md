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

## Aulas 3–15

Não iniciadas.
