## Resumo — Aula 14

Nas treze primeiras aulas deste curso, todas as formulações de otimização contínua basearam-se em uma premissa fundamental de cálculo multivariado: a **suavidade (diferenciabilidade)** da função de perda. Assumimos que o gradiente $\nabla f(\mathbf{w})$ existia em todos os pontos do domínio e que suas variações eram limitadas pela constante de Lipschitz ($L$-suavidade).

Entretanto, em problemas modernos de Aprendizado de Máquina, funções **não-suaves (não-diferenciáveis)** são indispensáveis. A mais célebre delas é a regularização com **norma $L_1$ (Lasso)**: $\|\mathbf{w}\|_1 = \sum_{i=1}^d |w_i|$. Ao contrário da regularização $L_2$ (Ridge), que apenas contrai os parâmetros continuamente sem nunca zerá-los, a norma $L_1$ possui a propriedade extraordinária de induzir **esparsidade exata**, zerando coeficientes irrelevantes e realizando seleção automática de atributos e compressão de modelos. Outros exemplos ubíquos incluem a perda com margem *Hinge Loss* em Support Vector Machines (SVM) e funções de ativação ReLU ($\max(0, x)$).

Esta aula estabelece a fundamentação matemática rigorosa para otimizar funções convexas não-suaves. No Bloco 1, examinamos a geometria de superfícies com "bicos" e descontinuidades de derivada, generalizando o conceito de gradiente para o **Subgradiente** e o **Subdiferencial** ($\partial f(\mathbf{w})$), e deduzindo a condição de otimalidade de Fermat generalizada ($\mathbf{0} \in \partial f(\mathbf{w}^\star)$). No Bloco 2, analisamos o **Método do Subgradiente clássico**, explicando por que subgradientes não são necessariamente direções de descida local e por que a convergência é inevitavelmente lenta ($\mathcal{O}(1/\sqrt{k})$). No Bloco 3, introduzimos a ferramenta conceitual mais elegante da análise convexa moderna: o **Operador Proximal** ($\text{prox}_h(\mathbf{w})$). Deduzimos passo a passo o operador de **Encolhimento Suave (*Soft-Thresholding*)** para a norma $L_1$, provando algebricamente por que ele projeta coordenadas pequenas estritamente em zero. Por fim, no Bloco 4, resolvemos problemas de **Otimização Composta** ($F(\mathbf{w}) = g(\mathbf{w}) + h(\mathbf{w})$) através dos algoritmos **ISTA** (*Iterative Shrinkage-Thresholding Algorithm*) e **FISTA** (*Fast ISTA*, Beck & Teboulle, 2009), que combina a aceleração de Nesterov com operadores proximais para atingir a cota teórica ótima $\mathcal{O}(1/k^2)$ na indução de esparsidade.

**Objetivos:**
1. Compreender a falha do gradiente clássico em pontos não-suaves e formalizar a definição geométrica de subgradientes e subdiferenciais de funções convexas.
2. Derivar a condição necessária e suficiente de otimalidade para funções convexas não-diferenciáveis ($\mathbf{0} \in \partial f(\mathbf{w}^\star)$) e aplicá-la à norma $L_1$ e ao Hinge Loss.
3. Analisar o comportamento do Método do Subgradiente, demonstrando por que taxas de aprendizado decrescentes são obrigatórias e por que sua taxa de convergência é $\mathcal{O}(1/\sqrt{k})$.
4. Derivar analiticamente a formulação do Operador Proximal e provar que o operador proximal da norma $L_1$ é o operador de *Soft-Thresholding*.
5. Implementar e contrastar os algoritmos ISTA e FISTA para regressão Lasso, demonstrando como a inércia de Nesterov acelera a convergência em problemas compostos de $\mathcal{O}(1/k)$ para $\mathcal{O}(1/k^2)$.

**Pré-requisitos:**
- Gradiente, Lema da Descida e suavidade Lipschitz (Aula 8).
- Convexidade, epígrafes e condições de primeira ordem (Aula 7).
- Gradiente Acelerado de Nesterov (Aula 12).
- Álgebra Linear: Produto interno euclidiano, projeções ortogonais e normas $L_1$ e $L_2$ (Aula 1).

**Problema-fio:** Regressão linear esparsa em alta dimensão ($d \gg N$), onde centenas de atributos irrelevantes devem ser rigorosamente zerados pelo Lasso, comparando o fracasso do SGD clássico em induzir zeros exatos com o sucesso do ISTA e a aceleração extrema do FISTA.

**Estratégia Pedagógica:** B (Inside-Out com Problema-Fio) — da falha da derivada em $w=0$ na regularização $L_1$ ao conceito geométrico de hiperplanos de suporte (subgradientes), superando a lentidão do método ingênuo através da formulação proximal do *Soft-Thresholding* e sua aceleração por FISTA.

---

## Plano de aula — Aula 14 (carga horária: ~110 min)

1. **Revisão e Introdução** (~12 min)
   - *Revisão:* Da Aula 12 e 13 (otimizadores acelerados e estruturados sob perdas diferenciáveis).
   - *A Pergunta Crítica:* Todos os algoritmos anteriores dependiam de $\nabla f(\mathbf{w})$. O que acontece quando adicionamos à perda a penalidade $L_1$ ($\lambda \sum |w_i|$) para selecionar atributos relevantes?
   - *Problema Motivador:* Conjunto de dados biomédicos com $d = 1.000$ biomarcadores e apenas $N = 100$ pacientes. Apenas 10 biomarcadores causam a doença. O Ridge ($L_2$) atribui valores pequenos e não-nulos a todos os 1.000 genes; o Lasso ($L_1$) deveria zerar exatamente os 990 irrelevantes, mas como derivar em zero?
   - *Roteiro (4 Perguntas Centrais):*
     1. Como definir inclinações e direções em pontos onde o gradiente clássico não existe?
     2. Por que o Método do Subgradiente não garante descida monótona e converge a apenas $\mathcal{O}(1/\sqrt{k})$?
     3. O que é o Operador Proximal e como a dedução do *Soft-Thresholding* prova a indução de zeros exatos na norma $L_1$?
     4. Como o algoritmo FISTA combina operadores proximais com a aceleração de Nesterov para atingir convergência $\mathcal{O}(1/k^2)$?
   - *Pausa 1.*

2. **Intuição — A Geometria do Bico e Hiperplanos de Suporte** (~8 min)
   - Em uma curva suave, o plano tangente toca a função em um único ponto e permanece abaixo dela.
   - Em um "bico" (como $f(w) = |w|$ em $w = 0$), não há uma reta tangente única: há um **leque infinito de retas de suporte** que permanecem abaixo da função.
   - Cada inclinação válida dessa família de retas é um **subgradiente**; a reunião de todas elas é o **subdiferencial**.

3. **Bloco 1: Subgradientes, Subdiferenciais e Otimalidade de Fermat** (~25 min)
   - Definição formal: $\mathbf{g} \in \partial f(\mathbf{w}) \iff f(\mathbf{u}) \ge f(\mathbf{w}) + \mathbf{g}^T (\mathbf{u} - \mathbf{w}) \quad \forall \mathbf{u}$.
   - O subdiferencial do valor absoluto: $\partial |w| = \begin{cases} \{1\}, & w > 0 \\ [-1, 1], & w = 0 \\ \{-1\}, & w < 0 \end{cases}$.
   - Subdiferencial da norma $L_1$: produto cartesiano coordenada a coordenada.
   - Subdiferencial do Hinge Loss ($\max(0, 1 - y \mathbf{w}^T \mathbf{x})$).
   - Regra de Fermat Generalizada: $\mathbf{0} \in \partial f(\mathbf{w}^\star)$ como condição necessária e suficiente para convexas.

4. **Bloco 2: O Método do Subgradiente e o Preço da Não-Suavidade** (~20 min)
   - Atualização: $\mathbf{w}_{k+1} = \mathbf{w}_k - \alpha_k \mathbf{g}_k$ com $\mathbf{g}_k \in \partial f(\mathbf{w}_k)$.
   - O paradoxo: $-\mathbf{g}_k$ não é necessariamente uma direção de descida local ($f(\mathbf{w}_{k+1}) > f(\mathbf{w}_k)$ pode ocorrer!).
   - O que decresce? A distância ao ótimo: $\|\mathbf{w}_{k+1} - \mathbf{w}^\star\|^2 \le \|\mathbf{w}_k - \mathbf{w}^\star\|^2 - 2\alpha_k (f(\mathbf{w}_k) - f^\star) + \alpha_k^2 \|\mathbf{g}_k\|^2$.
   - A necessidade de passos decrescentes (Robbins-Monro): $\sum \alpha_k = \infty$ e $\sum \alpha_k^2 < \infty$.
   - Cota de complexidade: $\mathcal{O}(1/\sqrt{k})$ passos para atingir erro $\epsilon$, tornando o subgradiente lento em problemas de grande porte.

5. **Bloco 3: Operadores Proximais e o Encolhimento Suave (*Soft-Thresholding*)** (~25 min)
   - A ideia proximal de Moreau (1965): substituir aproximação linear local por minimização quadrática regularizada.
   - Definição formal: $\text{prox}_{\gamma h}(\mathbf{w}) = \arg\min_{\mathbf{z}} \left( h(\mathbf{z}) + \frac{1}{2\gamma} \|\mathbf{z} - \mathbf{w}\|_2^2 \right)$.
   - Resolução analítica completa para $h(z) = \lambda |z|$:
     $$0 \in \frac{1}{\gamma}(z - w) + \lambda \partial |z| \implies z = \mathcal{S}_{\gamma \lambda}(w)$$
   - A fórmula do *Soft-Thresholding*:
     $$\mathcal{S}_{\gamma \lambda}(w) = \text{sign}(w) \max(|w| - \gamma \lambda, 0)$$
   - Contraste visual e algébrico entre Ridge ($L_2$: contração linear) e Lasso ($L_1$: contração com zona morta que zera coordenadas!).

6. **Bloco 4: Otimização Composta: ISTA e FISTA** (~15 min)
   - O problema composto: $\min_{\mathbf{w}} F(\mathbf{w}) = g(\mathbf{w}) + h(\mathbf{w})$ ($g$ suave, $h$ não-suave simples).
   - O algoritmo **ISTA**:
     $$\mathbf{w}_{k+1} = \text{prox}_{\alpha h}(\mathbf{w}_k - \alpha \nabla g(\mathbf{w}_k)) = \mathcal{S}_{\alpha \lambda}(\mathbf{w}_k - \alpha \nabla g(\mathbf{w}_k))$$
     Taxa de convergência: $\mathcal{O}(1/k)$.
   - O algoritmo **FISTA** (Beck & Teboulle, 2009):
     Incorpora o momentum de Nesterov $\beta_k = \frac{k-1}{k+2}$ no ponto antes da etapa proximal!
     $$\mathbf{y}_k = \mathbf{w}_k + \frac{k-1}{k+2}(\mathbf{w}_k - \mathbf{w}_{k-1})$$
     $$\mathbf{w}_{k+1} = \text{prox}_{\alpha h}(\mathbf{y}_k - \alpha \nabla g(\mathbf{y}_k))$$
     Recupera a cota ótima $\mathcal{O}(1/k^2)$ mesmo com regularizadores não-diferenciáveis!

7. **Fechamento e Conclusão do Curso** (~5 min)
   - Retrospectiva completa: Da geometria euclidiana da Aula 1 à otimização proximal da Aula 14.
   - A grande síntese da disciplina: Álgebra Linear e Otimização formam as duas faces inseparáveis da mesma moeda computacional em Machine Learning!
