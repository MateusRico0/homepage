# Gabarito das Pausas Ativas — Aula 5

Discute cada pergunta motivadora das pausas ativas do `index.qmd` e dá a
solução dos respectivos V/F. Nunca publicado no site (prefixo `_`). O
gabarito da seção de Exercícios de fechamento (discursivas + V/F) migrou
para `soluções.qmd`, publicado — ver `../../CLAUDE.md`, seção "Exercícios".

## Pausas Ativas

### Pausa 1 — Antes de Ajustar: O que "Melhor Reta" Já Pressupõe?

**Pergunta motivadora:** Se eu te desse duas retas diferentes, ambas
passando "no meio" da nuvem de pontos, como você decidiria qual é
"melhor" sem fazer nenhuma conta?

**Discussão:** "Melhor" não pode significar apenas "passa perto da
média" — qualquer reta que passe pelo ponto médio $(\bar x,\bar y)$ tem
soma de desvios (sem elevar ao quadrado) exatamente zero, mesmo retas
absurdas, giradas em ângulos que claramente não acompanham a nuvem.
Duas retas com o mesmo ponto médio podem ter inclinações completamente
diferentes e tratar os desvios de forma muito distinta. Um critério
"melhor reta" só é informativo se penalizar desvios de um jeito que
distinga retas boas de ruins — é isso que a soma de quadrados resolve.

**V/F resolvido:**
- ✗ Duas retas que passam pelo mesmo ponto médio $(\bar x,\bar y)$ da nuvem de dados são necessariamente igualmente boas, pois ambas capturam a tendência central dos dados.
- ✔ Se todos os pontos da nuvem estivessem exatamente sobre uma única reta (sem nenhum ruído), qualquer critério razoável de "melhor reta" apontaria para essa mesma reta.
- ✗ Um termostato que prevê a temperatura de amanhã a partir da de hoje enfrenta a mesma estrutura de "melhor reta", mas isso não implica que a inclinação ótima seja necessariamente próxima de 1.
- ✔ Julgar "melhor reta" pela soma dos desvios (sem quadrado, sem valor absoluto) é degenerado: qualquer reta pela média $(\bar x,\bar y)$ tem soma de desvios zero, inclusive retas absurdas.

---

### Pausa 2 — Projeção, Resíduos e Equações Normais

**Pergunta motivadora:** Geometricamente, por que o vetor de resíduos
$y-\hat y$ ser ortogonal ao subespaço gerado pelas colunas de $X$ é
exatamente a condição que caracteriza a MELHOR aproximação, e não uma
coincidência do cálculo?

**Discussão:** Não é coincidência — é Pitágoras. Mover $\hat y$ para
qualquer outro ponto do subespaço $\mathcal S$ só pode *aumentar* a
distância $\lVert y-\hat y\rVert$, porque qualquer deslocamento dentro
de $\mathcal S$ soma um termo estritamente positivo à distância ao
quadrado. Ortogonalidade é a única forma de $\hat y$ não deixar
"sobra" evitável dentro do subespaço — é exatamente essa condição que
as equações normais ($X^T(y-X\hat\beta)=0$) impõem algebricamente.

**V/F resolvido:**
- ✔ Minimizar $\lVert y-X\beta\rVert^2$ e minimizar $\lVert y-X\beta\rVert$ produzem o mesmo $\hat\beta$, porque a raiz quadrada é estritamente crescente em distâncias não-negativas.
- ✔ Se as colunas de $X$ forem linearmente dependentes, $X^TX$ deixa de ser invertível e $\hat\beta$ perde unicidade — mas a projeção $\hat y=X\hat\beta$ continua bem definida e única.
- ✗ Num sistema de recomendação com perfis latentes linearmente dependentes, a lógica de projeção continua valendo, mas a unicidade de $\hat\beta$ não — a mesma ressalva do item anterior.
- ✗ Ortogonalidade ao subespaço $\mathcal S$ não implica resíduo nulo — só implica que o resíduo não tem componente dentro de $\mathcal S$; se $y\notin\mathcal S$ (o caso típico com ruído real), o resíduo é não-nulo e ainda assim ortogonal a $\mathcal S$.

---

### Pausa 3 — Premissas do Ruído Gaussiano Homocedástico

**Pergunta motivadora:** Se a variância do ruído crescesse conforme a
renda mediana aumenta — imóveis mais caros têm preços mais
"espalhados" — o que exatamente, na construção da verossimilhança de
hoje, deixaria de valer?

**Discussão:** O símbolo que ganharia um índice $n$ é justamente
$\sigma^2$ — de uma constante única para uma função $\sigma^2(x_n)$
que varia por observação. A fatoração da verossimilhança conjunta em
produto de densidades individuais sobrevive (ainda depende só da
suposição de independência, não de homocedasticidade), mas a forma de
cada fator muda: cada termo carregaria seu próprio $\sigma(x_n)$, e a
log-verossimilhança teria $\ln\sigma(x_n)$ dentro do somatório, em vez
de um único $N\ln\sigma$ fatorado para fora.

**V/F resolvido:**
- ✔ Se $\sigma^2$ dependesse de $x_n$, a verossimilhança conjunta ainda seria produto das densidades individuais (assumindo independência), mas cada fator teria sua própria variância $\sigma^2(x_n)$.
- ✔ No limite $\sigma^2\to0$, a densidade gaussiana se concentra inteiramente sobre o valor predito, e o modelo probabilístico se aproxima do caso determinístico sem ruído.
- ✗ Verificar homocedasticidade num sensor não garante nada sobre outro sensor, nem do mesmo fabricante — a suposição nunca "generaliza de graça", exige checagem individual.
- ✗ A estimativa de mínimos quadrados continua sendo uma escolha razoável mesmo sem normalidade exata (ela minimiza RSS por construção); o que se perde sem normalidade é a interpretação como MLE, não a validade do ponto estimado.

---

### Pausa 4 — OLS = MLE: O Que a Prova Realmente Diz

**Pergunta motivadora:** A busca numérica encontrou exatamente o mesmo
$\hat\beta$ que a fórmula fechada, a menos de $10^{-8}$. Isso prova que
maximizar a log-verossimilhança SEMPRE encontra o mínimo de RSS, para
qualquer distribuição de ruído — ou é uma coincidência do caso
gaussiano?

**Discussão:** É uma propriedade do caso gaussiano especificamente — a
prova do Bloco 3 usou explicitamente a forma exponencial-quadrática
$\exp\{-(\cdot)^2/2\sigma^2\}$ da densidade gaussiana, num passo
específico da derivação (isolar o termo em $\beta$). Trocar o ruído
assumido por outra distribuição (Laplace, por exemplo) produziria
outra função de erro a minimizar pela mesma lógica geral — mas não a
mesma soma de quadrados. A confirmação numérica é uma verificação
empírica sobre um dataset específico com um otimizador que convergiu
corretamente, não uma prova matemática geral; a prova matemática é a
derivação algébrica do Bloco 3.

**V/F resolvido:**
- ✔ Se o ruído fosse Laplace em vez de gaussiano, maximizar a verossimilhança levaria a minimizar a soma dos valores absolutos dos resíduos, não a soma de quadrados.
- ✔ No limite $N\to\infty$ com modelo verdadeiramente linear e gaussiano, $\hat\beta_{\text{MLE}}$ e $\hat\sigma^2_{\text{MLE}}$ convergem para os valores populacionais, e o viés relativo de $\hat\sigma^2_{\text{MLE}}$ desaparece assintoticamente.
- ✗ Comparar log-verossimilhanças máximas entre famílias distribucionais diferentes (gaussiana vs. Bernoulli) não é válido sem correção (AIC/BIC) — as escalas não são diretamente comparáveis.
- ✗ Confirmar numericamente para um dataset e um otimizador que convergiu corretamente não estende a garantia a qualquer otimizador (um que não converge não chegaria ao mesmo ponto).
