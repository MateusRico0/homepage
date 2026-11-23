import re

path = "teaching/optimization-linear-algebra/aula12/index.qmd"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# ==================== PAUSA 1 ====================
p1_old_start = '::: {.content-visible when-format="html" unless-format="revealjs"}\n## Pausa 1: O Dilema das Oscilações Transversais e a Inércia'
p1_old_end = '# Bloco 2: O Gradiente Acelerado de Nesterov (NAG)'

p1_new = r'''::: {.content-visible when-format="html" unless-format="revealjs"}
## Pausa 1: O Dilema das Oscilações Transversais e a Inércia

::: {.callout-tip icon=false}
### Teste Seus Conhecimentos — Pausa 1
Uma partícula está em uma ravina elíptica $f(w_1, w_2) = \frac{1}{2}(100 w_1^2 + w_2^2)$. O gradiente instantâneo no ponto inicial é $\mathbf{g}_0 = (100 w_1, w_2)^T$. Suponha que ao longo das iterações $k$, as derivadas parciais na direção transversal alternem de sinal: $g_{k, 1} \in \{+10, -10, +10, -10, \dots\}$, enquanto na calha longitudinal avancem com sinal constante: $g_{k, 2} \approx 1$.

1. O que acontece com o deslocamento útil do Gradiente Descendente sob taxa escalar segura $\alpha = 0{,}02$?
2. Como a soma geométrica do momento $\mathbf{v}_{k+1} = \beta \mathbf{v}_k - \alpha \mathbf{g}_k$ cancela as oscilações transversais e amplifica a velocidade longitudinal para $\beta = 0{,}9$?
:::

::: {.callout-note icon=false}
### Julgue V ou F para cada afirmação:

- □ Na presença de gradientes oscilatórios transversais, a soma ponderada por $\beta$ cancela as amplitudes de sinais opostos, enquanto componentes consistentes somam-se até o fator $\frac{1}{1-\beta}$.
- □ O momento clássico de Polyak modifica a geometria da função de perda ao alterar a matriz Hessiana local para $H^{1/2}$.
- □ Aumentar o coeficiente de momento $\beta$ sem reduzir a taxa de aprendizado $\alpha$ pode desestabilizar o sistema dinâmico e induzir oscilações caóticas.
- □ Em superfícies de custo estocásticas (SGD com mini-batches), o vetor momento atua como uma média móvel suave que atenua as flutuações amostrais.
:::
:::

::: {.content-visible when-format="revealjs"}
## Pausa 1: O Dilema das Oscilações Transversais e a Inércia

::: {.callout-tip}
## O Dilema do Vale Estreito
Em uma ravina elíptica ($\kappa = 100$), o gradiente transversal oscila de sinal ($\pm 10$), enquanto o longitudinal é constante ($+1$).
Qual é o passo máximo $\alpha$ do GD clássico para evitar divergência? Como a inércia com $\beta = 0{,}9$ cancela o ziguezague e amplifica a velocidade longitudinal em $10\times$?
:::

::: {.callout-tip}
## Dinâmica de Inércia

Julgue V ou F — a questão só conta se acertar os 4 itens:

- □ Na presença de gradientes oscilatórios transversais, a soma ponderada por $\beta$ cancela as amplitudes de sinais opostos, enquanto componentes consistentes somam-se até o fator $\frac{1}{1-\beta}$.
- □ O momento clássico de Polyak modifica a geometria da função de perda ao alterar a matriz Hessiana local para $H^{1/2}$.
- □ Aumentar o coeficiente de momento $\beta$ sem reduzir a taxa de aprendizado $\alpha$ pode desestabilizar o sistema dinâmico e induzir oscilações caóticas.
- □ Em superfícies de custo estocásticas (SGD com mini-batches), o vetor momento atua como uma média móvel suave que atenua as flutuações amostrais.
:::

## Pausa 1: O Dilema das Oscilações Transversais e a Inércia — Resposta

::: {.callout-tip}
## Dinâmica de Inércia — Resposta

- ✔ **Verdadeiro.** A soma geométrica acumula passos consistentes até $\frac{1}{1-\beta} = 10\times$ e cancela flutuações alternadas.
- ✗ **Falso.** O momento não altera a Hessiana; altera a dinâmica de 1ª para 2ª ordem, modificando o raio espectral da matriz de transição.
- ✔ **Verdadeiro.** Se o raio espectral de $T_i$ ultrapassar $1$, o sistema dinâmico linear torna-se instável e diverge.
- ✔ **Verdadeiro.** Como média móvel exponencial (EMA), o momento amortece o ruído de alta variância dos mini-batches.
:::

::: {.fragment}
**Voltando à pergunta:** Para estabilidade transversal, o GD requer $\alpha < 2/100 = 0{,}02$, avançando apenas $0{,}02$ por passo no vale. Com $\beta = 0{,}9$, o momento cancela as oscilações transversais e constrói velocidade longitudinal terminal $v_{\text{long}} = \frac{\alpha}{1-\beta} = 10\alpha$, acelerando $10\times$!
:::
:::
'''

# ==================== PAUSA 2 ====================
p2_old_start = '::: {.content-visible when-format="html" unless-format="revealjs"}\n## Pausa 2: Aceleradores de Nesterov e Amortecimento'
p2_old_end = '# Bloco 3: A Grande Síntese — O Otimizador Adam'

p2_new = r'''::: {.content-visible when-format="html" unless-format="revealjs"}
## Pausa 2: Aceleradores de Nesterov e Amortecimento

::: {.callout-tip icon=false}
### Teste Seus Conhecimentos — Pausa 2
Considere uma função 1D parabólica $f(w) = \frac{1}{2}w^2$. Uma partícula está em $w_k = 2$ com velocidade residual negativa $v_k = -3$, sob $\alpha = 0{,}5$ e $\beta = 0{,}9$.
1. Onde a regra de Polyak posiciona $w_{k+1}$ e qual é a sua nova velocidade $v_{k+1}$?
2. Onde a regra de Nesterov avalia o ponto antecipado $w_{\text{ahead}}$ e qual é o ponto final $w_{k+1}$ gerado com a frenagem preventiva?
:::

::: {.callout-note icon=false}
### Julgue V ou F para cada afirmação:

- □ O gradiente de Nesterov avaliado em $\mathbf{w}_k + \beta \mathbf{v}_k$ detecta subidas da função antes que a partícula as atinja, aplicando força contrária que amortece o *overshoot*.
- □ O NAG atinge a cota assintótica ótima $\mathcal{O}(1/k^2)$ para funções convexas $L$-suaves gerais, provada matematicamente por Nesterov.
- □ Avaliar o gradiente antecipado em Nesterov exige duas passagens completas de retropropagação (*backpropagation*) por iteração, duplicando o custo em relação ao GD.
- □ Em problemas não-convexos com ruído estocástico severo de mini-batch, antecipar a posição pode ocasionalmente amplificar a instabilidade amostral.
:::
:::

::: {.content-visible when-format="revealjs"}
## Pausa 2: Aceleradores de Nesterov e Amortecimento

::: {.callout-tip}
## O Freio Preditivo em 1D
Em $f(w) = \frac{1}{2}w^2$, considere $w_k = 2$ e velocidade $v_k = -3$ sob $\alpha = 0{,}5$ e $\beta = 0{,}9$.
Onde Polyak posiciona $w_{k+1}$ e qual é sua nova velocidade? Onde Nesterov avalia o ponto antecipado $w_{\text{ahead}}$ e como ele amortece o *overshoot*?
:::

::: {.callout-tip}
## Propriedades do NAG vs. Polyak

Julgue V ou F — a questão só conta se acertar os 4 itens:

- □ O gradiente de Nesterov avaliado em $\mathbf{w}_k + \beta \mathbf{v}_k$ detecta subidas da função antes que a partícula as atinja, aplicando força contrária que amortece o *overshoot*.
- □ O NAG atinge a cota assintótica ótima $\mathcal{O}(1/k^2)$ para funções convexas $L$-suaves gerais, provada matematicamente por Nesterov.
- □ Avaliar o gradiente antecipado em Nesterov exige duas passagens completas de retropropagação (*backpropagation*) por iteração, duplicando o custo em relação ao GD.
- □ Em problemas não-convexos com ruído estocástico severo de mini-batch, antecipar a posição pode ocasionalmente amplificar a instabilidade amostral.
:::

## Pausa 2: Aceleradores de Nesterov e Amortecimento — Resposta

::: {.callout-tip}
## Propriedades do NAG vs. Polyak — Resposta

- ✔ **Verdadeiro.** Ao saltar antes de medir, detecta a elevação da encosta e aplica amortecimento ativo preventivo.
- ✔ **Verdadeiro.** A cota $\mathcal{O}(1/k^2)$ é a fronteira inferior absoluta de complexidade para métodos de 1ª ordem em funções convexas $L$-suaves.
- ✗ **Falso.** Exige exatamente **uma única** avaliação de gradiente por passo (feita em $\mathbf{w}_{\text{ahead}}$), com custo $\mathcal{O}(d)$.
- ✔ **Verdadeiro.** Com mini-batches ruidosos, projetar o gradiente à frente pode elevar a variância da estimativa estocástica.
:::

::: {.fragment}
**Voltando à pergunta:** Polyak calcula gradiente em $w = 2 \implies v_{k+1} = -3{,}7 \implies w_{k+1} = -1{,}7$ (*overshoot* severo!). Nesterov antecipa para $w_{\text{ahead}} = 2 - 2{,}7 = -0{,}7$; como a derivada lá é negativa ($-0{,}7$), freia a velocidade para $v_{k+1} = -2{,}35 \implies w_{k+1} = -0{,}35$, muito mais perto do ótimo!
:::
:::
'''

# ==================== PAUSA 3 ====================
p3_old_start = '::: {.content-visible when-format="html" unless-format="revealjs"}\n## Pausa 3: A Síntese do Adam e a Correção de Viés'
p3_old_end = '# Bloco 4: A Cirurgia Crítica — Do $L_2$ Regularization ao AdamW'

p3_new = r'''::: {.content-visible when-format="html" unless-format="revealjs"}
## Pausa 3: A Síntese do Adam e a Correção de Viés

::: {.callout-tip icon=false}
### Teste Seus Conhecimentos — Pausa 3
Inicializamos o Adam com $\beta_1 = 0{,}9$, $\beta_2 = 0{,}999$, $\epsilon = 10^{-8}$ e inicializadores zerados $m_0 = 0$, $v_0 = 0$. Suponha que no passo $t=1$ o gradiente seja $g_1 = 5{,}0$.
1. Qual seria o passo $\Delta w_1$ sem as correções de viés?
2. Como a divisão por $1 - \beta^t$ normaliza exatamente o passo inicial para $-\alpha$?
:::

::: {.callout-note icon=false}
### Julgue V ou F para cada afirmação:

- □ A divisão por $1 - \beta_1^t$ e $1 - \beta_2^t$ compensa o fato de que $\mathbf{m}_t$ e $\mathbf{v}_t$ são inicializados em zero, tornando as estimativas não-enviesadas desde o primeiro passo.
- □ Conforme o número de iterações cresce ($t \to \infty$), os termos de correção de viés convergem para $0$, anulando as atualizações do Adam.
- □ O termo $\sqrt{\hat{\mathbf{v}}_t}$ no denominador atua como um precondicionador diagonal, acelerando coordenadas de gradiente pequeno e desacelerando coordenadas íngremes.
- □ Em coordenadas onde o gradiente troca constantemente de sinal, $\hat{\mathbf{m}}_t$ tende a zero enquanto $\sqrt{\hat{\mathbf{v}}_t}$ acumula a energia, reduzindo o passo e amortecendo oscilações.
:::
:::

::: {.content-visible when-format="revealjs"}
## Pausa 3: A Síntese do Adam e a Correção de Viés

::: {.callout-tip}
## A Partida a Frio do Adam
Em $t=1$, com $\beta_1 = 0{,}9$, $\beta_2 = 0{,}999$, inicializadores $\mathbf{m}_0 = \mathbf{0}, \mathbf{v}_0 = \mathbf{0}$ e gradiente $g_1 = 5{,}0$.
Qual seria o passo $\Delta w_1$ sem a correção de viés? Como a divisão por $1 - \beta^t$ normaliza exatamente o passo inicial para $-\alpha$?
:::

::: {.callout-tip}
## Mecânica do Adam

Julgue V ou F — a questão só conta se acertar os 4 itens:

- □ A divisão por $1 - \beta_1^t$ e $1 - \beta_2^t$ compensa o fato de que $\mathbf{m}_t$ e $\mathbf{v}_t$ são inicializados em zero, tornando as estimativas não-enviesadas desde o primeiro passo.
- □ Conforme o número de iterações cresce ($t \to \infty$), os termos de correção de viés convergem para $0$, anulando as atualizações do Adam.
- □ O termo $\sqrt{\hat{\mathbf{v}}_t}$ no denominador atua como um precondicionador diagonal, acelerando coordenadas de gradiente pequeno e desacelerando coordenadas íngremes.
- □ Em coordenadas onde o gradiente troca constantemente de sinal, $\hat{\mathbf{m}}_t$ tende a zero enquanto $\sqrt{\hat{\mathbf{v}}_t}$ acumula a energia, reduzindo o passo e amortecendo oscilações.
:::

## Pausa 3: A Síntese do Adam e a Correção de Viés — Resposta

::: {.callout-tip}
## Mecânica do Adam — Resposta

- ✔ **Verdadeiro.** Como $\mathbb{E}[\mathbf{m}_t] = (1 - \beta_1^t)\mathbb{E}[\mathbf{g}_t]$, dividir por $1 - \beta_1^t$ restaura a esperança correta.
- ✗ **Falso.** Como $\beta \in (0, 1)$, $\beta^t \to 0 \implies 1 - \beta^t \to 1$. A correção é crucial no início e neutra no final.
- ✔ **Verdadeiro.** Coordenadas com gradientes pequenos recebem divisão por valor pequeno, acelerando seu deslocamento relativo.
- ✔ **Verdadeiro.** $\mathbf{m}_t$ cancela os sinais opostos enquanto $\mathbf{v}_t$ acumula os quadrados, estrangulando o passo oscilatório transversal.
:::

::: {.fragment}
**Voltando à pergunta:** Sem correção, $m_1 = 0{,}5$ e $v_1 = 0{,}025 \implies \Delta w_1 = -\alpha \frac{0{,}5}{\sqrt{0{,}025}} \approx -3{,}16\alpha$ (distorcido!). Com correção, $\hat{m}_1 = \frac{0{,}5}{0{,}1} = 5{,}0$ e $\hat{v}_1 = \frac{0{,}025}{0{,}001} = 25{,}0 \implies \Delta w_1 = -\alpha \frac{5{,}0}{\sqrt{25{,}0}} = -\alpha \cdot 1{,}0$, perfeitamente calibrado!
:::
:::
'''

# ==================== PAUSA 4 ====================
p4_old_start = '::: {.content-visible when-format="html" unless-format="revealjs"}\n## Pausa 4: A Cirurgia do AdamW'
p4_old_end = '# Fechamento'

p4_new = r'''::: {.content-visible when-format="html" unless-format="revealjs"}
## Pausa 4: A Cirurgia do AdamW

::: {.callout-tip icon=false}
### Teste Seus Conhecimentos — Pausa 4
1. Por que no Gradiente Descendente euclidiano puro a regularização $L_2$ ($\frac{\lambda}{2}\|\mathbf{w}\|^2$) e o decaimento de pesos multiplicativo ($(1 - \alpha\lambda)\mathbf{w}$) são identicamente equivalentes?
2. O que acontece com a taxa efetiva de decaimento de um peso associado a uma palavra frequente versus uma palavra raríssima quando usamos regularização $L_2$ tradicional dentro do Adam?
:::

::: {.callout-note icon=false}
### Julgue V ou F para cada afirmação:

- □ No Gradiente Descendente clássico, aplicar regularização $L_2$ na perda é identicamente equivalente a aplicar decaimento multiplicativo de pesos (*weight decay*).
- □ No Adam com $L_2$ tradicional na perda, a taxa efetiva de decaimento de cada peso passa a ser inversamente proporcional à raiz do segundo momento ($\sqrt{\hat{v}_t} + \epsilon$).
- □ O AdamW resolve essa patologia subtraindo $\alpha \lambda \mathbf{w}_t$ diretamente da atualização do peso, fora da fração adaptativa que divide por $\sqrt{\hat{\mathbf{v}}_t}$.
- □ O AdamW altera o cálculo dos gradientes estocásticos $\mathbf{g}_t$ da perda da tarefa $\mathcal{L}(\mathbf{w})$, exigindo uma segunda passagem de backpropagation.
:::
:::

::: {.content-visible when-format="revealjs"}
## Pausa 4: A Cirurgia do AdamW

::: {.callout-tip}
## A Aberração da Penalidade Adaptativa
Por que somar $\lambda \mathbf{w}$ à função de perda é inofensivo no GD, mas catastrófico no Adam?
O que acontece com a taxa efetiva de decaimento de um peso associado a uma palavra frequente versus uma palavra raríssima em um modelo de linguagem?
:::

::: {.callout-tip}
## Regularização e Weight Decay

Julgue V ou F — a questão só conta se acertar os 4 itens:

- □ No Gradiente Descendente clássico, aplicar regularização $L_2$ na perda é identicamente equivalente a aplicar decaimento multiplicativo de pesos (*weight decay*).
- □ No Adam com $L_2$ tradicional na perda, a taxa efetiva de decaimento de cada peso passa a ser inversamente proporcional à raiz do segundo momento ($\sqrt{\hat{v}_t} + \epsilon$).
- □ O AdamW resolve essa patologia subtraindo $\alpha \lambda \mathbf{w}_t$ diretamente da atualização do peso, fora da fração adaptativa que divide por $\sqrt{\hat{\mathbf{v}}_t}$.
- □ O AdamW altera o cálculo dos gradientes estocásticos $\mathbf{g}_t$ da perda da tarefa $\mathcal{L}(\mathbf{w})$, exigindo uma segunda passagem de backpropagation.
:::

## Pausa 4: A Cirurgia do AdamW — Resposta

::: {.callout-tip}
## Regularização e Weight Decay — Resposta

- ✔ **Verdadeiro.** No GD, $\mathbf{w}_{t+1} = \mathbf{w}_t - \alpha(\nabla\mathcal{L} + \lambda\mathbf{w}) = (1 - \alpha\lambda)\mathbf{w}_t - \alpha\nabla\mathcal{L}$ contrai todos os pesos uniformemente.
- ✔ **Verdadeiro.** Como $\lambda w$ entra no gradiente, o decaimento é dividido por $\sqrt{\hat{v}_t} + \epsilon$, suprimindo a contração em pesos frequentes.
- ✔ **Verdadeiro.** Desacoplar restaura a contração multiplicativa $(1 - \alpha\lambda)$ homogênea por época em todos os parâmetros.
- ✗ **Falso.** O AdamW não altera o backpropagation nem adiciona custo: $\mathbf{g}_t$ continua sendo o gradiente usual da tarefa.
:::

::: {.fragment}
**Voltando à pergunta:** No Adam com $L_2$, a taxa efetiva de contração é $\frac{\alpha\lambda}{\sqrt{\hat{v}_i} + \epsilon}$. Para palavras frequentes ($\sqrt{\hat{v}} \gg 1$), a taxa é quase nula (sem regularização $\implies$ overfitting). Para palavras raras ($\sqrt{\hat{v}} \approx 0$), divide-se por $\epsilon = 10^{-8}$, implodindo o peso a zero! O AdamW corrige isso tornando a contração independente de $\hat{v}$.
:::
:::
'''

# Perform replacements in reverse order of appearance
sections = [
    (p4_old_start, p4_old_end, p4_new),
    (p3_old_start, p3_old_end, p3_new),
    (p2_old_start, p2_old_end, p2_new),
    (p1_old_start, p1_old_end, p1_new),
]

for start_m, end_m, new_sec in sections:
    pos_s = text.find(start_m)
    pos_e = text.find(end_m)
    assert pos_s != -1 and pos_e != -1, f"Not found: {start_m[:30]} or {end_m[:30]}"
    text = text[:pos_s] + new_sec + "\n\n" + text[pos_e:]

# Check div depth
div_depth = 0
for idx, line in enumerate(text.splitlines(), start=1):
    opens = len(re.findall(r'^:::\s*\{', line))
    closes = 1 if re.match(r'^:::\s*$', line) else 0
    div_depth += (opens - closes)
    if div_depth < 0:
        print(f"Error: negative div depth at line {idx}: {line}")
        break

print(f"Final div depth: {div_depth}")

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully written updated pausas to index.qmd!")
