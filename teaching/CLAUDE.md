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
│   ├── index.qmd               # página pública do curso + planejamento
│   ├── _fontes/                 # PDFs de referência (normalmente links simbólicos)
│   ├── _progresso.md            # registro de estado + dicionário de notações
│   ├── aula01/
│   │   ├── index.qmd            # a aula em si (saída HTML + RevealJS) — SEM exercícios embutidos
│   │   ├── exercicios.qmd       # publicado — questões da aula (discursivas + V/F), autocontido
│   │   ├── soluções.qmd         # publicado — gabarito de exercicios.qmd
│   │   ├── _00-plano-aula.md    # plano de aula, não publicado
│   │   ├── _01-fontes.md        # trechos citados literalmente, não publicado
│   │   └── _02-respostas-pausas.md  # gabarito das Pausas Ativas (não do Exercícios), não publicado
│   ├── aula02/
│   └── ...
└── ...
```

Cada disciplina é autocontida na sua subpasta. Cada aula é uma subpasta própria dentro da disciplina, nomeada `aulaNN` (`aula01`, `aula02`, ...). Algumas disciplinas (ex.: `optimization-linear-algebra`) também têm uma pasta `src/` com módulo Python compartilhado entre aulas — não é obrigatório, use se houver código repetido o bastante entre aulas para justificar.

**Por que os nomes com `_` na frente:** o Quarto ignora por convenção qualquer arquivo ou pasta cujo nome comece com `_` — nunca é renderizado nem copiado para o site publicado, e um link para um arquivo assim sempre dá 404 no site ao vivo (não é uma questão de configuração, é assim que o build do Quarto funciona). `_fontes/`, `_progresso.md`, `_00-plano-aula.md` e `_01-fontes.md` usam esse prefixo de propósito: são material de apoio/planejamento (e, no caso de `_fontes/`, PDFs de livros com direitos autorais) que nunca deve aparecer no site ao vivo. **Exceções deliberadas, sem `_`, que são páginas públicas de verdade:** o `index.qmd` de cada aula e da disciplina, e (desde 2026-09-14, ver "Exercícios" abaixo) `aulaNN/exercicios.qmd` e `aulaNN/soluções.qmd` — o gabarito por aula é público nesta convenção, uma mudança deliberada de política em relação à versão anterior deste documento (que só previa um gabarito público consolidado por disciplina, não por aula).

**Migração concluída (2026-09-14 a 2026-09-15):** a convenção acima (`exercicios.qmd`/`soluções.qmd` públicos por aula, substituindo a seção "Exercícios" embutida no `index.qmd` e o antigo arquivo oculto de gabarito) já foi aplicada em **todas** as disciplinas desta pasta que têm exercícios publicados: `supervised-learning`, `unsupervised-learning`, `optimization-linear-algebra` (2026-09-14), e `object-oriented-programming` e `computing-and-society` (2026-09-15). Não existe mais nenhuma página `exercicios.qmd` consolidada na raiz de disciplina, nem gabarito oculto de V/F por aula (`_01-respostas.md`/`_02-solucoes.md`) — onde esses arquivos ocultos ainda existem (ex.: `_01-respostas.md` em `object-oriented-programming`), sobrou só a seção de Pausas Ativas, que é um mecanismo diferente (ver "Pausa Ativa" acima) e continua oculta por design. Qualquer disciplina nova, ou uma disciplina hoje sem exercícios (`ai-ethics`, `operational-research`) que ganhe uma seção de Exercícios no futuro, deve nascer direto neste padrão — não recriar a página consolidada antiga.

**Fontes como link simbólico.** Os arquivos em `_fontes/` podem ser links simbólicos apontando para os PDFs/slides originais em outro lugar do disco (ex.: `ln -s ../../../livros/prml.pdf _fontes/prml.pdf`) — leia-os normalmente pelo caminho dentro de `_fontes/`, sem tratamento especial. Prefira links relativos, para o projeto continuar funcionando se a pasta for movida. **Nunca copie o PDF de verdade para dentro do projeto** — o prefixo `_` só garante que o Quarto ignore a pasta; um link simbólico garante também que o arquivo de direitos autorais nunca é versionado como blob do git.

---

## Etapa 0 — Identificar a disciplina (OBRIGATÓRIA, toda sessão)

Antes de ler, editar ou gerar qualquer arquivo, é preciso saber em qual subpasta de disciplina trabalhar nesta sessão.

- Se o usuário já declarou a disciplina na mensagem (ex: "Disciplina: supervised-learning" ou "trabalhando em optimization-linear-algebra"), usar essa subpasta e confirmar em uma linha antes de prosseguir.
- Se não declarou e houver mais de uma subpasta de disciplina em `teaching/`, **perguntar qual é a disciplina da sessão** antes de qualquer outra ação. Não adivinhar pela última disciplina usada em sessões anteriores — o estado pode ter mudado.
- Se o workspace aberto já é a subpasta de uma única disciplina, essa é a disciplina — não perguntar.

Todos os caminhos de arquivo nas etapas abaixo (`index.qmd`, `_fontes/`, `aulaNN/`, `_progresso.md`) são relativos à subpasta da disciplina identificada nesta etapa, não à raiz `teaching/`.

---

## Continuidade entre aulas (sem esgotar o contexto)

Manter notação, nível de formalismo e progressão consistentes entre aulas importa, mas reler o `index.qmd` inteiro de cada aula anterior aprovada, aula após aula, esgota a janela de contexto rapidamente numa disciplina já com várias aulas. Em vez disso:

1. Leia `_progresso.md` da disciplina primeiro — ele guarda tanto o que já foi aprovado em cada aula quanto um **dicionário de notações** (símbolo/termo → significado → aula onde foi introduzido). Esse dicionário é a fonte principal para saber se um símbolo já existe e o que ele significa.
2. Leia o **resumo do `_00-planejamento.md` da aula imediatamente anterior** (aula N-1) — o suficiente para saber onde a aula passada parou, qual foi o gancho de fechamento, e retomar a partir dali.
3. Só leia o `index.qmd` completo de uma aula anterior específica **sob demanda**, quando o dicionário de notações e o resumo do planejamento não bastarem para resolver uma dúvida concreta (ex.: "como exatamente essa fórmula foi apresentada", "que exemplo-fio foi usado ali") — não como prática padrão de toda sessão.

Sempre que uma aula nova introduzir notação nova relevante para aulas futuras, registre-a no dicionário de `_progresso.md` (Etapa 5 do ciclo, abaixo) — é isso que torna a leitura enxuta das próximas aulas possível.

---

## Estrutura da aula

### Estrutura macro (o "esqueleto" da aula)

Tendo em vista a natureza dos conteúdos do curso, a estrutura da aula deve seguir **uma de duas estratégias pedagogicamente fundamentadas**, a ser escolhida na etapa de Planejamento, de acordo com o tipo de objeto de estudo:
* **Estratégia A: *Outside-In* (Para Aulas de Modelos e Algoritmos)**
  *Uso:* Árvores de Decisão, SVM, Gradient Boosting, Regressão Logística, K-Means.
  *Lógica:* Guiada do prático para o formal: Modelo Mental/Catchy $\to$ Necessidade Teórica $\to$ Teoria Formal $\to$ Síntese e Limitações.
* **Estratégia B: *Inside-Out com Problema-Fio* (Para Aulas de Fundamentação Matemática/Linguagem)**
  *Uso:* Representações Matriciais, Derivadas/Gradiente, Espaços Vetoriais, SVD/Decomposição.
  *Lógica:* Guiada pela necessidade do idioma matemático: Problema-Fio da Engenharia/Geometria $\to$ Mecanismo/Operação $\to$ Diagnóstico Teórico $\to$ Ponte/Limitação para a próxima aula.

Ambas as abordagens devem manter os **3 movimentos fundamentais** (Abertura com problema/roteiro, Desenvolvimento segmentado em blocos de 10–15 min com pausas ativas onde tem perguntas e testes de V/F, e Fechamento retomando os desafios iniciais da aula):

**1. Abertura (10 min)** — o objetivo é criar o "gancho" cognitivo (deve ser chamado de Revisão e Introdução):
- **Revisão**: Faça uma revisão cuidadosa dos conceitos principais da aula anterior. Dando foco no que liga com a aula atual. **"Cuidadosa" significa explicar cada conceito, não só nomeá-lo ou enunciar o resultado em uma linha** — feedback explícito do usuário depois de revisar uma Revisão Rápida que citava três resultados da aula anterior num parágrafo só, cada um em uma frase, sem lembrar o porquê/mecanismo. Para cada conceito revisado: diga o que ele afirma, relembre (em 1-2 frases, não a prova inteira de novo) por que é verdade ou de onde vem, e só então conecte com a aula atual — não vale supor que citar o nome/resultado já reativa o entendimento do aluno. Isso é a mesma regra de "quantidade de informação quase igual entre notas e slides, nunca um resumo de tópicos" (ver "Formato do arquivo de aula" abaixo) aplicada especificamente à seção de Revisão, que é onde a tentação de só listar rótulos é maior.
- **Idéia Central** (Ausubel): Uma ideia-ponte que conecta o novo conteúdo ao que foi visto anteriormente.
- **Roteiro explícito**: dizer as 3–4 perguntas que a aula vai responder (não dá para ser só uma pergunta, deve ter alguma introdução para não ficar uma lista que é lida de passagem). Isso reduz carga cognitiva extrínseca porque o aluno para de gastar memória de trabalho tentando adivinhar para onde vai.
- **Problema motivador**: discuta e provoque os alunos a pensar um pouco. Isso vem antes do formalismo, não depois.
- **Pausa ativa** veja abaixo.

**2. Intuição (10 min)** Quando possível, explique em linhas gerais o algoritmo/modelo, sem grandes complicações matemáticas (exemplo: em árvore de decisão dá para explicar que vamos quebrar o espaço recursivamente, e a cada quebra a informação resumida em cada bloco é mais explicativa do que antes), mostre gráficos, algoritmos, diagramas. O aluno deve praticamente entender o que vamos fazer, só vai faltar detalhes mais pesados. Isso deve ser aplicado quase sempre na **Estratégia A** e quando cabível, na **Estratégia B**.

**3. Desenvolvimento (segmentado)** — o ponto crítico: não é um bloco contínuo.
- **Segmentação em blocos de 10–15 min**, cada um com um único "ponto de aterrissagem". A atenção sustentada em exposição passiva degrada rapidamente; o corte periódico reinicia o ciclo.
- **Use sinalização verbal**: "isto é o resultado central", "esta hipótese é a que vamos relaxar depois". Marcadores explícitos de hierarquia evitam que tudo pareça igualmente importante.
- **Pausas ativas ao final do bloco.**
- **Desenvolvimento matemático *principled***: uma vez passada a Intuição, o rigor sobe — não apresente a fórmula/técnica final já pronta. Primeiro **anuncie explicitamente as premissas/suposições** que vão ser assumidas (ex.: "vamos assumir que $p(\mathbf{x})$ é aproximadamente constante dentro de uma região pequena $R$"), depois **desenvolva passo a passo** como essas premissas levam à técnica final, deixando visível cada passo lógico/matemático do caminho — o aluno precisa conseguir seguir *como* se chega no resultado, não só receber o resultado e confiar nele.

**4. Fechamento (5 min)** — quase sempre o mais sacrificado e o mais valioso:
- Retomar as perguntas da abertura e responder cada uma em uma frase.
- Nomear explicitamente o que ficou em aberto e o que vem na próxima aula.

**Geral - Pausa Ativa (3 min)** — A pausa ativa visa fazer o aluno parar para refletir sobre o problema e confiar que entendeu o que veio antes. Pausas ativas ficam tanto nos slides quanto nas notas.

- **Pergunta Motivadora**: faça uma pergunta provocadora que provoque o aluno a pensar sobre o que discutimos, não só guardar, use essa estrutura:

  ::: {.callout-tip}
  ## Pergunta provocadora.

  Dica para ajudar a conduzir.
  :::
- **V/F condutor**: crie perguntas de verdadeiro ou falso que validem o conteúdo anterior e ajudem o aluno a pensar mais profundamente na pergunta motivadora. **Não use a sintaxe de lista de tarefas do Markdown (`- [ ]`)** — o Pandoc renderiza isso como um `<input type="checkbox">` de verdade, clicável no navegador (feedback explícito do usuário: "isso não é bom").

  **Cuidado — nem todo glifo de caixa "parece seguro" realmente é.** A extensão `task_lists` do Pandoc trata alguns glifos Unicode como sinônimos de `[ ]`/`[x]` mesmo fora da sintaxe de colchetes, e os converte no mesmo `<input type="checkbox">` clicável — **`☐` (U+2610) e `☒` (U+2612) são especiais para o Pandoc e viram checkbox mesmo assim** (verificado testando `pandoc -f markdown -t html` isoladamente; `☑` U+2611, por outro lado, não é especial e fica como texto puro — mas é melhor não confiar nessa assimetria). Os glifos **confirmados seguros** (testados, permanecem texto puro) são:
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

- **Resposta**: nos slides crie um novo slide com resposta do V/F e depois coloque de novo a pergunta motivadora e espere a resposta do aluno. Na resposta, reescreva cada item trocando `□` pelo glifo resolvido: `✔` para item **Verdadeiro**, `✗` para item **Falso** — a caixinha "estilizada" já comunica o veredito, sem precisar do rótulo "Verdadeiro"/"Falso" por extenso ao lado (pode manter uma justificativa curta depois do glifo, se ajudar). Exemplo:

  ::: {.callout-tip}
  ## Tema do V/F — Resposta

  - ✔ Afirmação 1 (verdadeira).
  - ✗ Afirmação 2 (falsa) — breve razão.
  :::

  **Nas notas de aula, a resposta da Pausa Ativa NÃO fica no `index.qmd` publicado.** Ela vai para `aulaNN/_02-respostas-pausas.md` (oculto, prefixo `_` — nunca deve aparecer no site), discutindo cada pergunta motivadora e dando a solução dos V/F com os mesmos glifos `✔`/`✗`. O `index.qmd` das notas só contém a pergunta em si (mesmo bloco `::: {.callout-tip}` usado no slide de Pergunta, sem duplicar), nunca a resolução. **Isso é diferente do gabarito da seção Exercícios** (ver "Exercícios" abaixo), que é público desde 2026-09-14 — a Pausa Ativa continua oculta porque é uma provocação pontual para reflexão em aula, não um banco de questões para os alunos consultarem depois.

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

## Registro e vocabulário

Ser didático não significa usar linguagem ruim. Evite gírias/coloquialismos comerciais para descrever vantagens e limitações de um método — em especial **"o que X compra"** / **"o que X custa"** (ex.: "o que a MST compra", "o preço de não assumir forma nenhuma"), um vício de escrita que já apareceu repetido em várias aulas. Prefira nomear a coisa diretamente: **vantagens e limitações**, **custo computacional**, **o que se ganha e o que se perde**, ou reescrever a frase sem a metáfora comercial (ex.: "X permite fazer Y sem precisar de Z, mas exige W").

## Formato do arquivo de aula

Cada aula é um **único arquivo `index.qmd`** dentro da sua pasta `aulaNN/`, não um par separado de slides e notas. O mesmo arquivo produz duas saídas (HTML e RevealJS) via blocos `::: {.content-visible when-format="..."}`:

**O papel de cada saída não é "completo" vs. "resumido" — é "corrido" vs. "itemizado", com quantidade de informação quase igual.** Feedback explícito do usuário, depois de revisar slides "muito simplificados" de uma aula cujas notas estavam boas: a diferença entre `notas.html` e `slides.html` **não é de profundidade de conteúdo**, é de **forma de organização**. Antes de aceitar uma versão de slide como pronta, pergunte: "se um aluno só tivesse acesso a este slide (nunca às notas), ele teria a mesma informação, só organizada de outro jeito — ou ele perderia algo que só está na versão em prosa?" Se a resposta for "perderia", o slide está simplificado demais.

- **HTML** (`unless-format="revealjs"`): prosa corrida, contando a aula como uma **história com detalhes** — com as provas/derivações por extenso, citações de página do livro, avisos de leitura e notas de rodapé pedagógicas. Sai como `notas.html` em TODA aula, sem exceção (ver "Nomes de arquivo de saída" abaixo) — o ícone de livro no rodapé dos slides (`../logos-footer.html`) linka direto pra `notas.html` como caminho relativo fixo, contando com esse nome ser sempre o mesmo.
- **RevealJS**: a **mesma história, quase o mesmo tanto de detalhe**, só que reorganizada em itens/fragmentos em vez de parágrafos corridos — nunca um resumo de tópicos. Os slides precisam sustentar a aula sozinhos em sala, não só sinalizar *highlights* ("só highlights é complicado para trabalhar", feedback explícito do usuário). Isso inclui coisas fáceis de esquecer de levar para o slide porque "já foram ditas na nota": **o que uma variável/coluna do dataset significa de verdade** (não só o nome da coluna — se as notas explicam que `radius_mean` é o raio médio do tumor medido no exame, o slide também precisa dizer isso, não só usar o nome da variável como se fosse autoexplicativo), o porquê de uma escolha, o contraste com o que veio antes. Usar bullets/fragmentos (`. . .`, `::: {.fragment}`) para revelar progressivamente e organizar uma ideia por slide, mas sem cortar explicações, derivações e nuances essenciais — o corte em relação à versão HTML é de ritmo e organização visual, não de profundidade de conteúdo. Conceitos não-triviais (ex: teoria kantiana, normas *prima facie*) precisam do mesmo cuidado explicativo nos slides que têm nas notas — não vale simplificar a ponto de distorcer. Sai como `slides.html`.

  **Use caixas para destacar informações (`callout-tip`/`note`/`important`/`warning`).** Mas não faz sentido ter mais de uma caixa por slide.

  **Intercale HTML e RevealJS.** Os blocos `content-visible` de HTML e de RevealJS devem ficar intercalados ao longo do arquivo — importante para evitar duplicidade de código Python/TikZ que vai ser rodado. Ordem lógica dentro de cada bloco, quando há um gráfico/diagrama envolvido: **(A)** prosa das notas fazendo referência ao gráfico → **(B)** slide em tópicos apontando para o mesmo gráfico → **(C)** o *chunk* de código (Python/TikZ) que gera o gráfico, compartilhado pelos dois formatos, para não reprocessar nada.

  **Nenhum slide pode ficar vazio/esvaziado de conteúdo.** Um slide com só um título e uma frase curta (ou pior, um título e nada — texto que "sobrou" depois de um gráfico ter ficado no slide anterior) não sustenta um minuto de fala sozinho. Antes de aceitar um slide como pronto, pergunte: "isto ocupa o slide, ou está vazio demais?" Duas saídas, nunca "deixar assim": **(a)** falta conteúdo — adicionar mais explicação, outra citação, uma reafirmação com uma perspectiva nova — não só um enfeite; ou **(b)** o conteúdo é fino demais para justificar um slide próprio — juntar com o slide vizinho (anterior ou seguinte) em vez de espalhar pouca informação por muitos slides. Um caso comum desse problema: um gráfico/diagrama aparece sozinho num slide, e o slide seguinte só comenta esse gráfico em texto, sem o gráfico por perto — nesse caso, prefira manter o comentário no mesmo slide do gráfico (ou repetir/reduzir o gráfico ao lado do comentário) em vez de separar imagem e leitura da imagem em dois slides.

  **Depois de montar os slides de um bloco inteiro, faça uma passada de revisão só de "picotamento" (fluxo), separada da revisão de conteúdo.** Feedback explícito do usuário, depois de revisar uma aula inteira: slides "picotados" são comuns e têm sempre uma das duas causas do parágrafo acima (falta conteúdo, ou o conteúdo devia estar junto de outro slide) — mas essa avaliação individual, feita slide a slide enquanto se escreve, não pega o problema com confiabilidade, porque cada slide sozinho pode parecer "aceitável" e o corte só fica óbvio olhando a sequência inteira. Depois de escrever (ou editar) um bloco de slides, releia a lista de headings `##` daquele bloco em sequência (ex.: `grep -o '<h2[^>]*>[^<]*'` no HTML renderizado, ou simplesmente a lista de `##` do `.qmd`) e, para cada slide, pergunte: "este título tem um único ponto de aterrissagem substancial, ou é só uma fração de uma ideia que continua no vizinho?" Sinais concretos de picotamento: (i) um slide com um só fragmento curto quando o vizinho imediato termina ou começa a mesma ideia; (ii) uma figura/diagrama sozinho num slide cujo único comentário mora no slide seguinte (o caso já descrito acima); (iii) uma sequência de 3+ slides que, lidos em voz alta, soam como um único parágrafo cortado em pedaços artificiais em vez de pontos de pausa naturais. Quando encontrar isso, funda os slides (reescrevendo a transição em prosa, não só concatenando fragmentos) em vez de deixar "assim mesmo" — o teste não é "cada slide tem conteúdo?" (o já coberto acima), é "esta sequência de slides tem o número certo de cortes?".

**Nomes de arquivo de saída:** definir explicitamente no YAML do `index.qmd`, já que o padrão do Quarto usaria o nome do próprio arquivo (`index`) para ambos os formatos. **`output-file: notas.html` não é só convenção — é obrigatório**: o ícone de livro no rodapé dos slides (`../logos-footer.html`) linka pra `notas.html` como caminho relativo fixo; uma aula sem esse `output-file` sairia como `index.html` e o ícone quebraria (404) nela.

```yaml
format:
  html:
    output-file: notas.html
  revealjs:
    output-file: slides.html
```

Além disso, cada aula soma o tema visual e as configurações compartilhadas de slide (footer, logos, dimensões) por cima — ver um `index.qmd` de aula já existente para o bloco `format:` completo, copiando-o em vez de reescrever do zero. **Essas configurações compartilhadas vivem no front matter de CADA aula, não no `_quarto.yml` do projeto** — um `format: revealjs:` global já quebrou o build do site inteiro de forma silenciosa (nem toda página some do render, e o erro reportado não aponta pra causa real), então não promova essas configurações pro `_quarto.yml`, mesmo que pareça redundante repeti-las em cada aula.

## Dados: prefira exemplos reais a sintéticos

As aulas têm ficado teóricas demais para quem está aprendendo Aprendizado de Máquina/Otimização pela primeira vez — sem um dado real e palpável por trás, a matemática fica abstrata demais. Ao escolher o dataset que ilustra o fio condutor de uma aula (o "problema-fio" que atravessa os blocos), **prefira um dataset real a um dataset sintético**, e **prefira ambos a um dataset de brinquedo como Iris** — interessante para ensinar sintaxe, mas pouco palpável (poucos alunos têm intuição sobre pétalas de flor).

**De onde puxar o dataset: Hugging Face Hub, não pedir arquivo ao usuário a cada aula.** Em vez de esperar o usuário trazer um CSV para cada aula nova, use a lista curada abaixo — todos os itens foram testados com `datasets.load_dataset(repo_id)`, sem token/chave (datasets públicos do Hub não exigem autenticação; só datasets *gated*/privados exigiriam, via `HF_TOKEN`, o que não é o caso de nenhum item desta lista). O kernel Jupyter usado nas aulas (`homepage`, declarado como `jupyter: homepage` no front matter de cada aula — o ambiente vem de `dependencies` em `pyproject.toml`, `uv sync`) já tem `datasets` e `huggingface_hub` instalados. Ao carregar, aparece um aviso de "unauthenticated requests" — é só um aviso de limite de taxa, não um bloqueio; pode ignorar.

| Dataset (repo Hugging Face) | Linhas | Uso recomendado | Observações |
|---|---|---|---|
| **Adult / Census Income** — `scikit-learn/adult-census-income` | 32.561 | Classificação binária (renda >50k), atributos mistos (contínuos + categóricos) — bom para Naive Bayes, árvores, regressão logística | Sem colunas problemáticas |
| **Breast Cancer Wisconsin** — `scikit-learn/breast-cancer-wisconsin` | 569 | Classificação binária médica (diagnóstico M/B), todos os atributos contínuos | Descartar `id` e `Unnamed: 32` (coluna vazia, artefato do CSV original) |
| **Pima Indians Diabetes** — `khoaguin/pima-indians-diabetes-database` | 768 | Médico, multivariado contínuo (Glicose, IMC, pressão, etc.), alvo binário — bom para Aula 1 de `supervised-learning` (Beta 1D, usando só `Glucose`) **e** Aula 1 de `unsupervised-learning` (Gaussiana multivariada/Mahalanobis, no lugar dos sensores sintéticos) | Coluna alvo já vem nomeada `y` |
| **California Housing** — `gvlassis/california_housing` | 20.640 (já dividido train/val/test) | Regressão — preço de imóvel a partir de 8 atributos contínuos; bom para regressão linear, regularização, e para `optimization-linear-algebra` (escalas bem diferentes entre atributos, motiva *feature scaling*) | Substitui o antigo Boston Housing (removido do scikit-learn por um problema ético numa variável) |
| **Default of Credit Card Clients (UCI)** — `Lancer73/uci-credit-card-default` | 30.000 (já dividido train/val/test) | Risco de crédito, classificação binária, atributos de histórico de pagamento — bom para árvores, ensembles | — |
| **German Credit Data (Statlog)** — `AiresPucrs/german-credit-data` | 1.000 | Risco de crédito, mistura explícita de categóricos (Sexo, Moradia, Propósito) e numéricos (Idade, Valor, Duração) — bom encaixe para Naive Bayes com atributos de tipos diferentes | Dataset pequeno, bom para uma aula que não quer um treino pesado |
| **Credit Card Transactions Fraud Detection** — `dazzle-nu/CIS435-CreditCardFraudDetection` | ~1.048.575 | Fraude/anomalia com atributos interpretáveis (valor, categoria, localização) — melhor para a lógica de detecção de anomalia da Aula 1 de `unsupervised-learning` do que o dataset clássico da ULB, cujos atributos são componentes de PCA anônimos, não interpretáveis | Grande: **subamostrar** para uso em aula; descartar colunas `Unnamed: 0`, `Unnamed: 23`, `6006` (artefatos); classe muito desbalanceada (avisar antes de usar) |

Isso não bane dados sintéticos por completo: eles seguem úteis para isolar um ponto matemático específico (ex.: um contraexemplo controlado, ou uma verificação numérica de uma propriedade, como o contraexemplo de Gini/entropia da Aula 3 de `supervised-learning`). Mas o **exemplo-fio** que atravessa os blocos de uma aula — o problema que dá contexto para tudo o resto — deve, sempre que possível, vir de um dataset real, preferencialmente um da tabela acima.

**Como usar no `.qmd`:** carregar no bloco de setup global, junto com os outros imports:

```python
from huggingface_hub.utils import logging as hf_logging
hf_logging.set_verbosity_error()  # evita o aviso "unauthenticated requests" vazando no chunk

from datasets import disable_progress_bar
disable_progress_bar()  # evita barra de progresso poluindo a saída do chunk

from datasets import load_dataset
ds = load_dataset("scikit-learn/adult-census-income")["train"].to_pandas()
```

Sem as duas primeiras linhas, tanto o aviso de "unauthenticated requests" quanto a barra de progresso do download vazam para a saída do chunk renderizado (mesmo com `echo: false`, que só esconde o código, não a saída/stderr) — com elas, a saída fica limpa.

O download é armazenado em cache local (`~/.cache/huggingface/`) — renderizações seguintes na mesma máquina não baixam de novo. Se, algum dia, um dataset novo (fora desta lista) for necessário, teste o `load_dataset(repo_id)` antes de incorporar à aula (confirmar que carrega sem token e checar as colunas), e considere adicionar à tabela acima se for reutilizável em outras aulas.

## Citações e trechos de fontes: sempre traduzidos no `index.qmd`

Fontes bibliográficas em inglês (comum neste projeto) devem ter seus trechos **traduzidos para português** no `index.qmd` da aula — tanto nas notas quanto nos slides. Deixar a citação em inglês tem um custo alto de troca de idioma para quem lê ou apresenta em português (feedback explícito do usuário). Evite "copiar e colar" trechos dos livros.

- No `_00-planejamento.md` (seção de fontes, ver ciclo abaixo), o trecho deve ser **citado literalmente na língua original**, extraído do PDF/slide antigo — nunca reescrito de memória, nunca parafraseado, nunca traduzido nessa etapa, para que a checagem do usuário seja direta contra o PDF.
- No `index.qmd` da aula, usar a tradução para português do trecho, deixando claro que é tradução nossa (ex.: "tradução livre"), não uma citação literal de outra fonte. Termos técnicos sem tradução direta e estável (ex.: *prima facie*, em latim) podem ficar no original, com uma explicação ao lado na primeira aparição.

## Fluxogramas e diagramas

Ao montar o bloco, se o conteúdo tiver estrutura sequencial, uma árvore de decisão, um processo com ramificações, ou uma comparação de caminhos alternativos (ex: "três saídas honestas para um problema"), **proponha um diagrama TikZ** (` ```{.tikz} `), sem esperar o usuário pedir. O site já está configurado (`_quarto.yml` da raiz do projeto) com o filtro `pandoc-ext/diagram` e o *engine* TikZ (via `pdflatex`), renderizando nativamente nos dois formatos de saída (HTML e RevealJS). Use as cores preferenciais do IC (ver `lesson-theme.scss`) nos elementos do diagrama quando fizer sentido. Só pergunte se não estiver claro que o diagrama ajuda mais do que texto.

**Não use `%%| fig-align: center` nem `%%| out-width: ...` num bloco `{.tikz}` — não têm efeito nenhum.** Verificado lendo o próprio filtro (`_extensions/pandoc-ext/diagram/diagram.lua`): `fig-align` só é aplicado quando a imagem tem legenda (`fig-cap`), e sem legenda o filtro devolve um `<img>` solto, sem nenhuma classe de alinhamento/tamanho. Para centralizar e/ou redimensionar um diagrama TikZ (ou qualquer figura de chunk Python que precise de um tamanho diferente do padrão da aula), ver "Redimensionar figuras e diagramas" abaixo.

### Redimensionar figuras e diagramas

**`out-width`, `fig-width` e `fig-height` (chunk options) não funcionam nas aulas.** Essas três são implementadas só pelo engine `knitr` (R) — confirmado no schema oficial do Quarto (`tags: {engine: knitr}` em cada uma) e testado ao vivo (valores diferentes de `out-width`/`fig-width` num chunk Python não mudavam o tamanho da imagem gerada). Como toda aula usa `jupyter: <kernel>`, essas opções são silenciosamente ignoradas — não proponha nem use nenhuma delas.

**Regra para figuras e diagramas**: todo chunk Python que gera figura e todo bloco `{.tikz}` devem sair já envolvidos em `.fig-resize`, mesmo que o tamanho padrão (100%) sirva.

::: {.fig-resize style="width: 100%; margin: 0 auto;"}
```{python}
...
```
:::

## Exercícios (obrigatório em toda aula)

Toda aula precisa de exercícios de fechamento. **Desde 2026-09-14, em `supervised-learning`, `unsupervised-learning` e `optimization-linear-algebra`, esses exercícios NÃO ficam dentro do `index.qmd` da aula** — vivem em dois arquivos-irmãos, ambos publicados (páginas reais do site, sem prefixo `_`):

- **`aulaNN/exercicios.qmd`** — as questões em si, sem solução: **2 a 3 questões discursivas/conceituais** e **entre 6 e 10 questões de V/F** (não itens — **blocos de 4 itens cada**, ou seja, 24 a 40 itens ao todo, cada bloco num tema diferente da aula, cobrindo o conteúdo da aula de ponta a ponta) — o número exato dentro dessas faixas ajusta conforme a densidade da aula: uma aula com menos blocos de conteúdo não deve ser esticada até 10 questões de V/F só para bater uma cota, nem uma aula densa deve ser espremida em 6. Pode reaproveitar questões de fim de capítulo das próprias fontes bibliográficas (citando de onde vieram, como já se faz com trechos citados) ou propor questões originais — nesse caso, sinalizar que são originais, não da fonte. Cada questão de V/F tem 4 itens do mesmo tema, e só é considerada correta se todos os 4 forem acertados (na avaliação, o aluno pode deixar a questão em branco com punição de 20% da nota da questão). Use esse formato:

  ::: {.callout-note icon=false}
  ## Teste N — Tema das questões

  - □ Afirmação 1.
  - □ Afirmação 2.
  - □ Afirmação 3.
  - □ Afirmação 4.
  :::

  **Numeração "Teste N" (desde 2026-09-15).** Cada bloco de V/F leva um número sequencial no próprio título do bloco, no formato `Teste N — Tema das questões` — nunca só `Tema das questões` sem o prefixo. A numeração **reinicia em 1 a cada aula** (a primeira aula de uma disciplina e a última não compartilham a sequência; cada `aulaNN/exercicios.qmd` tem seu próprio `Teste 1`, `Teste 2`, ...) e segue a ordem em que os blocos já aparecem no arquivo — não há critério de ordenação além disso. O mesmo prefixo é repetido em `soluções.qmd`, em ambos os títulos do par pergunta/resposta (`## Teste N — Tema` e `## (Resposta) Teste N — Tema`, ver "Registro da justificativa" abaixo). Um eventual bloco de aviso/nota solto no fim do arquivo (fora do padrão pergunta+resposta) não é numerado.

  **Mesma regra do glifo não-clicável da Pausa Ativa se aplica aqui**: nunca usar a sintaxe de lista de tarefas do Markdown (`- [ ]`), nem os glifos `☐`/`☒` (ambos especiais para a extensão `task_lists` do Pandoc, viram `<input type="checkbox">` clicável mesmo fora dos colchetes) — usar sempre `□` (U+25A1) como texto simples.

  **Autocontido é obrigatório.** Como `exercicios.qmd` pode ser usado diretamente como banco de questões de prova (feedback explícito do usuário/monitor, depois de um monitor encontrar blocos que só faziam sentido lendo a aula inteira), nenhum item pode depender de contexto que só existe no `index.qmd` da aula — nunca escrever algo como "os pontos B e C desta aula" ou usar uma notação/exemplo introduzido só na aula sem redefini-lo ali mesmo. Se o item precisa de um exemplo ou de notação da aula para fazer sentido, inclua esse contexto (reescrito, resumido) diretamente no enunciado do item ou num preâmbulo curto do bloco — o item deve poder ser lido, entendido e resolvido por alguém que nunca assistiu àquela aula.

  **`aulaNN/soluções.qmd`** — o gabarito de `exercicios.qmd`, também publicado (ver "Registro da justificativa" abaixo para o formato).

- **`index.qmd` da aula:** não tem seção de Exercícios própria — no lugar dela (tipicamente perto do Fechamento, tanto nas notas quanto nos slides), um link simples para as duas páginas-irmãs, no mesmo padrão dos links `[Slides](slides.html)`/`[Lista de aulas](../index.qmd)` já usados no topo de cada aula, por exemplo: `[Exercícios](exercicios.qmd){.see-all .exercicios-link} [Soluções](soluções.qmd){.see-all .solucoes-link}`. **As classes `.exercicios-link`/`.solucoes-link` são obrigatórias** (desde 2026-09-14) — é o que dá a cada link seu ícone (interrogação para Exercícios, `bi-check2-square` para Soluções; CSS em `styles.css`, regras `a.see-all.exercicios-link::before`/`a.see-all.solucoes-link::before`); sem a classe, o link aparece sem ícone. `exercicios.qmd` e `soluções.qmd` também usam essas classes nos links de navegação de topo que apontam um para o outro, mais uma terceira classe própria no link de volta pra aula: `[Aula](index.qmd){.see-all .aula-link}` (`bi-journal-text`, `a.see-all.aula-link::before`) — **as três classes são obrigatórias nesses dois arquivos**, correção feita em 2026-09-15 depois de um usuário notar que os links de `exercicios.qmd`/`soluções.qmd` não apareciam "bonitos" como os da aula: faltava tanto a classe do ícone de "Aula" (sem ela a caixa do cabeçalho ficava vazia, sem ícone nenhum) quanto o include abaixo.

  **`include-after-body` obrigatório no YAML de `exercicios.qmd`/`soluções.qmd`.** O visual "caixa quadrada só com ícone" desses três links no cabeçalho da aula (ver "Cabeçalho da aula" em `styles.css`) não é CSS puro — depende de `teaching/toc-accordion.js`, que move todo `a.see-all` da página pra dentro de `.quarto-title-meta` (o bloco de metadados abaixo do título, ao lado de Autor/Data). Sem carregar esse script, os três links de `exercicios.qmd`/`soluções.qmd` ficam onde o Markdown os colocou — pílulas azuis genéricas com texto, não as caixas do cabeçalho — mesmo com as classes de ícone certas. O `index.qmd` de cada aula já carrega o script via `include-after-body: ../../lesson-toc-accordion.html` no YAML (bloco `format: html:`); `exercicios.qmd` e `soluções.qmd` **precisam da mesma linha**, logo abaixo de `html:`, senão os links nunca saem do corpo da página. Esse era um requisito que faltava desde a criação do padrão (2026-09-14) — corrigido retroativamente em todas as disciplinas em 2026-09-15.

- **Slides (RevealJS):** as Pausas Ativas continuam intercaladas ao longo da aula (sem passar mais de 15 minutos de conteúdo sem uma) — isso não muda; é a seção final de Exercícios que saiu do `index.qmd`.

### Metodologia de criação de cada item de V/F (notas e slides)

**Objetivo:** cada item deve testar compreensão estrutural, capacidade de síntese e aplicação do conhecimento — não memorização rasa. Um aluno que decorou a aula sem entender a mecânica por trás dela deve errar; um aluno que entendeu deve acertar mesmo nunca tendo visto aquela frase exata antes.

**Toda afirmação precisa nascer de uma das heurísticas abaixo** (a lista não é exaustiva — o importante é a avaliação profunda, não a lista em si):

1. **Cenário contrafactual** — inverta uma premissa fundamental ou altere uma condição essencial do conceito, e afirme algo sobre a consequência lógica dessa alteração.
2. **Caso limite/extremo** — teste o comportamento do conceito num extremo absoluto (uma variável indo a infinito ou a zero, a ausência total de um fator limitante, $N\to\infty$, $\lambda\to 0$, etc.).
3. **Transferência de domínio** — descreva um cenário prático ou analítico que **não** apareceu na aula, e afirme que o conceito se aplica (ou falha) ali de um jeito específico.
4. **Falsa dicotomia/falsa equivalência** — construa uma afirmação que soe plausível por usar o jargão certo da aula, mas que erre a relação de causa e efeito de forma sutil e estrutural.

**A heurística 3 (Transferência de domínio) deve migrar para outro cenário de Aprendizado de Máquina, nunca para um domínio estapafúrdio ou decorativo.** Feedback explícito do usuário, depois de revisar uma aula cujas Pausas Ativas usavam vigas de engenharia estrutural, modos de vibração de molas acopladas, crescimento populacional e sistemas de controle como "outro domínio" — nenhum desses é errado matematicamente, mas o curso é de Aprendizado de Máquina, e espalhar as transferências por física/engenharia/ecologia deixa os exercícios com cara de banco de questões genérico, desconectado do resto do material. Ao escolher o cenário da heurística 3, prefira: outro modelo ou arquitetura (ex.: uma camada linear de rede neural, a Hessiana da função de perda de uma regressão logística), outro dataset já catalogado nesta disciplina (ver "Dados: prefira exemplos reais a sintéticos" acima — Breast Cancer Wisconsin, German Credit, Adult Census etc.) ou outra técnica de ML que usa a mesma estrutura matemática (cadeias de Markov em aprendizado por reforço, matriz de covariância em PCA). Isso vale tanto para as Pausas Ativas quanto para a seção de Exercícios final, em qualquer disciplina de ML desta pasta — não só nesta aula.

**Proibido:**
- Perguntas do tipo "o que é X" ou "X é definido como Y".
- Paráfrase literal de uma frase da aula.
- Afirmações cuja falsidade dependa só de trocar uma palavra (ex: "sempre" por "nunca", "positivo" por "negativo") sem alterar a mecânica do conceito por trás.
- Cenário de aplicação fora de Aprendizado de Máquina na heurística de Transferência de domínio (ver parágrafo acima).

**Registro da justificativa — em `aulaNN/soluções.qmd`, público.** A justificativa de cada item — por que é V ou F, apontando exatamente qual falha conceitual o aluno cometeria ao errar — vai em `aulaNN/soluções.qmd` (ver acima; **não** no arquivo oculto de Pausas Ativas, que é outro arquivo, `_02-respostas-pausas.md`). A heurística usada (Contrafactual/Limite/Transferência/Falsa dicotomia) é só uma ferramenta de construção do item (ver "Metodologia" acima) e não aparece registrada no arquivo.

**Desde 2026-09-14, cada bloco (questão discursiva ou bloco de V/F) vira um par de caixas `callout`: a pergunta repetida (idêntica a `exercicios.qmd`, inclusive qualquer preâmbulo/contexto do bloco) numa caixa `callout-note`, seguida imediatamente da resposta numa caixa `callout-tip` intitulada "(Resposta) — [mesmo título]".** Formato, por bloco de V/F:

```markdown
::: {.callout-note icon=false}
## Teste N — [Tema do bloco]

- □ [texto exato da afirmação, idêntico a exercicios.qmd, com o glifo □].
- □ [outra afirmação do mesmo bloco].
- □ [...]
- □ [...]
:::

::: {.callout-tip}
## (Resposta) Teste N — [Tema do bloco]

- ✔ Verdadeiro — [justificativa: explicação analítica e direta de por que é V/F — sem meio-termo, apontando o erro conceitual específico que o aluno cometeria ao marcar a resposta errada].
- ✗ Falso — [justificativa].
- [...]
:::
```

**Na prática (todas as disciplinas já migradas), `soluções.qmd` contém só os blocos de V/F — as questões discursivas não têm gabarito publicado.** A correção de uma questão discursiva depende da qualidade e precisão técnica do argumento apresentado, não de uma resposta fixa comparável a um V/F, então não há um par pergunta/resposta "Questão N" a publicar; o enunciado da questão discursiva mora só em `exercicios.qmd`. Se um dia isso mudar para alguma disciplina específica, o par de caixas seguiria o mesmo padrão do bloco de V/F acima, com `## Questão N` / `## (Resposta) Questão N` no lugar de `## Teste N — [Tema]` (sem o prefixo "Teste", que é exclusivo dos blocos de V/F) — mas essa não é a convenção atual.

Note que a caixa da pergunta usa `callout-note icon=false` (sem ícone) e a caixa da resposta usa `callout-tip` puro (com o ícone padrão do tip) — a diferença de ícone já ajuda a distinguir pergunta de resposta visualmente, além da cor. Quando o arquivo já tem um título maior agrupando várias questões (ex.: `## Questões de Verdadeiro/Falso` ou `## Questões discursivas`), o título dentro de cada par de caixas desce um nível, para `### Tema` / `### Questão N` / `### (Resposta) ...`, mantendo as caixas do mesmo jeito.

**Desde 2026-09-14, os slides (RevealJS) não repetem mais a seção de Exercícios.** Antes, o bloco de Exercícios era duplicado dentro do `index.qmd` (notas em prosa + os mesmos itens de novo em slides, com resposta revelada no slide seguinte) — essa duplicação é exatamente o tipo de "múltiplas cópias que podem dessincronizar" que motivou tirar os Exercícios do `index.qmd`. Os slides terminam no Fechamento e no link para `exercicios.qmd`/`soluções.qmd` (ver acima); o conteúdo de Exercícios em si — pergunta e (agora publicamente) resposta — existe uma única vez, nesses dois arquivos. Isso vale só para a seção de Exercícios final: as **Pausas Ativas continuam exatamente como antes**, intercaladas nos slides com a resposta revelada no slide seguinte (ver "Pausa Ativa" acima) — não são afetadas por esta mudança.


## Avaliações e Provas (Submódulo `evals/`)

Quando o usuário solicitar a criação de questões para **provas** ou **avaliações de disciplina** (diferente dos exercícios de fechamento de aula), estas devem ser criadas e armazenadas exclusivamente no submódulo `evals/`.

---

## Para cada aula (repetir o ciclo)

### 1. Identificar a aula e o contexto
Consultar `index.qmd` da disciplina e confirmar com o usuário o tema, objetivos e carga horária da aula NN. Ler `_progresso.md` (dicionário de notações + estado) e o resumo do `_00-plano-aula.md` da aula N-1, como descrito em "Continuidade entre aulas" acima. Não seguir sem confirmação.

### 2. Gerar o arquivo de apoio `_00-plano-aula.md`
Um único arquivo consolidando plano de aula e fontes:

- **Resumo** (5-10 linhas): o que a aula cobre, objetivos de aprendizagem, pré-requisitos (conferindo com o dicionário de notações e o resumo da aula anterior).
- **Estratégia Pedagógica Escolhida:** Estratégia A (Outside-In) ou Estratégia B (Inside-Out com Problema-Fio), com justificativa em 1 linha (ex.: "Estratégia B por se tratar de aula de fundação matemática de representação/linguagem").
- **Plano de aula**: sequência de blocos/tópicos na ordem em que serão apresentados, com tempo estimado por bloco (somando à carga horária da aula) e a lógica de transição entre eles (ex.: "Bloco 1 termina com uma pergunta sem resposta, que o Bloco 2 resolve").
- **Fontes usadas**: para cada fonte — referência (livro, capítulo, seção, páginas), o uso pretendido daquele trecho na aula, e o **trecho citado literalmente na língua original** (ver "Citações e trechos de fontes" acima — a tradução só acontece depois, no `index.qmd` da Etapa 3).

Formato:

```markdown
## Resumo — Aula N

[5-10 linhas: cobertura, objetivos, pré-requisitos]

**Estratégia Pedagógica:** [Estratégia A (Outside-In) OU Estratégia B (Inside-Out com Problema-Fio)] — [Justificativa em 1 linha]

## Plano de aula — Aula N (carga horária: XXmin)

1. **[Nome do bloco]** (~XX min) — [o que cobre, por que vem aqui]
2. **[Nome do bloco]** (~XX min) — [o que cobre, como conecta com o anterior]
...

## Fontes usadas — Aula N

### Fonte 1: PRML, §1.5.1, pp. 39-41
**Uso pretendido:** prova de que o cruzamento das conjuntas minimiza o erro esperado.

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

**PARAR** e esperar aprovação/edição do usuário.

### 3. Montar a aula completa
Gerar `aulaNN/index.qmd`: arquivo único com saída dupla HTML/RevealJS, código Python embutido, seguindo o estilo descrito acima e o tom das aulas já publicadas em outras disciplinas (comece a partir de uma delas como referência de formato), e a estrutura de blocos definida em `_00-plano-aula.md`. Incluir diagramas TikZ onde fizer sentido (ver seção acima), as Pausas Ativas intercaladas — mas **não** a seção de Exercícios, que vai em `exercicios.qmd` (Etapa 4) — e, depois de montar cada bloco de slides, a passada de revisão anti-picotamento descrita em "Formato do arquivo de aula". **PARAR.**

### 4. Gerar `aulaNN/exercicios.qmd`, `aulaNN/soluções.qmd` e o gabarito das Pausas Ativas
Três arquivos, não um só:

- `aulaNN/exercicios.qmd` — as questões (ver "Exercícios" acima: autocontido, sem depender do `index.qmd`), com o link de volta para a aula no topo (mesmo padrão `[Aula](index.qmd){.see-all}` dos demais links de navegação).
- `aulaNN/soluções.qmd` — o gabarito de `exercicios.qmd` (formato "Registro da justificativa" acima), com o mesmo link de volta.
- `aulaNN/_02-respostas-pausas.md` — a solução de cada Pausa Ativa da aula (oculto, prefixo `_`, nunca publicado).

**PARAR.**

### 5. Atualizar o `index.qmd` da disciplina e `_progresso.md`
Após o usuário aprovar `index.qmd` da aula (fim da Etapa 3):

- Propor a atualização do `index.qmd` da disciplina (a listagem de aulas do curso): adicionar ou atualizar o link da aula, no mesmo formato das demais entradas dessa disciplina, apontando para `./aulaNN/index.qmd`. **Esta é uma edição de um arquivo já existente, não a criação de um arquivo novo** — mostrar no chat o trecho exato que será alterado/adicionado (a linha nova, ou o antes/depois se for atualização), esperar confirmação explícita do usuário, e só então aplicar a edição. Se o usuário pedir para regenerar `index.qmd` de uma aula que já tinha entrada (ex.: reaprovação de versão revisada), tratar a atualização do link/título da mesma forma.
- Atualizar `_progresso.md`: marcar a aula atual e o que já foi aprovado nela (planejamento / aula completa / respostas), e registrar no dicionário de notações qualquer símbolo/termo novo introduzido nesta aula que aulas futuras vão precisar reconhecer.

### 6. Avançar
Só gerar a aula N+1 quando o usuário disser algo como "próxima aula" ou "continuar".

---

## Precisão de conteúdo técnico

Ao lidar com conteúdo matemático/estatístico, sinalizar explicitamente quando algo estiver sendo inferido ou generalizado a partir do livro, em vez de copiado fielmente — especialmente em provas, propriedades estatísticas, e afirmações sobre otimalidade.

**Definições, teoremas e demonstrações devem sempre ser formais e cuidadosos** — em notas e em slides, sem exceção para o formato mais itemizado do RevealJS. "Formal e cuidadoso" significa: toda igualdade algébrica escrita por extenso, sem passos telescopados ou notação inventada no meio do caminho (ex.: nunca escrever algo como `X^{TT}` esperando que o leitor infira "transposta da transposta" — escrever `(X^T)^T` e, se ajudar, nomear a regra usada); toda propriedade atribuída à entidade certa, nunca a outra parecida (ex.: **simetria é propriedade de uma matriz** — $A=A^T$ ou não — enquanto **ortogonalidade é propriedade de um conjunto de vetores** — perpendiculares entre si, ou não; são conceitos relacionados por um teorema, não sinônimos, e a prosa nunca deve escrever a frase de um jeito que sugira que "autovetor" pode "ser simétrico" ou que uma matriz pode "ser ortogonal" quando o que se quer dizer é outra coisa); e todo teorema citado com hipótese e tese completas, não uma versão resumida que omite quando ele se aplica. Um slide RevealJS pode dividir a mesma demonstração em mais fragmentos que a versão em prosa da nota, mas nunca pode reduzir o rigor — a mesma regra de "quantidade de informação quase igual" entre notas e slides (seção "Formato do arquivo de aula") vale com força total para definições/teoremas/provas especificamente, porque é ali que um corte "só para caber no slide" mais facilmente introduz um erro real, não só uma perda de nuance estilística.

**Todo resultado não óbvio precisa vir acompanhado do nome do teorema/referência e/ou de uma demonstração — nunca apresentado como se fosse evidente por si só.** Um resultado é "não óbvio" quando ele não segue diretamente, por definição, do que já foi dito — mesmo que pareça familiar ou intuitivo para quem já domina o assunto. Erro concreto que motivou esta regra: uma aula afirmava que um sistema homogêneo quadrado $B\mathbf{x}=\mathbf{0}$ tem solução não-trivial se, e somente se, $\det(B)=0$, citando apenas o critério de posto (posto incompleto $\iff$ solução não-trivial, já demonstrado em aula anterior) e pulando direto para $\det(B)=0$ sem nunca justificar a ponte entre "posto incompleto/singular" e "determinante zero" — essa ponte é, ela mesma, um teorema (não uma definição nem uma consequência imediata), e apareceu no texto como se fosse óbvia. Ao encadear uma equivalência que depende de mais de um resultado, cada elo do encadeamento precisa da sua própria justificativa: ou aponta o teorema exato (nome/número e página da fonte, no padrão de citação já usado na aula) que garante aquele elo, ou demonstra o elo diretamente. Isso vale tanto para resultados "conhecidos" de cursos anteriores quanto para os desta própria disciplina — se o link não foi provado ou citado dentro do material desta aula (ou de uma aula anterior já referenciável), ele não pode ser usado como se já estivesse disponível.
