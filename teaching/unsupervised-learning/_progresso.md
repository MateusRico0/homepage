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

## Aulas 3–12

Não iniciadas.
