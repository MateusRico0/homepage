# Respostas das Pausas Ativas — Aula 6

Discussão das perguntas provocadoras e soluções analíticas das afirmações de Verdadeiro/Falso das Pausas Ativas da Aula 6 (Regressão Logística e Modelos Lineares Generalizados). Arquivo de apoio docente, não publicado.

---

## Pausa Ativa 1 — Regressão Linear Aplicada a Rótulos Binários

### Discussão da Pergunta Motivadora
A tentativa de aplicar Mínimos Quadrados Ordinários (OLS) a uma variável de resposta binária $y \in \{0, 1\}$ (o chamado "Modelo de Probabilidade Linear") esbarra em três inconsistências estruturais:
1. **Resíduos não-normais:** Para cada $\mathbf{x}$, o erro assume apenas dois valores discretos ($1 - \mathbf{w}^T\mathbf{x}$ ou $-\mathbf{w}^T\mathbf{x}$). Não existe suporte para a premissa de normalidade dos resíduos.
2. **Heterocedasticidade intrínseca:** Como $Y\mid\mathbf{x} \sim \text{Bernoulli}(\mu(\mathbf{x}))$, a variância teórica é $\text{Var}(Y\mid\mathbf{x}) = \mu(\mathbf{x})(1 - \mu(\mathbf{x}))$. A dispersão varia com $\mathbf{x}$, violando a homocedasticidade e tornando OLS ineficiente.
3. **Penalização de acertos convictos:** A perda quadrática $(y - \hat{y})^2$ penaliza predições maiores que $1$ ou menores que $0$, forçando a reta a mudar de inclinação mesmo quando a classificação está perfeitamente correta.

### Resolução das Afirmações
- ✔ **Afirmação 1 (Verdadeiro):** Os resíduos assumem apenas dois valores condicionais para cada ponto observado, violando fundamentalmente a continuidade e a simetria da distribuição normal.
- ✔ **Afirmação 2 (Verdadeiro):** A variância condicional é $\mu(\mathbf{x})(1-\mu(\mathbf{x}))$, variando ponto a ponto ao longo do espaço amostral.
- ✗ **Afirmação 3 (Falso):** Pontos com previsões $>1$ (por exemplo, $\hat{y}=1{,}4$ com $y=1$) geram resíduo não-nulo de $-0{,}4$, adicionando penalidade quadrática de $0{,}16$ ao RSS e forçando a rotação da reta.
- ✗ **Afirmação 4 (Falso):** A truncagem ad-hoc após o ajuste não restaura a verossimilhança de Bernoulli durante o treinamento, gerando estimativas viesadas e incoerentes.

---

## Pausa Ativa 2 — A Verossimilhança de Bernoulli e a Entropia Cruzada

### Discussão da Pergunta Motivadora
A perda de Entropia Cruzada Binária é deduzida diretamente da Máxima Verossimilhança de variáveis de Bernoulli independentes. A penalidade logarítmica $-\ln(\mu_n)$ assegura que erros com alta convicção sejam punidos com custo assintoticamente infinito, forçando o modelo a calibrar probabilidades realistas.

### Resolução das Afirmações
- ✗ **Afirmação 1 (Falso):** A distribuição de Bernoulli exige estritamente $y \in \{0, 1\}$. Multiplicar por uma constante quebra a soma unitária das probabilidades e descaracteriza a verossimilhança.
- ✔ **Afirmação 2 (Verdadeiro):** Em dados muito desbalanceados, prever a proporção majoritária atinge valor de entropia cruzada baixo (a entropia da distribuição marginal da classe), mas não aprende nenhuma dependência funcional com $\mathbf{x}$.
- ✗ **Afirmação 3 (Falso):** A Máxima Verossimilhança padrão busca estimar as probabilidades verdadeiras $p(C_1\mid\mathbf{x})$; custos de erro assimétricos pertencem à Teoria da Decisão (escolha do limiar ótimo $\tau$) ou a pesos de classe adicionados externamente.
- ✗ **Afirmação 4 (Falso):** Embora a expansão de Taylor de segunda ordem da entropia cruzada em torno de $0{,}5$ produza um termo quadrático, as perdas são analiticamente diferentes em todo o domínio e divergem drasticamente nos extremos.

---

## Pausa Ativa 3 — Otimização Convexa, Hessiana e o Algoritmo IRLS

### Discussão da Pergunta Motivadora
O algoritmo Newton-Raphson utiliza a informação de segunda ordem (curvatura) para realizar passos direcionados ao mínimo da função. Como a Hessiana $H = X^T R X$ é estritamente definida positiva em todo o domínio, a superfície de perda não possui mínimos locais, e o método atinge convergência quadrática local.

### Resolução das Afirmações
- ✗ **Afirmação 1 (Falso):** O método de Newton é invariante a transformações afins lineares dos atributos; a curvatura da Hessiana compensa escalas desiguais, convergindo com número de passos muito inferior ao Gradient Descent em matrizes mal-condicionadas.
- ✔ **Afirmação 2 (Verdadeiro):** Conforme $\mu_n \to 0$ ou $1$, o produto $\mu_n(1-\mu_n) \to 0$, fazendo com que a matriz $R$ se aproxime de zero e a Hessiana perca posto efetivo (saturação).
- ✔ **Afirmação 3 (Verdadeiro):** Sendo uma função estritamente convexa em $\mathbb{R}^D$, a perda de entropia cruzada possui um único minimizador global, independente do ponto de partida.
- ✗ **Afirmação 4 (Falso):** OLS possui Hessiana constante e gradiente linear em $\mathbf{w}$, sendo resolvido em um único passo. Na regressão logística, $R$ varia dinamicamente a cada passo, exigindo convergência iterativa.

---

## Pausa Ativa 4 — Modelos Lineares Generalizados e a Ligação Canônica

### Discussão da Pergunta Motivadora
O Teorema da Ligação Canônica estabelece que a escolha da função de ligação que conecta a média ao parâmetro natural canônico da Família Exponencial induz sempre o mesmo gradiente simplificado $\nabla E = X^T(\boldsymbol\mu - \mathbf{y})$. Esse resultado unifica regressão linear, logística, Poisson e Softmax sob o mesmo mecanismo analítico.

### Resolução das Afirmações
- ✔ **Afirmação 1 (Verdadeiro):** O modelo *probit* utiliza a inversa da CDF normal como ligação; sua derivada não cancela o denominador da Bernoulli, resultando em um fator corretivo não-trivial no gradiente.
- ✔ **Afirmação 2 (Verdadeiro):** Para a distribuição normal com variância fixa, $\eta = \mu$, de modo que a ligação canônica é a função identidade $g(\mu) = \mu$.
- ✗ **Afirmação 3 (Falso):** O modelo de Poisson com ligação logarítmica canônica $\eta = \ln \mu$ pertence à Família Exponencial, gerando exatamente o gradiente $X^T(\boldsymbol\mu - \mathbf{y})$, onde $\mu_n = \exp(\mathbf{w}^T\mathbf{x}_n)$.
- ✗ **Afirmação 4 (Falso):** A ligação canônica é determinada estritamente pela álgebra da Família Exponencial ($\eta = \psi(\mu)$), e não por qualquer função contínua que limite o intervalo de saída.

---

## Pausa Ativa 5 — Separação Perfeita e a Transição para Regularização

### Discussão da Pergunta Motivadora
Quando os dados são linearmente separáveis, a perda de entropia cruzada pode ser reduzida arbitrariamente para zero empurrando a magnitude do vetor de pesos ao infinito ($\|\mathbf{w}\| \to \infty$). Isso expõe a limitação da Máxima Verossimilhança pura em pequenas amostras separáveis e motiva a regularização Bayesiana (MAP / Ridge / Lasso).

### Resolução das Afirmações
- ✗ **Afirmação 1 (Falso):** Mapear os dados para espaços polinomiais de dimensão superior aumenta a probabilidade de separabilidade perfeita, agravando a divergência dos pesos.
- ✔ **Afirmação 2 (Verdadeiro):** A fronteira de decisão $\mathbf{w}^T\mathbf{x} = 0$ é homogênea de grau zero em relação a escalas positivas $k\mathbf{w}$; portanto, a geometria do hiperplano permanece perfeitamente definida mesmo quando $\|\mathbf{w}\| \to \infty$.
- ✗ **Afirmação 3 (Falso):** A perda de entropia cruzada continua estritamente convexa; a divergência decorre de o infímo da função estar situado no limite assintótico no infinito, e não em um mínimo local finito.
- ✔ **Afirmação 4 (Verdadeiro):** A penalidade Ridge adiciona curvatura positiva $\lambda I$ à Hessiana ($X^T R X + \lambda I$), impedindo que a norma de $\mathbf{w}$ cresça indefinidamente e garantindo uma solução finita e única.
