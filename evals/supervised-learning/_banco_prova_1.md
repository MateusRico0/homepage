# Banco de Questões para a Prova — Aprendizado Supervisionado (Aulas 1-4)
Data: 2026-09-21
Status: Privado (Não publicado via Quarto)

---

## Parte 1: Seleção de Exercícios Existentes (Blocos de 4 itens)

### Questão 1 — Distribuições, priori e fronteira de decisão (L1)
- □ Se as duas classes fossem igualmente frequentes ($\pi_A=\pi_B=0{,}5$), o cruzamento das conjuntas passaria a coincidir exatamente com o cruzamento das condicionais $T_{COND}$.
- □ No limite em que $\pi_A \to 1$, o cruzamento das conjuntas $T_{CONJ}$ tende a se afastar cada vez mais do cruzamento das condicionais $T_{COND}$, na direção do território de B.
- □ Considere uma triagem de segurança em aeroportos em que $99\%$ dos passageiros não representam ameaça. Mesmo com condicionais simétricas e bem separadas, cortar sempre no cruzamento das CONDICIONAIS (ignorando essa priori $99\%/1\%$) não é a regra de decisão ótima sob perda 0-1.
- □ Como o cruzamento das condicionais não depende das prioris, conclui-se que a taxa de erro total (Tipo I + Tipo II, ponderados pelas prioris) também não depende de onde as prioris colocam o peso relativo entre os dois tipos de erro.

### Questão 2 — Teorema de Bayes e um teste diagnóstico (L1)
- □ No limite em que a prevalência da doença tende a zero, mantendo sensibilidade e falso positivo fixos em $0{,}90$ e $0{,}03$, a posteriori $p(D\mid+)$ também tende a zero.
- □ Se a prevalência da doença fosse $50\%$ em vez de $1\%$ (mantendo sensibilidade $0{,}90$ e falso positivo $0{,}03$), a posteriori $p(D\mid+)$ passaria a ser maior que $90\%$.
- □ Num teste de triagem usado em campanhas de vacinação em massa, com prevalência ainda menor (1 em 10.000) e sensibilidade e especificidade excelentes (99% cada), a proporção de positivos que são realmente doentes seria ainda menor do que no valor de referência acima (${\approx}23{,}3\%$).
- □ Como a evidência $p(+)$ é definida como $\sum_k p(+\mid\mathcal{C}_k)p(\mathcal{C}_k)$, ela representa a probabilidade de um resultado positivo vindo especificamente da classe doente.

### Questão 3 — A distribuição Beta e detecção de anomalias (L1)
- □ No limite em que $a\to\infty$ e $b\to\infty$ mantendo $a/(a+b)$ constante, a distribuição Beta se concentra cada vez mais estreitamente em torno de sua média, tendendo a uma distribuição degenerada (variância $\to 0$).
- □ Se o limiar de decisão for definido como o percentil $99$ da densidade $\operatorname{Beta}(x\mid a,b)$ ajustada aos escores normais, trocar esse limiar pelo percentil $95$ aumentaria a taxa de detecção de anomalias verdadeiras, mas também aumentaria a taxa de falsos positivos entre os escores normais.
- □ Num sistema de recomendação que modela a taxa de cliques (CTR) de cada anúncio (um valor em $[0,1]$), a Beta seria uma escolha tão razoável quanto para modelar os escores de anomalia descritos.
- □ A distribuição Beta é inadequada para modelar escores de anomalia normalizados em $[0,1]$ porque sua densidade não pode ser ajustada via máxima verossimilhança (MLE).

### Questão 4 — A maldição da dimensionalidade (L2)
- □ No limite em que $d\to\infty$, mantendo $M=10$ fixo por eixo, o número de células $M^d$ cresce mais rápido do que qualquer conjunto de dados de tamanho polinomial em $d$.
- □ Se, em vez de $M$ células por eixo, usássemos apenas $M=2$ (uma grade binária), o problema de crescimento exponencial em $d$ desapareceria.
- □ Num problema de reconhecimento de imagens em que cada pixel é uma dimensão (por exemplo, $28\times28=784$ dimensões), um histograma multidimensional ingênuo seria ainda mais inviável do que o exemplo de $d=15$ descrito acima.
- □ Como o problema vem do crescimento exponencial de $M^d$, comprar mais capacidade computacional (mais GPUs) resolveria a maldição da dimensionalidade.

### Questão 5 — Teoria da decisão: risco e regra de Bayes (L2)
- □ No limite em que a matriz de perda $L$ se torna a perda 0-1, a regra de Bayes coincide exatamente com a regra do posterior máximo.
- □ Se a matriz de perda $L$ fosse alterada para ter custos muito diferentes entre os tipos de erro, mas a posteriori $p(\mathcal{C}_k\mid\mathbf{x})$ permanecesse a mesma, a regra de Bayes mudaria a fronteira de decisão.
- □ O risco de Bayes $R^\star$ é o menor risco esperado possível, calculado supondo que o modelo usado para $p(\mathcal{C}_k\mid\mathbf{x})$ é o verdadeiro processo gerador dos dados.
- □ A regra do posterior máximo é a regra ótima de decisão para qualquer matriz de perda $L$ arbitrária, desde que as prioris sejam conhecidas.

### Questão 6 — Árvores como estimação não-paramétrica (L3)
- □ Se, em vez de cortes alinhados aos eixos, uma árvore pudesse usar cortes ao longo de qualquer direção linear (hiperplanos oblíquos), mantendo a mesma lógica gulosa, ela deixaria de ser um modelo não-paramétrico.
- □ Se o número mínimo de pontos por folha for reduzido a $1$ e a profundidade máxima não for limitada, o número de parâmetros efetivos de uma árvore pode crescer até se igualar ao número de pontos de treino $N$.
- □ Suponha que se queira usar uma árvore para modelar a distribuição conjunta completa $p(\mathbf{x}, y)$, não só a fronteira de decisão. Isso é possível diretamente com o mesmo procedimento guloso descrito acima, sem nenhuma modificação.
- □ Numa árvore com uma única folha (nenhum corte realizado), a estimativa em classificação se reduz à proporção empírica de cada classe $k$ na amostra de treino inteira (a priori marginal $\hat\pi_k$), ignorando completamente $\mathbf{x}$.

### Questão 7 — O estimador ótimo numa folha de regressão (L3)
- □ Se, em vez de uma verossimilhança gaussiana, assumíssemos uma verossimilhança de Laplace para os alvos de uma folha, o estimador de máxima verossimilhança de $y_\tau$ deixaria de ser a média amostral e passaria a ser a mediana amostral.
- □ Se todos os $N_\tau$ alvos de uma folha forem idênticos entre si (variância zero), o valor mínimo de $Q_\tau$ é zero, e a log-verossimilhança gaussiana correspondente, no limite $\sigma^2\to 0$, tende a $+\infty$.
- □ Uma folha com $N_\tau=1$ ainda define um $Q_\tau$ mínimo bem definido e igual a zero, mas a variância amostral desse único ponto não pode ser estimada de forma não-enviesada.
- □ Como $Q_\tau$ e a variância amostral $\hat\sigma^2_\tau = Q_\tau/N_\tau$ diferem apenas por uma constante multiplicativa, a minimização de $Q_\tau$ é equivalente a maximizar a variância amostral da folha.

### Questão 8 — O Viés do Erro de Treino (L4)
- □ No limite em que a profundidade da árvore não é limitada e há um ponto de treino distinto por folha, o erro de treino tende a $0\%$, independentemente de quão complexa seja a fronteira real entre as classes.
- □ Se a árvore de profundidade 15 tem a mesma acurácia de teste que a árvore de profundidade 6, isso prova que a árvore mais profunda é necessariamente pior no teste do que uma menos profunda.
- □ Num modelo de previsão de preços de imóveis ajustado com um polinômio de grau muito alto (que passa exatamente por todos os pontos de treino), o erro de treino seria próximo de zero, mas isso não garante nada sobre o erro em imóveis não vistos.
- □ Como o erro de treino tende a subestimar o erro de generalização, conclui-se que um modelo com erro de treino alto necessariamente generaliza melhor do que um com erro de treino baixo.

### Questão 9 — Train/Validation/Test (L4)
- □ No limite em que o conjunto de teste é consultado repetidas vezes durante o ajuste de hiperparâmetros, a estimativa final de desempenho no teste se torna tão otimista quanto medir no próprio conjunto de treino.
- □ Se o conjunto de validação, em vez de do teste, fosse consultado repetidamente para escolher hiperparâmetros, isso não teria custo estatístico algum, pois validação existe exatamente para ser consultada quantas vezes for preciso.
- □ Numa competição de ciência de dados, o "leaderboard público" funciona como um conjunto de validação consultável repetidamente; competidores que otimizam demais para ele costumam piorar no leaderboard privado.
- □ Como o conjunto de treino é usado para ajustar os parâmetros do modelo, conclui-se que o conjunto de validação é usado para ajustar os dados do modelo (limpá-los ou transformá-los), não seus hiperparâmetros.

### Questão 10 — O Procedimento k-fold (L4)
- □ No limite em que $k=N$ (LOOCV), cada fold de validação contém exatamente um único ponto.
- □ Se, em vez de treinar $k$ modelos diferentes, k-fold CV usasse um único modelo treinado com todos os dados para avaliar cada fold de validação, a estimativa deixaria de simular uma amostra de teste verdadeiramente independente do ajuste.
- □ Num estudo médico com pacientes de 10 hospitais diferentes, se cada fold de uma 5-fold CV misturar aleatoriamente pacientes de todos os hospitais, a CV pode superestimar o desempenho num hospital totalmente novo.
- □ O erro de validação cruzada é sempre um estimador não-enviesado do risco esperado $R(\theta)$, independentemente do valor de $k$ escolhido.

---

## Parte 2: Novas Questões Propostas (Blocos de 4 itens)

### Questão 11 — Custos Assimétricos e Decisão (L1)
- □ Se o custo de um Falso Negativo for 100 vezes maior que o de um Falso Positivo, a fronteira de decisão ótima se desloca para aumentar a região da classe "doente/anômala", reduzindo a taxa de escapes.
- □ Sob perda 0-1, a regra de decisão ótima é classificar como $\mathcal{C}_B$ sempre que $p(\mathcal{C}_B\mid x) > p(\mathcal{C}_A\mid x)$.
- □ Aumentar a penalidade de um erro Tipo II (escape) sem alterar a penalidade do erro Tipo I (alarme falso) desloca o ponto de corte $T_{CONJ}$ na direção da classe normal $\mathcal{C}_A$.
- □ Se as prioris forem $\pi_A=0{,}99$ e $\pi_B=0{,}01$, a regra do posterior máximo ($\text{MAP}$) ignorará a diferença de frequência e focará apenas nas densidades condicionais.

### Questão 12 — Detecção de Anomalias One-Class (L1)
- □ Em sistemas de detecção de anomalias onde apenas a classe normal $\mathcal{C}_A$ é modelada, o limiar de decisão é tipicamente definido como um percentil alto (ex: 95% ou 99%) da distribuição de escores de $\mathcal{C}_A$.
- □ Se reduzirmos o limiar de decisão de $99\%$ para $90\%$, a taxa de falsos positivos (alarmes falsos) diminuirá.
- □ A suposição de que a classe anômala $\mathcal{C}_B$ possui escores significativamente diferentes da classe normal $\mathcal{C}_A$ é fundamental para que a detecção baseada em $p(x\mid\mathcal{C}_A)$ funcione.
- □ O uso de uma distribuição Beta para modelar escores em $[0,1]$ impede que o sistema seja ajustado via Máxima Verossimilhança (MLE).

### Questão 13 — Independência no Naive Bayes (L2)
- □ A suposição de independência condicional do Naive Bayes implica que, dada a classe, a presença de um atributo não fornece informação sobre a presença de outro.
- □ Se dois atributos forem perfeitamente correlacionados, o Naive Bayes "conta" a evidência desse atributo duas vezes, o que pode levar a probabilidades posteriores extremas (próximas de 0 ou 1).
- □ O Naive Bayes é geralmente mais robusto a overfitting do que modelos complexos como árvores profundas, devido à sua simplicidade e baixo número de parâmetros.
- □ A fronteira de decisão do Naive Bayes é sempre linear, independentemente de como as densidades condicionais $p(x_i\mid\mathcal{C}_k)$ são modeladas.

### Questão 14 — Volume e Esparsidade no Espaço de Atributos (L2)
- □ A "maldição da dimensionalidade" refere-se ao fato de que, à medida que $d$ cresce, o volume do espaço cresce tão rapidamente que os dados disponíveis tornam-se esparsos.
- □ Em dimensões muito altas, a maioria dos pontos de um dataset tende a ficar concentrada perto da fronteira do espaço (ou nas "quinas" do hipercubo), tornando a noção de "vizinho próximo" menos útil.
- □ Um histograma com 2 bins por dimensão em $\mathbb{R}^{10}$ possui menos células totais do que um histograma com 100 bins em $\mathbb{R}^1$.
- □ A maldição da dimensionalidade afeta apenas modelos baseados em histogramas, não impactando modelos como Naive Bayes ou Árvores de Decisão.

### Questão 15 — Critérios de Split em Árvores (L3)
- □ O índice Gini e a Entropia medem a "impureza" de um nó; ambos tendem a zero quando o nó contém exemplos de apenas uma única classe.
- □ A taxa de erro de classificação é um critério de split preferível ao Gini para crescer a árvore, pois é mais sensível a pequenas mudanças na distribuição de classes.
- □ Em regressão, a minimização da soma dos quadrados dos resíduos (SSE) em cada folha é equivalente a maximizar a verossimilhança sob a suposição de ruído gaussiano com variância constante.
- □ O particionamento guloso garante que a árvore final seja a árvore globalmente ótima em termos de erro de treino.

### Questão 16 — Complexidade e Poda de Árvores (L3)
- □ Uma árvore de decisão crescida sem limites de profundidade tende a sofrer de alta variância (overfitting).
- □ A poda de custo-complexidade (cost-complexity pruning) remove ramos que não reduzem o erro de validação significativamente, trocando um pouco de acurácia por simplicidade.
- □ Se aumentarmos o número mínimo de pontos por folha, a árvore resultante tende a ser mais profunda e complexa.
- □ A profundidade de uma árvore é um hiperparâmetro que controla o trade-off entre overfiting e simplicidade.

### Questão 17 — Viés e Variância (L4)
- □ Modelos com alta flexibilidade (ex: árvores profundas, polinômios de grau alto) tendem a ter baixo viés e alta variância.
- □ O "overfitting" ocorre quando o modelo captura o ruído dos dados de treino em vez do sinal subjacente da população.
- □ Aumentar o tamanho do conjunto de treino geralmente reduz a variância do modelo, mas não afeta o viés intrínseco da arquitetura escolhida.
- □ Um modelo com viés alto (underfitting) é aquele que é simples demais para capturar a estrutura dos dados.

### Questão 18 — Vazamento de Dados e Validação (L4)
- □ O vazamento de dados (data leakage) ocorre quando informações do conjunto de teste "vazam" para o conjunto de treino, resultando em estimativas de erro excessivamente otimistas.
- □ Calcular a média e o desvio-padrão de todo o dataset para normalizar os dados *antes* de dividir em treino e teste é um exemplo de vazamento de dados.
- □ Para evitar vazamento, qualquer transformação de dados (como normalização ou seleção de atributos) deve ser aprendida apenas no conjunto de treino e aplicada ao de teste.
- □ A validação cruzada (CV) elimina completamente a necessidade de um conjunto de teste independente ao final do projeto.

### Questão 19 — Bootstrap e Bagging (L4)
- □ O Bootstrap consiste em criar novas amostras do mesmo tamanho do dataset original, selecionando pontos com reposição.
- □ Em uma amostra de bootstrap, espera-se que aproximadamente $63{,}2\%$ dos pontos originais sejam selecionados ao menos uma vez.
- □ O Bagging (Bootstrap Aggregating) reduz a variância de modelos instáveis (como árvores de decisão) ao tirar a média de várias previsões independentes.
- □ O erro de treino de um modelo treinado via Bagging é sempre menor do que o erro de treino de um único modelo treinado com todos os dados.

### Questão 20 — Risco Empírico vs Risco Esperado (L4)
- □ O risco empírico $\hat{R}(\theta)$ é a média da perda calculada sobre os dados de treino.
- □ O risco esperado $R(\theta)$ é a média da perda sobre a distribuição populacional real $P(X,Y)$.
- □ O erro de treino é geralmente um estimador não-enviesado do risco esperado, independentemente da complexidade do modelo.
- □ A diferença entre o risco esperado e o risco empírico é a base para a necessidade de conjuntos de validação e teste.

