# Respostas e Guia Docente — Pausas da Aula 10

Este documento reúne as resoluções detalhadas, a justificativa analítica de cada item de Verdadeiro/Falso e diretrizes didáticas para condução das cinco Pausas da **Aula 10: Gradiente Descendente Estocástico (SGD) e Mini-Batching**.

---

## Pausa 1: O Gargalo do Lote e a Filosofia Estocástica

### 1. Resolução da Pergunta Aberta
*Cenário:* $N = 2 \times 10^7$ amostras, dimensão $d = 100$. Taxa de throughput de hardware: $10^6$ gradientes de amostras por segundo. BGD requer 500 iterações; SGD requer 2 épocas.

- **Tempo do Batch Gradient Descent (BGD):**
  Cada iteração requer avaliar todos os $N = 2 \times 10^7$ gradientes:
  $$\text{Tempo por iteração} = \frac{2 \times 10^7 \text{ gradientes}}{10^6 \text{ gradientes/s}} = 20\text{ segundos}$$
  Para 500 iterações:
  $$\text{Tempo Total (BGD)} = 500 \times 20\text{ s} = 10.000\text{ segundos} \approx 2\text{ horas e } 46\text{ minutos}$$

- **Tempo do Stochastic Gradient Descent (SGD puro):**
  Uma época corresponde a avaliar exatamente $N$ gradientes. Portanto, 2 épocas correspondem a $2N = 4 \times 10^7$ gradientes no total:
  $$\text{Tempo Total (SGD)} = \frac{4 \times 10^7 \text{ gradientes}}{10^6 \text{ gradientes/s}} = 40\text{ segundos}$$

- **Conclusão Pedagógica:**
  Enquanto o BGD levou quase 3 horas, o SGD convergiu em apenas 40 segundos — uma aceleração de 250 vezes! Isso demonstra que a métrica ingênua de "número de iterações" é falaciosa em otimização de larga escala: 500 iterações de BGD realizaram apenas 500 atualizações de pesos, enquanto 2 épocas de SGD realizaram $4 \times 10^7$ atualizações consecutivas de pesos pelo mesmo custo de amostragem.

### 2. Gabarito Comentado dos Testes Conceituais (V/F)
*   **(A) Verdadeiro.** A regra de atualização do SGD puro sorteia um único índice $i_k$ e avalia $\mathbf{w}_{k+1} = \mathbf{w}_k - \alpha_k \nabla f_{i_k}(\mathbf{w}_k)$. O custo de calcular o gradiente de uma única amostra com $d$ atributos é $\mathcal{O}(d)$, totalmente independente de haver $10^3$ ou $10^{12}$ amostras armazenadas no disco.
*   **(B) Verdadeiro.** Por definição matemática, uma época de treinamento corresponde à passagem completa pelo equivalente ao volume de dados do conjunto de treino. Em ambos os casos, avalia-se exatamente $N$ vezes a perda/gradiente de uma amostra (no BGD, de uma só vez para compor um único passo; no SGD, dividida em $N$ passos sucessivos).
*   **(C) Falso.** O SGD puro garante apenas que o gradiente é não-enviesado em esperança ($\mathbb{E}[\nabla f_{i_k}] = \nabla F$). Em uma iteração particular, a amostra sorteada $i_k$ pode ter gradiente que aponta em direção transversal ou oposta ao gradiente global, de modo que a perda global pode aumentar temporariamente ($F(\mathbf{w}_{k+1}) > F(\mathbf{w}_k)$). A descida monotônica estrita é uma propriedade exclusiva do BGD sob passo suficientemente pequeno.
*   **(D) Verdadeiro.** Se duas amostras são identicamente iguais ($(\mathbf{x}_a, y_a) = (\mathbf{x}_b, y_b)$), a função de perda local $f_a(\mathbf{w}) = \ell(h(\mathbf{x}_a; \mathbf{w}), y_a)$ é a mesma função matemática que $f_b(\mathbf{w})$. Avaliadas no mesmo vetor de parâmetros $\mathbf{w}$, as derivadas parciais serão rigorosamente idênticas.

---

## Pausa 2: Estatística do Ruído Estocástico

### 1. Resolução da Pergunta Aberta
*Cenário:* $f_1(w) = \frac{1}{2}(1 \cdot w - 2)^2$ e $f_2(w) = \frac{1}{2}(1 \cdot w - 4)^2$.

- A perda média global é:
  $$F(w) = \frac{1}{2}[f_1(w) + f_2(w)] = \frac{1}{4}[(w - 2)^2 + (w - 4)^2] = \frac{1}{4}[2w^2 - 12w + 20] = \frac{1}{2}w^2 - 3w + 5$$
- O gradiente global é $\nabla F(w) = w - 3$. Impondo $\nabla F(w^\star) = 0$, obtemos:
  $$w^\star = 3$$
- Avaliando os gradientes individuais no ponto ótimo $w^\star = 3$:
  $$f_1'(w^\star) = 1 \cdot (1 \cdot 3 - 2) = +1$$
  $$f_2'(w^\star) = 1 \cdot (1 \cdot 3 - 4) = -1$$
  Note que $\nabla F(w^\star) = \frac{1}{2}(+1 + (-1)) = 0$, como esperado.
- A variância do gradiente estocástico no ponto ótimo é:
  $$\sigma^2(w^\star) = \frac{1}{2}[(f_1'(w^\star) - 0)^2 + (f_2'(w^\star) - 0)^2] = \frac{1}{2}[(+1)^2 + (-1)^2] = 1$$
- *Efeito da Interpolação Perfeita:* Se $(x_2, y_2) = (1, 2)$, teríamos $w^\star = 2$. Nesse ponto, $f_1'(2) = 0$ e $f_2'(2) = 0$. Ambos os gradientes individuais se anulariam simultaneamente, e a variância seria nula ($\sigma^2(w^\star) = 0$). Na presença de dados ruidosos e contradições reais, contudo, a variância no mínimo nunca é zero.

### 2. Gabarito Comentado dos Testes Conceituais (V/F)
*   **(A) Falso.** A propriedade de não-enviesamento $\mathbb{E}_{i}[\nabla f_i(\mathbf{w})] = \frac{1}{N}\sum_{i=1}^N \nabla f_i(\mathbf{w}) = \nabla F(\mathbf{w})$ decorre exclusivamente da linearidade da esperança matemática e do sorteio uniforme dos índices. Ela é válida para qualquer função derivável, seja convexa, não-convexa ou mesmo côncava.
*   **(B) Verdadeiro.** Se o modelo admite interpolação perfeita com perda nula em todas as amostras ($f_i(\mathbf{w}^\star) = 0$ para todo $i$), e a função de perda é suave e não-negativa (como o erro quadrático ou a entropia cruzada), o ponto de mínimo global de cada função individual coincide com $\mathbf{w}^\star$. Logo, $\nabla f_i(\mathbf{w}^\star) = \mathbf{0}$ para todo $i$, implicando que $\sigma^2(\mathbf{w}^\star) = \frac{1}{N}\sum \|\mathbf{0} - \mathbf{0}\|^2 = 0$.
*   **(C) Falso.** Conforme demonstrado na pergunta aberta, no mínimo global $w^\star = 3$, o gradiente médio é zero, mas os gradientes individuais são $+1$ e $-1$. Logo, o ruído $\boldsymbol{\xi}_1 = 1 - 0 = +1 \neq 0$ e $\boldsymbol{\xi}_2 = -1 - 0 = -1 \neq 0$. O ruído só se anula se todas as amostras individuais tiverem gradiente nulo no mesmo ponto.
*   **(D) Verdadeiro.** Se reescalonamos a perda por $c$, o novo gradiente é $\nabla(c f_i) = c \nabla f_i$. A matriz de covariância é $\Sigma_c = \text{Cov}(c \boldsymbol{\xi}) = \mathbb{E}[(c\boldsymbol{\xi})(c\boldsymbol{\xi})^T] = c^2 \mathbb{E}[\boldsymbol{\xi}\boldsymbol{\xi}^T] = c^2 \Sigma$.

---

## Pausa 3: Mini-Batching e Eficiência de Hardware

### 1. Resolução da Pergunta Aberta
*Cenário:*
- $B = 1$: tempo por passo = $0{,}5\text{ ms} = 5 \times 10^{-4}\text{ s}$.
  $$\text{Throughput} = \frac{1 \text{ amostra}}{0{,}0005\text{ s}} = 2.000\text{ amostras/segundo}$$
- $B = 64$: tempo por passo = $0{,}8\text{ ms} = 8 \times 10^{-4}\text{ s}$.
  $$\text{Throughput} = \frac{64 \text{ amostras}}{0{,}0008\text{ s}} = 80.000\text{ amostras/segundo}$$
- $B = 512$: tempo por passo = $4{,}0\text{ ms} = 4 \times 10^{-3}\text{ s}$.
  $$\text{Throughput} = \frac{512 \text{ amostras}}{0{,}004\text{ s}} = 128.000\text{ amostras/segundo}$$

- **Análise de Hardware:**
  O salto de $B = 1$ para $B = 64$ multiplica o throughput por **40 vezes** (de 2 mil para 80 mil amostras/s), consumindo apenas $0{,}3\text{ ms}$ adicionais de relógio. Isso ocorre porque $B = 1$ deixava as unidades SIMD/Tensor Cores da GPU praticamente ociosas, dominadas pela latência de chamada de kernel. Já o salto de $B = 64$ para $B = 512$ (um aumento de 8 vezes no lote) aumenta o throughput em apenas $1{,}6\times$ (de 80 mil para 128 mil), pois a GPU já atingiu seu regime saturado de computação (*compute-bound*).

### 2. Gabarito Comentado dos Testes Conceituais (V/F)
*   **(A) Verdadeiro.** Pelo Teorema de Redução de Variância sob amostragem com reposição, $\operatorname{Var}(\mathbf{g}_B) = \frac{\sigma^2}{B}$. Para $B = 16$, temos $\sigma^2/16$; para $B = 64$, temos $\sigma^2/64 = \frac{1}{4}(\sigma^2/16)$. A variância cai exatamente por um fator de 4.
*   **(B) Verdadeiro.** Na amostragem sem reposição, o fator de correção de população finita é $\frac{N-B}{N-1}$. Fazendo $B = N$, o numerador torna-se $N - N = 0$, zerando a variância do estimador e recuperando o gradiente determinístico exato do lote completo.
*   **(C) Falso.** Em hardware paralelo real, $B = 1$ sofre de latência de lançamento de instruções e saturação de largura de banda de memória (*memory latency bound*). Embora faça menos FLOPS teóricos por passo, o tempo de relógio por época é ordens de grandeza superior ao de $B = 64$ devido à ineficiência de execução escalar.
*   **(D) Verdadeiro.** Se todos os gradientes individuais são iguais ao gradiente médio ($\nabla f_i(\mathbf{w}) = \nabla F(\mathbf{w})$ para todo $i$), qualquer amostra sorteada fornecerá exatamente o vetor $\nabla F(\mathbf{w})$. O ruído é identicamente nulo e o SGD com $B = 1$ executará passos indistinguíveis do BGD.

---

## Pausa 4: Convergência de Robbins-Monro e Dinâmica Estocástica

### 1. Resolução da Pergunta Aberta
*Análise das três sequências:*
1. $\alpha_k = \frac{1}{\sqrt{k}}$:
   - $\sum_{k=1}^\infty \frac{1}{\sqrt{k}}$ é uma série $p$ com $p = 1/2 \le 1$, que **diverge** ($\sum \alpha_k = \infty$).
   - $\sum_{k=1}^\infty \alpha_k^2 = \sum_{k=1}^\infty \frac{1}{k}$ é a série harmônica ($p = 1$), que também **diverge** ($\sum \alpha_k^2 = \infty$).
   - *Veredito:* Viola a segunda condição de Robbins-Monro. O ruído estocástico acumula variância infinita e o algoritmo não assenta no mínimo exato (permanece oscilando em uma vizinhança residual).
2. $\alpha_k = \frac{1}{k^2}$:
   - $\sum_{k=1}^\infty \frac{1}{k^2} = \frac{\pi^2}{6} < \infty$, logo **converge** ($\sum \alpha_k^2 < \infty$).
   - Contudo, $\sum_{k=1}^\infty \alpha_k = \frac{\pi^2}{6} < \infty$ também **converge**!
   - *Veredito:* Viola a primeira condição de Robbins-Monro. O comprimento total de caminho que o algoritmo pode percorrer é limitado por $\alpha_0 \frac{\pi^2}{6}$. Se $\mathbf{w}_0$ estiver mais distante do que esse raio máximo, o algoritmo congela prematuramente antes de alcançar o mínimo!
3. $\alpha_k = 0{,}01$ (constante):
   - $\sum_{k=1}^\infty 0{,}01 = \infty$ (diverge).
   - $\sum_{k=1}^\infty (0{,}01)^2 = \sum 0{,}0001 = \infty$ (diverge).
   - *Veredito:* Viola a supressão do ruído. Conforme provado no Bloco 4, estaciona em uma bola de ruído de raio proporcional a $\sqrt{\alpha \sigma^2 / \mu}$, nunca convergindo para um ponto fixo.

### 2. Gabarito Comentado dos Testes Conceituais (V/F)
*   **(A) Verdadeiro.** A sequência $\alpha_k = 1/\sqrt{k}$ tem soma divergente ($\sum k^{-1/2} = \infty$), mas o quadrado de seus termos forma a série harmônica $\sum 1/k$, que diverge para o infinito. Logo, viola a segunda condição de Robbins-Monro.
*   **(B) Verdadeiro.** Como a série $\sum 1/k^2$ converge para um número finito ($\approx 1{,}645$), o algoritmo só consegue viajar uma distância euclidiana máxima limitada a partir de $\mathbf{w}_0$. Se o mínimo global estiver fora desse raio de alcance, os passos decaem tão rápido que o otimizador congela no meio do caminho.
*   **(C) Verdadeiro.** A fórmula assintótica da bola de ruído deduzida no Bloco 4 estabelece $\lim_{k \to \infty} \mathbb{E}[\|\mathbf{w}_k - \mathbf{w}^\star\|^2] \le \frac{\alpha \sigma^2}{2\mu}$. Quanto mais fortemente convexa for a função (maior $\mu$), mais íngreme é o poço de potencial, comprimindo a dispersão espacial do ruído estocástico.
*   **(D) Verdadeiro.** Se $\Sigma(\mathbf{w}) = \mathbf{0}$, não existe ruído ($\boldsymbol{\xi}_k = \mathbf{0}$). O SGD reduz-se identicamente ao BGD, para o qual o Lema da Descida garante convergência exata sob qualquer passo $\alpha < 2/L$.

---

## Pausa 5: Síntese e Desafios de Otimização

### 1. Resolução da Pergunta Aberta
*Cenário:* Paisagem anisotrópica com $\kappa = \lambda_{\max}/\lambda_{\min} \gg 1$.
- O gradiente estocástico sofre duplamente: além das oscilações direcionais devidas à curvatura elíptica (onde a força aponta quase perpendicularmente ao eixo do vale), o ruído estocástico $\boldsymbol{\xi}_k$ atua como uma perturbação transversal caótica.
- Na direção do autovetor de maior curvatura ($\lambda_{\max}$), os passos precisam ser minúsculos para não divergir ($\alpha < 2/\lambda_{\max}$). Na direção do autovetor de menor curvatura ($\lambda_{\min}$), o avanço é extremamente lento, e as flutuações do ruído dominam o sinal verdadeiro. O algoritmo ziguezagueia freneticamente entre as paredes do vale, exigindo métodos de aceleração direcional (Momento) ou pré-condicionamento.

### 2. Gabarito Comentado dos Testes Conceituais (V/F)
*   **(A) Falso.** O ruído estocástico é isotrópico ou orientado pelos dados, mas não "alinha" as curvaturas da Hessiana. Em um desfiladeiro com $\kappa \gg 1$, o SGD continua sofrendo de oscilações severas e progresso lento. O escalonamento e pré-condicionamento das variáveis permanecem tão ou mais vitais no SGD quanto no BGD.
*   **(B) Verdadeiro.** Em um ponto de sela com $\nabla F = \mathbf{0}$, o BGD fica paralisado porque o passo é nulo. No SGD, o ruído amostral $\boldsymbol{\xi}_k$ tem componentes não-nulas nas direções dos autovetores com autovalores negativos da Hessiana, fornecendo a perturbação estocástica necessária para empurrar o otimizador morro abaixo.
*   **(C) Verdadeiro.** O *Cosine Annealing* começa com uma taxa de aprendizado alta, permitindo exploração rápida do relevo e travessia de barreiras de potencial, e decai monotonicamente até $\alpha_{\min} \approx 0$, colapsando a bola de ruído para assentar com precisão no fundo do mínimo.
*   **(D) Verdadeiro.** Lotes muito pequenos ($B = 4$) introduzem alta variância de ruído, o que ejetará os parâmetros de mínimos locais estreitos e profundos (*sharp minima*), permitindo que o modelo só estabilize em bacias largas e suaves (*flat minima*), cuja variabilidade sob perturbação de dados é menor, gerando melhor generalização fora da amostra.

