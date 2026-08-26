## Resumo — Aula 1

### Posição no curso

This lesson establishes the thesis that the remaining eleven lessons will elaborate: **every supervised algorithm is a distributional assumption, a likelihood, and a decision rule.** Lesson 1 makes all three visible at once, in the simplest possible setting — a single continuous feature on a bounded interval and two classes — so that later lessons can add dimensions, non-linearity, and optimization machinery without the student losing sight of the underlying structure.

The deliberate choice of a **one-dimensional** problem is what makes this possible: the decision boundary is a single number, the error probabilities are literal areas under two curves, and the trade-off between them can be drawn on the board rather than asserted.

### Pré-requisitos

Basic calculus (integration, change of variables), elementary probability (random variables, expectation, variance), and familiarity with Python and NumPy/SciPy. No prior exposure to machine learning is assumed.

### Objetivos de aprendizagem

- **ML Concept:** One-dimensional binary classification and outlier detection.
- **Statistical Concept:** Fitting continuous densities to bounded data (Beta distribution) and defining decision thresholds from low-probability regions. The unavoidable trade-off between Type I and Type II errors as a consequence of overlapping class-conditional densities.
- **Objectives:** Understand classification as a comparison between fitted densities, and thresholds as statistical decisions with explicit error costs.
- **Expected Competencies:** Ability to fit a Beta distribution to observed data, place a decision threshold based on tail probabilities, and quantify the resulting Type I and Type II error rates.

*(fonte: `../index.md`, Lesson 1)*

### Estratégia Pedagógica

**Estratégia A (Outside-In)** — classificação por comparação de
densidades é um modelo/procedimento concreto (não um idioma matemático
de fundação como espaços vetoriais ou derivadas), e a aula já abre
assim de fato: depois do preâmbulo obrigatório de Aula 1 ("Proposta do
Curso", necessário só por ser a primeira aula do semestre), o gancho
real é o exemplo concreto "duas populações, o formato que os dados
assumem" — deliberadamente sem fórmula, sem família nomeada — antes de
qualquer formalização de Beta, MLE ou limiar de decisão. **Adicionado
nesta revisão (2026-08-26)** para conformidade com a nova política de
`../../CLAUDE.md`; sem mudança de conteúdo no `index.qmd` — a aula já
seguia essa lógica, só faltava a declaração formal.

## Plano de aula — Aula 1 (carga horária: ~130min)

**Nota de reconciliação (adicionada ao revisar a aula já pronta).** A
sequência abaixo foi reescrita para refletir o `02-aula.qmd` real, que
diverge do roteiro originalmente rascunhado em dois pontos estruturais: (1)
a aula **não** abre com o exemplo de triagem médica — abre com um exemplo
abstrato de duas populações contínuas sem nome de família, e a triagem
médica só aparece depois, como **segunda** confirmação do mesmo fenômeno,
já com o Teorema de Bayes formalizado; (2) a regra da soma/produto e Bayes
formal e as propriedades gerais de distribuições contínuas (densidade vs.
probabilidade, momentos, caudas) foram acrescentadas como blocos novos.

**Segunda rodada de ajuste (decisão do usuário, após a primeira
reconciliação):** o catálogo de distribuições foi **cortado** (era a parte
menos amarrada à aula — nenhuma citação de página, pouco ligada ao fio
condutor Beta/anomalias); a comparação Gaussiana vs. $t$ de Student
sobrevive, mas encostada no bloco da Beta, como nota de robustez do ajuste,
não como bloco próprio; os antigos Blocos 6 e 7 (Beta + detecção de
anomalias) foram fundidos e simplificados — a Beta não é mais derivada em
detalhe (sem digama, sem exercício de normalização no quadro), e sim
tratada como algo que se ajusta chamando `scipy.stats.beta.fit`; em troca,
o bloco de custo cresceu para cobrir teoria da decisão por completo,
incorporando matriz de confusão / precisão / recall / ROC, que estavam na
leitura obrigatória (`01-fontes.md`) mas nunca tinham sido escritos na aula.

**Terceira rodada:** tempo total ~130 min, acima da sessão de 100 min
original — **aprovado pelo usuário** aceitar a aula mais longa em vez de
cortar mais ou dividir em duas sessões.

Timings são proporções, não compromissos.

*(Cada item abaixo corresponde ao "Bloco N" citado em `01-fontes.md`, com
N = posição na lista menos 1 — item 1 = Bloco 0, item 2 = Bloco 1, etc.)*

1.  **Bloco 0 — Abertura: a tese do curso** (~5 min) — "Proposta do Curso": a tese de
    que todo algoritmo supervisionado é suposição distributiva +
    verossimilhança + regra de decisão; formulação estatística mínima do
    aprendizado ($p(x,y)$, amostra $\mathcal{D}$, classificação vs.
    regressão); bibliografia (PRML + DLFC); pergunta de abertura — "o que
    significa 'aprender a distribuição dos dados'?".

2.  **Duas populações sem nome, e onde cortar** (~20 min) — "O que é uma
    distribuição" (formato dos dados, sem fórmula ainda) → "Classificação e
    o problema do corte" (limiar no cruzamento das curvas — a resposta que
    a turma dá) → "Tipos de erros" (Tipo I/II, exigência de hipótese nula,
    erro de Bayes irredutível) → "A conta que desmente a intuição" (as
    classes não são igualmente frequentes; contagem empírica mostra que o
    corte no cruzamento perde). Termina com a fronteira "óbvia" desmentida
    pelos dados — o Bloco 3 resolve.

3.  **Regra da soma, regra do produto e Teorema de Bayes** (~15 min, novo) —
    Formalização de conjunta $p(x,\mathcal{C}_k)$, condicional
    $p(x\mid\mathcal{C}_k)$/$p(\mathcal{C}_k\mid x)$, e marginal $p(x)$
    (PRML §1.2, pp. 14–24; DLFC §2.1.2, pp. 26–28). Derivação do Teorema de
    Bayes a partir da regra do produto, com leitura dos quatro papéis
    (priori, verossimilhança, evidência, posteriori).

4.  **A correção pela priori, a prova de otimalidade, e a triagem médica**
    (~20 min) — "A importância da priori e Bayes": por que o corte no
    cruzamento falhou — as curvas descrevem cada classe isoladamente, não a
    posteriori. Correção: escalar cada curva pela priori $\pi_k$ e cortar
    no cruzamento das **conjuntas**. Prova de que esse cruzamento minimiza
    $p(\text{erro})$ (PRML eqs. 1.78–1.79, pp. 39–40; Figura 1.24, p. 40;
    §1.5.1, pp. 39–41) — o argumento é ponto a ponto e não usa nenhuma
    família paramétrica. Em seguida, "Exemplo: triagem médica" (DLFC
    §2.1.1, pp. 25–26, revisitado em §2.1.4, p. 30) como **segunda**
    aparição do mesmo fenômeno, agora no caso discreto: sensibilidade 90%,
    falso positivo 3%, prevalência 1%, posteriori ≈23%.

5.  **Propriedades de distribuições contínuas** (~12 min) — Densidade vs.
    probabilidade (DLFC §2.2, pp. 32–33): a densidade pode exceder 1;
    mudança de variável exige Jacobiano, e por isso a moda não é invariante
    a reparametrizações (mas a decisão $\arg\max_k p(\mathcal{C}_k\mid x)$
    é). Momentos e comportamento de cauda — vocabulário mínimo, usado no
    bloco seguinte para a nota de robustez, não para um catálogo.

6.  **A Beta como ferramenta, e detecção de anomalias com uma classe**
    (~18 min) — Tratar a Beta $\text{Beta}(x \mid a, b)$ (PRML eq. 2.13,
    p. 71) como **ferramenta**, não como objeto a derivar: suporte em
    $[0,1]$ é decisão de modelagem; dois parâmetros cobrem formas em U,
    uniforme, e unimodal assimétrica (PRML Figura 2.2, p. 72); ajusta-se
    chamando `scipy.stats.beta.fit`. Duas armadilhas práticas continuam
    merecendo tempo: zeros/uns exatos quebrando o ajuste, e a nota de
    robustez Gaussiana vs. $t$ de Student. Em seguida, o cenário sem
    anomalias rotuladas: ajustar a Beta só aos dados normais; limiar como
    quantil do modelo. **O ponto central da aula:** com uma única densidade
    ajustada, o erro Tipo II não está definido — "três saídas honestas".

7.  **Teoria da decisão: custo, avaliação e rejeição** (~35 min, ampliado) —
    Cobre teoria da decisão de ponta a ponta: (a) matriz de perda e
    fronteira ótima sob custo assimétrico (PRML §1.5.2, p. 41; DLFC §5.2.2,
    p. 140); (b) matriz de confusão, precisão, recall, taxa de falso
    positivo (DLFC §5.2.5, pp. 147–148); (c) curva ROC (DLFC §5.2.6, pp.
    148–150) como o mesmo gráfico do Bloco 1 replotado; (d) opção de
    rejeição (PRML §1.5.3, p. 42), regra de Chow.

8.  **Fechamento e ponte** (~5 min) — Três frases de resumo (distribuição =
    formato; classificar = comparar formatos ponderados pela priori;
    limiar = decisão com custo explícito) mais o ponto negativo (com uma
    densidade, só o Tipo I é calculável). Ponte para a Aula 2: em $d$
    variáveis, $p(x\mid\mathcal{C}_k)$ exige $M^d$ células de histograma —
    inestimável sem estrutura — e o Naive Bayes é a primeira suposição
    estrutural do curso.

---

### Derivações para o quadro

Com a simplificação da Beta (Bloco 6), as derivações da própria Beta
(normalização, média/variância) não são mais feitas no quadro — ficam como
leitura opcional (ver Exercícios Sugeridos). O que fica no quadro é a
cadeia de teoria da decisão, já que é o ponto da aula agora:

1.  **A fronteira de má-classificação mínima** como o cruzamento das
    densidades conjuntas (PRML eqs. 1.78–1.79, pp. 39–40).
2.  **Como a fronteira se move sob uma matriz de perda assimétrica** —
    modificação de duas linhas da derivação 1 que muda completamente a
    resposta prática.
3.  **Por que a curva ROC é o mesmo sweep do gráfico Tipo I/Tipo II do
    Bloco 2** — mesmo limiar, mesmas duas quantidades, só replotadas como
    (FPR, TPR) em vez de duas curvas contra $t$. Vale fazer explicitamente
    uma vez no quadro, para não parecer um objeto novo.

### Laboratório computacional

Um único notebook, executado na segunda metade da aula ou atribuído
imediatamente depois:

1.  Simular (ou carregar) um atributo limitado para duas populações;
    plotar histogramas contra densidades Beta ajustadas.
2.  Ajustar por método dos momentos e por MLE numérica
    (`scipy.stats.beta.fit`); comparar as estimativas e discutir a
    discrepância.
3.  Calcular as taxas de erro Tipo I e Tipo II analiticamente via
    `scipy.stats.beta.cdf` e verificar empiricamente por simulação.
4.  Varrer o limiar, plotar a curva ROC, e marcar três pontos de operação:
    erro total mínimo, orçamento de alarme falso fixo de $\alpha=0.05$, e o
    ponto de perda esperada mínima sob assimetria de custo 10:1.
5.  Repetir o passo 4 com uma priori fortemente desbalanceada e observar
    como o limiar ótimo e a curva ROC respondem diferente — a ROC é
    invariante à priori da classe, o ponto de operação escolhido não é.

O passo 5 é o retorno intelectual do laboratório e não deve ser cortado.

### Exercícios sugeridos

*   **PRML 2.5** (p. 128) — normalização da Beta. *Opcional agora que a
    derivação não é feita em aula* (simplificação do Bloco 6) — para quem
    quiser a mecânica.
*   **PRML 2.6** (p. 129) — média, variância e moda da Beta. Mesmo status:
    opcional.
*   **PRML 1.24** (p. 64) — perda esperada mínima com opção de rejeição, e
    a relação entre o custo de rejeitar e o limiar de rejeição.
*   **Exercício do curso:** dadas duas Betas ajustadas e uma razão de
    custo, resolver numericamente o limiar ótimo e mostrar que ele coincide
    com o ponto de tangência na curva ROC.

### Notas de condução e armadilhas comuns

*   **Densidades não são probabilidades.** Espere pelo menos um aluno
    incomodado com uma densidade Beta passando de 1.
*   **Zeros e uns exatos quebram a verossimilhança da Beta** quando
    $a<1$ ou $b<1$. Mencionar *clipping* e modelos zero/one-inflated como
    correções honestas; não deixar os alunos descobrirem isso em silêncio
    no laboratório.
*   **A distinção Beta-como-priori vs. Beta-como-modelo-de-dados** vai
    confundir quem ler PRML §2.1.1 sem aviso.
*   **Conjunta vs. condicional de classe** na Figura 1.24 do PRML — repetir
    isso pelo menos duas vezes.
*   **"Tipo I" e "Tipo II" exigem uma hipótese nula declarada.** Anunciar a
    convenção antes de usar os termos.
*   Resistir à tentação de introduzir a razão de verossimilhanças
    formalmente aqui — ela aterrissa melhor na Aula 2, já no caso
    multidimensional.
*   **Não deixar o Bloco 7 parecer três tópicos soltos.** Declarar
    explicitamente, antes de começar, que limiar sensível a custo, matriz
    de confusão e ROC são três vistas do *mesmo* objeto de sweep de limiar
    introduzido no Bloco 2.
*   **A simplificação da Beta é deliberada, não um atalho por pressa de
    tempo.** Se um aluno pedir a derivação da MLE, apontar para os
    Exercícios PRML 2.5/2.6 como leitura opcional em vez de derivar ao
    vivo.
