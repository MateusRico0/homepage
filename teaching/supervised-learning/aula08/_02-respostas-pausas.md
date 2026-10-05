# Respostas das Pausas Ativas — Aula 08

## Pausa Ativa 1: O Estimador como Variável Aleatória

### Pergunta Aberta
**Pergunta:** Se coletarmos $100$ conjuntos de dados de treino independentes $\mathcal{D}_1, \dots, \mathcal{D}_{100}$, todos de mesmo tamanho $N=20$, gerados pelo mesmo processo físico com ruído aleatório, e ajustarmos uma regressão linear simples em cada um, obteremos $100$ retas com coeficientes $\hat\beta_0$ e $\hat\beta_1$ ligeiramente diferentes. Se calcularmos a média dessas $100$ retas, essa reta média $\bar{f}(x)$ ainda conterá variância amostral? Ela será capaz de capturar uma curvatura senoidal intrínseca nos dados?

**Discussão e Condução:**
A média amostral das retas aproxima o estimador esperado $\bar{f}(x) = \mathbb{E}_{\mathcal{D}}[\hat{f}(x; \mathcal{D})]$. No limite teórico de infinitos conjuntos de dados, a variância do estimador médio tende a zero (ele converge para uma função determinística fixa). Contudo, como cada modelo individual é uma reta linear ($y = \beta_0 + \beta_1 x$), a média de retas é **obrigatoriamente outra reta**. Portanto, ela jamais conseguirá se curvar para se ajustar a um seno. A incapacidade intrínseca da classe de funções de se aproximar da verdade é o **viés estrutural**, que persiste mesmo que a variância do estimador seja eliminada por amostragem infinita.

### Bloco V/F
1. **Afirmação:** O modelo ajustado $\hat{f}(x; \mathcal{D})$ é uma variável aleatória porque depende estocasticamente da amostra específica $\mathcal{D}$ sorteada da distribuição populacional.
   - **Gabarito: V**.
   - **Justificativa:** Como o conjunto de treinamento $\mathcal{D} = \{(\mathbf{x}_n, y_n)\}_{n=1}^N$ é uma realização amostral aleatória de $P(X, Y)$, qualquer função calculada a partir dele (incluindo os parâmetros estimados) é uma variável aleatória.
2. **Afirmação:** O estimador médio $\bar{f}(x) = \mathbb{E}_{\mathcal{D}}[\hat{f}(x; \mathcal{D})]$ muda de valor a cada novo conjunto de treinamento de tamanho $N$ coletado.
   - **Gabarito: F**.
   - **Justificativa:** O valor esperado sobre a distribuição de todos os possíveis conjuntos de dados $\mathcal{D}$ é uma função determinística fixa para um dado algoritmo e tamanho $N$; quem varia a cada amostra é $\hat{f}(x; \mathcal{D})$, não sua média teórica $\bar{f}(x)$.
3. **Afirmação:** Em um problema prático real com um único conjunto de dados estático $\mathcal{D}_{\text{real}}$, podemos calcular analiticamente o viés exato do modelo sem fazer nenhuma hipótese adicional.
   - **Gabarito: F**.
   - **Justificativa:** O cálculo exato do viés $(f(x) - \bar{f}(x))^2$ requer conhecer a função verdadeira subjacente $f(x)$, que na prática é desconhecida; em aplicações reais, o viés só pode ser estimado via validação cruzada ou aproximações.
4. **Afirmação:** Se um estimador for não enviesado para qualquer ponto $x$ (isto é, $\mathbb{E}_{\mathcal{D}}[\hat{f}(x)] = f(x)$), seu erro de predição em qualquer conjunto de teste será rigorosamente igual a zero.
   - **Gabarito: F**.
   - **Justificativa:** Mesmo com viés zero, o erro quadrático esperado ainda contém a variância do estimador $\text{Var}_{\mathcal{D}}(\hat{f}(x))$ e o ruído irredutível $\sigma^2 > 0$.

---

## Pausa Ativa 2: A Decomposição Formal e o Termo Cruzado

### Pergunta Aberta
**Pergunta:** Na expansão algébrica do erro quadrático esperado $\mathbb{E}_{\mathcal{D}}[(f(x) - \hat{f}(x; \mathcal{D}))^2]$, somamos e subtraímos o estimador médio $\bar{f}(x) = \mathbb{E}_{\mathcal{D}}[\hat{f}(x)]$, gerando o termo cruzado $2(f(x) - \bar{f}(x)) \mathbb{E}_{\mathcal{D}}[\bar{f}(x) - \hat{f}(x; \mathcal{D})]$. Por que esse termo cruzado se anula rigorosamente? O que aconteceria se a perda fosse o erro absoluto médio $|y - \hat{f}(x)|$ em vez da perda quadrática?

**Discussão e Condução:**
O termo cruzado anula-se pela linearidade do operador esperança: $\mathbb{E}_{\mathcal{D}}[\bar{f}(x) - \hat{f}(x; \mathcal{D})] = \bar{f}(x) - \mathbb{E}_{\mathcal{D}}[\hat{f}(x; \mathcal{D})] = \bar{f}(x) - \bar{f}(x) = 0$.
Além disso, o termo $f(x) - \bar{f}(x)$ é uma constante determinística em relação à distribuição amostral $\mathcal{D}$, podendo ser colocado para fora da esperança.
Se utilizássemos a perda em valor absoluto $|y - \hat{f}(x)|$, a decomposição aditiva pura em viés ao quadrado e variância não seria obtida, pois $|a + b| \le |a| + |b|$ envolve desigualdades triangulares não lineares, sem ortogonalidade nos termos. A decomposição aditiva perfeita é uma propriedade geométrica exclusiva de normas $L_2$ e produtos internos associados à perda quadrática.

### Bloco V/F
1. **Afirmação:** O erro irredutível $\sigma^2 = \text{Var}(\epsilon)$ pode ser reduzido a zero se coletarmos um número suficientemente grande de observações de treinamento ($N \to \infty$).
   - **Gabarito: F**.
   - **Justificativa:** $\sigma^2$ é o ruído estocástico intrínseco do processo gerador $y = f(x) + \epsilon$; ele independe do tamanho amostral $N$ e do algoritmo de aprendizado utilizado.
2. **Afirmação:** Na perda quadrática esperada $\text{EMSE}(x) = \text{Bias}^2(x) + \text{Var}(x) + \sigma^2$, os três termos são estritamente não negativos para qualquer ponto $x$.
   - **Gabarito: V**.
   - **Justificativa:** O viés ao quadrado $(f(x) - \bar{f}(x))^2 \ge 0$, a variância $\mathbb{E}[(\hat{f}(x) - \bar{f}(x))^2] \ge 0$ e a variância do ruído $\sigma^2 \ge 0$ são todas grandezas quadráticas.
3. **Afirmação:** O termo cruzado $2 \mathbb{E}_{\mathcal{D}, \epsilon}[(f(x) - \hat{f}(x)) \epsilon]$ na decomposição do erro anula-se porque o ruído de teste $\epsilon$ tem média zero e é estatisticamente independente dos dados de treino $\mathcal{D}$.
   - **Gabarito: V**.
   - **Justificativa:** Por independência, $\mathbb{E}[(f(x) - \hat{f}(x)) \epsilon] = \mathbb{E}[f(x) - \hat{f}(x)] \cdot \mathbb{E}[\epsilon] = \mathbb{E}[f(x) - \hat{f}(x)] \cdot 0 = 0$.
4. **Afirmação:** A variância do estimador $\text{Var}_{\mathcal{D}}(\hat{f}(x))$ mede o quanto a predição média do modelo afasta-se da função verdadeira $f(x)$.
   - **Gabarito: F**.
   - **Justificativa:** A discrepância entre a predição média e a verdade é a definição de **viés**; a variância mede a dispersão das predições de modelos individuais em torno de sua própria média $\bar{f}(x)$.

---

## Pausa Ativa 3: Capacidade de Hipóteses e Tamanho Amostral $N$

### Pergunta Aberta
**Pergunta:** Suponha que estejamos ajustando uma regressão polinomial a dados ruidosos gerados por uma função complexa. Se aumentarmos o grau do polinômio de 1 para 15 com $N=30$ fixo, o que acontece com o viés e a variância? E se mantivermos o grau 15 fixo, mas aumentarmos o número de pontos de treino de $N=30$ para $N=10.000$?

**Discussão e Condução:**
Ao aumentar o grau do polinômio de 1 para 15 com $N=30$ fixo, o espaço de hipóteses $\mathcal{H}$ expande-se dramaticamente: o viés ao quadrado cai drasticamente (pois polinômios de alta ordem conseguem aproximar quase qualquer curva), mas a variância explode (o modelo decora o ruído de cada amostra e flutua loucamente entre os pontos).
Ao fixar o grau em 15 e aumentar o tamanho amostral de $N=30$ para $N=10.000$, o viés estrutural permanece essencialmente constante (pois a classe de funções é a mesma), mas a **variância do estimador decresce com $O(1/N)$**. Com dados abundantes, os parâmetros são estimados com altíssima precisão e as oscilações espúrias desaparecem.

### Bloco V/F
1. **Afirmação:** Aumentar a capacidade de um modelo (ex.: grau de polinômio ou profundidade de árvore) tende a reduzir monotonicamente o viés ao quadrado, mas aumenta a variância do estimador.
   - **Gabarito: V**.
   - **Justificativa:** Uma classe de funções mais flexível contém aproximações mais próximas de $f(x)$ (reduzindo viés), mas torna-se mais sensível às flutuações amostrais de $\mathcal{D}$ (aumentando variância).
2. **Afirmação:** Se um modelo possui alto viés estrutural (ex.: reta linear tentando ajustar dados com curvatura quadrática pronunciada), coletar milhões de dados adicionais fará o viés tender a zero.
   - **Gabarito: F**.
   - **Justificativa:** O viés vem da incapacidade representacional do modelo; mesmo com $N \to \infty$, o melhor ajuste linear ainda errará a curvatura intrínseca. Mais dados reduzem variância, não viés estrutural.
3. **Afirmação:** O erro quadrático médio esperado integrado $\text{EMSE} = \int \text{EMSE}(x) p(x) \, \mathrm{d}x$ atinge seu valor mínimo exatamente quando o viés e a variância são ambos simultaneamente iguais a zero.
   - **Gabarito: F**.
   - **Justificativa:** Na prática com amostras finitas e funções gerais, viés e variância movem-se em direções opostas; além disso, mesmo se viés e variância fossem zero, o erro integrado mínimo seria $\sigma^2 > 0$ (erro irredutível).
4. **Afirmação:** Para um estimador linear ordinário (OLS) com $p$ parâmetros, a variância média do estimador escala proporcionalmente com $p/N$.
   - **Gabarito: V**.
   - **Justificativa:** Pela conta da matriz chapéu do Bloco 2 ($\text{Cov}(\hat{\mathbf y})=\sigma^2H$, $\mathrm{tr}\,H=p$), $\frac{1}{N} \sum_{n=1}^N \text{Var}(\hat{y}_n) = \sigma^2 \frac{p}{N}$ exatamente, com desenho fixo, confirmando que a variância cresce com a dimensão $p$ e decresce com $N$.

---

## Pausa Ativa 4: Ridge e a Injeção Deliberada de Viés

### Pergunta Aberta
**Pergunta:** Na Aula 5, vimos pelo Teorema de Gauss-Markov que o estimador OLS $\hat{\boldsymbol\beta}_{\text{OLS}}$ é o "BLUE" (Melhor Estimador Linear Não Enviesado), significando que ele possui a menor variância possível entre todos os estimadores não enviesados. Se o OLS já tem a menor variância entre os não enviesados, por que alguém escolheria deliberadamente o estimador Ridge $\hat{\boldsymbol\beta}_{\text{Ridge}} = (X^TX + \lambda I)^{-1} X^T\mathbf{y}$, que é comprovadamente enviesado?

**Discussão e Condução:**
O Teorema de Gauss-Markov restringe sua garantia estritamente à classe de estimadores **não enviesados** ($\text{Bias} = 0$).
No entanto, o nosso objetivo real em aprendizado de máquina não é ter viés zero por vaidade estatística, mas sim **minimizar o erro quadrático total**: $\text{MSE} = \text{Bias}^2 + \text{Var}$.
Ao relaxar a restrição de viés nulo e aceitar uma pequena quantidade de viés ($\text{Bias}^2 > 0$), o estimador Ridge consegue reduzir a variância de forma desproporcionalmente maior do que o viés adicionado. O Teorema de Hoerl & Kennard (1970) prova matematicamente que sempre existe algum $\lambda > 0$ cuja redução de variância supera o aumento quadrático de viés, resultando em um erro total menor que o do OLS.

### Bloco V/F
1. **Afirmação:** O estimador de regressão Ridge $\hat{\boldsymbol\beta}_{\text{Ridge}}$ é um estimador não enviesado dos verdadeiros coeficientes $\boldsymbol\beta^*$ para qualquer $\lambda > 0$.
   - **Gabarito: F**.
   - **Justificativa:** $\mathbb{E}[\hat{\boldsymbol\beta}_{\text{Ridge}}] = (X^TX + \lambda I)^{-1} X^TX \boldsymbol\beta^* \neq \boldsymbol\beta^*$ para todo $\lambda > 0$; ele encolhe os coeficientes em direção à origem, introduzindo viés deliberadamente.
2. **Afirmação:** A matriz de covariância do estimador Ridge satisfaz $\text{Cov}(\hat{\boldsymbol\beta}_{\text{Ridge}}) \prec \text{Cov}(\hat{\boldsymbol\beta}_{\text{OLS}})$ para qualquer $\lambda > 0$, significando que a variância do estimador regularizado é estritamente menor que a do OLS em todas as direções.
   - **Gabarito: V**.
   - **Justificativa:** Como $(X^TX + \lambda I)^{-1} \prec (X^TX)^{-1}$ para $\lambda > 0$, a propagação do ruído $\sigma^2$ é estritamente atenuada.
3. **Afirmação:** O Teorema de Hoerl & Kennard (1970) garante que sempre existe um valor de penalidade $\lambda > 0$ tal que o erro quadrático total do Ridge é estritamente inferior ao do estimador OLS.
   - **Gabarito: V**.
   - **Justificativa:** Na vizinhança de $\lambda = 0$, a derivada do viés ao quadrado em relação a $\lambda$ é zero, enquanto a derivada da variância é estritamente negativa; logo, a derivada do erro total em $\lambda=0$ é negativa.
4. **Afirmação:** Aumentar indefinidamente o parâmetro de regularização $\lambda \to \infty$ faz o erro de predição convergir para zero.
   - **Gabarito: F**.
   - **Justificativa:** Quando $\lambda \to \infty$, todos os coeficientes $\boldsymbol\beta \to \mathbf{0}$, fazendo a variância tender a zero mas explodindo o viés estrutural, resultando em subajuste extremo.

---

## Pausa Ativa 5: Leitura e Diagnóstico de Curvas de Aprendizado

### Pergunta Aberta
**Pergunta:** Uma equipe de engenharia treina uma rede neural profunda para prever preços de imóveis. Eles geram a curva de aprendizado (Erro vs. Tamanho do Treino $N$):
- Com $N=1.000$, o erro de treino é $0{,}02$ e o erro de validação é $0{,}45$.
- Com $N=10.000$, o erro de treino sobe ligeiramente para $0{,}05$ e o erro de validação cai para $0{,}38$.
- Há uma lacuna persistente considerável entre as duas curvas.
O modelo está limitado por viés ou por variância? Coletar mais $50.000$ exemplos de treino resolverá o problema? Que outras intervenções seriam recomendadas?

**Discussão e Condução:**
O modelo está claramente limitado por **alta variância (overfitting)**: o erro de treino é excelente ($0{,}05$, muito baixo), mas há um abismo (*gap*) substancial em relação ao erro de validação ($0{,}38$).
Como a curva de validação continua caindo quando $N$ aumenta de $1.000$ para $10.000$, coletar mais dados de treino ($N=50.000$) é uma intervenção altamente efetiva neste cenário, pois mais dados forçam o modelo a generalizar e reduzem a variância.
Outras intervenções recomendadas para alta variância incluem: introduzir regularização (penalidade $L_2$/weight decay), reduzir a capacidade do modelo (menos camadas/unidades), aplicar dropout ou realizar seleção de atributos.

### Bloco V/F
1. **Afirmação:** Em um cenário de alto viés (*underfitting*), tanto o erro de treino quanto o erro de validação convergem rapidamente para valores altos, com uma lacuna mínima entre eles.
   - **Gabarito: V**.
   - **Justificativa:** Se o modelo for simples demais para capturar os padrões dos dados, ele não consegue ajustar bem nem mesmo a amostra de treino, e adicionar dados não altera seu teto de desempenho.
2. **Afirmação:** Se um modelo sofre de alta variância (*overfitting*), a melhor intervenção imediata é aumentar a complexidade da arquitetura para que ele aprenda representações ainda mais ricas.
   - **Gabarito: F**.
   - **Justificativa:** Aumentar a complexidade aumentará ainda mais a variância e agravará o overfitting; o correto é regularizar, podar atributos, reduzir capacidade ou coletar mais dados.
3. **Afirmação:** O erro de treino de um modelo de aprendizado supervisionado é tipicamente uma estimativa otimista (subestimada) do verdadeiro erro de generalização.
   - **Gabarito: V**.
   - **Justificativa:** Como os parâmetros foram otimizados exatamente para minimizar o erro naquela amostra específica, o estimador adapta-se ao ruído da amostra, gerando viés de otimismo (*training optimism*).
4. **Afirmação:** Na presença de ruído irredutível $\sigma^2 > 0$, o erro de validação assintótico para $N \to \infty$ pode atingir zero se usarmos um modelo universal como árvores de decisão sem poda.
   - **Gabarito: F**.
   - **Justificativa:** Nenhuma quantidade de dados ou flexibilidade de modelo pode ultrapassar a barreira de Bayes; o erro de validação jamais será inferior a $\sigma^2$.
