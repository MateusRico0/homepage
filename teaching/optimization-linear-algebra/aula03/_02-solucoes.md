# Soluções — Questões de Verdadeiro/Falso (Aula 3)

> Arquivo de apoio, não publicado (prefixo `_`). Contém a resposta e a
> justificativa de cada item das 12 questões de V/F do `index.qmd`
> (48 itens, 12 blocos de 4). O `index.qmd` publicado continua sem
> solução — este arquivo existe só para conferência do professor/monitor,
> seguindo a metodologia de heurísticas (contrafactual, limite,
> transferência de domínio, falsa dicotomia) definida em `../../CLAUDE.md`.
> Dentro de cada bloco, os itens seguem a ordem fixa
> (a) contrafactual, (b) caso-limite, (c) transferência de domínio,
> (d) falsa dicotomia — usada consistentemente na construção dos 48
> itens desta aula.

---

### Sistemas sobredeterminados e a melhor aproximação — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se um sistema $A\mathbf{x}=\mathbf{b}$ fosse
subdeterminado ($n>m$) em vez de sobredeterminado, ainda haveria um
sentido útil para "melhor aproximação" via projeção, mas ele coincidiria
trivialmente com uma das infinitas soluções exatas, não com um ponto
fora do espaço-coluna de $A$.

**Resposta:** Verdadeiro

**Justificativa:** No regime subdeterminado, se o sistema for solúvel,
$\mathbf{b}$ já está no espaço-coluna de $A$ — logo a "melhor
aproximação" (a projeção de $\mathbf{b}$ sobre esse espaço) é
$\mathbf{b}$ mesmo, uma das infinitas soluções exatas existentes. A
mecânica de "minimizar distância a um ponto fora do subespaço" (o cerne
do Bloco 4) só é não-trivial no regime sobredeterminado, que é o caso
desta aula.

### Sistemas sobredeterminados e a melhor aproximação — item (b)

**Heurística:** Caso limite

**Afirmação:** ✔ No caso-limite em que $\mathbf{y}$ está exatamente
sobre o espaço-coluna de $X$, a "melhor aproximação"
$\hat{\mathbf{y}}=X\hat{\mathbf{w}}$ coincide com $\mathbf{y}$, e o
problema de mínimos quadrados se reduz ao caso já resolvido pela Aula 2
(sistema com solução exata).

**Resposta:** Verdadeiro

**Justificativa:** Se $\mathbf{y}\in\text{col}(X)$, o ponto de
$\text{col}(X)$ mais próximo de $\mathbf{y}$ é o próprio $\mathbf{y}$
(distância zero) — o caso extremo em que a projeção é trivial e o
sistema $X\mathbf{w}=\mathbf{y}$ tem solução exata, exatamente o
critério de posto da Aula 2.

### Sistemas sobredeterminados e a melhor aproximação — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Num problema de previsão de demanda de energia
elétrica, com muito mais medições horárias (equações) do que parâmetros
do modelo físico a estimar (incógnitas), a mesma lógica de "sistema
sobredeterminado sem solução exata, resolvido por projeção" se
aplicaria.

**Resposta:** Verdadeiro

**Justificativa:** A mecânica de projeção ortogonal não depende do
domínio dos dados — só da estrutura $N\gg d$ (mais equações que
incógnitas). Qualquer sistema sobredeterminado, seja de preços de
imóveis ou de demanda de energia, é resolvido pela mesma matemática do
Bloco 4.

### Sistemas sobredeterminados e a melhor aproximação — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como um sistema sobredeterminado não tem solução
exata, isso implica que qualquer $\mathbf{w}$ escolhido produzirá um
erro de magnitude semelhante — a escolha de $\mathbf{w}$ não afetaria
significativamente a qualidade da aproximação.

**Resposta:** Falso

**Justificativa:** A ausência de solução exata não torna a escolha de
$\mathbf{w}$ irrelevante — pelo contrário, é exatamente por isso que
existe uma noção precisa de "melhor" $\mathbf{w}$ (o que minimiza
$\|\mathbf{y}-X\mathbf{w}\|$), e $\mathbf{w}$'s distantes desse ótimo
produzem erros muito maiores, como visto no contraste entre o
$\mathbf{w}$ inventado da Aula 2 e o $\hat{\mathbf{w}}$ ajustado desta
aula.

---

### A intuição da sombra — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se a fonte de luz da analogia da sombra viesse de um
ângulo oblíquo fixo (não perpendicular ao subespaço), o ponto de
chegada no subespaço, em geral, não seria mais o ponto mais próximo do
ponto original.

**Resposta:** Verdadeiro

**Justificativa:** Só a projeção perpendicular minimiza a distância —
é a mesma geometria do Teorema de Pitágoras: a hipotenusa de um
triângulo formado por um ângulo oblíquo é maior do que o cateto
perpendicular. Uma luz oblíqua fixa produz, em geral, um ponto de
chegada mais distante de $\mathbf{y}$ do que a projeção ortogonal.

### A intuição da sombra — item (b)

**Heurística:** Caso limite

**Afirmação:** ✔ No caso-limite em que o subespaço $U$ tem a mesma
dimensão do espaço ambiente ($U=V$), a "sombra" de qualquer ponto sobre
$U$ coincide com o próprio ponto, para qualquer ponto escolhido.

**Resposta:** Verdadeiro

**Justificativa:** Se $U=V$, todo ponto do espaço já pertence a $U$;
logo sua "sombra" (o ponto de $U$ mais próximo dele mesmo) é ele
próprio, com resíduo nulo — não há nada fora de $U$ para projetar.

### A intuição da sombra — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ A ideia de reduzir a dimensionalidade de dados de alta
dimensão para visualização (ex.: reduzir atributos de um dataset para 2
dimensões e plotar um gráfico de dispersão) usa, na essência, a mesma
operação geométrica de projeção perpendicular discutida nesta aula.

**Resposta:** Verdadeiro

**Justificativa:** Técnicas de redução de dimensionalidade (como PCA,
mencionada no MathML como aplicação de projeções ortogonais) projetam
vetores de alta dimensão sobre um subespaço de menor dimensão que
retém o máximo de informação — a mesma operação geométrica da "sombra",
com o subespaço escolhido de forma a minimizar a perda de informação em
agregado, não só para um único vetor.

### A intuição da sombra — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como a projeção perpendicular minimiza a distância ao
subespaço, ela produz sempre o ponto de menor norma dentro do
subespaço, entre todos os candidatos.

**Resposta:** Falso

**Justificativa:** Minimizar a distância até $\mathbf{y}$ e minimizar a
norma do próprio ponto do subespaço são critérios completamente
independentes. A projeção $\hat{\mathbf{y}}$ pode ter norma grande ou
pequena, dependendo de onde $\mathbf{y}$ está — o único critério que
importa é a proximidade a $\mathbf{y}$, não o tamanho do ponto
escolhido.

---

### Subespaços e o complemento ortogonal — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se $U$ e $W$ são dois subespaços distintos de mesma
dimensão $M$ dentro de um espaço $V$ de dimensão $D$, seus complementos
ortogonais $U^\perp$ e $W^\perp$ têm, necessariamente, a mesma dimensão
entre si ($D-M$), ainda que $U^\perp \ne W^\perp$ como conjuntos.

**Resposta:** Verdadeiro

**Justificativa:** A fórmula $\dim(U^\perp)=D-\dim(U)$ depende só da
dimensão de $U$ e do espaço ambiente, não de qual subespaço específico
$U$ é. Dois subespaços diferentes de mesma dimensão $M$ têm
complementos ortogonais de mesma dimensão $D-M$, mesmo sendo conjuntos
distintos (a menos que $U=W$).

### Subespaços e o complemento ortogonal — item (b)

**Heurística:** Caso limite

**Afirmação:** ✔ No caso-limite $M=D$ (o subespaço é o espaço inteiro),
o complemento ortogonal se reduz ao subespaço trivial $\{\mathbf{0}\}$.

**Resposta:** Verdadeiro

**Justificativa:** Se $U=V$ (dimensão $M=D$), o único vetor ortogonal a
todo vetor de $V$ é o próprio vetor nulo — logo $U^\perp=\{\mathbf{0}\}$,
de dimensão $D-M=0$, consistente com a fórmula geral.

### Subespaços e o complemento ortogonal — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Em processamento de sinais, decompor um sinal de
áudio em uma componente dentro de uma banda de frequência específica
(um subespaço) e uma componente fora dela usa a mesma lógica de
decomposição única $V=U\oplus U^\perp$ discutida nesta aula.

**Resposta:** Verdadeiro

**Justificativa:** Qualquer decomposição ortogonal de um espaço em
"dentro de uma banda" e "fora dessa banda" segue exatamente a estrutura
$V=U\oplus U^\perp$: união disjunta (a menos do vetor nulo) e soma que
recompõe o sinal original de forma única.

### Subespaços e o complemento ortogonal — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como todo vetor de $V$ se decompõe de forma única em
$U\oplus U^\perp$, isso implica que essa decomposição é a única forma
possível de escrever qualquer vetor de $V$ como soma de dois vetores de
$V$.

**Resposta:** Falso

**Justificativa:** A unicidade é específica da decomposição em $U$ e
seu complemento ortogonal $U^\perp$ — não da decomposição em
**quaisquer** dois vetores de $V$ que somem o vetor original. Existem
infinitas formas de escrever um vetor como soma de dois vetores
arbitrários de $V$ (basta escolher um deles livremente e o outro como
a diferença); só a decomposição $U\oplus U^\perp$ específica é única.

---

### Definição formal de projeção — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se $\pi:V\to U$ satisfaz $\pi^2=\pi$, então, para
qualquer vetor $\mathbf{u}$ que já pertença a $U$, necessariamente
$\pi(\mathbf{u}) = \mathbf{u}$.

**Resposta:** Verdadeiro

**Justificativa:** Como $\pi$ mapeia $V$ sobre $U$ (é sobrejetora em
$U$), todo $\mathbf{u}\in U$ é da forma $\mathbf{u}=\pi(\mathbf{v})$
para algum $\mathbf{v}\in V$. Aplicando $\pi$ novamente:
$\pi(\mathbf{u})=\pi(\pi(\mathbf{v}))=\pi^2(\mathbf{v})=\pi(\mathbf{v})=\mathbf{u}$,
usando exatamente a propriedade $\pi^2=\pi$ da Definição 3.10.

### Definição formal de projeção — item (b)

**Heurística:** Caso limite

**Afirmação:** ✔ No caso-limite em que a matriz de projeção $P_\pi$ é
a matriz identidade, o subespaço $U$ sobre o qual ela projeta é o
espaço ambiente $V$ inteiro.

**Resposta:** Verdadeiro

**Justificativa:** $P_\pi=I$ significa que $P_\pi\mathbf{x}=\mathbf{x}$
para todo $\mathbf{x}$ — ou seja, todo vetor já é sua própria projeção,
o que só ocorre quando o subespaço de projeção é o espaço inteiro
($U=V$), como no item (b) do bloco anterior.

### Definição formal de projeção — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Num sistema de compressão de vídeo que descarta
certas componentes de frequência (mantendo só um subconjunto), a
operação de manter as componentes retidas e descartar as demais pode
ser descrita, de forma exata, por uma matriz de projeção $P_\pi$ com
$P_\pi^2=P_\pi$.

**Resposta:** Verdadeiro

**Justificativa:** "Manter algumas componentes e zerar as demais" é
exatamente a definição de uma projeção sobre o subespaço gerado pelas
componentes retidas — aplicar essa operação duas vezes dá o mesmo
resultado que aplicá-la uma vez ($\pi^2=\pi$), a assinatura algébrica
de toda projeção.

### Definição formal de projeção — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como toda matriz de projeção satisfaz
$P_\pi^2=P_\pi$, isso significa que qualquer matriz quadrada que
satisfaça essa condição algébrica também é, necessariamente, simétrica.

**Resposta:** Falso

**Justificativa:** Idempotência ($P^2=P$) e simetria são propriedades
independentes. Existem projeções **oblíquas** — idempotentes, mas não
simétricas — que projetam sobre um subespaço numa direção diferente da
perpendicular. Só as projeções **ortogonais** (as desta aula, definidas
via produto interno) são necessariamente simétricas; a definição geral
de projeção (Definição 3.10, $\pi^2=\pi$) não exige isso.

---

### Derivação das Equações Normais — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se a condição de ortogonalidade fosse verificada
apenas para algumas colunas de $X$ (não todas), em vez de todas as $d$
colunas, isso não seria suficiente, em geral, para garantir que o
resíduo é ortogonal a todo o espaço-coluna de $X$.

**Resposta:** Verdadeiro

**Justificativa:** O Passo (iii) do Bloco 4 argumenta que basta checar
a ortogonalidade coluna a coluna porque **toda** combinação linear das
colunas herda a ortogonalidade — mas isso exige que a ortogonalidade
valha para uma base completa de $\text{col}(X)$ (todas as $d$ colunas,
se forem linearmente independentes). Checar só um subconjunto deixaria
direções de $\text{col}(X)$ sem garantia de ortogonalidade.

### Derivação das Equações Normais — item (b)

**Heurística:** Caso limite

**Afirmação:** ✔ No caso-limite $d=1$ (uma única coluna, isto é, $X$ é
um vetor-coluna $\mathbf{x}\in\mathbb{R}^N$), as Equações Normais
$X^TX\hat{\mathbf{w}}=X^T\mathbf{y}$ se reduzem a uma única equação
escalar, $\hat{w}=\dfrac{\mathbf{x}^T\mathbf{y}}{\mathbf{x}^T\mathbf{x}}$.

**Resposta:** Verdadeiro

**Justificativa:** Com $d=1$, $X^TX=\mathbf{x}^T\mathbf{x}$ é um
escalar (positivo, se $\mathbf{x}\ne\mathbf{0}$), e $X^T\mathbf{y}=
\mathbf{x}^T\mathbf{y}$ também é escalar. Isolando $\hat{w}$ obtemos
exatamente a fórmula do MathML para projeção sobre uma reta (§3.8.1,
eq. 3.41), o caso 1D do qual o Bloco 4 generalizou.

### Derivação das Equações Normais — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Num problema de estimar um único parâmetro físico
(temperatura média) a partir de $N$ leituras redundantes de um
termômetro (cada leitura sendo $y_i = \theta + \text{ruído}$), a mesma
derivação das Equações Normais levaria a uma estimativa que é,
essencialmente, a média das leituras.

**Resposta:** Verdadeiro

**Justificativa:** Nesse problema, $X$ é o vetor-coluna de todos os
$1$'s ($\mathbf{x}=\mathbf{1}$), e a fórmula do item (b) dá
$\hat\theta=\dfrac{\mathbf{1}^T\mathbf{y}}{\mathbf{1}^T\mathbf{1}}=
\dfrac{\sum_i y_i}{N}$ — exatamente a média aritmética das leituras.

### Derivação das Equações Normais — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como as Equações Normais são obtidas impondo
ortogonalidade coluna a coluna, isso implica que, se duas colunas de
$X$ forem ortogonais entre si, a equação normal correspondente a cada
uma delas pode ser resolvida de forma totalmente independente da
outra, sem nenhum termo cruzado.

**Resposta:** Falso

**Justificativa:** Ortogonalidade **entre apenas duas colunas** $i$ e
$j$ zera só a entrada $(i,j)$ de $X^TX$. Se $X$ tiver outras colunas
não ortogonais a $i$ ou $j$, as equações para $\hat{w}_i$ e
$\hat{w}_j$ continuam acopladas através dessas outras colunas — só a
ortogonalidade mútua entre **todas** as colunas (deixando $X^TX$
inteiramente diagonal) desacopla completamente o sistema, não a
ortogonalidade de um único par.

---

### Invertibilidade de $X^TX$ e a pseudo-inversa — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se $X$ tivesse posto deficiente (colunas linearmente
dependentes), $X^TX$ deixaria de ser invertível, mas isso não
impediria, por si só, que existisse **algum** $\hat{\mathbf{w}}$
satisfazendo as Equações Normais — apenas deixaria de haver um único.

**Resposta:** Verdadeiro

**Justificativa:** O sistema $X^TX\hat{\mathbf{w}}=X^T\mathbf{y}$ é
sempre consistente, mesmo com $X^TX$ singular, porque $X^T\mathbf{y}$
está sempre no espaço-linha de $X^TX$ (um fato geral de álgebra
linear: $\text{col}(X^TX)=\text{col}(X^T)$). Existem soluções — só não
uma única, como visto no Caso 1 do Bloco 6 (a coluna duplicada).

### Invertibilidade de $X^TX$ e a pseudo-inversa — item (b)

**Heurística:** Caso limite

**Afirmação:** ✔ No caso-limite em que $X$ tem uma única coluna
não-nula ($d=1$, $\mathbf{x}\ne\mathbf{0}$), $X^TX$ é sempre invertível
(é um escalar positivo).

**Resposta:** Verdadeiro

**Justificativa:** $X^TX=\mathbf{x}^T\mathbf{x}=\|\mathbf{x}\|^2>0$
sempre que $\mathbf{x}\ne\mathbf{0}$ — um escalar positivo é trivialmente
invertível (basta dividir por ele).

### Invertibilidade de $X^TX$ e a pseudo-inversa — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Num problema de reconstrução de sinais com uma matriz
de observação $X$ de posto deficiente, a pseudo-inversa
$(X^TX)^{-1}X^T$ não pode ser calculada da forma usual, mas existem
generalizações (pseudo-inversa de Moore-Penrose, via SVD) que
contornam exatamente esse problema.

**Resposta:** Verdadeiro

**Justificativa:** A pseudo-inversa "ingênua" apresentada nesta aula
($(X^TX)^{-1}X^T$) exige $X^TX$ invertível; quando isso falha (posto
deficiente), a pseudo-inversa de Moore-Penrose (definida via SVD, tema
de aula futura) generaliza o conceito para qualquer matriz, cheia ou
deficiente em posto.

### Invertibilidade de $X^TX$ e a pseudo-inversa — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como $(X^TX)^{-1}X^T$ é chamada de pseudo-inversa de
$X$, isso significa que ela satisfaz $X\cdot(X^TX)^{-1}X^T = I$ (a
identidade), do mesmo jeito que uma inversa de matriz quadrada de
verdade.

**Resposta:** Falso

**Justificativa:** $X\cdot(X^TX)^{-1}X^T = P_\pi$, a matriz de
projeção sobre $\text{col}(X)$ — não a identidade, a menos que
$N=d$ (caso em que $\text{col}(X)$ já é o espaço inteiro). Em geral
($N>d$, o caso desta aula), $P_\pi$ tem posto $d<N$, logo é
necessariamente **singular**, nunca a identidade. "Pseudo" no nome
existe justamente porque ela não tem todas as propriedades de uma
inversa verdadeira.

---

### Aplicação numérica e verificação de ortogonalidade — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se, em vez de comparar $\hat{\mathbf{w}}$ obtido pela
fórmula fechada com `np.linalg.lstsq`, comparássemos com uma resolução
por eliminação de Gauss do sistema $X^TX\hat{\mathbf{w}}=X^T\mathbf{y}$,
esperaríamos, a menos de erro de arredondamento, o mesmo vetor.

**Resposta:** Verdadeiro

**Justificativa:** Eliminação de Gauss, inversão explícita e `lstsq`
resolvem a mesma equação matemática (as Equações Normais, ou o
problema de mínimos quadrados equivalente); diferem apenas no algoritmo
numérico usado, não no resultado exato.

### Aplicação numérica e verificação de ortogonalidade — item (b)

**Heurística:** Caso limite

**Afirmação:** ✔ No caso-limite em que $\mathbf{y}$ é o vetor nulo, o
$\hat{\mathbf{w}}$ que resolve as Equações Normais (com $X$ de posto
completo) é necessariamente o vetor nulo também.

**Resposta:** Verdadeiro

**Justificativa:** Com $\mathbf{y}=\mathbf{0}$, $X^T\mathbf{y}=\mathbf{0}$,
e a equação fica $X^TX\hat{\mathbf{w}}=\mathbf{0}$. Como $X^TX$ é
invertível (posto completo), a única solução desse sistema homogêneo é
$\hat{\mathbf{w}}=\mathbf{0}$.

### Aplicação numérica e verificação de ortogonalidade — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Num experimento de física em que um pesquisador mede
a mesma grandeza $N$ vezes com ruído aleatório, verificar que o
resíduo entre o valor estimado e as medições é ortogonal aos
"atributos" do modelo é um teste válido de correção, do mesmo jeito
que foi usado nesta aula para o California Housing.

**Resposta:** Verdadeiro

**Justificativa:** A verificação de ortogonalidade do resíduo
(Passo iii do Bloco 4) é uma identidade algébrica geral, consequência
das Equações Normais — vale para qualquer $X$ e $\mathbf{y}$, não é
específica do California Housing.

### Aplicação numérica e verificação de ortogonalidade — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como o resíduo é ortogonal a cada coluna de $X$,
isso implica que o modelo captura toda a informação relevante contida
nos dados disponíveis para prever $\mathbf{y}$.

**Resposta:** Falso

**Justificativa:** Ortogonalidade do resíduo é garantida sempre que
$\hat{\mathbf{w}}$ resolve as Equações Normais, **independentemente**
de quão informativos são os atributos escolhidos — visto no Bloco 5,
onde o resíduo é ortogonal a cada coluna, mas $R^2\approx 0{,}518$ (o
modelo só explica pouco mais da metade da variação de `MedHouseVal`).
Ortogonalidade garante *otimalidade dentro do subespaço disponível*,
não *suficiência* dos atributos escolhidos.

---

### $R^2$ e o que a ortogonalidade do resíduo garante — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se o $R^2$ do ajuste fosse exatamente $0$ (o modelo
não explica nada da variação de $\mathbf{y}$ além da média), o resíduo
ainda seria ortogonal a cada coluna de $X$, contanto que
$\hat{\mathbf{w}}$ resolva as Equações Normais.

**Resposta:** Verdadeiro

**Justificativa:** A ortogonalidade do resíduo (Passo iii) é uma
consequência direta de $\hat{\mathbf{w}}$ resolver as Equações Normais
— não depende do valor de $R^2$. Mesmo um ajuste inútil ($R^2=0$,
equivalente a prever sempre a média) mantém essa propriedade, se for o
$\hat{\mathbf{w}}$ ótimo dentro de $\text{col}(X)$.

### $R^2$ e o que a ortogonalidade do resíduo garante — item (b)

**Heurística:** Caso limite

**Afirmação:** ✔ No caso-limite $R^2=1$ (ajuste perfeito), o resíduo
$\mathbf{y}-X\hat{\mathbf{w}}$ é o vetor nulo.

**Resposta:** Verdadeiro

**Justificativa:** $R^2=1$ significa que toda a variação de
$\mathbf{y}$ é explicada pelo modelo, ou seja, a soma dos quadrados dos
resíduos é zero — e a única forma de a soma de quadrados ser zero é o
próprio vetor resíduo ser nulo.

### $R^2$ e o que a ortogonalidade do resíduo garante — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Num modelo de previsão de nota de estudantes usando
só o número de horas de sono (um único atributo, claramente
insuficiente para prever notas), seria possível obter um $R^2$ baixo e,
ainda assim, um resíduo perfeitamente ortogonal a essa única coluna —
exatamente como ocorreu com os 4 atributos do California Housing nesta
aula.

**Resposta:** Verdadeiro

**Justificativa:** A mesma lógica do item (a)/Bloco 5 se aplica a
qualquer conjunto de atributos, incluindo um único atributo claramente
insuficiente: a ortogonalidade do resíduo é garantida pela derivação
matemática, não pelo poder explicativo do(s) atributo(s) escolhido(s).

### $R^2$ e o que a ortogonalidade do resíduo garante — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como o resíduo é sempre ortogonal ao espaço-coluna de
$X$ quando $\hat{\mathbf{w}}$ resolve as Equações Normais, um $R^2$
baixo indica necessariamente um erro no cálculo de $\hat{\mathbf{w}}$,
não uma limitação dos atributos escolhidos.

**Resposta:** Falso

**Justificativa:** É exatamente o oposto do que o Bloco 5 mostrou: com
$\hat{\mathbf{w}}$ corretamente calculado (verificado contra `lstsq` e
via ortogonalidade do resíduo), o $R^2\approx 0{,}518$ reflete uma
**limitação dos atributos disponíveis** (só 4, faltando localização,
qualidade da construção etc.), não um erro de cálculo — a ortogonalidade
do resíduo é, na verdade, evidência de que o cálculo está correto, não
de que o ajuste é bom.

---

### Posto e multicolinearidade exata (conexão com a Aula 2) — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se a coluna redundante fabricada no Bloco 6 fosse
$-5\times$`AveRooms` em vez de $2\times$`AveRooms`, o posto de $X$
ainda cairia da mesma forma ao ser adicionada (permaneceria em 4, não
subiria para 5).

**Resposta:** Verdadeiro

**Justificativa:** Qualquer múltiplo escalar não-nulo de uma coluna já
existente (positivo, negativo, fração) é uma combinação linear exata
dessa coluna — não acrescenta nenhuma direção independente ao
espaço-coluna. O valor específico do múltiplo (2, $-5$, ou qualquer
outro não-nulo) não importa para o efeito sobre o posto.

### Posto e multicolinearidade exata (conexão com a Aula 2) — item (b)

**Heurística:** Caso limite

**Afirmação:** ✔ No caso-limite em que todas as $d$ colunas de $X$
fossem múltiplos escalares de uma única coluna não-nula, o posto de
$X$ seria exatamente $1$, independentemente do valor de $d$.

**Resposta:** Verdadeiro

**Justificativa:** Se todas as colunas são múltiplos de uma mesma
direção, o espaço-coluna gerado é uma única reta — dimensão $1$ — não
importa quantas colunas ($d$) existam repetindo essencialmente a mesma
informação.

### Posto e multicolinearidade exata (conexão com a Aula 2) — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✗ Num dataset de sensores IoT em que um atributo é
reportado tanto em Celsius quanto em Fahrenheit (uma transformação
linear afim exata da outra, não apenas um múltiplo escalar), a
inclusão de ambas as colunas na matriz de design também produziria
posto deficiente, pelo mesmo princípio da coluna duplicada exata desta
aula.

**Resposta:** Falso

**Justificativa:** Celsius e Fahrenheit se relacionam por
$F=\frac{9}{5}C+32$ — uma transformação **afim**, com um deslocamento
constante ($+32$), não uma relação puramente linear (múltiplo escalar)
como $2\times$`AveRooms`. Como vetores-coluna, $F_{\text{col}}\ne
\lambda\, C_{\text{col}}$ para nenhum escalar $\lambda$ (a menos que
todas as entradas de $C_{\text{col}}$ sejam iguais, caso degenerado);
a dependência linear só apareceria se a matriz de design **já**
tivesse uma coluna constante (intercepto). Sem esse intercepto, as
colunas de Celsius e Fahrenheit são, em geral, linearmente
**independentes** — o mecanismo não é "o mesmo princípio" da coluna
duplicada exata.

### Posto e multicolinearidade exata (conexão com a Aula 2) — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como a coluna redundante fabricada não acrescenta
nenhuma direção independente ao espaço-coluna de $X$, isso implica que
removê-la necessariamente reduz a qualidade das previsões do modelo
ajustado.

**Resposta:** Falso

**Justificativa:** É o oposto: como a coluna redundante não acrescenta
nenhuma direção nova, $\text{col}(X)$ não muda ao removê-la — a
projeção $\hat{\mathbf{y}}$ (e portanto a qualidade das previsões)
permanece exatamente a mesma. O que se perde ao remover é só a
ambiguidade na distribuição do peso entre a coluna original e sua
cópia, não capacidade preditiva.

---

### Quase-multicolinearidade e número de condição (preview da Aula 4) — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se, em vez de perturbar `MedHouseVal` em 1% do
desvio-padrão, perturbássemos em 10 vezes esse valor (10% do
desvio-padrão), a variação relativa esperada no peso de `AveBedrms` no
par quase-dependente seria, ao menos aproximadamente, também maior do
que a observada com a perturbação de 1% — o número de condição alto
amplifica perturbações maiores tanto quanto amplifica as pequenas.

**Resposta:** Verdadeiro

**Justificativa:** Para o sistema linear de mínimos quadrados, o erro
em $\hat{\mathbf{w}}$ decorrente de uma perturbação em $\mathbf{y}$ é
(aproximadamente) proporcional ao tamanho da perturbação, com o número
de condição como fator de amplificação — dobrar ou multiplicar por 10 o
tamanho do ruído tende a escalar proporcionalmente o efeito sobre
$\hat{\mathbf{w}}$, não a atenuá-lo.

### Quase-multicolinearidade e número de condição (preview da Aula 4) — item (b)

**Heurística:** Caso limite

**Afirmação:** ✔ No caso-limite em que o número de condição de $X^TX$
tende a infinito, $X^TX$ se torna, no limite, singular (não
invertível).

**Resposta:** Verdadeiro

**Justificativa:** O número de condição de $X^TX$ tende a infinito
exatamente quando seu menor autovalor tende a zero — o limite em que a
matriz se torna singular (determinante zero). É a mesma transição
gradual entre "quase-multicolinear" (Caso 2) e "multicolinear exata"
(Caso 1) do Bloco 6.

### Quase-multicolinearidade e número de condição (preview da Aula 4) — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Num modelo de precificação de opções financeiras com
duas variáveis de entrada quase redundantes (ex.: duas medidas de
volatilidade calculadas por métodos ligeiramente diferentes), a mesma
fragilidade numérica (pesos instáveis sob pequena perturbação dos
dados) apareceria, mesmo com o posto de $X$ tecnicamente completo.

**Resposta:** Verdadeiro

**Justificativa:** O mecanismo do Caso 2 (quase-dependência entre
colunas $\Rightarrow$ $X^TX$ mal-condicionada $\Rightarrow$ pesos
instáveis) não depende do domínio dos dados, só da estrutura de
correlação entre atributos — o mesmo problema apareceria com qualquer
par de atributos fortemente correlacionados, financeiro ou não.

### Quase-multicolinearidade e número de condição (preview da Aula 4) — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como o número de condição de $X^TX$ com os 4
atributos completos ($\approx 23\,460$) é maior do que o do par
isolado `AveRooms`/`AveBedrms` ($\approx 420$), isso implica que a
previsão $\hat{\mathbf{y}}$ do modelo completo é proporcionalmente mais
instável do que a previsão do modelo com só esse par de atributos.

**Resposta:** Falso

**Justificativa:** O número de condição mede a instabilidade da
**decomposição** $\hat{\mathbf{w}}$, não da **projeção**
$\hat{\mathbf{y}}$ em si — o padrão "sombra estável, receita instável"
visto ao longo de todo o Bloco 6. Comparar números de condição entre
modelos com números de atributos diferentes não permite concluir nada
diretamente sobre a estabilidade das respectivas previsões
$\hat{\mathbf{y}}$.

---

### A matriz de projeção $P_\pi$ — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se, em vez de projetar $\mathbf{y}$ sobre
$\text{col}(X)$, quiséssemos projetar sobre um subespaço diferente
gerado pelas colunas de outra matriz $Z$ (mesmas dimensões de $X$), a
matriz de projeção correspondente seria $P_\pi'=Z(Z^TZ)^{-1}Z^T$, com a
mesma propriedade $P_\pi'^2=P_\pi'$.

**Resposta:** Verdadeiro

**Justificativa:** A derivação do Passo (iv)/Fonte 6 não depende de
nenhuma particularidade de $X$ — vale para qualquer matriz com colunas
linearmente independentes. Substituir $X$ por $Z$ reproduz exatamente
a mesma fórmula e a mesma propriedade de idempotência.

### A matriz de projeção $P_\pi$ — item (b)

**Heurística:** Caso limite

**Afirmação:** ✔ No caso-limite em que as colunas de $X$ já são
ortonormais ($X^TX=I$), a matriz de projeção se simplifica para
$P_\pi=XX^T$.

**Resposta:** Verdadeiro

**Justificativa:** Com $X^TX=I$, a fórmula
$P_\pi=X(X^TX)^{-1}X^T$ se reduz a $P_\pi=XI^{-1}X^T=XX^T$ — o caso
particular citado pelo MathML (tradução nossa, §3.8.2, Remark, eq.
3.65) quando a base do subespaço já é ortonormal.

### A matriz de projeção $P_\pi$ — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Em compressão de imagem via PCA, manter apenas as
$k$ componentes principais mais informativas e descartar as demais
pode ser descrito por uma matriz de projeção $P_\pi$ com as mesmas
propriedades ($P_\pi^2=P_\pi$, simétrica) discutidas nesta aula.

**Resposta:** Verdadeiro

**Justificativa:** PCA projeta os dados sobre o subespaço gerado pelas
$k$ componentes principais — uma projeção ortogonal, com a mesma
matriz de projeção idempotente e simétrica derivada nesta aula (com as
componentes principais no papel das colunas de $X$, assumidas
ortonormais).

### A matriz de projeção $P_\pi$ — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como $P_\pi=X(X^TX)^{-1}X^T\in\mathbb{R}^{N\times N}$
e toda matriz quadrada invertível que satisfaz $P^2=P$ só pode ser a
identidade, isso implica que $P_\pi$ só pode ser a matriz identidade
quando $X$ tem posto completo.

**Resposta:** Falso

**Justificativa:** A premissa "toda matriz quadrada invertível que
satisfaz $P^2=P$ só pode ser a identidade" é verdadeira, mas
**inaplicável** a $P_\pi$: quando $N>d$ (o caso desta aula), $P_\pi$
tem posto $d<N$ — logo é **singular**, nunca invertível, e portanto
nunca pode ser a identidade, independentemente do posto de $X$. $P_\pi$
só coincidiria com a identidade no caso degenerado $N=d$ (quando
$\text{col}(X)$ já é o espaço inteiro).

---

### Síntese: da falta de solução à ponte para a Aula 4 — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se a Aula 4 mostrasse que o número de condição de
$X^TX$ pode ser calculado exatamente a partir da razão entre o maior e
o menor autovalor de $X^TX$, isso tornaria desnecessário o tipo de
experimento de perturbação numérica usado no Bloco 6 desta aula para
*detectar* fragilidade — mas o experimento de perturbação continuaria
sendo uma forma válida de *demonstrar* o efeito prático dessa
fragilidade.

**Resposta:** Verdadeiro

**Justificativa:** Uma fórmula exata (via autovalores) substitui a
necessidade de *medir empiricamente* o número de condição por
perturbação repetida — mas não torna inválido usar a perturbação como
**demonstração pedagógica** do efeito prático de um número de condição
alto, que é exatamente o papel que ela teve nesta aula.

### Síntese: da falta de solução à ponte para a Aula 4 — item (b)

**Heurística:** Caso limite

**Afirmação:** ✔ No caso-limite em que $X$ tem colunas mutuamente
ortogonais e todas de norma $1$ (uma base ortonormal do espaço-coluna),
o número de condição de $X^TX$ é exatamente $1$ — o melhor
condicionamento numérico possível.

**Resposta:** Verdadeiro

**Justificativa:** Colunas ortonormais implicam $X^TX=I$, cujos
autovalores são todos iguais a $1$; o número de condição (razão entre
maior e menor autovalor) é $1/1=1$, o valor mínimo possível — o caso
oposto extremo à quase-singularidade do Bloco 6.

### Síntese: da falta de solução à ponte para a Aula 4 — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Num pipeline de aprendizado de máquina em que os
atributos de entrada são primeiro padronizados (média 0,
desvio-padrão 1) antes do ajuste, essa etapa de pré-processamento pode,
dependendo dos dados, influenciar o número de condição de $X^TX$
resultante, mesmo sem alterar o posto de $X$.

**Resposta:** Verdadeiro

**Justificativa:** Padronizar os atributos muda as escalas relativas
das colunas de $X$ (e, portanto, os autovalores de $X^TX$), sem mudar
quais colunas são linearmente (in)dependentes — o posto é preservado,
mas o número de condição pode melhorar ou piorar, dependendo da
estrutura de correlação e escala originais dos dados.

### Síntese: da falta de solução à ponte para a Aula 4 — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como as Equações Normais fornecem uma fórmula fechada
exata para $\hat{\mathbf{w}}$ sempre que $X$ tem posto completo, isso
implica que essa fórmula é sempre o método numericamente mais
recomendado para calcular $\hat{\mathbf{w}}$ na prática,
independentemente do número de condição de $X^TX$.

**Resposta:** Falso

**Justificativa:** É exatamente o ponto do Fechamento desta aula:
"mais simples de descrever" não é o mesmo que "mais estável de
calcular". Quando $X^TX$ está mal-condicionada (Bloco 6), inverter
$X^TX$ diretamente amplifica erros numéricos; métodos que evitam formar
$X^TX$ explicitamente (decomposição $QR$, $SVD$ — temas futuros do
curso) são numericamente mais recomendados nesse regime, mesmo
resolvendo, em teoria, a mesma equação.
