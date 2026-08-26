# Soluções — Questões de Verdadeiro/Falso (Aula 2)

> Arquivo de apoio, não publicado (prefixo `_`). Contém a resposta e a
> justificativa de cada item das 12 questões de V/F do `index.qmd`. O
> `index.qmd` publicado continua sem solução — este arquivo existe só
> para conferência do professor/monitor, seguindo a metodologia de
> criação de questões definida em `../../CLAUDE.md`.
>
> Este arquivo acompanha a reescrita completa dos itens de V/F desta
> aula (notas e slides), feita a pedido do usuário depois de uma
> auditoria que encontrou a maioria dos itens anteriores violando a
> metodologia de heurísticas do `CLAUDE.md` (paráfrase literal do texto
> já apresentado, em vez de contrafactual/limite/transferência/falsa
> equivalência).

## A matriz de design

**a.** [ ] Se a matriz de design fosse transposta (linhas = atributos, colunas = observações), o produto que calcula as previsões, $X\mathbf{w}$, ainda faria sentido dimensional sem qualquer outra mudança na definição de $\mathbf{w}\in\mathbb{R}^d$.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** Transpor $X$ muda suas dimensões de $N\times d$ para $d\times N$; multiplicar essa matriz transposta por $\mathbf{w}\in\mathbb{R}^d$ pela direita não é dimensionalmente compatível ($d\times N$ vezes $d\times 1$ não fecha) — a convenção linha=observação/coluna=atributo não é arbitrária, é o que torna $X\mathbf{w}$ bem definido exatamente com $\mathbf{w}\in\mathbb{R}^d$.

**b.** [ ] No caso degenerado em que o dataset tem uma única observação ($N=1$), a matriz de design $X$ se reduz a um vetor-linha, e o produto $X\mathbf{w}$ ainda é bem definido e produz um único número (a previsão daquela observação).

**Heurística:** Caso limite
**Resposta:** Verdadeiro
**Justificativa:** Com $N=1$, $X\in\mathbb{R}^{1\times d}$ é literalmente o vetor de atributos daquela observação, como linha; $X\mathbf{w}=\mathbf{a}_1^T\mathbf{w}$ é um escalar bem definido. O caso $N=1$ não quebra a definição, só a torna trivial.

**c.** [ ] Somar a coluna "renda média" com a coluna "número de cômodos" de um dataset produziria um número sem interpretação física direta, ainda que a operação de soma de vetores esteja matematicamente bem definida.

**Heurística:** Transferência de domínio
**Resposta:** Verdadeiro
**Justificativa:** Nada na álgebra linear proíbe somar entradas de unidades diferentes — a soma está bem definida como operação vetorial —, mas o resultado não corresponde a nenhuma grandeza física com significado (dólares + cômodos não é nada). É a distinção entre "operação bem definida" e "resultado interpretável".

**d.** [ ] Se dois atributos tiverem escalas numéricas muito distintas (ex.: renda em dólares e número de cômodos), isso impede, por si só, que a matriz de design seja usada corretamente num produto matriz-vetor $X\mathbf{w}$.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** A definição de $X\mathbf{w}$ não exige nenhuma relação entre as escalas dos atributos — o produto está matematicamente bem definido independentemente da escala. Diferenças de escala podem afetar o condicionamento numérico do ajuste (tema de aula futura), mas não impedem a operação de estar definida.

---

## Definição formal de matriz e produto matricial

**a.** [ ] Se $A\in\mathbb{R}^{m\times n}$ e $B\in\mathbb{R}^{n\times k}$ com $k=1$, o produto $AB$ se reduz exatamente ao produto matriz-vetor $A\mathbf{x}$ estudado nesta aula, com $\mathbf{x}=B$ visto como vetor-coluna.

**Heurística:** Caso limite
**Resposta:** Verdadeiro
**Justificativa:** É exatamente como o texto introduz $A\mathbf{x}$: o caso particular $k=1$ da fórmula geral de produto de matrizes (Eq. 2.13 do MathML). Testar esse limite confirma que o produto matriz-vetor não é uma operação à parte, é um caso especial do produto matricial geral.

**b.** [ ] Se a matriz de design $X$ tivesse mais colunas do que linhas ($d>N$), o produto $X\mathbf{w}$ com $\mathbf{w}\in\mathbb{R}^d$ ainda estaria bem definido e produziria um vetor de previsões em $\mathbb{R}^N$.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** A definição do produto matriz-vetor só exige que o número de colunas de $X$ ($d$) seja igual à dimensão de $\mathbf{w}$ — não importa a relação entre $N$ e $d$. O produto está bem definido mesmo com $d>N$ (esse caso é o regime "subdeterminado", tema futuro, mas a operação em si não quebra).

**c.** [ ] Trocar a ordem do produto matriz-vetor, calculando $\mathbf{w}^T X^T$ em vez de $X\mathbf{w}$, produz o mesmo conjunto de valores de previsão, ainda que como um vetor-linha em vez de vetor-coluna.

**Heurística:** Transferência de domínio
**Resposta:** Verdadeiro
**Justificativa:** Pela identidade $(AB)^T=B^TA^T$, temos $(X\mathbf{w})^T=\mathbf{w}^TX^T$ — os mesmos $N$ números, só organizados como linha em vez de coluna. Testa se o aluno reconhece a transposição como preservando os valores, mudando só a forma.

**d.** [ ] Como o produto $AB$ só está definido quando o número de colunas de $A$ é igual ao número de linhas de $B$, isso significa que $A\mathbf{x}$ e $\mathbf{x}^TA$ nunca podem estar ambos definidos para a mesma matriz $A$ e o mesmo vetor $\mathbf{x}$.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** Se $A$ for quadrada ($n\times n$) e $\mathbf{x}\in\mathbb{R}^n$, tanto $A\mathbf{x}$ ($n\times n$ vezes $n\times 1$) quanto $\mathbf{x}^TA$ ($1\times n$ vezes $n\times n$) estão definidos simultaneamente — a afirmação de que "nunca podem estar ambos definidos" ignora esse caso comum.

---

## As duas leituras do produto matriz-vetor

**a.** [ ] Se a matriz $A$ tivesse todas as suas colunas iguais entre si (idênticas), a leitura "por linha" de $A\mathbf{x}$ deixaria de ser válida, mas a leitura "por coluna" continuaria válida.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** As duas leituras são identidades algébricas válidas para qualquer matriz $A$, sem exceção. Colunas repetidas não invalidam a leitura por linha — o produto interno linha a linha ($\mathbf{a}_i^T\mathbf{x}$) continua bem definido independentemente de haver colunas iguais.

**b.** [ ] No caso em que $\mathbf{x}$ é o vetor da base canônica $\mathbf{e}_j$ (uma única entrada igual a $1$, as demais $0$), a leitura "por coluna" de $A\mathbf{x}$ se reduz exatamente à $j$-ésima coluna de $A$, isolada.

**Heurística:** Caso limite
**Resposta:** Verdadeiro
**Justificativa:** $A\mathbf{e}_j=\sum_l e_{jl}\mathbf{a}^{(l)}=\mathbf{a}^{(j)}$ — só o termo $l=j$ sobrevive, com coeficiente 1. Confirma concretamente que a leitura "por coluna" é, de fato, a combinação linear pesada pelas entradas de $\mathbf{x}$.

**c.** [ ] As duas leituras do produto matriz-vetor descrevem operações matematicamente diferentes, que apenas coincidem por coincidência numérica.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** As duas leituras não são operações diferentes que "coincidem por acaso" — são a mesma soma dupla (Eq. 2.13) reagrupada de duas formas (por linha, por coluna). É a mesma identidade algébrica, vista de dois ângulos, não uma coincidência numérica entre operações distintas.

**d.** [ ] Se $X$ é a matriz de design e $\mathbf{w}$ tem exatamente uma entrada não nula (só o peso do atributo `AveRooms`), a leitura "por coluna" de $X\mathbf{w}$ implica que $\hat{\mathbf{y}}$ é simplesmente um múltiplo escalar da coluna `AveRooms` de $X$.

**Heurística:** Transferência de domínio
**Resposta:** Verdadeiro
**Justificativa:** Com só um $w_j\ne0$, a combinação linear $\sum_j w_j\mathbf{x}^{(j)}$ se reduz a $w_j\mathbf{x}^{(j)}$ — um múltiplo escalar daquela única coluna. Aplicação direta e verificável da Leitura 2 a um caso concreto do dataset da aula.

---

## Regressão Linear Múltipla como sistema linear

**a.** [ ] Se, em vez de $N\gg d$, tivéssemos $N=d$ exatamente e a matriz $X$ tivesse posto completo, o sistema $X\mathbf{w}=\mathbf{y}$ teria, genericamente, exatamente uma solução — nem sobredeterminado nem subdeterminado.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** Com $N=d$ e posto completo, $X$ é quadrada e invertível — o sistema tem exatamente uma solução por construção, o caso intermediário exato entre sobredeterminado ($N>d$) e subdeterminado ($N<d$).

**b.** [ ] No limite em que $d=1$ (um único atributo), o sistema $X\mathbf{w}=\mathbf{y}$ sobredeterminado ($N\gg 1$) se reduz a encontrar um único escalar $w$ que melhor "explica" $N$ pontos $(x_i,y_i)$.

**Heurística:** Caso limite
**Resposta:** Verdadeiro
**Justificativa:** Com $d=1$, $X$ é um vetor-coluna e $\mathbf{w}$ um escalar; o sistema sobredeterminado se reduz ao caso mais simples de regressão — ajustar $y\approx wx$ com um só parâmetro, ainda sobredeterminado se $N>1$.

**c.** [ ] Um sistema sobredeterminado de imagens de satélite, com muito mais pixels medidos ($N$) do que parâmetros de um modelo físico a estimar ($d$), enfrentaria, genericamente, o mesmo problema de "nenhuma solução exata" discutido nesta aula para o California Housing.

**Heurística:** Transferência de domínio
**Resposta:** Verdadeiro
**Justificativa:** A conclusão "sobredeterminado genericamente não tem solução exata" é uma propriedade estrutural de $N\gg d$ equações ruidosas — não depende do domínio da aplicação (imóveis, imagens de satélite, ou qualquer outro).

**d.** [ ] Como um sistema sobredeterminado não tem, genericamente, solução exata, isso implica que a Regressão Linear Múltipla é uma técnica inútil nesse regime.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** É exatamente o oposto da conclusão da aula: a ausência de solução exata não é um beco sem saída, é o problema que motiva a Aula 3 (encontrar a melhor solução aproximada). Regressão Linear Múltipla existe precisamente para lidar com esse regime.

---

## As três formas de solução de um sistema linear

**a.** [ ] Existe algum sistema sobredeterminado (mais equações que incógnitas) que tenha, mesmo assim, uma solução exata — não é uma impossibilidade lógica, só um evento não genérico.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** "Genericamente" não é "sempre" — é possível construir um sistema sobredeterminado em que todas as equações extras sejam exatamente consistentes com a mesma solução (ex.: duplicar uma equação já existente). Raro em dados reais ruidosos, mas não impossível.

**b.** [ ] No caso-limite em que $m=0$ (sistema sem nenhuma equação), qualquer $\mathbf{x}\in\mathbb{R}^n$ é, trivialmente, uma "solução" — o sistema tem infinitas soluções por vacuidade.

**Heurística:** Caso limite
**Resposta:** Verdadeiro
**Justificativa:** Sem nenhuma restrição, todo o espaço $\mathbb{R}^n$ satisfaz vacuamente o sistema — um caso degenerado, mas consistente com "nenhuma, uma, ou infinitas", já que zero restrições é o extremo de "poucas restrições o bastante para não isolar um único ponto".

**c.** [ ] O caso "infinitas soluções" do exemplo geométrico desta aula ($x_1+x_2=4$ e $2x_1+2x_2=8$) tem uma propriedade que o distingue do caso homogêneo da Aula 1: o conjunto de soluções não passa pela origem, a menos que $\mathbf{b}$ seja escolhido de forma a incluí-la.

**Heurística:** Transferência de domínio
**Resposta:** Verdadeiro
**Justificativa:** A reta $x_1+x_2=4$ não passa por $(0,0)$, já que $0+0\ne4$. O conjunto-solução de um sistema não homogêneo com infinitas soluções é uma reta/hiperplano deslocado da origem — diferente do caso homogêneo (Aula 1), cujo conjunto-solução é sempre um subespaço que contém a origem.

**d.** [ ] Um sistema linear real que admitisse exatamente duas soluções distintas $\mathbf{x}_1\ne\mathbf{x}_2$ teria, na verdade, que ter infinitas soluções — incluindo toda combinação $\lambda\mathbf{x}_1+(1-\lambda)\mathbf{x}_2$.

**Heurística:** Falsa dicotomia
**Resposta:** Verdadeiro
**Justificativa:** Por linearidade, $A(\lambda\mathbf{x}_1+(1-\lambda)\mathbf{x}_2)=\lambda\mathbf{b}+(1-\lambda)\mathbf{b}=\mathbf{b}$ — toda combinação afim de duas soluções também é solução. Se duas soluções distintas existem, essa família inteira (infinita) de combinações também são soluções — é exatamente por isso que "exatamente duas" nunca acontece.

---

## Sistemas homogêneos vs. não homogêneos

**a.** [ ] Se um sistema homogêneo $A\mathbf{x}=\mathbf{0}$ tem apenas a solução trivial, então o sistema não homogêneo correspondente $A\mathbf{x}=\mathbf{b}$, quando tem solução, tem exatamente uma solução (nunca infinitas).

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** Se duas soluções distintas $\mathbf{x}_1,\mathbf{x}_2$ de $A\mathbf{x}=\mathbf{b}$ existissem, $\mathbf{x}_1-\mathbf{x}_2$ seria solução não trivial de $A\mathbf{x}=\mathbf{0}$ (por linearidade) — contradizendo a suposição de que só a trivial existe. Logo, unicidade do homogêneo implica unicidade do não homogêneo (quando solúvel).

**b.** [ ] No caso em que $A$ é a matriz nula ($A=\mathbf{0}$), o sistema homogêneo $A\mathbf{x}=\mathbf{0}$ tem $\mathbb{R}^n$ inteiro como conjunto-solução, e o sistema não homogêneo $A\mathbf{x}=\mathbf{b}$ com $\mathbf{b}\ne\mathbf{0}$ não tem solução alguma.

**Heurística:** Caso limite
**Resposta:** Verdadeiro
**Justificativa:** Com $A=\mathbf{0}$, $A\mathbf{x}=\mathbf{0}$ para qualquer $\mathbf{x}$ (o subespaço-solução é tudo); mas $A\mathbf{x}=\mathbf{0}\ne\mathbf{b}$ para qualquer $\mathbf{x}$ e qualquer $\mathbf{b}\ne\mathbf{0}$ — nenhuma solução. O caso mais extremo de "solução homogênea máxima, solução não homogênea vazia".

**c.** [ ] O conjunto-solução de um sistema não homogêneo $A\mathbf{x}=\mathbf{b}$, com $\mathbf{b}\ne\mathbf{0}$, também é sempre um subespaço vetorial.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** Todo subespaço contém a origem, mas $\mathbf{x}=\mathbf{0}$ nunca satisfaz $A\mathbf{x}=\mathbf{b}$ quando $\mathbf{b}\ne\mathbf{0}$ (já que $A\cdot\mathbf{0}=\mathbf{0}\ne\mathbf{b}$). O conjunto-solução não homogêneo, quando existe e não é único, não pode ser um subespaço.

**d.** [ ] Se $\mathbf{x}_1,\mathbf{x}_2$ são duas soluções distintas de $A\mathbf{x}=\mathbf{b}$ com $\mathbf{b}\ne\mathbf{0}$, a soma $\mathbf{x}_1+\mathbf{x}_2$ também é, em geral, solução do mesmo sistema.

**Heurística:** Transferência de domínio
**Resposta:** Falso
**Justificativa:** $A(\mathbf{x}_1+\mathbf{x}_2)=A\mathbf{x}_1+A\mathbf{x}_2=\mathbf{b}+\mathbf{b}=2\mathbf{b}\ne\mathbf{b}$ (a menos que $\mathbf{b}=\mathbf{0}$). O conjunto-solução não homogêneo não é fechado sob soma — a segunda propriedade de subespaço que falha, além de não conter a origem (item c).

---

## Combinações lineares e independência

**a.** [ ] Se um conjunto de vetores $\{\mathbf{x}_1,\dots,\mathbf{x}_k\}$ é linearmente dependente, então necessariamente pelo menos um deles pode ser escrito como combinação linear dos demais.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** Se existe combinação não trivial $\sum\lambda_i\mathbf{x}_i=\mathbf{0}$ com algum $\lambda_j\ne0$, isolando o termo $j$: $\mathbf{x}_j=-\frac{1}{\lambda_j}\sum_{i\ne j}\lambda_i\mathbf{x}_i$ — sempre é possível isolar um vetor com coeficiente não nulo e escrevê-lo em função dos outros.

**b.** [ ] Um conjunto formado por um único vetor não nulo, $\{\mathbf{x}_1\}$ com $\mathbf{x}_1\ne\mathbf{0}$, é sempre linearmente independente.

**Heurística:** Caso limite
**Resposta:** Verdadeiro
**Justificativa:** A única forma de $\lambda_1\mathbf{x}_1=\mathbf{0}$ com $\mathbf{x}_1\ne\mathbf{0}$ é $\lambda_1=0$ — não há outros vetores para combinar, então é independente por definição, mesmo no caso degenerado de um único elemento.

**c.** [ ] Se um dos atributos da matriz de design fosse literalmente o vetor nulo (uma coluna de zeros, ex.: um sensor sempre desligado), essa coluna, junto com qualquer outra coluna não nula, formaria um conjunto linearmente dependente.

**Heurística:** Transferência de domínio
**Resposta:** Verdadeiro
**Justificativa:** O vetor nulo, sozinho, já admite combinação não trivial que dá zero ($\lambda\cdot\mathbf{0}=\mathbf{0}$ para qualquer $\lambda\ne0$) — qualquer conjunto que inclua o vetor nulo é automaticamente dependente, não importa quais outros vetores o acompanham.

**d.** [ ] Como um conjunto de vetores linearmente independentes "não tem redundância", isso significa que todo subconjunto de um conjunto linearmente dependente também deve ser linearmente dependente.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** Um conjunto dependente pode conter subconjuntos independentes — ex.: $\{\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_1+\mathbf{v}_2\}$ é dependente, mas o subconjunto $\{\mathbf{v}_1,\mathbf{v}_2\}$ pode ser perfeitamente independente. "Ter redundância" descreve o conjunto todo, não implica que toda parte dele também seja redundante.

---

## Vetores em excesso e dependência forçada

**a.** [ ] Se, no exemplo dos 3 vetores em $\mathbb{R}^2$ desta aula, $\mathbf{v}_3$ tivesse sido escolhido de forma completamente aleatória (em vez do valor específico usado), o resultado — dependência linear entre os três — ainda seria garantido.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** O argumento (mais vetores que dimensões força dependência) vale para qualquer terceiro vetor em $\mathbb{R}^2$, não só para o exemplo numérico específico usado — não foi coincidência da escolha de $\mathbf{v}_3$, como o texto já explicita.

**b.** [ ] $d+1$ vetores quaisquer em $\mathbb{R}^d$ são sempre linearmente dependentes.

**Heurística:** Transferência de domínio
**Resposta:** Verdadeiro
**Justificativa:** É a generalização direta do contraexemplo dos 3 vetores em $\mathbb{R}^2$ para dimensão arbitrária $d$: mais vetores do que dimensões disponíveis força dependência, sempre.

**c.** [ ] É possível encontrar 5 vetores linearmente independentes em $\mathbb{R}^3$.

**Heurística:** Transferência de domínio
**Resposta:** Falso
**Justificativa:** O número máximo de vetores linearmente independentes em $\mathbb{R}^3$ é 3 — a mesma lógica do item anterior, aplicada ao caso $d=3$: 5 vetores (mais que $d+1=4$) forçam dependência com ainda mais folga.

**d.** [ ] Como o número máximo de vetores linearmente independentes em $\mathbb{R}^d$ é $d$, isso implica que qualquer conjunto de exatamente $d$ vetores em $\mathbb{R}^d$ é automaticamente linearmente independente.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** $d$ ser o número máximo possível não garante que um conjunto específico de $d$ vetores atinja esse máximo — é fácil construir $d$ vetores dependentes em $\mathbb{R}^d$ (ex.: repetir um vetor). "No máximo $d$" é um teto, não uma garantia para qualquer escolha de exatamente $d$ vetores.

---

## Multicolinearidade em atributos de um dataset

**a.** [ ] Se, em vez de "área em m²" e "área em pés²" (proporcionais, fator de conversão fixo), tivéssemos "área em m²" e "área em m² mais um ruído de medição aleatório e independente", essas duas colunas formariam um par exatamente multicolinear (dependência linear exata).

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** Adicionar ruído independente rompe a relação linear exata entre as colunas — elas continuam fortemente correlacionadas (quase-multicolineares), mas não mais exatamente proporcionais. Qualquer ruído genuíno já torna a relação apenas aproximada, não uma dependência linear exata.

**b.** [ ] No caso em que duas colunas de atributos são idênticas (não só proporcionais, mas exatamente iguais, ex.: o mesmo atributo duplicado por erro de importação de dados), elas são um caso particular de multicolinearidade exata, com fator de proporcionalidade igual a $1$.

**Heurística:** Caso limite
**Resposta:** Verdadeiro
**Justificativa:** Colunas idênticas satisfazem $\mathbf{a}^{(j)}=1\cdot\mathbf{a}^{(i)}$, uma combinação linear (trivialmente) exata — o caso mais simples e mais comum de multicolinearidade exata na prática (erro de duplicação de coluna).

**c.** [ ] Duas colunas de um dataset financeiro, "salário anual" e "salário mensal" (uma sendo exatamente 12 vezes a outra, sem nenhuma variação adicional), formariam um par de colunas multicolineares exatas, pela mesma lógica do exemplo de área em m²/pés² desta aula.

**Heurística:** Transferência de domínio
**Resposta:** Verdadeiro
**Justificativa:** É a mesma estrutura — duas colunas relacionadas por um fator de conversão fixo e exato (12, em vez de $\approx10{,}76$ de m² para pés²) são linearmente dependentes por definição, independentemente do domínio.

**d.** [ ] Como medir o mesmo atributo em duas unidades diferentes tipicamente produz colunas multicolineares exatas, isso significa que toda dupla de atributos fisicamente relacionados entre si (não necessariamente a mesma grandeza em unidades diferentes) também deve ser exatamente multicolinear.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** Relação física (ex.: `AveRooms` e `AveBedrms`) não é o mesmo que ser a mesma grandeza medida duas vezes. O próprio Bloco 6 da aula mostra atributos fisicamente relacionados, fortemente correlacionados ($0{,}865$), mas **não** exatamente multicolineares (posto continua completo).

---

## Posto de uma matriz

**a.** [ ] Se uma matriz $A\in\mathbb{R}^{m\times n}$ tivesse todas as suas $n$ colunas idênticas entre si (e $n>1$), seu posto seria exatamente $1$, independentemente de $m$ e $n$.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** Colunas idênticas são todas múltiplas umas das outras — o número de colunas linearmente independentes entre elas é exatamente 1 (qualquer uma sozinha "gera" todas as outras). O posto é 1, não importa quantas colunas repetidas existam.

**b.** [ ] O posto de uma matriz $A\in\mathbb{R}^{m\times n}$ nunca pode ser maior que $\min(m,n)$.

**Heurística:** Caso limite
**Resposta:** Verdadeiro
**Justificativa:** É o teto estrutural implícito na própria definição de "posto completo" ($\text{rk}(A)=\min(m,n)$ sendo o maior posto possível) — não há como ter mais colunas (ou linhas) independentes do que o menor dos dois números disponíveis.

**c.** [ ] Uma matriz de design $X\in\mathbb{R}^{N\times d}$ com $N\gg d$ (o regime típico de ML descrito nesta aula) tem, no melhor caso (posto completo), $\text{rk}(X)=d$ — nunca $N$, mesmo com $N$ muito maior que $d$.

**Heurística:** Transferência de domínio
**Resposta:** Verdadeiro
**Justificativa:** Com $N\gg d$, $\min(N,d)=d$, então o teto de posto completo é $d$, não $N$ — ter muito mais observações do que atributos não aumenta o número máximo de colunas independentes possíveis, limitado pelo menor dos dois (número de atributos).

**d.** [ ] Uma matriz é dita deficiente em posto quando seu posto é maior do que $\min(m,n)$.

**Heurística:** Caso limite
**Resposta:** Falso
**Justificativa:** É logicamente impossível ter posto maior que $\min(m,n)$ (item b) — deficiente em posto significa posto **menor** que $\min(m,n)$, não maior. O item testa se o aluno confunde a direção da desigualdade que define deficiência.

---

## Posto e solvabilidade de sistemas lineares

**a.** [ ] Se $\text{rk}(A)\ne\text{rk}([A|\mathbf{b}])$ para um sistema específico, isso implica necessariamente que $\text{rk}([A|\mathbf{b}]) = \text{rk}(A)+1$, nunca uma diferença maior.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** Acrescentar uma única coluna ($\mathbf{b}$) a uma matriz pode aumentar o posto em, no máximo, 1 — uma coluna nova contribui com, no máximo, uma nova direção independente. Se os postos diferem, a diferença só pode ser exatamente 1.

**b.** [ ] No caso em que $\mathbf{b}=\mathbf{0}$ (sistema homogêneo), $\text{rk}([A|\mathbf{0}]) = \text{rk}(A)$ sempre, e portanto o critério de solvabilidade é automaticamente satisfeito.

**Heurística:** Caso limite
**Resposta:** Verdadeiro
**Justificativa:** Acrescentar uma coluna de zeros nunca aumenta o posto (a coluna nula é combinação linear trivial de qualquer conjunto de colunas) — por isso o sistema homogêneo sempre tem solução (ao menos a trivial), agora visto pela lente do critério de posto.

**c.** [ ] Um sistema $A\mathbf{x}=\mathbf{b}$ em que $A$ tem posto deficiente, mas $\mathbf{b}$ está fora do espaço gerado pelas colunas de $A$, não tem solução, mesmo que $A$ tenha, tecnicamente, "várias direções redundantes" disponíveis.

**Heurística:** Transferência de domínio
**Resposta:** Verdadeiro
**Justificativa:** Posto deficiente por si só não garante solubilidade — o critério exige que $\mathbf{b}$ seja alcançável como combinação das colunas de $A$. Ter colunas redundantes não ajuda se $\mathbf{b}$ simplesmente não está no espaço gerado por elas.

**d.** [ ] Como posto deficiente pode indicar multicolinearidade exata, toda vez que um sistema $A\mathbf{x}=\mathbf{b}$ não tem solução, a causa deve ser posto deficiente de $A$.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** Um sistema pode não ter solução mesmo com $A$ de posto completo — é o caso sobredeterminado típico de ML ($N\gg d$, posto completo igual a $d$, mas $\mathbf{y}$ genericamente fora do espaço gerado pelas colunas). Posto deficiente é uma causa possível, não a única nem a mais comum no regime desta aula.

---

## Multicolinearidade exata vs. quase-multicolinearidade

**a.** [ ] Se a correlação entre `AveRooms` e `AveBedrms` fosse exatamente $1{,}0$ (em vez de $0{,}865$), o posto da matriz de design cairia de $4$ para $3$.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** Correlação exatamente $1$ entre duas colunas significa que uma é combinação linear exata da outra — dependência linear exata, reduzindo o posto em 1 (de 4 colunas independentes para 3), exatamente como a coluna duplicada artificial do Bloco 5 desta aula.

**b.** [ ] No limite em que a correlação entre dois atributos tende a $1$ mas nunca a alcança exatamente (ex.: $0{,}999999$), o posto da matriz permanece tecnicamente completo, mas o sistema fica numericamente cada vez mais instável.

**Heurística:** Caso limite
**Resposta:** Verdadeiro
**Justificativa:** Por mais próxima de 1 que a correlação esteja, sem ser exatamente 1 as colunas permanecem, tecnicamente, linearmente independentes (posto completo) — mas a instabilidade numérica (número de condição, Aula 4) cresce sem limite conforme a correlação se aproxima do caso exato.

**c.** [ ] Quase-multicolinearidade pode causar instabilidade numérica no ajuste de um modelo, mesmo sem reduzir tecnicamente o posto da matriz.

**Heurística:** Falsa equivalência
**Resposta:** Verdadeiro
**Justificativa:** É exatamente a distinção central do Bloco 6: posto completo (tecnicamente correto) não é o mesmo que "bem-condicionado na prática" — os dois conceitos, posto e estabilidade numérica, medem coisas diferentes e podem divergir.

**d.** [ ] Dois atributos de um dataset médico, "peso em kg" e "índice de massa corporal (IMC)", fortemente correlacionados mas não exatamente proporcionais (o IMC depende também da altura), ilustrariam o mesmo tipo de quase-multicolinearidade discutido para `AveRooms`/`AveBedrms`, não uma multicolinearidade exata.

**Heurística:** Transferência de domínio
**Resposta:** Verdadeiro
**Justificativa:** Peso e IMC estão relacionados (IMC = peso/altura²) mas não são proporcionais um ao outro sem envolver uma terceira variável (altura) — a mesma categoria de "correlacionados, não exatamente dependentes" do exemplo `AveRooms`/`AveBedrms` da aula.
