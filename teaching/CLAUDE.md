# Fluxo de trabalho — geração de aulas

Esta pasta (`teaching/`) contém MÚLTIPLAS disciplinas, cada uma em sua própria subpasta (ex.: `supervised-learning/`, `optimization-linear-algebra/`, `computing-and-society/`,
`unsupervised-learning/`). Este `CLAUDE.md` vale para todas elas.

Este projeto segue um processo de checkpoints POR AULA, com aprovação humana obrigatória em cada etapa. NUNCA pule uma etapa, NUNCA gere a etapa seguinte sem que o usuário tenha sinalizado aprovação explícita (ex: "pode seguir", "próxima etapa", "ok"). Após a etapa de planejamento, consulte o usuário se ele deseja já criar a aula direto (passando pelas etapas intermediárias) ou se deseja conferir as outras etapas.

O `index.qmd` de cada disciplina é a página pública do curso no site (lista de aulas, objetivos, competências esperadas) e também a referência de planejamento do semestre — use-o para identificar tema, objetivos de aprendizagem e a sequência das aulas. Não proponha alterações nele além de acrescentar/atualizar a entrada da aula em
questão, a não ser que explicitamente dito ou aprovado pelo usuário.

---

## Estrutura de pastas

```
teaching/
├── CLAUDE.md
├── lesson-theme.scss          # paleta azul/laranja/vermelho, só das aulas
├── logos-footer.html          # rodapé com os logos UNICAMP/IC nos slides
├── UNICAMP.png, IC.png
├── supervised-learning/
│   ├── index.qmd              # página pública do curso + planejamento
│   ├── _fontes/                # PDFs de referência (normalmente links simbólicos)
│   ├── _progresso.md           # registro de estado, não publicado
│   ├── aula01/
│   │   ├── index.qmd           # a aula em si (saída HTML + RevealJS)
│   │   ├── _00-plano-aula.md   # plano de aula, não publicado
│   │   └── _01-fontes.md       # fontes citadas, não publicado
│   ├── aula02/
│   └── ...
├── optimization-linear-algebra/
│   ├── index.qmd
│   ├── src/                   # módulo Python compartilhado entre aulas
│   ├── _fontes/
│   ├── _progresso.md
│   └── aula01/, aula02/, ...
└── ...
```

Cada disciplina é autocontida na sua subpasta. Cada aula é uma subpasta própria dentro da disciplina, nomeada `aulaNN` (`aula01`, `aula02`, ...).

**Por que os nomes com `_` na frente:** o Quarto ignora por convenção qualquer arquivo ou pasta cujo nome comece com `_` — nunca é renderizado nem copiado para o site publicado. `_fontes/`, `_progresso.md`, `_00-plano-aula.md` e `_01-fontes.md` usam esse prefixo de propósito: são material de apoio/planejamento (e, no caso de `_fontes/`, PDFs de livros com direitos autorais) que nunca deve aparecer no site ao vivo — só o `index.qmd` de cada aula (e o `index.qmd` da disciplina) é público.

---

## Etapa 0 — Identificar a disciplina (OBRIGATÓRIA, toda sessão)

Antes de ler, editar ou gerar qualquer arquivo, é preciso saber em qual subpasta de disciplina trabalhar nesta sessão.

- Se o usuário já declarou a disciplina na mensagem (ex: "Disciplina:   supervised-learning" ou "trabalhando em optimization-linear-algebra"), usar essa subpasta e confirmar em uma linha antes de prosseguir.
- Se não declarou e houver mais de uma subpasta de disciplina em `teaching/`, **perguntar qual é a disciplina da sessão** antes de   qualquer outra ação. Não adivinhar pela última disciplina usada em sessões anteriores — o estado pode ter mudado.
- Se o workspace aberto já é a subpasta de uma única disciplina, essa é   a disciplina — não perguntar.

Todos os caminhos de arquivo nas etapas abaixo (`index.qmd`, `_fontes/`, `aulaNN/`, `_progresso.md`) são relativos à subpasta da disciplina identificada nesta etapa, não à raiz `teaching/`.

---

## Estrutura da aula

### Estrutura macro (o "esqueleto" da aula)

Tendo em vista a natureza dos conteúdos do curso, a estrutura da aula deve seguir **uma de duas estratégias pedagogicamente fundamentadas**, a ser escolhida na **Etapa 1 (Plano de Aula)** de acordo com o tipo de objeto de estudo:
* **Estratégia A: *Outside-In* (Para Aulas de Modelos e Algoritmos)**
  *Uso:* Árvores de Decisão, SVM, Gradient Boosting, Regressão Logística, K-Means.
  *Lógica:* Guiada do prático para o formal: Modelo Mental/Catchy $\to$ Necessidade Teórica $\to$ Teoria Formal $\to$ Síntese e Limitações.
* **Estratégia B: *Inside-Out com Problema-Fio* (Para Aulas de Fundamentação Matemática/Linguagem)**
  *Uso:* Representações Matriciais, Derivadas/Gradiente, Espaços Vetoriais, SVD/Decomposição.
  *Lógica:* Guiada pela necessidade do idioma matemático: Problema-Fio da Engenharia/Geometria $\to$ Mecanismo/Operação $\to$ Diagnóstico Teórico $\to$ Ponte/Limitação para a próxima aula.

Ambas as abordagens devem manter os **3 movimentos fundamentais** (Abertura com problema/roteiro, Desenvolvimento segmentado em blocos de 10–15 min com pausas ativas onde tem perguntas e testes de V/F, e Fechamento retomando os desafios iniciais da aula):

**1. Abertura (5–10 min)** — o objetivo é criar o "gancho" cognitivo:
- **Organizador prévio** (Ausubel): Uma ideia-ponte que conecta o novo conteúdo ao que já se sabe. 
- **Revisão rápida**: Relembre parta da aula anterior para ajudar o aluno a lembrar.
- **Roteiro explícito**: dizer as 3–4 perguntas que a aula vai responder. Isso reduz carga cognitiva extrínseca porque o aluno para de gastar memória de trabalho tentando adivinhar para onde vai.
- **Problema motivador** discuta e provoque os alunos a pensar um pouco Isso vem antes do formalismo, não depois. 
- **Pausa ativa** veja abaixo.

**2. Intuição (10 min)** Quando possível, explique em linhas gerais o algoritmo/modelo, sem grandes complicações matemáticas (exemplo: em arvore de decisão dá para explicar que vamos quebrar o espaço recursivamente, e a cada quebra a informação resumida em cada bloco é mais explicativa do que antes), mostre gráficos, algoritmos, diagramas. O aluno deve praticamente entender o que vamos fazer, só vai faltar detalhes mais pesados. Isso deve ser aplicado quase sempre na **Estratégia A** e quando cabível, na **Estratégia B**.

**3. Desenvolvimento (segmentado)** — o ponto crítico: não é um bloco contínuo.
- **Segmentação em blocos de 10–15 min**, cada um com um único "ponto de aterrissagem". A atenção sustentada em exposição passiva degrada rapidamente; o corte periódico reinicia o ciclo.
- **Use sinalização verbal**: "isto é o resultado central", "esta hipótese é a que vamos relaxar depois". Marcadores explícitos de hierarquia evitam que tudo pareça igualmente importante.
- **Pausas ativa ao final do bloco**
- **Desenvolvimento matemático *principled***: uma vez passada a
  Intuição, o rigor sobe — não apresente a fórmula/técnica final já
  pronta. Primeiro **anuncie explicitamente as premissas/suposições**
  que vão ser assumidas (ex.: "vamos assumir que $p(\mathbf{x})$ é
  aproximadamente constante dentro de uma região pequena $R$"), depois
  **desenvolva passo a passo** como essas premissas levam à técnica
  final, deixando visível cada passo lógico/matemático do caminho — o
  aluno precisa conseguir seguir *como* se chega no resultado, não só
  receber o resultado e confiar nele.

**3. Fechamento (5 min)** — quase sempre o mais sacrificado e o mais valioso:
- Retomar as perguntas da abertura e responder cada uma em uma frase.
- Nomear explicitamente o que ficou em aberto e o que vem na próxima aula.

**Geral - Pausa Ativa (3 min)** - A pausa ativa visa fazer o aluno parar para refletir sobre o problema e confiar que entendeu o que veio antes. Pausas ativas ficam tanto nos slides quanto nas notas.
- **Pergunta Motivadora** faça uma pergunta provocara que provoque o aluno a pensar sobre o que discutimos, não só guardar, use essa estrutura:
  
  ::: {.callout-tip}
  ## Pergunta provocadora.

  Dica para ajudar a conduzir.
  :::
- **V/F condutor** crie perguntas de verdadeiro ou falso que validem o
  conteúdo anterior e ajudem o aluno a pensar mais profundamente na
  pergunta motivadora. **Não use a sintaxe de lista de tarefas do
  Markdown (`- [ ]`)** — o Pandoc renderiza isso como um `<input
  type="checkbox">` de verdade, clicável no navegador (feedback
  explícito do usuário: "isso não é bom").

  **Cuidado — nem todo glifo de caixa "parece seguro" realmente é.** A
  extensão `task_lists` do Pandoc trata alguns glifos Unicode como
  sinônimos de `[ ]`/`[x]` mesmo fora da sintaxe de colchetes, e os
  converte no mesmo `<input type="checkbox">` clicável — **`☐`
  (U+2610) e `☒` (U+2612) são especiais para o Pandoc e viram
  checkbox mesmo assim** (verificado testando `pandoc -f markdown -t
  html` isoladamente; `☑` U+2611, por outro lado, não é especial e
  fica como texto puro — mas é melhor não confiar nessa assimetria).
  Os glifos **confirmados seguros** (testados, permanecem texto puro)
  são:
  - `□` (U+25A1, quadrado vazio) para item ainda não resolvido;
  - `✔` (U+2714, marca de verificação) para item **Verdadeiro**;
  - `✗` (U+2717, X) para item **Falso**.

  Use `□` como texto simples no início de cada item:
  ::: {.callout-tip}
  ## Tema do V/F.

- □ Afirmação 1.
- □ Afirmação 2.
- □ Afirmação 3.
- □ Afirmação 4.

  :::
- **Resposta** nos slides crie um novo slide com resposta do V/F e
  depois coloque de novo a pergunta motivadora e espere a resposta do
  aluno. Na resposta, reescreva cada item trocando `□` pelo glifo
  resolvido: `✔` para item **Verdadeiro**, `✗` para item **Falso** — a
  caixinha "estilizada" já comunica o veredito, sem precisar do rótulo
  "Verdadeiro"/"Falso" por extenso ao lado (pode manter uma
  justificativa curta depois do glifo, se ajudar). Exemplo:

  ::: {.callout-tip}
  ## Tema do V/F — Resposta

- ✔ Afirmação 1 (verdadeira).
- ✗ Afirmação 2 (falsa) — breve razão.

  :::

  **Nas notas de aula, a resposta NÃO fica no `index.qmd` publicado.**
  Crie um arquivo novo e não publicado, `aulaNN/_03-respostas-pausas.md`
  (mesmo prefixo `_` dos demais arquivos de apoio — nunca deve aparecer
  no site), discutindo cada pergunta motivadora e dando a solução dos
  V/F com os mesmos glifos `✔`/`✗`. O `index.qmd` das notas só contém a
  pergunta em si (mesmo bloco `::: {.callout-tip}` usado no slide de
  Pergunta, sem duplicar), nunca a resolução.

### Técnicas de nível micro

| Técnica | Para que serve |
|---|---|
| **Exemplo resolvido (worked example)** antes de exercício | Reduz carga cognitiva em conteúdo novo; a ordem inversa só funciona com alunos já proficientes |
| **Contraexemplo deliberado** | Delimita a fronteira do conceito. "Onde este método falha?" ensina mais que três casos de sucesso |
| **Duplo registro** (intuição → formalismo → volta à intuição) | Evita que a derivação matemática se torne um fim em si |
| **Perguntas de diagnóstico** com alternativas plausíveis erradas | Revela concepções equivocadas; funciona melhor que "alguma dúvida?", que quase nunca produz resposta |
| **Princípio da redundância** (Mayer) | Não ler o slide em voz alta — texto e narração idênticos competem pelo mesmo canal. Slide com pouco texto + fala elaborando |
| **Explicitar a estrutura argumentativa** | "Vou fazer três suposições; a terceira é frágil e vou atacá-la no fim" |

---

## Formato do arquivo de aula

Cada aula é um **único arquivo `index.qmd`** dentro da sua pasta
`aulaNN/`, não um par separado de slides e notas. O mesmo arquivo
produz duas saídas (HTML e RevealJS) via blocos
`::: {.content-visible when-format="..."}`:

**O papel de cada saída não é "completo" vs. "resumido" — é "corrido"
vs. "itemizado", com quantidade de informação quase igual.** Feedback
explícito do usuário, depois de revisar slides "muito simplificados"
de uma aula cujas notas estavam boas: a diferença entre `notas.html` e
`slides.html` **não é de profundidade de conteúdo**, é de **forma de
organização**. Antes de aceitar uma versão de slide como pronta,
pergunte: "se um aluno só tivesse acesso a este slide (nunca às
notas), ele teria a mesma informação, só organizada de outro jeito —
ou ele perderia algo que só está na versão em prosa?" Se a resposta for
"perderia", o slide está simplificado demais.

- **HTML** (`unless-format="revealjs"`): prosa corrida, contando a
  aula como uma **história com detalhes** — com as provas/derivações
  por extenso, citações de página do livro, avisos de leitura e notas
  de rodapé pedagógicas. Sai como `notas.html` em TODA aula, sem
  exceção (ver "Nomes de arquivo de saída" abaixo) — o ícone de livro
  no rodapé dos slides (`../logos-footer.html`) linka direto pra
  `notas.html` como caminho relativo fixo, contando com esse nome ser
  sempre o mesmo.
- **RevealJS**: a **mesma história, quase o mesmo tanto de detalhe**,
  só que reorganizada em itens/fragmentos em vez de parágrafos corridos
  — nunca um resumo de tópicos. Os slides precisam sustentar a aula
  sozinhos em sala, não só sinalizar *highlights* ("só highlights é
  complicado para trabalhar", feedback explícito do usuário). Isso
  inclui coisas fáceis de esquecer de levar para o slide porque "já
  foram ditas na nota": **o que uma variável/coluna do dataset
  significa de verdade** (não só o nome da coluna — se as notas
  explicam que `radius_mean` é o raio médio do tumor medido no exame,
  o slide também precisa dizer isso, não só usar o nome da variável
  como se fosse autoexplicativo), o porquê de uma escolha, o
  contraste com o que veio antes. Usar bullets/fragmentos (`. . .`,
  `::: {.fragment}`) para revelar progressivamente e organizar uma
  ideia por slide, mas sem cortar explicações, derivações e nuances
  essenciais — o corte em relação à versão HTML é de ritmo e
  organização visual, não de profundidade de conteúdo. Conceitos
  não-triviais (ex: teoria kantiana, normas *prima facie*) precisam do
  mesmo cuidado explicativo nos slides que têm nas notas — não vale
  simplificar a ponto de distorcer. Sai como `slides.html`.

  **Use caixas para destacar informações (`callout-tip`/`note`/`important`/`warning`).**
  Mas não faz sentido ter mais de uma caixa por slide, 

  **Intercale HTML e RevealJS** Os blocos `content-visible` de HTML e de RevealJS devem ficar intercalados ao longo do arquivo, é importante fazer isso para evitar duplicidade de códigos python que vão ser rodados. Então se eu tenho um código python ou tikz no ponto C, a gente pode colocar A (nota/html), B(slide/revealjs), e C(plot/python/tikz) para evitar reprocessamento

  **Nenhum slide pode ficar vazio/esvaziado de conteúdo.** Um slide com
  só um título e uma frase curta (ou pior, um título e nada — texto que
  "sobrou" depois de um gráfico ter ficado no slide anterior) não
  sustenta um minuto de fala sozinho. Antes de aceitar um slide como
  pronto, pergunte: "isto ocupa o slide, ou está vazio demais?" Duas
  saídas, nunca "deixar assim": **(a)** falta conteúdo — adicionar mais
  explicação, outra citação, uma reafirmação com uma perspectiva nova
  — não só um enfeite; ou **(b)** o conteúdo é fino demais para
  justificar um slide próprio — juntar com o slide vizinho (anterior ou
  seguinte) em vez de espalhar pouca informação por muitos slides. Um
  caso comum desse problema: um gráfico/diagrama aparece sozinho num
  slide, e o slide seguinte só comenta esse gráfico em texto, sem o
  gráfico por perto — nesse caso, prefira manter o comentário no mesmo
  slide do gráfico (ou repetir/reduzir o gráfico ao lado do comentário)
  em vez de separar imagem e leitura da imagem em dois slides.

## Dados: prefira exemplos reais a sintéticos

As aulas têm ficado teóricas demais para quem está aprendendo Aprendizado de Máquina/Otimização pela primeira vez — sem um dado real e palpável por trás, a matemática fica abstrata demais. Ao escolher o dataset que ilustra o fio condutor de uma aula (o
"problema-fio" que atravessa os blocos), **prefira um dataset real a um dataset sintético**, e **prefira ambos a um dataset de brinquedo como Iris** — interessante para ensinar sintaxe, mas pouco palpável (poucos alunos têm intuição sobre pétalas de flor).

**De onde puxar o dataset: Hugging Face Hub, não pedir arquivo ao usuário a cada aula.** Em vez de esperar o usuário trazer um CSV para cada aula nova, use a lista curada abaixo — todos os itens foram testados com `datasets.load_dataset(repo_id)`, sem token/chave
(datasets públicos do Hub não exigem autenticação; só datasets *gated*/privados exigiriam, via `HF_TOKEN`, o que não é o caso de nenhum item desta lista). O kernel Jupyter usado nas aulas (`sensibleml-moo`) já tem `datasets` e `huggingface_hub` instalados. Ao carregar, aparece um aviso de "unauthenticated requests" — é só um
aviso de limite de taxa, não um bloqueio; pode ignorar.

| Dataset (repo Hugging Face) | Linhas | Uso recomendado | Observações |
|---|---|---|---|
| **Adult / Census Income** — `scikit-learn/adult-census-income` | 32.561 | Classificação binária (renda >50k), atributos mistos (contínuos + categóricos) — bom para Naive Bayes, árvores, regressão logística | Sem colunas problemáticas |
| **Breast Cancer Wisconsin** — `scikit-learn/breast-cancer-wisconsin` | 569 | Classificação binária médica (diagnóstico M/B), todos os atributos contínuos | Descartar `id` e `Unnamed: 32` (coluna vazia, artefato do CSV original) |
| **Pima Indians Diabetes** — `khoaguin/pima-indians-diabetes-database` | 768 | Médico, multivariado contínuo (Glicose, IMC, pressão, etc.), alvo binário — bom para Aula 1 de `supervised-learning` (Beta 1D, usando só `Glucose`) **e** Aula 1 de `unsupervised-learning` (Gaussiana multivariada/Mahalanobis, no lugar dos sensores sintéticos) | Coluna alvo já vem nomeada `y` |
| **California Housing** — `gvlassis/california_housing` | 20.640 (já dividido train/val/test) | Regressão — preço de imóvel a partir de 8 atributos contínuos; bom para regressão linear, regularização, e para `optimization-linear-algebra` (escalas bem diferentes entre atributos, motiva *feature scaling*) | Substitui o antigo Boston Housing (removido do scikit-learn por um problema ético numa variável) |
| **Default of Credit Card Clients (UCI)** — `Lancer73/uci-credit-card-default` | 30.000 (já dividido train/val/test) | Risco de crédito, classificação binária, atributos de histórico de pagamento — bom para árvores, ensembles | — |
| **German Credit Data (Statlog)** — `AiresPucrs/german-credit-data` | 1.000 | Risco de crédito, mistura explícita de categóricos (Sexo, Moradia, Propósito) e numéricos (Idade, Valor, Duração) — bom encaixe para Naive Bayes com atributos de tipos diferentes | Dataset pequeno, bom para uma aula que não quer um treino pesado |
| **Credit Card Transactions Fraud Detection** — `dazzle-nu/CIS435-CreditCardFraudDetection` | ~1.048.575 | Fraude/anomalia com atributos interpretáveis (valor, categoria, localização) — melhor para a lógica de detecção de anomalia da Aula 1 de `unsupervised-learning` do que o dataset clássico da ULB, cujos atributos são componentes de PCA anônimos, não interpretáveis | Grande: **subamostrar** para uso em aula; descartar colunas `Unnamed: 0`, `Unnamed: 23`, `6006` (artefatos); classe muito desbalanceada (avisar antes de usar) |

Isso não bane dados sintéticos por completo: eles seguem úteis para isolar um ponto matemático específico (ex.: um contraexemplo controlado, ou uma verificação numérica de uma propriedade, como o contraexemplo de Gini/entropia da Aula 3 de `supervised-learning`). Mas o **exemplo-fio** que atravessa os blocos de uma aula — o problema que dá contexto para tudo o resto — deve, sempre que possível, vir de um
dataset real, preferencialmente um da tabela acima.

**Como usar no `.qmd`:** carregar no bloco de setup global, junto com
os outros imports:

```python
from huggingface_hub.utils import logging as hf_logging
hf_logging.set_verbosity_error()  # evita o aviso "unauthenticated requests" vazando no chunk

from datasets import disable_progress_bar
disable_progress_bar()  # evita barra de progresso poluindo a saída do chunk

from datasets import load_dataset
ds = load_dataset("scikit-learn/adult-census-income")["train"].to_pandas()
```

Sem as duas primeiras linhas, tanto o aviso de "unauthenticated requests" quanto a barra de progresso do download vazam para a saída do chunk renderizado (mesmo com `echo: false`, que só esconde o código, não a saída/stderr) — com elas, a saída fica limpa.

O download é armazenado em cache local (`~/.cache/huggingface/`) — renderizações seguintes na mesma máquina não baixam de novo. Se, algum dia, um dataset novo (fora desta lista) for necessário, teste o `load_dataset(repo_id)` antes de incorporar à aula (confirmar que carrega sem token e checar as colunas), e considere adicionar à tabela
acima se for reutilizável em outras aulas.

## Citações e trechos de fontes: sempre traduzidos no `index.qmd`

Fontes bibliográficas em inglês (comum neste projeto) devem ter seus trechos **traduzidos para português** no `index.qmd` da aula — tanto nas notas quanto nos slides. Deixar a citação em inglês tem um custo alto de troca de idioma para quem lê ou apresenta em português (feedback explícito do usuário). Evite "copiar e colar" trechos dos livros.

- Em `_01-fontes.md`, o "Trecho" deve ser um overview dos conceitos, a   citação literal deve sempre ser traduzida para evitar travas de   direitos autorais — a intenção é ter um registro de verificação direta contra o PDF (Etapa 3, não mexer nisso).
- No `index.qmd` da aula, usar a tradução para português do trecho, deixando claro que é tradução nossa (ex.: "tradução livre"), não uma citação literal de outra fonte. Termos técnicos sem tradução direta e estável (ex.: *prima facie*, em latim) podem ficar no original, com uma explicação ao lado na primeira aparição.

**Nomes de arquivo de saída:** definir explicitamente no YAML do `index.qmd`, já que o padrão do Quarto usaria o nome do próprio arquivo (`index`) para ambos os formatos. **`output-file: notas.html` não é só convenção — é obrigatório**: o ícone de livro no rodapé dos slides (`../logos-footer.html`) linka pra `notas.html` como caminho relativo
fixo; uma aula sem esse `output-file` sairia como `index.html` e o ícone quebraria (404) nela.

```yaml
format:
  html:
    output-file: notas.html
  revealjs:
    output-file: slides.html
```

Além disso, cada aula soma o tema visual e as configurações compartilhadas de slide (footer, logos, dimensões) por cima — ver um `index.qmd` de aula já existente para o bloco `format:` completo, copiando-o em vez de reescrever do zero. **Essas configurações
compartilhadas vivem no front matter de CADA aula, não no `_quarto.yml` do projeto** — um `format: revealjs:` global já quebrou o build do site inteiro de forma silenciosa (nem toda página some do render, e o erro reportado não aponta pra causa real), então não promova essas configurações pro `_quarto.yml`, mesmo que pareça redundante repeti-las
em cada aula.

## Fluxogramas e diagramas

Ao montar o bloco, se o conteúdo tiver estrutura sequencial, uma árvore de decisão, um processo com ramificações, ou uma comparação de caminhos alternativos (ex: "três saídas honestas para um problema"), **proponha um diagrama TikZ** (` ```{.tikz} `), sem esperar o usuário pedir. O site já está configurado (`_quarto.yml` da raiz do projeto) com o filtro `pandoc-ext/diagram` e o *engine* TikZ (via `pdflatex`), renderizando nativamente nos dois formatos de saída (HTML e RevealJS). Use as cores preferenciais do IC (ver seção acima) nos elementos do diagrama quando fizer sentido. Só pergunte se não estiver claro que o diagrama ajuda mais do que texto.

**Não use `%%| fig-align: center` nem `%%| out-width: ...` num bloco `{.tikz}` — não têm efeito nenhum.** Verificado lendo o próprio filtro (`_extensions/pandoc-ext/diagram/diagram.lua`): `fig-align` só é aplicado quando a imagem tem legenda (`fig-cap`), e sem legenda o filtro devolve um `<img>` solto, sem nenhuma classe de alinhamento/tamanho. Para centralizar e/ou redimensionar um diagrama TikZ (ou qualquer figura de chunk Python que precise de um tamanho diferente do padrão da aula), ver "Redimensionar figuras e diagramas" abaixo.

### Redimensionar figuras e diagramas

**`out-width`, `fig-width` e `fig-height` (chunk options) não funcionam nas aulas.** Essas três são implementadas só pelo engine `knitr` (R) — confirmado no schema oficial do Quarto (`tags: {engine: knitr}` em cada uma) e testado ao vivo (valores diferentes de `out-width`/`fig-width` num chunk Python não mudavam o tamanho da imagem gerada). Como toda aula usa `jupyter: <kernel>`, essas opções são silenciosamente ignoradas — não proponha nem use nenhuma delas.

**Regra de para figuras e diagramas**: todo chunk Python que gera figura e todo bloco `{.tikz}` devem sair já envolvidos em `.fig-resize`, mesmo que o tamanho padrão (100%) sirva.

::: {.fig-resize style="width: 100%; margin: 0 auto;"}
```{python}
...
```
:::

## Exercícios (obrigatório em toda aula)

Toda aula precisa de exercícios — em dois formatos distintos, um por saída, que não devem ser confundidos entre si:

- **Notas (HTML):** terminar o arquivo com uma seção de **Exercícios** (dentro do bloco `content-visible` exclusivo de HTML), com **exatamente 3 questões discursivas/conceituais** e **12 questões de V/F** (não 12 itens — **12 blocos de 4 itens cada**, ou seja, 48 itens ao todo, cada bloco num tema diferente da aula, cobrindo o conteúdo da aula de ponta a ponta) — quotas fixas, por aula. Pode reaproveitar questões de fim de capítulo das próprias fontes bibliográficas (citando de onde vieram, como já se faz com trechos citados) ou propor questões originais — nesse caso, sinalizar que são originais, não da fonte. Ficam sem solução no arquivo (é trabalho para o aluno resolver por conta, fora da aula). Cada questão de V/F tem 4 itens do mesmo tema, e só é considerada correta se todos os 4 forem acertados (na avaliação, o aluno pode deixar a questão em branco com punição de 20% da nota da questão). Use esse formato:

::: {.callout-note icon=false}
## Tema das questões

- □ Afirmação 1.
- □ Afirmação 2.
- □ Afirmação 3.
- □ Afirmação 4.
:::

**Mesma regra do glifo não-clicável da Pausa Ativa se aplica aqui**:
nunca usar a sintaxe de lista de tarefas do Markdown (`- [ ]`), nem os
glifos `☐`/`☒` (ambos especiais para a extensão `task_lists` do
Pandoc, viram `<input type="checkbox">` clicável mesmo fora dos
colchetes) — usar sempre `□` (U+25A1) como texto simples.

- **Slides (RevealJS):** como indicado acima, esses exercícios devem ser contínuos sem passar mais de 15 sem um.

### Metodologia de criação de cada item de V/F (notas e slides)

**Objetivo:** cada item deve testar compreensão estrutural, capacidade de síntese e aplicação do conhecimento — não memorização rasa. Um aluno que decorou a aula sem entender a mecânica por trás dela deve errar; um aluno que entendeu deve acertar mesmo nunca tendo visto aquela frase exata antes.

**Toda afirmação precisa nascer de uma das heurísticas abaixo** (a lista não é exaustiva — o importante é a avaliação profunda, não a lista em si):

1. **Cenário contrafactual** — inverta uma premissa fundamental ou altere uma condição essencial do conceito, e afirme algo sobre a consequência lógica dessa alteração.
2. **Caso limite/extremo** — teste o comportamento do conceito num extremo absoluto (uma variável indo a infinito ou a zero, a ausência total de um fator limitante, $N\to\infty$, $\lambda\to 0$, etc.).
3. **Transferência de domínio** — descreva um cenário prático ou analítico que **não** apareceu na aula, e afirme que o conceito se aplica (ou falha) ali de um jeito específico.
4. **Falsa dicotomia/falsa equivalência** — construa uma afirmação que soe plausível por usar o jargão certo da aula, mas que erre a relação de causa e efeito de forma sutil e estrutural.

**Proibido:**
- Perguntas do tipo "o que é X" ou "X é definido como Y".
- Paráfrase literal de uma frase da aula.
- Afirmações cuja falsidade dependa só de trocar uma palavra (ex:
  "sempre" por "nunca", "positivo" por "negativo") sem alterar a
  mecânica do conceito por trás.

**Registro da justificativa — só para as notas, em arquivo separado.**As notas continuam saindo **sem solução no `index.qmd` publicado** (é trabalho do aluno resolver por conta — isso não muda). Mas a justificativa de cada item — por que é V ou F, apontando exatamente qual falha conceitual o aluno cometeria ao errar — deve ser escrita num
arquivo novo e não publicado, `aulaNN/_02-solucoes.md` (mesmo prefixo `_` dos demais arquivos de apoio, pelo mesmo motivo: nunca deve aparecer no site). Formato, por item:

```markdown
### [Tema do bloco] — item (a)

**Heurística:** Contrafactual | Limite | Transferência | Falsa dicotomia

**Afirmação:** ✔ (o texto exato do item, como aparece no `index.qmd` — ✔ se Verdadeiro, ✗ se Falso)

**Resposta:** Verdadeiro / Falso

**Justificativa:** [explicação analítica e direta de por que é V/F — sem meio-termo, apontando o erro conceitual específico que o aluno cometeria ao marcar a resposta errada]
```

O glifo (`✔`/`✗`) antes do texto da afirmação já comunica visualmente o
veredito, além do campo **Resposta** por extenso (redundância
proposital — o glifo para leitura rápida, o campo por extenso para
busca em texto). **Não use `☑`/`☒` aqui** — `☒` é um dos glifos
especiais do Pandoc (vira checkbox clicável mesmo em arquivos que não
são renderizados, por hábito/cópia-e-cola para um `index.qmd`).

Nos **slides**, a lógica de criação dos itens é a mesma (mesmas quatro heurísticas, mesmas proibições), mas **sem justificativa** — a resposta de cada V/F continua no slide imediatamente seguinte, só com o julgamento (V/F) de cada item marcado pelo glifo `✔`/`✗` (ver "Resposta" na seção da Pausa Ativa, acima); não é necessário nenhum arquivo extra para os slides.
---

## Para cada aula (repetir o ciclo)

### 1. Identificar a aula no planejamento
Consultar `index.qmd` da disciplina e confirmar com o usuário o tema,
objetivos e carga horária da aula NN. Não seguir sem confirmação.

### 2. Plano de aula (resumo + estrutura)
Gerar `aulaNN/_00-plano-aula.md`, contendo:

- **Resumo** (5-10 linhas): o que a aula cobre, objetivos de
  aprendizagem, pré-requisitos (conferindo com o que já foi dado nas
  aulas anteriores aprovadas).
- **Plano de aula**: sequência de blocos/tópicos na ordem em que serão
  apresentados, com tempo estimado por bloco (somando à carga horária
  da aula) e a lógica de transição entre eles (ex: "Bloco 1 termina
  com uma pergunta sem resposta, que o Bloco 2 resolve").
- **Estratégia Pedagógica Escolhida:** Indicar explicitamente se a aula seguirá a Estratégia A (Outside-In) ou Estratégia B (Inside-Out com Problema-Fio) e a justificativa em 1 linha (ex.: "Estratégia B por se tratar de aula de fundação matemática de representação/linguagem").

Formato:

```markdown
## Resumo — Aula N

[5-10 linhas: cobertura, objetivos, pré-requisitos]

**Estratégia Pedagógica:** [Estratégia A (Outside-In) OU Estratégia B (Inside-Out com Problema-Fio)] — [Justificativa em 1 linha]

## Plano de aula — Aula N (carga horária: XXmin)

1. **[Nome do bloco]** (~XX min) — [o que cobre, por que vem aqui]
2. **[Nome do bloco]** (~XX min) — [o que cobre, como conecta com o anterior]
...
```

**PARAR** e esperar aprovação/edição do usuário.

### 3. Fontes — com trecho citado literalmente
Gerar `aulaNN/_01-fontes.md` listando cada fonte usada, com:
- referência (livro, capítulo, seção, páginas);
- **o uso pretendido** daquele trecho na aula;
- **o trecho citado literalmente**, extraído do PDF/slide antigo,
  **na língua original da fonte** — nunca reescrito de memória, nunca
  paraphraseado, nunca traduzido nesta etapa, para que a checagem do
  usuário seja direta contra o PDF. A tradução para português (ver seção
  "Citações e trechos de fontes" acima) é feita depois, só no
  `index.qmd` da aula (Etapa 4).

Formato:

```markdown
## Fontes usadas — Aula N

### Fonte 1: PRML, §1.5.1, pp. 39-41
**Uso pretendido:** prova de que o cruzamento das conjuntas minimiza
o erro esperado.

**Trecho:**
> "the smallest probability of misclassification is achieved if
> each value of x is assigned to the class for which the joint
> probability p(x, Ck) is largest..."

---

### Fonte 2: DLFC, §2.1.1, pp. 25-26
**Uso pretendido:** exemplo de triagem médica (Bayes discreto).

**Trecho:**
> [trecho copiado literalmente do PDF]
```

**Fontes como link simbólico:** os arquivos em `_fontes/` podem ser
links simbólicos apontando para os PDFs/slides originais em outro
lugar do disco (ex: `ln -s ../../../livros/prml.pdf _fontes/prml.pdf`).
Leia-os normalmente pelo caminho dentro de `_fontes/` — não há
tratamento especial necessário. Prefira links relativos, para o
projeto continuar funcionando se a pasta for movida. **Nunca copie o
PDF de verdade para dentro do projeto** — o prefixo `_` só garante que
o Quarto ignore a pasta; um link simbólico garante também que o
arquivo de direitos autorais nunca é versionado como blob do git.

**PARAR** e esperar aprovação/edição do usuário.

### 4. Montar a aula completa
Gerar `aulaNN/index.qmd`: arquivo único com saída dupla HTML/RevealJS,
código Python embutido, seguindo o estilo descrito acima e o tom das
aulas já publicadas em outras disciplinas (comece a partir de uma
delas como referência de formato, já que o antigo diretório de
exemplos de estilo não foi trazido para este projeto), e a estrutura
de blocos definida em `_00-plano-aula.md`. Incluir diagramas TikZ onde
fizer sentido (ver seção acima), e os exercícios obrigatórios (ver
seção "Exercícios" acima: seção de exercícios ao fim das notas HTML;
exercícios de checagem intercalados nos slides, cada um seguido da
solução no slide seguinte). **PARAR.**

### 5. Atualizar o `index.qmd` da disciplina
Após o usuário aprovar `index.qmd` da aula (fim da Etapa 4), propor a
atualização do `index.qmd` da disciplina — a listagem de aulas do
curso.

Adicionar (ou atualizar, se a aula já tinha uma entrada anterior) o
link da aula, no mesmo formato das demais entradas dessa disciplina
(ver as lições já linkadas no mesmo arquivo para o formato exato —
título, conceito de ML, conceito teórico, objetivos, competências
esperadas), apontando para `./aulaNN/index.qmd`.

**Esta é uma edição de um arquivo já existente, não a criação de um
arquivo novo — por isso o mesmo cuidado das etapas anteriores não
basta.** Antes de escrever no `index.qmd`:

1. Mostrar no chat o trecho exato que será alterado/adicionado (a
   linha nova ou o antes/depois, se for uma atualização).
2. Esperar confirmação explícita do usuário.
3. Só então aplicar a edição no arquivo.

Se o usuário pedir para regenerar `index.qmd` da aula depois de já ter
uma entrada no `index.qmd` da disciplina (ex: reaprovação de uma
versão revisada), tratar a atualização do link/título da mesma forma —
propor, mostrar, esperar aprovação.

### 6. Avançar
Só gerar a aula N+1 quando o usuário disser algo como "próxima aula"
ou "continuar".

---

## Continuidade entre aulas

Antes de gerar uma aula nova, reler os planos de aula e os `index.qmd`
das aulas anteriores já aprovadas, para manter notação, nível de
formalismo e progressão consistentes — e para não repetir conteúdo já
coberto.

## Precisão de conteúdo técnico

Ao lidar com conteúdo matemático/estatístico, sinalizar explicitamente
quando algo estiver sendo inferido ou generalizado a partir do livro,
em vez de copiado fielmente — especialmente em provas, propriedades
estatísticas, e afirmações sobre otimalidade.

## Registro de estado

Sempre atualizar `_progresso.md` marcando a aula atual e o que já foi
aprovado nela (plano de aula / fontes / aula completa).
