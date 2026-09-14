# Gabarito — Aula 5 (Decomposição em Valores Singulares e Aproximações de Baixo Posto)

Arquivo de apoio, nunca publicado (prefixo `_`). Contém a discussão das 5
Pausas Ativas (com a resolução dos V/F condutores, que no `index.qmd`
só aparecem — com glifo resolvido — nos slides RevealJS, nunca nas
notas HTML). O gabarito da seção Exercícios (agora pública) vive em
`soluções.qmd`.

## Pausas Ativas

### Pausa Ativa 1 (Abertura) — "De volta a $X^TX$: o que muda (e o que não muda) para $X$"

**Discussão.** A pergunta motivadora pedia para verificar se autovalor e
autovetor "existem, só que garantidos de forma mais fraca" para uma
matriz retangular — a resposta correta é mais radical: eles não existem
**de forma alguma**, porque a própria equação $A\mathbf{x}=
\lambda\mathbf{x}$ perde tipo (lados em espaços diferentes) quando
$A$ não é quadrada. O Teorema Espectral Real (Aula 4) é uma afirmação
sobre matrizes simétricas, não sobre "matrizes em geral que dá para
tentar simetrizar" — $X^TX$ é sempre simétrica **por construção**
($X^TX)^T=X^TX^{TT}=X^TX$, mas isso não empresta nenhuma propriedade de
volta para $X$.

**V/F resolvido:**

- ✗ Simetria é hipótese do teorema, não consequência de ser quadrada
  — sem ela, autovalores podem ser complexos (Aula 4, Bloco 3, matrizes
  de rotação).
- ✗ Posto $1$ $\Rightarrow$ só um valor singular não-nulo — um único
  perfil já explica toda a matriz (o Bloco 5 confirma isso formalmente).
- ✔ Mesma mecânica ($W$ retangular sem autovalores, com SVD sempre
  bem definida), outro modelo de ML (camada linear de rede neural).
- ✗ Confunde a entidade: a garantia é sobre $X^TX$ (sempre quadrada),
  não sobre $X$ — se $X$ for retangular, ela simplesmente não tem
  autovalores, não é "secundária".

### Pausa Ativa 2 (Intuição Geométrica) — "Autovetor e vetor singular: a mesma seta, dois papéis diferentes?"

**Discussão.** A figura do Bloco 2 já entrega a resposta visualmente:
os vetores singulares $\mathbf{v}_1,\mathbf{v}_2$ (colunas de $V$) são,
por construção, sempre ortogonais entre si — a ortogonalidade vem
direto do Teorema Espectral aplicado a $A^TA$ (Aula 4), que não exige
nada sobre $A$ além de existir. Os autovetores de $A$, em contraste,
só têm garantia de ortogonalidade quando $A$ é simétrica. A matriz do
Bloco 2 foi escolhida deliberadamente não-simétrica para tornar essa
diferença visível: $\approx 106{,}9°$ entre autovetores vs. exatamente
$90°$ entre vetores singulares.

**V/F resolvido:**

- ✔ Exatamente o que o Bloco 3 prova: se $A=A^T$, a SVD e a
  decomposição espectral coincidem (a menos de sinal em casos com
  autovalor negativo — ver Exercícios, bloco "SVD vs. decomposição
  espectral").
- ✔ O Teorema 4.22 (MathML) não faz nenhuma hipótese sobre os
  autovalores de $A$ — a SVD existe mesmo que $A$ (quadrada) tenha
  autovalores complexos.
- ✔ A mesma mecânica do painel esquerdo do Bloco 2 se generaliza para
  qualquer matriz de pesos não-simétrica.
- ✗ Confunde ortogonalidade **entre os vetores singulares** com a
  forma da imagem — o formato (círculo ou elipse) é determinado pelos
  fatores de escala $\sigma_i$, não pela ortogonalidade de
  $\mathbf{u}_1,\mathbf{u}_2$ (que vale sempre, mesmo quando a imagem é
  uma elipse bem achatada).

### Pausa Ativa 3 (Construção Formal) — "Se $A^TA$ tivesse autovalor negativo, a construção quebraria onde?"

**Discussão.** O ponto de ruptura é preciso: o Passo 1 usa
$\sigma_i:=\sqrt{\lambda_i}$, e essa raiz só é garantidamente real
porque a Premissa 1 (Aula 4: $A^TA$ é sempre semidefinida positiva,
$\lambda_i\ge 0$) está disponível. Sem essa premissa — por exemplo, se
alguém tentasse aplicar a mesma receita a uma matriz $M$ qualquer que
não fosse da forma $A^TA$ — a raiz cairia em números complexos e a
construção inteira desmoronaria já no primeiro passo.

**V/F resolvido:**

- ✔ Exatamente: sem a Premissa 1, $\sqrt{\lambda_i}$ cairia em números
  complexos — a construção não teria por onde nem começar.
- ✗ Só vale para matrizes **normais** ($AA^T=A^TA$); uma matriz
  invertível qualquer, não-simétrica, tem valores singulares diferentes
  dos módulos de seus autovalores (o próprio exemplo do Bloco 2:
  autovalor $\approx1{,}642$ vs. valor singular $\approx1{,}675$ —
  próximos, mas não iguais).
- ✔ Mesma mecânica (raiz de autovalor PSD), aplicação já vista (Aula 4,
  Bloco 6 — covariância empírica, sempre PSD).
- ✗ A garantia é sobre $A^TA$, não sobre $A$ — uma matriz $A$ quadrada
  qualquer pode ter autovalores negativos ou complexos mesmo com $A^TA$
  garantidamente PSD.

### Pausa Ativa 4 (SVD de $X$) — "$\sigma_{\min}(X)=0$: o que isso diria sobre as 4 colunas?"

**Discussão.** $\sigma_{\min}=0 \Rightarrow \lambda_{\min}(X^TX)=0$
(pela identidade $\sigma_i^2=\lambda_i$) $\Rightarrow X^TX$ singular
$\Rightarrow$ posto incompleto de $X$ (critério já estabelecido nas
Aulas 2-3) $\Rightarrow$ colunas linearmente dependentes. É exatamente
o mesmo fenômeno de multicolinearidade exata já visto (a coluna
duplicada $2\times$`AveRooms` das Aulas 2-4), agora visto pela lente dos
valores singulares.

**V/F resolvido:**

- ✔ Correto — a cadeia de implicações acima é exata, sem nenhuma
  aproximação.
- ✗ **Correção importante:** a Proposição $\text{cond}(X^TX)=
  \text{cond}(X)^2$ (Bloco 4) diz exatamente o contrário do que o item
  afirma. Se $\sigma_{\max}=\sigma_{\min}$ (todos os valores singulares
  iguais), então $\text{cond}(X)=1$ e, pela Proposição,
  $\text{cond}(X^TX)=1^2=1$ também — longe de "não dizer nada", o
  valor de $\text{cond}(X^TX)$ fica completamente determinado.
- ✔ Mesma mecânica (valor singular pequeno $\Rightarrow$ direção quase
  redundante), outro cenário de ML (embeddings de palavras).
- ✗ A identidade poupa **uma** conta (obter $\sigma$ a partir de
  $\lambda$ já calculado), mas não substitui a SVD inteira — os vetores
  $\mathbf{u}_i$ (dimensão $16\,640$, o codomínio) não vêm de $X^TX$
  sozinha, e são usados nos Blocos 5-6 (aproximação de baixo posto,
  decomposição polar).

### Pausa Ativa 5 (Aproximação de Baixo Posto) — "Um perfil de gosto totalmente novo, fora dos $k$ perfis capturados"

**Discussão.** $\hat{A}^{(k)}$ é, por construção, uma combinação linear
de exatamente $k$ perfis latentes (os $k$ primeiros pares
$\mathbf{u}_i,\mathbf{v}_i$) — ela não tem "espaço" para representar
nenhuma direção fora desse subespaço de dimensão $k$, não importa
quantos dados históricos existam sobre esse espectador específico. Isso
não é uma falha do método: é exatamente o que "posto $k$" significa.
Como o erro $\|A-\hat{A}^{(k)}\|_2$ é não-crescente em $k$ (cada termo
adicional só pode ajudar, nunca atrapalhar — os $\sigma_i$ são
não-negativos por definição), aumentar $k$ sempre é uma opção segura
quando se suspeita de um perfil não capturado, mas nunca ultrapassa a
otimalidade que o Teorema de Eckart-Young-Mirsky já garante para cada
$k$ fixo.

**V/F resolvido:**

- ✔ Exatamente a limitação estrutural: um perfil ortogonal aos $k$ já
  capturados fica fora do alcance de $\hat{A}^{(k)}$, dados históricos
  ou não.
- ✔ $\sigma_i\ge 0$ sempre, e $\hat{A}^{(k+1)}=\hat{A}^{(k)}+
  \sigma_{k+1}\mathbf{u}_{k+1}\mathbf{v}_{k+1}^T$ só adiciona
  informação — o erro é monótono não-crescente em $k$.
- ✔ Mesma mecânica (perfis/tópicos latentes truncados), outro cenário
  de ML (embeddings de texto/tópicos latentes).
- ✗ O Teorema de Eckart-Young-Mirsky é exatamente a garantia contrária:
  $\hat{A}^{(k)}$ **já é** o mínimo global entre todas as matrizes de
  posto $k$ — nenhum método alternativo pode reduzir $\sigma_{k+1}$
  para o mesmo $k$.
