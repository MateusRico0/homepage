# Progresso — Unsupervised Learning

Estrutura conforme `CLAUDE.md`: `index.md` é o planejamento do semestre;
cada aula é `aulaNN/` com `00-plano-aula.md`, `01-fontes.md`, `02-aula.qmd`.
Fontes em `fontes/`: `prml.pdf`, `dlfc.pdf`, `esl.pdf` (mesmos links de
`supervised`), mais `exemplos-estilo/exemplo.qmd` (symlink para
`aula01/02-aula.qmd`).

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

## Aulas 3–12

Não iniciadas.
