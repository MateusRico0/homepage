# Fontes usadas — Aula 4

> Trechos literais extraídos em 2026-08-24 de `../fontes/esl.pdf`
> (Hastie, Tibshirani & Friedman, *The Elements of Statistical Learning*,
> 2ª ed., 12ª impressão — "ESLII_print12_toc.pdf"). Offset confirmado
> entre página impressa e página do arquivo PDF: **+19** (ex.: p. 241
> impressa = página 260 do PDF) — diferente do offset +20 já usado para
> PRML/DLFC nesta disciplina; confirmado lendo o número impresso em
> várias páginas ao redor do Capítulo 7, não assumido por analogia com
> os outros dois livros. Esta é a primeira aula da disciplina a citar
> ESL (`_progresso.md` já registrava o livro como disponível, mas nunca
> citado até agora).

### Fonte 1: Hastie, Tibshirani & Friedman (ESL), §7.10, p. 241
**Uso pretendido:** definição de validação cruzada como estimador do erro esperado fora da amostra (Bloco 2/4).

**Trecho:**
> "Probably the simplest and most widely used method for estimating
> prediction error is cross-validation. This method directly estimates
> the expected extra-sample error Err = E[L(Y, fˆ(X))], the average
> generalization error when the method fˆ(X) is applied to an
> independent test sample from the joint distribution of X and Y."

---

### Fonte 2: Hastie, Tibshirani & Friedman (ESL), §7.10.1, pp. 241–242
**Uso pretendido:** mecânica do k-fold, a fórmula do estimador, e os valores típicos de $K$ (Bloco 4/5).

**Trecho:**
> "K-fold cross-validation uses part of the available data to fit the
> model, and a different part to test it. [...] For the kth part, we fit
> the model to the other K − 1 parts of the data, and calculate the
> prediction error of the fitted model when predicting the kth part of
> the data. [...]
>
> CV(fˆ) = (1/N) Σ L(yi, fˆ₋κ(i)(xi)).
>
> Typical choices of K are 5 or 10 [...]. The case K = N is known as
> leave-one-out cross-validation." (pp. 241–242)

---

### Fonte 3: Hastie, Tibshirani & Friedman (ESL), §7.10.1, pp. 242–243
**Uso pretendido:** viés e variância do próprio estimador de CV em função de $K$ (Bloco 5).

**Trecho:**
> "What value should we choose for K? With K = N, the cross-validation
> estimator is approximately unbiased for the true (expected) prediction
> error, but can have high variance because the N 'training sets' are so
> similar to one another." (p. 242–243)

---

### Fonte 4: Hastie, Tibshirani & Friedman (ESL), §7.10.2, pp. 245–246
**Uso pretendido:** o exemplo canônico de vazamento de dados — selecionar atributos antes do split (Bloco 8, Armadilhas).

**Trecho:**
> "Consider a scenario with N = 50 samples in two equal-sized classes,
> and p = 5000 quantitative predictors [...] that are independent of the
> class labels. The true (test) error rate of any classifier is 50%. We
> carried out the above recipe, choosing in step (1) the 100 predictors
> having highest correlation with the class labels, and then using a
> 1-nearest neighbor classifier [...]. Over 50 simulations from this
> setting, the average CV error rate was 3%. This is far lower than the
> true error rate of 50%. [...] The problem is that the predictors have
> an unfair advantage, as they were chosen in step (1) on the basis of
> all of the samples."

---

### Fonte 5: Hastie, Tibshirani & Friedman (ESL), final de §7.10.3, p. 249
**Uso pretendido:** a importância de reportar o desvio-padrão da estimativa de CV, não só a média (Bloco 8, Armadilhas).

**Trecho:**
> "The results of applying five-fold cross-validation to each of 50
> simulated datasets [...]. As we would hope, the average cross-validation
> error is around 50%, which is the true expected prediction error for
> this classifier. [...] On the other hand, there is considerable
> variability in the error, underscoring the importance of reporting the
> estimated standard error of the CV estimate."

---

### Fonte 6: Hastie, Tibshirani & Friedman (ESL), §7.11, pp. 249–250
**Uso pretendido:** definição geral do Bootstrap e a diferença de propósito frente à validação cruzada (Bloco 7).

**Trecho:**
> "The bootstrap is a general tool for assessing statistical accuracy.
> [...] the bootstrap seeks to estimate the conditional error ErrT, but
> typically estimates well only the expected prediction error Err. [...]
> The basic idea is to randomly draw datasets with replacement from the
> training data, each sample the same size as the original training set.
> This is done B times [...], producing B bootstrap datasets [...]. From
> the bootstrap sampling we can estimate any aspect of the distribution
> of S(Z), for example, its variance,
>
> V̂ar[S(Z)] = (1/(B−1)) Σᵦ (S(Z*ᵇ) − S̄*)²."

---

## Notas sobre as fontes

- PRML e DLFC não têm um capítulo dedicado à mesma profundidade sobre
  validação cruzada e Bootstrap (PRML trata `cross-validation` de forma
  breve em §1.3, p. 32–33, sem a mesma formalização); por isso esta aula
  se apoia primariamente em ESL §7.10–7.11, o tratamento de referência
  do tema.
- O exemplo do "jeito errado de fazer CV" (Fonte 4) é reaproveitado quase
  literalmente como o núcleo do bloco de armadilhas — números (N=50,
  p=5000, erro real 50%, CV errada 3%) preservados do livro, não
  inventados.
- O dataset-fio da aula (Breast Cancer Wisconsin) não é discutido no
  livro — é a aplicação nossa da teoria de ESL a um problema real,
  sinalizado como tal no `index.qmd`.
