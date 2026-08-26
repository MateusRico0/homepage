## Resumo — Aula 2: Representações Matriciais, Sistemas Lineares e Independência

A Aula 1 tratou um vetor por vez — um ponto no espaço de características.
Mas um dataset real nunca é um vetor só: são $N$ observações, cada uma com
$d$ atributos. Esta aula dá o passo natural — empilhar esses vetores numa
**matriz de design** $X \in \mathbb{R}^{N\times d}$ — e usa a Regressão
Linear Múltipla como fio condutor concreto: prever $\hat{\mathbf{y}} =
X\mathbf{w}$ é, literalmente, resolver (ou aproximar) um sistema linear
$X\mathbf{w} = \mathbf{y}$. A aula formaliza operações matriz-vetor sob
duas óticas (linha a linha vs. combinação linear de colunas), as três
formas qualitativas que a solução de um sistema linear pode assumir, e
fecha com independência linear e posto (*rank*) — a ferramenta que decide,
antes de tentar resolver qualquer coisa, se um sistema *pode* ter solução
única, e a base matemática para diagnosticar multicolinearidade num
dataset real.

**Pré-requisitos:** Aula 1 completa — em particular, a prova de que o
conjunto-solução de $A\mathbf{x}=\mathbf{0}$ é um subespaço vetorial
(Bloco 3 da Aula 1) é revisitada aqui como caso particular do problema
mais geral desta aula, $A\mathbf{x}=\mathbf{b}$ com $\mathbf{b}$
qualquer. Álgebra matricial básica do ensino médio (multiplicação de
matrizes por definição, sem interpretação geométrica ainda).

**Objetivos de aprendizagem** (do `index.md`, Lesson 2):
- **ML Concept:** Representações matriciais multivariáveis de dados e
  Regressão Linear Múltipla.
- **Mathematical Concept:** Operações matriz-vetor, posto (*rank*),
  independência linear, e solvabilidade de sistemas ($A\mathbf{x} =
  \mathbf{b}$).
- **Objectives:** Formular transformações de dataset e modelos lineares
  através de sistemas matriciais.
- **Expected Competencies:** Expressar datasets multidimensionais como
  matrizes de projeto (*design matrices*), calcular o posto de uma
  matriz, e identificar problemas de multicolinearidade no espaço de
  características.

**Estratégia Pedagógica:** Estratégia B (Inside-Out com Problema-Fio) —
aula de fundação matemática de representação/linguagem (matrizes,
sistemas lineares), guiada pela necessidade do idioma matemático mais
do que por um modelo/algoritmo específico a "desmontar".

**Dataset real usado como fio condutor:** *California Housing* (via
Hugging Face Hub, `gvlassis/california_housing`), já usado na Aula 1 —
continuidade de dataset entre aulas. Um subconjunto de atributos
(`MedInc`, `HouseAge`, `AveRooms`, `AveBedrms`) forma a matriz de design
$X$ para prever `MedHouseVal`. `AveRooms` e `AveBedrms` são naturalmente
correlacionados (mais cômodos tendem a vir com mais quartos) — bom
candidato real para ilustrar quase-multicolinearidade no Bloco 5, sem
precisar fabricar uma coluna artificialmente duplicada.

## Plano de aula — Aula 2 (carga horária real da turma: 100min)

Feedback do usuário (2026-08-26): o conteúdo original desta aula, na
prática, se dava em ~50min — muito abaixo dos 100min reais de aula.
Não era um problema de foco (o conteúdo selecionado já servia o fio
condutor da aula), era falta de profundidade real nos mesmos blocos.
Quatro adições feitas para preencher a carga horária real sem diluir o
fio condutor — detalhadas dentro dos blocos 2, 3 e 5 abaixo.

1.  **Da Vetor ao Dataset: a Matriz de Design** (~15 min) — Organizador
    prévio: a Aula 1 trabalhou com um vetor $\mathbf{x}\in\mathbb{R}^d$
    por vez; um dataset é $N$ desses vetores empilhados. Definição de
    matriz como tabela de números e como "pilha" de vetores-linha (cada
    linha = uma observação) ou vetores-coluna (cada coluna = um
    atributo). A matriz de design $X\in\mathbb{R}^{N\times d}$ do
    subconjunto real de California Housing. Roteiro explícito da aula:
    (1) como generalizar vetor para matriz e o que isso compra; (2) o
    que significa multiplicar uma matriz por um vetor, de duas formas
    diferentes; (3) quando um sistema linear tem solução, e quantas; (4)
    como saber se um conjunto de atributos tem informação redundante.

2.  **Operações com Matrizes: Duas Leituras de $A\mathbf{x}$** (~20 min)
    — O produto matriz-vetor $A\mathbf{x}$ sob duas óticas
    complementares: (a) linha a linha, cada entrada de $A\mathbf{x}$ é o
    produto interno de uma linha de $A$ com $\mathbf{x}$; (b) coluna a
    coluna, $A\mathbf{x}$ é uma **combinação linear das colunas de $A$**,
    pesada pelas entradas de $\mathbf{x}$ — a leitura que mais importa
    daqui para frente (posto, independência, Aula 3). Conectar com ML:
    a predição da regressão múltipla $\hat{\mathbf{y}} = X\mathbf{w}$ é
    exatamente um produto matriz-vetor, e $\mathbf{w}$ pondera o quanto
    cada atributo (coluna de $X$) contribui para a previsão. Produto
    matriz-matriz definido brevemente (será revisitado na Aula 3 via
    $X^TX$). **[Adição 2026-08-26]** Walkthrough completo com um
    $\mathbf{w}$ inventado: previsão dos 6 bairros da amostra vs. valor
    real (`MedHouseVal`), introduzindo o **resíduo**
    $\hat{\mathbf{y}}-\mathbf{y}$ como antecipação direta da pergunta
    da Aula 3 (existe $\mathbf{w}$ que minimiza esse erro?).

3.  **Sistemas Lineares: Quando $A\mathbf{x}=\mathbf{b}$ Tem Solução?**
    (~25 min) — Generalização direta do resultado já visto na Aula 1
    ($A\mathbf{x}=\mathbf{0}$, sempre com pelo menos a solução trivial,
    é um subespaço): agora $\mathbf{b}$ é arbitrário, e a pergunta muda
    de "que subespaço é a solução" para "existe solução, e é única?".
    As três formas qualitativas (nenhuma, exatamente uma, infinitas
    soluções), ilustradas geometricamente em $\mathbb{R}^2$/$\mathbb{R}^3$
    antes do caso geral. Ponte com ML: o "sonho" de ajuste perfeito
    $X\mathbf{w}=\mathbf{y}$ é um sistema com $N$ equações (uma por
    observação) e $d$ incógnitas (uma por atributo). Em problemas reais,
    $N \gg d$ (muito mais observações que atributos) — um sistema
    **sobredeterminado**, que genericamente não tem solução exata
    nenhuma. Esse é o problema sem resposta que fecha a aula e abre a
    Aula 3 (projeções ortogonais, mínimos quadrados). **[Adição
    2026-08-26]** Exemplo resolvido completo de eliminação de Gauss
    (sistema 3×3, forma triangular, substituição reversa), incluindo
    como reconhecer os outros dois casos (linha "$0=$ não-zero" =
    contradição/sem solução; linha "$0=0$" = redundância/infinitas
    soluções) sem fazer a conta toda — a ponte natural para o atalho do
    posto no Bloco 5.

4.  **Independência Linear** (~20 min) — Definição formal: um conjunto
    de vetores é linearmente independente se a única combinação linear
    que dá o vetor nulo é a trivial (todos os coeficientes zero).
    Intuição: um vetor linearmente dependente dos demais não carrega
    informação nova — é redundante. Contraexemplo deliberado: dado um
    conjunto de 3 vetores em $\mathbb{R}^2$, eles nunca podem ser
    independentes (mais vetores que dimensões força dependência) —
    verificado numericamente. Conexão com ML: se uma coluna da matriz de
    design é combinação linear exata de outras (ex.: um atributo
    duplicado em outra unidade), essa coluna não acrescenta informação
    ao modelo — a primeira definição formal de multicolinearidade.

5.  **Base e Posto (*Rank*): Medindo Informação Independente** (~25 min)
    — Posto como o número máximo de colunas (ou linhas — mesmo valor,
    por um teorema citado, não provado aqui) linearmente independentes
    de uma matriz. Matriz de posto completo em coluna vs. matriz
    deficiente em posto. Conectar de volta ao Bloco 3: $A\mathbf{x} =
    \mathbf{b}$ tem solução única apenas quando $A$ tem posto completo
    (no sentido apropriado); posto deficiente $\Rightarrow$ ou nenhuma
    solução, ou infinitas. Exemplo real: calcular o posto da matriz de
    design do subconjunto de California Housing, e mostrar
    quase-multicolinearidade real entre `AveRooms` e `AveBedrms`
    (correlação alta, mas não exatamente $1$ — dependência linear
    aproximada, não exata). **Aviso explícito, verificado nesta sessão
    antes de escrever a aula:** multicolinearidade *exata* é rara em
    dados reais (exigiria uma relação linear perfeita); o problema
    prático mais comum é a quase-dependência, que não quebra o posto
    tecnicamente mas antecipa a instabilidade numérica que a Aula 4
    (autovalores) vai quantificar via número de condição. **[Adições
    2026-08-26]** (a) Antes da definição formal de posto, uma
    visualização geométrica do espaço-coluna (no exemplo do Bloco 3:
    o espaço-coluna de $A$ é uma reta, e $\mathbf{b}$ está nela ou não)
    — a definição formal e o critério $\text{rk}(A)=\text{rk}(A|\mathbf{b})$
    vêm depois, como formalização do que o desenho já mostrou, não como
    ponto de partida. (b) Demonstração numérica da instabilidade da
    quase-multicolinearidade: ajuste por mínimos quadrados numa amostra
    pequena (20 bairros) de `AveRooms`/`AveBedrms`, perturbação de 1% em
    `MedHouseVal` fazendo o peso de `AveBedrms` variar ~30%, contra
    <1% de variação no par bem condicionado `MedInc`/`HouseAge` sob o
    mesmo ruído — evidência concreta, não só uma promessa de "isso é
    assunto da Aula 4".

6.  **Fechamento: Multicolinearidade na Prática e Ponte para a Aula 3**
    (~10 min) — Retomar as quatro perguntas de abertura, cada uma
    respondida em uma frase. Nomear o que fica em aberto: sistemas
    sobredeterminados (o caso comum em ML) genericamente não têm solução
    exata — a Aula 3 responde "qual é a melhor aproximação possível" via
    projeção ortogonal sobre o espaço-coluna de $X$, chegando às
    Equações Normais ($X^TX\hat{\mathbf{w}} = X^T\mathbf{y}$, adiantadas
    aqui só de nome).
