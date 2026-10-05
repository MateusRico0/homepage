## Resumo — Aula 08

A aula formaliza matematicamente a **decomposição viés-variância** (*Bias-Variance Decomposition*) do erro quadrático médio esperado em regressão. Partindo da pergunta deixada em aberto na Aula 7 (como justificar teoricamente a escolha da intensidade de regularização $\lambda$), tratamos o modelo ajustado $\hat{f}(x; \mathcal{D})$ como uma variável aleatória condicionada ao conjunto de treinamento $\mathcal{D}$. Demonstramos analiticamente que o erro esperado decompõe-se exatamente em três componentes ortogonais: viés ao quadrado, variância do estimador e erro irredutível $\sigma^2$. Conectamos essa teoria com a regularização Ridge (provando o Teorema de Hoerl & Kennard sobre a redução de variância às custas de viés) e estabelecemos o vocabulário analítico indispensável para a Parte 3 do curso (Ensembles: Bagging como redutor de variância e Boosting como redutor de viés).

**Estratégia Pedagógica:** Estratégia B (Inside-Out com Problema-Fio) — Iniciamos com um problema-fio experimental sintético onde a função verdadeira $f(x)$ e o ruído $\sigma^2$ são perfeitamente conhecidos, permitindo calcular o viés e a variância exatos sobre múltiplas réplicas de conjuntos de dados $\mathcal{D}$. A partir dessa observação empírica, derivamos a teoria matemática rigorosa, generalizamos para o caso real (*California Housing*) com regularização Ridge, e fechamos com o diagnóstico prático via curvas de aprendizado.

**Datasets-fio:**
1. *Laboratório Sintético* ($f(x) = \sin(2\pi x)$ com ruído gaussiano $\epsilon \sim \mathcal{N}(0, \sigma^2)$): permite simular 100 conjuntos de treino independentes de tamanho $N=25$, ajustando modelos de complexidades variadas para visualizar e calcular as esperanças $\mathbb{E}_{\mathcal{D}}[\hat{f}(x)]$ e as variâncias exatas.
2. *California Housing* (`gvlassis/california_housing`): aplicação prática real, avaliando o tradeoff em função da força de regularização $\lambda$ no modelo linear e polinomial.

---

## Plano de aula — Aula 08 (carga horária: ~115–125 min)

1. **Revisão e Introdução** (~10 min) — Da Aula 7: $\lambda$ foi ajustado visualmente; o que significa "complexidade ótima"? Ideia central: o estimador como variável aleatória dependente de $\mathcal{D}$. Problema motivador no laboratório sintético. Pausa Ativa 1.
2. **Intuição — As Três Fontes de Erro** (~10 min) — O que é erro de aproximação estrutural (viés), o que é sensibilidade à amostra (variância) e o que é o limite informacional dos dados (erro irredutível $\sigma^2$).
3. **Bloco 1: A Decomposição Formal do EMSE** (~20 min) — Modelo gerador $y = f(x) + \epsilon$. Definição do estimador médio $\bar{f}(x) = \mathbb{E}_{\mathcal{D}}[\hat{f}(x; \mathcal{D})]$. Derivação algébrica passo a passo. Demonstração de que o termo cruzado anula-se identicamente sob a esperança. Pausa Ativa 2.
4. **Bloco 2: Complexidade de Hipóteses e o Ponto Ótimo** (~18 min) — Espaço de hipóteses $\mathcal{H}$ e dimensão polinomial. Dinâmica com o tamanho amostral $N$: demonstração, com a matriz chapéu $H$ (simétrica, idempotente, $\mathrm{tr}\,H=p$), de que $\frac1N\sum_n\text{Var}(\hat y_n)=\sigma^2p/N$ (desenho fixo); o viés estrutural não cai com $N$. Integração do erro sobre a distribuição marginal $p(x)$. Pausa Ativa 3.
5. **Bloco 3: Conexão com Regularização e MAP (Aula 7)** (~15 min) — Expressão analítica do viés e variância do estimador Ridge: $\mathbb{E}[\hat{\boldsymbol\beta}_{\text{Ridge}}] \neq \boldsymbol\beta^*$ e $\text{Cov}(\hat{\boldsymbol\beta}_{\text{Ridge}}) \prec \text{Cov}(\hat{\boldsymbol\beta}_{\text{OLS}})$. O Teorema de Hoerl & Kennard (1970): sempre existe $\lambda > 0$ que reduz o erro quadrático total. Pausa Ativa 4.
6. **Bloco 4: Curvas de Aprendizado e Diagnóstico Prático** (~25 min) — Definição operacional (grade de $N$, treino, validação, repetições). O que cada curva estima. Conta exata do otimismo do treino para OLS: $\mathbb{E}[\overline{\text{err}}]=B+\sigma^2(1-p/N)$, $\mathbb{E}[\text{Err}_{\text{in}}]=\sigma^2+B+\sigma^2p/N$, gap $2\sigma^2p/N$ (o viés se cancela). Forma típica e patamar $\sigma^2+B_\infty$; figura com graus 1, 3 e 10; figura do gap medido contra a teoria. Três perguntas de leitura, tabela sintoma → ação, cuidados práticos. Pausa Ativa 5.
7. **Fechamento** (~5 min) — Retomada das 5 perguntas centrais. O que fica em aberto (perda $0-1$ em classificação e o tradeoff multiplicativo). Ponte para a Parte 3 (Bagging como redutor de variância e Boosting como redutor de viés).

---

## Fontes usadas — Aula 08

### Fonte 1: Bishop, C. M. (2006), *Pattern Recognition and Machine Learning* (PRML), §3.2
**Uso pretendido:** Derivação analítica formal da decomposição do erro quadrático médio esperado em viés ao quadrado, variância e ruído intrínseco (§3.2, pp. 147–152), e o experimento canônico com $100$ conjuntos de treino de $f(x) = \sin(2\pi x)$.
**Trecho:**
> "The expected squared loss can be decomposed into the sum of three terms: a squared bias term, which represents the extent to which the average prediction over all data sets differs from the desired regression function; a variance term, which measures the extent to which the solutions for individual data sets vary around their average; and an irreducible noise term."

### Fonte 2: Hastie, T., Tibshirani, R., & Friedman, J. (2009), *The Elements of Statistical Learning* (ESL), Cap. 7 (§7.2–7.3)
**Uso pretendido:** Discussão sobre complexidade de modelos, erro de generalização (*expected test error*), estimativa via validação empírica e análise do trade-off sob regularização e dimensionalidade.
**Trecho:**
> "As model complexity of our procedure increases, the bias tends to drop, while the variance increases. There is typically an intermediate complexity that achieves minimum expected prediction error."

### Fonte 2b: ESL, §7.3 (p. 224), §7.4 (pp. 228–229) e §7.10.1 (p. 243)
**Uso pretendido:** variância média $\sigma^2p/N$ (eq. 7.12, demonstrada na aula com a matriz chapéu); erro dentro da amostra, otimismo e gap $2d\sigma^2/N$ (eqs. 7.18–7.24; a derivação com $I-H$ é nossa); curva de aprendizado e sua inclinação (Fig. 7.8).
**Trechos:**
> "While this variance changes with x0, its average (with x0 taken to be each of the sample values xi) is (p/N)σε², and hence [...] (7.12) the in-sample error."

> "This expression simplifies if ŷi is obtained by a linear fit with d inputs or basis functions. For example, Σ Cov(ŷi, yi) = dσε² (7.23) for the additive error model Y = f(X) + ε, and so Ey(Errin) = Ey(err) + 2 · (d/N) σε². (7.24)"

> "Figure 7.8 shows a hypothetical 'learning curve' for a classifier on a given task, a plot of 1 − Err versus the size of the training set N. [...] To summarize, if the learning curve has a considerable slope at the given training set size, five- or tenfold cross-validation will overestimate the true prediction error."

### Fonte 3: Hoerl, A. E. & Kennard, R. W. (1970), "Ridge Regression: Biased Estimation for Nonorthogonal Problems", *Technometrics*, 12(1), 55–67
**Uso pretendido:** Justificativa teórica rigorosa para a superioridade do estimador Ridge sobre o OLS via redução de variância e o teorema da existência de $\lambda > 0$ estritamente benéfico.
