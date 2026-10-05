# Respostas da Aula 6 — Pausas Ativas

> Arquivo de apoio, não publicado (prefixo `_`). Discussão em prosa das
> 5 pausas ativas do `index.qmd` (a pergunta motivadora + a resolução
> do V/F, que no `index.qmd` só aparece nos slides RevealJS, nunca nas
> notas HTML).
>
> (O gabarito dos 6 blocos de V/F da seção Exercícios **não** é
> discutido aqui — vive em `exercicios.qmd`/`soluções.qmd`, páginas
> públicas e separadas desta aula.)

### Pausa 1 — Trocar a variável latente categórica (GMM) por uma contínua muda o tipo de problema que se resolve, ou é só uma variação técnica?

Muda o tipo de pergunta que se faz aos dados, mas não a lógica de
fundo. No GMM (Aulas 3–5), $z_n$ respondia "de qual das $K$ populações
este ponto veio?" — uma resposta discreta, um rótulo entre $K$ opções.
Aqui, $\mathbf{z}\in\mathbb{R}^M$ responde "que posição, num espaço
contínuo de dimensão $M$, resume este ponto?" — uma resposta em
princípio muito mais rica (um contínuo de posições, não $K$
categorias), mas ainda a mesma tarefa de fundo: **resumir sem perder o
que importa**. A partição em $K$ categorias fixas é, na verdade, um
caso particular (mais grosseiro) dessa mesma tarefa, só com variável
latente discreta em vez de contínua — por isso o item (a) é
verdadeiro.

O item (b) generaliza a mesma lógica ao caso-limite $M=D$: sem redução
de dimensionalidade nenhuma (guardar todos os $D$ números), qualquer
base ortonormal completa reconstrói cada ponto exatamente, com
distorção zero — não há mais critério que distinga uma base de outra,
e "escolher a melhor direção" deixa de ser um problema bem definido
(o Mecanismo II vai formalizar isso via $J^\star=\sum_{i=M+1}^D\lambda_i=0$
quando $M=D$).

O item (c) é a armadilha central desta pausa: é tentador pensar que,
porque a decomposição do ELBO $\mathcal{L}(q)+\mathrm{KL}(q\|p)$ da
Aula 5 não assume nada sobre a natureza de $\mathbf{Z}$ (discreta ou
contínua), ela deveria ser a ferramenta "certa" também aqui — mas isso
confunde **generalidade** da decomposição com **necessidade de uso**.
Para uma estrutura puramente linear-Gaussiana (o que a PPCA vai
formalizar no bloco da PPCA), a decomposição espectral fechada da PCA
clássica é uma ferramenta muito mais direta, sem otimização iterativa
nenhuma; o ELBO entra só quando a posterior deixa de ter forma fechada
— o que não é o caso aqui.

Por fim, o item (d) já antecipa o bloco seguinte, do autoencoder linear (cujo produto $\mathbf{W}\mathbf{V}$ é justamente uma fatoração de baixo posto): a mesma tarefa
de "resumir muitos números em poucos números que preservam o que
importa" reaparece ao comprimir os pesos de uma camada de rede neural
por fatoração de baixo posto, mesmo antes de qualquer treinamento
supervisionado — o objeto muda (parâmetros de rede em vez de dados
brutos), a lógica matemática não.

- ✔ Uma partição em $K$ categorias fixas É uma forma (bem mais
  grosseira) de redução de dimensionalidade — um rótulo entre $K$
  opções também resume o ponto, só que com uma variável latente
  discreta.
- ✔ Com $M=D$, todo ponto é reconstruído exatamente por qualquer base
  completa (eq. 12.9 do PRML) — a distorção é $0$ para qualquer
  escolha de base, tornando a otimização degenerada (múltiplas
  soluções igualmente ótimas).
- ✗ A decomposição do ELBO é geral, mas isso não torna o ELBO a
  ferramenta "certa" por padrão — para uma estrutura puramente linear,
  a PCA (decomposição espectral fechada, sem otimização iterativa) é a
  ferramenta mais direta; o ELBO entra quando a posterior não é
  calculável em forma fechada.
- ✔ Fatoração de baixo posto de uma matriz de pesos é exatamente o
  mesmo problema de "poucos números que preservam o que importa",
  aplicado a parâmetros de rede em vez de dados.

### Pausa 2 — Duas redes treinadas com sementes diferentes chegam ao mesmo erro de reconstrução, mas dão códigos latentes diferentes ao mesmo paciente. Qual delas aprendeu o espaço latente "certo"?

Nenhuma — ou as duas. O erro de reconstrução só enxerga o produto
$\mathbf{W}\mathbf{V}$, e para qualquer $\mathbf{G}$ invertível o par
$(\mathbf{G}\mathbf{V},\mathbf{W}\mathbf{G}^{-1})$ tem o mesmo produto.
Os códigos mudam para $\mathbf{G}\mathbf{z}_n$, mas o plano
$\mathcal{C}(\mathbf{W})$ em que as reconstruções vivem não muda. O que
os dados determinam é o **plano**; os **eixos** dentro dele são uma
convenção. Duas redes com o mesmo erro aprenderam o mesmo plano em
coordenadas diferentes. Para compará-las, compara-se planos (por
exemplo, pelos ângulos principais entre eles), não coordenadas — ou
fixa-se uma convenção de eixos, que é o que a PCA fará: eixos
ortonormais, ordenados pela variância que carregam.

O item (a) é o caso mais simples da invariância, $\mathbf{G}=2I$:
multiplicar o codificador por $2$ e dividir o decodificador por $2$
mantém o produto e dobra os códigos. Quem marca F está pensando que o
mínimo do erro fixa os pesos individualmente.

O item (b) usa o caso-limite $M=D$: sem gargalo, $\mathbf{W}=\mathbf{V}^{-1}$
dá $\mathbf{W}\mathbf{V}=I$ e reconstrução perfeita, mas o "código
latente" é só uma mudança de coordenadas de $\mathbb{R}^D$, sem
compressão nenhuma. A utilidade do espaço latente vem do gargalo
$M<D$.

O item (c) é a falsa equivalência central: "o erro só depende de
$\mathbf{W}\mathbf{V}$" é verdade, mas a conclusão correta é a oposta —
exatamente por isso a coordenada $z_1$ isolada não tem significado fixo
entre redes.

O item (d) transfere a mesma estrutura para outro modelo de ML: numa
fatoração $R\approx PQ^T$ para recomendação, $PGG^{-1}Q^T=PQ^T$, e os
fatores latentes de usuários e itens só estão definidos a menos de
$G$ — o mesmo motivo pelo qual "o fator latente 3" de um sistema de
recomendação não tem interpretação garantida.

- ✔ É a invariância com $\mathbf{G}=2I$: $\tfrac12\mathbf{W}\cdot2\mathbf{V}=\mathbf{W}\mathbf{V}$, mesmo erro, códigos $2\mathbf{z}_n$.
- ✔ $\mathbf{W}\mathbf{V}=I$ reconstrói tudo; sem gargalo, o código é só uma mudança de coordenadas de $\mathbb{R}^D$.
- ✗ Os códigos mudam para $\mathbf{G}\mathbf{z}_n$ sem mudar o erro: $z_1$ isolado não tem significado fixo entre redes.
- ✔ Mesma estrutura de produto de fatores: $PGG^{-1}Q^T=PQ^T$.

### Pausa 3 — O multiplicador de Lagrange λ1 é só um artifício técnico da restrição, ou carrega significado próprio?

Carrega significado pleno, não é só mecânica de otimização. A prova do
Mecanismo II mostra isso em dois passos: primeiro, $\mathbf{Su}_1=
\lambda_1\mathbf{u}_1$ obriga $\mathbf{u}_1$ a ser autovetor de
$\mathbf{S}$; segundo, pré-multiplicando por $\mathbf{u}_1^T$ e usando
$\mathbf{u}_1^T\mathbf{u}_1=1$, chega-se a
$\mathbf{u}_1^T\mathbf{S}\mathbf{u}_1=\lambda_1$ — ou seja, no ponto
ótimo, $\lambda_1$ **é**, literalmente, o valor da variância projetada
máxima, não um subproduto técnico da restrição de Lagrange.

O item (a) testa a direção oposta do mesmo argumento: se em vez de
maximizar minimizássemos $\mathbf{u}^T\mathbf{S}\mathbf{u}$ sob a mesma
restrição, o mesmo argumento de Lagrange (mesma equação de
estacionariedade $\mathbf{Su}=\lambda\mathbf{u}$) levaria ao autovetor
de **menor** autovalor — inverter a direção da otimização inverte qual
extremo do espectro é selecionado, sem mudar a mecânica.

O item (b) usa o caso-limite $\mathbf{S}=\mathbf{I}$ (dados
isotrópicos, sem correlação e todas as variâncias iguais):
$\mathbf{u}^T\mathbf{Iu}=\|\mathbf{u}\|^2=1$ para qualquer
$\mathbf{u}$ unitário — todo "autovalor" é igual a $1$, e nenhuma
direção é preferível a outra; a ideia de "melhor direção" só faz
sentido quando há alguma anisotropia real nos dados.

O item (c) é a falsa dicotomia central da pausa — o texto usa o jargão
certo ("$\lambda_1$ aparece só para impor a restrição") para chegar a
uma conclusão errada ("não tem significado interpretável"); o próprio
Passo 4 do Mecanismo II mostra exatamente o contrário.

O item (d) estende a mesma equação de autovalores
$\mathbf{Su}=\lambda\mathbf{u}$ a outro contexto de ML: a análise
espectral da matriz do Laplaciano de um grafo, base do *clustering*
espectral — mesma estrutura matemática (autovalores/autovetores de uma
matriz simétrica), aplicada a outro objeto (o Laplaciano, não a
covariância).

- ✔ Inverter para minimização inverte a direção da desigualdade de
  Lagrange, favorecendo o menor autovalor — a mesma mecânica, sentido
  oposto.
- ✔ Com $\mathbf{S}=I$, $\mathbf{u}^TI\mathbf{u}=\|\mathbf{u}\|^2=1$
  para qualquer $\mathbf{u}$ unitário — nenhuma direção é preferível.
- ✗ Pelo contrário: $\mathbf{u}_1^T\mathbf{S}\mathbf{u}_1=\lambda_1$
  no ótimo — $\lambda_1$ **é**, literalmente, a variância projetada
  máxima, um número com significado direto, não só mecânico.
- ✔ Autovalores/autovetores da matriz Laplaciana de um grafo são
  exatamente a base do *clustering* espectral — mesma estrutura
  matemática, outro domínio de aplicação dentro de ML.

### Pausa 4 — Se as unidades ocultas usassem ativação não linear, o mínimo global mudaria de subespaço?

Não, na arquitetura rasa — e essa é precisamente a ressalva que o DLFC
destaca (citada no bloco De Volta ao Autoencoder, logo depois da prova): trocar só a ativação por uma função não
linear (por exemplo sigmoide), mantendo a mesma arquitetura
$D$-$M$-$D$ de uma única camada oculta, ainda leva o mínimo do erro de
reconstrução ao mesmo subespaço de PCA. A não linearidade, isoladamente,
não é o que falta — é a **profundidade** (camadas adicionais de
unidades não lineares) que permite escapar da limitação linear, o
assunto da Aula 7.

O item (a) é exatamente essa ressalva.

O item (b) usa o caso-limite $M=D$: sem gargalo real, qualquer base
completa do espaço de entrada permite reconstrução exata: com
$\mathbf{V}$ invertível, $\mathbf{W}=\mathbf{V}^{-1}$ dá
$\mathbf{W}\mathbf{V}=I$. O mesmo caso-limite reaparece na PCA clássica
($J^\star=0$ quando $M=D$, Mecanismo II) e no item (a) do bloco de
Exercícios sobre o autoencoder linear.

O item (c) é a falsa dicotomia mais sutil desta pausa: o Teorema
garante que o autoencoder encontra o mesmo **subespaço** ótimo (mesmo
erro mínimo), não que os pesos aprendidos formem a mesma **base
ortonormal** dos autovetores da PCA. É a invariância por $\mathbf{G}$
do bloco do autoencoder (e da Pausa 2): $(\mathbf{G}\mathbf{V},\mathbf{W}\mathbf{G}^{-1})$
tem o mesmo erro para qualquer $\mathbf{G}$ invertível, e na rede
treinada os dois vetores de pesos de entrada têm cosseno
$\approx-0{,}58$ entre si, longe de ortogonais.

O item (d) generaliza a técnica de prova anunciada para o Teorema do autoencoder (mostrar que
duas famílias de soluções alcançáveis coincidem, logo os mínimos dos
respectivos problemas de otimização coincidem) para outro contexto de
ML: o mesmo tipo de argumento de equivalência por redução aparece ao
comparar a solução de Ridge com $\lambda\to0$ contra mínimos quadrados
ordinários — dois problemas de otimização formalmente diferentes que,
no limite, convergem à mesma solução.

- ✔ Exatamente a ressalva do DLFC citada no bloco — arquitetura rasa,
  mesmo não linear, ainda encontra o mesmo subespaço de PCA; é preciso
  profundidade extra para escapar.
- ✔ Com $M=D$ e $\mathbf{V}$ invertível, $\mathbf{W}=\mathbf{V}^{-1}$
  dá $\mathbf{W}\mathbf{V}=I$: toda entrada é reconstruída exatamente.
- ✗ O Teorema garante o mesmo **subespaço** (mesmo erro), não a mesma
  **base** — os pesos podem ser qualquer base desse subespaço, não
  precisando ser ortonormais (invariância por $\mathbf{G}$; cosseno
  $\approx-0{,}58$ na rede treinada).
- ✔ Mesma técnica de prova: mostrar equivalência de duas famílias de
  soluções alcançáveis (ou convergência no limite) para concluir que os
  mínimos coincidem — usada em vários contextos de otimização em ML.

### Pausa 5 — Se a distribuição condicional da PPCA usasse covariância geral em vez de isotrópica, o limite σ²→0 ainda recuperaria a PCA do mesmo jeito?

Não do mesmo jeito — o argumento do limite $\sigma^2\to0$ depende crucialmente de
$\sigma^2$ ser um **único** escalar isotrópico, não uma matriz de
covariância geral $\boldsymbol\Sigma$. A demonstração do caso-limite
(posterior média
$\to(\mathbf{W}^T\mathbf{W})^{-1}\mathbf{W}^T(\mathbf{x}-\bar{\mathbf{x}})$
quando $\sigma^2\to0$) usa o fato de haver exatamente um parâmetro
escalar de ruído a ser levado a zero; com $\boldsymbol\Sigma$ geral,
não há mais esse único grau de liberdade a anular, e o modelo se
aproxima de uma estrutura mais geral (Análise Fatorial), cujo
comportamento limite não coincide necessariamente com a projeção
ortogonal da PCA.

O item (a) é exatamente essa conclusão, generalizada.

O item (b) explora um caso-limite complementar, dentro do próprio
regime isotrópico: quando $\sigma^2\to0$, a covariância marginal
$\mathbf{C}=\mathbf{WW}^T+\sigma^2\mathbf{I}\to\mathbf{WW}^T$, que tem
posto no máximo $M<D$ — uma matriz $D\times D$ de posto deficiente é,
por definição, singular (não invertível). Isso é consistente (não
contraditório) com o resultado do bloco da PPCA: no limite exato
$\sigma^2=0$ a densidade de $\mathbf{x}$ deixa de ter forma completa
(degenera sobre o subespaço, o mesmo fenômeno do item (a) do Exercício
3 sobre PPCA determinística), e é por isso que a demonstração do bloco
da PPCA trata $\sigma^2\to0$ como limite, nunca $\sigma^2=0$ exatamente.

O item (c) é uma falsa dicotomia sedutora: "modelo probabilístico" não
implica "sempre mais informativo" — o bloco da PPCA provou exatamente o
oposto no caso-limite, que os dois métodos produzem o mesmo resultado
quando $\sigma^2\to0$.

O item (d) fecha a pausa situando a PPCA dentro de uma família mais
ampla: a mesma estrutura de variável latente linear-Gaussiana (prior
Gaussiano sobre $\mathbf{z}$, observação linear mais ruído Gaussiano) é
a base da Análise Fatorial, historicamente anterior à PPCA e usada em
psicometria — a PPCA é, na prática, um caso particular/restrito da
Análise Fatorial (ruído isotrópico em vez de ruído diagonal geral).

- ✔ Com $\boldsymbol\Sigma$ geral (não isotrópica), não há um único
  escalar de ruído a levar a zero — o argumento do limite $\sigma^2\to0$
  perde a variável que precisa desaparecer; o modelo vira algo mais
  próximo de Análise Fatorial, com comportamento limite diferente.
- ✔ $\mathbf{WW}^T$ tem posto no máximo $M<D$ — no limite,
  $\mathbf{C}\to\mathbf{WW}^T$, singular por construção.
- ✗ Pelo contrário: o bloco da PPCA mostrou que ela **recupera exatamente**
  a PCA clássica no limite $\sigma^2\to0$ — "sempre mais informativa,
  nunca igual" contradiz esse resultado central.
- ✔ PRML observa essa conexão explicitamente — PPCA é um caso
  particular/restrito de Análise Fatorial, mesma estrutura de variável
  latente linear-Gaussiana.
