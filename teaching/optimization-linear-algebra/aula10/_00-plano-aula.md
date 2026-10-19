## Resumo — Aula 10

A Aula 9 derivou a Regra da Cadeia Multivariada e deduziu as equações de retropropagação em Perceptrons Multicamadas, mas evidenciou o gargalo da derivação manual: para grafos complexos com ramificações e controle de fluxo, calcular derivadas no papel é impraticável, enquanto a diferenciação simbólica tradicional sofre de inchaço exponencial de termos (*expression swell*). Esta aula investiga e constrói a tecnologia fundamental sobre a qual todos os frameworks modernos de Inteligência Artificial repousam: os **Grafos Acíclicos Direcionados (DAGs)** e a **Diferenciação Automática** (*Automatic Differentiation* - Autodiff). Comparamos rigorosamente os quatro paradigmas de diferenciação (manual, simbólico, numérico por diferenças finitas e automático), provando por que apenas a autodiff combina precisão de máquina exata com tempo de execução linear. Em seguida, formalizamos os dois modos canônicos de propagação: o **Modo Forward** (tangente / *pushforward*), ótimo quando a entrada é de baixa dimensão ($d_{\text{in}} \ll d_{\text{out}}$), e o **Modo Reverse** (adjunto / *pullback* / *backpropagation* generalizado), ideal para aprendizado de máquina onde a perda escalar agrega milhões ou bilhões de parâmetros ($d_{\text{out}} = 1 \ll d_{\text{in}}$). Demonstramos o célebre **Teorema de Baur-Strassen**, que garante que o custo de calcular todos os $d_{\text{in}}$ gradientes no modo reverso é no máximo um pequeno múltiplo constante (entre 3 e 5 vezes) do custo de avaliar a função direta. Construímos um motor de diferenciação automática reversa do zero em Python puro orientado a objetos com ordenação topológica por busca em profundidade, validando-o com o dataset California Housing, e encerramos analisando o custo de memória da fita de execução (*tape*) e a necessidade de *activation checkpointing*.

**Objetivos:** comparar analiticamente os 4 métodos de diferenciação computacional; formalizar grafos computacionais como DAGs; deduzir as equações diferenciais dos modos forward (tangente) e reverse (adjunto); demonstrar o Teorema de Baur-Strassen de complexidade temporal assintótica; implementar um mini-motor de autodiff reverso vetorizado com ordenação topológica do zero; analisar o footprint de memória das ativações e o princípio do *activation checkpointing*.
**Pré-requisitos:** regra da cadeia multivariada e Jacobianos em *denominator layout* (Aulas 6 e 9); sensibilidades em redes neurais $\boldsymbol{\delta}^{(l)}$ (Aula 9); vetores e matrizes (Aulas 1 e 2).
**Dataset-fio:** California Housing ($N = 20.640, d = 4$), treinando a arquitetura não-linear de 2 camadas através do motor de autodiff construído do zero, validando os gradientes contra PyTorch e diferenças finitas.

**Estratégia Pedagógica:** B (Inside-Out com Problema-Fio) — fundamentação da teoria dos grafos de cálculo e diferenciação adjunta motivada pelo colapso da derivação manual e simbólica, culminando na implementação prática do zero aplicada ao California Housing.

---

## Plano de aula — Aula 10 (carga horária: ~110 min)

1. **Revisão e Introdução** (~12 min) — Da regra da cadeia matricial da Aula 9 ao dilema de código arbitrário. Problema motivador: ao construir um modelo com ramificações condicionais, conexões residuais e centenas de camadas, por que nem a diferenciação analítica no papel nem o SymPy nem `scipy.optimize.approx_fprime` conseguem treinar uma rede moderna? Pausa Ativa 1.
2. **Intuição — O Fluxo e o Eco no Grafo de Computação** (~8 min) — O avanço dos dados pela correnteza das operações elementares (forward) e o retorno do sinal de sensibilidade como um eco que reverbera rio acima até as nascentes (reverse).
3. **Bloco 1: Os Quatro Paradigmas da Diferenciação Computacional** (~20 min) — Análise comparativa profunda:
   - Diferenciação Manual: exata, mas vulnerável a erros humanos e intransferível.
   - Diferenciação Numérica (Diferenças Finitas): $f'(x) \approx \frac{f(x+h)-f(x)}{h}$. O dilema entre erro de truncamento $O(h)$ e erro de cancelamento subtrativo catastrófico de ponto flutuante $\epsilon_{\text{mach}}/h$. Custo proibitivo para gradientes: $d+1$ avaliações completas do modelo.
   - Diferenciação Simbólica: manipulação formal de árvores de expressões. O fenômeno do inchaço exponencial de termos (*expression swell*) decorrente da repetição descontrolada de subexpressões na regra do produto.
   - Diferenciação Automática: avaliação exata de derivadas em tempo de execução via decomposição em operações elementares com regras atômicas conhecidas. Pausa Ativa 2.
4. **Bloco 2: DAGs e os Modos Forward e Reverse de Autodiff** (~25 min) — Formalização de Grafos Acíclicos Direcionados: nós $v_i$, arestas e ordem topológica.
   - Modo Forward (Tangente / Pushforward): perturbação direcional $\dot{v}_i = \sum_{j \in \text{Pa}(i)} \frac{\partial \phi_i}{\partial v_j} \dot{v}_j$. Custo temporal: $O(d_{\text{in}} \cdot C_{\text{eval}})$. Eficiente quando $d_{\text{in}} \ll d_{\text{out}}$.
   - Modo Reverse (Adjunto / Pullback / Backpropagation Generalizado): variáveis adjuntas $\bar{v}_i = \frac{\partial \mathcal{L}}{\partial v_i} = \sum_{k \in \text{Ch}(i)} \bar{v}_k \frac{\partial \phi_k}{\partial v_i}$. Custo temporal: $O(d_{\text{out}} \cdot C_{\text{eval}})$.
   - Teorema de Baur-Strassen / Speelpenning: se um programa computa $f: \mathbb{R}^n \to \mathbb{R}$ em $C$ operações aritméticas, o gradiente completo $\nabla f \in \mathbb{R}^n$ pode ser computado no modo reverso em no máximo $5C$ operações, independentemente de $n$! Pausa Ativa 3.
5. **Bloco 3: Construção de um Motor de Autodiff do Zero em Python** (~25 min) — Implementação orientada a objetos:
   - A classe `Value` (ou `Tensor` minimalista): armazenamento de `.data`, `.grad`, `_prev` e `_backward`.
   - Sobrecarga de operadores dunder (`__add__`, `__mul__`, `__pow__`, `__neg__`, `__sub__`, `relu`).
   - Construção da passagem reversa via ordenação topológica por Busca em Profundidade (DFS) no método `.backward()`.
   - Aplicação e validação no California Housing: cálculo do gradiente em um mini-batch e comparação de máquina com NumPy analítico e PyTorch. Pausa Ativa 4.
6. **Bloco 4: Footprint de Memória e Checkpointing de Ativações** (~15 min) — O custo oculto do modo reverso: enquanto o modo forward não retém estado intermediário, o modo reverso precisa congelar na RAM/VRAM todas as ativações intermediárias $v_i$ da passagem direta para uso nas derivadas locais da passagem reversa (a fita de execução ou *tape*).
   - O gargalo de memória de GPU em modelos de fronteira (Transformers / LLMs).
   - A técnica de *Activation Checkpointing* (Griewank & Walther / Chen et al.): descartar ativações intermediárias entre blocos e recomputá-las durante o backward pass, reduzindo o consumo de memória de $O(L)$ para $O(\sqrt{L})$ ao custo de apenas $33\%$ a mais de tempo de computação. Pausa Ativa 5.
7. **Fechamento** (~5 min) — Retomada das cinco perguntas essenciais. Fechamento da Parte 2 do curso (O Cálculo da Otimização Diferenciável). Ponte para a Parte 3 (Dinâmica Avançada e Escala — Aula 11: Gradiente Descendente Estocástico e Mini-Batching).

---

## Fontes usadas — Aula 10

Deslocamentos página impressa → PDF: `mathml.pdf` +6; `optml.pdf` (Wright & Recht).

### Fonte 1: Deisenroth, Faisal & Ong, *Mathematics for Machine Learning*, §5.6.2, pp. 161–164 (PDF pp. 167–170)
**Uso pretendido:** Definição formal de Diferenciação Automática, representação de programas como grafos de computação, distinção entre modo forward e modo reverse através da associatividade da regra da cadeia, e equações de propagação direta e reversa com nós pais e filhos.
**Trechos:**
> "Automatic differentiation is a formalization of Example 5.14. Let $x_1, \dots, x_d$ be the input variables to the function, $x_{d+1}, \dots, x_{D-1}$ be the intermediate variables, and $x_D$ the output variable. Then the computation graph can be expressed as follows: For $i = d + 1, \dots, D: x_i = g_i(x_{\text{Pa}(x_i)})$, where the $g_i(\cdot)$ are elementary functions and $x_{\text{Pa}(x_i)}$ are the parent nodes of the variable $x_i$ in the graph... Recall that by definition $f = x_D$ and hence $\frac{\partial f}{\partial x_D} = 1$. For other variables $x_i$, we apply the chain rule:
> $$\frac{\partial f}{\partial x_i} = \sum_{x_j: x_i \in \text{Pa}(x_j)} \frac{\partial f}{\partial x_j}\frac{\partial x_j}{\partial x_i} = \sum_{x_j: x_i \in \text{Pa}(x_j)} \frac{\partial f}{\partial x_j}\frac{\partial g_j}{\partial x_i}$$
> where $\text{Pa}(x_j)$ is the set of parent nodes of $x_j$ in the computation graph. Equation (5.143) is the forward propagation of a function, whereas (5.145) is the backpropagation of the gradient through the computation graph." (§5.6.2, pp. 163–164)
> "Due to the associativity of matrix multiplication, we can choose between $\frac{dy}{dx} = \left(\frac{dy}{db}\frac{db}{da}\right)\frac{da}{dx}$ (reverse mode) and $\frac{dy}{dx} = \frac{dy}{db}\left(\frac{db}{da}\frac{da}{dx}\right)$ (forward mode)... In the context of neural networks, where the input dimensionality is often much higher than the dimensionality of the labels, the reverse mode is computationally significantly cheaper than the forward mode." (§5.6.2, p. 161)

### Fonte 2: Griewank, A. & Walther, A., *Evaluating Derivatives: Principles and Techniques of Algorithmic Differentiation*, SIAM (2008), §1.2 e §3.3; e Baur & Strassen (1983)
**Uso pretendido:** Teorema de Baur-Strassen / Speelpenning sobre a complexidade temporal da diferenciação reversa em circuitos aritméticos e o compromisso tempo-memória.
**Trecho:**
> "Theorem (Baur-Strassen, 1983). Let $f: \mathbb{R}^n \to \mathbb{R}$ be computed by a straight-line arithmetic circuit of length $L$ using operations $\{+, -, \times, /\}$ and unit-cost elementary functions. Then the gradient $\nabla f(x) \in \mathbb{R}^n$ can be computed by an arithmetic circuit of length at most $5L$ (and under standard implementations, at most $3L$ to $4L$)."

### Fonte 3: Baydin, A. G., Pearlmutter, B. A., Radul, A. A., & Siskind, J. M., *Automatic Differentiation in Machine Learning: A Survey*, JMLR (2018), §2 e §3
**Uso pretendido:** Comparação sistemática dos quatro métodos de diferenciação: manual, simbólico (e a prova do inchaço exponencial de termos em funções aninhadas), numérico (instabilidade do passo $h$ por erro de arredondamento) e automático.
**Trecho:**
> "Automatic differentiation (AD) is distinct from both symbolic differentiation and numerical differentiation. Where symbolic differentiation operates on mathematical expressions and numerical differentiation approximates derivatives via finite differences, AD executes a program that computes the analytical derivative of another program... Symbolic differentiation suffers from the problem of 'expression swell', where expressions grow exponentially with nesting depth unless complex algebraic simplification algorithms are applied at each step."

