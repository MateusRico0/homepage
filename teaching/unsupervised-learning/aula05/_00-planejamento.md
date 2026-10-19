## Resumo — Aula 5

Versão nova da Aula 5 (a Aula 5 original é mantida intacta — esta é uma
segunda versão, mais ambiciosa, do mesmo tema). Cobre seleção Bayesiana
de modelos como princípio geral (evidência, Navalha de Occam orgânica),
o GMM Bayesiano completo (priori Normal-Wishart em $\mu,\Sigma$ **e**
Dirichlet em $\pi$ — diferente da Aula 5 original, que só dava priori a
$\pi$), a decomposição do ELBO variacional resultante, validação
empírica via verossimilhança preditiva held-out (ELPD) com discussão
explícita do viés de otimismo/*double-dipping*, métricas geométricas
unificadas (Silhueta + Índice de Dunn, com adaptação de Silhueta via
$k$-ésimo vizinho para DBSCAN), e Posterior Predictive Checks
**quantitativos** (projeções aleatórias + teste KS, MMD com kernel
RBF) — versão mais rigorosa do PPC qualitativo da Aula 5 original.

**Pré-requisitos:** EM clássico e GMM (Aula 4); a própria Aula 5
original não é pré-requisito (esta aula é autocontida e redefine KL/
ELBO do zero).

**Continuidade de dataset:** mesmo problema-fio das Aulas 3–5 —
Breast Cancer Wisconsin, atributos `radius_worst` e
`concave points_worst`, padronizados. Contraexemplo de forma: duas
"luas" (`make_moons`), mesmo de antes.

**Estratégia Pedagógica:** Estratégia A (*Outside-In*) — parte do
limite prático do EM clássico (Aula 4) e sobe ao formalismo Bayesiano,
depois volta à prática (validação empírica, PPC).

## Plano de aula — Aula 5 (carga horária: ~135min, aula estendida)

1. **Revisão e Introdução** (~12 min) — EM clássico não penaliza
   complexidade; log-verossimilhança de treino nunca cai em $K$;
   pergunta central de seleção de modelos.
2. **Bloco 1 — Seleção Bayesiana de Modelos** (~20 min). Reformado em
   2026-10-07, para não atropelar o ELBO:
   - *Abertura:* Bayes sobre estruturas em log, com os três termos
     visíveis (evidência, priori, normalizador); a priori nunca some
     (uniforme = constante comum). A evidência embute Occam. A
     intratabilidade fica concreta: $K^N$ termos, $2^{569}\approx10^{171}$,
     com $\theta$ integrado acoplando os pontos. Callout de estratégia:
     construir $\mathcal L_m(q)\le\ln p(\mathbf X\mid\mathcal M_m)$ e
     comparar $\mathcal L_m(q)+\ln p(\mathcal M_m)$.
   - *Digressão: KL.* Definição, forma de esperança, não simetria com
     figura (p bimodal, q num modo vs. q larga; PRML Fig. 10.3) e Gibbs
     com prova.
   - *O ELBO.* $\mathcal L_m$ **derivado** a partir de
     $\ln p(\mathbf X\mid\mathcal M_m)$ (seis passos), teorema e
     corolário, por que é calculável, a priori de volta
     ($q(\mathcal M_m)\propto p(\mathcal M_m)e^{\mathcal L_m}$, PRML
     10.36), otimizar em $q$ (dois produtos), as duas KLs (priori =
     termo do objetivo; posterior = folga) e a ressalva do *proxy*.
3. **Bloco 2 — GMM Bayesiano: a Mecânica das Prioris** (~20 min) —
   $\mathbf H=(\mathbf Z,\pi,\mu,\Sigma)$ inteiro dentro do tratamento
   variacional; Normal-Wishart barra o colapso de $\Sigma_k$; Dirichlet
   com $\alpha_0$ fixo neutro poda componentes via comparação de ELBO
   entre $K$'s (não mais variando $\alpha_0$, como na Aula 5 antiga).
4. **Bloco 3 — Dissecando o ELBO Variacional** (~15 min) — decomposição
   ajuste−KL especializada a este $\mathbf H$; ELBO empírico sobe e
   desce em função de $K$ (ao contrário da verossimilhança crua).
5. **Bloco 4 — Teoria Preditiva e Validação Empírica** (~30 min) — ELPD
   como alvo estatístico verdadeiro; viés de treino (*double-dipping*);
   estimador Monte Carlo via conjunto de validação; três razões para o
   ELBO de treino não bastar (folga variacional, má especificação,
   comparação universal); Silhueta + Dunn (DBSCAN adaptado via
   $k$-NN) na validação.
6. **Bloco 5 — PPC Quantitativo** (~25 min) — ponto cego dos escalares;
   projeções aleatórias + KS; MMD com kernel RBF (e o papel da largura
   de banda); contraexemplo das duas luas, quantificado.
7. **Fechamento** (~8 min) — retomada das perguntas; ponte para a
   Aula 6 (o ELBO reaparece na PPCA/VAE).

## Fontes usadas — Aula 5

### Trechos literais do PRML (`_fontes/prml.pdf`), usados no Bloco 1 reformado

- **§1.6.1, p. 55** (não simetria da KL): "Note that it is not a
  symmetrical quantity, that is to say KL(p‖q) ≢ KL(q‖p)."
- **§10.1, p. 463** (decomposição e otimização em $q$): "As before, we
  can maximize the lower bound L(q) by optimization with respect to the
  distribution q(Z), which is equivalent to minimizing the KL
  divergence. If we allow any possible choice for q(Z), then the maximum
  of the lower bound occurs when the KL divergence vanishes, which
  occurs when q(Z) equals the posterior distribution p(Z|X)."
- **§10.1.2, p. 468** (assimetria, Fig. 10.3): "Thus minimizing this
  form of KL divergence leads to distributions q(Z) that avoid regions
  in which p(Z) is small. Conversely, the Kullback-Leibler divergence
  KL(p‖q) is minimized by distributions q(Z) that are nonzero in regions
  where p(Z) is nonzero."
- **§10.1.4, pp. 473–474** (priori sobre modelos): "we may also wish to
  compare a set of candidate models, labelled by the index m, and having
  prior probabilities p(m). Our goal is then to approximate the
  posterior probabilities p(m|X)" […] "We can maximize Lm with respect
  to the distribution q(m) using a Lagrange multiplier, with the result
  q(m) ∝ p(m) exp{Lm}. (10.36)"

Nota: o parágrafo abaixo, que diz não haver PDF disponível, foi escrito
antes de o `prml.pdf` estar em `_fontes/`; as citações do Bloco 1 agora
são literais.

Disciplina sem `_fontes/` PDF específico para este conteúdo (não há um
capítulo único do PRML fisicamente disponível localmente cobrindo
GMM Bayesiano completo — §10.1–10.2 é a referência, citada por número
de seção/equação a partir do conhecimento consolidado do livro, não de
um trecho literal copiado de PDF). Citações adicionais, fora do padrão
usual desta disciplina (mesmo desvio já registrado na Aula 5 original):

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*.
  Springer. §3.4 (evidência/Occam), §10.1 (Variational Bayes geral),
  §10.2 (GMM Bayesiano — Dirichlet + Normal-Wishart, atualizações
  variacionais).
- Dunn, J. C. (1974). "Well-Separated Clusters and Optimal Fuzzy
  Partitions." *Journal of Cybernetics*, 4(1), 95–104.
- Gretton, A., Borgwardt, K. M., Rasmussen, C. J., Schölkopf, B., &
  Smola, A. (2012). "A Kernel Two-Sample Test." *Journal of Machine
  Learning Research*, 13, 723–773.
- Vehtari, A., & Ojanen, J. (2012). "A Survey of Bayesian Predictive
  Methods for Model Assessment, Selection and Comparison." *Statistics
  Surveys*, 6, 142–228.
- Massey, F. J. (1951). "The Kolmogorov-Smirnov Test for Goodness of
  Fit." *Journal of the American Statistical Association*, 46(253),
  68–78.
- Rousseeuw, P. J. (1987) e Gelman, A. & Rubin, D. B. (1996) —
  reaproveitadas da Aula 5 original (Silhueta e PPC qualitativo).

Todos os números apresentados na aula (log-verossimilhanças, ELBOs,
Silhueta/Dunn, estatísticas KS/MMD) foram computados diretamente do
Breast Cancer Wisconsin (mesmos 2 atributos padronizados das Aulas
3–5) e do dataset sintético de duas luas, nunca fabricados — ver
`index.qmd` para o código completo.
