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
(o Bloco 3 vai formalizar isso via $J^\star=\sum_{i=M+1}^D\lambda_i=0$
quando $M=D$).

O item (c) é a armadilha central desta pausa: é tentador pensar que,
porque a decomposição do ELBO $\mathcal{L}(q)+\mathrm{KL}(q\|p)$ da
Aula 5 não assume nada sobre a natureza de $\mathbf{Z}$ (discreta ou
contínua), ela deveria ser a ferramenta "certa" também aqui — mas isso
confunde **generalidade** da decomposição com **necessidade de uso**.
Para uma estrutura puramente linear-Gaussiana (o que a PPCA vai
formalizar no Bloco 5), a decomposição espectral fechada da PCA
clássica é uma ferramenta muito mais direta, sem otimização iterativa
nenhuma; o ELBO entra só quando a posterior deixa de ter forma fechada
— o que não é o caso aqui.

Por fim, o item (d) já antecipa a ponte para o Bloco 6: a mesma tarefa
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

### Pausa 2 — O multiplicador de Lagrange λ1 é só um artifício técnico da restrição, ou carrega significado próprio?

Carrega significado pleno, não é só mecânica de otimização. A prova do
Bloco 3 mostra isso em dois passos: primeiro, $\mathbf{Su}_1=
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
Passo 3 do Bloco 3 mostra exatamente o contrário.

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

### Pausa 3 — A alta acurácia obtida (92,1%) sem usar o rótulo prova que a PCA "sabia" sobre o diagnóstico durante o ajuste?

Não — e a pergunta é uma armadilha de causalidade clássica: correlação
(alta acurácia de um critério não supervisionado com um rótulo
externo) não implica que o critério usou o rótulo. Releitura cuidadosa
dos Blocos 3–4: `diagnosis` nunca entra no cálculo de $\mathbf{S}$ nem
na decomposição espectral — só é usado depois, para colorir o gráfico e
medir a acurácia de um limiar sobre $z_1$. A separação de $92,1\%$ é um
achado genuíno: a variação biológica entre tumores benignos e
malignos domina boa parte da variância total dos $30$ atributos, e o
critério de máxima variância (cego ao rótulo) capturou essa estrutura
por coincidência estrutural, não por vazamento de informação.

O item (a) aponta o alicerce técnico por trás dos dois Teoremas
(Blocos 3 e 4): ambos dependem do Teorema Espectral (autovetores
ortogonais de matriz simétrica); se $\mathbf{S}$ não fosse simétrica, a
garantia de ortogonalidade desaparece, e a prova de equivalência das
duas formulações (que depende dessa ortogonalidade para o argumento de
Pitágoras do Bloco 4) deixaria de valer.

O item (b) testa se a equivalência das duas formulações vale só para
$M=1$ — não vale só para esse caso: o Teorema do Bloco 4 é geral,
provado por indução para qualquer $M<D$ (o argumento de Pitágoras soma
sobre todos os pontos e todas as direções retidas/descartadas, sem
restrição de $M=1$).

O item (c) é a confusão causal central da pausa: alta acurácia não é
evidência de que o rótulo foi usado no ajuste — é evidência de que a
estrutura não supervisionada (variância) e a estrutura supervisionada
(diagnóstico) coincidem nos dados, um achado sobre a biologia do
problema, não sobre a mecânica do algoritmo.

O item (d) generaliza essa mesma lógica para outro contexto de ML:
embeddings pré-treinados por auto-supervisão (otimizando um critério
sem rótulo, como reconstrução ou variância) frequentemente preservam
estrutura útil para classificação supervisionada depois — o mesmo
padrão "achado sem rótulo, útil para tarefa com rótulo depois" já
visto nas Aulas 3–4 (HDBSCAN, GMM) com o mesmo dataset.

- ✔ A prova de ambos os Teoremas depende do Teorema Espectral
  (autovetores ortogonais de matriz simétrica) — sem simetria de
  $\mathbf{S}$, o argumento de Lagrange não garante mais ortogonalidade
  entre os $\mathbf{u}_i$.
- ✗ O Teorema do Bloco 4 é geral para **qualquer** $M<D$, não só
  $M=1$ — as duas formulações concordam para todo $M$, prova por
  indução do Bloco 3 incluída.
- ✗ A PCA usou só os $30$ atributos — `diagnosis` só entrou depois, para
  **colorir** o gráfico e avaliar; a separação é um achado real, não um
  vazamento de rótulo.
- ✔ Exatamente o argumento por trás de embeddings auto-supervisionados:
  otimizar um critério sem rótulo (aqui, variância; noutros métodos,
  reconstrução ou contraste) pode preservar estrutura útil para
  classificação depois.

### Pausa 4 — Se a distribuição condicional da PPCA usasse covariância geral em vez de isotrópica, o limite σ²→0 ainda recuperaria a PCA do mesmo jeito?

Não do mesmo jeito — o argumento do Bloco 5 depende crucialmente de
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
contraditório) com o resultado do Bloco 5: no limite exato
$\sigma^2=0$ a densidade de $\mathbf{x}$ deixa de ter forma completa
(degenera sobre o subespaço, o mesmo fenômeno do item (a) do Exercício
3 sobre PPCA determinística), e é por isso que a demonstração do Bloco
5 trata $\sigma^2\to0$ como limite, nunca $\sigma^2=0$ exatamente.

O item (c) é uma falsa dicotomia sedutora: "modelo probabilístico" não
implica "sempre mais informativo" — o Bloco 5 provou exatamente o
oposto no caso-limite, que os dois métodos produzem o mesmo resultado
quando $\sigma^2\to0$.

O item (d) fecha a pausa situando a PPCA dentro de uma família mais
ampla: a mesma estrutura de variável latente linear-Gaussiana (prior
Gaussiano sobre $\mathbf{z}$, observação linear mais ruído Gaussiano) é
a base da Análise Fatorial, historicamente anterior à PPCA e usada em
psicometria — a PPCA é, na prática, um caso particular/restrito da
Análise Fatorial (ruído isotrópico em vez de ruído diagonal geral).

- ✔ Com $\boldsymbol\Sigma$ geral (não isotrópica), não há um único
  escalar de ruído a levar a zero — o argumento do limite (Bloco 5)
  perde a variável que precisa desaparecer; o modelo vira algo mais
  próximo de Análise Fatorial, com comportamento limite diferente.
- ✔ $\mathbf{WW}^T$ tem posto no máximo $M<D$ — no limite,
  $\mathbf{C}\to\mathbf{WW}^T$, singular por construção.
- ✗ Pelo contrário: o Bloco 5 mostrou que a PPCA **recupera exatamente**
  a PCA clássica no limite $\sigma^2\to0$ — "sempre mais informativa,
  nunca igual" contradiz esse resultado central.
- ✔ PRML observa essa conexão explicitamente — PPCA é um caso
  particular/restrito de Análise Fatorial, mesma estrutura de variável
  latente linear-Gaussiana.

### Pausa 5 — Se as unidades ocultas usassem ativação não linear, o mínimo global mudaria de subespaço?

Não, na arquitetura rasa — e essa é precisamente a ressalva que o DLFC
destaca (citada no Bloco 6): trocar só a ativação por uma função não
linear (por exemplo sigmoide), mantendo a mesma arquitetura
$D$-$M$-$D$ de uma única camada oculta, ainda leva o mínimo do erro de
reconstrução ao mesmo subespaço de PCA. A não linearidade, isoladamente,
não é o que falta — é a **profundidade** (camadas adicionais de
unidades não lineares) que permite escapar da limitação linear, o
assunto da Aula 7.

O item (a) é exatamente essa ressalva.

O item (b) usa o caso-limite $M=D$: sem gargalo real, qualquer base
completa do espaço de entrada permite reconstrução exata — mesmo
argumento já visto no caso $M=D$ da PCA clássica (Bloco 3) e reforçado
pelo item (a) do bloco de Exercícios sobre o autoencoder linear.

O item (c) é a falsa dicotomia mais sutil desta pausa: o Teorema
garante que o autoencoder encontra o mesmo **subespaço** ótimo (mesmo
erro mínimo), não que os pesos aprendidos formem a mesma **base
ortonormal** dos autovetores da PCA — a verificação numérica da aula
confirma isso diretamente (cossenos dos ângulos principais
$\approx0{,}98$/$0{,}93$, não exatamente $1$, mesmo com o erro de
reconstrução coincidindo a $5$ algarismos significativos).

O item (d) generaliza a técnica de prova usada no Bloco 6 (mostrar que
duas famílias de soluções alcançáveis coincidem, logo os mínimos dos
respectivos problemas de otimização coincidem) para outro contexto de
ML: o mesmo tipo de argumento de equivalência por redução aparece ao
comparar a solução de Ridge com $\lambda\to0$ contra mínimos quadrados
ordinários — dois problemas de otimização formalmente diferentes que,
no limite, convergem à mesma solução.

- ✔ Exatamente a ressalva do DLFC citada no bloco — arquitetura rasa,
  mesmo não linear, ainda encontra o mesmo subespaço de PCA; é preciso
  profundidade extra para escapar.
- ✔ Com $M=D$, qualquer base completa reconstrói exatamente (mesmo
  argumento do $M=D$ da PCA clássica, Bloco 3).
- ✗ O Teorema garante o mesmo **subespaço** (mesmo erro), não a mesma
  **base** — os pesos podem ser qualquer base desse subespaço, não
  precisando ser ortonormais (confirmado na verificação numérica).
- ✔ Mesma técnica de prova: mostrar equivalência de duas famílias de
  soluções alcançáveis (ou convergência no limite) para concluir que os
  mínimos coincidem — usada em vários contextos de otimização em ML.
