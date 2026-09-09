# Gabarito — Aula 4: Autovalores, Autovetores e Matrizes Simétricas

Este arquivo consolida (1) a discussão e a solução V/F das 5 Pausas
Ativas da aula e (2) a justificativa analítica de cada item de
Verdadeiro/Falso da seção Exercícios do `index.qmd`. Nunca publicado no
site (prefixo `_`).

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
  mal-condicionada), outro domínio de engenharia.
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
- ✔ Leitura física padrão de autovalor/autovetor em sistemas lineares —
  modos normais de vibração são autovetores da matriz do sistema.
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
  de um contexto geométrico.
- ✗ É o oposto do exemplo da aula: $A-\lambda I$ deu **uma** equação
  independente por autovalor ($x_1=2x_2$, $x_1=-x_2$) — o autoespaço de
  $A_{\text{exemplo}}$ tem dimensão $1$ em cada caso.

### Pausa Ativa 4 (Bloco 4 — Teorema Espectral Real)

**Pergunta motivadora:** duas matrizes simétricas sempre comutam
($AB=BA$)?

**Discussão:** não, em geral. Duas matrizes simétricas comutam **apenas**
quando compartilham a mesma base de autovetores (são simultaneamente
diagonalizáveis por um mesmo $Q$ ortogonal) — não é uma consequência
automática de "ambas serem simétricas". O caso mais simples que
confirma isso: se $A=Q\Lambda_AQ^T$ e $B=Q\Lambda_BQ^T$ compartilham o
mesmo $Q$, então $AB=Q\Lambda_A\Lambda_BQ^T=Q\Lambda_B\Lambda_AQ^T=BA$
(matrizes diagonais sempre comutam entre si) — mas duas matrizes
simétricas escolhidas ao acaso, cada uma com sua própria base de
autovetores, não têm por que comutar.

**V/F — Resposta:**
- ✗ Falso em geral: comutar exige compartilhar a base de autovetores,
  uma condição extra além de "ambas simétricas".
- ✔ $A=3I$: $A\mathbf{v}=3\mathbf{v}$ para todo $\mathbf{v}$ — o
  autoespaço único ocupa o espaço inteiro, autovalor repetido $n$ vezes.
- ✔ Aplicação direta e correta do Teorema Espectral Real, fora do
  contexto de regressão.
- ✗ É o oposto: autovetores do mesmo autoespaço **podem sempre** ser
  escolhidos ortogonais via Gram-Schmidt (MathML Exemplo 4.8) — só não
  vêm ortogonais "de graça" como no caso de autovalores distintos.

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
- ✔ Aplicação correta do conceito fora do domínio de regressão.
- ✗ É uma média **ponderada** pelos pesos $c_i^2$ (componentes de
  $\mathbf{x}$ na base de autovetores), não a média aritmética simples —
  só coincidem se todos os pesos forem iguais.

---

## Exercícios — Verdadeiro/Falso

### Autovalores e autovetores: a equação básica — item (a)

**Heurística:** Caso limite/extremo ($\lambda=0$)

**Afirmação:** ✔ Se $\mathbf{x}$ é autovetor de $A$ associado ao
autovalor $\lambda=0$, então $\mathbf{x}$ pertence ao núcleo
(espaço-nulo) de $A$, no mesmo sentido definido na Aula 2 para sistemas
homogêneos.

**Resposta:** Verdadeiro

**Justificativa:** $A\mathbf{x}=\lambda\mathbf{x}$ com $\lambda=0$ dá
$A\mathbf{x}=\mathbf{0}$ — exatamente a definição de núcleo/espaço-nulo
de $A$ (Aula 2). O caso-limite $\lambda=0$ conecta diretamente as duas
linguagens: "autovetor de autovalor zero" e "vetor do núcleo" são a
mesma coisa.

### Autovalores e autovetores: a equação básica — item (b)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Uma matriz de rotação pura em $\mathbb{R}^2$ por um
ângulo de $90°$ não tem nenhum autovetor real, porque nenhuma direção
não-nula do plano é mapeada sobre si mesma (nem esticada, nem
invertida) por essa rotação.

**Resposta:** Verdadeiro

**Justificativa:** Uma rotação de $90°$ manda todo vetor não-nulo para
uma direção perpendicular à original — nenhuma reta que passa pela
origem fica invariante. Isso é consistente com o polinômio
característico dessa rotação não ter raiz real (as raízes são
complexas, $\pm i$): o caso extremo em que "não girar" falha para
**toda** direção do espaço.

### Autovalores e autovetores: a equação básica — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Num sistema dinâmico discreto
$\mathbf{x}_{k+1}=A\mathbf{x}_k$, se $\mathbf{x}_0$ for exatamente um
autovetor de $A$ com autovalor $\lambda$, então toda a trajetória
futura $\mathbf{x}_1,\mathbf{x}_2, \dots$ permanece sobre a mesma reta
que $\mathbf{x}_0$, só variando em magnitude por potências de
$\lambda$.

**Resposta:** Verdadeiro

**Justificativa:** Por indução, $\mathbf{x}_k=A^k\mathbf{x}_0$; se
$A\mathbf{x}_0=\lambda\mathbf{x}_0$, então
$A^k\mathbf{x}_0=\lambda^k\mathbf{x}_0$ (aplicar $A$ repetidamente só
multiplica pelo mesmo escalar cada vez). A trajetória inteira fica sobre
a reta gerada por $\mathbf{x}_0$ — aplicação direta da definição de
autovetor a um domínio (sistemas dinâmicos) não discutido na aula.

### Autovalores e autovetores: a equação básica — item (d)

**Heurística:** Falsa dicotomia/falsa equivalência

**Afirmação:** ✗ Como o autovetor associado a um autovalor não é único,
a equação de autovalor $A\mathbf{x}=\lambda\mathbf{x}$ admite, para
qualquer $A$ e qualquer $\lambda$ real, pelo menos um autovetor
não-nulo que a satisfaça.

**Resposta:** Falso

**Justificativa:** A não-unicidade (Bloco 2) só vale **depois** de já
existir um autovetor para aquele $\lambda$ — qualquer múltiplo escalar
dele também serve. Isso não implica que **todo** $\lambda$ real seja
autovalor de $A$: só os $\lambda$ que são raízes do polinômio
característico $p_A(\lambda)$ (Bloco 3) têm autovetor associado. O erro
é confundir "quando existe um autovetor, existem infinitos" com "sempre
existe um autovetor".

### O polinômio característico — item (a)

**Heurística:** Cenário contrafactual

**Afirmação:** ✗ Se o polinômio característico de uma matriz
$A\in\mathbb{R}^{2 \times 2}$ tiver uma raiz **dupla** (discriminante
zero em Bhaskara), isso garante automaticamente que $A$ tem apenas um
autovetor linearmente independente associado a essa raiz.

**Resposta:** Falso

**Justificativa:** Contraexemplo direto: $A=2I$ tem polinômio
característico $(\lambda-2)^2$ (raiz dupla $\lambda=2$), mas **todo**
vetor não-nulo de $\mathbb{R}^2$ é autovetor — o autoespaço $E_2$ tem
dimensão $2$, não $1$. Raiz dupla (multiplicidade algébrica 2) não
força multiplicidade geométrica 1; a relação entre as duas
multiplicidades é só "geométrica $\le$ algébrica", nunca uma implicação
automática de igualdade.

### O polinômio característico — item (b)

**Heurística:** Cenário contrafactual

**Afirmação:** ✔ Multiplicar uma matriz $A$ inteira por um escalar
$c\ne 0$ (obtendo $cA$) preserva exatamente os mesmos autovetores de
$A$, mas multiplica cada autovalor por $c$.

**Resposta:** Verdadeiro

**Justificativa:** Se $A\mathbf{x}=\lambda\mathbf{x}$, então
$(cA)\mathbf{x}=c(A\mathbf{x})=c(\lambda\mathbf{x})=(c\lambda)\mathbf{x}$
— o mesmo $\mathbf{x}$ resolve a equação de autovalor de $cA$, com
autovalor $c\lambda$. Alterar a matriz por um cenário contrafactual
(escalá-la inteira) preserva a direção especial, só reescala o fator de
esticamento.

### O polinômio característico — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Num modelo de epidemiologia descrito por uma matriz de
transição de estados $3\times 3$, encontrar os autovalores dessa matriz
via seu polinômio característico (grau 3) é uma aplicação legítima da
mesma técnica usada nesta aula para matrizes $2\times 2$.

**Resposta:** Verdadeiro

**Justificativa:** O Teorema 4.8 (autovalor $\iff$ raiz do polinômio
característico) não depende da origem da matriz — vale para qualquer
$A\in\mathbb{R}^{n\times n}$, incluindo matrizes de transição de
epidemiologia, ecologia ou qualquer outro domínio. A técnica generaliza
diretamente para grau 3 (só fica algebricamente mais trabalhosa).

### O polinômio característico — item (d)

**Heurística:** Falsa dicotomia/falsa equivalência

**Afirmação:** ✗ Como $\det(A-\lambda I)=0$ é a condição para autovalor,
isso implica que $\det(A)=0$ é condição necessária para que $A$ tenha
algum autovalor real.

**Resposta:** Falso

**Justificativa:** $\det(A)=0$ é a condição para que $\lambda=0$
especificamente seja autovalor de $A$ (basta substituir $\lambda=0$ em
$\det(A-\lambda I)$). Não é necessária para a existência de **algum**
autovalor real — contraexemplo: $A=2I$ tem autovalor real $\lambda=2$
(múltiplas vezes), mas $\det(A)=4\ne 0$. O erro é generalizar uma
condição específica ($\lambda=0$) para todo o conjunto de autovalores.

### Não-unicidade e autoespaços — item (a)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Se dois autovetores distintos, $\mathbf{x}_1$ e
$\mathbf{x}_2$, de uma mesma matriz $A$ (não necessariamente simétrica)
estiverem associados ao **mesmo** autovalor $\lambda$, então qualquer
combinação linear não-nula $c_1\mathbf{x}_1+c_2\mathbf{x}_2$ também é
autovetor de $A$ com esse mesmo autovalor $\lambda$.

**Resposta:** Verdadeiro

**Justificativa:**
$A(c_1\mathbf{x}_1+c_2\mathbf{x}_2)=c_1A\mathbf{x}_1+c_2A\mathbf{x}_2=
c_1\lambda\mathbf{x}_1+c_2\lambda\mathbf{x}_2=\lambda(c_1\mathbf{x}_1+
c_2\mathbf{x}_2)$ — o autoespaço $E_\lambda$ é, por construção, um
subespaço (fechado sob combinação linear, Aula 1), propriedade que vale
para **qualquer** matriz, simétrica ou não; a simetria só entra quando
se compara autoespaços de autovalores **diferentes** (Bloco 4).

### Não-unicidade e autoespaços — item (b)

**Heurística:** Caso limite/extremo

**Afirmação:** ✗ Se uma matriz $A\in\mathbb{R}^{2\times 2}$ tivesse dois
autovalores distintos, mas um deles com autoespaço de dimensão $2$,
isso seria matematicamente possível para essa matriz.

**Resposta:** Falso

**Justificativa:** Se um autoespaço já tem dimensão $2$ dentro de
$\mathbb{R}^2$, ele ocupa o espaço inteiro — não sobra nenhuma direção
independente para um segundo autovalor **distinto** ter autovetor
próprio (autoespaços de autovalores distintos são sempre linearmente
independentes entre si). O caso extremo (dimensão do autoespaço igual à
dimensão do espaço todo) já esgota a matriz: ela só pode ser $A=cI$,
sem espaço para um segundo autovalor diferente de $c$.

### Não-unicidade e autoespaços — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Num problema de classificação de imagens em que cada
"direção" do espaço de atributos representasse uma característica
visual, um autoespaço de dimensão maior que $1$ significaria, na
prática, que existe mais de uma direção de atributos igualmente
"especial" (mesmo fator de escala) para a transformação em questão.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente a leitura correta de "autoespaço de
dimensão $>1$": não uma única direção especial, mas um subespaço
inteiro de direções que compartilham o mesmo autovalor (mesmo fator de
escala) — aplicação direta e correta do conceito a um domínio (visão
computacional) fora do fio condutor da aula.

### Não-unicidade e autoespaços — item (d)

**Heurística:** Falsa dicotomia/falsa equivalência

**Afirmação:** ✗ Como o vetor nulo nunca é considerado autovetor por
definição, isso implica que um autoespaço $E_\lambda$ nunca contém o
vetor $\mathbf{0}$.

**Resposta:** Falso

**Justificativa:** A Definição 4.6 exclui $\mathbf{0}$ da lista de
vetores que podem ser **chamados** de autovetor, mas o autoespaço
$E_\lambda=\{\mathbf{x}:A\mathbf{x}=\lambda\mathbf{x}\}$ é, por
construção, um subespaço vetorial — e todo subespaço contém
$\mathbf{0}$ (Aula 1). $\mathbf{0}$ pertence a $E_\lambda$ mesmo sem ser
chamado de "autovetor"; a confusão é entre o conjunto (subespaço, que
inclui $\mathbf{0}$) e o rótulo aplicado a seus elementos não-nulos.

### Teorema Espectral Real — item (a)

**Heurística:** Cenário contrafactual

**Afirmação:** ✔ Se duas matrizes simétricas $A$ e $B$ compartilhassem
exatamente a mesma base ortonormal de autovetores (mesmo $Q$ na
decomposição espectral, com $\Lambda$ possivelmente diferentes), então
$A$ e $B$ comutariam, ou seja, $AB=BA$.

**Resposta:** Verdadeiro

**Justificativa:** Com $A=Q\Lambda_AQ^T$ e $B=Q\Lambda_BQ^T$ (mesmo
$Q$), $AB=Q\Lambda_AQ^TQ\Lambda_BQ^T=Q\Lambda_A\Lambda_BQ^T$ (usando
$Q^TQ=I$); como $\Lambda_A$ e $\Lambda_B$ são diagonais, sempre comutam
entre si ($\Lambda_A\Lambda_B=\Lambda_B\Lambda_A$), logo $AB=
Q\Lambda_B\Lambda_AQ^T=BA$. Compartilhar a base é a condição extra que
falta no caso geral (ver Pausa Ativa 4).

### Teorema Espectral Real — item (b)

**Heurística:** Falsa dicotomia/falsa equivalência

**Afirmação:** ✗ O Teorema Espectral Real garante que toda matriz
simétrica $A\in\mathbb{R}^{n\times n}$ tem exatamente $n$ autovalores
**distintos** entre si.

**Resposta:** Falso

**Justificativa:** O Teorema 4.15/Teorema Espectral garante $n$
autovalores **reais** (contados com multiplicidade) e uma base
ortonormal de autovetores — não distinção entre eles. Contraexemplo
direto: $A=3I$ é simétrica e tem um único valor de autovalor ($3$),
repetido $n$ vezes; o teorema continua valendo (base ortonormal existe,
qualquer base ortonormal de $\mathbb{R}^n$ serve), só que sem
autovalores distintos.

### Teorema Espectral Real — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Numa rede elétrica descrita por uma matriz de
admitância simétrica, o Teorema Espectral Real garante autovalores
reais e autovetores ortogonais, ainda que o contexto físico não tenha
nenhuma relação com regressão ou projeção.

**Resposta:** Verdadeiro

**Justificativa:** O Teorema 4.15 é um resultado puramente algébrico
sobre matrizes simétricas — não depende de a matriz vir de regressão,
projeção, ou qualquer contexto específico. Qualquer matriz de admitância
simétrica (comum em análise de redes elétricas) herda a mesma garantia.

### Teorema Espectral Real — item (d)

**Heurística:** Cenário contrafactual

**Afirmação:** ✔ Se uma matriz $A$ tivesse autovalores reais, mas seus
autovetores associados a autovalores distintos não fossem ortogonais
entre si, isso seria suficiente para concluir que $A$ não é simétrica.

**Resposta:** Verdadeiro

**Justificativa:** É a contrapositiva exata da prova do Bloco 4: "$A$
simétrica $\Rightarrow$ autovetores de autovalores distintos
ortogonais" equivale logicamente a "autovetores de autovalores
distintos não ortogonais $\Rightarrow$ $A$ não simétrica". Ter
autovalores reais não basta — a prova usou a simetria especificamente
para forçar a ortogonalidade; sem ela, nada garante o ângulo reto.

### Definitude positiva — item (a)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Se uma matriz simétrica $A\in\mathbb{R}^{n\times n}$
tiver exatamente um autovalor igual a zero e todos os demais
estritamente positivos, então $A$ é semidefinida positiva, mas não
definida positiva.

**Resposta:** Verdadeiro

**Justificativa:** $A\succeq 0$ exige $\lambda_i\ge 0$ para todo $i$ —
satisfeito (zero conta). $A\succ 0$ exige $\lambda_i>0$ estrito para
todo $i$ — falha exatamente no autovalor zero. É o caso-limite entre as
duas categorias, a fronteira exata entre "semidefinida" e "definida".

### Definitude positiva — item (b)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ A soma de duas matrizes simétricas definidas positivas
de mesma dimensão, $A+B$, é sempre definida positiva.

**Resposta:** Verdadeiro

**Justificativa:** Para $\mathbf{x}\ne\mathbf{0}$:
$\mathbf{x}^T(A+B)\mathbf{x}=\mathbf{x}^TA\mathbf{x}+\mathbf{x}^TB
\mathbf{x}>0+0=0$, na verdade $>0+>0>0$ (ambas as parcelas
estritamente positivas) — a soma de dois positivos é positiva.
Aplicação direta da Definição 3.4 a uma operação (soma de matrizes) não
discutida explicitamente na aula.

### Definitude positiva — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Num problema de otimização de portfólio financeiro, se
a matriz de covariância dos retornos dos ativos não fosse definida
positiva (algum autovalor exatamente zero), isso indicaria a existência
de uma combinação de ativos com variância nula — um portfólio livre de
risco a partir de ativos individualmente arriscados.

**Resposta:** Verdadeiro

**Justificativa:** Se $\Sigma$ (covariância) tem autovalor $0$ com
autovetor $\mathbf{v}$, então $\mathbf{v}^T\Sigma\mathbf{v}=0$ — a
"variância" de um portfólio com pesos proporcionais a $\mathbf{v}$ é
exatamente zero, mesmo que cada ativo individual tenha variância
positiva. Aplicação correta e não-trivial do conceito de definitude a
um domínio financeiro.

### Definitude positiva — item (d)

**Heurística:** Falsa dicotomia/falsa equivalência

**Afirmação:** ✔ Como a forma quadrática $\mathbf{x}^TA\mathbf{x}$ de
uma matriz definida positiva nunca é negativa, isso implica que
$\mathbf{x}^TA\mathbf{x}=0$ é impossível para $A$ definida positiva e
$\mathbf{x}$ não-nulo qualquer.

**Resposta:** Verdadeiro

**Justificativa:** A Definição 3.4 já exige $\mathbf{x}^TA\mathbf{x}>0$
estritamente (não só $\ge 0$) para toda matriz **definida** positiva —
diferente de **semidefinida**, em que $\mathbf{x}^TA\mathbf{x}=0$ é
permitido para algum $\mathbf{x}\ne\mathbf{0}$. A armadilha do item é a
premissa "nunca é negativa" soar como só $\ge 0$ (o caso semidefinido);
mas a hipótese explícita é "definida positiva", que já garante
positividade estrita, tornando $=0$ de fato impossível para
$\mathbf{x}\ne\mathbf{0}$.

### Quociente de Rayleigh e número de condição — item (a)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Se $\mathbf{x}$ for exatamente um autovetor de $A$
associado ao autovalor $\lambda_{\max}(A)$, então o quociente de
Rayleigh $\mathbf{x}^TA\mathbf{x}/\mathbf{x}^T\mathbf{x}$ avaliado
nesse $\mathbf{x}$ é exatamente igual a $\lambda_{\max}(A)$.

**Resposta:** Verdadeiro

**Justificativa:** $A\mathbf{x}=\lambda_{\max}\mathbf{x}$
$\Rightarrow$ $\mathbf{x}^TA\mathbf{x}=\lambda_{\max}\mathbf{x}^T
\mathbf{x}$ $\Rightarrow$ o quociente vale exatamente
$\lambda_{\max}$ — o caso-limite em que o supremo do quociente de
Rayleigh (Boyd) é de fato **atingido**, não só aproximado.

### Quociente de Rayleigh e número de condição — item (b)

**Heurística:** Cenário contrafactual

**Afirmação:** ✗ Se todos os autovalores de uma matriz simétrica
definida positiva $A$ dobrarem de valor (cada $\lambda_i\to
2\lambda_i$), o número de condição de $A$ também dobra.

**Resposta:** Falso

**Justificativa:** $\text{cond}(A)=\lambda_{\max}(A)/\lambda_{\min}(A)$;
dobrando todos os autovalores, o novo número de condição é
$\frac{2\lambda_{\max}}{2\lambda_{\min}}=\frac{\lambda_{\max}}
{\lambda_{\min}}$ — **exatamente o mesmo** de antes, porque o fator $2$
cancela na razão. O número de condição depende só da **razão** entre
extremos, não da escala absoluta dos autovalores.

### Quociente de Rayleigh e número de condição — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Num sistema de equações normais mal-condicionado por
causa de dois sensores redundantes (quase a mesma leitura), remover
fisicamente um dos dois sensores tende a aumentar o menor autovalor
relativo de $X^TX$ e, com isso, reduzir o número de condição.

**Resposta:** Verdadeiro

**Justificativa:** A direção quase-degenerada (menor autovalor) vem
exatamente de duas colunas quase-redundantes competindo pela mesma
informação (o mesmo mecanismo do par `AveRooms`/`AveBedrms`, Bloco 6);
removendo uma delas, a matriz de design perde a coluna que causava a
quase-dependência, e o menor autovalor da nova $X^TX$ (menor,
dimensão reduzida) tende a não ser mais espremido perto de zero —
melhorando o condicionamento.

### Quociente de Rayleigh e número de condição — item (d)

**Heurística:** Falsa dicotomia/falsa equivalência

**Afirmação:** ✗ Como o número de condição de uma matriz simétrica
definida positiva é sempre maior ou igual a $1$, isso implica que
qualquer matriz com número de condição exatamente igual a $1$ tem que
ser, necessariamente, a matriz identidade.

**Resposta:** Falso

**Justificativa:** $\text{cond}(A)=1$ significa $\lambda_{\max}(A)=
\lambda_{\min}(A)$, ou seja, **todos** os autovalores iguais entre si —
isso força $A=cI$ para **algum** escalar $c>0$, não necessariamente
$c=1$. Contraexemplo: $A=5I$ tem $\text{cond}(A)=5/5=1$, mas
$A\ne I$.

### $X^TX$: simetria e as duas faces desta aula — item (a)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Se duas colunas de uma matriz de design $X$ fossem
exatamente ortogonais entre si (produto interno zero) e tivessem a
mesma norma, a submatriz $2\times 2$ correspondente de $X^TX$ restrita
a essas duas colunas seria um múltiplo escalar da identidade, com
número de condição igual a $1$.

**Resposta:** Verdadeiro

**Justificativa:** Com colunas $\mathbf{x}_1,\mathbf{x}_2$ ortogonais
($\mathbf{x}_1^T\mathbf{x}_2=0$) e mesma norma $r$
($\mathbf{x}_1^T\mathbf{x}_1=\mathbf{x}_2^T\mathbf{x}_2=r^2$), a
submatriz $2\times 2$ de $X^TX$ é
$\begin{bmatrix}r^2&0\\0&r^2\end{bmatrix}=r^2I$ — múltiplo escalar da
identidade, com os dois autovalores iguais a $r^2$, logo
$\text{cond}=1$. O caso-limite ideal de condicionamento.

### $X^TX$: simetria e as duas faces desta aula — item (b)

**Heurística:** Falsa dicotomia/falsa equivalência

**Afirmação:** ✗ Para qualquer matriz retangular
$X\in\mathbb{R}^{N\times d}$ com $N\ne d$, a própria matriz $X$ (não
$X^TX$) sempre tem $\min(N,d)$ autovalores reais, pela mesma lógica do
polinômio característico aplicada a $X^TX$.

**Resposta:** Falso

**Justificativa:** Autovalores só são definidos para matrizes
**quadradas** — o polinômio característico $\det(X-\lambda I)$ nem faz
sentido dimensionalmente para $X$ retangular ($N\ne d$). O que $X$
retangular **tem** são $\min(N,d)$ **valores singulares** (via SVD,
Aula 5) — uma noção relacionada, mas distinta de autovalor. É
exatamente a lacuna anunciada no Fechamento desta aula: autovalores
exigem quadrada (e idealmente simétrica); $X$ retangular precisa de
outra ferramenta.

### $X^TX$: simetria e as duas faces desta aula — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Numa matriz de covariância genética (relacionando a
expressão de vários genes numa amostra de pacientes), o mesmo
raciocínio de autovalor pequeno $\Rightarrow$ direção quase redundante
entre variáveis se aplicaria, ainda que o domínio seja biológico, não
imobiliário.

**Resposta:** Verdadeiro

**Justificativa:** O raciocínio do Bloco 6 (autovalor pequeno de uma
matriz de covariância $\Rightarrow$ direção quase degenerada, variáveis
quase redundantes) é uma consequência puramente algébrica do Teorema
Espectral e do quociente de Rayleigh — não depende de os dados serem
imobiliários, genéticos, ou de qualquer outro domínio.

### $X^TX$: simetria e as duas faces desta aula — item (d)

**Heurística:** Falsa dicotomia/falsa equivalência

**Afirmação:** ✗ Como $X^TX$ é sempre simétrica semidefinida positiva
(independentemente do posto de $X$), isso implica que $X^TX$ é sempre
invertível, qualquer que seja $X$.

**Resposta:** Falso

**Justificativa:** Semidefinida positiva ($\lambda_i\ge 0$) não implica
invertível — invertibilidade exige **definida** positiva
($\lambda_i>0$ estrito para todo $i$), que só vale quando $X$ tem posto
completo (Teorema 4.14, MathML). O contraexemplo já apareceu na Aula 3:
a coluna duplicada ($2\times$`AveRooms`) deixa $X^TX$ singular
($\det=0$), mesmo continuando semidefinida positiva.

### Covariância empírica e a semente de PCA — item (a)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Se a matriz de covariância empírica de dois atributos
tiver um dos autovalores muito próximo de zero, isso indica que os
dados, nesse par de atributos, estão quase inteiramente concentrados ao
longo de uma única direção no plano.

**Resposta:** Verdadeiro

**Justificativa:** Um autovalor da covariância mede a variância dos
dados **projetados** na direção do autovetor correspondente (Bloco 6);
se um autovalor é quase zero, a variância nessa direção é quase nula —
os pontos quase não se espalham ali, ficando concentrados ao longo da
direção do outro autovetor (o de autovalor grande). O caso-limite exato
é uma reta perfeita (autovalor menor exatamente zero).

### Covariância empírica e a semente de PCA — item (b)

**Heurística:** Cenário contrafactual

**Afirmação:** ✗ Padronizar cada atributo (subtrair a média, dividir
pelo desvio-padrão) antes de calcular a covariância nunca muda a
**direção** do autovetor principal, só a magnitude do autovalor
associado.

**Resposta:** Falso

**Justificativa:** É exatamente o oposto do aviso do Bloco 6: dividir
cada coluna pelo próprio desvio-padrão muda a escala **relativa** entre
as colunas, e a direção de maior variância (o autovetor principal)
depende dessa escala relativa. No exemplo dos 4 atributos, a
covariância bruta tem autovetor principal dominado por `HouseAge`
(maior variância numérica bruta); padronizando, essa dominância deixa
de existir e a direção principal passa a refletir a estrutura de
correlação real entre os atributos, não a escala de cada um — a
direção pode, sim, mudar.

### Covariância empírica e a semente de PCA — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Num conjunto de dados de sensores industriais com
escalas físicas muito diferentes entre si (ex.: temperatura em graus
Celsius e pressão em milhares de Pascals), calcular a covariância bruta
(sem padronizar) tende a produzir um autovetor principal dominado pelo
sensor de maior variância numérica, não necessariamente o fisicamente
mais relevante.

**Resposta:** Verdadeiro

**Justificativa:** Mesmo mecanismo do aviso do Bloco 6 (`HouseAge`
dominando a covariância bruta dos 4 atributos), transposto para
sensores industriais: a escala numérica bruta (não a relevância física)
decide qual sensor domina a direção principal, quando a covariância não
é calculada sobre dados padronizados.

### Covariância empírica e a semente de PCA — item (d)

**Heurística:** Falsa dicotomia/falsa equivalência

**Afirmação:** ✗ Como a matriz de covariância é sempre semidefinida
positiva, isso implica que a soma das variâncias de todos os atributos
(o traço da matriz) é sempre igual à soma dos quadrados das
covariâncias fora da diagonal.

**Resposta:** Falso

**Justificativa:** Não existe identidade geral desse tipo. O traço de
uma matriz de covariância é a soma das variâncias (que, pelo Teorema
Espectral, também é igual à soma dos **autovalores**) — uma quantidade
sem relação algébrica direta e geral com a soma dos quadrados das
entradas fora da diagonal. Semidefinida positiva garante autovalores
não-negativos, não nenhuma identidade entre traço e covariâncias
cruzadas; a afirmação combina dois fatos verdadeiros isolados (matriz
PSD, traço existe) numa conclusão que não decorre deles.
