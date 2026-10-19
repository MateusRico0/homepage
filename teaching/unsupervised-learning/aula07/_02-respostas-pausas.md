# Respostas das Pausas Ativas — Aula 7

Os números citados vêm da execução da aula (setup global do `index.qmd`).

## Pausa 1 — O Que Restringe a Reconstrução

**Pergunta aberta:** se o decoder fosse uma função afim de $\mathbf{z}$, $\hat{\mathbf{x}}=\mathbf{B}\mathbf{z}+\mathbf{c}$, que forma teria o conjunto de todas as reconstruções possíveis, por mais complicado que fosse o encoder?

**Resposta:** um subespaço afim $\mathbf{c}+\mathcal{C}(\mathbf{B})$ de dimensão $\le M$, ou seja, um "plano". O encoder, por mais complexo, só escolhe o vetor $\mathbf{z}$, isto é, em que ponto desse plano cada dado cai; o plano em si é fixado pelo decoder. Para que a superfície de reconstruções se curve, a não linearidade precisa estar entre $\mathbf{z}$ e $\hat{\mathbf{x}}$. É o que explica a ressalva do DLFC (p. 565) de que o AE raso com unidades ocultas não lineares continua com a solução da PCA.

**V/F:**

- ✗ No MNIST com $M=2$, a PCA reconstrói pior que o AE profundo porque a PCA não minimiza o erro quadrático de reconstrução. A PCA minimiza o erro quadrático, mas apenas entre reconstruções sobre subespaços. O AE procura numa classe maior de funções; a diferença é de classe, não de critério.
- ✔ Um autoencoder com várias camadas ocultas, todas lineares, tem erro mínimo de treino igual ao da PCA com o mesmo $M$. A composição é linear e o gargalo limita o posto a $M$ (Teorema da Aula 6).
- ✗ Erro de treino menor garante melhor resumo para dados novos. É *double-dipping* (Aula 5); o Breast Cancer do Bloco 1 é o contraexemplo.
- ✔ Na PPCA, a covariância da posterior é $\sigma^2\mathbf{B}^{-1}$, que não depende de $\mathbf{x}$ (PRML p. 573).

## Pausa 2 — Quando a Flexibilidade Compensa

**Pergunta aberta:** no Breast Cancer, o AE profundo reduz o erro de treino a um terço do da PCA e piora no teste. O que mudaria esse resultado: mais camadas, mais pacientes ou um $M$ maior?

**Resposta:** mais camadas ou um $M$ maior aumentam a capacidade e tendem a agravar o sobreajuste. O que ajuda é aumentar a informação disponível (mais pacientes) ou restringir a capacidade (rede menor, regularização como *weight decay*, parada antecipada guiada por um conjunto de validação). Antes de tudo, convém perguntar se há curvatura real a capturar: na Aula 6, um único componente principal já explicava 44,27% da variância e separava os diagnósticos com 92,1% de acerto; com estrutura quase linear e $455$ pontos, a PCA é o modelo adequado. No MNIST ($20\,000$ imagens, variedade curva), a mesma flexibilidade compensa.

**V/F:**

- ✗ Camadas não lineares só no encoder, com decoder afim, não curvam a reconstrução (Proposição do Bloco 1).
- ✔ Com $M=D$ a identidade passa pelo gargalo e o erro de treino é zero sem resumir nada.
- ✗ O erro deixa de ser quadrático nos parâmetros; o problema é não convexo e o gradiente pode parar em mínimos locais (DLFC p. 566).
- ✔ No *denoising*, entrada corrompida $\ne$ alvo limpo, então copiar não zera o erro, mesmo com camada mais larga que a entrada (DLFC §19.1.4).

## Pausa 3 — Corrigir o Espaço Latente Depois

**Pergunta aberta:** ajustar uma distribuição aos códigos do AE já treinado (uma Gaussiana, ou um GMM da Aula 4) e sortear dela resolveria o problema de gerar?

**Resposta:** em parte. Uma distribuição ajustada descreve onde os códigos estão e reduz o número de amostras em regiões vazias. Um GMM, por exemplo, acompanha melhor os aglomerados do que uma Gaussiana. Mas três problemas permanecem: (i) o decoder continua sem nenhum sinal de treino fora dos códigos, de modo que a qualidade nas regiões entre aglomerados não é controlada; (ii) a forma da nuvem é acidente do treino (invariância por reparametrização), e outro treino daria outra forma; (iii) não há $p(\mathbf{x}\mid\mathbf{z})$, logo não há verossimilhança para comparar modelos. O VAE ataca o problema pelo lado oposto: fixa $p(\mathbf{z})$ antes do treino e força encoder e decoder a respeitá-la. Na aula, a fração de amostras longe de todo código de treino foi de alguns por cento com a Gaussiana ajustada ao AE e de menos de 1% com a priori do VAE.

**V/F:**

- ✗ Padronizar acerta média e variância de cada coordenada, mas não remove ilhas nem buracos; uma nuvem multimodal padronizada não é Gaussiana.
- ✗ Reconstruir bem os pontos de treino não diz nada sobre o decoder nos buracos entre os códigos.
- ✗ Sem $p(\mathbf{x}\mid\mathbf{z})$ não há verossimilhança; e, mesmo acrescentando ruído, a integral $\int p(\mathbf{x}\mid\mathbf{z})p(\mathbf{z})\,\mathrm{d}\mathbf{z}$ com decoder não linear não tem forma fechada.
- ✔ $\mathbf{h}(\mathbf{z})=\mathbf{G}\mathbf{z}$ é um caso particular de reparametrização invertível do espaço latente.

## Pausa 4 — Um Encoder para Todos

**Pergunta aberta:** por que não otimizar uma $q_n(\mathbf{z}_n)$ separada para cada ponto? O que se ganha e o que se perde com um único encoder?

**Resposta:** com uma $q_n$ por ponto, cada aproximação pode chegar mais perto de sua posterior (só a família Gaussiana limita), mas são $N$ problemas de otimização, todos refeitos a cada atualização de $\mathbf{w}$, e cada ponto novo exige mais uma otimização (DLFC p. 572). Com o encoder único (inferência amortizada), a inferência de um ponto novo é uma passagem pela rede, e pontos parecidos compartilham informação. Perde-se precisão: a rede impõe uma função suave $\mathbf{x}\mapsto(\boldsymbol\mu,\boldsymbol\sigma)$, e essa folga de amortização se soma à da família Gaussiana diagonal.

**V/F:**

- ✔ Com decoder afim, o modelo é a PPCA, cuja posterior é Gaussiana (PRML eq. 12.42).
- ✗ A covariância exata $\sigma^2\mathbf{B}^{-1}$, com $\mathbf{B}=\mathbf{W}^T\mathbf{W}+\sigma^2\mathbf{I}$, só é diagonal quando as colunas de $\mathbf{W}$ são ortogonais entre si. Pela invariância a rotações da Aula 6, há soluções $\mathbf{W}$ em que ela não é diagonal, e então a Gaussiana diagonal não a representa.
- ✔ É o ganho da amortização: uma passagem pelo encoder, sem otimização.
- ✗ Sobra a folga $\mathrm{KL}(q\|p(\mathbf{z}\mid\mathbf{x}))>0$ (DLFC p. 573); no Bloco 4, ela foi estimada em pelo menos 5 nats por imagem no MNIST.

## Pausa 5 — O Termo Que Organiza o Espaço

**Pergunta aberta:** sem o termo KL ($\beta=0$), o encoder levou $\sigma_{nj}$ a quase zero. Por que o treino "quer" eliminar o ruído da amostragem, e o que o termo KL faz para impedir isso?

**Resposta:** o termo de reconstrução é avaliado em $\mathbf{z}=\boldsymbol\mu+\boldsymbol\sigma\odot\boldsymbol\epsilon$. Quanto maior $\boldsymbol\sigma$, mais longe do código ideal o decoder recebe a entrada, e pior a reconstrução esperada. Sozinho, esse termo leva $\boldsymbol\sigma\to0$, e o VAE vira um AE determinístico (na aula, $\sigma_{nj}$ médio da ordem de $10^{-3}$, com escala latente arbitrária). A parcela $-\tfrac12\ln\sigma_j^2$ da KL cresce sem limite quando $\sigma_j\to0$, e a parcela $\tfrac12\mu_j^2$ puxa as médias para a origem. O equilíbrio fica num $\sigma_{nj}>0$: cada dado ocupa uma nuvem, e o decoder aprende a responder bem a toda a vizinhança do código, que é o que permite gerar a partir da priori.

**V/F:**

- ✔ Os minimizadores dependem só de $\beta\sigma^2$; dobrar qualquer um dos dois dá o mesmo produto.
- ✗ O mínimo da parcela é em $\sigma_j=1$ e $\mu_j=0$; em $\sigma_j\to0$ ela vai a $+\infty$.
- ✔ KL $\approx0$ para todo ponto significa $q(\mathbf{z}\mid\mathbf{x})\approx p(\mathbf{z})$: *posterior collapse* (DLFC p. 577).
- ✗ Trocar a verossimilhança afeta só o termo de reconstrução (que vira entropia cruzada); o KL compara $q$ com a priori e não muda.

## Pausa 6 — Quando Não Há Caminho Contínuo

**Pergunta aberta:** num modelo com latente categórica (um GMM com decoder neural), como obter o gradiente do termo de reconstrução em relação aos parâmetros do encoder?

**Resposta:** não existe $\mathbf{z}=h(\boldsymbol\phi,\boldsymbol\epsilon)$ diferenciável que só assuma $K$ valores, então a reparametrização não se aplica diretamente (DLFC p. 575: "limitado a variáveis contínuas"). Há duas saídas. (i) O estimador *score function*, que usa apenas valores de $f$ e a derivada de $\ln q(k\mid\mathbf{x},\boldsymbol\phi)$, e funciona com $\mathbf{z}$ discreta, ao custo da variância alta. (ii) Com $K$ pequeno, somar exatamente sobre as categorias: $\mathbb{E}_q[f]=\sum_kq(k\mid\mathbf{x},\boldsymbol\phi)f(k)$, que é diferenciável em $\boldsymbol\phi$ sem amostragem. É a mesma soma ponderada por responsabilidades do passo E do GMM.

**V/F:**

- ✗ Não enviesado não é o mesmo que preciso: com $L=1$, o desvio-padrão do *score function* foi dezenas de vezes maior que o da reparametrização.
- ✔ Lema da reparametrização, componente a componente, com componentes independentes.
- ✗ O gradiente continua sendo uma estimativa de Monte Carlo (sobre $\boldsymbol\epsilon$ e sobre o minilote); o truque muda a variância, não a natureza estocástica.
- ✔ $\exp:\mathbb{R}\to(0,\infty)$ é bijetora; a família representável é a mesma, sem restrição na saída da rede.
