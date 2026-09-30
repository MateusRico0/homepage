## Revisão desta sessão (ajuste e refinamento)

O rascunho anterior tinha um bug que impedia qualquer render: o
dataset California Housing foi carregado com a coluna alvo chamada
`"target"`, mas a coluna real (confirmada testando `load_dataset`) é
`MedHouseVal` — corrigido nas três ocorrências do chunk de setup.
Também havia `:::` desbalanceado (abertura de bloco HTML faltando
antes de "Resumo e Ponte") e nenhuma Pausa Ativa na aula inteira.

Refinamentos de conteúdo, além do bug: (1) a Abertura passou a
recapitular explicitamente a patologia de separação perfeita da Aula 6
como gancho de Ausubel, em vez de só "MLE fica instável"; (2) Ridge
ganhou a derivação fechada $\hat{\boldsymbol\beta}_{\text{Ridge}} =
(X^TX+\lambda I)^{-1}X^T\mathbf{y}$, mostrando explicitamente que
resolve a singularidade do Bloco 1; (3) a ponte Bayesiana ganhou as
duas derivações completas (prior Gaussiana → Ridge com $\lambda =
\sigma^2/\tau^2$; prior de Laplace → Lasso com $\lambda=\sigma^2/b$),
que antes só eram citadas por fonte, sem dedução própria; (4) a
"geometria da sparsity" ganhou uma prova algébrica (soft-thresholding
via subgradiente em 1D), além da intuição visual do diamante — a versão
anterior só tinha a intuição, sem prova, o que viola a regra de
`../../CLAUDE.md` de que todo resultado não óbvio precisa de
demonstração. Adicionadas 4 Pausas Ativas (uma por bloco de
desenvolvimento, seguindo o padrão de três blocos da Aula 6: HTML +
"Pergunta" + "Resposta" em RevealJS). `exercicios.qmd`/`soluções.qmd`
expandidos de 2 discursivas + 3 blocos de V/F (12 itens, sem cobrir MAP)
para 3 discursivas + 6 blocos de V/F (24 itens, cobrindo também MAP,
as duas derivações e soft-thresholding). Removido `00-plano-aula.md`
(duplicata sem underscore, publicava por engano).

---

# Resumo — Aula 7

Esta aula aborda a regularização de modelos lineares, conectando a prática de adicionar penalidades de complexidade ($L_1$ e $L_2$) com a fundamentação estatística Bayesiana. O objetivo é mostrar que regularizar não é apenas um "truque" para evitar overfitting, mas sim o resultado de incorporar crenças prévias (*priors*) sobre a distribuição dos parâmetros.

**Estratégia Pedagógica:** Estratégia B (Inside-Out com Problema-Fio) — Partiremos da necessidade de controlar a variância de estimadores de máxima verossimilhança (MLE) para introduzir a ideia de que parâmetros podem ser tratados como variáveis aleatórias com distribuições de probabilidade conhecidas.

**Dataset-fio:** California Housing (`gvlassis/california_housing`) — um dataset de regressão com atributos em escalas muito diferentes. Isso é ideal para demonstrar por que a regularização é necessária (para lidar com multicolinearidade e escalas) e como o Ridge/Lasso reage a diferentes distribuições de features.

## Plano de aula — Aula 7 (carga horária estimada: ~130min)

1. **Bloco 0 — Abertura: O problema da complexidade excessiva** (~15 min) — Revisão rápida de MLE e a tendência de modelos complexos de "decorar" o ruído. Pergunta: "Como podemos punir modelos que têm parâmetros excessivamente grandes ou complexos?" Roteiro: de penalidades ad-hoc ao paradigma Bayesiano.

2. **O limite da Máxima Verossimilhança (MLE)** (~20 min) — Mostrar como o MLE em modelos lineares pode produzir coeficientes instáveis quando há multicolinearidade ou quando o número de parâmetros se aproxima do número de observações. Introdução ao conceito de *overfitting* via parâmetros.

3. **Regularização Frequentista: Ridge e Lasso** (~30 min) — Apresentação das penalidades $L_2$ (Ridge) e $L_1$ (Lasso). Demonstração prática: como o Ridge "encolhe" os coeficientes e como o Lasso pode zerá-los (seleção de variáveis). Uso de gráficos de trajetórias de coeficientes ($\alpha$ vs $\beta$).

Mostrar que Ridge tem formula fechada e pode ser usado o gradiente descendente.

Explicar que o Lasso vai ter problemas tanto para formula fechada quanto para gradiente. Explicar como soft thresholding trabalha o gradiente da Loss para ficar como perda com L1.

Explicar o algoritmo de soft thresholding.

4. **A Ponte Bayesiana: De Penalidades a Priors** (~30 min) — O salto conceitual: mostrar que adicionar uma penalidade $L_2$ ao log-verossimilhança é matematicamente equivalente a realizar uma estimativa MAP com uma *prior* Gaussiana. Mostrar que o Lasso equivale a uma *prior* de Laplace.

5. **MAP (Maximum A Posteriori) e a Geometria da Sparsity** (~25 min) — Formalismo de MAP: $P(\theta|D) \propto P(D|\theta)P(\theta)$. Explicação geométrica de por que a "forma" da prior (círculo para Gaussiana, diamante para Laplace) faz com que o Lasso encontre soluções esparsas nos eixos.

6. **Fechamento e ponte** (~10 min) — Recapitulação. Ponte para a Aula 8: como essa regularização afeta o tradeoff viés-variância que será analisado formalmente.

## Fontes usadas — Aula 7

### Fonte 1: ESL, §3.4, pp. 63-67
**Uso pretendido:** Definição formal de Ridge e Lasso e a motivação para o controle de complexidade.

**Trecho:**
> "Ridge regression... is a method for shrinking the regression coefficients towards zero... Lasso regression... performs variable selection by forcing some coefficients to be exactly zero."

### Fonte 2: PRML, §3.3.1, pp. 119-121
**Uso pretendido:** Derivação da estimativa MAP e a conexão com a distribuição de probabilidade dos parâmetros.

**Trecho:**
> "The MAP estimate is the mode of the posterior distribution... it can be seen as a regularized version of the MLE."

### Fonte 3: PRML, §3.3.2, pp. 122-124
**Uso pretendido:** Explicação da prior Gaussiana e Laplace e sua relação com Ridge e Lasso.

**Trecho:**
> "A Gaussian prior on the weights leads to the Ridge regression solution... A Laplace prior leads to the Lasso solution."
