## Resumo — Aula 12

A Aula 11 terminou com uma observação que inverte o paradigma usado até ali: em vez de fixar a métrica ou o espaço de atributos de antemão (como o kernel da MMD), o teste por classificador **aprende** uma função diretamente a partir da tarefa de distinguir duas amostras, sem rótulos anotados. A Aula 12 generaliza essa ideia para o **aprendizado de representações auto-supervisionado**: treinar um codificador neural para distinguir pares de visões que pertencem ao mesmo objeto (pares positivos) de pares de objetos distintos (pares negativos), usando a perda **InfoNCE**.

A aula parte de uma falha fundamental dos modelos de reconstrução das Aulas 6 e 7 (PCA e Autoencoder): quando a variância dominante dos dados vem de atributos irrelevantes (*nuisance*, como ruído de fundo ou iluminação), minimizar o erro quadrático de reconstrução desperdiça a capacidade do espaço latente. Mostramos então como a definição operacional de invariância por aumentação de dados leva ao colapso trivial se não houver força repulsiva, motivando a perda contrastiva InfoNCE. No núcleo teórico da aula, derivamos o crítico ótimo de Bayes como a razão de densidades $p(\mathbf{x}'\mid\mathbf{x})/p(\mathbf{x}')$, provamos a **cota inferior da Informação Mútua** $I(\mathbf{x};\mathbf{x}^+) \ge \ln(K+1) - \mathcal{L}_{\text{InfoNCE}}$ (Oord et al., 2018; Poole et al., 2019), e analisamos a geometria das representações normalizadas na hiperesfera $\mathbb{S}^{M-1}$ via decomposição em **alinhamento** e **uniformidade** (Wang & Isola, 2020). O último bloco trata de escolhas arquiteturais e práticas — temperatura $\tau$, número de negativos $K$, cabeça de projeção (*projection head*) e escolha de aumentações — e encerra o curso conectando os três blocos da disciplina.

**Objetivos:**
1. Explicar por que métodos baseados em reconstrução (PCA, Autoencoders) falham quando a variância dominante não coincide com a semântica, e por que invariância sem repulsão leva ao colapso da representação.
2. Formular a perda InfoNCE e derivar que seu ótimo de Bayes estima a razão de densidades $\frac{p(\mathbf{x}'\mid \mathbf{x})}{p(\mathbf{x}')}$.
3. Demonstrar a relação entre InfoNCE e a cota inferior da Informação Mútua, $I(\mathbf{x};\mathbf{x}^+) \ge \ln(K+1) - \mathcal{L}_{\text{InfoNCE}}$, identificando o papel limitante do número de negativos $K$.
4. Interpretar a geometria da InfoNCE na hiperesfera unitária $\mathbb{S}^{M-1}$ em termos de alinhamento de positivos e uniformidade (entropia máxima) dos negativos, bem como o papel da temperatura $\tau$.
5. Avaliar escolhas práticas (cabeça de projeção $g_{\boldsymbol\psi}$, força das aumentações, avaliação via *linear probe*) e situar métodos sem negativos explícitos (BYOL, SimSiam, Barlow Twins).

**Pré-requisitos (conferidos no dicionário de notações):** entropia diferencial/discreta e divergência KL (Aulas 5, 7 e 8); PCA e autoencoder como codificadores por reconstrução (Aulas 6 e 7); distância cosseno em alta dimensão (Aula 2); kernel Gaussiano (Aulas 2 e 11); teste por classificador como aprendizado de função discriminativa sem rótulos (Aula 11).

**Estratégia Pedagógica:** A (*Outside-In*) — parte-se da falha empírica da PCA e do Autoencoder num problema com *nuisance* de alta variância, passa-se ao colapso do alinhamento puro, e introduz-se a teoria (InfoNCE, MI e geometria esférica) para explicar e controlar o comportamento observado.

**Datasets:**
1. **Sintético 20D (Sinal 2D + Ruído 18D de alta variância):** 1.200 pontos de 3 classes em $\mathbb{R}^2$ concatenados a 18 dimensões de ruído gaussiano ($\sigma_{\text{nuis}} = 3{,}0$). Serve como contraexemplo limpo onde PCA e AE falham (~33–40% no *linear probe*) e InfoNCE atinge ~100%.
2. ***Digits* (`sklearn.datasets.load_digits`):** 1.797 imagens $8\times 8$ (64 pixels) de dígitos manuscritos (0–9), sem necessidade de download externo. Usado para treinar um codificador SimCLR em PyTorch (~3–5 s em CPU), comparar $\mathbf{h}$ vs $\mathbf{z}$ (cabeça de projeção), e rodar ablações de temperatura $\tau$ e tamanho de lote $B$ ($K = 2B-2$).

---

## Plano de aula — Aula 12 (carga horária: 60 min)

1. **Revisão e Introdução** (~6 min) — Ponte da Aula 11 (teste por classificador aprende a distinguir amostras sem rótulos); o problema com reconstrução (PCA/AE no dataset sintético 20D com *nuisance* de alta variância); a ideia de aprender invariância a perturbações estocásticas e as 4 perguntas da aula.
2. **Bloco 1: Invariância, Colapso e a Perda InfoNCE** (~14 min, com Pausa 1) — Definição operacional de par positivo via aumentação $t \sim \mathcal{T}$; por que minimizar só $\|\mathbf{z}_1 - \mathbf{z}_2\|^2$ leva ao colapso constante; formulação da InfoNCE como classificação $(K+1)$-ária de ruído contrastivo (Oord et al., 2018) e versão em lote do SimCLR (Chen et al., 2020).
3. **Bloco 2: Teoria da Informação — Razão de Densidades e Cota de Informação Mútua** (~16 min, com Pausa 2) — Revisão de $I(X;Y) = \mathrm{KL}(p(x,y)\|p(x)p(y))$; derivação do crítico ótimo de Bayes $f^\star(\mathbf{x},\mathbf{x}') = \ln \frac{p(\mathbf{x}'\mid \mathbf{x})}{p(\mathbf{x}')} + c(\mathbf{x})$; prova da cota $I(\mathbf{x};\mathbf{x}^+) \ge \ln(K+1) - \mathcal{L}_{\text{InfoNCE}}$; discussão do teto $\ln(K+1)$ e da necessidade de $K$ grande.
4. **Bloco 3: Geometria na Hiperesfera — Alinhamento, Uniformidade e Temperatura** (~12 min, com Pausa 3) — Normalização $\mathbf{z}\in\mathbb{S}^{M-1}$; decomposição assintótica de Wang & Isola (2020) em $\mathcal{L}_{\text{align}}$ e $\mathcal{L}_{\text{uniform}}$ (conexão com kernel Gaussiano da Aula 11); dilema uniformidade-tolerância governado por $\tau$; resultados e ablações reais em `load_digits`.
5. **Bloco 4: Arquitetura, Armadilhas Práticas e Panorama Moderno** (~9 min, com Pausa 4) — Papel da cabeça de projeção $g_{\boldsymbol\psi}$ ($\mathbf{h}$ vs $\mathbf{z}$); princípio InfoMin para escolha de aumentações; panorama breve de métodos sem negativos explícitos (MoCo, BYOL/SimSiam, Barlow Twins).
6. **Fechamento da Aula e do Curso** (~3 min) — Retomada das 4 perguntas; quadro comparativo (PCA/AE vs VAE vs InfoNCE); síntese integradora das 12 aulas.

**Se faltar tempo:** nos slides, resumir os passos intermediários da cota de Informação Mútua (remetendo às notas para a prova completa) e os itens V/F das Pausas 3 e 4 (mantendo as perguntas abertas).

---

## Notação nova e colisões

- $\mathbf{h} = f_{\boldsymbol\phi}(\mathbf{x}) \in \mathbb{R}^M$: representação aprendida pelo codificador (*backbone*), usada no *linear probe*. **Colisão:** $h$ é a largura de banda do KDE (Aula 2), $\mathbf{H}$ é a variável latente genérica (Aula 5) e $H$ é a matriz da NMF (Aula 10); além disso $H(\cdot)$ nesta aula denota entropia de Shannon.
- $\mathbf{z} = g_{\boldsymbol\psi}(\mathbf{h}) / \|g_{\boldsymbol\psi}(\mathbf{h})\|_2 \in \mathbb{S}^{M_z-1}$: projeção normalizada na hiperesfera unitária (reuso de $\mathbf{z}$ contínuo das Aulas 6–7, agora restrito à esfera unitária).
- $(\mathbf{x}, \mathbf{x}^+)$ e $\{\mathbf{x}_j^-\}_{j=1}^K$: par positivo (duas visões estocásticas da mesma amostra) e $K$ amostras negativas da marginal $p(\mathbf{x})$. **Colisão de $K$:** $K$ vizinhos (Aulas 2–3) e $K$ componentes de mistura (Aulas 4–5).
- $\tau > 0$: parâmetro de temperatura na *softmax* da InfoNCE.
- $\mathcal{L}_{\text{InfoNCE}}$: perda contrastiva (reuso de $\mathcal{L}$, que denotava o ELBO nas Aulas 5 e 7).
- $I(X; Y)$: Informação Mútua entre $X$ e $Y$.
- $\text{sim}(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u}^T\mathbf{v}}{\|\mathbf{u}\|\|\mathbf{v}\|}$: similaridade cosseno (evita colisão com $s(i)$ da Silhueta na Aula 5 e $s(I)$ do suporte na Aula 9).

---

## Fontes usadas — Aula 12

1. **Oord, A. van den, Li, Y., & Vinyals, O. (2018).** *Representation Learning with Contrastive Predictive Coding*. arXiv:1807.03748. (Definição da perda InfoNCE, crítico ótimo proporcional à razão de densidades e cota inferior de Informação Mútua.)
2. **Poole, B., Ozair, S., Oord, A. van den, Alemi, A. A., & Tucker, G. (2019).** *On Variational Bounds of Mutual Information*. ICML 2019. (Formalização rigorosa das cotas variacionais de Informação Mútua e do limite $\ln(K+1)$ da InfoNCE.)
3. **Chen, T., Kornblith, S., Norouzi, M., & Hinton, G. (2020).** *A Simple Framework for Contrastive Learning of Visual Representations (SimCLR)*. ICML 2020. (Formulação em lote $2N$, normalização $\ell_2$, temperatura $\tau$, papel empírico da cabeça de projeção $g_{\boldsymbol\psi}$ e composição de aumentações.)
4. **Wang, T., & Isola, P. (2020).** *Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere*. ICML 2020. (Decomposição assintótica em alinhamento e uniformidade com kernel Gaussiano na hiperesfera $\mathbb{S}^{M-1}$.)
5. **Tian, Y., Sun, C., Poole, B., Krishnan, D., Schmid, C., & Isola, P. (2020).** *What Makes for Good Views for Contrastive Learning? (InfoMin)*. NeurIPS 2020. (Princípio InfoMin para escolha de aumentações de dados.)
6. **Bishop, C. M., & Bishop, H. (2024).** *Deep Learning: Foundations and Concepts* (DLFC). Springer. (Fundamentos de entropia, KL, informação mútua e aprendizado auto-supervisionado.)
