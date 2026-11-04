# Respostas das Pausas Ativas — Aula 11: Máquinas de Vetores de Suporte (SVM)

Este documento contém o gabarito detalhado, as discussões analíticas das perguntas abertas e as diretrizes pedagógicas para a condução das 5 Pausas Ativas da Aula 11.

---

## Pausa Ativa 1: A Ruptura com a Verossimilhança e o Hiperplano Canônico

### Pergunta Aberta
**Cenário:** Em uma aplicação de diagnóstico médico, a Regressão Logística estima que um novo paciente tem probabilidade estimada $\hat{p} = 0{,}51$ de apresentar nódulo maligno, enquanto uma SVM Linear treinada no mesmo conjunto classifica o paciente como benigno com escore de margem $f(\mathbf{x}) = +0{,}85$. Explique conceitualmente por que esses dois modelos lineares podem produzir decisões divergentes mesmo tendo acesso aos mesmos dados.

**Discussão e Condução Pedagógica:**
- A divergência entre os modelos resulta diretamente de suas funções de perda e critérios de otimização epistemologicamente distintos:
  1. **Regressão Logística (Máxima Verossimilhança):** A perda de entropia cruzada avalia a probabilidade $p(y \mid \mathbf{x}) = \sigma(\mathbf{w}^T \mathbf{x} + b)$ sobre **todas as $N$ observações do conjunto de treinamento**. Cada ponto exerce uma força atrativa proporcional ao resíduo de probabilidade $y_i - p_i$. Se houver uma nuvem massiva de pacientes malignos localizados muito longe da fronteira de decisão, essa densidade populacional puxará o vetor de pesos e o limiar para acomodar melhor a calibração global das probabilidades.
  2. **SVM Linear (Margem Máxima):** A SVM abandona a modelagem da densidade populacional global. Pela condição KKT, pontos situados no interior das classes possuem multiplicadores de Lagrange nulos ($\alpha_i = 0$), sendo **completamente ignorados pelo algoritmo**. A orientação de $\mathbf{w}$ e o valor de $b$ são determinados unicamente pelas amostras que repousam sobre as margens canônicas (os vetores de suporte).
- Como consequência, em regiões limítrofes onde os dados apresentam ligeira assimetria de densidade ou classes desbalanceadas, o centro de massa da Regressão Logística desloca a fronteira de decisão, enquanto a SVM mantém o hiperplano rigorosamente centralizado no corredor geométrico de maior folga entre as classes.

### Teste V/F
- ✗ **F:** Em conjuntos de dados linearmente separáveis, a função de verossimilhança da regressão logística sem regularização não possui ponto crítico finito; o algoritmo diverge com $\|\mathbf{w}\| \to \infty$ na tentativa de saturar as probabilidades em 0 e 1. A SVM, por outro lado, possui uma formulação quadrática com mínimo único e finito que maximiza a margem geométrica.
- ✔ **V:** A distância ortogonal euclidiana de qualquer ponto ao hiperplano afim é dada pela fórmula analítica $d = \frac{|\mathbf{w}^T \mathbf{x} + b|}{\|\mathbf{w}\|}$, dependendo inversamente da norma $\|\mathbf{w}\|$.
- ✔ **V:** Pela teoria da dualidade e pelas condições de Karush-Kuhn-Tucker, apenas os pontos com multiplicadores estritamente positivos ($\alpha_i > 0$) compõem o vetor de pesos $\mathbf{w} = \sum \alpha_i y_i \mathbf{x}_i$. Observações com $y_i(\mathbf{w}^T \mathbf{x}_i + b) > 1$ têm $\alpha_i = 0$ e não exercem força alguma sobre o hiperplano.
- ✗ **F:** O resultado clássico da Teoria do Aprendizado Estatístico de Vapnik demonstra que a Dimensão VC de um hiperplano de margem canônica com margem geométrica $\gamma$ sobre uma esfera de raio $R$ satisfaz $h \le \min\left(d, \left\lceil \frac{R^2}{\gamma^2} \right\rceil\right) + 1$. Portanto, a capacidade de generalização é controlada fundamentalmente pela margem geométrica $\gamma$, podendo ser finita mesmo quando a dimensão do espaço de entrada for imensa ou infinita.

---

## Pausa Ativa 2: Dualidade de Lagrange e Esparsidade dos Vetores de Suporte

### Pergunta Aberta
**Cenário:** Imagine que após treinar uma SVM de margem rígida em um banco com $N = 100.000$ transações financeiras, identificamos que exatamente 42 amostras são vetores de suporte ($\alpha_i > 0$). Se um operador acidentalmente deletar $50.000$ observações do conjunto de treino que possuíam $\alpha_i = 0$ e retreinar a SVM do zero nas $50.000$ restantes, o que acontecerá com os parâmetros $(\mathbf{w}, b)$ do hiperplano final?

**Discussão e Condução Pedagógica:**
- Os parâmetros $(\mathbf{w}, b)$ permanecerão **rigorosamente idênticos**.
- Em otimização convexa sob restrições de desigualdade, as condições KKT dividem as restrições em ativas (aquelas que se mantêm como igualdade no ponto ótimo, $g_i(\mathbf{w}) = 0$) e inativas (aquelas estritamente satisfeitas como desigualdade estrita, $g_i(\mathbf{w}) > 0$).
- As observações com $\alpha_i = 0$ correspondem a restrições inativas. Elas não limitam a região viável em torno do ótimo e não fornecem nenhuma contribuição para a combinação linear que define $\mathbf{w} = \sum_{i \in \text{SV}} \alpha_i y_i \mathbf{x}_i$.
- Remover qualquer subconjunto de restrições inativas de um programa quadrático convexo preserva o mesmo ponto de mínimo global. Essa é a base teórica da **esparsidade extrema da SVM**.

### Teste V/F
- ✔ **V:** Como $\alpha_i = 0$ para todos os pontos fora da margem canônica, a expansão primal $\mathbf{w} = \sum_{i=1}^N \alpha_i y_i \mathbf{x}_i$ colapsa exatamente na soma restrita aos vetores de suporte $\sum_{i \in \text{SV}} \alpha_i y_i \mathbf{x}_i$.
- ✔ **V:** Na formulação dual de Wolfe, $\max_{\boldsymbol{\alpha}} \sum \alpha_i - \frac{1}{2} \sum \sum \alpha_i \alpha_j y_i y_j \langle \mathbf{x}_i, \mathbf{x}_j \rangle$, a dimensão $d$ do espaço de entrada intervém exclusivamente no cálculo prévio da matriz de Gram $G_{ij} = \langle \mathbf{x}_i, \mathbf{x}_j \rangle$. Uma vez calculada, a otimização depende apenas de $N$.
- ✗ **F:** Pela condição de folga complementar KKT, $\alpha_i [y_i(\mathbf{w}^T \mathbf{x}_i + b) - 1] = 0$. Se $\alpha_i > 0$, o termo entre colchetes deve ser zero, o que significa que o ponto repousa exatamente sobre a margem canônica, tendo distância ortogonal igual a exatamente $1/\|\mathbf{w}\|$.
- ✗ **F:** O termo independente $b$ não é governado pelo maior multiplicador $\alpha_i$. Qualquer vetor de suporte livre $j$ satisfaz $y_j(\mathbf{w}^T \mathbf{x}_j + b) = 1$, donde $b = y_j - \mathbf{w}^T \mathbf{x}_j$. Na prática computacional, calcula-se a média sobre todos os vetores de suporte para atenuar imprecisões numéricas de ponto flutuante.

---

## Pausa Ativa 3: Margem Suave, Perda Hinge e o Hiperparâmetro $C$

### Pergunta Aberta
**Cenário:** Compare a curva da Perda Hinge com a curva da Perda Logística para $z = y \cdot f(\mathbf{x}) \ge 2$. O que acontece com o gradiente de cada função nessa região e como esse comportamento matemático explica por que a SVM possui soluções esparsas enquanto a Regressão Logística é obrigada a manter coeficientes dependentes de todas as amostras?

**Discussão e Condução Pedagógica:**
- Para uma amostra bem classificada e situada com folga além da margem de decisão ($z = y f(\mathbf{x}) \ge 1$):
  1. **Perda Hinge:** A função vale $L_{\text{hinge}}(z) = \max(0, 1 - z) = 0$. Sua derivada é identicamente **zero** ($\frac{d L}{dz} = 0$). Isso significa que essa observação não produz força restauradora nem gradiente; no problema dual, seu multiplicador é exatamente $\alpha_i = 0$. Ela torna-se perfeitamente invisível para o modelo final.
  2. **Perda Logística:** A função vale $L_{\text{logistic}}(z) = \ln(1 + e^{-z})$. Para $z = 2$, a perda vale $\approx 0{,}127$; sua derivada é $-\frac{e^{-z}}{1 + e^{-z}} \approx -0{,}119$. Mesmo para $z = 10$, a derivada vale $-e^{-10} \approx -4{,}5 \times 10^{-5} \neq 0$.
- Essa derivada estritamente não nula da perda logística obriga o algoritmo de Máxima Verossimilhança a ajustar infinitesimalmente os pesos para acomodar cada uma das $N$ amostras do banco de dados, destruindo qualquer possibilidade de esparsidade matemática.

### Teste V/F
- ✗ **F:** A variável de folga $\xi_i$ mede a violação da margem canônica. Para $0 < \xi_i \le 1$, o ponto penetrou no corredor de margem, mas sua margem funcional ainda é não negativa ($y_i f(\mathbf{x}_i) \ge 0$), logo ele está classificado corretamente. Erros de classificação ocorrem exclusivamente se $\xi_i > 1$.
- ✔ **V:** Quando $C \to \infty$, o modelo impõe penalização drástica a qualquer valor de $\xi_i > 0$, aproximando-se da margem rígida. Isso reduz a margem geométrica e torna o hiperplano refém de flutuações e ruídos locais, elevando a variância e o risco de overfitting.
- ✔ **V:** No problema dual da margem suave, as condições KKT estabelecem que $\alpha_i + \mu_i = C$ e $\mu_i \xi_i = 0$. Se $0 < \alpha_i < C$, temos necessariamente $\mu_i > 0$, o que força $\xi_i = 0$. Esse ponto é um vetor de suporte livre que toca perfeitamente a margem.
- ✗ **F:** A perda Hinge possui uma quina não diferenciável no ponto de transição $z = 1$, onde a derivada lateral à esquerda é $-1$ e a derivada lateral à direita é $0$. Por isso, sua otimização requer subgradientes ou formulação em programação quadrática cônica/dual.

---

## Pausa Ativa 4: O Truque do Kernel e a Geometria do Espaço de Hilbert

### Pergunta Aberta
**Cenário:** Um analista de dados afirma: *"Já que o Kernel RBF projeta os dados em um espaço de dimensão infinita, qualquer conjunto de dados com $N$ observações se tornará linearmente separável; logo, podemos dispensar as variáveis de folga $\xi_i$ e usar sempre $C \to \infty$."* Explique o erro conceitual dessa afirmação e descreva o que acontecerá com a fronteira de decisão se os dados contiverem rótulos com ruído.

**Discussão e Condução Pedagógica:**
- A afirmação confunde **capacidade representacional de interpolação** com **generalização estatística**:
  1. É matematicamente verdadeiro que, com um kernel RBF gaussiano e sem pontos com atributos idênticos e rótulos opostos, a matriz de Gram é estritamente definida positiva e tem posto completo $N$, tornando qualquer amostra de tamanho finito separável por um hiperplano no espaço de Hilbert $\ell^2$.
  2. No entanto, em conjuntos reais com ruído de rótulo ou sobreposição inerente de distribuições, forçar $C \to \infty$ obrigará o modelo a encontrar um hiperplano em $\mathcal{H}$ que classifique perfeitamente até mesmo os outliers corrompidos.
  3. No espaço de entrada original $\mathbb{R}^d$, isso se manifesta como o surgimento de pequenas "ilhas de decisão" fechadas e estreitas contornando cada ponto ruidoso isolado.
  4. Essa contorção violenta destrói a largura da margem geométrica de segurança, resultando em um modelo com variância catastrófica que falhará miseravelmente em novos dados de teste.
- O parâmetro $C$ (e a formulação de margem suave com folgas $\xi_i$) continua sendo indispensável mesmo em dimensão infinita para permitir que ruídos sejam ignorados em prol de uma fronteira de decisão suave e generalizável.

### Teste V/F
- ✗ **F:** Pelo Teorema de Mercer, para que uma função contínua simétrica $k(\mathbf{x}, \mathbf{z})$ defina um produto interno em um espaço de Hilbert, a matriz de Gram $K_{ij} = k(\mathbf{x}_i, \mathbf{x}_j)$ deve ser **semidefinida positiva (PSD)**; portanto, todos os seus autovalores devem ser **maiores ou iguais a zero** ($\lambda_i \ge 0$).
- ✔ **V:** No kernel RBF $k(\mathbf{x}, \mathbf{z}) = \exp(-\gamma \|\mathbf{x} - \mathbf{z}\|^2)$, quando $\mathbf{x} = \mathbf{z}$, a distância euclidiana é nula e a exponencial atinge seu valor unitário máximo $\exp(0) = 1$. Conforme a separação euclidiana $\|\mathbf{x} - \mathbf{z}\|$ cresce, a função decai suavemente em direção a zero.
- ✔ **V:** Quando $\gamma \to \infty$, a largura da função de base radial $\sigma = \frac{1}{\sqrt{2\gamma}}$ colapsa para zero. Cada vetor de suporte passa a influenciar apenas uma vizinhança microscópica ao seu redor, criando bolhas fechadas e fragmentadas que memorizam o treino.
- ✗ **F:** A inferência da SVM com kernel requer avaliar $f(\mathbf{x}) = \sum_{i \in \text{SV}} \alpha_i y_i k(\mathbf{x}_i, \mathbf{x}) + b$. Essa operação requer avaliar a função escalar $k$ exatamente $N_{\text{SV}}$ vezes no espaço original $\mathbb{R}^d$, com custo $O(N_{\text{SV}} \cdot d)$, sendo completamente independente da dimensão do espaço de Hilbert transformado.

---

## Pausa Ativa 5: Calibração de Platt e o Tubo de Insensibilidade da SVR

### Pergunta Aberta
**Cenário:** Na Support Vector Regression ($\varepsilon$-SVR), o cientista decide configurar o raio do tubo $\varepsilon = 0$. O que acontece com a esparsidade da solução resultante? O modelo ainda desfrutará da propriedade de ignorar observações não informativas?

**Discussão e Condução Pedagógica:**
- Ao fixar $\varepsilon = 0$, a função de perda $\varepsilon$-insensível simplifica-se para:
  $$L_{\varepsilon=0}(y, f(\mathbf{x})) = \max(0, |y - f(\mathbf{x})| - 0) = |y - f(\mathbf{x})|$$
  que é a clássica **perda em valor absoluto ($L_1$)**.
- O tubo de insensibilidade colapsa para uma linha de espessura nula. Consequentemente:
  1. Apenas pontos cujo resíduo numérico seja rigorosamente zero ($y_i = f(\mathbf{x}_i)$) estarão isentos de penalidade.
  2. Como os dados contêm ruído contínuo, a probabilidade amostral de um ponto ter erro exatamente igual a zero é nula.
  3. Portanto, praticamente **todas as $N$ observações do conjunto de treinamento violarão o tubo e receberão multiplicadores de Lagrange $\alpha_i > 0$ ou $\alpha_i^* > 0$**.
  4. A **esparsidade é completamente destruída**: o número de vetores de suporte salta para aproximadamente $100\%$ das amostras de treino ($N_{\text{SV}} \approx N$).
- Isso transforma a inferência computacional em um processo tão custoso quanto o de métodos não paramétricos globais, anulando a elegância e eficiência estrutural da SVR.

### Teste V/F
- ✗ **F:** Ajustar os coeficientes $A$ e $B$ da sigmoide de Platt sobre os próprios escores obtidos no conjunto de treino causa grave vazamento de dados (*data leakage*). Como a SVM maximizou a separação no treino, os escores de treino são artificialmente inflados, levando a sigmoide a gerar probabilidades superestimadas e com péssima calibração em teste. Platt (1999) estipula o uso obrigatório de validação cruzada out-of-fold.
- ✔ **V:** Na formulação da $\varepsilon$-SVR, a condição KKT estabelece que $\alpha_i (|y_i - f(\mathbf{x}_i)| - \varepsilon - \xi_i) = 0$. Para observações dentro do tubo ($|y_i - f(\mathbf{x}_i)| < \varepsilon$), a folga é $\xi_i = 0$ e a restrição de violação está inativa, o que obriga $\alpha_i = \alpha_i^* = 0$.
- ✗ **F:** O escore $f(\mathbf{x})$ é puramente uma distância métrica ao hiperplano multiplicada pela norma de $\mathbf{w}$. Não possui propriedades axiomáticas de probabilidade (não integra 1, pode ser menor que zero ou maior que um, e não reflete a densidade a posteriori). A calibração (Platt ou isotônica) é indispensável para uso probabilístico.
- ✔ **V:** Quanto maior o valor de $\varepsilon$, mais largo é o tubo de tolerância cilíndrico em torno da função estimada. Mais observações têm seus resíduos absorvidos dentro da tolerância sem custo de perda, resultando em menos pontos fora da margem e, portanto, em um número menor de vetores de suporte (maior esparsidade).

