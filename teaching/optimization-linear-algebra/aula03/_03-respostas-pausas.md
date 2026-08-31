# Respostas das Pausas Ativas — Aula 3

> Arquivo de apoio, não publicado (prefixo `_`). Discute as perguntas
> motivadoras das pausas ativas do `index.qmd` e dá a solução dos
> respectivos V/F. O `index.qmd` publicado só contém a pergunta em
> cada pausa ativa (idêntica nas notas e nos slides); a resolução, nos
> slides, aparece no slide seguinte — mas nunca nas notas em HTML.

## Sistemas sobredeterminados e a melhor aproximação

A troca de "solução exata" por "solução aproximada" muda completamente a
contagem de casos da Aula 2. No regime subdeterminado, "mais próximo"
tende a ser trivial (zero, porque já existe solução exata); no regime
sobredeterminado (o caso desta aula, com posto completo), "mais próximo"
tem exatamente uma resposta — é isso que o Bloco 4 vai provar via
projeção ortogonal. A ausência de solução exata não é ausência de
utilidade: é exatamente o problema que a projeção resolve.

- ✔ Subdeterminado, se solúvel: infinitas soluções exatas — a pergunta
  "qual é mais próximo?" perde o sentido de erro irredutível e passa a
  ser sobre escolher entre soluções, não sobre minimizar distância a um
  ponto fora do espaço-coluna.
- ✔ $N=d$ com $X$ de posto completo: sistema quadrado invertível,
  solução exata, erro zero — caso-limite consistente.
- ✔ Mesma estrutura matemática (sistema sobredeterminado resolvido por
  projeção), outro domínio (GPS em vez de preço de imóvel).
- ✗ Falta de solução exata não implica inutilidade — é precisamente o
  problema que a projeção ortogonal resolve nesta aula, dando a melhor
  aproximação possível.

## A intuição da sombra

A "sombra" só funciona como analogia de menor distância quando a luz é
perpendicular ao subespaço — qualquer outro ângulo produz um ponto de
chegada que, em geral, não minimiza a distância (o mesmo argumento do
triângulo retângulo: a hipotenusa de um triângulo formado por um ângulo
oblíquo é maior que o cateto perpendicular). Essa observação geométrica
simples é o que o Bloco 4 formaliza como equivalência entre "mínimo" e
"ortogonal".

- ✗ Luz oblíqua, em geral, não produz o ponto mais próximo — só a
  perpendicular garante a distância mínima; é a mesma geometria do
  Teorema de Pitágoras.
- ✔ Se $\mathbf{y}$ já pertence a $U$, a sombra coincide com o próprio
  $\mathbf{y}$ (resíduo nulo) — caso trivial, mas consistente com a
  definição.
- ✔ Mesma operação geométrica (projeção ortogonal), outro domínio —
  compressão/PCA aparece de novo mais adiante no curso (Aprendizado Não
  Supervisionado).
- ✗ Minimizar a distância a $\mathbf{y}$ não tem nenhuma relação com a
  norma do próprio ponto do subespaço — são duas quantidades
  independentes; a projeção perpendicular não "escolhe" o ponto de
  maior ou menor norma, escolhe o mais próximo de $\mathbf{y}$.

## Subespaços e o complemento ortogonal

O caso do subespaço trivial $\{\mathbf{0}\}$ é o caso-limite mais simples
da definição de complemento ortogonal: como todo vetor tem produto
interno nulo com o vetor nulo, "ortogonal a todo vetor de $U$" é uma
condição vazia quando $U=\{\mathbf{0}\}$ — logo todo vetor de $V$
cumpre, e $U^\perp=V$. O caso simétrico ($U=V$) resulta em
$U^\perp=\{\mathbf{0}\}$.

- ✔ $U=\{\mathbf{0}\}$: qualquer vetor de $V$ é ortogonal ao vetor
  nulo, então a condição que define $U^\perp$ vale para todo vetor de
  $V$ — $U^\perp=V$.
- ✔ Caso simétrico: só o vetor nulo é ortogonal a todo vetor de
  $V=U$, então $U^\perp=\{\mathbf{0}\}$.
- ✔ É exatamente a definição de complemento ortogonal aplicada a
  $U=\text{col}(X)$ — antecipa a conclusão central do Bloco 4.
- ✗ $\dim U=M$ e $\dim U^\perp=D-M$ são iguais apenas se $D=2M$, não em
  geral; na regressão desta aula, $M=4$ e $D-M=16\,636$ — bem
  diferentes.

## Equações Normais e o que a ortogonalidade garante

A equivalência "mínimo $\iff$ ortogonal" do Passo (i) depende
inteiramente da geometria da norma $L_2$ (produto interno, ângulos);
minimizar a norma $L_1$ segue uma lógica distinta (subgradiente nulo),
sem a mesma caracterização por ortogonalidade. E ortogonalidade do
resíduo ao espaço-coluna não é o mesmo que resíduo nulo — só fixa a
*direção* do erro, não o seu tamanho.

- ✗ A equivalência "mínimo $\iff$ ortogonal" é específica da norma
  $L_2$; minimizar $L_1$ não leva à mesma condição geométrica de ângulo
  reto.
- ✔ Se $\mathbf{y}\in\text{col}(X)$, a melhor aproximação é o próprio
  $\mathbf{y}$: as Equações Normais dão um $\hat{\mathbf{w}}$ com
  $X\hat{\mathbf{w}}=\mathbf{y}$ exatamente.
- ✔ Mesma estrutura matemática de mínimos quadrados via projeção, outro
  domínio (calibração de sensores em vez de preço de imóvel).
- ✗ Ortogonalidade ao espaço-coluna não força resíduo nulo — só força
  que o resíduo esteja no complemento ortogonal; ele só é zero quando
  $\mathbf{y}$ já estava em $\text{col}(X)$, exceção e não regra no caso
  sobredeterminado.

## Verificação numérica: algoritmos diferentes, mesma equação

`lstsq`, eliminação de Gauss e inversão explícita de $X^TX$ resolvem a
mesma equação — as Equações Normais —, então (a menos de erro de
arredondamento) devem produzir o mesmo $\hat{\mathbf{w}}$; a diferença
entre eles é robustez numérica, não o resultado matemático. E
ortogonalidade do resíduo é uma consequência necessária das Equações
Normais, não uma coincidência da amostra — mas não tem relação com o
quão bom é o ajuste em termos de $R^2$: vimos $R^2\approx 0{,}518$ com
resíduo perfeitamente ortogonal.

- ✔ Mesma equação ($X^TX\hat{\mathbf{w}}=X^T\mathbf{y}$), algoritmos
  diferentes (inversão, eliminação, decomposição): mesmo resultado a
  menos de arredondamento.
- ✗ É consequência **necessária** de $X^T(\mathbf{y}-X\hat{\mathbf{w}})=\mathbf{0}$,
  não coincidência — vale para toda amostra em que $\hat{\mathbf{w}}$
  resolve as Equações Normais.
- ✔ A verificação (produto interno do resíduo com cada coluna $\approx
  0$) é uma identidade algébrica geral, independente de domínio ou
  escala dos atributos.
- ✗ Vimos, nesta aula, $R^2\approx 0{,}518$ com resíduo perfeitamente
  ortogonal — ortogonalidade fixa a *direção* do erro, não seu
  *tamanho*; um ajuste fraco (poucos atributos relevantes) pode ter
  resíduo perfeitamente ortogonal e $R^2$ baixo ao mesmo tempo.

## Multicolinearidade e o que permanece estável

A distinção central do Bloco 6 é entre a *projeção* $\hat{\mathbf{y}}$
(geometricamente determinada, estável) e a *decomposição* em
$\hat{\mathbf{w}}$ (pode ser não-única ou instável quando há colunas
redundantes ou quase-redundantes). Qualquer múltiplo escalar não-nulo de
uma coluna já existente, ou qualquer combinação linear exata das demais,
tem o mesmo efeito sobre o posto — não importa a forma específica da
redundância.

- ✔ Qualquer coluna que seja combinação linear exata das demais colunas
  não acrescenta direção nova ao espaço gerado — o posto cai da mesma
  forma, seja a redundância um múltiplo simples ou uma combinação mais
  complexa.
- ✔ Correlação exatamente $1$ é dependência linear exata: $X^TX$ ficaria
  singular, mesma consequência da coluna duplicada do Caso 1.
- ✔ Mesma mecânica de quase-dependência (colunas fortemente
  correlacionadas, mas não exatamente proporcionais), outro domínio
  (crédito em vez de imóveis).
- ✗ É o oposto do observado nos números: a projeção $\hat{\mathbf{y}}$
  (o ponto mais próximo de $\mathbf{y}$ em $\text{col}(X)$) é
  geometricamente determinada e muda pouco sob perturbação; é a
  **decomposição** em $\hat{\mathbf{w}}$ entre colunas quase-redundantes
  que oscila descontroladamente — exatamente o padrão "sombra estável,
  receita instável" visto também no Caso 1 (multicolinearidade exata).
