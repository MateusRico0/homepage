## Resumo — Aula 2: Vector Spaces, KNN, and Kernel Density Estimation (KDE)

A Aula 1 fechou com uma aposta específica: assumir que os dados vêm de
uma Gaussiana multivariada, e uma ressalva anunciada mas não resolvida —
$\hat\Sigma$ só é invertível se $N > d$, e o próprio ajuste piora
conforme $d$ cresce. Esta aula puxa esse fio até o fim: por que espaços
de alta dimensão são geometricamente estranhos (maldição da
dimensionalidade e concentração de medida — a intuição de "distância" e
"vizinhança" formada em 2–3 dimensões falha), e o que fazer quando não
se quer mais assumir nenhuma forma paramétrica para $p(\mathbf{x})$. A
resposta é não-paramétrica: dois métodos-espelho constroem a mesma
estimativa geral $p(\mathbf{x}) = K/(NV)$ de direções opostas — fixar
$K$ e deixar o volume $V$ crescer até conter $K$ pontos ($k$-vizinhos-
mais-próximos) ou fixar $V$ e contar quantos pontos $K$ caem dentro
(KDE, culminando no kernel gaussiano suave). A aula fecha preparando o
terreno para a Aula 3: a distância ao $k$-ésimo vizinho,
$d_k(\mathbf{x})$, não serve só para estimar densidade — vira, ela
mesma, uma métrica de densidade local usável para construir grafos.

**Pré-requisitos:** Aula 1 (Gaussiana multivariada, estimação por
máxima verossimilhança de $\hat{\boldsymbol\mu}$ e $\hat\Sigma$, e a
observação de que $\hat\Sigma$ exige $N > d$ — o gancho direto para
esta aula). Álgebra linear básica (norma, produto interno) e
probabilidade básica (distribuição binomial, valor esperado).

**Objetivos de aprendizagem** (do `index.qmd`, Lesson 2):
- **ML Concept:** Busca de vizinhos mais próximos em alta dimensão
  (ANN) e estimação de densidade local.
- **Statistical Concept:** A maldição da dimensionalidade e
  concentração de medida (análise das métricas $L_1$, $L_2$ e Cosseno).
  O núcleo da aula: mostrar que a distância ao $k$-ésimo vizinho mais
  próximo, $d_k(\mathbf{x})$, é inversamente proporcional à densidade
  local ($p(\mathbf{x}) \propto 1/d_k(\mathbf{x})^d$). Transição desse
  contador rígido para KDE, em que a densidade é suavizada por uma
  função de peso gaussiana local.
- **Objectives:** Compreender o comportamento geométrico de espaços de
  alta dimensão e a estimação suave de densidade local.
- **Expected Competencies:** Avaliar métricas de distância em alta
  dimensão e implementar KDE para estimar a distribuição subjacente dos
  dados.

**Fonte principal desta aula:** Bishop, PRML (2006) — §1.4 "The Curse of
Dimensionality" (pp. 33–37) para a maldição/concentração de medida, e
§2.5 "Nonparametric Methods" (pp. 120–127), com as subseções 2.5.1
"Kernel density estimators" e 2.5.2 "Nearest-neighbour methods". Offset
do PDF confirmado nesta sessão: **+20** (mesmo valor já usado nas
Aulas 1 e nas fontes de `supervised-learning`) — página impressa 121 =
página 141 do PDF, verificado lendo diretamente.

**Ressalva de precisão, a resolver na Etapa 3 (fontes):** o PRML cobre
muito bem a maldição da dimensionalidade em geral (concentração de
volume numa casca fina da hiperesfera, e da massa de uma gaussiana em
alta dimensão) e os dois métodos não-paramétricos ($k$-NN e KDE) — mas
**não** cobre, pelo que localizei nesta sessão, uma comparação
explícita entre as métricas $L_1$, $L_2$ e Cosseno especificamente
citada no `index.qmd` desta disciplina. Isso é conteúdo padrão da
literatura de *approximate nearest neighbor search* (ANN), não do
PRML. Vou verificar DLFC e ESL na Etapa 3 antes de assumir que fica sem
citação de livro — se nenhum dos três cobrir, sinalizo explicitamente
como demonstração numérica nossa (mesmo tratamento já dado aos
resultados sem fonte da Aula 1, como a distribuição $\chi^2_d$ da
Mahalanobis).

**Dataset real (fio condutor):** proponho o **Breast Cancer Wisconsin**
(`scikit-learn/breast-cancer-wisconsin`, 569 amostras, 30 atributos
contínuos — já na tabela curada do `CLAUDE.md`), diferente do Pima
Indians Diabetes da Aula 1. Motivo da troca: o ponto central desta aula
precisa de uma dimensionalidade **variável e alta** (subamostrar
$d=2,5,10,20,30$ atributos para mostrar a concentração de medida
crescendo com $d$) — o Pima só tem 8 atributos, insuficiente para
mostrar o efeito com força. Mantém-se o domínio médico/diagnóstico, o
que permite uma transição natural do "isso daria uma boa 5ª (ou 6ª)
dimensão para o exemplo da Aula 1" caso queira comentar em aula. **Pauta
para sua aprovação:** ok trocar de dataset entre aulas por esse motivo,
ou prefere manter o Pima e aceitar um efeito de concentração mais fraco
na demonstração?

## Plano de aula — Aula 2 (carga horária: ~110–120min)

1.  **Abertura: o que fazer sem uma forma paramétrica, e sem $N \gg d$**
    (~10 min) — Retomar o fio deixado pela Aula 1: $\hat\Sigma$ exige
    $N > d$, e o ajuste piora conforme $d$ cresce mesmo quando $N > d$
    tecnicamente vale. Duas perguntas centrais de hoje: (1) por que
    exatamente "espaço de alta dimensão" é um problema geométrico, não
    só um problema de contagem de parâmetros; (2) se não quisermos mais
    assumir uma forma funcional (Gaussiana) para $p(\mathbf{x})$, como
    estimar densidade "deixando os dados falarem por si"?

2.  **A maldição da dimensionalidade, geometricamente** (~20 min) —
    PRML §1.4: o problema do histograma em $D$ dimensões ($M^D$
    células, crescimento exponencial, p. 121); o resultado central —
    fração do volume de uma hiperesfera entre $r=1-\epsilon$ e $r=1$
    tende a 1 quando $D\to\infty$ mesmo para $\epsilon$ pequeno (eq.
    1.75–1.76, pp. 36–37): em alta dimensão, quase todo o volume mora
    numa casca fina perto da superfície. Segundo exemplo: a massa de
    uma gaussiana em alta $D$ também se concentra numa casca fina, não
    perto da média (Fig. 1.23). **Consequência prática para métricas de
    distância** ($L_1$, $L_2$, Cosseno): à medida que $D$ cresce, a
    razão entre a distância mais próxima e a mais distante de um ponto
    de referência tende a 1 — "todo mundo fica igualmente longe de todo
    mundo". Demonstração numérica com o Breast Cancer Wisconsin,
    subamostrando $d=2,5,10,20,30$ atributos.

3.  **Da ideia geral ao estimador: $p(\mathbf{x}) = K/(NV)$** (~15 min)
    — PRML §2.5 intro (pp. 122–123): lições do histograma (localidade;
    o parâmetro de suavização não pode ser grande nem pequeno demais);
    o resultado geral — fixado um ponto $\mathbf{x}$ e uma região $R$
    pequena de volume $V$ ao redor dele, o número $K$ de pontos de
    treino que cai em $R$ segue $\mathrm{Bin}(K\mid N,P)$ com $P\approx
    p(\mathbf{x})V$, dando $p(\mathbf{x})\approx K/(NV)$ (eq. 2.246).
    Duas formas de explorar essa mesma identidade: fixar $K$ e
    encontrar $V$ nos dados ($k$-NN), ou fixar $V$ e contar $K$ (kernel/
    KDE).

4.  **$k$-vizinhos-mais-próximos para densidade** (~20 min) — Fixar $K$;
    crescer uma esfera centrada em $\mathbf{x}$ até conter exatamente
    $K$ pontos de treino; o raio dessa esfera é, por definição,
    $d_K(\mathbf{x})$ (PRML pp. 124–125). Como o volume de uma esfera de
    raio $r$ em $D$ dimensões escala como $r^D$ (mesma identidade do
    Bloco 2, eq. 1.75), $V \propto d_K(\mathbf{x})^D$, e substituindo em
    $p(\mathbf{x})=K/(NV)$:
    $$p(\mathbf{x}) \propto \frac{1}{d_K(\mathbf{x})^D}$$
    — o resultado central da aula, citado explicitamente no `index.qmd`
    da disciplina. Interpretação direta: ponto num bairro denso → $K$
    vizinhos estão próximos → $d_K$ pequeno → densidade estimada alta;
    ponto isolado → $d_K$ grande → densidade baixa. Efeito de $K$ como
    parâmetro de suavização (Fig. 2.26: $K$ pequeno = ruidoso, $K$
    grande = borra estrutura). Nota honesta (PRML p. 125): o modelo de
    $k$-NN não é uma densidade de verdade — a integral sobre todo o
    espaço diverge.

5.  **Do histograma ao kernel suave: KDE** (~20 min) — Caminho espelhado:
    fixar $V$ (um hipercubo de lado $h$ centrado em $\mathbf{x}$),
    contar $K$ via a função-janela de Parzen (eq. 2.247–2.249, p. 123).
    Problema do hipercubo: descontinuidades artificiais nas bordas — o
    mesmo problema do histograma. Solução: trocar a janela dura por um
    **kernel gaussiano** (eq. 2.250, p. 124) — cada ponto de treino
    "empresta" uma gaussiana de largura $h$, somadas e normalizadas.
    $h$ desempenha o mesmo papel de parâmetro de suavização que $K$
    desempenhava no Bloco 4 e $\Delta$ desempenhava no histograma (Fig.
    2.25: $h$ pequeno = ruidoso, $h$ grande = borra estrutura) — mesmo
    trade-off, três disfarces diferentes.

6.  **$k$-NN vs. KDE, lado a lado, no dado real** (~15–20 min) —
    Aplicar os dois métodos ao Breast Cancer Wisconsin (1–2 atributos
    mais informativos, para visualização), comparando: KDE tem largura
    de suavização **fixa** ($h$ igual em toda parte); $k$-NN tem largura
    de suavização **adaptativa** (o raio $d_K$ se ajusta à densidade
    local — encolhe onde há muitos pontos, cresce onde há poucos). Qual
    é mais robusto a regiões de densidade muito desigual? Conectar de
    volta ao Bloco 2: ambos os métodos, mesmo sendo não-paramétricos,
    ainda **sofrem** com a maldição da dimensionalidade — precisam de
    quantidade de dados que cresce descontroladamente com $d$ para
    continuar confiáveis (PRML p. 127, "these nonparametric methods are
    still severely limited"). Não-paramétrico não é "imune" à maldição
    — só falha de um jeito diferente do paramétrico.

7.  **Armadilhas, custo, e ponte para a Aula 3** (~10 min) — Custo
    computacional: os dois métodos exigem guardar **todo** o conjunto
    de treino e não têm fase de "treinamento" de verdade (PRML p. 127)
    — ao contrário do ajuste por máxima verossimilhança da Aula 1, que
    resume $N$ pontos em $\hat{\boldsymbol\mu}$ e $\hat\Sigma$. Ponte
    explícita: a distância ao $k$-ésimo vizinho, $d_K(\mathbf{x})$, que
    hoje serviu para estimar densidade, será reaproveitada na Aula 3
    como uma métrica de densidade local para construir caminhos num
    grafo (Clustering Hierárquico e HDBSCAN) — o mesmo número, um uso
    novo.

---

**Resolução dos pontos abertos (usuário sinalizou "continue", sem
objeção às propostas — seguindo com os defaults propostos):**

- Dataset trocado para Breast Cancer Wisconsin, confirmado carregável
  (569 amostras, 30 atributos contínuos + `id`/`Unnamed: 32` descartados,
  per a tabela do `CLAUDE.md`).
- **Achado importante na Etapa 3:** o ESL (Hastie, Tibshirani & Friedman)
  tem uma seção — **§2.5 "Local Methods in High Dimensions"** (pp.
  21–24 impressas, offset **+19** confirmado nesta sessão) — que cobre a
  maldição da dimensionalidade especificamente para métodos locais
  (k-NN), com resultados ainda mais concretos que o PRML: a fórmula do
  comprimento de aresta $e_p(r)=r^{1/p}$ (capturar 10% dos dados em
  $p=10$ exige cobrir 80% da amplitude de cada eixo — "vizinhanças não
  são mais locais"); a fórmula da distância mediana à origem
  $d(p,N)=(1-(1/2)^{1/N})^{1/p}$; e a densidade amostral $\propto
  N^{1/p}$. Isso complementa (não substitui) o PRML §1.4 — dois livros,
  duas óticas convergentes, ótimo para duplo registro. **O Bloco 2 foi
  enriquecido para usar os dois.**
- **L1/L2/Cosseno:** confirmado que nenhuma das três fontes do curso
  (PRML, ESL, DLFC) faz a comparação explícita das três métricas
  especificamente para maldição da dimensionalidade. Tratado como
  demonstração numérica nossa (medida de "contraste relativo",
  Aggarwal-style, $(\text{dist}_{\max}-\text{dist}_{\min})/\text{dist}_{\min}$),
  sinalizada como tal — mesmo tratamento já dado ao $\chi^2_d$ na Aula
  1. **Já verificada numericamente nesta sessão** no próprio Breast
  Cancer Wisconsin: contraste relativo médio cai de $\approx 221$ (d=2)
  para $\approx 28$ (d=5), $\approx 14$ (d=10), $\approx 11$ (d=20), e
  $\approx 10$ (d=30) — um colapso real e visualmente forte, verificado
  antes de escrever a aula.
- Ordem dos 7 blocos: mantida como proposto.

**Verificações numéricas já feitas nesta sessão (antes de escrever
`index.qmd`), para não inventar números na aula:**
- Contraste relativo por dimensão (acima).
- KDE gaussiano em `radius_mean` (univariado): $h=0.3$ → 12 picos
  espúrios (ruído); $h=1.0$ → 3 picos (captura a bimodalidade B/M sem
  ruído excessivo); $h=3.0$ → 1 pico só (borra a bimodalidade).
- Densidade por $k$-NN em `radius_mean`, três pontos-teste
  ($x_0=12,17{,}5,25$) e três $K$ ($5,20,50$): $d_K$ cresce muito mais
  rápido no ponto na cauda ($x_0=25$: $d_K$ de $1{,}49$ a $5{,}27$) do
  que no ponto denso ($x_0=12$: $d_K$ de $0{,}04$ a $0{,}29$) — a
  propriedade de suavização **adaptativa** do $k$-NN, usada no Bloco 6.
