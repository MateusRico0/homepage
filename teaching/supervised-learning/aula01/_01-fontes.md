# Fontes usadas — Aula 1

> Trechos literais preenchidos em 2026-08-09 a partir dos PDFs em
> `../fontes/prml.pdf` (Bishop, 2006) e `../fontes/dlfc.pdf` (Bishop &
> Bishop, 2024), agora linkados. Offset confirmado entre página impressa e
> página do arquivo PDF: **+20** para os dois livros (ex.: p. 14 impressa
> = página 34 do PDF). Cada trecho abaixo foi extraído diretamente da
> página citada, não reescrito de memória.
>
> Numeração de blocos atualizada para corresponder ao `00-plano-aula.md`
> reconciliado com o `02-aula.qmd` real e com a segunda rodada de ajuste
> (catálogo cortado, Beta simplificada, decisão ampliada) — Blocos 0–7, não
> ao roteiro original.

### Fonte 1: Bishop & Bishop (2024), §2.1.1, §2.1.3–2.1.5, pp. 25–31
**Uso pretendido:** exemplo motivador de triagem médica e derivação do teorema de Bayes (Bloco 3, segunda aparição do fenômeno — não é mais a abertura da aula).

**Trecho:**
> "Consider the problem of screening a population in order to provide early
> detection of cancer, and let us suppose that 1% of the population
> actually have cancer. [...] when the test is given to people who are
> free of cancer, 3% of them will test positive. [...] when the test is
> given to people who do have cancer, 10% of them will test negative."
> (p. 25)
>
> "We see that if a person is tested at random there is a roughly 4% chance
> that the test will be positive even though there is a 1% chance that
> they actually have cancer." (p. 30)
>
> "so that if a person is tested at random and the test is positive, there
> is a 23% probability that they actually have cancer." (p. 31)

---

### Fonte 2: Bishop & Bishop (2024), §2.2, §2.2.1, pp. 32–34
**Uso pretendido:** condições de normalização e não-negatividade de densidades; distinção densidade vs. probabilidade (Bloco 4).

**Trecho:**
> "We define the probability density p(x) over a continuous variable x to
> be such that the probability of x falling in the interval (x, x + δx) is
> given by p(x)δx for δx → 0." (p. 32)
>
> "Because probabilities are non-negative, and because the value of x must
> lie somewhere on the real axis, the probability density p(x) must
> satisfy the two conditions p(x) ⩾ 0 [and] ∫∞−∞ p(x) dx = 1." (p. 32)

---

### Fonte 3: Bishop (2006, PRML), §2.1.1, pp. 71–74
**Uso pretendido:** definição e galeria de formas da distribuição Beta (Bloco 5) — usada agora só como referência de formato/suporte, não para derivar o ajuste em aula.

**Trecho:**
> "We therefore choose a prior, called the beta distribution, given by
>
> Beta(μ|a, b) = [Γ(a + b)/Γ(a)Γ(b)] μ^(a−1)(1 − μ)^(b−1)  (2.13)
>
> where Γ(x) is the gamma function defined by (1.141), and the coefficient
> in (2.13) ensures that the beta distribution is normalized." (p. 71)

---

### Fonte 4: Bishop (2006, PRML), §1.5, §1.5.1, pp. 38–41
**Uso pretendido:** teoria da decisão, taxa de má-classificação, regra do posterior máximo (Bloco 3).

**Trecho:**
> "A mistake occurs when an input vector belonging to class C1 is assigned
> to class C2 or vice versa." (p. 39)
>
> "Thus, if p(x, C1) > p(x, C2) for a given value of x, then we should
> assign that x to class C1. [...] the minimum probability of making a
> mistake is obtained if each value of x is assigned to the class for
> which the posterior probability p(Ck|x) is largest." (p. 39–40)

---

### Fonte 5: Bishop (2006, PRML), §1.5.2–1.5.3, pp. 41–42
**Uso pretendido:** perda esperada com matriz de custo assimétrica; opção de rejeição (Bloco 7).

**Trecho:**
> "We can formalize such issues through the introduction of a loss
> function, also called a cost function, which is a single, overall
> measure of loss incurred in taking any of the available decisions or
> actions." (p. 41)
>
> "We can achieve this by introducing a threshold θ and rejecting those
> inputs x for which the largest of the posterior probabilities p(Ck|x) is
> less than or equal to θ." (p. 42)

---

### Fonte 6: Bishop & Bishop (2024), §5.2.1–5.2.3, pp. 139–143
**Uso pretendido:** tratamento moderno da taxa de má-classificação e da perda esperada (Bloco 7).

**Trecho:**
> "Clearly, to minimize p(mistake) we should arrange that each x is
> assigned to whichever class has the smaller value of the integrand in
> (5.20). [...] this result is illustrated for two classes and a single
> input variable x in Figure 5.5." (p. 140)
>
> "We can formalize such issues through the introduction of a loss
> function, also called a cost function, which is a single, overall
> measure of loss incurred in taking any of the available decisions or
> actions." (p. 141)

---

### Fonte 7: Bishop & Bishop (2024), §5.2.5, pp. 147–148
**Uso pretendido:** matriz de confusão, precisão, recall, taxa de falso positivo (Bloco 7). *Escrito em 2026-08-23 (achado numa auditoria do planejamento: tinha ficado de fora de todas as versões anteriores do arquivo, apesar de constar como "resolvido" aqui) — está no `index.qmd`, seção "Teoria da Decisão: Custo, Avaliação e Rejeição" § "Além da acurácia: matriz de confusão, precisão e recall".*

**Trecho:**
> "We can see that accuracy can be misleading if there are strongly
> imbalanced classes. In our cancer screening example, for instance, where
> only 1 person in 1,000 has cancer, a naive classifier that simply
> decides that nobody has cancer will achieve 99.9% accuracy and yet is
> completely useless." (p. 148)
>
> "Precision = N_TP/(N_TP+N_FP) [...] Recall = N_TP/(N_TP+N_FN) [...] False
> positive rate = N_FP/(N_FP+N_TN) [...] False discovery rate =
> N_FP/(N_FP+N_TP)" (p. 148, eqs. 5.30–5.33)

---

### Fonte 8: Bishop & Bishop (2024), §5.2.6, pp. 148–150
**Uso pretendido:** curva ROC, replotada a partir do mesmo sweep de limiar do Bloco 1 (Bloco 7). Mesmo status de resolução da Fonte 7 — escrito em 2026-08-23, seção "A curva ROC: o mesmo sweep do Bloco 1, replotado".

**Trecho:**
> "As the decision boundary [...] is moved from −∞ to ∞, the ROC curve is
> traced out and can then be generated by plotting the cumulative fraction
> of correct detection of cancer on the y-axis versus the cumulative
> fraction of incorrect detection on the x-axis." (p. 148)
>
> "One approach is to measure the area under the curve (AUC). A value of
> 0.5 for the AUC represents random guessing whereas a value of 1.0
> represents a perfect classifier." (p. 150)

---

### Fonte 9: Bishop (2006, PRML), §1.2, pp. 14–24 *(adicionada na reconciliação)*
**Uso pretendido:** regra da soma e regra do produto, base formal da aula a partir do Bloco 2.

**Trecho:**
> "With this more compact notation, we can write the two fundamental rules
> of probability theory in the following form.
>
> sum rule  p(X) = ∑Y p(X, Y)  (1.10)
> product rule  p(X, Y) = p(Y|X)p(X).  (1.11)" (p. 14)
>
> "p(Y|X) = p(X|Y)p(Y) / p(X)  (1.12)
>
> which is called Bayes' theorem and which plays a central role in pattern
> recognition and machine learning." (p. 15)

---

### Fonte 10: Bishop & Bishop (2024), §2.1.2, pp. 26–28 *(adicionada na reconciliação)*
**Uso pretendido:** tratamento moderno da regra da soma e do produto (Bloco 2).

**Trecho:**
> "With this more compact notation, we can write the two fundamental rules
> of probability theory in the following form:
>
> sum rule  p(X) = ∑Y p(X,Y)  (2.8)
> product rule  p(X,Y) = p(Y|X)p(X).  (2.9)" (p. 28)
>
> "p(Y|X) = p(X|Y)p(Y) / p(X),  (2.10)
>
> which is called Bayes' theorem and plays an important role in machine
> learning." (p. 28)

---

*(O catálogo de distribuições — Bernoulli, Binomial, Multinomial, Gaussiana,
Laplace, $t$ de Student, Exponencial, Uniforme — foi cortado da aula na
segunda rodada de ajuste, junto com a tabela de citações prováveis, mas não
confirmadas, que existia aqui para ele. A comparação Gaussiana vs. $t$ de
Student sobrevive como nota de robustez dentro do Bloco 5, sem citação de
página própria — é uma ilustração, não leitura obrigatória.)*

---

## Notas sobre as fontes

Primeiro, o livro *Deep Learning* de 2024 **não** cobre a distribuição
Beta — o Capítulo 3 vai direto de Bernoulli/binomial para a Gaussiana
multivariada. Todo o material sobre Beta deve vir do PRML §2.1.1.
Segundo, o PRML introduz a Beta como uma *priori conjugada sobre o
parâmetro* \(\mu\) de uma Bernoulli, não como densidade sobre dados
observados. Esta aula reaproveita a Beta como modelo de dados para
observações limitadas \(x \in [0,1]\). A matemática é idêntica; a
interpretação não é, e a diferença deve ser dita explicitamente em
aula, não deixada implícita.
