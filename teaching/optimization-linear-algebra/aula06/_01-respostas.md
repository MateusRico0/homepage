# Gabarito — Aula 6 (Derivadas Parciais, Jacobiano e o Vetor Gradiente)

Arquivo de apoio, nunca publicado (prefixo `_`). Contém a discussão das
5 Pausas Ativas (com a resolução dos V/F condutores, que no `index.qmd`
só aparecem — com glifo resolvido — nos slides RevealJS, nunca nas
notas HTML). O gabarito da seção Exercícios (agora pública) vive em
`soluções.qmd`.

## Pausas Ativas

### Pausa Ativa 1 (Abertura) — "Com 1 parâmetro já sabemos achar o mínimo. Com 4, o quê muda?"

**Discussão.** No Cálculo 1, "achar o mínimo" se resume a igualar a
derivada a zero e checar o sinal em volta. Com $4$ parâmetros, "a
derivada" deixa de ser um único número — a pergunta motivadora da
Abertura ("em que direção mover $\boldsymbol{\beta}$?") só faz sentido
porque existem **infinitas** direções possíveis assim que há mais de um
parâmetro, não só quando há "muitos". A resposta certa exige um objeto
matemático novo (vetor, não escalar) que resuma a taxa de variação em
todas as direções ao mesmo tempo — o gradiente, construído a partir do
Bloco 2 em diante.

**V/F resolvido:**

- ✔ Exatamente o problema que abre a aula: falta um objeto matemático
  novo (vetor) para substituir "a derivada" com várias variáveis.
- ✗ A partir de $2$ parâmetros já existem infinitas direções no plano
  de parâmetros — a pergunta não exige "muitos" parâmetros, só mais de
  um.
- ✔ Mesma mecânica, outro modelo de ML (rede neural via gradiente).
- ✗ $X^TX$ cresce com o quadrado do número de parâmetros, e invertê-la
  custa o cubo — inviável para milhões de parâmetros, não uma questão
  de escala "de brinquedo".

### Pausa Ativa 2 (Derivada Parcial) — "Se a perda dependesse só de $\beta_1$, o que ocorre com $\partial L/\partial\beta_2$?"

**Discussão.** "Fixar as demais variáveis" na Definição 5.5 é uma
operação sobre **qual variável varia** na razão incremental — não uma
afirmação de que o valor numérico da derivada parcial é independente
das demais variáveis. No exemplo do Bloco 2, $\partial L/
\partial\beta_1=2\sum_ir_i\texttt{MedInc}_i$ depende do valor de
$\beta_2$ através de $r_i$ — as duas coisas (definição vs. valor
calculado) não podem ser confundidas.

**V/F resolvido:**

- ✔ Sem $\beta_2$ na expressão, a derivada parcial em relação a uma
  variável ausente é indefinida.
- ✗ A soma $2\sum_ir_i\texttt{MedInc}_i$ é calculável para qualquer
  valor de $r_i$, inclusive esse específico.
- ✔ Mesma mecânica, outro modelo de ML (regressão logística).
- ✗ $r_i$ depende de $\beta_2$, e $r_i$ entra na fórmula de
  $\partial L/\partial\beta_1$ — o valor muda com $\beta_2$, mesmo que a
  definição "fixe" $\beta_2$ apenas no sentido de qual variável varia.

### Pausa Ativa 3 (Gradiente) — "Trocar o quadrado por $L_1$ ($\sum_i|r_i|$): a derivação continua igual?"

**Discussão.** O Passo 1 do Bloco 3 usa a regra da cadeia com
$h(t)=t^2$, $h'(t)=2t$ — válida porque $h$ é diferenciável em
**todo** ponto. Trocar por $h(t)=|t|$ quebra exatamente aí: $|t|$ tem
um "bico" em $t=0$ (não-diferenciável), e o resíduo $r_i$ pode assumir
o valor $0$ para algum ponto de $\boldsymbol{\beta}$ — a derivação por
extenso deixa de valer nesse(s) ponto(s). O restante do argumento
(Passos 2-3, regra da soma) não depende do formato de $h$.

**V/F resolvido:**

- ✔ Exatamente o ponto de ruptura: a cadeia precisa de $h$
  diferenciável; $|t|$ falha em $t=0$, ponto que o resíduo pode
  atingir.
- ✔ Nada no argumento usa $n=4$ — vale para qualquer número de
  colunas.
- ✔ Regra da soma (MathML §5.2.1): gradiente da soma = soma dos
  gradientes.
- ✗ O Passo 2 usa que $r_i$ é afim (qualquer $X$), não uma
  particularidade do California Housing.

### Pausa Ativa 4 (Derivada Direcional) — "$\nabla f(\mathbf{x})=\mathbf{0}$: o que a Proposição diz sobre a direção de subida?"

**Discussão.** A hipótese $\nabla f(\mathbf{x})\ne\mathbf{0}$ é usada
explicitamente na prova, na divisão por $\|\nabla f(\mathbf{x})\|$ —
sem ela, a Proposição simplesmente não tem nada a dizer. De fato, com
$\nabla f(\mathbf{x})=\mathbf{0}$, $D_{\mathbf{v}}f(\mathbf{x})=
\nabla f(\mathbf{x})\cdot\mathbf{v}=0$ para **toda** direção — não há
nenhuma direção que aumente $f$ a uma taxa positiva de primeira ordem.
Esse é, precisamente, o critério de ponto crítico que abre a Aula 7.

**V/F resolvido:**

- ✔ Exatamente a hipótese usada na divisão da prova — sem ela, nada é
  garantido, e $\nabla f=\mathbf{0}$ é o critério de ponto crítico.
- ✗ $D_{\mathbf{v}}f(\mathbf{x})=0$ para toda direção **é** o que
  acontece quando $\nabla f=\mathbf{0}$ — a implicação no item vai na
  direção errada (empate entre direções não força gradiente nulo em
  geral, só quando **todas** empatam em zero).
- ✔ A proposição é local — o número de mínimos locais da superfície
  inteira é irrelevante para a direção de subida naquele ponto
  específico.
- ✗ O máximo é $\|\nabla f(\mathbf{x})\|$, quase sempre maior que
  qualquer componente individual isolada (soma de quadrados de todas
  as componentes, não uma só).

### Pausa Ativa 5 (Jacobiano) — "Modelo com 2 saídas: como muda a forma do Jacobiano do resíduo?"

**Discussão.** A Definição 5.6 organiza o Jacobiano com uma linha por
componente de saída e uma coluna por variável de entrada (*numerator
layout*). Aumentar o número de saídas por observação aumenta o número
de **linhas**; aumentar o número de atributos (parâmetros) aumenta o
número de **colunas** — os dois graus de liberdade são independentes
entre si, e a regra da cadeia com Jacobiano (Bloco 5) vale para
qualquer composição diferenciável, não só para a perda quadrática desta
aula.

**V/F resolvido:**

- ✔ *Numerator layout*: linhas = elementos de $f$ — $2$ saídas por
  observação dobra as linhas.
- ✔ Colunas = número de parâmetros, independente do número de saídas.
- ✔ Numerator layout: linhas = elementos de $f$ (aqui, os $10$
  neurônios de saída) — exatamente a Definição 5.6.
- ✗ A regra da cadeia com Jacobiano (MathML Exemplo 5.11, adaptado)
  vale para qualquer composição diferenciável $g\circ\mathbf{r}$ — a
  perda quadrática é só o caso usado nesta aula.
