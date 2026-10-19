## Resumo — Aula 7

A aula sai do mundo linear da Aula 6 (autoencoder linear ≡ PCA; PPCA como modelo gerador linear-Gaussiano) e cobre duas extensões não lineares. (1) O *deep autoencoder*: por que a não linearidade rasa não basta (DLFC p. 565), onde ela precisa estar (no caminho de $\mathbf{z}$ até a reconstrução) e quando a flexibilidade compensa: compensa no MNIST, mas sobreajusta no Breast Cancer com $N=455$. (2) O *Variational Autoencoder* como PPCA não linear: o modelo gerador $p(\mathbf{z})p(\mathbf{x}\mid\mathbf{z},\mathbf{w})$, a posterior sem forma fechada, a inferência amortizada, o ELBO da Aula 5 especializado (reconstrução − KL, com a KL Gaussiana derivada), o papel de $\beta$ e $\sigma^2$ e o *reparameterization trick* (comparado ao estimador *score function*, com números).

**Pré-requisitos (dicionário de notações):** decomposição $\ln p=\mathcal{L}(q)+\mathrm{KL}(q\|p(\mathbf{H}\mid\mathbf{X}))$ e definição de KL (Aula 5); EM como alternância E/M (Aula 4); PPCA, $\mathbf{W}$, $\sigma^2$, $M$, autoencoder linear e o Teorema "ativação linear ⇒ subespaço de PCA" (Aula 6); *double-dipping* (Aula 5).

**Dataset-fio:** Breast Cancer Wisconsin (30 atributos, com divisão treino/teste 80/20) para o *deep AE*, e MNIST (`ylecun/mnist`, 20 000 imagens de treino e 2 000 de teste) para o gap generativo e o VAE. Um arco sintético em 2D isola o ponto geométrico (onde a não linearidade precisa estar).

**Estratégia Pedagógica:** A (Outside-In). O tema é um modelo: parte-se do que ele faz (comprimir em curva, gerar), chega-se à necessidade teórica (posterior intratável) e então à teoria formal (ELBO, KL fechada, reparametrização).

## Plano de aula — Aula 7 (carga horária: 90 min)

1. **Revisão e Introdução** (~10 min). Revisão da Aula 6 explicando o mecanismo: autoencoder linear ≡ PCA, PPCA com posterior Gaussiana fechada e a ressalva do DLFC sobre não linearidade rasa. Revisão da decomposição do ELBO (Aula 5). Problema Motivador: no MNIST com $M=2$, as reconstruções da PCA contra as do *deep AE*, com números. Pausa 1.
2. **Intuição — Curvar a Variedade** (~8 min). A hipótese da variedade (DLFC §16 e §6.1.3: dígitos transladados formam uma variedade não linear). Arco 2D com $M=1$: PCA, AE raso (tanh) e AE profundo. O raso empata com a PCA, e só o profundo curva. Diagrama TikZ do *deep AE* ($F_1$/$F_2$, DLFC Fig. 19.2–19.3).
3. **Bloco 1: O *Deep Autoencoder*** (~15 min). Definição formal. Proposição (decoder afim ⇒ reconstruções num subespaço afim de dimensão $\le M$), com prova, que explica a ressalva do DLFC. Limitações (otimização não convexa, $M$ fixado antes). Resultado no Breast Cancer: o erro de treino cai a um terço, mas o de teste piora (*double-dipping* da Aula 5). Variantes (*sparse*, *denoising*). Pausa 2. Transição: no MNIST a compressão funciona; pode-se então gerar?
4. **Bloco 2: O Gap Generativo** (~10 min). O mapa latente do AE no MNIST tem escala arbitrária, ilhas e buracos. Amostras decodificadas de uma Gaussiana ajustada aos códigos e interpolação 1→7. Diagnóstico: o objetivo do AE não contém $p(\mathbf{z})$ e não define $p(\mathbf{x})$. Pausa 3. Transição: falta um modelo gerador, que a PPCA já tinha.
5. **Bloco 3: O VAE como PPCA Não Linear** (~12 min). O modelo gerador (DLFC 16.80), com a PPCA como caso particular. A marginal (19.4) e a posterior (19.12) são intratáveis, ao contrário da PPCA (PRML 12.42). A inferência amortizada com encoder Gaussiano diagonal (19.13) e a analogia com o EM (DLFC Fig. 19.9): o passo E deixa de ser exato. Pausa 4.
6. **Bloco 4: O ELBO do VAE** (~15 min). Derivação a partir da Aula 5: $\mathcal{L}_n=\mathbb{E}_q[\ln p(\mathbf{x}_n\mid\mathbf{z})]-\mathrm{KL}(q\|p(\mathbf{z}))$. A verossimilhança Gaussiana leva a MSE$/(2\sigma^2)$. Teorema da KL Gaussiana em forma fechada, com prova e visualização de $\tfrac12(\mu^2+s^2-1-\ln s^2)$. O $\beta$ e a equivalência $\beta\leftrightarrow\sigma^2$. Experimento com $\beta\in\{0,1,20\}$ ($\sigma\to0$ sem KL; colapso com $\beta$ grande). A folga ELBO vs. $\ln p(\mathbf{x})$ estimada por amostragem por importância. Pausa 5.
7. **Bloco 5: O *Reparameterization Trick* e o VAE Treinado** (~15 min). O problema: o gradiente de uma esperança sob uma distribuição que depende de $\boldsymbol\phi$ (DLFC Fig. 19.10). Estimador *score function* (DLFC Ex. 19.1), com prova. Lema da reparametrização e estimador *pathwise*. Variância medida no VAE treinado (desvio-padrão dezenas de vezes menor). Algoritmo de treino. Resultados: grade decodificada, amostras de $p(\mathbf{z})$, interpolação 1→7, borrão. Pausa 6.
8. **Fechamento** (~5 min). As 4 perguntas. O que fica em aberto: borrão, posterior agregada ≠ priori, *posterior collapse*, escolha de $M$, difusão como VAE hierárquico. Ponte para a Aula 8: o mapa 2D do VAE é subproduto da reconstrução e espreme as classes num disco. Para visualizar, otimiza-se o mapa diretamente (MDS, t-SNE) e surge o *crowding problem*.

## Fontes usadas — Aula 7

### Fonte 1: DLFC, §19.1.1, p. 565
**Uso pretendido:** ressalva de que a não linearidade rasa não escapa da PCA (Revisão, Intuição, Bloco 1).
**Trecho:**
> "It might be thought that the limitations of a linear manifold could be overcome by using nonlinear activation functions for the hidden units in the network in Figure 19.1. However, even with nonlinear hidden units, the minimum error solution is again given by the projection onto the principal component subspace (Bourlard and Kamp, 1988)."

### Fonte 2: DLFC, §19.1.2, pp. 565–566
**Uso pretendido:** definição do *deep autoencoder*, interpretação $F_1$/$F_2$ e limitações (Bloco 1).
**Trecho:**
> "The situation is different, however, if additional nonlinear layers are included in the network." […] "Such a network effectively performs a nonlinear form of PCA. It has the advantage of not being limited to linear transformations, although it contains standard PCA as a special case. However, training the network now involves a nonlinear optimization, since the error function (19.1) is no longer a quadratic function of the network parameters. Computationally intensive nonlinear optimization techniques must be used, and there is the risk of finding a sub-optimal local minimum of the error function. Also, the dimensionality of the subspace must be specified before training the network."

### Fonte 3: DLFC, Cap. 16 (introdução), p. 496
**Uso pretendido:** hipótese da variedade com dígitos transladados (Intuição).
**Trecho:**
> "Note that the manifold will be nonlinear because, for instance, if we translate the digit past a particular pixel, that pixel value will go from zero (white) to one (black) and back to zero again, which is clearly a nonlinear function of the digit position."

### Fonte 4: DLFC, §19.1, p. 564
**Uso pretendido:** limitação do AE como gerador (Bloco 2).
**Trecho:**
> "Simple autoencoders are rarely used directly in modern deep learning, as they do not provide semantically meaningful representations in the latent space and they are not able directly to generate new examples from the data distribution."

### Fonte 5: DLFC, §19.1.3–19.1.4, pp. 566–567
**Uso pretendido:** variantes *sparse* e *denoising* (Bloco 1).
**Trecho:**
> "Instead of limiting the number of nodes in one of the hidden layers in the network, an alternative way to constrain the internal representation is to use a regularizer to encourage a sparse representation, leading to a lower effective dimensionality." […] "An alternative approach, that also forces the model to discover interesting internal structure in the data, is to use a denoising autoencoder (Vincent et al., 2008)."

### Fonte 6: DLFC, §16.4.1, pp. 522–523
**Uso pretendido:** modelo gerador não linear e por que é preciso ruído em $p(\mathbf{x}\mid\mathbf{z})$ (Bloco 3).
**Trecho:**
> "However, one problem with this framework is that it assigns zero probability density to any data vector that does not lie exactly on the manifold" […] "If, for example, x comprises a vector of continuous variables then we can choose the conditional distribution to be a Gaussian: p(x|z, w) = N (x|g(z, w), σ2 I) (16.80)"

### Fonte 7: PRML, §12.2, p. 573
**Uso pretendido:** a posterior da PPCA é Gaussiana fechada, eq. (12.42) (Revisão, Bloco 3).
**Trecho:**
> "As well as the predictive distribution p(x), we will also require the posterior distribution p(z|x), which can again be written down directly using the result (2.116) for linear-Gaussian models" […] "Note that the posterior mean depends on x, whereas the posterior covariance is independent of x."

### Fonte 8: DLFC, §19.2, pp. 569–571
**Uso pretendido:** as três ideias do VAE e a intratabilidade da posterior (Bloco 3).
**Trecho:**
> "There are three key ideas in the VAE: (i) use of the evidence lower bound (ELBO) to approximate the likelihood function, leading to a close relationship to the EM algorithm, (ii) amortized inference in which a second model, the encoder network, is used to approximate the posterior distributions over latent variables in the E step, rather than evaluating the posterior distribution for each data point exactly, and (iii) making the training of the encoder model tractable using the reparameterization trick." […] "The numerator is straightforward to evaluate for our deep generative model. However, we see that the denominator is given by the likelihood function, which as we have already noted, is intractable."

### Fonte 9: DLFC, §19.2.1, pp. 572–573
**Uso pretendido:** inferência amortizada e a folga residual (Blocos 3 e 4).
**Trecho:**
> "In the variational autoencoder, instead of trying to evaluate a separate posterior distribution p(zn |xn , w) for each of the data points xn individually, we train a single neural network, called the encoder network, to approximate all these distributions. This technique is called amortized inference" […] "A key difference compared to EM is that, for a given value of w, optimizing with respect to the parameters φ of the encoder does not in general reduce the Kullback-Leibler divergence to zero, because the encoder network is not a perfect predictor of the posterior latent distribution and so there is a residual gap between the lower bound and the true log likelihood."

### Fonte 10: DLFC, §19.2.2, pp. 574–575
**Uso pretendido:** forma do ELBO por ponto (19.14), KL fechada (19.15), o problema do gradiente e a reparametrização (Blocos 4 e 5).
**Trecho:**
> "the gradient with respect to φ is problematic because changes to φ will change the distribution q(zn |xn , φ) from which the samples are drawn and yet these samples are fixed values so that we do not have a way to obtain the derivatives of these samples with respect to φ." […] "The reparameterization trick can be extended to other distributions but is limited to continuous variables. There are techniques to evaluate gradients directly without the reparameterization trick (Williams, 1992), but these estimators have high variance, and so reparameterization can also be viewed as a variance reduction technique."

**Nota de leitura:** a eq. (19.18) do DLFC está impressa como $z_{nj}^{(l)}=\mu_j\epsilon_{nj}+\sigma_j^2$ (também no Algoritmo 19.1). A forma correta é $\mu_j+\sigma_j\epsilon_{nj}$, consistente com (19.17) e com o texto depois de (19.19). Na p. 576, "the first term in the ELBO (19.14) encourages the encoder distribution q(z|x, φ) to be close to the prior" refere-se ao termo KL, que é o segundo. As notas sinalizam as duas.

### Fonte 11: DLFC, §19.2.2, pp. 576–577
**Uso pretendido:** *posterior collapse* e o coeficiente $\beta$ (Bloco 4).
**Trecho:**
> "When training VAEs, a problem can arise in which the variational distribution q(z|x, φ) converges to the prior distribution p(z) and therefore becomes uninformative because it no longer depends on x. In effect the latent code is ignored. This is known as posterior collapse." […] "Both problems can be addressed by introducing a coefficient β in front of the first term in (19.14) to control the regularization effectiveness of the Kullback–Leibler divergence, where typically β > 1 (Higgins et al., 2017)."

### Fonte 12: DLFC, Cap. 20 (introdução), p. 582
**Uso pretendido:** O Que Fica em Aberto (difusão como VAE hierárquico).
**Trecho:**
> "Diffusion models can be viewed as a form of hierarchical variational autoencoder in which the encoder distribution is fixed, and defined by the noise process, and only the generative distribution is learned (Luo, 2022)."

### Resultados inferidos (não copiados do livro)
- A proposição "decoder afim ⇒ reconstruções num subespaço afim de dimensão $\le M$" é um argumento elementar que explica *por que* a ressalva da Fonte 1 vale. Não é a prova de Bourlard & Kamp (que trata do mínimo global), e as notas sinalizam isso.
- A equivalência entre $\beta$ e $\sigma^2$ (os minimizadores dependem só do produto $\beta\sigma^2$) é derivada nas notas, não citada.
- A estimativa de $\ln p(\mathbf{x})$ por amostragem por importância usa a identidade $p(\mathbf{x})=\mathbb{E}_{q}[p(\mathbf{x},\mathbf{z})/q(\mathbf{z}\mid\mathbf{x})]$, demonstrada em uma linha nas notas.
