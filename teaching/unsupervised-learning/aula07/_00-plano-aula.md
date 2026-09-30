## Resumo — Aula 07
A aula transita da redução de dimensionalidade linear (PCA/PPCA) para a não linear. Começa com Autoencoders (AE) tradicionais, explorando a hipótese do manifold e a compressão via redes profundas. Em seguida, aborda a limitação dos AEs como modelos generativos, introduzindo os Variational Autoencoders (VAE). O foco técnico é a aplicação do ELBO (visto na Aula 5) em redes neurais, culminando no *reparameterization trick* para permitir o treinamento via gradiente descendente.

**Estratégia Pedagógica:** A (Outside-In) — Parte-se da necessidade de compressão não linear (AE) para a necessidade de um espaço latente estruturado (VAE), finalizando com a fundamentação matemática (ELBO e Reparametrização).

**Dataset-fio:** 
1. Breast Cancer (comparação de erro de reconstrução: Linear vs Não Linear).
2. MNIST (via Hugging Face) para visualização de interpolação no espaço latente e geração de amostras.

## Plano de aula — Aula 07 (carga horária: 90 min)
1. **Revisão e Introdução** (~10 min) — Ponte da Aula 6 (Linear AE $\equiv$ PCA). O que acontece quando trocamos a ativação linear por $\sigma(\cdot)$? Problema motivador: reconstruir dados com curvatura.
2. **Intuição — O Gargalo e o Manifold** (~10 min) — A ideia de "estrangulamento" de informação. A hipótese do manifold: dados de alta dimensão residem em variedades de baixa dimensão.
3. **Bloco 1: Autoencoders (AE) Tradicionais** (~15 min) — Arquitetura (Encoder/Decoder). Função de custo (MSE). O risco do mapeamento identidade e a necessidade de subespaços reduzidos.
4. **Bloco 2: O Gap Generativo** (~10 min) — Por que o AE não é generativo? O espaço latente "buracado". A diferença entre compressão e modelagem de densidade.
5. **Bloco 3: Variational Autoencoders (VAE)** (~15 min) — A mudança de paradigma: o Encoder agora estima parâmetros de uma distribuição $q(\mathbf{z}|\mathbf{x})$. O Decoder como modelo generativo $p(\mathbf{x}|\mathbf{z})$.
6. **Bloco 4: O Objetivo do VAE (ELBO)** (~15 min) — Retomada da Aula 5. Decomposição do custo: Erro de Reconstrução (Fidelidade) vs Divergência KL (Regularização). O equilíbrio entre "memorizar" e "generalizar".
7. **Bloco 5: O Reparameterization Trick** (~10 min) — O problema do gradiente através de amostragem estocástica. A solução: $\mathbf{z} = \boldsymbol\mu + \boldsymbol\sigma \odot \boldsymbol\epsilon$.
8. **Fechamento** (~5 min) — Retomando as perguntas. Ponte para a Aula 8: quando a reconstrução não basta e queremos preservar a topologia local (MDS/t-SNE).

## Fontes usadas — Aula 07
### Fonte 1: Goodfellow et al., "Deep Learning", Cap. 14
**Uso pretendido:** Definição de Autoencoders e a discussão sobre a função de custo de reconstrução.
**Trecho:**
> "An autoencoder is a feed-forward network that trains to minimize a reconstruction function, which measures the difference between the input and the reconstruction."

### Fonte 2: Kingma & Welling, "Auto-Encoding Variational Bayes" (2013)
**Uso pretendido:** Fundamentação do VAE e a derivação do *reparameterization trick*.
**Trecho:**
> "The reparameterization trick is a method to rewrite the random variable as a deterministic transformation of an independent noise variable, allowing gradients to propagate back to the parameters of the distribution."

### Fonte 3: PRML, §10.1
**Uso pretendido:** Revisão de Inferência Variacional e ELBO para conectar com a Aula 5.
**Trecho:**
> "The evidence lower bound (ELBO) is a lower bound on the log-marginal likelihood of the observed data."
