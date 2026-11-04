# Respostas das Pausas Ativas — Aula 10: Gradient Boosting e Otimização Numérica no Espaço de Funções

Este documento contém o gabarito detalhado, as discussões das perguntas abertas e as diretrizes pedagógicas para a condução das 5 Pausas Ativas da Aula 10.

---

## Pausa Ativa 1: A Inversão Filosófica entre Bagging e Boosting

### Pergunta Aberta
**Cenário:** Uma equipe de cientistas de dados precisa modelar um problema tabular ruidoso e dispõe de dois algoritmos: Random Forests (Aula 9) e Gradient Boosting (Aula 10). Um membro júnior propõe: *"Vamos configurar o Gradient Boosting para treinar árvores profundas e não podadas com $J = 256$ nós terminais, exatamente como fizemos com a Random Forest na aula passada, para garantir que o modelo aprenda padrões complexos desde a primeira iteração."* Avalie criticamente a proposta desse profissional. O que acontecerá com o comportamento do ensemble ao longo das iterações $m = 1, \dots, M$?

**Discussão e Condução Pedagógica:**
- A proposta comete um erro conceitual grave ao confundir os mecanismos antagônicos de redução de erro de Bagging e Boosting.
- **No Bagging / Random Forests:** As árvores individuais são propositalmente profundas e não podadas (alta variância, baixíssimo viés). Como a agregação é feita por **média aritmética paralela**, a média amortece a variância $\sigma^2$ das árvores através do fator $(1-\rho)/B$. Portanto, o Bagging precisa de modelos de alta capacidade como bloco construtor.
- **No Boosting:** O mecanismo de redução de erro é a **adição sequencial focada no viés**. Cada nova árvore é treinada para corrigir os erros residuais do modelo acumulado. Se utilizarmos árvores profundas com $J = 256$ folhas logo na primeira iteração:
  1. A primeira árvore já interpolará quase perfeitamente o conjunto de treinamento, decorando ruídos e outliers.
  2. Os resíduos $r_{i1} = y_i - f_1(\mathbf{x}_i)$ para a iteração 2 serão essencialmente ruído puro de altíssima frequência.
  3. A segunda árvore ajustará esse ruído, amplificando o sobreajuste (*overfitting*) de maneira incontrolável.
  4. O Gradient Boosting perderá completamente a capacidade de generalização no conjunto de teste.
- **Conclusão:** O Boosting exige **modelos fracos** (*weak learners*), tipicamente árvores muito rasas com $J \in [4, 8]$ nós terminais (profundidade 2 ou 3) e uma taxa de aprendizado encolhida $\nu \le 0{,}1$. A complexidade do modelo final emerge da **acumulação de centenas de passos graduais**, e não da capacidade de uma única árvore individual.

### Teste V/F
- ✔ **V:** Pela decomposição de erro, o Bagging reduz variância via média de árvores profundas e independentes, enquanto o Boosting reduz viés ajustando modelos fracos sequencialmente aos erros.
- ✗ **F:** O Boosting acumula termos aditivos sequenciais que buscam minimizar a perda de treino; com árvores muito complexas e sem regularização, ele sobreajusta rapidamente com o aumento de $M$.
- ✔ **V:** A média de estimadores preserva a esperança ($\mathbb{E}[\bar{T}] = \mathbb{E}[T]$); portanto, estimadores fracos com alto viés permanecem enviesados após o Bagging.
- ✗ **F:** Árvores com profundidade 1 (*decision stumps*) possuem apenas um corte, sendo incapazes de modelar interações entre duas ou mais variáveis em uma única árvore; interações requerem profundidade pelo menos 2 ($J \ge 3$).

---

## Pausa Ativa 2: Descida de Gradiente no Espaço de Funções

### Pergunta Aberta
**Cenário:** Na descida de gradiente clássica em $\mathbb{R}^d$, damos um passo na direção $-\nabla_{\mathbf{w}} L(\mathbf{w})$ para atualizar parâmetros finitos $\mathbf{w}$. No Gradient Boosting de Friedman (2001), o vetor $-\mathbf{g} = [r_1, \dots, r_N]^T \in \mathbb{R}^N$ fornece o gradiente negativo nos $N$ pontos de treino. Por que não podemos simplesmente atualizar diretamente as predições de treino fazendo $f_m(\mathbf{x}_i) = f_{m-1}(\mathbf{x}_i) + \rho r_{im}$ para cada $i = 1, \dots, N$? Qual é o papel indispensável da árvore de regressão $h_m(\mathbf{x})$ nesse processo?

**Discussão e Condução Pedagógica:**
- Se atualizássemos diretamente $f_m(\mathbf{x}_i) = f_{m-1}(\mathbf{x}_i) + \rho r_{im}$ apenas nos pontos do conjunto de treinamento, obteríamos uma tabela finita de valores numéricos que minimiza a perda nos $N$ dados observados, mas que é **completamente incapaz de predizer qualquer novo ponto de teste $\mathbf{x} \notin \mathcal{D}$**.
- Em problemas supervisionados, nosso objetivo não é memorizar o vetor discreto de rótulos de treino, mas sim estimar uma **função de mapeamento contínua ou por partes $f: \mathcal{X} \to \mathbb{R}$** que generalize para toda a distribuição $P(X, Y)$.
- O vetor de gradientes negativos $-\mathbf{g} \in \mathbb{R}^N$ reside no espaço não paramétrico irrestrito dos dados de treino.
- Ao ajustar uma árvore de regressão $h_m(\mathbf{x})$ aos alvos $r_{im}$ por mínimos quadrados, estamos realizando uma **projeção geométrica** do gradiente irrestrito sobre a classe de hipóteses restrita $\mathcal{H}$ das árvores de decisão.
- A árvore $h_m(\mathbf{x})$ induz uma partição do espaço de atributos $\mathcal{X}$ em regiões disjuntas $R_{jm}$, permitindo que a direção do gradiente aprendida no treino seja avaliada em **qualquer ponto arbitrário $\mathbf{x}$** do espaço.

### Teste V/F
- ✔ **V:** O vetor $-\mathbf{g} \in \mathbb{R}^N$ define a direção de máxima descida local da função de perda avaliada nos pontos da amostra de treino.
- ✗ **F:** Atualizar diretamente os valores nos pontos de treino geraria um vetor discreto que não possui regra de inferência para pontos fora da amostra de treino ($\mathbf{x} \notin \mathcal{D}$).
- ✔ **V:** O ajuste da árvore aos pseudo-resíduos por mínimos quadrados minimiza $\sum_{i=1}^N (r_{im} - h_m(\mathbf{x}_i))^2$, que é formalmente a projeção ortogonal do gradiente sobre o espaço de funções das árvores.
- ✔ **V:** A partição induzida pelos nós da árvore define regiões no domínio contínuo $\mathbb{R}^p$, permitindo que o modelo compute previsões para novas instâncias.

---

## Pausa Ativa 3: A Mecânica do AdaBoost e a Perda Exponencial

### Pergunta Aberta
**Cenário:** Em uma tarefa de diagnóstico clínico onde $y \in \{-1, +1\}$, o histórico médico contém $5\%$ de exames laboratoriais incorretamente rotulados devido a falhas humanas de digitação (ruído de rótulo). Um cientista treina o AdaBoost clássico com 200 iterações e nota que a acurácia de teste cai drasticamente a partir da 30ª iteração, enquanto uma Regressão Logística regularizada mantém desempenho estável. Por que a formulação matemática da função de perda do AdaBoost torna o algoritmo tão vulnerável a esse tipo de contaminação?

**Discussão e Condução Pedagógica:**
- O AdaBoost minimiza a **perda exponencial** $L(y, f) = e^{-yf}$.
- Quando um ponto é classificado incorretamente com alta margem (por exemplo, um paciente doente $y = +1$ que recebeu o rótulo corrompido $y = -1$, ou vice-versa), a quantidade $yf(\mathbf{x})$ torna-se um número negativo grande, digamos $yf(\mathbf{x}) = -4$.
- Sob a perda exponencial, a penalidade imposta é $e^{-(-4)} = e^4 \approx 54{,}6$. Se a predição for ainda mais confiante no sentido oposto, a penalidade explode exponencialmente ($e^{10} \approx 22.026$).
- Na regra de atualização dos pesos do AdaBoost, $w_i^{(m+1)} = w_i^{(m)} e^{-\alpha_m y_i h_m(\mathbf{x}_i)}$, o algoritmo multiplica repetidamente os pesos das instâncias erradas por fatores superiores a 1.
- Como esses $5\%$ de pontos rotulados incorretamente são inerentemente impossíveis de separar de forma coerente com o restante dos dados, o AdaBoost despende quase **toda a sua capacidade nas iterações seguintes tentando ajustar esses poucos pontos ruidosos**, distorcendo severamente as fronteiras de decisão e arruinando o erro de teste nas observações normais.
- A Regressão Logística (perda deviance / log-loss) penaliza erros grandes de forma **assintoticamente linear**: $- \ln(1 + e^{-yf}) \approx |yf|$ quando $yf \to -\infty$, sofrendo uma influência muito menor de pontos atípicos.

### Teste V/F
- ✔ **V:** O AdaBoost.M1 é analiticamente equivalente ao modelo aditivo em estágios progressivos (*FSAM*) minimizando a perda exponencial $L(y, f) = e^{-yf}$.
- ✔ **V:** A derivada da perda exponencial em relação a $\alpha_m$ conduz diretamente à fórmula fechada $\alpha_m = \frac{1}{2} \ln \left(\frac{1 - \text{err}_m}{\text{err}_m}\right)$.
- ✗ **F:** O peso de instâncias classificadas corretamente é multiplicado por $e^{-\alpha_m} < 1$, enquanto instâncias incorretas têm seus pesos multiplicados por $e^{+\alpha_m} > 1$.
- ✗ **F:** A perda exponencial cresce como $O(e^{|yf|})$ para erros graves, sendo exponencialmente mais sensível a outliers do que a perda logística, que cresce apenas de forma assintoticamente linear $O(|yf|)$.

---

## Pausa Ativa 4: Pseudo-Resíduos e Busca Linear nas Folhas

### Pergunta Aberta
**Cenário:** Um economista deseja modelar a renda familiar utilizando Gradient Boosting. Ele sabe que a base de dados contém bilionários com rendas ordens de magnitude superiores à média (caudas pesadíssimas). Se ele utilizar a perda quadrática $L_2$ ($L(y, f) = \frac{1}{2}(y - f)^2$), o modelo produz previsões instáveis dominadas por esses valores atípicos. Ele então substitui a perda pela perda absoluta $L_1$ ($L(y, f) = |y - f|$). Como essa mudança de perda altera a definição do pseudo-resíduo $r_{im}$ e o cálculo do valor ótimo $\gamma_{jm}$ em cada folha da árvore?

**Discussão e Condução Pedagógica:**
- A substituição da perda $L_2$ pela perda $L_1$ transforma profundamente a dinâmica do algoritmo em duas frentes fundamentais:
  1. **Definição do Pseudo-Resíduo:**
     - Para a perda $L_2$: $r_{im} = -\frac{\partial}{\partial f}\left[\frac{1}{2}(y_i - f)^2\right] = y_i - f_{m-1}(\mathbf{x}_i)$. A magnitude do resíduo escala linearmente com a distância. Para um bilionário com erro de $\$100.000.000$, o pseudo-resíduo é $+100.000.000$, dominando todo o particionamento da árvore.
     - Para a perda $L_1$: $r_{im} = -\frac{\partial}{\partial f}|y_i - f| = \text{sign}(y_i - f_{m-1}(\mathbf{x}_i)) \in \{-1, +1\}$. A magnitude do erro é completamente descartada! O pseudo-resíduo informa apenas a **direção** (se a predição atual está abaixo ou acima do valor real). Um bilionário com erro gigantesco exerce exatamente a mesma atração ($\pm 1$) que uma família comum com erro de dez centavos.
  2. **Cálculo do Valor da Folha ($\gamma_{jm}$ via busca linear):**
     - Para a perda $L_2$: $\gamma_{jm} = \arg\min_\gamma \sum_{i \in R_{jm}} \frac{1}{2}(y_i - f_{m-1}(\mathbf{x}_i) - \gamma)^2 = \frac{1}{|R_{jm}|}\sum_{i \in R_{jm}} (y_i - f_{m-1}(\mathbf{x}_i))$ (a **média amostral** dos resíduos na folha).
     - Para a perda $L_1$: $\gamma_{jm} = \arg\min_\gamma \sum_{i \in R_{jm}} |y_i - f_{m-1}(\mathbf{x}_i) - \gamma| = \text{mediana}_{\mathbf{x}_i \in R_{jm}} \{y_i - f_{m-1}(\mathbf{x}_i)\}$ (a **mediana** dos resíduos na folha).
- **Conclusão:** O estimador resultante sob $L_1$ é extraordinariamente robusto contra caudas pesadas e valores aberrantes.

### Teste V/F
- ✔ **V:** Para a perda quadrática $L_2$, o pseudo-resíduo coincide exatamente com o resíduo algébrico tradicional $r_{im} = y_i - f_{m-1}(\mathbf{x}_i)$.
- ✔ **V:** Na perda $L_1$, o gradiente negativo é a função sinal $\text{sign}(y_i - f_{m-1}(\mathbf{x}_i))$, o que impede que observações atípicas distorçam a direção da árvore base.
- ✗ **F:** O valor ótimo da folha $\gamma_{jm}$ sob a perda $L_1$ é a mediana dos resíduos na folha, e não a média.
- ✔ **V:** A perda de Huber utiliza um limiar $\delta$ para operar como mínimos quadráticos em erros menores que $\delta$ e como erro absoluto em erros maiores que $\delta$, combinando suavidade analítica com robustez a outliers.

---

## Pausa Ativa 5: Regularização, Arquitetura de Árvores e Interpretabilidade

### Pergunta Aberta
**Cenário:** Um estatístico treina um modelo de Gradient Boosting com taxa de aprendizado $\nu = 1{,}0$ e observa que com $M = 30$ árvores o modelo atinge erro mínimo no teste, mas o erro dispara a partir de $M = 50$. Um colega sugere: *"Vamos reduzir a taxa de aprendizado para $\nu = 0{,}05$ e manter exatamente as mesmas $M = 30$ árvores."* O que acontecerá com o erro de treino e teste do novo modelo? Como o número de iterações $M$ deve ser ajustado para colher os benefícios do encolhimento (*shrinkage*)?

**Discussão e Condução Pedagógica:**
- Se o pesquisador apenas reduzir $\nu$ de $1{,}0$ para $0{,}05$ mantendo $M = 30$ árvores fixas, o modelo sofrerá de **subajuste severo (*underfitting*)**.
- Com $\nu = 0{,}05$, cada árvore contribui com apenas $5\%$ da sua capacidade preditiva para o modelo global. Com apenas 30 árvores, o comitê terá percorrido uma fração ínfima da distância necessária até o mínimo da função de perda no espaço de funções. Tanto o erro de treino quanto o erro de teste serão muito piores do que no modelo anterior.
- **O Princípio do Encolhimento (Friedman, 2001):** Os parâmetros $\nu$ e $M$ operam em um tradeoff acoplado. Reduzir a taxa de aprendizado por um fator 20 ($\nu = 1{,}0 \to 0{,}05$) exige **multiplicar o número de iterações $M$ por aproximadamente 10 a 20 vezes** (por exemplo, expandir de $M = 30$ para $M = 400$ a $600$ iterações).
- Quando acompanhado desse aumento de $M$, o encolhimento $\nu \le 0{,}1$ produz uma trajetória de descida muito mais suave e estável, encontrando mínimos mais amplos e robustos na superfície de perda, o que resulta em um erro de teste significativamente menor do que qualquer modelo treinado com $\nu = 1{,}0$. A estratégia recomendada é fixar $\nu$ pequeno ($\nu \le 0{,}1$) e encontrar $M$ ótimo via parada antecipada (*early stopping*) com validação cruzada.

### Teste V/F
- ✔ **V:** O parâmetro de encolhimento $\nu \in (0, 1]$ atenua o passo de atualização de cada árvore, prevenindo o sobreajuste prematuro e atuando como um regularizador $L_2$ implícito no espaço de funções.
- ✗ **F:** Reduzir $\nu$ diminui a velocidade de convergência de cada iteração, exigindo um número $M$ estritamente maior de árvores para atingir o mesmo risco de treino.
- ✔ **V:** Conforme demonstrado por Friedman (2001), uma árvore com $J$ folhas possui no máximo $J-1$ nós internos e, portanto, pode modelar interações entre no máximo $J-1$ variáveis.
- ✔ **V:** Gráficos de Dependência Parcial (PDP) integram numericamente as variáveis complementares $X_C$, permitindo visualizar o impacto marginal isolado de uma ou duas variáveis selecionadas $X_S$ sobre a função estimada.

