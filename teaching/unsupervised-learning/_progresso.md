# Progresso — Unsupervised Learning

Estrutura conforme `CLAUDE.md`: `index.md` é o planejamento do semestre;
cada aula é `aulaNN/` com `00-plano-aula.md`, `01-fontes.md`, `02-aula.qmd`.
Fontes em `fontes/`: `prml.pdf`, `dlfc.pdf`, `esl.pdf` (mesmos links de
`supervised`), mais `exemplos-estilo/exemplo.qmd` (symlink para
`aula01/02-aula.qmd`).

## Dicionário de Notações

> Criado nesta sessão (2026-09-12/13), na Aula 5 — não existia antes,
> apesar de já ser exigido pelo `CLAUDE.md` desde a Aula 2. Backfill
> resumido das Aulas 1–4, seguido pelas adições de cada aula nova a
> partir daqui.

| Símbolo/termo | Significado | Introduzido em |
|---|---|---|
| $\hat{\boldsymbol\mu}$, $\hat\Sigma$ | Média e covariância amostrais (estimadores de máxima verossimilhança) | Aula 1 |
| $D_M(\mathbf{x})^2$ | Distância de Mahalanobis ao quadrado, $(\mathbf{x}-\hat{\boldsymbol\mu})^T\hat\Sigma^{-1}(\mathbf{x}-\hat{\boldsymbol\mu})$ | Aula 1 |
| $\chi^2_d$ | Distribuição de $D_M(\mathbf{x})^2$ sob o modelo ajustado; base do $p$-valor de anomalia | Aula 1 |
| $d_K(\mathbf{x})$ | Distância ao $K$-ésimo vizinho mais próximo | Aula 2 |
| $p(\mathbf{x})=K/(NV)$ | Estimador geral de densidade (fixa $K$ e acha $V$, ou vice-versa) — dá origem a $k$-NN e KDE | Aula 2 |
| $h$ | Parâmetro de suavização (largura de banda) do KDE | Aula 2 |
| $L_\lambda=\{\mathbf{x}:p(\mathbf{x})\ge\lambda\}$ | Conjunto de nível de densidade; cluster = componente conexa de $L_\lambda$ | Aula 3 |
| $d_{\mathrm{mreach}}(a,b)$ | Distância de alcançabilidade mútua, $\max(\mathrm{core}_K(a),\mathrm{core}_K(b),d(a,b))$ | Aula 3 |
| MST, persistência | Árvore Geradora Mínima; critério de robustez de um cluster na árvore condensada (HDBSCAN) | Aula 3 |
| $z_n$, $\pi_k$ | Variável latente categórica 1-de-$K$ (origem do ponto $n$); prior de mistura, $\sum_k\pi_k=1$ | Aula 4 |
| $\gamma(z_{nk})$ | Responsabilidade — $p(z_{nk}=1\mid\mathbf{x}_n,\theta)$, posterior via Bayes | Aula 4 |
| Passo E / Passo M | As duas etapas alternadas do Algoritmo EM | Aula 4 |
| $\mathbf{H}$ | **Reescrito em 2026-09-16** (versão anterior da Aula 5 usava $\mathbf{Z}$ genérico; a atual usa $\mathbf{H}$ propositalmente, para não colidir com $\mathbf{W}$ da PPCA, Aula 6, abaixo): variável não observada genérica na decomposição do ELBO — pode ser a variável latente $\mathbf{Z}$, o parâmetro $\theta$, ou os dois juntos | Aula 5 |
| $\mathrm{KL}(q\|p)$ | Divergência de Kullback-Leibler, $-\int q\ln\{p/q\}$; $\ge0$, não simétrica | Aula 5 |
| $\mathcal{L}(q)$, $\mathcal{L}(q,\theta)$ | ELBO (*Evidence Lower Bound*) — cota inferior de $\ln p(\mathbf{X})$ (ou $\ln p(\mathbf{X}\mid\theta)$), igual à evidência sse $q$ = posterior exata | Aula 5 |
| Decomposição $\ln p(\mathbf{X})=\mathcal{L}(q)+\mathrm{KL}(q\|p(\mathbf{H}\mid\mathbf{X}))$ | Identidade central da Aula 5, para qualquer $\mathbf{H}$ e $q(\mathbf{H})$ normalizada | Aula 5 |
| $q(\mathbf{Z},\theta)\approx q(\mathbf{Z})q(\theta)$ | Aproximação de campo médio (*mean field*) — fatoração usada para tornar o ELBO com $\theta$ dentro do tratamento variacional tratável | Aula 5 |
| $\alpha_0$ | Parâmetro de concentração da priori de Dirichlet sobre os pesos de mistura $\pi$ num GMM Bayesiano — menor $\alpha_0$ favorece poda automática de componentes supérfluos | Aula 5 |
| Inferência Bayesiana Variacional (*Variational Bayes*) | Procedimento que otimiza $q(\mathbf{Z})$ **e** $q(\theta)$ (com $\theta$ tendo uma priori $p(\theta)$) — diferente do EM clássico, que trata $\theta$ como ponto fixo, sem prior | Aula 5 |
| $s(i)$ | Coeficiente de Silhueta de um ponto (Rousseeuw, 1987): $\frac{b(i)-a(i)}{\max\{a(i),b(i)\}}\in[-1,1]$, maior é melhor | Aula 5 |
| $\mathrm{DB}$ | Índice de Davies-Bouldin (Davies & Bouldin, 1979): $\frac1K\sum_k\max_{j\ne k}R_{jk}$, $R_{jk}=\frac{\sigma_j+\sigma_k}{\|\mathbf{c}_j-\mathbf{c}_k\|}$; menor é melhor | Aula 5 |
| PPC (*Posterior Predictive Check*) | Amostrar $\theta$ aprendido, gerar $\mathbf{X}_{\text{sim}}$ do modelo generativo, comparar contra $\mathbf{X}_{\text{real}}$ — único teste desta aula que compara **forma**, não só um número agregado (Gelman & Rubin, 1996) | Aula 5 |
| $\mathbf{S}$ | Matriz de covariância amostral, $\frac1N\sum_n(\mathbf{x}_n-\bar{\mathbf{x}})(\mathbf{x}_n-\bar{\mathbf{x}})^T$ — simétrica e semidefinida positiva | Aula 6 |
| $\mathbf{u}_i$, subespaço principal | Autovetores de $\mathbf{S}$ associados aos $M$ maiores autovalores; direções/base da PCA | Aula 6 |
| $J$ | Distorção média de reconstrução da PCA, $\frac1N\sum_n\|\mathbf{x}_n-\tilde{\mathbf{x}}_n\|^2$ (mesma letra do $J$ de distorção do KMeans, Aula 4 — família de significado análoga, não coincidência de símbolo) | Aula 6 |
| $\mathbf{z}\in\mathbb{R}^M$ | **Atenção — reuso de símbolo:** variável latente **contínua** da PPCA (Gaussiana, $\mathcal{N}(\mathbf{0},\mathbf{I})$); não confundir com $z_n$/$z_{nk}$ da Aula 4, que é a variável latente **categórica** (1-de-$K$) do GMM, nem com o $\mathbf{H}$ genérico da Aula 5 | Aula 6 |
| $\mathbf{W}$, $\sigma^2$ | Parâmetros da PPCA: matriz de carregamento ($D\times M$) e variância do ruído isotrópico — **não confundir** com o $\mathbf{H}$ genérico da Aula 5 (renomeado de propósito para não colidir com este $\mathbf{W}$) | Aula 6 |
| $\mathbf{C}=\mathbf{WW}^T+\sigma^2\mathbf{I}$ | Covariância marginal de $\mathbf{x}$ no modelo PPCA | Aula 6 |
| $M$ (dimensão latente/subespaço) | Dimensão do subespaço/variável latente contínua da PPCA | Aula 6 |
| $\mathcal{M}_m$ | Estrutura/modelo candidato (ex.: "GMM com $K=m$"), tratado como variável na seleção Bayesiana de modelos | Aula 5.1 |
| $p(\mathbf{X}\mid\mathcal{M}_m)$ (evidência) | Verossimilhança marginal de $\mathcal{M}_m$, $\int p(\mathbf{X},\mathbf{H}\mid\mathcal{M}_m)\,\mathrm{d}\mathbf{H}$ — já embute Navalha de Occam antes de qualquer aproximação | Aula 5.1 |
| $\mathcal{L}_m(q)$ | ELBO da estrutura $\mathcal{M}_m$ — cota inferior tratável para a evidência, usada como *proxy* de ranqueamento | Aula 5.1 |
| $N_k$ | Contagem esperada de pontos no componente $k$ sob $q(\mathbf{Z})$, $\sum_n\gamma(z_{nk})$ — real, não necessariamente inteira | Aula 5.1 |
| Normal-Wishart, $\Lambda_k=\Sigma_k^{-1}$, $(m_0,\beta_0,W_0,\nu_0)$ | Priori conjugada sobre $(\mu_k,\Sigma_k)$ no GMM Bayesiano — impede analiticamente o colapso $\Sigma_k\to\mathbf{0}$, via $W_k^{-1}\succeq W_0^{-1}\succ0$ | Aula 5.1 |
| CAVI (*Coordinate Ascent Variational Inference*) | Resultado geral que otimiza um fator de $q$ por vez, $\ln q_j^\star=\mathbb{E}_{i\ne j}[\ln p(\mathbf{X},\mathbf{H})]+\text{const}$ (citado de PRML §10.1.1, não rederivado) | Aula 5.1 |
| ELPD (*Expected Log Predictive Density*) | $\mathbb{E}_{\mathbf{x}\sim p_{\text{true}}}[\ln p(\mathbf{x}\mid\mathbf{X}_{\text{train}})]$ — alvo estatístico verdadeiro da validação preditiva | Aula 5.1 |
| *Double-dipping* / viés de otimismo | Viés de estimar o ELPD usando os próprios dados de treino — reutilizar pontos de ajuste na avaliação | Aula 5.1 |
| Índice de Dunn | $\min$ distância inter-cluster / $\max$ diâmetro intra-cluster (Dunn, 1974) — geométrico, livre de distribuição, sensível a extremos | Aula 5.1 |
| PPC quantitativo, MMD, teste *sliced* | Checagem preditiva a posteriori com números: projeções aleatórias + KS (Massey, 1951) e *Maximum Mean Discrepancy* com kernel RBF (Gretton et al., 2012) | Aula 5.1 |

## Aula 1 — Data Space, Parametric Generative Models, and Anomalies

Construída do zero em sessão anterior — não havia nada além do `index.md`.
**Reavaliada em 2026-08-19** para se ajustar ao novo paradigma de aula do
`CLAUDE.md` (o mesmo aplicado às Aulas 1–3 de `supervised`): roteiro
explícito de 4 perguntas na abertura, 3 pausas ativas (pergunta-título
entre blocos), 3 testes V/F nos slides — cada um com slide de resposta
separado, verificado via extração de `<section id=...>` do `slides.html`
renderizado — e a seção de Exercícios nas notas HTML (3 discursivas + 12
blocos de V/F, 48 itens), cobrindo a aula de ponta a ponta. Conteúdo
técnico não mudou; só a estrutura pedagógica e os exercícios foram
adicionados. Revalidado com `quarto render --to html` e `--to revealjs`
(precisa ativar `../.venv` — mesmo detalhe de ambiente já registrado em
`supervised/progresso.md`).

- [x] `00-plano-aula.md` — 7 blocos, ~120 min. O Bloco 6 foi reescrito a
      partir do feedback do usuário: o rascunho original só definia um
      limiar fixo (dentro/fora); a versão final trata o escore de anomalia
      como um **$p$-valor** (via $\chi^2_d$ da distância de Mahalanobis), e
      contrasta a versão conjunta com a versão por-dimensão sob suposição
      de independência (combinada pelo teste de Fisher, $\chi^2_{2d}$) — o
      mesmo trade-off do Naive Bayes, agora em teste de hipótese.
- [x] `01-fontes.md` — 7 fontes do PRML (Gaussiana multivariada,
      Mahalanobis, MLE, viés do estimador de covariância, restrição a
      $\Sigma$ diagonal), todas com trecho literal extraído e offset
      confirmado (+20). **DLFC não localizado** para os tópicos desta aula
      dentro do esforço da sessão — fica pendente se algum dia quiser o
      par completo. Dois resultados centrais do Bloco 6 (distribuição
      qui-quadrado da distância de Mahalanobis; teste combinado de Fisher)
      **não têm citação de livro** — são estatística multivariada clássica,
      derivados e verificados na sessão, não copiados de fonte alguma.
- [x] `02-aula.qmd` — escrito nesta sessão. Núcleo: dois pontos construídos
      via decomposição espectral de $\hat\Sigma$ (B: 2 desvios ao longo do
      autovetor de maior variância; C: 3 desvios ao longo do de menor
      variância) para ilustrar o contraste pedido pelo usuário — **B**
      tem $p$-valor conjunto alto (0,135) mas seria um falso alarme pelo
      teste por dimensão (Fisher $p=0{,}019$); **C** tem $p$-valor conjunto
      baixo (0,011, anomalia real) mas passaria batido pelo teste por
      dimensão ($p=0{,}539$). Verificado com um script Python independente
      antes de confiar no render, não só no código do próprio `.qmd`. Um
      bug de renderização corrigido: `\boldsymbol` dentro de `ax.text()` do
      matplotlib não é suportado pelo mathtext (diferente do MathJax usado
      no resto do documento) — trocado por `\hat\mu` simples nesse ponto
      específico. Validado com `quarto render --to html` e `--to
      revealjs`, sem erro; 2 diagramas Mermaid presentes no HTML final.

**Dado sintético trocado por dado real em 2026-08-19** (aplicação da
diretriz "Dados: prefira exemplos reais a sintéticos" do `CLAUDE.md`): o
problema-fio da aula — antes dois sensores sintéticos de temperatura e
vibração — agora é **espessura da dobra cutânea vs. IMC**, dados reais
do **Pima Indians Diabetes Dataset** (`khoaguin/pima-indians-diabetes-database`
no Hugging Face Hub, 768 pacientes). Zeros em `SkinThickness`/`BMI` são
valores ausentes no dataset original (filtrados), assim como uma
paciente com `SkinThickness=99mm` (outlier fisiologicamente
improvável) — filtrada da população de ajuste ($N=538$), mas reciclada
no Bloco 7 como exemplo *real* de contaminação por outlier (infla
$\det\hat\Sigma$ em ${\sim}13\%$ sozinha). Os pontos didáticos B e C
continuam construídos via decomposição espectral (não há como garantir
que dois pacientes reais caiam exatamente nas direções dos autovetores)
— mas agora sobre a população real ajustada, não mais sintética;
verificado numericamente que o contraste pedagógico se mantém
intacto: $p_B=0{,}135$ (mas Fisher por dimensão $=0{,}032$, falso
alarme) e $p_C=0{,}011$ (mas Fisher por dimensão $=0{,}181$, escapa do
teste por dimensão). Bloco 7 também ganhou um segundo achado real: a
população se divide por diagnóstico de diabetes (não usado no ajuste)
em IMC médio $31{,}4$ vs. $35{,}9$, uma indicação honesta de
subestrutura que a Gaussiana única borra. Revalidado com `quarto
render --to html` e `--to revealjs`; confirmado que o aviso
"unauthenticated requests" do Hugging Face e a barra de progresso do
download não vazam para a saída renderizada (checado antes/depois de
suprimir com `hf_logging.set_verbosity_error()` +
`disable_progress_bar()`).

**Correção de padrão de slide em 2026-08-19**: as 2 pausas ativas e os
3 testes V/F desta aula usavam a pergunta/tema inteiro como título real
do slide, com a caixa `callout-tip` carregando só uma dica curta —
padrão errado. Corrigido para o padrão confirmado pelo usuário e
documentado no `CLAUDE.md`: título real do slide é o rótulo genérico
`Pergunta` (e `Resposta` no slide seguinte), com a pergunta/tema
específico como título do `callout-tip`, dentro da caixa. Revalidado
com `quarto render --to html` e `--to revealjs`; confirmado via
extração de `<section id=...>` do `slides.html` (5 slides `Pergunta` +
3 `Resposta`, sem heading duplicado ou solto).

**Ajustes de conteúdo em 2026-08-19** (pedidos pontuais do usuário,
depois da reavaliação de paradigma):

- **Diagrama Mermaid restante convertido para TikZ** (o fluxograma
  "supor independência entre dimensões?" no Bloco 6) — usava
  `{mermaid}`, único diagrama do arquivo que não tinha sido convertido
  ainda. Reescrito com nó de decisão (losango) e blocos retangulares,
  cores IC (`#0085CA`/`#FF5E00`/`#E03C31`), mesma convenção `.tikz` do
  outro diagrama já existente na aula. Confirmado no SVG gerado que as
  cores corretas foram aplicadas.
- **Derivação de $D_M(\mathbf{x})^2\sim\chi^2_d$ explicada com mais
  cuidado** (pedido explícito do usuário: "isso precisa ser explicado
  com mais carinho") — trocado o antigo one-liner ("verificação:
  Y=Σ^-1/2(X-μ)~N(0,I_d)...") por uma derivação completa em 3 passos
  (branqueamento $\mathbf{Y}=\Sigma^{-1/2}(\mathbf{X}-\boldsymbol\mu)$;
  mostrar $\mathbf{Y}\sim\mathcal{N}(0,I_d)$ via média/covariância;
  mostrar $\mathbf{Y}^T\mathbf{Y}=D_M(\mathbf{X})^2$), com intuição
  ("desfazer a elipse") antes do formalismo, e uma verificação numérica
  nova (simulação de 20.000 pontos de $\mathcal{N}(\hat\mu,\hat\Sigma)$,
  histograma vs. densidade teórica $\chi^2_d$) — testada isoladamente
  via script antes de incorporar. Versão RevealJS expandida em 3 slides
  (derivação, verificação, fórmula do $p$-valor) em vez de uma citação
  de uma linha.
- **Novo exemplo completo de detecção de anomalia, com dado real**
  (pedido explícito do usuário: faltava um exemplo claro mostrando a
  utilidade do que foi aprendido) — adicionado antes do contraste B/C:
  a paciente real do Pima com maior IMC do dataset ($46$mm/$67{,}1$
  kg/m², fora do filtro de outlier de $99$mm), com o pipeline completo
  aplicado passo a passo (modelo ajustado → $D_M^2\approx 29{,}85$ →
  $p\approx 3{,}3\times10^{-7}$), deliberadamente um caso **não
  ambíguo** (IMC já extremo isoladamente, percentil $99{,}8$), em
  contraste com a sutileza de B/C logo depois. Novo gráfico com a
  mesma convenção de elipses de contorno já usada na aula.

**Exemplo prático de descasamento de distribuição, com dado real**
(pedido explícito do usuário: faltava mostrar concretamente que "às
vezes a distribuição não casa e por isso dá errado", não só afirmar
isso em abstrato) — adicionado ao Bloco 7, estendendo o ponto de
multimodalidade já existente. Achado real, verificado por script antes
de escrever: a paciente diabética com a menor dobra cutânea de todo o
dataset ($7$mm) e IMC $27{,}6$ é flagrada como anômala ($p\approx
0{,}016$) sob um modelo ajustado só à subpopulação diabética, mas
**deixa de ser flagrada** ($p\approx 0{,}057$, acima do limiar de 5%)
sob o modelo *pooled* (população inteira) que a aula usa até ali —
mesma paciente, mesmos números, veredito oposto, só porque a população
de referência mudou. Novo gráfico de dois painéis (mesma paciente
marcada nos dois, contorno de 95% de cada modelo) deixa a diferença
visualmente óbvia. Adicionado tanto nas notas quanto num novo slide
RevealJS dedicado.

**Reorganização estrutural em 2026-08-19** (pedido explícito do
usuário: faltava clareza sobre por que se quer detectar anomalia nesta
aula, e o fim dos slides misturava "exemplo prático" com "fechamento
da aula"):

- **Nova seção dedicada, "Exemplo Prático: Detecção de Anomalia em
  Ação"**, criada entre o fim do Bloco 6 (teoria) e o Bloco 7
  (armadilhas/fechamento) — reúne os dois exemplos que antes estavam
  espalhados (um dentro do Bloco 6, outro dentro do Bloco 7) num único
  lugar, com título de slide próprio marcando claramente onde a "parte
  prática" começa e onde termina (antes do "Armadilhas e Ponte para a
  Aula 2", que agora fica só com o fechamento).
- **Motivação explícita adicionada** respondendo duas perguntas do
  usuário: (1) *por que* detectar anomalia aqui — não é diagnóstico (o
  rótulo nunca entra no ajuste), é controle de qualidade de dados e
  triagem de perfis atípicos para checagem manual; (2) a população
  usada no ajuste **não** é só de pessoas saudáveis — é uma coorte
  clínica geral, $359$ sem diabetes e $179$ com diabetes ($N=538$), o
  que já prepara o terreno para o exemplo de descasamento de
  distribuição logo a seguir.
- **Bug de ordem corrigido**: a versão RevealJS tinha os slides do
  "exemplo completo" ANTES dos slides da derivação do $\chi^2_d$,
  enquanto as notas HTML tinham a ordem oposta (derivação primeiro) —
  descoberto ao mapear a sequência de slides renderizados. Corrigido
  para a mesma ordem nos dois formatos.
- **Slide RevealJS que faltava**: a caixa "Armadilha de interpretação"
  (que um $p$-valor baixo não significa "prob. de vir da distribuição
  verdadeira") só existia nas notas HTML — nunca aparecia nos slides.
  Adicionado um slide dedicado para ela.

**Ajustes finos em 2026-08-19** (dúvidas do usuário sobre dois pontos
específicos, respondidas no chat e depois incorporadas ao `.qmd`):

- **Slide "Conjunta vs. por dimensão" dividido em 3** — estava
  acumulando o texto introdutório, o diagrama TikZ das duas rotas e o
  gráfico de barras do erro de B/C, tudo num único slide RevealJS (sem
  heading separando). Adicionados dois headings novos, compartilhados
  entre HTML e RevealJS — "Duas Rotas para o Mesmo $p$-valor" (antes do
  diagrama) e "Onde a Suposição de Independência Erra" (antes do
  gráfico de barras) — e uma explicação em fragmentos para o gráfico no
  RevealJS, que antes só existia nas notas HTML.
- **Conclusão do exemplo "Quando o modelo erra" (diabéticas vs. pooled)
  esclarecida** — o texto antigo descrevia os dois $p$-valores
  diferentes mas não dizia em qual confiar nem por quê. Adicionado um
  parágrafo (HTML) e um slide dedicado, "Qual dos Dois Confiar, e Por
  Quê?" (RevealJS): nenhum dos dois $p$-valores está errado
  aritmeticamente, mas o modelo *pooled* é a ferramenta errada aqui,
  porque borra duas subpopulações com composição corporal diferente
  numa única Gaussiana — e é por isso que uma anomalia real de
  subgrupo escapa.

## Etapa 5 — index.md

Link da Aula 1 adicionado (não existia nenhum antes — só texto em negrito
sem link): `../../unsupervised/aula01/notas.html` (+ Slides), mesmo padrão
das outras disciplinas. Mostrado no chat antes de aplicar.

## Aula 2 — Vizinhos Mais Próximos, Maldição da Dimensionalidade e KDE

Construída do zero nesta sessão (2026-08-25/26), a pedido do usuário
("Começe a criar a aula 2 não supervisionado ... pode criar o index
inclusive").

- [x] `_00-plano-aula.md` — 7 blocos, ~110–120 min. Continuidade direta
      com a Aula 1: o gancho de fechamento da Aula 1 ("$\hat\Sigma$
      exige $N>d$") é retomado na abertura. **Dataset trocado** de Pima
      Indians Diabetes (Aula 1) para **Breast Cancer Wisconsin**
      (30 atributos contínuos) — motivo explícito: a demonstração de
      concentração de medida precisa de dimensionalidade variável e
      alta, que os 8 atributos do Pima não sustentam.
- [x] `_01-fontes.md` — PRML §1.4 (maldição, offset +20, já usado nas
      Aulas anteriores) e §2.5 (KDE, $k$-NN, offset +20); **ESL
      (Hastie, Tibshirani & Friedman), §2.5 "Local Methods in High
      Dimensions" usado por primeira vez nesta disciplina** (offset
      **+19**, confirmado nesta sessão) — cobre a maldição
      especificamente para métodos locais, com fórmulas mais concretas
      que o PRML (comprimento de aresta $e_p(r)=r^{1/p}$; distância
      mediana ao vizinho mais próximo). L1/L2/Cosseno do `index.qmd` da
      disciplina não encontrado em nenhum dos 3 livros-texto (PRML, ESL,
      DLFC) — tratado como demonstração numérica nossa (métrica de
      "contraste relativo", estilo Beyer et al. 1999), sinalizada como
      tal, mesmo tratamento do $\chi^2_d$ da Aula 1.
- [x] `index.qmd` — todos os números centrais **verificados por script
      antes de escrever a aula** (não inventados): contraste relativo
      no Breast Cancer Wisconsin ($d=2\to30$: $\approx221\to\approx10$);
      picos de KDE gaussiano em `radius_mean` para $h=0{,}3/1{,}0/3{,}0$
      (12/3/1 picos); densidade por $k$-NN em 3 pontos-teste × 3 valores
      de $K$, mostrando a suavização adaptativa ($d_K$ cresce muito mais
      na cauda que na região densa). Bloco 6 revela, só ao final, que a
      bimodalidade encontrada sem rótulo corresponde à divisão
      benigno/maligno — mesmo padrão de "achado real, rótulo nunca usado
      no ajuste" já estabelecido na Aula 1 com o Pima.
      **Exercícios**: 3 discursivas + 12 blocos de V/F (48 itens) nas
      notas; 4 exercícios de checagem intercalados nos slides (um por
      bloco, Blocos 2, 4, 5, 6), cada um com slide de Resposta imediato
      — confirmado via extração de `id=` do `slides.html` renderizado
      (4 pares `pergunta-N`/`resposta-N`).
      **Bug de div encontrado e corrigido**: 3 dos 4 blocos de checagem
      nos slides tinham uma linha `:::` extra sobrando (fechamento
      duplicado) logo após o par abertura/`callout-tip`, um erro de
      digitação ao gerar o arquivo — sem efeito visual óbvio no render,
      mas quebrando o balanço de divs; corrigido removendo a linha
      solta nos 3 pontos, confirmado por script de balanço antes e
      depois de cada correção.
- [x] `_02-solucoes.md` — justificativa dos 48 itens, heurística nomeada
      por item. Um item foi reescrito no meio da sessão (bloco "$h$ como
      parâmetro de suavização", item a) por depender de um teorema
      (monotonicidade do número de modas do KDE gaussiano em função de
      $h$, Silverman 1981) nunca ensinado na aula — substituído por um
      caso-limite ($h\to0^+$) diretamente derivável do que foi
      apresentado.
- Validado com `quarto render --to html` e `--to revealjs` via
  `--output-dir` para diretório de teste (mesmo problema de path do
  pipeline normal já registrado em `computing-and-society/_progresso.md`)
  — 22 células Python executadas sem erro, sem warning de div, 10
  imagens geradas, 4 pares Pergunta/Resposta confirmados.
- [x] Etapa 5 — link da Aula 2 adicionado ao `index.qmd` da disciplina
  (`[**Lesson 2: ...**](./aula02/index.qmd)`, mesmo padrão da Aula 1),
  mostrado no chat e aplicado após aprovação do usuário.
- **Conformidade com a nova política de Estratégia Pedagógica
  (2026-08-26)**, a pedido do usuário ("veja como está a nova política
  de criação de aulas e refaça a estrutura"): `CLAUDE.md` passou a
  exigir a declaração explícita, no plano de aula, de qual das duas
  estratégias macro (A — Outside-In, para modelos/algoritmos; B —
  Inside-Out com Problema-Fio, para fundamentação matemática) a aula
  segue. `_00-plano-aula.md` atualizado com **Estratégia B**,
  justificada (o desafio de abertura é geométrico — maldição da
  dimensionalidade —, não um modelo prático chamativo), e um mapeamento
  explícito dos 7 blocos existentes às 4 fases da Estratégia B
  (Problema-Fio → Mecanismo → Diagnóstico → Ponte). Nesta rodada,
  **sem mudança de conteúdo no `index.qmd`** — só na rodada seguinte
  (abaixo).

## Reconstrução completa por nova revisão do `CLAUDE.md` (2026-08-26)

O usuário revisou `../CLAUDE.md` de forma mais profunda (não só a
Estratégia A/B) e pediu para refazer a Aula 2 inteira **sem consultar**,
para garantir aderência total. Mudanças da nova política, e como cada
uma foi aplicada:

- **Novo bloco obrigatório "Aula Simplificada"** (~10 min, entre
  Abertura e Desenvolvimento, "quando cabível" para Estratégia B) —
  adicionado como Bloco 2: duas metáforas sem matemática ("andar até
  achar $K$ casas" para $k$-NN; "somar o brilho de cada casa" para
  KDE), antes de qualquer geometria.
- **Pausa ativa ao final de todo bloco**, não mais um mínimo de 3
  espalhadas — agora **7 pausas ativas** (Abertura, Aula Simplificada,
  Maldição, $K/(NV)$ geral, $k$-NN, KDE, Comparação), cada uma com
  pergunta motivadora + dica + V/F de 4 itens.
- **Formato de V/F mudou de lettered (`a. ( )`) para checkbox**
  (`- [ ] Afirmação`) — aplicado em todas as pausas ativas e nos 12
  blocos de Exercícios. Confirmado no HTML renderizado:
  `<input type="checkbox">` gerado corretamente pelo Pandoc a partir da
  sintaxe de lista de tarefas do Markdown.
- **Slide de Resposta agora repete a pergunta motivadora ao final**
  (como fragmento de texto simples, não uma segunda caixa — a nova
  regra de "no máximo uma caixa por slide" não permite duas).
- **Nova seção "Respostas da Aula"** nas notas HTML, discutindo as 7
  perguntas motivadoras e dando a solução dos V/F de pausa ativa — os
  12 blocos de V/F do final (Exercícios) continuam sem solução no
  `index.qmd`, com justificativa só em `_02-solucoes.md`, como já era.
- **Chunks de código/TikZ compartilhados entre HTML e RevealJS, não
  mais duplicados** — cada figura agora é um único chunk fora dos
  blocos `content-visible quando`, gerado uma vez, visível nos dois
  formatos. Confirmado no render: **13 células executadas**, contra 22
  na versão anterior (quase metade, sem nenhuma duplicação de plot).
- **Caixas (`callout-*`) liberadas de volta** — a instrução anterior de
  "evite caixas" foi revertida pela nova política; só a regra de no
  máximo uma caixa por slide se aplica.
- **Formato do Exercícios mudou de `callout-tip` para `callout-note
  icon=false`**, mantendo o checkbox nos itens.
- Conteúdo técnico e números verificados (contraste relativo, picos de
  KDE, densidade por $k$-NN) **não mudaram** — só a estrutura/formato,
  seguindo exatamente a instrução do usuário de "refazer a estrutura".
- Revalidado com `quarto render --to html` e `--to revealjs` via
  `--output-dir`, sem erro nem warning de div; confirmado por extração
  de `id=` do `slides.html`: **7 pares `pergunta`/`resposta`** (antes
  eram 4); balanço de divs conferido por script antes e depois do
  render.
- `_02-solucoes.md` mantido sem alteração de conteúdo (os itens e suas
  justificativas continuam corretos — só o marcador visual no
  `index.qmd` mudou de letra para checkbox, o texto de cada afirmação é
  idêntico).

## Aula Simplificada reescrita (2026-08-26, mesma sessão)

Feedback direto do usuário: a primeira versão do Bloco 2 ("Aula
Simplificada") — duas metáforas em prosa ("bairro povoado"/"casa que
espalha brilho") — ficou **"muito ruim"**. O usuário revisou o
`../CLAUDE.md` de novo, detalhando o que essa etapa precisa ter: um
exemplo concreto ancorado no próprio algoritmo/aula (o `CLAUDE.md` cita
como referência a explicação de árvore de decisão: "vamos quebrar o
espaço recursivamente..."), **gráficos/diagramas de verdade**, e o
aluno devendo "praticamente entender o que vamos fazer" ao final do
bloco — não uma metáfora abstrata sem nenhuma imagem.

- **Bloco 2 reescrito do zero**, agora ancorado direto em
  `radius_mean` (o atributo real já usado no resto da aula), com duas
  ideias descritas em termos do próprio dado ("contar vizinhos por
  perto" / "somar contribuições de cada paciente") — nada de bairro ou
  casas.
- **Gráfico novo adicionado**: preview lado a lado de $k$-NN ($K=20$) e
  KDE ($h=1{,}0$) nos 569 pacientes reais, sem nenhuma fórmula no
  texto ao redor — o aluno já vê a forma final antes de qualquer
  equação, satisfazendo a exigência de "mostrar gráficos" e "já
  entender o que vamos fazer".
- Pausa ativa 2 reescrita para perguntar sobre esse gráfico
  específico ("por que as duas curvas concordam, vindo de contas
  diferentes"), em vez da pergunta genérica sobre metáforas.
- `_00-plano-aula.md` atualizado registrando explicitamente a rejeição
  da primeira versão e o motivo.
- Revalidado com `quarto render --to html` e `--to revealjs`: 14
  células executadas (1 a mais que a rodada anterior, pela nova
  figura), sem erro nem warning de div; 7 pares `pergunta`/`resposta`
  confirmados, 10 imagens no `slides.html` (1 a mais).

## Desenvolvimento matemático tornado "principled" (2026-08-26, mesma sessão)

Feedback do usuário: gostou da nova Aula Simplificada, mas pediu que a
**parte matemática** (Blocos 4–6: $K/(NV)$ geral, $k$-NN, KDE) fosse
"mais bem desenvolvida" — anunciar as premissas primeiro, depois
desenvolver passo a passo até a técnica final, em vez de apresentar o
resultado já pronto. O usuário também pediu para registrar essa
exigência no `../CLAUDE.md` (feito: novo bullet "Desenvolvimento
matemático *principled*" na seção Desenvolvimento).

- **Bloco 4 ($K/(NV)$ geral)**: reescrito com uma caixa explícita
  "Premissas desta derivação" (3 premissas numeradas: ponto+região+
  volume; $p(\mathbf{x})$ aprox. constante; $N$ pontos i.i.d.) seguida
  de 5 passos numerados até $p(\mathbf{x})=K/(NV)$, cada passo
  referenciando qual premissa o justifica. A tensão interna $V$
  pequeno/grande agora é apresentada como consequência direta das
  premissas (Premissa 2 vs. Passo 4), não como observação solta.
- **Bloco 5 ($k$-NN)**: mesma tratativa — 2 premissas (fixar $K$;
  $V$ vem dos dados) + 3 passos até $p(\mathbf{x})\propto
  1/d_K(\mathbf{x})^D$, citando explicitamente qual resultado anterior
  cada passo reaproveita (a escala $r^D$ do bloco da maldição da
  dimensionalidade; o $K/(NV)$ do bloco anterior).
- **Bloco 6 (KDE)**: mesma tratativa — 2 premissas (fixar $V=h^D$; $K$
  vem dos dados) + 4 passos (janela de Parzen → contar pontos →
  substituir em $K/(NV)$ → trocar o kernel duro pelo gaussiano),
  deixando explícito que a fórmula gaussiana final vem do **mesmo**
  Passo 3 (substituir em $K/(NV)$), só trocando a função de peso do
  Passo 1.
- **Correção lateral**: as referências antigas a "Bloco 2"/"Bloco 4"
  (números de bloco que ficaram desatualizados depois da reestruturação
  anterior, quando "Aula Simplificada" virou o Bloco 2) foram trocadas
  por referências descritivas ("o bloco da maldição da
  dimensionalidade", "o bloco anterior"), evitando nova referência
  frágil a numeração.
- Espelhado nos slides com a mesma estrutura (Premissas em caixa,
  passos como fragmentos numerados sequenciais).
- Revalidado com `quarto render --to html` e `--to revealjs`: 14
  células, sem erro nem warning de div; 7 slides `Pergunta` confirmados
  (nenhuma pausa ativa foi afetada pela reescrita — só o texto entre
  elas mudou).

## Respostas separadas do material + caixinhas não-clicáveis (2026-08-26, mesma sessão)

Duas peças de feedback do usuário: (1) a seção "Respostas da Aula"
estava dentro do `index.qmd` **publicado** — deveria estar separada;
(2) os itens de V/F usavam a sintaxe de lista de tarefas do Markdown
(`- [ ]`), que o Pandoc renderiza como `<input type="checkbox">`
**clicável** no navegador — indesejado; pediu também que a solução
mostrasse "o V ou o X estilizado nas caixinhas".

- **`# Respostas da Aula` removida do `index.qmd`**, movida para um
  arquivo novo e não publicado, `aulaNN/_03-respostas-pausas.md` (o
  `index.qmd` agora só contém a pergunta de cada pausa ativa, nunca a
  resolução).
- **Achado técnico real, documentado no `../CLAUDE.md`**: a extensão
  `task_lists` do Pandoc trata alguns glifos Unicode como sinônimos de
  `[ ]`/`[x]` **mesmo fora da sintaxe de colchetes** — testado
  isoladamente com `pandoc -f markdown -t html`: `☐` (U+2610) e `☒`
  (U+2612) viram `<input type="checkbox">` clicável só de aparecerem
  no início de um item de lista; `☑` (U+2611), por coincidência, não é
  tratado como especial. A primeira tentativa de correção (trocar `[ ]`
  por `☐`/`☑`/`☒`) **não resolveu o problema** — só descobri isso
  testando o HTML renderizado, não bastava trocar por "qualquer
  glifo de caixa".
- **Glifos confirmados seguros, usados em toda a aula**: `□` (U+25A1,
  quadrado vazio) para item não resolvido; `✔` (U+2714) para
  Verdadeiro; `✗` (U+2717) para Falso — nenhum dos três é especial
  para o Pandoc, testado e confirmado no HTML renderizado (0 ocorrências
  de `<input type="checkbox">` real, só uma regra CSS órfã e inofensiva
  para uma classe `task-list` que não existe mais no documento).
- Aplicado nos 76 itens de pergunta (7 pausas × 4 + 12 blocos de
  Exercícios × 4) e nos 28 itens resolvidos das 7 respostas de slide,
  mais os 48 itens de `_02-solucoes.md` (glifo escolhido
  programaticamente a partir do campo **Resposta** já existente de
  cada item, para não reintroduzir erro manual).
- Revalidado com `quarto render --to html` e `--to revealjs`: sem
  erro, sem warning de div, sem `<input type="checkbox">` real, 7 pares
  `pergunta`/`resposta` confirmados.

## Fase "Aula Simplificada" renomeada para "Intuição" (2026-08-26, mesma sessão)

Feedback do usuário: o nome da fase (e o título de seção resultante,
"Aula Simplificada — O Resultado Final, Antes da Matemática") ficou
"bem zoado". Depois de descartar alternativas específicas para esta
aula (o pedido era sobre o nome da **fase em geral**, para todas as
aulas), o usuário escolheu **"Intuição"** como novo nome da fase no
`../CLAUDE.md` (Abertura → Intuição → Desenvolvimento → Fechamento).

- `../CLAUDE.md` atualizado: "Aula Simplificada" → "Intuição" no nome
  da fase e na referência dentro do bullet "Desenvolvimento matemático
  *principled*".
- `index.qmd`: título da seção trocado para "Intuição — Contando e
  Somando Vizinhos" (título descritivo do conteúdo real do bloco —
  contar vizinhos por perto / somar contribuições —, não mais uma
  descrição genérica do papel pedagógico do bloco). Espelho em
  RevealJS ("## O Resultado Final, Antes da Matemática") também
  renomeado para "## Contando e Somando Vizinhos".
- `_00-plano-aula.md` atualizado com o novo nome, registrando o motivo
  da mudança.
- Revalidado com `quarto render --to html`, sem erro nem warning de
  div.

## Slides enriquecidos para paridade de detalhe com as notas (2026-08-26, mesma sessão)

Feedback do usuário: os slides desta aula estavam "muito
simplificados" — `radius_mean` era usado sem nunca ser explicado, e de
forma geral faltava informação para dar a aula só com o slide. Isso
motivou uma nova seção no `../CLAUDE.md` ("## Formato do arquivo de
aula") deixando explícito que o papel de HTML vs. RevealJS não é
"completo" vs. "resumido", é "corrido" vs. "itemizado" — quantidade de
informação quase igual — com um autoteste concreto ("se o aluno só
tivesse o slide, ele perderia algo que só está na prosa?").

Aplicado retroativamente nesta aula, bloco a bloco, comparando cada
slide RevealJS com o trecho HTML correspondente:

- **Intuição:** slide agora explica que `radius_mean` é "o raio médio
  do tumor medido no exame — um único número por paciente", antes
  ausente do slide (só nas notas).
- **Maldição da dimensionalidade:** adicionados ao RevealJS — a
  interpretação numérica do resultado $D=100$ (quase 100% do volume na
  casca) com a analogia à Gaussiana; a interpretação do resultado
  $p=30$ do ESL (93% da amplitude para capturar 10% dos dados); o elo
  conceitual antes ausente entre os dois resultados (casca + vizinho na
  borda) e a métrica de contraste relativo ("todo mundo fica a
  distâncias parecidas de todo mundo"); e a leitura do resultado
  numérico final (contraste caindo de ≈220 para ≈10 no próprio
  Breast Cancer Wisconsin).
- **$p(\mathbf{x})=K/(NV)$:** adicionado o slide "Duas Rotas, Não Duas
  Técnicas" (ausente do RevealJS; só existia nas notas) — $k$-NN e KDE
  não são "técnicas parecidas", são a mesma identidade explorada de
  dois lados opostos.
- **$k$-NN:** adicionada a citação literal de PRML (pp. 124–125) que
  faltava no slide, e um slide novo sobre a pista do *rug plot* (duas
  concentrações de pontos sugerindo `radius_mean` não-unimodal),
  ausente do RevealJS.
- **KDE:** adicionada a citação final de PRML (p. 124) sobre $h$ como
  parâmetro de suavização e o trade-off ruído/sobre-suavização, ausente
  do slide.
- **$k$-NN vs. KDE lado a lado:** adicionada a leitura interpretativa
  dos números de $d_K$ fixo-vs-adaptativo (antes só nas notas); e a
  explicação de que os tumores benignos têm `radius_mean` médio
  ≈12,1 e os malignos ≈17,5 — o que os 3 picos realmente são —, ausente
  do RevealJS.

Revalidado com `quarto render --to html` e `--to revealjs`: sem erro,
sem warning de div (`:::` balanceado), sem `<input type="checkbox">`
real, 7 pares `pergunta`/`resposta` confirmados intactos.

## Abertura reforçada: recapitulação da Aula 1 mais completa (2026-08-26, mesma sessão)

Feedback do usuário sobre o slide "Da Aula 1 Para Hoje": simplificado
demais — faltava resumir a Aula 1 de forma mais completa antes de
trazer a problemática desta aula. Também apontou que o slide "O Que Já
Dá Para Ver" (bloco Intuição) ficava "tosco" por vir depois do gráfico,
sem o gráfico por perto. Isso motivou uma nova regra geral no
`../CLAUDE.md`: nenhum slide pode ficar vazio/fino demais — ou tem
conteúdo suficiente para se sustentar sozinho, ou junta com o slide
vizinho.

- **Abertura:** recapitulação da Aula 1 reescrita, nas notas e nos
  slides, cobrindo o que antes só estava implícito ou faltava
  completamente: o problema de *profiling* sem rótulo, a fórmula do
  ajuste por máxima verossimilhança, a fórmula da distância de
  Mahalanobis e sua deformação geométrica, a conversão para $p$-valor
  via $\chi^2_d$, o contraste conjunta-vs-por-dimensão (Fisher), e as
  duas rachaduras já anunciadas no fechamento da Aula 1 (multimodalidade,
  outliers) antes de chegar na terceira rachadura ($N>d$) que abre esta
  aula. Nos slides, esse recap agora ocupa 2 slides cheios
  ("Da Aula 1: O Que Fizemos" e "Da Aula 1: Conjunta vs. Por Dimensão,
  e as Rachaduras") antes do slide-ponte original ("Da Aula 1 Para
  Hoje"), em vez de um único slide raso.
- **Intuição:** o slide "O Que Já Dá Para Ver" (texto puro, sem
  gráfico) foi fundido de volta no slide anterior que já contém o
  gráfico de $k$-NN/KDE — heading removido, conteúdo virou continuação
  em fragmentos do mesmo slide, para não separar imagem da leitura da
  imagem.
- `../CLAUDE.md`: nova regra sob "Formato do arquivo de aula" — nenhum
  slide pode ficar vazio ou fino demais; ou adicionar conteúdo, ou
  juntar com o slide vizinho; caso específico citado (gráfico num
  slide, comentário do gráfico isolado no seguinte) como padrão a
  evitar.

Revalidado com `quarto render --to html` e `--to revealjs`: sem erro,
sem warning de div, sem `<input type="checkbox">` real, 7 pares
`pergunta`/`resposta` confirmados intactos.

## Duas correções pontuais de conteúdo/didática (2026-08-26, mesma sessão)

**1. Exemplo das "3 bolas" corrigido para ser literal, não analogia.**
Feedback do usuário: o exemplo de volume-na-casca deveria ter sido
feito em $D=1$, $D=2$, $D=3$ — as únicas dimensões em que a geometria é
literalmente desenhável — em vez da versão anterior ($D=2,10,100$),
que usava uma área 2D como *proxy* visual para representar a fração de
volume em dimensões que não dá para desenhar de verdade. Reescrito:

- $D=1$: um segmento de reta (o "volume" é comprimento, escala com
  $r$) — barra horizontal com núcleo/casca por comprimento real.
- $D=2$: um disco de verdade (área, escala com $r^2$) — círculos
  concêntricos com raio geométrico real.
- $D=3$: uma esfera de verdade, renderizada em 3D
  (`ax.plot_surface`, projeção `3d` do matplotlib) — volume real,
  escala com $r^3$.

Em nenhum dos três painéis há truque de área-como-proxy: o raio do
núcleo é sempre o raio geométrico real $1-\epsilon$, e a fração de
"volume" (comprimento/área/volume, cada um na sua dimensão) sai
automaticamente correta por construção — sem precisar de nenhuma
analogia ou aviso de "isto não é literal". O texto que acompanhava o
exemplo (que dizia "em D=10/D=100 é uma analogia visual") foi reescrito
para deixar claro que as três bolas agora são exatas, e que o efeito
dramático da maldição da dimensionalidade só aparece de fato no cálculo
numérico já existente para $D=10,30,100$ (que continua logo depois,
sem mudança).

**2. Bloco "Contando e Somando Vizinhos" (Intuição) reestruturado para
ser mais algorítmico.** Feedback do usuário: a apresentação das duas
heurísticas podia ser mais explícita/passo-a-passo, e o gráfico de
densidade com seu significado deveria ficar num slide separado,
seguinte às heurísticas (não junto). Reescrito:

- **Heurística 1** mudou de "contar até juntar um número fixo de
  vizinhos" (que secretamente pré-anunciava $k$-NN) para "definir um
  raio fixo $r$ e contar quantos pacientes caem dentro da janela
  $[x-r,x+r]$" — mais literal/algorítmico, e alinhado com o que a
  Heurística 1 realmente vira depois: a **janela de Parzen** do Bloco 5
  (KDE), não o $k$-NN do Bloco 4. Adicionada função nova no chunk de
  setup, `radius_count_1d(x_eval, data, r)`, substituindo o uso de
  `knn_density_1d` nesse preview.
- **Heurística 2** manteve a ideia (peso que desconta com a distância),
  mas com explicação mais detalhada da aspereza que ela resolve (o
  corte abrupto dentro/fora da Heurística 1).
- Nos slides, o desafio + as duas heurísticas agora ocupam 3 slides
  cheios ("O Desafio", "Heurística 1: Contar Dentro de um Raio Fixo",
  "Heurística 2: Peso Descontado pela Distância") — só depois vem o
  slide com o gráfico de densidade, seu significado, e os desafios que
  ficam em aberto (estrutura que já existia, mantida como o "próximo
  slide").
- O texto de conexão com o resto da aula foi corrigido para refletir a
  nova mecânica: agora explicitamente liga Heurística 1 → janela de
  Parzen (KDE) e Heurística 2 → kernel gaussiano (KDE), com o $k$-NN
  reaparecendo como "a rota gêmea" que fixa a contagem em vez do raio —
  consistente com o fork Fixar-$K$-vs-Fixar-$V$ que o Bloco 3
  ($p(\mathbf{x})=K/(NV)$) já formaliza.

Revalidado com `quarto render --to html` e `--to revealjs` (a
renderização HTML falhou uma vez por corrida com o serviço
`homepage-preview.service`, que re-renderiza em segundo plano a cada
alteração do arquivo — não um erro de conteúdo; sucesso na segunda
tentativa): sem erro, sem warning de div, sem `<input
type="checkbox">` real, 7 pares `pergunta`/`resposta` confirmados
intactos.

## Três correções pontuais de clareza (2026-08-26, mesma sessão)

**1. Slide "O Mesmo Efeito, do Ponto de Vista de um Vizinho" — confuso,
tornado didático.** O slide era só a citação literal em inglês do ESL
($e_p(r)=r^{1/p}$) sem nenhuma explicação do que "vizinhança
hipercúbica" ou "comprimento de aresta" significam. Reescrito nas notas
e nos slides: explicado o setup (uma caixa de aresta $e$ que precisa
capturar uma fração $r$ dos dados), por que $e^p=r$ (mesma identidade
$r^D$ de volume do Bloco 2), e só depois a fórmula/citação — agora
**traduzida** (tradução nossa), corrigindo também uma citação que
estava em inglês direto no `index.qmd`, contra a regra do CLAUDE.md de
sempre traduzir trechos de fonte. *Nota: o restante do arquivo ainda
tem outras citações de PRML/ESL em inglês não traduzidas — não
mexidas nesta rodada, fora do pedido específico do usuário, mas
sinalizado como pendência futura.*

**2. "Premissas Desta Derivação" (bloco $p(\mathbf{x})=K/(NV)$) —
resumo muito raso, reescrito mais claro.** As 3 premissas (nas notas e
nos slides) diziam só *o quê*, sem *por quê*. Reescritas para explicar
o papel de cada premissa na derivação (ex.: a Premissa 2 existe porque
permite trocar uma integral por multiplicação no Passo 2; a Premissa 3
existe porque permite tratar a contagem como binomial no Passo 3).
Aplicada a mesma melhoria às "Premissas desta rota" do bloco de $k$-NN
(Bloco 4), por consistência de estilo.

**3. Passos 3 e 4 da derivação — explicados por completo.** Pedido
explícito do usuário: os passos "amostragem independente ⇒
$K\sim\mathrm{Bin}(N,P)$" e "$N$ grande ⇒ $K\simeq NP$" apareciam sem
nenhuma justificativa, só a conclusão. Adicionado, nas notas e nos
slides: o Passo 3 agora explica a analogia com uma moeda viciada
(cada um dos $N$ pontos "cai dentro de $R$" com probabilidade $P$,
independente dos demais — contar sucessos em tentativas independentes
com a mesma probabilidade é, por definição, uma binomial). O Passo 4
agora explica a concentração da binomial: média $NP$, desvio-padrão
$\sqrt{NP(1-P)}$, e o desvio *relativo* encolhendo como $1/\sqrt{N}$ —
por isso $K$ se aproxima de $NP$ para $N$ grande (mesma lógica de "1
milhão de moedas dá ~50% de caras").

Revalidado com `quarto render --to html` e `--to revealjs`: sem erro,
sem warning de div, sem `<input type="checkbox">` real, 7 pares
`pergunta`/`resposta` confirmados intactos.

## Bug crítico encontrado e corrigido: Exercícios da Aula 2 não apareciam no site (2026-08-28)

Feedback do usuário: os exercícios de nenhuma das duas aulas já dadas
apareciam no site. Investigação:

- **Aula 2 JÁ TINHA a seção de Exercícios no `index.qmd`** (48 itens de
  V/F + 3 discursivas), criada em rodada anterior desta sessão — mas
  ela nunca aparecia no `notas.html` publicado. Causa raiz: um `:::`
  de fechamento faltando, introduzido durante a reestruturação do
  bloco "$k$-NN vs. KDE" mais adiante nesta sessão (a fusão de um
  fragmento de slide com um heading dentro dele, sem fechar o bloco
  `::: {.content-visible when-format="revealjs"}` externo). O bug era
  **silencioso**: o Pandoc emite só um aviso ("Div ... unclosed...
  closing implicitly"), fecha implicitamente no fim do arquivo, e como
  o div não fechado era `when-format="revealjs"`, o filtro de
  `content-visible` escondia **todo o resto do arquivo** (incluindo a
  seção de Exercícios, que é `when-format="html"`) ao renderizar para
  HTML — sem gerar erro, só um aviso fácil de não notar entre dezenas
  de outros avisos de LaTeX/citação.
  - **Como foi encontrado:** meu próprio script de verificação de
    balanceamento de `:::` (usado em toda validação desta sessão) tinha
    um bug — permitia "casar" um fechamento com qualquer abertura de
    mesmo número de dois-pontos em qualquer posição da pilha, não só a
    mais recente (LIFO). Isso mascarava desbalanceamentos reais. Regra
    correta do Pandoc para divs indistintos por comprimento (todos
    usando exatamente 3 dois-pontos, como neste projeto): sempre LIFO —
    todo fechamento encerra o div mais recentemente aberto. Reescrito o
    script de verificação com essa regra; ele imediatamente apontou a
    linha exata do bug.
  - **Corrigido:** heading solto reintroduzido corretamente fora do
    fragmento, com o `:::` de fechamento do bloco externo restaurado.
    Revalidado com `quarto render --to html`, sem nenhum aviso de div,
    e confirmado que a seção de Exercícios agora aparece (76 glifos
    `□` no total: 48 dos exercícios + 28 das 7 pausas ativas × 4 itens
    — antes do fix, só os 28 das pausas apareciam).
  - **Lição para o futuro:** ao validar qualquer aula nesta sessão,
    sempre checar avisos de `[WARNING] Div ... unclosed` na saída do
    `quarto render` (não só o meu script de contagem), e sempre grep
    por conteúdo esperado no HTML final (ex.: `grep -c "Exerc"`), não
    só contar `:::`/checkboxes — um div mal fechado pode esconder
    seções inteiras sem gerar erro.

## Exercícios da Aula 1 criados do zero (2026-08-28)

A Aula 1 nunca teve seção de Exercícios — não fazia parte do arquivo
original. Criados, seguindo exatamente o mesmo padrão das demais aulas:

- **`index.qmd`:** seção "# Exercícios" (bloco `content-visible`
  exclusivo de HTML) com 3 questões discursivas (distribuição empírica
  vs. família teórica; geometria de Mahalanobis nos pontos B/C;
  aplicar os objetos matemáticos da aula a uma das duas rachaduras não
  resolvidas) e 12 blocos de V/F × 4 itens (48 itens), cobrindo a aula
  de ponta a ponta: profiling/distribuição empírica, geometria da
  Gaussiana multivariada, por que a Gaussiana (entropia máxima/TCL),
  ajuste por máxima verossimilhança, a armadilha $N\le d$, distância de
  Mahalanobis, geometria dos pontos B/C, do limiar ao $p$-valor,
  armadilha de interpretação do $p$-valor, conjunta vs. por dimensão,
  multimodalidade, outliers no ajuste/ponte para a Aula 2. Todos os
  itens nascem de uma das 4 heurísticas (contrafactual, limite,
  transferência de domínio, falsa dicotomia), usando sempre `□` como
  glifo (nunca `☐`/`☒`).
- **`_02-solucoes.md` criado do zero**, com heurística nomeada e
  justificativa analítica por item, mesmo formato padronizado das
  outras disciplinas.

Revalidado com `quarto render --to html` e `--to revealjs`: sem erro,
sem warning de div, sem `<input type="checkbox">` real, 48 glifos `□`
confirmados no HTML renderizado (0 pausas ativas nesta aula — não fazem
parte do escopo deste pedido, e a Aula 1 nunca teve essa estrutura).

## Aula 3 — Etapa 1–2 (2026-08-30)

Tema confirmado com o usuário: "Density Topography and Graphs:
Hierarchical Clustering and HDBSCAN" (Lesson 3 do `../index.qmd`).
`aula03/_00-plano-aula.md` criado — Estratégia A (Outside-In), carga
horária ~120min, 8 blocos (Abertura → Intuição com contraexemplo
sintético de duas luas/anéis → conjuntos de nível → alcançabilidade
mútua → MST/single-linkage → árvore condensada e persistência →
síntese → fechamento/ponte para GMM). Dataset-fio: Breast Cancer
Wisconsin (sem rótulos durante o clustering). Verificado nesta sessão:
`sklearn.cluster.HDBSCAN` disponível no kernel `sensibleml-moo`
(scikit-learn 1.8.0) — usar essa implementação, não o pacote `hdbscan`
externo (não instalado). **PARADO, aguardando aprovação do plano.**

## Aula 3 — Etapas 3–4 concluídas e validadas (2026-08-30)

Continuação da sessão anterior: `_01-fontes.md` e `index.qmd` já
tinham sido escritos por uma sessão interrompida antes da validação e
dos arquivos de apoio. Fechado nesta sessão:

- **Diagrama TikZ que faltava, adicionado.** O plano previa 3 diagramas
  (montanhas/conjuntos de nível no Bloco 3; construção da
  alcançabilidade mútua no Bloco 4; MST→árvore condensada no Bloco 6),
  mas só 2 existiam no `index.qmd` (`grep -c '{.tikz}'` = 2) — faltava o
  esqueleto abstrato do Bloco 3. Adicionado um diagrama novo (corte
  transversal 1D da "paisagem" de densidade, duas montanhas e um vale,
  com um limiar $\lambda$ e as duas componentes de $L_\lambda$
  destacadas), inserido antes da definição formal, seguindo o mesmo
  padrão de intercalação HTML/RevealJS/diagrama-compartilhado já usado
  nos outros dois. Contagem final: **3 diagramas TikZ**, confirmados no
  `slides.html` e no `notas.html` renderizados (3 SVGs em
  `index_files/mediabag/`).
- **Bug de TikZ pré-existente encontrado e corrigido**: o diagrama do
  Bloco 4 (alcançabilidade mútua) definia um estilo de nó chamado
  `out` (`out/.style={...}`, usado como `\node[out] (M) at (...)`) —
  `out` é uma chave reservada do TikZ (ângulo de saída de curvas
  Bézier), então o `pdflatex` falhava com `Package pgfkeys Error: The
  key '/tikz/out' requires a value`, ignorando o estilo (o nó
  compilava, mas sem a caixa/cor pretendida) e reportando erro no log,
  mesmo com o render geral "funcionando". Renomeado para `outbox` —
  confirmado sem erro no render depois da correção.
- **`_02-solucoes.md` criado do zero** — 48 itens (12 blocos × 4),
  heurística nomeada e justificativa analítica por item, no formato
  padrão do `../CLAUDE.md`. Texto de cada item extraído literalmente
  do `index.qmd` (não reinventado); V/F determinado por mim nesta
  sessão (as respostas não estavam em lugar nenhum, por design — só as
  8 pausas ativas já tinham "Resposta" no próprio `.qmd`, dentro do
  bloco RevealJS).
- **`_03-respostas-pausas.md` criado do zero** — as 8 pausas ativas
  (uma por bloco), discussão em prosa + resolução V/F com
  `✔`/`✗`, reaproveitando as respostas já escritas no `index.qmd`
  (dentro dos blocos `Resposta` exclusivos de RevealJS, nunca
  publicados nas notas HTML).
- **Validação por render completo**, usando o workaround de projeto
  isolado (`_quarto.yml` local com `project: {type: default}` +
  `filters: [diagram]`, e symlink `_extensions` local) para contornar o
  `FilesystemLoop` de `publications/mraimundo/` na raiz do projeto —
  ambos removidos ao final, junto com `notas.html`, `slides.html`,
  `.gitignore` e `.quarto/` que o render isolado deixou na pasta (só
  `_00-plano-aula.md`, `_01-fontes.md`, `_02-solucoes.md`,
  `_03-respostas-pausas.md`, `index.qmd` e `index_files/` — restrito a
  `figure-html/` e `mediabag/` — permanecem, mesmo padrão das Aulas
  1-2). Uma corrida com o `homepage-preview.service` (o mesmo problema
  já registrado na Aula 2) apagou um `notas.html` recém-gerado no meio
  da verificação; resolvido rodando os dois renders (`--to html` e
  `--to revealjs`) em sequência sem nenhuma edição de arquivo entre
  eles, evitando novo disparo do watcher.
  - `quarto render --to html` e `--to revealjs`: **ambos com exit
    code 0, sem nenhum `[WARNING]`/erro** (só ruído inofensivo de
    stderr do Inkscape na conversão PDF→SVG dos TikZ).
  - Balanço de `:::` (regra LIFO) limpo antes e depois de todas as
    edições.
  - `grep -n '☐\|☒\|- \[ \]\|- \[x\]'` sem nenhuma ocorrência em
    `index.qmd`, `_02-solucoes.md` e `_03-respostas-pausas.md`.
  - Exercícios confirmados no `notas.html` renderizado (não só no
    `.qmd` fonte) — 3 discursivas + 12 blocos de V/F (48 itens),
    80 glifos `□` no total (48 dos exercícios + 32 das 8 pausas
    ativas × 4), 0 `<input type="checkbox">` real.
  - 8 pares `id="pergunta"`/`id="resposta"` (mais `-1`...`-7`)
    confirmados no `slides.html`.
  - `output-file: notas.html`/`slides.html` confirmados no YAML.
- **Número real HDBSCAN-vs-diagnóstico, confirmado no `notas.html`
  renderizado** (não só no código-fonte): sobre os dois atributos
  `radius_worst`/`concave points_worst` do Breast Cancer Wisconsin,
  sem usar o rótulo — HDBSCAN encontra 2 clusters + 168/569
  ($\approx 29{,}5\%$) de ruído; Cluster 0 (54 pacientes) é 100%
  maligno; Cluster 1 (347 pacientes) é $\approx 90{,}8\%$ benigno (315
  benignos, 32 malignos); dos 212 malignos totais, 126
  ($\approx 59{,}4\%$) caem em ruído. ARI $=0{,}644$ excluindo ruído,
  $0{,}493$ incluindo ruído como rótulo próprio.
- `index.qmd` final: **2440 linhas**.

**Verificação independente (2026-08-30, sessão supervisora):** reconferi
tudo acima — balanço LIFO limpo, glifos limpos, 3 `{.tikz}`, estilo
`outbox` confirmado (não mais `out`), 80 `□` / 13 `callout-note
icon=false`. Rerenderei eu mesma (`--to html` depois `--to revealjs`)
usando o mesmo workaround de projeto isolado: peguei a mesma corrida com
o `homepage-preview.service` já registrada acima (`notas.html`
desapareceu entre um render e o outro) — confirmada de novo, mesma
causa, resolvida do mesmo jeito. `notas.html` renderizado mostra os
números reais do ARI ($0{,}644$/$0{,}493$) e a seção Exercícios
completa. **Limpeza adicional:** a pasta ainda tinha `index_files/libs/`
(artefato só do render isolado — nenhuma outra aula deste projeto tem
essa subpasta, porque o projeto real `type: website` centraliza esses
assets fora de `index_files/`) — removida. Diretório final de
`aula03/` bate exatamente com o conjunto de arquivos de toda outra
aula do projeto.

**Etapa 5 concluída (2026-08-30):** usuário aprovou ("pode seguir e
fechar"). Entrada da Lesson 3 no `../index.qmd` convertida de texto
simples para link: `*   [**Lesson 3: Density Topography and Graphs:
Hierarchical Clustering and HDBSCAN**](./aula03/index.qmd)`. Aula 3
encerrada.

## Aulas 7–12

Não iniciadas. (Aula 6 foi concluída na mesma sessão que fechou a Aula
5 — ver seção "Aula 6" ao final deste arquivo; esta nota de status foi
corrigida depois que a máquina rodando a sessão foi desligada no meio
da Etapa 5 da Aula 6, deixando temporariamente essa linha desatualizada.)

## Aula 4 — Modelos de Mistura Gaussiana e o Algoritmo EM

Construída sem aprovação por etapa (autorização explícita do usuário
para esta rodada). Fontes: PRML §9.1-9.3 (Bishop, 2006, pp. 424-444 —
mistura de gaussianas, variável latente, log-verossimilhança e a
necessidade do EM, o Passo E de responsabilidades posteriores, o Passo
M de atualizações ponderadas, KMeans como caso limite do GMM) e ESL
§8.5-8.5.1 (Hastie/Tibshirani/Friedman, 2009, pp. 272-274). Todos os
trechos citados literalmente em inglês no `_00-planejamento.md`, com
página (offset registrado explicitamente), e traduzidos no `index.qmd`.

**Dataset:** Breast Cancer Wisconsin (`scikit-learn/breast-cancer-wisconsin`),
mesmo par de atributos `radius_worst`/`concave points_worst` já usado
na Aula 3 — GMM ajustado nos mesmos dois atributos, sem usar o
diagnóstico, permitindo comparar diretamente a partição rígida do
HDBSCAN (Aula 3) contra a atribuição probabilística do GMM (esta
aula) na mesma figura/eixos.

**Conteúdo:** Revisão/Introdução → Intuição ("duas nuvens que se
tocam", motivando soft clustering como resposta ao limite do
HDBSCAN) → O Modelo de Mistura Gaussiana com variável latente →
Por Que Não Maximizar a Verossimilhança Direto (o argumento que motiva
o EM) → O Passo E (responsabilidades posteriores via Bayes) → O Passo
M (atualizações ponderadas por máxima verossimilhança) → O Algoritmo
EM Completo em Ação (worked example) → KMeans Como Caso Limite do GMM
(covariâncias esféricas idênticas, variância → 0) → Fechamento e Ponte
para a Aula 5.

**Pausas ativas:** 5 (Ruído do HDBSCAN vs. ambiguidade do GMM;
o que significa responsabilidade 50/50; responsabilidade muda com os
parâmetros; GMM completo é sempre melhor que o KMeans?; mais
componentes, mais verossimilhança? — esta última no fechamento).

**Exercícios:** 7 blocos de V/F de 4 itens (28 itens), todos originais
pelas 4 heurísticas exigidas, cobrindo partição rígida vs.
probabilística, a variável latente e a história geradora do GMM, a
log-verossimilhança e a necessidade do EM, o Passo E, e os demais
tópicos da aula.

**Achado de processo (retomada após limite de sessão):** o agente
atingiu o limite de sessão da conta (reset 16h America/Sao_Paulo) logo
antes/durante a escrita de `_01-respostas.md` — mas o arquivo já
estava completo (5 pausas + gabarito das 28 questões) quando retomei;
faltavam apenas a verificação final e os updates de `index.qmd`/
`_progresso.md` da disciplina, feitos por mim. Encontrei e corrigi um
bug real durante a verificação: um `label=f"...{,}5|<0{,}05$)"` — um
f-string do Python contendo chaves literais de notação decimal
brasileira (`{,}`) usadas para o LaTeX do matplotlib — o Python tentava
interpretar `{,}` como uma expressão de interpolação f-string
inválida, gerando `SyntaxError: f-string: expecting a valid expression
after '{'`. Corrigido separando a parte interpolada (`f"{ambig_mask.sum()}"`)
da parte literal com chaves LaTeX (`r"..."`), concatenadas com `+`.

**Validação (minha).** Checador de balanceamento de `:::`: zero
unclosed. `quarto render --to html` e `--to revealjs`: ambos "Output
created", sem erros. Contagem de glifos no `_site/`: `notas.html` — 48
`□` (28 exercícios + 20 pausas), 0 `✔`/`✗`; `slides.html` — 20 `□`
(pausas pré-resolução), 20 `✔`/`✗` (14 verdadeiros + 6 falsos). Único
`type="checkbox"` em cada HTML é a regra CSS genérica do tema, não um
checkbox real.

## Aula 5 — Seleção de Modelos, ELBO e Validação Empírica

**Reescrita completa em 2026-09-16**, substituindo do zero a versão
anterior (focada em BIC/aproximação de Laplace/prova de que o EM é
subida de coordenadas no ELBO — ver git history para essa versão). A
reescrita seguiu um roteiro de 5 blocos fornecido pelo usuário,
mapeado para `_00-planejamento.md` (Etapa 2) e aprovado antes da
montagem do `index.qmd`. Estratégia A (*Outside-In*): o eixo agora é um
framework de **decisão prática** — como calibrar e validar a estrutura
de um modelo não supervisionado sem rótulo de gabarito — não mais uma
fundamentação matemática autocontida em torno do BIC.

**Motivação da reescrita:** numa sessão anterior (documento
`_nota-variacional-e-selecao-de-modelos.md`, também desta pasta),
identificou-se e corrigiu-se um erro conceitual em uma explicação
informal sobre ELBO e seleção de modelos — a confusão entre "o ELBO que
o EM clássico calcula" (colapsa a $\ln p(\mathbf{X}\mid
\theta_{\mathrm{ML}})$, sem penalidade de complexidade) e "o ELBO que
de fato serve para seleção" (exige $\theta$ **dentro** do tratamento
variacional, com uma priori de verdade — Inferência Bayesiana
Variacional). Essa distinção corrigida virou o núcleo do Bloco 1 da
aula reescrita.

**Fontes:**

- PRML §1.6.1 "Relative entropy and mutual information" — definição da
  KL e prova de não-negatividade via Jensen (reaproveitada, mais
  enxuta, da versão anterior desta aula).
- PRML §9.4 "The EM Algorithm in General" — decomposição com $\theta$
  como parâmetro fixo (a especialização que devolve o EM clássico, sem
  prior).
- PRML §10.1–10.2 "Variational Inference" / GMM Variacional — base da
  decomposição com $\theta$ dentro do tratamento variacional (campo
  médio $q(\mathbf{Z},\theta)\approx q(\mathbf{Z})q(\theta)$) e da poda
  automática de componentes via priori de Dirichlet.
- Rousseeuw (1987) e Davies & Bouldin (1979) — Silhueta e Índice de
  Davies-Bouldin; citados por nome/ano (fórmula reproduzida
  diretamente), fora dos três livros-texto de `_fontes/`.
- Gelman & Rubin (1996) — conceito de *Posterior Predictive Check*,
  citado por nome/ano, explicado com palavras próprias (mesma
  observação de "fora de `_fontes/`" acima).

**Dataset:** Breast Cancer Wisconsin (`radius_worst`/`concave
points_worst`, mesmo par das Aulas 3–4) continua como problema-fio em
todos os blocos, com divisão treino ($N=398$)/validação ($N=171$,
$30\%$, `random_state=42`) introduzida nos Blocos 3–4. Contraexemplo
sintético deliberado (duas "luas", `make_moons`) usado só no Bloco 5,
para isolar a limitação de métricas agregadas de forma — não substitui
o dataset real como fio condutor.

**Conteúdo (8 blocos):** Revisão/Introdução (EM/GMM da Aula 4 sem
priori sobre $\theta$; reencena o teste "$K$ sempre sobe") → Intuição
(duas formas de pagar por complexidade: analítica vs. empírica) → Do EM
ao ELBO (KL/decomposição geral com $\mathbf{H}$ genérico; EM clássico =
$\mathbf{H}=\mathbf{Z}$, $\theta$ fixo, sem penalidade; alternativa =
$\mathbf{H}=(\mathbf{Z},\theta)$, campo médio, priori de verdade,
Navalha de Occam; demonstração de poda automática via
`BayesianGaussianMixture`) → O Dilema dos Hiperparâmetros ($\alpha_0$
vs. $K$ do K-Means vs. $\epsilon$/`min_samples` do DBSCAN, com diagrama
TikZ) → Validação Empírica em Clusterização Dura (Silhueta,
Davies-Bouldin, treino/validação) → Validação por Verossimilhança
(log-verossimilhança treino vs. validação, diagnóstico de sobreajuste,
mesma receita aplicada a comparar $\alpha_0$) → A Prova Final: PPC
(dados sintéticos vs. reais, contraexemplo das luas) → Síntese,
Fechamento e Ponte para a Aula 6 (mantida — mudança de eixo categórico
→ contínuo, ELBO volta na Aula 7/VAE).

**Números centrais** (computados por script Python independente antes
da montagem, reproduzidos no `.qmd`): log-verossimilhança de treino
(todos os dados) de $-1339{,}45$ ($K=1$) a $-1169{,}66$ ($K=10$),
monotônica. GMM Bayesiano ($K=8$ "de sobra"): $\alpha_0=0{,}001\to$
pesos $(0{,}6045,0{,}3955,0,\dots)$, 2 componentes; $\alpha_0=100\to4$
componentes com peso $>1\%$. Silhueta/Davies-Bouldin na validação
(K-Means): ambas ótimas em $K=2$ ($0{,}593$ / $0{,}590$). GMM treinado
só no treino: log-verossimilhança de validação máxima em $K=2$
($-361{,}95$), caindo depois — descolada da curva de treino
(monotônica). ELBO em validação por $\alpha_0$: $-366{,}57$
($\alpha_0=0{,}001$) vs. $-404{,}82$ ($\alpha_0=100$) — priori
concentrada generaliza melhor. PPC no problema-fio: médias/desvios
sintéticos batendo com os reais; PPC nas luas: GMM elíptico
($K=2$, log-verossimilhança $-684{,}75$) gera sintéticos que
extrapolam o arco real e preenchem a região côncava entre as luas.

**Pausas ativas:** 5, reescritas do zero (verossimilhança de treino e
singularidade; priori sobre $\mathbf{Z}$ vs. sobre $\theta$; métricas
de treino vs. validação em clusterização dura; o que o descolamento
treino/validação prova e o que não prova; por que boas métricas
agregadas não garantem forma correta) — discussão em prosa movida para
`_01-respostas.md` (reescrito).

**Exercícios:** reescritos do zero — 3 discursivas + 8 blocos de V/F de
4 itens (32 itens), cobrindo os 8 blocos de conteúdo da aula.

**Correção de notação:** a decomposição geral usa $\mathbf{H}$ (não
$\mathbf{Z}$ nem $\mathbf{W}$) para a variável não observada genérica —
$\mathbf{Z}$ ficaria ambíguo com a variável latente categórica
específica do GMM, e $\mathbf{W}$ colidiria com a matriz de carregamento
da PPCA (Aula 6). Ver dicionário de notações no topo deste arquivo.

**Validação.** Balanceamento de `:::` (regra LIFO): zero unclosed em
`index.qmd`/`exercicios.qmd`/`soluções.qmd`. Grep por `- [ ]`, `- [x]`,
`☐`, `☒`: zero ocorrências. `uv run quarto render` de cada um dos três
arquivos, individualmente (evitando o bug de multi-arquivo do
`preview-watch.py` corrigido em sessão anterior): sem erros, sem
`NotFound`/`Traceback`/`SyntaxError` no HTML renderizado. Contagem de
blocos: 8 `## Teste N` em `exercicios.qmd`, 8 pares
pergunta/resposta em `soluções.qmd` — correspondência 1 a 1 confirmada.

**Pendência para a Aula 6:** nenhuma pendência de conteúdo específica
desta reescrita além da mudança de eixo já anunciada na Ponte (variável
latente categórica → contínua). A Aula 6 (já escrita antes desta
reescrita, ver seção abaixo) não depende de nenhum resultado específico
do BIC que foi removido — só do ELBO/decomposição geral, que
permanece.

## Aula 5.1 — Modelos Variacionais, GMM Bayesiano e Seleção de Modelos

**Estado: aula completa criada do zero, em pasta nova `aula05_1/`,
2026-09-17.** Não é uma correção da Aula 5 — é uma **segunda versão**,
mais ambiciosa, do mesmo tema, criada a pedido explícito do usuário
("Essa aula 5 não ficou boa e criei um novo planejamento... Crie uma
nova aula, a aula 5.1 só para não apagarmos a atual. Pode criar tudo
sem a minha confirmação"), com um roteiro detalhado fornecido por ele.
A Aula 5 original (`aula05/`) foi mantida **intacta**, sem nenhuma
edição nesta sessão — as duas coexistem lado a lado no
`index.qmd` da disciplina.

**Diferença central em relação à Aula 5 original.** A Aula 5 original
dava priori de verdade só a $\pi$ (mantendo $\mu_k,\Sigma_k$ fixos,
como no EM clássico) — uma simplificação deliberada, pedida
explicitamente pelo usuário numa sessão anterior. A Aula 5.1 vai mais
longe: coloca $\mathbf{H}=(\mathbf{Z},\pi,\mu,\Sigma)$ **inteiro**
dentro do tratamento variacional, com priori Normal-Wishart em
$(\mu_k,\Sigma_k)$ além da Dirichlet em $\pi$ — o GMM Bayesiano
completo, tal como o `BayesianGaussianMixture` do scikit-learn de fato
implementa (a Aula 5 original já avisava, num callout, que a
implementação "vai além do que foi derivado"; a Aula 5.1 deriva essa
parte também). Consequência prática: em vez de variar $\alpha_0$ para
forçar poda (Aula 5 original), a Aula 5.1 fixa $\alpha_0=1$ (neutro)
e usa a **comparação do ELBO entre diferentes $K$'s** para decidir a
estrutura — um mecanismo de seleção diferente, mais próximo da prática
real de comparação de modelos Bayesianos.

**Estrutura:** Abertura (revisão da Aula 4 + Problema Motivador,
log-verossimilhança monótona em $K$) + 5 Blocos + Fechamento, ~135min
(aula estendida). Bloco 1 — seleção Bayesiana de modelos em geral
($p(\mathcal{M}_m\mid\mathbf{X})\propto p(\mathcal{M}_m)p(\mathbf{X}
\mid\mathcal{M}_m)$, evidência com Occam orgânico, KL/decomposição/
ELBO derivados do zero — autocontido, não depende da Aula 5 original).
Bloco 2 — priori Dirichlet sobre $\pi$ (com derivação curta e completa
de $q^\star(\pi)=\mathrm{Dir}(\alpha_0+N_1,\dots,\alpha_0+N_K)$ via
CAVI, citado mas não rederivado de PRML §10.1.1) e priori
Normal-Wishart sobre $(\mu_k,\Sigma_k)$ (mecanismo do não-colapso via
$W_k^{-1}\succeq W_0^{-1}\succ0$, citada de PRML §10.2.1, com a fórmula
exata verificável mesmo sem rederivar toda a álgebra variacional).
Bloco 3 — decomposição do ELBO completo (ajuste $-$ KL, especializando
a decomposição geral do Bloco 1), numérico: ELBO sobe até $K=2$ e cai
depois, ao contrário da log-verossimilhança clássica (monótona).
Bloco 4 — ELPD como alvo estatístico verdadeiro, *double-dipping*,
estimador de Monte Carlo via validação (com justificativa via Lei dos
Grandes Números); três razões para o ELBO de treino não bastar (folga
variacional, má especificação, comparação universal); Silhueta + Índice
de Dunn (novo nesta aula, Dunn 1974) na validação, com DBSCAN adaptado
via classificador $k$-NN (sem `predict` nativo do DBSCAN). Bloco 5 —
PPC quantitativo: projeções aleatórias + teste KS (Massey, 1951,
*sliced test*) e MMD com kernel RBF (Gretton et al., 2012) — o
contraexemplo das duas luas mostra que a largura de banda do kernel
decide que escala de discrepância o MMD enxerga (heurística da mediana
não rejeita; $4\times$ mais estreita, rejeita claramente).

**Números computados, não fabricados** (Breast Cancer Wisconsin,
`radius_worst`/`concave points_worst`, mesmos atributos das Aulas 3–5;
contraexemplo `make_moons`): log-verossimilhança clássica $K=1..10$,
$-1339{,}45$ a $-1169{,}66$ (monótona); ELBO Bayesiano ($\alpha_0=1$),
$-174\,522{,}02$ ($K=1$) até máximo $-105\,559{,}38$ em $K=2$, caindo a
$-123\,818{,}91$ ($K=10$); log-verossimilhança preditiva na validação
(clássica e Bayesiana), ambas com máximo em $K=2$; Silhueta na
validação máxima em $K=2$ ($0{,}593$) mas Dunn máximo em $K=5$
($0{,}0463$) — discordância real, deliberadamente mantida como ponto
pedagógico (não maquiada); DBSCAN adaptado via $k$-NN
($\epsilon=0{,}35$): Silhueta $0{,}4591$, Dunn $0{,}0618$; PPC:
problema-fio sem evidência de diferença (KS máx. $0{,}0738$, $0\%$
direções significativas; $\mathrm{MMD}^2\approx-0{,}0005$,
$p\approx0{,}565$), duas luas com diferença clara (KS máx. $0{,}1025$,
$55\%$ significativas; $\mathrm{MMD}^2=0{,}0032$, $p=0{,}005$ com
largura de banda $4\times$ mais estreita que a mediana).

**Arquivos criados:** `_00-planejamento.md`, `index.qmd` (~2275
linhas), `exercicios.qmd` (3 questões discursivas + 8 blocos `Teste N`
de V/F), `soluções.qmd` (gabarito dos 8 blocos), `_01-respostas.md`
(discussão das 6 Pausas Ativas — uma a mais que a Aula 5 original,
por ter 5 blocos de conteúdo em vez de 4). Todos verificados via
`uv run quarto render` individual (evitando o bug de corrida do
`preview-watch.py`), sem erros/`NotFound`/`Traceback`/`SyntaxError`.

**Citações fora do padrão usual da disciplina** (mesmo desvio já
registrado e aceito na Aula 5 original): Bishop, PRML (2006) §3.4,
§10.1, §10.2 (evidência, CAVI, GMM Bayesiano); Dunn (1974); Gretton et
al. (2012); Vehtari & Ojanen (2012); Massey (1951) — nenhuma tem PDF em
`_fontes/`, usadas por conhecimento consolidado, não por trecho
literal copiado.

**Pendência conhecida:** o `index.qmd` da disciplina foi atualizado
para listar a Aula 5.1 como entrada nova (ver seção "Etapa 5" abaixo,
se aplicável, ou o próprio `index.qmd`); a Aula 4 e a Aula 6 **não**
foram tocadas — seus links/pontes continuam apontando para a Aula 5
original, não para a 5.1. Isso é intencional por ora (a Aula 5.1
coexiste, não substitui), mas se um dia a Aula 5 original for
descontinuada em favor da 5.1, essas referências cruzadas precisarão
ser atualizadas.

## Aula 6 — O Mundo Linear: PCA, PPCA e Autoencoders Lineares

Construída sem aprovação por etapa (mesma autorização explícita do
usuário desta rodada, junto com a Aula 5). Estratégia B (*Inside-Out
com Problema-Fio*): a pergunta "que posição, em dimensão $M\ll D$,
resume este paciente sem perder o que importa?" atravessa as quatro
perspectivas do bloco central (geométrica, algébrica, probabilística,
neural) antes da síntese/limitação final.

**Fontes** (offsets PDF conferidos nesta sessão, comparando o cabeçalho
impresso de cada página; PRML símlink em `_fontes/prml.pdf`, offset
**+20**, já confirmado na Aula 5; DLFC símlink em `_fontes/dlfc.pdf`,
offset **+11**, conferido agora pela primeira vez — printed p. 565,
§19.1.1, bate com PDF p. 576, cabeçalho "19.1. Deterministic
Autoencoders"):

- PRML §12.1.1 "Maximum variance formulation", pp. 561–562 (PDF
  581–582) — dedução da PCA por máxima variância, restrição de Lagrange,
  Teorema Espectral.
- PRML §12.1.2 "Minimum-error formulation", pp. 563–565 (PDF 583–585) —
  dedução por erro mínimo de reconstrução, argumento de Pitágoras
  ligando as duas formulações.
- PRML §12.2 "Probabilistic PCA", pp. 570–577 (PDF 590–597), eq.
  12.31–12.50 — definição do modelo gerador da PPCA, solução de MLE
  (Tipping & Bishop, 1999), invariância rotacional, limite
  $\sigma^2\to0$.
- DLFC §19.1.1 "Autoencoders", p. 565 (PDF 576) — definição do
  autoencoder e o resultado (sem demonstração no livro) de que a
  ativação linear recupera o subespaço de PCA (Bourlard & Kamp, 1988;
  Baldi & Hornik, 1989); demonstração completa é original desta aula,
  por redução ao Teorema de erro mínimo (Bloco 4) — sinalizado
  explicitamente no texto como inferência própria, não do livro.

**Dataset:** Breast Cancer Wisconsin (`scikit-learn/breast-cancer-wisconsin`),
agora usando os **30 atributos completos** (não só o par 2D das Aulas
3–5) para o fio condutor probabilístico/algébrico; o par 2D
(`radius_worst`, `concave points_worst`) reaparece só para a ilustração
geométrica inicial do Bloco 2. Rótulo `diagnosis` nunca entra no
ajuste — só para avaliação posterior (acurácia de $92,1\%$ com um
único limiar no primeiro componente).

**Conteúdo:** Revisão/Introdução (fecha a Aula 5, troca variável
latente categórica → contínua) → Problema-Fio em 2D (duas direções
candidatas, variância como critério) → Mecanismo I: PCA por máxima
variância (Lagrange, equação de autovalores, Teorema + prova por
indução) → Mecanismo II: PCA por erro mínimo (distorção $J$,
mesma equação de autovalores por outro caminho, argumento de Pitágoras
provando a equivalência das duas formulações) → Diagnóstico Teórico:
PPCA (Definição do modelo gerador linear-Gaussiano, Teorema de MLE de
Tipping & Bishop, invariância rotacional, limite $\sigma^2\to0$
recuperando a PCA clássica) → Autoencoder Linear (Definição, Teorema de
Bourlard&Kamp/Baldi&Hornik, demonstração original por redução ao Bloco
4, verificação numérica) → Síntese (quatro ângulos do mesmo subespaço),
Fechamento e Ponte para a Aula 7 (Deep Autoencoder e VAE, ELBO da Aula
5 volta a ser necessário porque a posterior deixa de ter forma
fechada).

**Números centrais, verificados no próprio código do `.qmd`** (Breast
Cancer Wisconsin, $D=30$, `np.linalg.eigh` com reordenação explícita
para ordem descendente): $\lambda_1=13{,}2816$ ($44{,}27\%$ da
variância), $\lambda_2=5{,}6914$ ($18{,}97\%$) — $63{,}24\%$ acumulado
em $M=2$. Um único limiar no primeiro componente separa
benigno/maligno com $92{,}1\%$ de acurácia, sem nunca usar o rótulo no
ajuste. PPCA: $\sigma^2_{\mathrm{ML}}=0{,}39382$, confirmado igual à
média dos $28$ autovalores descartados; projeção da covariância
marginal $\mathbf{C}$ bate exatamente com $\lambda_1$ (direção retida) e
com $\sigma^2_{\mathrm{ML}}$ (direção descartada), como a eq. 12.36
prevê. Autoencoder linear (`MLPRegressor(activation="identity")`,
treinado por gradiente, nunca vendo a decomposição espectral): erro de
reconstrução $0{,}367575$ contra o ótimo teórico da PCA $0{,}367568$ —
coincidência a $5$ algarismos significativos; cossenos dos ângulos
principais entre os subespaços $\approx0{,}98$/$\approx0{,}93$ (próximo
de $1$, não exato — consistente com o Teorema, que não exige base
ortonormal alinhada, e explicado como efeito da convergência finita do
otimizador, não falha teórica).

**Pausas ativas:** 5 (mudança de variável latente categórica→contínua
muda o tipo de problema?; significado do multiplicador de Lagrange
$\lambda_1$; a acurácia de $92,1\%$ prova vazamento de rótulo?;
covariância geral em vez de isotrópica ainda recuperaria a PCA no
limite?; ativação não linear muda o subespaço do autoencoder raso?).

**Exercícios:** 3 discursivas + 6 blocos de V/F de 4 itens (24 itens),
cobrindo: formulação de máxima variância; formulação de erro mínimo e
equivalência; PPCA como modelo gerador; MLE da PPCA e o caso-limite
clássico; o autoencoder linear; síntese/limitações e ponte para a Aula
7. Densidade de V/F um pouco menor que a Aula 5 (24 vs. 28), calibrada
pela orientação do `CLAUDE.md` de não esticar por cota — a Aula 6 tem um
bloco central a menos (quatro mecanismos compactos em vez de cinco
blocos de conteúdo independentes).

**Dois diagramas TikZ**: modelo gerador da PPCA (variável latente
$\mathbf{z}_n$ contínua $\to$ observação $\mathbf{x}_n$, mesma
convenção de placa $N$ das Aulas 1 e 4, coordenadas absolutas); a
arquitetura do autoencoder ($D$-$M$-$D$, codificador/decodificador).
Ambos com margens generosas, sem rótulo tocando borda — confirmado por
inspeção visual do SVG renderizado.

**Validação.** Checador de balanceamento de `:::` (regra LIFO): zero
unclosed. `uv run python3 preview-watch.py --incremental`: render
incremental concluído, sem erro. Contagem de glifos no `_site/`:
`notas.html` — 6 `<img>` (3 figuras matplotlib + 2 diagramas TikZ + 1
figura de barras do autoencoder), 44 `□` (24 exercícios + 20 pausas), 0
`✔`/`✗`; único `type="checkbox"` é a regra CSS genérica do tema
(confirmado via `grep`, não é um `<input>` real). `slides.html` — 20
`□` (pausas pré-resolução) + 20 `✔`/`✗` (resolvidas). Contagens
conferem exatamente com o esperado (5 pausas × 4 itens = 20; 6 blocos
de exercícios × 4 itens = 24).

**Pendência para a Aula 7:** a Ponte já anuncia explicitamente as duas
direções que a Aula 7 precisa amarrar — (1) o Deep Autoencoder, que
finalmente escapa da limitação linear identificada no Fechamento desta
aula ao adicionar camadas de unidades não lineares (a ressalva do DLFC,
Bloco 6, já deixou claro que trocar só a ativação numa arquitetura rasa
não basta); e (2) o Variational Autoencoder (VAE), que generaliza a
PPCA desta aula ao caso em que $\mathbf{x}\mid\mathbf{z}$ deixa de ser
linear-Gaussiano — a posterior $p(\mathbf{z}\mid\mathbf{x})$ perde a
forma fechada que a PPCA teve (Bloco 5), obrigando a Aula 7 a reativar o
ELBO e a decomposição $\mathcal{L}(q)=\ln p(\mathbf{x})-\mathrm{KL}(q\|p)$
construídos na Aula 5, agora com $q$ aproximado por uma rede neural (o
*reparameterization trick*) em vez de calculado em forma fechada.

## Migração para exercicios.qmd/soluções.qmd públicos por aula (2026-09-14)

Concluída a migração desta disciplina para a convenção descrita em
`../CLAUDE.md` ("Exercícios (obrigatório em toda aula)"): a seção
Exercícios embutida no `index.qmd` de cada aula (HTML e RevealJS) saiu
de lá e passou a viver em dois arquivos-irmãos públicos por aula,
`aulaNN/exercicios.qmd` (questões, autocontidas — sem depender de
"nesta aula" ou de notação/exemplo só definido na aula) e
`aulaNN/soluções.qmd` (gabarito, agora público). O `index.qmd` de cada
aula perdeu a seção Exercícios e ganhou, perto do Fechamento (notas e
slides), um link `[Exercícios](exercicios.qmd){.see-all}
[Soluções](soluções.qmd){.see-all}`. Trabalho retomado nesta sessão
após uma tentativa anterior interrompida por um rate limit de API
(vários sub-agentes paralelos morreram no meio) — desta vez feito
sequencialmente, aula por aula, sem sub-agentes.

**Estado por aula, ao final desta sessão:**
- **Aula 1:** `exercicios.qmd`/`soluções.qmd` já existiam (10 blocos de
  V/F, 3 discursivas) e já corrigiam o problema original relatado por um
  aluno (o bloco "Os pontos B e C: geometria da crista" não fazia
  sentido fora da aula) — verificado e confirmado autocontido nesta
  sessão. Faltava só remover a seção Exercícios ainda embutida no
  `index.qmd` e adicionar o link de navegação; `_02-solucoes.md` (agora
  redundante) removido.
- **Aula 2:** migração completa do zero. `exercicios.qmd` novo (3
  discursivas + 12 blocos de V/F — acima da faixa de 6–10 do
  `CLAUDE.md`, mas preservando o conteúdo original já aprovado antes da
  migração, sem cortar questões) e `soluções.qmd` novo, a partir do
  gabarito de `_02-solucoes.md` (removido); reescrita para
  autocontenção removeu referências a "Bloco N"/"Aula N" (ex.: "o Bloco
  6 mostrou..." virou uma descrição direta do cenário, com o dataset
  Breast Cancer Wisconsin e a variável `radius_mean` glosados no
  preâmbulo). `index.qmd` da aula limpo, link adicionado.
- **Aula 3:** só faltava `soluções.qmd` (o `exercicios.qmd`, com 10
  blocos, já estava pronto e autocontido). Criado a partir do gabarito
  de `_02-solucoes.md` (removido), com a mesma limpeza de referências a
  "Bloco N"/"Aula N" nas justificativas. `index.qmd` limpo (a seção
  Exercícios embutida saía logo depois de um bloco de Pausa Ativa
  intercalado — cuidado extra para não remover a Pausa Ativa junto).
  `_04-explicacao-dmreach.md` preservado, sem relação com esta migração.
- **Aula 4:** `exercicios.qmd`/`soluções.qmd` e a limpeza do `index.qmd`
  já estavam prontos de uma sessão anterior. Verificado que
  `soluções.qmd` (7 blocos) supersede fielmente a Parte 2 (gabarito) de
  `_01-respostas.md` — mesmos números, mesma lógica, só sem as
  referências a "Bloco N"/"Aula N" — antes de remover essa parte;
  `_01-respostas.md` reduzido só à Parte 1 (Pausas Ativas).
- **Aula 5:** mesmo padrão da Aula 4: `soluções.qmd` (7 blocos, também
  já existente) verificado fiel antes de trimar `_01-respostas.md` para
  só Pausas Ativas. Corrigido, nesta sessão, um desvio de formatação
  encontrado em `soluções.qmd`: os títulos "Tema — item (x)" estavam em
  `##` (nível 2) em vez de `###` (nível 3, o padrão de
  `../CLAUDE.md`/das demais aulas) — corrigido para `###` em todos os 28
  itens. `index.qmd` da aula ainda tinha a seção Exercícios embutida
  (incluindo um parágrafo de metodologia solto antes de "Questões
  Discursivas") — removida, link de navegação adicionado em ambos os
  blocos HTML/RevealJS do Fechamento.
- **Aula 6:** migração completa do zero, convenção mais antiga (só
  `_00-planejamento.md`/`_01-respostas.md` misturando Pausas Ativas e
  gabarito de Exercícios). `exercicios.qmd` novo (3 discursivas + 6
  blocos de V/F, dentro da faixa 6–10) e `soluções.qmd` novo, extraídos
  da Parte 2 de `_01-respostas.md`; reescrita removeu referências a
  "Bloco N"/"Aula N" (ex.: comparações com o GMM passaram a nomear o
  método por extenso — "Modelo de Mistura Gaussiana (GMM)" — em vez de
  "o GMM da Aula 4"; o item de ponte para a Aula 7 ganhou a definição
  inline do ELBO para não depender de ter lido a Aula 5). `index.qmd`
  limpo, `_01-respostas.md` reduzido só à Parte 1 (Pausas Ativas).

**Limpeza em nível de disciplina:** removido `exercicios.qmd` da raiz da
disciplina — a página consolidada antiga (um só arquivo com as
Exercícios de todas as aulas, incluindo o próprio bloco "pontos B e C"
que motivou o relato original do aluno) que esta migração substitui;
removido o link `[Exercícios de todas as aulas]` do `index.qmd` da
disciplina.

**Verificação aplicada a toda aula tocada:** balanceamento de `:::`
(contagem LIFO, checado via script Python, zero não fechados em todos os
`index.qmd`/`exercicios.qmd`/`soluções.qmd`); grep por `- [ ]`, `- [x]`,
`☐`, `☒` (zero ocorrências em todos); comparação item a item entre o
texto de cada afirmação em `exercicios.qmd` e o campo **Afirmação** do
`soluções.qmd` correspondente (correspondência exata, a menos de
diferenças triviais de quebra de linha/espaçamento em LaTeX que não
afetam a renderização). Render via
`uv run python3 preview-watch.py --incremental` confirmado sem erros,
com `exercicios.html`/`soluções.html` publicados sob
`_site/teaching/unsupervised-learning/aulaNN/` para as 6 aulas.
