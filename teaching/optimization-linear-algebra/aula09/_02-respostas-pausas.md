# Gabarito e Guia das Pausas Ativas — Aula 09: Séries de Taylor e a Regra da Cadeia Multivariada

Este documento contém o gabarito das questões de Verdadeiro/Falso e as diretrizes pedagógicas para condução das discussões das perguntas abertas em cada uma das cinco Pausas Ativas da Aula 09.

---

## Pausa Ativa 1: O Dilema da Composição e da Aproximação

### Pergunta Aberta
*Se você estivesse projetando um algoritmo para atualizar os pesos de uma rede neural profunda com 50 camadas, por que tentar derivar uma fórmula fechada explícita para cada peso individual seria inviável, e como a aproximação local contorna esse problema?*

**Diretrizes de Discussão com a Turma:**
- **Inchaço de Expressões (*Expression Swell*):** Peça aos alunos para imaginarem a expansão simbólica de uma composição de 50 funções univariadas $f_{50}(f_{49}(\dots f_1(x)\dots))$. Pela regra do produto e da cadeia, o número de nós na árvore de sintaxe abstrata cresce exponencialmente com a profundidade. Tentar escrever uma fórmula algébrica única para $\frac{\partial \mathcal{L}}{\partial W^{(1)}}$ geraria uma expressão com mais termos do que átomos no universo observável.
- **Modularidade Numérica Local:** A saída genial do cálculo diferencial aplicado à computação é nunca expandir a fórmula globalmente: avaliamos os valores numéricos intermediários camada a camada na passagem direta, e retropropagamos matrizes numéricas na passagem reversa. A aproximação local de Taylor garante que essas avaliações numéricas discretas descrevem com fidelidade a inclinação da superfície de erro ao redor do ponto atual.

### Julgamento de Verdadeiro ou Falso
- ✔ **V:** O modelo de 1ª ordem é $T_1(\mathbf{x}_0 + \mathbf{h}) = f(\mathbf{x}_0) + \nabla f(\mathbf{x}_0)^T \mathbf{h}$, que é linear em relação ao vetor de perturbação $\mathbf{h}$ e uma função afim em relação a $\mathbf{x}$.
- ✗ **F:** O aninhamento sucessivo de funções de ativação não-lineares destrói a propriedade de convexidade; as perdas em redes neurais são fortemente não-convexas, repletas de pontos de sela, mínimos locais e platôs.
- ✔ **V:** Pela própria definição analítica de diferenciabilidade de Fréchet, o resto satisfaz $\lim_{\|\mathbf{h}\| \to 0} \frac{|R_1(\mathbf{h})|}{\|\mathbf{h}\|} = 0$, o que significa que o erro decai estritamente mais rápido do que a primeira potência de $\|\mathbf{h}\|$ ($R_1 = o(\|\mathbf{h}\|)$).
- ✗ **F:** No *denominator layout* adotado no curso (e consistente com a literatura de otimização em matrizes), as derivadas de $\mathbf{f} \in \mathbb{R}^m$ por $\mathbf{x} \in \mathbb{R}^n$ formam uma matriz $n \times m$, cujas colunas são os gradientes de cada componente.

---

## Pausa Ativa 2: A Geometria de Taylor e o Passo Gradiente

### Pergunta Aberta
*Se a aproximação de 2ª ordem $T_2$ inclui a Hessiana e captura a curvatura, por que não minimizamos diretamente $T_2$ a cada iteração em vez de usar a aproximação linear com penalidade $T_1 + \frac{1}{2\alpha}\|\mathbf{h}\|^2$?*

**Diretrizes de Discussão com a Turma:**
- **Derivação do Passo de Newton:** Mostre no quadro que minimizar $T_2(\mathbf{x}_0 + \mathbf{h}) = f(\mathbf{x}_0) + \nabla f^T \mathbf{h} + \frac{1}{2}\mathbf{h}^T H \mathbf{h}$ igualando a zero resulta em $\nabla_{\mathbf{h}} T_2 = \nabla f + H\mathbf{h} = \mathbf{0} \implies \mathbf{h} = -H^{-1}\nabla f$.
- **Gargalo Computacional de Memória e Tempo:** Para um vetor de parâmetros com $d = 10^7$ (típico de redes moderadas), armazenar $H \in \mathbb{R}^{d \times d}$ exigiria $10^{14}$ floats ($400\text{ Terabytes}$ de RAM), e resolver o sistema linear $H\mathbf{h} = -\nabla f$ custaria $O(d^3) \approx 10^{21}$ operações por iteração!
- **Instabilidade em Pontos de Sela:** Em problemas não-convexos, $H$ possui autovalores negativos. Minimizar uma forma quadrática indefinida é ilimitado e saltar para o ponto crítico pode atrair o otimizador para um máximo local ou sela.

### Julgamento de Verdadeiro ou Falso
- ✔ **V:** Pelo Lema da Descida quadrático provado na Aula 8, a $L$-suavidade de Lipschitz implica diretamente que a função é limitada superiormente por uma parábola com curvatura $L$, garantindo $|R_1(\mathbf{h})| \le \frac{L}{2}\|\mathbf{h}\|_2^2$.
- ✗ **F:** A função $T_1(\mathbf{x}_0 + \mathbf{h})$ é um hiperplano; ao caminhar na direção $-\nabla f(\mathbf{x}_0)$ com passo tendendo ao infinito, o valor tende a $-\infty$. Sem um termo de penalidade proximal ou restrição de caixa, não há mínimo finito.
- ✔ **V:** Se $H = \nabla^2 f(\mathbf{x}_0) \succ 0$, a Hessiana é estritamente convexa e invertível, de modo que seu único minimizador é $\mathbf{h} = -H^{-1}\nabla f$.
- ✔ **V:** Como uma forma quadrática é um polinômio de grau 2, todas as derivadas parciais de ordem 3 ou superior são nulas em qualquer ponto, anulando exatamente o termo de resto $R_2(\mathbf{h})$.

---

## Pausa Ativa 3: A Mecânica Tensorial da Regra da Cadeia

### Pergunta Aberta
*Se tivermos uma composição de 4 funções vetoriais $\mathbf{x}_0 \xrightarrow{\mathbf{f}_1} \mathbf{x}_1 \xrightarrow{\mathbf{f}_2} \mathbf{x}_2 \xrightarrow{\mathbf{f}_3} \mathbf{x}_3 \xrightarrow{L} \mathbb{R}$, o produto associativo de matrizes nos permite multiplicar os Jacobianos da esquerda para a direita ou da direita para a esquerda. Qual dessas duas ordens é ordens de grandeza mais barata computacionalmente e por quê?*

**Diretrizes de Discussão com a Turma:**
- **Associatividade de Matrizes:** O produto $A B C \mathbf{v}$ pode ser calculado como $( (A B) C ) \mathbf{v}$ ou $A ( B ( C \mathbf{v} ) )$.
- **Custo Flops:** Se cada dimensão intermediária for $d$, multiplicar matriz-matriz custa $O(d^3)$ operações. Como a perda $L$ é um escalar ($p=1$), seu gradiente é um vetor coluna $d \times 1$. Começar pela direita e retroceder realiza apenas produtos matriz-vetor $O(d^2)$.
- **Destaque:** Isso antecipa o coração da Aula 10: a passagem reversa (*reverse-mode autodiff*) é infinitamente superior à passagem progressiva (*forward-mode*) para funções escalares de muitas variáveis!

### Julgamento de Verdadeiro ou Falso
- ✔ **V:** Na convenção *denominator layout*, a $j$-ésima coluna armazena $\nabla_{\mathbf{x}} f_j \in \mathbb{R}^n$.
- ✔ **V:** Para $\mathbf{u} = A\mathbf{x}$, cada $u_j = \sum_k A_{jk} x_k$. Assim, $\frac{\partial u_j}{\partial x_i} = A_{ji}$, o que corresponde à transposta $A^T$.
- ✔ **V:** A regra da cadeia multivariada expressa a composição de operadores diferenciais lineares tangentes.
- ✗ **F:** No *numerator layout* (usado no livro MathML), o gradiente de um escalar por um vetor coluna é definido como um vetor linha $1 \times n$.

---

## Pausa Ativa 4: A Dinâmica da Retropropagação Algébrica

### Pergunta Aberta
*O que acontece com o vetor de sensibilidade $\boldsymbol{\delta}^{(l)}$ se as ativações da camada $\mathbf{z}^{(l)}$ estiverem em uma região onde a função logística satura ($\sigma(z) \approx 1$ ou $\sigma(z) \approx 0$)? Como isso afeta o treinamento das camadas iniciais de uma rede profunda?*

**Diretrizes de Discussão com a Turma:**
- **Derivada da Sigmoide:** Lembre que $\sigma'(z) = \sigma(z)(1 - \sigma(z))$. Se $z = 5$, $\sigma(z) \approx 0{,}993 \implies \sigma'(z) \approx 0{,}006$.
- **Cadeia Multiplicativa:** A fórmula recursiva $\boldsymbol{\delta}^{(l)} = \big((W^{(l+1)})^T \boldsymbol{\delta}^{(l+1)}\big) \odot \sigma'(\mathbf{z}^{(l)})$ multiplica esse fator diminuto a cada camada. Ao longo de 5 camadas saturadas, o sinal de erro é atenuado por $(10^{-2})^5 = 10^{-10}$.
- **Consequência:** As primeiras camadas da rede ($\boldsymbol{\delta}^{(1)}$) recebem gradientes nulos e seus pesos $W^{(1)}$ congelam no tempo, inviabilizando o aprendizado.

### Julgamento de Verdadeiro ou Falso
- ✔ **V:** Para uma única amostra, $\nabla_{W^{(l)}}\mathcal{L} = \boldsymbol{\delta}^{(l)} (\mathbf{a}^{(l-1)})^T$. O produto externo de dois vetores não-nulos possui posto exatamente 1.
- ✗ **F:** A preservação de norma euclidiana em transformações lineares gerais (matrizes retangulares) exige que todos os valores singulares da matriz sejam iguais a 1 (isometria), não autovalores.
- ✔ **V:** Para $z > 0$, a derivada da ReLU é exatamente 1; logo, ela atua como um condutor perfeito de sensibilidade, sem atenuar o erro retropropagado.
- ✗ **F:** Pela derivação, $\nabla_{\mathbf{b}^{(l)}}\mathcal{L} = \boldsymbol{\delta}^{(l)}$, sem dependência direta de $\mathbf{a}^{(l-1)}$.

---

## Pausa Ativa 5: O Alcance dos Modelos Locais

### Pergunta Aberta
*Se o modelo quadrático $T_2$ prevê a perda com tanta precisão para passos maiores do que $T_1$, por que na prática de Deep Learning ainda realizamos centenas de milhares de passos minúsculos de primeira ordem ($\alpha \sim 10^{-3}$) em vez de passos largos de segunda ordem?*

**Diretrizes de Discussão com a Turma:**
- **Conecte com a Prática:** Reitere os dois fatores fundamentais: custo $O(d^3)$ para inverter a Hessiana e não-convexidade (autovalores negativos empurrando para o infinito).
- **Estocasticidade:** Em aprendizado de máquina, avaliamos o gradiente em mini-batches ruidosos. Calcular uma Hessiana ruidosa de tamanho colossal seria um desperdício monstruoso de computação.

### Julgamento de Verdadeiro ou Falso
- ✔ **V:** Como $|R_1(\mathbf{h})| \le C \|\mathbf{h}\|^2$, tomando logaritmo em ambos os lados obtemos $\log |R_1| \le \log C + 2 \log \|\mathbf{h}\|$, que define uma reta de inclinação 2 em escala log-log.
- ✗ **F:** A diferença finita progressiva simples $\frac{f(x+\epsilon)-f(x)}{\epsilon}$ possui erro de truncamento de primeira ordem $\mathcal{O}(\epsilon)$; a diferença finita **central** $\frac{f(x+\epsilon)-f(x-\epsilon)}{2\epsilon}$ é que atinge precisão $\mathcal{O}(\epsilon^2)$.
- ✔ **V:** Um hiperplano não tem limite inferior. Se tomarmos um passo na direção de descida $-\nabla \mathcal{L}$ suficientemente grande, $T_1$ pode assumir valores arbitrariamente negativos, contrariando a positividade intrínseca de uma perda quadrática.
- ✔ **V:** É a definição formal da derivada direcional de segunda ordem ao longo de um vetor unitário $\mathbf{v}$.

