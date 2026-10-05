# Respostas das Pausas Ativas — Aula 07

## Pausa 1: O que define um "Manifold"?

**Pergunta aberta:** Se os dados de alta dimensão residem em um manifold de baixa dimensão, o que acontece com a distância euclidiana entre dois pontos próximos no manifold quando medida no espaço original?

**Resposta:** A distância euclidiana no espaço original pode ser enganosa. Dois pontos podem estar próximos no manifold (seguindo a curvatura da superfície), mas distantes no espaço original se a medida for feita em linha reta através do "vazio" (fora do manifold). O Autoencoder tenta aprender a métrica intrínseca do manifold para que a distância no espaço latente reflita a similaridade real.

**V/F:**
- ✔ Um Autoencoder linear com gargalo $M$ aprende o mesmo subespaço que a PCA.
- ✔ A função de ativação ReLU introduz a não linearidade necessária para aprender manifolds.
- ✗ Aumentar a dimensão do gargalo ($M$) sempre melhora a generalização do modelo. (Gargalos muito grandes levam ao mapeamento identidade/overfitting).
- ✔ O objetivo de um AE é minimizar a distância entre a entrada e a reconstrução.

## Pausa 2: O Gap Generativo

**Pergunta aberta:** O que aconteceria se forçássemos todos os $\mathbf{z}$ a estarem dentro de um círculo unitário? Isso resolveria o problema dos "buracos" no espaço latente?

**Resposta:** Apenas mudar a escala não resolve. O problema é a topologia do espaço. Podemos ter todos os pontos dentro do círculo, mas com "ilhas" de dados separadas por vastos desertos de baixa probabilidade. Precisamos de uma força (como a regularização KL do VAE) que "empurre" as representações para preencher o espaço de forma regular e contínua.

**V/F:**
- ✗ O Autoencoder tradicional aprende a densidade de probabilidade dos dados. (Ele aprende um mapeamento determinístico).
- ✔ No AE, a função de custo penaliza a distância entre a entrada e a saída.
- ✔ Um espaço latente contínuo é essencial para a interpolação de características.
- ✗ O decoder de um AE funciona como um modelo generativo por definição. (Ele reconstrói, mas não sabe como amostrar novos dados coerentes).

## Pausa 3: Reparameterization Trick

**Pergunta aberta:** O que acontece se removermos o termo KL do VAE? O modelo ainda consegue gerar imagens?

**Resposta:** Se removermos o KL, o VAE vira essencialmente um AE tradicional com ruído. Ele ainda consegue reconstruir, mas o espaço latente perde a regularização. Se você amostrar um $\mathbf{z}$ aleatório de $\mathcal{N}(\mathbf{0}, \mathbf{I})$, as chances de cair em um "buraco" (região não visitada durante o treino) são altíssimas, resultando em imagens que não se parecem com dígitos.

**V/F:**
- ✔ O Reparameterization Trick torna a amostragem diferenciável.
- ✗ No VAE, o encoder prevê o valor exato de $\mathbf{z}$ para cada $\mathbf{x}$. (Ele prevê $\boldsymbol\mu$ e $\boldsymbol\sigma$).
- ✔ A divergência KL no VAE atua como um regularizador do espaço latente.
- ✔ O decoder de um VAE é capaz de transformar qualquer $\mathbf{z} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ em um dado plausível (desde que bem treinado).
