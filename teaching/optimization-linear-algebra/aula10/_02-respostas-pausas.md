# Gabarito e Guia das Pausas Ativas — Aula 10: Grafos de Computação e Diferenciação Automática

Este documento contém o gabarito das questões de Verdadeiro/Falso e as diretrizes pedagógicas para condução das discussões das perguntas abertas em cada uma das cinco Pausas Ativas da Aula 10.

---

## Pausa Ativa 1: O Dilema da Diferenciação Computacional

### Pergunta Aberta
*Se a diferenciação numérica por diferenças finitas $f'(x) \approx \frac{f(x+h)-f(x)}{h}$ converge para a derivada exata quando $h \to 0$, por que simplesmente não escolhemos $h = 10^{-20}$ no computador para obter uma aproximação perfeita?*

**Diretrizes de Discussão com a Turma:**
- **Representação em Ponto Flutuante (IEEE 754):** Explique que números `float64` possuem 53 bits de mantissa (~15 a 17 dígitos decimais de precisão significativa). A menor perturbação relativa distinguível de $1{,}0$ é $\epsilon_{\text{mach}} \approx 2{,}22 \cdot 10^{-16}$.
- **O Fenômeno do Cancelamento Subtrativo:** Se $x = 1{,}0$ e escolhemos $h = 10^{-20}$, o somador de ponto flutuante avalia $x + h = 1{,}00000000000000000000 \to 1{,}0$. Portanto, $f(x+h) - f(x) = 0{,}0$, resultando em uma derivada aproximada igual a zero!
- **A Conclusão:** O erro numérico possui duas curvas opostas: o erro de truncamento da matemática ($O(h)$ ou $O(h^2)$) e o erro de arredondamento do hardware ($\epsilon_{\text{mach}}/h$). Elas se cruzam em um vale em U, impedindo que diferenças finitas alcancem a precisão de máquina.

### Julgamento de Verdadeiro ou Falso
- ✔ **V:** A diferenciação simbólica aplica regras formais de cálculo analítico diretamente sobre as árvores sintáticas das expressões.
- ✗ **F:** A autodiff não calcula quocientes de diferenças; ela computa derivadas exatas em tempo de execução combinando derivadas atômicas pré-conhecidas via regra da cadeia.
- ✔ **V:** Quando $h < \sqrt{\epsilon_{\text{mach}}}$, a perda de dígitos na subtração destrói a precisão (o clássico cancelamento catastrófico).
- ✗ **F:** O Teorema de Baur-Strassen prova que o tempo de execução é **estritamente linear** ($\le 5\times$ a passagem direta), nunca exponencial!

---

## Pausa Ativa 2: Os Quatro Métodos em Perspectiva

### Pergunta Aberta
*Se a diferenciação automática avalia a regra da cadeia numericamente, por que ela não sofre do mesmo problema de cancelamento subtrativo das diferenças finitas?*

**Diretrizes de Discussão com a Turma:**
- **Ausência de Divisões Infinitesimais:** Destaque que a autodiff nunca realiza subtrações de valores quase idênticos seguidas de divisões por números minúsculos $h$.
- **Uso de Derivadas Analíticas Atômicas:** A autodiff utiliza a derivada analítica fechada de cada operador elementar. Por exemplo, para a multiplicação $v_3 = v_1 \times v_2$, a sensibilidade em relação a $v_1$ é simplesmente multiplicada pelo valor exato de $v_2$. As operações efetuadas são apenas somas e produtos de números ordinários, operando com a máxima precisão da máquina.

### Julgamento de Verdadeiro ou Falso
- ✗ **F:** Para a diferença central, o erro mínimo ocorre no ponto de equilíbrio $h^\star \approx \epsilon_{\text{mach}}^{1/3} \approx 10^{-5}$; em $h = 10^{-8}$ o cancelamento subtrativo já começou a dominar.
- ✗ **F:** A diferenciação simbólica manipula termos matemáticos puros (expressões simbólicas), não código compilado de baixo nível.
- ✔ **V:** A autodiff dinâmica (*tape-based* / PyTorch) rastreia o fluxo de controle em tempo de execução, diferenciando laços e condicionais perfeitamente.
- ✗ **F:** São necessárias $d+1$ avaliações para a diferença progressiva: a função no ponto base e em $d$ perturbações coordenadas.

---

## Pausa Ativa 3: A Assimetria Temporal entre Forward e Reverse

### Pergunta Aberta
*Se o modo reverso é tão superior para calcular gradientes em aprendizado de máquina ($d_{\text{out}} = 1$), em qual cenário prático da engenharia e ciência da computação o modo forward seria estritamente superior ao modo reverso?*

**Diretrizes de Discussão com a Turma:**
- **Inversão da Razão de Dimensões ($d_{\text{in}} \ll d_{\text{out}}$):** Peça aos alunos para pensarem em problemas onde temos poucos parâmetros de controle de entrada e milhares de saídas.
- **Exemplos Reais:**
  1. *Robótica e Animação:* Cinemática direta de um braço robótico com 3 motores ($d_{\text{in}} = 3$) cuja posição gera milhares de pontos em uma malha 3D ($d_{\text{out}} = 10.000$). O modo forward obtém o Jacobiano em 3 passagens, enquanto o modo reverso exigiria 10.000 passagens!
  2. *Equações Diferenciais (ODEs):* Simulação de trajetória de foguete com 2 parâmetros de queima de combustível gerando centenas de pontos temporais.

### Julgamento de Verdadeiro ou Falso
- ✔ **V:** No modo forward, a variável tangente $\dot{v}_i$ é calculada no mesmo passo em que $v_i$ é produzido.
- ✗ **F:** A cota de Baur-Strassen aplica-se a **funções escalares** ($m=1$). Para saídas multidimensionais, o custo escala linearmente com $m$.
- ✔ **V:** Pela regra da cadeia, o valor da adjunta acumula as sensibilidades que retornam de todos os filhos imediatos: $\bar{v}_i = \sum_{k \in \text{Ch}(i)} \bar{v}_k \frac{\partial \phi_k}{\partial v_i}$.
- ✗ **F:** Ciclos direcionados tornam impossível estabelecer uma ordem topológica (onde todas as arestas apontam na direção do fluxo).

---

## Pausa Ativa 4: A Dinâmica da Acumulação de Gradientes

### Pergunta Aberta
*Por que dentro do método `_backward()` de cada operação nós acumulamos os gradientes usando `self.grad += ...` em vez de simplesmente atribuir `self.grad = ...`? O que aconteceria em um grafo onde uma mesma variável é reutilizada em duas operações distintas (ex.: $y = x \cdot x$ ou conexões residuais $x + f(x)$)?*

**Diretrizes de Discussão com a Turma:**
- **Caminhos Disjuntos no Grafo:** Desenhe no quadro um grafo em forma de diamante: $x$ alimenta $a$ e $b$, que por sua vez se somam em $y$. Pelo cálculo multivariado, $\frac{\partial y}{\partial x} = \frac{\partial y}{\partial a}\frac{\partial a}{\partial x} + \frac{\partial y}{\partial b}\frac{\partial b}{\partial x}$.
- **Sobrescrita Acidental:** Se o método usasse atribuição simples `=`, a passagem reversa que processa o nó $b$ sobrescreveria o gradiente já computado pelo nó $a$, perdendo metade da sensibilidade real. A acumulação aditiva `+=` é a garantia algorítmica de que a soma de caminhos da regra da cadeia será respeitada.

### Julgamento de Verdadeiro ou Falso
- ✔ **V:** Cada ramificação representa uma rota independente de influência que deve ser somada na adjunta total.
- ✔ **V:** No PyTorch, `grad` não é zerado automaticamente após `.step()` para permitir acumulação de gradientes entre múltiplos mini-batches (*gradient accumulation*); logo, `zero_grad()` é obrigatório.
- ✔ **V:** A busca em profundidade visita cada nó e cada aresta uma única vez, executando a ordenação topológica em tempo $\mathcal{O}(|V| + |E|)$.
- ✗ **F:** Motores de autodiff utilizam a derivada generalizada de Clarke / subgradiente, definindo convencionalmente $\text{ReLU}'(0) = 0$, o que viabiliza o treinamento sem interrupções.

---

## Pausa Ativa 5: O Compromisso Tempo-Espaço em Grafos

### Pergunta Aberta
*Durante a fase de inferência de um modelo de linguagem (quando estamos apenas gerando texto e não treinando), é necessário reter o grafo de computação e as ativações intermediárias em memória? Como frameworks como PyTorch otimizam esse processo?*

**Diretrizes de Discussão com a Turma:**
- **Finalidade do Grafo:** Relembre que o grafo, as referências `_prev` e as funções `_backward` existem exclusivamente para permitir a retropropagação do erro.
- **Inferência Pura:** Na geração de tokens, nenhum gradiente será calculado. Reter ativações intermediárias consome memória desnecessariamente.
- **O Modo Sem Gradiente:** O contexto `with torch.no_grad():` desativa a construção dinâmica do grafo. Os tensores intermediários são desalocados da VRAM no instante em que sua operação termina, reduzindo o consumo de memória em até $80\%$ e eliminando o overhead de alocação de nós.

### Julgamento de Verdadeiro ou Falso
- ✔ **V:** Todas as ativações $v_i$ utilizadas como argumentos nas funções de derivada local precisam ser estocadas na RAM/VRAM até o backward pass.
- ✗ **F:** O checkpointing é matematicamente exato; ele apenas recalcula os mesmos valores exatos durante a passagem reversa.
- ✔ **V:** Sem a necessidade de manter o grafo de retropropagação, a memória ocupada pelas ativações intermediárias é liberada instantaneamente.
- ✔ **V:** No modo forward, como a derivada avança junto com os dados, os nós podem ser descartados imediatamente após sua utilização.

