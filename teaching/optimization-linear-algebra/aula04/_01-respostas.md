# Gabarito — Aula 4: Autovalores, Autovetores e Matrizes Simétricas

Este arquivo consolida a discussão e a solução V/F das 5 Pausas Ativas
da aula. Nunca publicado no site (prefixo `_`). O gabarito da seção
Exercícios (agora pública) vive em `soluções.qmd`.

## Pausas Ativas

### Pausa Ativa 1 (Bloco 1 — Revisão e Introdução)

**Pergunta motivadora:** se dois pares de atributos têm a mesma
correlação entre si, eles necessariamente têm o mesmo número de
condição de $X^TX$?

**Discussão:** não — a Aula 3 mediu a fragilidade via perturbação, sem
isolar o que exatamente a causa. Correlação mede o alinhamento angular
entre duas colunas (o cosseno do ângulo entre elas, na linguagem da
Aula 1); número de condição de $X^TX$ mistura esse alinhamento **com** a
escala/variância de cada coluna. Duas colunas quase-colineares mas com
variâncias parecidas dão um número de condição alto principalmente pelo
alinhamento; duas colunas ortogonais mas com variâncias muito diferentes
ainda podem dar um número de condição alto, dessa vez pela escala — o
Bloco 6 confirma isso nos autovalores reais dos dois pares (`AveRooms`/
`AveBedrms` vs. `MedInc`/`HouseAge`).

**V/F — Resposta:**
- ✔ Ortogonalidade (correlação $0$) só garante $X^TX$ diagonal; se as
  variâncias das duas colunas forem muito diferentes, o número de
  condição ainda pode ser grande.
- ✔ Mesma mecânica (colunas quase-redundantes $\Rightarrow$ $X^TX$
  mal-condicionada), outro dataset e outra tarefa de ML (risco de
  crédito, German Credit).
- ✗ Correlação e número de condição não medem a mesma coisa —
  correlação é só alinhamento; número de condição combina alinhamento e
  escala.
- ✗ Existe forma de calcular sem perturbar nada: é exatamente o que esta
  aula ensina, via autovalores de $X^TX$.

### Pausa Ativa 2 (Bloco 2 — Intuição: Autovetores)

**Pergunta motivadora:** se $A\mathbf{v}=-3\mathbf{v}$ para algum
$\mathbf{v}\ne\mathbf{0}$, isso significa que $\mathbf{v}$ não é
autovetor de $A$, já que a direção "inverteu"?

**Discussão:** não. A equação de autovalor $A\mathbf{x}=\lambda\mathbf{x}$
não exige $\lambda>0$ — $\lambda=-3$ é um autovalor perfeitamente válido
(é real). "Não girar" significa que $A\mathbf{v}$ continua sobre a
**mesma reta** que $\mathbf{v}$; o sinal de $\lambda$ só decide se o
sentido sobre essa reta é preservado ($\lambda>0$) ou invertido
($\lambda<0$). O que de fato desqualificaria $\mathbf{v}$ como autovetor
seria $A\mathbf{v}$ apontar para uma reta **diferente** da reta de
$\mathbf{v}$ — isso, sim, seria "girar".

**V/F — Resposta:**
- ✗ $\lambda=-3$ é autovalor válido; a reta é preservada, só o sentido
  inverte — $\mathbf{v}$ continua autovetor.
- ✔ Se todo vetor canônico é autovetor, em particular $\mathbf{e}_1$,
  $\mathbf{e}_2$ são, o que já força $A$ diagonal; exigir o mesmo
  comportamento de escala em toda direção força $A=cI$.
- ✔ Aplicação direta e correta da mesma equação de autovalor a uma
  camada linear de rede neural — mesma matemática, outro domínio de ML.
- ✗ Não-unicidade (múltiplos escalares) não força dimensão $>1$ do
  autoespaço — no exemplo da aula, cada autoespaço de
  $A_{\text{exemplo}}$ tem dimensão $1$ apesar de conter infinitos
  vetores (a reta menos a origem).

### Pausa Ativa 3 (Bloco 3 — Polinômio Característico)

**Pergunta motivadora:** se o polinômio característico de uma matriz
$3\times 3$ tivesse grau 3 mas só uma raiz real, quantos autovalores
reais essa matriz teria?

**Discussão:** exatamente um. O Teorema 4.8 (MathML) conecta autovalor
**real** a raiz **real** do polinômio característico — raízes complexas
não correspondem a autovalores reais da matriz. Uma matriz $n\times n$
real pode, portanto, ter menos de $n$ autovalores reais; o caso extremo
é uma rotação pura em $\mathbb{R}^2$ (ângulo diferente de $0°/180°$),
cujo polinômio característico não tem nenhuma raiz real — nenhuma
direção do plano só estica/encolhe sob uma rotação, todas giram.

**V/F — Resposta:**
- ✔ Leitura correta do Teorema 4.8: só raízes reais do polinômio
  característico contam como autovalor real.
- ✔ Consistente: rotação pura por ângulo $\ne0°,180°$ não tem direção
  que só estique/encolha — toda direção gira, sem autovetor real.
- ✔ Mesma técnica algébrica (polinômio característico), aplicada fora
  de um contexto geométrico, a uma matriz de transição de aprendizado
  por reforço.
- ✗ É o oposto do exemplo da aula: $A-\lambda I$ deu **uma** equação
  independente por autovalor ($x_1=2x_2$, $x_1=-x_2$) — o autoespaço de
  $A_{\text{exemplo}}$ tem dimensão $1$ em cada caso.

### Pausa Ativa 4 (Bloco 4 — Teorema Espectral Real)

**Pergunta motivadora:** o Teorema 4.21 garante autovetores ortogonais
para autovalores distintos. Se um autovalor de uma matriz simétrica
aparece repetido, os autovetores associados a ele nunca podem ser
escolhidos ortogonais entre si?

**Discussão:** não — é o oposto. A demonstração do Bloco 4 só cobre
diretamente o caso de autovalores distintos (usa a ortogonalidade entre
autoespaços diferentes), mas isso é uma limitação da prova apresentada,
não do teorema: dentro de um autoespaço de dimensão $>1$ (autovalor
repetido), sempre é possível escolher uma base ortonormal desse
autoespaço via Gram-Schmidt (MathML, Exemplo 4.8) — a ortogonalidade só
não vem "de graça" nesse caso, precisa ser imposta. O caso extremo deixa
isso bem claro: se $A=3I$, todo vetor não-nulo de $\mathbb{R}^n$ é
autovetor (autovalor $3$ com multiplicidade $n$), e **qualquer** base
ortonormal de $\mathbb{R}^n$ é uma escolha válida de autovetores
ortogonais — a mesma degenerescência aparece na matriz de covariância
de um dataset de ML sempre que dois atributos (ou combinações deles)
têm exatamente a mesma variância: os eixos de PCA correspondentes a
esse autovalor repetido não são unicamente determinados.

**V/F — Resposta:**
- ✗ É o oposto: autovetores do mesmo autoespaço **podem sempre** ser
  escolhidos ortogonais via Gram-Schmidt (MathML Exemplo 4.8) — só não
  vêm ortogonais "de graça" como no caso de autovalores distintos.
- ✔ $A=3I$: $A\mathbf{v}=3\mathbf{v}$ para todo $\mathbf{v}$ — o
  autoespaço único ocupa o espaço inteiro, e qualquer base ortonormal de
  $\mathbb{R}^n$ é, em particular, uma escolha válida de autovetores.
- ✔ Aplicação direta e correta do Teorema 4.21 à matriz de covariância
  de qualquer dataset — a mesma degenerescência de $A=3I$ aparece em PCA
  sempre que duas direções têm exatamente a mesma variância.
- ✗ A conclusão do Teorema 4.21 (diagonalização ortogonal sempre existe)
  vale para **toda** matriz simétrica, distintos ou não; autovalores
  repetidos só mudam a **demonstração** (precisa de Gram-Schmidt dentro
  do autoespaço), não o resultado.

### Pausa Ativa 5 (Bloco 5 — Definitude Positiva)

**Pergunta motivadora:** se $\lambda_{\min}(A)$ estivesse muito próximo
de zero (mas ainda positivo), o que aconteceria com o número de
condição, mesmo $A$ continuando definida positiva?

**Discussão:** o número de condição ficaria muito grande. Como
$\text{cond}(A)=\lambda_{\max}(A)/\lambda_{\min}(A)$, um denominador que
tende a zero (mesmo sem cruzar zero) faz a razão explodir — exatamente
o mecanismo do mal-condicionamento, sem contradizer definitude positiva
($A$ continua com todos os autovalores estritamente positivos, só um
deles muito pequeno). É exatamente o que a Aula 3 observou de forma
empírica no par quase-colinear `AveRooms`/`AveBedrms`, e que o Bloco 6
confirma via autovalores: o menor autovalor de $X^TX$ para esse par
($\approx 1{,}77$) é minúsculo perto do maior ($\approx 742$).

**V/F — Resposta:**
- ✔ Denominador $\to 0^+$ com numerador fixo positivo $\Rightarrow$
  razão $\to\infty$ — mecanismo exato de mal-condicionamento, sem violar
  definitude positiva.
- ✔ $A=cI$ ($c>0$): único autovalor $c$ repetido $\Rightarrow$
  $\lambda_{\max}=\lambda_{\min}=c$ $\Rightarrow$ $\text{cond}(A)=1$, o
  melhor condicionamento possível.
- ✔ Aplicação correta do conceito à otimização de outro modelo de ML
  (Hessiana da perda de uma regressão logística), fora do domínio de
  regressão linear.
- ✗ É uma média **ponderada** pelos pesos $c_i^2$ (componentes de
  $\mathbf{x}$ na base de autovetores), não a média aritmética simples —
  só coincidem se todos os pesos forem iguais.
