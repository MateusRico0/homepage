## Resumo — Aula 11

A Aula 10 terminou com uma suposição em aberto: tudo ali valia enquanto os dados continuassem parecidos com os do treino. A Aula 11 trata de como perceber que eles mudaram, sem rótulos novos. O problema é o **teste de duas amostras**: dadas uma amostra de referência e uma amostra de produção, decidir se vêm da mesma distribuição.

A aula começa pelo problema e pelas comparações que qualquer um tentaria primeiro (médias, um teste por atributo, densidades estimadas), mostra em exemplos pequenos onde cada uma deixa passar uma diferença, e só então chega à **Maximum Mean Discrepancy (MMD)**. A Aula 5 já usou a MMD como ferramenta pronta, com a fórmula do estimador e o teste de permutação; aqui derivamos a fórmula a partir da definição, provamos por que a permutação controla o erro e estudamos o que decide se o teste enxerga uma diferença (largura de banda, dimensão, tamanho da amostra). O último bloco volta ao sistema em produção: que tipo de mudança um teste em $P(\mathbf{x})$ consegue ver, quando um alarme importa, e o que é alinhar duas distribuições.

**Objetivos:**
1. Formular a detecção de *drift* como teste de duas amostras e explicar por que comparar médias, marginais ou densidades estimadas não basta.
2. Demonstrar que o teste de permutação tem nível $\alpha$ sem nenhuma suposição sobre a forma das distribuições.
3. Derivar $\mathrm{MMD}^2=\mathbb{E}[k(\mathbf{x},\mathbf{x}')]-2\,\mathbb{E}[k(\mathbf{x},\mathbf{y})]+\mathbb{E}[k(\mathbf{y},\mathbf{y}')]$ a partir da definição como supremo, e ler a função-testemunha como diferença de dois KDEs (Aula 2).
4. Distinguir os estimadores viesado e não viesado, explicar o valor negativo visto na Aula 5 e relacionar largura de banda, dimensão e poder do teste.
5. Interpretar um alarme de *drift*: tipos de mudança, significância × relevância, e alinhamento como redução da MMD.

**Pré-requisitos (conferidos no dicionário de notações):** teste de hipótese e $p$-valor (Aula 1, $\chi^2_d$); KDE e largura de banda $h$, concentração de distâncias (Aula 2); KS em projeções, estimador da MMD e teste de permutação usados sem derivação (Aula 5); PCA e autoencoder como redutores (Aulas 6 e 7). Kernel como produto interno num espaço de atributos não foi derivado nesta disciplina: a aula o introduz a partir de PRML §6.1–6.2.

**Estratégia Pedagógica:** A (Outside-In) — o tema é um método (um teste), e a necessidade da teoria aparece nas falhas das comparações simples.

**Datasets:**
1. ***Gas Sensor Array Drift*** (UCI, Vergara, 2012; CC BY 4.0), dataset-fio. 13.910 medições de 16 sensores químicos, 8 atributos por sensor (128 no total), 6 gases, coletadas ao longo de 36 meses e organizadas em 10 lotes cronológicos. O lote 1 (meses 1 e 2) faz o papel de treino; os demais, de produção. O gás (rótulo) só aparece para conferir, como no resto do curso. Não está no Hugging Face Hub: o chunk de setup baixa o `.zip` da UCI uma vez e guarda em cache local. Testado em 2026-11-11: carrega, 128 colunas, contagens por lote batem com a página da UCI.
2. **Sintéticos 2D e 1D**, só para isolar um ponto: pares de amostras com mesma média, mesmas marginais ou mesmos dois primeiros momentos.
3. **MNIST × USPS** (`ylecun/mnist`, `flwrlabs/usps`; o segundo testado em 2026-11-11, 16×16, 7.291 + 2.007 imagens): participação curta no Bloco 5, como mudança de domínio que se vê a olho. É a parte mais fácil de cortar se o tempo apertar.

**Sondagem feita antes do plano (números preliminares, serão recalculados no `index.qmd`):**
- Um classificador treinado no lote 1 (97% em validação cruzada) cai para 82% no lote 2, 63% no lote 3 e fica entre 33% e 47% do lote 5 em diante.
- $\widehat{\mathrm{MMD}}^2_u$ (RBF, mediana) entre metades aleatórias do lote 1: 0,008. Entre o lote 1 e os lotes 2 a 10: de 0,10 a 0,49, todos com $p$ no mínimo possível para 300 permutações.
- Calibração: em 200 divisões aleatórias do lote 1, o teste rejeitou em 6% a 5% de nível.
- O drift não é só mudança na mistura de gases: comparando um mesmo gás entre lotes (etanol, etileno, acetona), a MMD também rejeita em todos. A mistura também muda (o tolueno tem 5 leituras no lote 2 e nenhuma nos lotes 3 a 5), então há as duas coisas.
- KS por atributo com Bonferroni rejeita em 109 a 128 dos 128 atributos nos lotes 2 a 10 e em nenhum na divisão do lote 1. Neste dataset a comparação simples funciona, e a aula vai dizer isso (bate com Rabanser et al., 2019).
- Padronizar cada lote com a própria média e desvio reduz bastante a MMD e recupera parte da acurácia, sem zerar nenhuma das duas. Os números da sondagem inicial foram substituídos pelos do `index.qmd` (com truncamento em ±10 desvios e referência 1a): a MMD cai de 5 a 58 vezes e a acurácia melhora em 7 dos 9 lotes (lote 6: de 46,7% para 76,9%; lote 4 piora, de 65,8% para 61,5%).

---

## Plano de aula — Aula 11 (carga horária: 60 min)

Versão final, enxuta para uma aula de 1 hora (o plano original somava cerca de 95 min em 5 blocos). Cortes em relação ao plano original: testemunha em 2D, experimento de redução de dimensão no gás, figura da mistura de gases e da MMD por gás, figura de significância × tamanho da amostra, MNIST × USPS. A demonstração do nível do teste de permutação fica completa nas notas; nos slides vai só a ideia em três passos. O teste por classificador foi para o Fechamento, como ponte.

1. **Revisão e Introdução** (~6 min) — o problema no *Gas Sensor Array Drift* (acurácia do classificador por lote e projeção em 2 componentes principais); o que já vimos (KDE da Aula 2, MMD usada sem explicação na Aula 5, Aula 10); ideia central (comparar médias de funções) e 4 perguntas.
2. **As comparações mais simples** (~5 min) — diferença de médias, KS por atributo, médias e covariâncias; quatro pares sintéticos em 2D e tabela de poder. Nenhuma detecta o caso (d). No gás as comparações simples funcionam, e isso é dito.
3. **Intuição: a função que mais separa as duas amostras** (~3 min) — Gaussiana × Laplace com a mesma média e variância; função testemunha; a MMD como maior diferença de médias.
4. **Bloco 1: Teste de duas amostras e teste de permutação** (~10 min, com a Pausa 1) — hipóteses, nível e poder; procedimento e p-valor; histogramas no gás e no caso (d); proposição do nível (ideia nos slides, demonstração nas notas). Termina com: o nível vale para qualquer estatística, falta uma estatística com poder.
5. **Bloco 2: A MMD** (~15 min, com a Pausa 2) — definição; caso linear e atributos $(x,x^2)$; kernel e espaço de atributos; teorema $\mathrm{MMD}^2=\mathbb{E}k(\mathbf{x},\mathbf{x}')-2\mathbb{E}k(\mathbf{x},\mathbf{y})+\mathbb{E}k(\mathbf{y},\mathbf{y}')$ com demonstração; testemunha como diferença de dois KDEs; kernel característico e contraexemplo polinomial. Resultado central da aula.
6. **Bloco 3: Estimação, largura do kernel e dimensão** (~10 min, com a Pausa 3) — estimador não viesado e valores negativos; limiar por permutação e custo; heurística da mediana e as duas luas da Aula 5; poder × dimensão.
7. **Bloco 4: Uso no monitoramento e alinhamento** (~9 min, com a Pausa 4) — resultado nos 10 lotes com Bonferroni; o que a rejeição não informa (tipo de mudança, perda de acurácia, tamanho da diferença); padronização por lote como alinhamento e sua hipótese; DAN citada.
8. **Fechamento** (~3 min) — 4 respostas, quadro dos métodos, teste por classificador, Ponte para a Aula 12 (aprendizado contrastivo, InfoNCE).

**Se faltar tempo:** pular o Passo 4 da demonstração do teorema (remeter às notas), o slide da dimensão e os V/F das Pausas (manter só a pergunta aberta).

---

## Notação nova e colisões

- $P$, $Q$: distribuições de referência e de produção. $X=\{\mathbf{x}_i\}_{i=1}^n\sim P$, $Y=\{\mathbf{y}_j\}_{j=1}^m\sim Q$, como na Aula 5. Gretton et al. usam $m$ para $X$ e $n$ para $Y$; avisar ao citar.
- $k(\mathbf{x},\mathbf{x}')=\exp\!\big(-\|\mathbf{x}-\mathbf{x}'\|^2/(2\sigma^2)\big)$, com $\gamma=1/(2\sigma^2)$ ligando ao $\gamma$ da Aula 5. Colisões: $\sigma^2$ é o ruído do decoder nas Aulas 6 e 7; $\gamma$ é a taxa de aprendizado na Aula 10; "kernel" na Aula 2 é a janela do KDE.
- $\mathcal{H}$ (espaço de atributos), $\phi$, $\boldsymbol\mu_P\in\mathcal{H}$ (*mean embedding*). Colisões: $\mathbf{H}$ genérico da Aula 5, $H$ da NMF, $\mu$ média global da Aula 10.
- $\alpha$ (nível do teste) contra $\alpha_0$ da Dirichlet (Aula 5). $B$: número de permutações. $f^\star$: função-testemunha.
- $y$ aparece só no Bloco 5 como rótulo, para escrever os tipos de mudança; no resto da aula $\mathbf{y}_j$ é um ponto da segunda amostra. Usar $c$ para a classe, se a ambiguidade incomodar.

---

## Fontes usadas — Aula 11

Os links de `_fontes/` apontam para `/home/marcos/...` e não abrem nesta máquina. Os PDFs abaixo foram baixados em 2026-11-11 para `../fontes/` ao lado do repositório (fora do git), e os trechos foram extraídos deles. Páginas impressas.

### Fonte 1: Gretton, A., Borgwardt, K. M., Rasch, M. J., Schölkopf, B. & Smola, A. (2012), "A Kernel Two-Sample Test", *JMLR* 13: 723–773
**Uso pretendido:** fonte central. Formulação do problema, definição da MMD, expressão em kernels, estimador não viesado, testemunha, distribuição nula, largura de banda.
**Trechos:**
> "Problem 1 Let x and y be random variables defined on a topological space X, with respective Borel probability measures p and q. Given observations X := {x1, . . . , xm} and Y := {y1, . . . , yn}, independently and identically distributed (i.i.d.) from p and q, respectively, can we decide whether p ≠ q?" (§2.1, p. 725)

> "Lemma 1 Let (X, d) be a metric space, and let p, q be two Borel probability measures defined on X. Then p = q if and only if Ex(f(x)) = Ey(f(y)) for all f ∈ C(X), where C(X) is the space of bounded continuous functions on X. Although C(X) in principle allows us to identify p = q uniquely, it is not practical to work with such a rich function class in the finite sample setting." (§2.1, p. 726)

> "Definition 2 Let F be a class of functions f : X → R and let p, q, x, y, X, Y be defined as above. We define the maximum mean discrepancy (MMD) as MMD[F, p, q] := sup_{f∈F} (Ex[f(x)] − Ey[f(y)]). In the statistics literature, this is known as an integral probability metric (Müller, 1997)." (§2.1, p. 726)

> "Lemma 4 Assume the condition in Lemma 3 for the existence of the mean embeddings µp, µq is satisfied. Then MMD²[F, p, q] = ‖µp − µq‖²_H." (§2.2, p. 727)

> "Evidently, this property will not hold for all H: for instance, a polynomial RKHS of degree two cannot distinguish between distributions with the same mean and variance, but different kurtosis (Sriperumbudur et al., 2010b, Example 3). [...] Theorem 5 Let F be a unit ball in a universal RKHS H, defined on the compact metric space X, with associated continuous kernel k(·, ·). Then MMD[F, p, q] = 0 if and only if p = q." (§2.2, p. 727)

> "Lemma 6 Given x and x′ independent random variables with distribution p, and y and y′ independent random variables with distribution q, the squared population MMD is MMD²[F, p, q] = E_{x,x′}[k(x, x′)] − 2E_{x,y}[k(x, y)] + E_{y,y′}[k(y, y′)], where x′ is an independent copy of x with the same distribution, and y′ is an independent copy of y. An unbiased empirical estimate is a sum of two U-statistics and a sample average" (§2.2, p. 728; a equação (3) segue)

> "It costs O((m + n)²) time to compute both statistics." (§2.2, p. 729)

> "We define the witness function f* to be the RKHS function attaining the supremum in (1) [...] f*(t) ∝ ⟨φ(t), µp − µq⟩_H = Ex[k(x, t)] − Ey[k(y, t)]" (§2.3, p. 729)

> "This test uses the asymptotic distribution of MMD²u under H0 [...] Theorem 12 [...] Then under H0, MMD²u converges in distribution according to t MMD²u[F, X, Y] → Σ_{l=1}^∞ λl [(ρx^{−1/2} al − ρy^{−1/2} bl)² − (ρx ρy)^{−1}]" (§5, p. 737)

> "One way to estimate the 1 − α quantile of the null distribution is using the bootstrap on the aggregated data, following Arcones and Giné (1992)." (§5, p. 737)

> "The empirical MMD is zero both for kernel size σ = 0 (where the aggregate Gram matrix over X and Y is a unit matrix), and also approaches zero as σ → ∞ (where the aggregate Gram matrix becomes uniformly constant). We set σ to be the median distance between points in the aggregate sample, as a compromise between these two extremes: this remains a heuristic [...] and the optimum choice of kernel size is an ongoing area of research. We further note that setting the kernel using the sample being tested may cause changes to the asymptotic distribution" (§8, p. 748)

### Fonte 2: Sriperumbudur, B. K., Gretton, A., Fukumizu, K., Schölkopf, B. & Lanckriet, G. R. G. (2010), "Hilbert Space Embeddings and Metrics on Probability Measures", *JMLR* 11: 1517–1561
**Uso pretendido:** definição de kernel característico e o critério para kernels invariantes por translação em $\mathbb{R}^d$, que cobre o Gaussiano fora de domínios compactos.
**Trechos:**
> "We show that a bounded continuous translation invariant kernel on R^d is characteristic if and only if the support of the Fourier transform of the kernel is the entire R^d." (§1, p. 1521)

> "Definition 6 (Characteristic kernel) A bounded measurable positive definite kernel k is characteristic to a set Q ⊂ P of probability measures defined on (M, A) if for P, Q ∈ Q, γk(P, Q) = 0 ⇔ P = Q." (§3, p. 1530)

### Fonte 3: PRML, §6.1–6.2, pp. 291–297 (PDF pp. 311–317)
**Uso pretendido:** kernel como produto interno num espaço de atributos e o kernel Gaussiano.
**Trechos:**
> "for models which are based on a fixed nonlinear feature space mapping φ(x), the kernel function is given by the relation k(x, x′) = φ(x)ᵀφ(x′). (6.1) From this definition, we see that the kernel is a symmetric function of its arguments" (cap. 6, p. 292)

> "Another commonly used kernel takes the form k(x, x′) = exp(−‖x − x′‖²/2σ²) (6.23) and is often called a 'Gaussian' kernel. Note, however, that in this context it is not interpreted as a probability density" (§6.2, p. 296)

### Fonte 4: Rabanser, S., Günnemann, S. & Lipton, Z. C. (2019), "Failing Loudly: An Empirical Study of Methods for Detecting Dataset Shift", NeurIPS (arXiv:1810.11953v4)
**Uso pretendido:** a prática de detecção: reduzir a dimensão e depois testar; comparação entre vários testes univariados e um multivariado.
**Trechos:**
> "Machine learning (ML) systems, however, which depend strongly on properties of their inputs (e.g. the i.i.d. assumption), tend to fail silently. [...] we show that across the dataset shifts that we explore, a two-sample-testing-based approach, using pre-trained classifiers for dimensionality reduction, performs best." (Abstract, p. 1)

> "As we cannot make strong assumptions about the (in)dependence among the tests, we rely on a conservative aggregation method, notably the Bonferroni correction [4], which rejects the null hypothesis if the minimum p-value among all tests is less than α/K (where α is the significance level of the test)." (§3.2, p. 4)

> "We were surprised to find that, despite the heavy correction, multiple univariate testing seem to offer comparable performance to multivariate testing (see Table 1a)." (§5, p. 6)

### Fonte 5: Reddi, S. J., Ramdas, A., Póczos, B., Singh, A. & Wasserman, L. (2014), "On the Decreasing Power of Kernel and Distance based Nonparametric Hypothesis Tests in High Dimensions" (arXiv:1406.2083v2; AAAI 2015)
**Uso pretendido:** separar a dificuldade de estimar a estatística da dificuldade de testar; poder decrescente com a dimensão.
**Trecho:**
> "we differentiate the hardness of estimation of test statistics from the hardness of testing whether these statistics are zero or not, and explicitly discuss a notion of 'fair' alternative hypotheses for these problems as dimension increases. We then demonstrate that the power of these tests actually drops polynomially with increasing dimension against fair alternatives." (Abstract, p. 1)

### Fonte 6: Long, M., Cao, Y., Wang, J. & Jordan, M. I. (2015), "Learning Transferable Features with Deep Adaptation Networks", ICML (arXiv:1502.02791)
**Uso pretendido:** alinhamento com a MMD como termo de perda. Só citado.
**Trecho:**
> "In DAN, hidden representations of all task-specific layers are embedded in a reproducing kernel Hilbert space where the mean embeddings of different domain distributions can be explicitly matched." (Abstract, p. 1)

### Fonte 7: Lopez-Paz, D. & Oquab, M. (2017), "Revisiting Classifier Two-Sample Tests", ICLR (arXiv:1610.06545v4)
**Uso pretendido:** teste por classificador como alternativa, e gancho para a Aula 12.
**Trecho:**
> "If the null hypothesis 'P = Q' is true, then the classification accuracy of a binary classifier on a held-out subset of this dataset should remain near chance-level." (Abstract, p. 1)

### Fonte 8: Vergara, A. (2012), *Gas Sensor Array Drift Dataset*, UCI Machine Learning Repository, doi:10.24432/C5RP6W
**Uso pretendido:** descrição do dataset-fio.
**Trechos (página do dataset, consultada em 2026-11-11):**
> "This archive contains 13910 measurements from 16 chemical sensors utilized in simulations for drift compensation in a discrimination task of 6 gases at various levels of concentrations."

> "Batch 1 Months 1 and 2 Batch 2 Months 3, 4, 8, 9 and 10 Batch 3 Months 11, 12, and 13 Batch 4 Months 14 and 15 Batch 5 Month 16 Batch 6 Months 17, 18, 19, and 20 Batch 7 Month 21 Batch 8 Months 22 and 23 Batch 9 Months 24 and 30 Batch 10 Month 36"

> "(1: Ethanol; 2: Ethylene; 3:Ammonia; 4: Acetaldehyde; 5: Acetone; 6: Toluene)"

### Trechos acrescentados na etapa 3 (extraídos dos mesmos PDFs)

> "Lemma 3 If k(·, ·) is measurable and Ex √k(x, x) < ∞ then µp ∈ H." (Gretton et al., 2012, §2.2, p. 727)

> "6. A Linear Time Statistic and Test" [...] "can be computed in linear time, and is an unbiased estimate of MMD²[F, p, q]" (Gretton et al., 2012, §6)

> "Note, however, that the rate of convergence of the squared, biased MMD estimate to its population value remains at 1/√m" (Gretton et al., 2012, §4)

> "Assumption 1 k(x, y) = ψ(x − y) where ψ is a bounded continuous real-valued positive definite function on M = Rd." / "Theorem 9 Suppose k satisfies Assumption 1. Then k is characteristic if and only if supp(Λ) = Rd, where Λ is defined as in (11)." (Sriperumbudur et al., 2010, p. 1533)

> "k(x, x′) = exp(−xᵀx/2σ²) exp(xᵀx′/σ²) exp(−(x′)ᵀx′/2σ²) (6.25) [...] Note that the feature vector that corresponds to the Gaussian kernel has infinite dimensionality." (PRML, §6.2, p. 296)

> "If we consider the slightly generalized kernel k(x, x′) = (xᵀx′ + c)² with c > 0, then the corresponding feature mapping φ(x) contains constant and linear terms as well as terms of order two." (PRML, §6.2)

> "these papers often assume either covariate shift q(x, y) = q(x)p(y|x) [15, 45, 49] or label shift q(x, y) = q(y)p(x|y) [7, 29, 38, 48, 56]." (Rabanser et al., 2019, §2, p. 2)

> "While off-the-shelf methods for kernel-based multivariate two-sample tests are appealing, they scale badly with dataset size and their statistical power is known to decay badly with high ambient dimension [37]." (Rabanser et al., 2019, p. 2)

> "We propose the following notion of fair alternatives - for two-sample testing as dimension increases, the Kullback Leibler (KL) divergence between the pairs of distributions should remain constant [...] For the aforementioned example of the Gaussians, the choice of (1, 0, 0, 0, ..., 0) turns out to be a fair alternative" (Reddi et al., 2014, §2.5)

### Desvios do plano na etapa 3

- MNIST × USPS saiu: a localização da mudança ficou com a testemunha (figuras em 1D e 2D) e com a MMD por gás, e a aula não depende do Hugging Face Hub.
- *Concept shift* ficou sem trecho literal: citado como Moreno-Torres et al. (2012), marcado na aula como não consultado.
- Reduzir a dimensão antes de testar não ajudou no gás (o teste nos 128 atributos teve o maior poder). A aula mostra o resultado como está e contrasta com o achado de Rabanser et al. em imagens.
- Pré-processamento: padronização com a metade 1a do lote 1 e truncamento em ±10 desvios (um valor do lote 2 chega a 15.025 desvios).

---

## Inferido ou a verificar

**Formulação nossa, com demonstração na aula (não copiada de fonte):** a proposição do nível do teste de permutação (resultado clássico; a referência usual é Lehmann & Romano, *Testing Statistical Hypotheses*, que não foi consultada); o caso de aquecimento com $\mathcal{F}$ linear; a leitura da testemunha como diferença de dois KDEs; a padronização por lote como alinhamento dos dois primeiros momentos por atributo.

**A verificar antes de entrar no `index.qmd`:**
- A página da UCI dá "January 2007 to February 2011 (36 months)", o que não fecha. A aula dirá só "36 meses".
- A mesma página diz "research purposes" na descrição e CC BY 4.0 na licença. Uso didático cabe nas duas; o arquivo não entra no repositório.
- O artigo original do dataset (Vergara et al., 2012, *Sensors and Actuators B*) não foi consultado. Detalhes dos sensores e dos 8 atributos por sensor saem só da página da UCI.
- Os três tipos de mudança (covariável, priori, conceito) estão sem trecho literal. Procurar a definição em Rabanser et al. (§2) ou baixar Moreno-Torres et al. (2012) antes de escrever o Bloco 5.
- Comportamento da MMD sob $H_1$ (normalidade assintótica): não citar sem localizar o enunciado em Gretton et al.
- Um valor de atributo no lote 2 chega a 14.757 desvios do lote 1. Decidir no setup entre cortar valores extremos e usar escala robusta, e declarar a escolha na aula.
- MNIST × USPS: carregamento testado, resultado não. Se a MMD em pixels entre os dois for trivial demais para ensinar algo, a parte sai.
- ESL não foi baixado (o servidor não respondeu) e não é usado nesta aula.
