# Respostas das Pausas Ativas — Aula 7

> Arquivo não publicado. As Pausas Ativas já trazem a resolução (✔/✗)
> nos slides (RevealJS); este arquivo serve para o professor aprofundar
> a discussão em sala, além do que cabe num slide.

---

## Pausa 1 — Multicolinearidade e a Matriz $X^TX$

**Discussão:** o ponto pedagógico é conectar posto de matriz (álgebra
linear, já visto em `optimization-linear-algebra`) com a fórmula
fechada do MLE. Vale desenhar no quadro: se $x_1 = c\cdot x_0$, a
segunda coluna de $X$ é combinação linear da primeira, então $X$ (e
$X^TX$) tem posto deficiente — o determinante de $X^TX$ é o produto dos
autovalores, e um autovalor nulo (na direção da dependência linear) zera
o produto inteiro. O terceiro item é o clímax do bloco: soma de
$\lambda I$ desloca **todos** os autovalores por $+\lambda$, então
mesmo o autovalor que era exatamente zero vira $\lambda > 0$ — a matriz
deixa de ser singular para qualquer $\lambda$ positivo, por menor que
seja. Vale enfatizar que isso é diferente de "melhorar" o
condicionamento aos poucos: é uma garantia de invertibilidade, ponto.

## Pausa 2 — O Papel de $\lambda$ e a Fórmula Fechada

**Discussão:** o item mais sutil é o terceiro (D > N). Alunos tendem a
achar que "matriz singular" é um estado permanente que a regularização
"conserta parcialmente" — vale reforçar que $(X^TX+\lambda I)$ é
invertível para **qualquer** $\lambda>0$ nesse cenário, não é uma
questão de $\lambda$ "grande o suficiente". Essa é a razão prática pela
qual Ridge (e regularização em geral) é indispensável em problemas de
alta dimensão ($D \gg N$), comuns em genômica, processamento de texto
(bag-of-words) e imagens.

## Pausa 3 — A Equivalência $\lambda = \sigma^2/\tau^2$

**Discussão:** o último item é o mais avançado do bloco — vale
verbalizar que o princípio geral é: **a log-posterior é sempre a soma
da log-verossimilhança com a log-prior**, e essa soma nunca depende de
qual família a verossimilhança pertence. Trocar Bernoulli por Gaussiana
muda o primeiro termo (de entropia cruzada para soma de quadrados), mas
o segundo termo (a penalidade $L_2$ vinda da prior Gaussiana) é sempre
somado do mesmo jeito — é exatamente esse princípio que permite
"Ridge logístico" e "Lasso logístico" (regularização de GLMs em geral),
mesmo sem solução fechada em nenhum dos dois casos.

## Pausa 4 — Soft-Thresholding e a Origem da Sparsity

**Discussão:** o exercício numérico do primeiro item ($\hat\beta_{\text{MLE}}=3$,
$\lambda=5$) vale fazer no quadro passo a passo: $\text{sign}(3)=+1$,
$|3|-5=-2$, $\max(-2,0)=0$, resultado $\beta^*=0$. É importante que os
alunos vejam que o "$\max(\cdot,0)$" é o que impede o coeficiente de
"passar para o outro lado" do zero — sem ele, a fórmula $\hat\beta_{\text{MLE}}-\lambda\,\text{sign}(\hat\beta_{\text{MLE}})$
daria $3-5=-2$, um valor negativo espúrio, sinal errado em relação ao
$\hat\beta_{\text{MLE}}$ original. O quarto item é a síntese conceitual
do bloco inteiro: a origem da sparsity não é "a forma do diamante" por
si só (isso é a intuição visual) — é, algebricamente, o fato de o
subgradiente de $|\beta|$ em zero ser um **intervalo**, não um ponto,
permitindo que a condição de otimalidade seja satisfeita exatamente em
$\beta=0$ para um intervalo inteiro de valores de $\hat\beta_{\text{MLE}}$.
