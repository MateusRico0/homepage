## Resumo — Aula 1

Aula 1 funde as duas sessões teóricas originais do curso ("Aula Teórica 1.1 —
O Paradigma Orientado a Objetos" e "Aula Teórica 1.2 — Orientação a Objetos
em Java", em `_fontes/material/Teoria/Aula 1.1.tex` e `Aula 1.2.tex`) numa
única aula do site, mantendo a mesma sequência de conteúdo e os mesmos
exemplos (o `Produto` do supermercado). Cobre a tese central do curso —
software é feito para mudar, e o design orientado a objetos existe para
manter esse custo de mudança baixo — e desce da teoria (paradigma,
encapsulamento) até a mecânica concreta da linguagem Java (JVM, memória,
sintaxe de classe, `this`, passagem de parâmetros).

**Pré-requisitos:** nenhum conhecimento prévio de POO; espera-se familiaridade
com programação procedural básica (variáveis, funções, estruturas de
controle), em qualquer linguagem.

**Objetivos de aprendizagem** (fonte: `../index.qmd`, Lesson 1):
- **OOP Concept:** o ecossistema Java (JVM, Bytecode), memória Stack vs.
  Heap, e a anatomia física de uma classe.
- **Design Concept:** abstrair o mundo real em estado e comportamento; a
  diferença entre classe (o molde) e objeto (a instância em memória);
  introdução à modelagem estrutural.
- **Objectives:** entender as restrições físicas do ambiente de execução e
  como traduzir entidades do mundo real em blueprints de código.
- **Expected Competencies:** definir uma classe, instanciar objetos na Heap,
  e explicar por que a JVM garante portabilidade.

**Estratégia Pedagógica:** Estratégia B (Inside-Out com Problema-Fio) — a
aula parte da necessidade do idioma orientado a objetos (design, encapsulamento)
e desce até o mecanismo concreto da linguagem Java, usando o `Produto` do
supermercado como problema-fio.

## Plano de aula — Aula 1 (carga horária: ~140min, sessão dupla)

1.  **Bloco 0 — Abertura: por que o design importa** (~10 min) — A
    inevitabilidade da mudança de software; o acrônimo **TRUE** (Transparent,
    Reasonable, Usable, Exemplary) de Sandi Metz como critério do que é um
    bom design; rigidez, fragilidade e imobilidade como sintomas de design
    pobre. Fecha com a tese: design não é sobre como o software funciona, é
    sobre como ele muda.

2.  **A mudança de paradigma: do procedural ao orientado a objetos** (~15
    min) — Paradigma procedural (dados e função separados, risco de efeito
    colateral em dados globais) vs. Espaço do Problema (dados e comportamento
    unidos numa entidade coesa). Exemplo condutor: o desconto no
    e-commerce — a visão procedural (preço como número passivo) contra a
    visão orientada a objetos (`Produto` como agente que recebe uma
    mensagem "aplique um desconto").

3.  **Estado, Comportamento, Identidade e Encapsulamento** (~15 min) — As
    três propriedades que fazem de algo um objeto; a "caixa preta" e o
    Information Hiding como estratégia de engenharia (não de segurança);
    por que ocultar implementação reduz acoplamento e protege contra o
    efeito cascata de mudanças.

4.  **Classe vs. Objeto** (~10 min) — A classe como planta baixa/contrato; o
    objeto como a materialização física na Heap; a classe também vive na
    memória (Metaspace/Method Area, carregada pelo `ClassLoader`) — ponto
    técnico que costuma confundir quem vem do procedural.

5.  **A infraestrutura Java: JVM, Bytecode e JIT** (~15 min) — Compilação em
    duas etapas (`javac` → bytecode → JVM); Write Once, Run Anywhere; o
    compilador JIT identificando *hotspots* e compilando-os para código
    nativo em tempo de execução — por que "bytecode interpretado" não
    significa "lento" em aplicações de longa duração.

6.  **Memória: Stack, Heap e o Coletor de Lixo** (~15 min) — A ilusão da
    destruição (fim de escopo mata o ponteiro, não o objeto); o grafo de
    alcançabilidade e as *GC Roots*; retenção obsoleta de objetos
    ("zumbis") em coleções estáticas como a versão real de vazamento de
    memória em Java; recursos do S.O. (arquivos, conexões) exigem
    fechamento determinístico via `try-with-resources`, porque o GC não
    cuida deles.

7.  **A anatomia de uma classe em código: o exemplo `Produto`** (~20 min) —
    Nome, atributos privados, construtor que garante nascimento válido,
    acessores como único caminho de mutação, interface pública vs.
    implementação privada. Construção incremental do exemplo (nome/comentário
    → estado/construtor → acessores/interface → métodos privados), cada
    passo mostrando o código real.

8.  **Modificadores de acesso e a palavra-chave `this`** (~15 min) —
    `public` como promessa, `private` como segredo aplicado pelo
    compilador; o problema do sombreamento (parâmetro e atributo com o
    mesmo nome) e como `this` resolve a ambiguidade indo da Stack para a
    Heap.

9.  **Primitivos vs. Referências: a mecânica de passagem de parâmetros**
    (~20 min) — Bloco central da aula do ponto de vista da causa mais comum
    de bugs para iniciantes: em Java, tudo é passado por valor, mas o
    "valor" de uma variável de referência é o endereço, não o objeto. Dois
    diagramas (adaptados do material original) mostrando a cópia de um
    primitivo (isolamento total) vs. a cópia de uma referência (mesmo
    objeto, dois "controles remotos"); a prova da reatribuição (por que
    `prod = new Produto(...)` dentro de um método não afeta a variável de
    quem chamou).

10. **Fechamento e ponte** (~5 min) — Recapitular a tese do Bloco 0 à luz de
    tudo que foi visto; ponte para a Aula 2: encapsulamento foi apresentado
    aqui como princípio e como sintaxe (`private`); a Aula 2 aprofunda como
    o **construtor** vira o guardião da integridade do objeto (invariantes,
    *fail-fast*) — o mesmo `Produto` desta aula ganhará validação real.

**Nota de escopo:** a infraestrutura de automação (Docker, DevContainer,
Maven), presente na `Aula 1.2.tex` original, foi deliberadamente reduzida a
uma nota breve de uma frase antes do fechamento — é conteúdo de ambiente de
desenvolvimento, não de Orientação a Objetos propriamente, e não tem
paralelo nas outras 9 aulas do curso (aparece só aqui). Fica registrado
como corte consciente, não esquecimento.

**Diferença desta disciplina em relação às outras já publicadas no site:**
sem chunks de código Python/Jupyter (não há execução de código nesta
disciplina) — os exemplos são blocos de código Java estáticos, com
destaque de sintaxe, como já eram no material original em LaTeX/Beamer.
Diagramas de memória (Stack/Heap) usam TikZ, adaptados dos originais.

## Fontes usadas — Aula 1

> Diferente das outras disciplinas deste projeto, a fonte primária aqui não
> é um livro de terceiros: é o material de aula já ministrado pelo próprio
> professor (`_fontes/material/Teoria/Aula 1.1.tex` e `Aula 1.2.tex`,
> símlink para `Disciplinas/Programação Orientada a Objetos/1s2026/material`).
> Os trechos abaixo são citados literalmente desses arquivos `.tex`. As
> citações que esses arquivos fazem aos 5 livros-base (Metz, Weisfeld,
> Bloch, Gosling & Holmes & Arnold, Eckel) foram herdadas como já estavam no
> material original — **não foram reconferidas página a página contra os
> PDFs nesta sessão**, diferente do padrão de offset-verificado usado nas
> outras disciplinas. Se algum dia for necessário citar página exata de um
> desses livros, isso ainda precisa ser feito.

### Fonte 1: `Teoria/Aula 1.1.tex` — "O Paradigma Orientado a Objetos"
**Uso pretendido:** Blocos 0–3 (TRUE, mudança de paradigma, encapsulamento, classe vs. objeto).

**Trecho — o acrônimo TRUE:**
> "O objetivo primordial do design orientado a objetos é garantir que o
> custo de mudança permaneça baixo e constante ao longo do tempo. Para
> isso, o código deve possuir características que \citet{metz2013practical}
> define pelo acrônimo TRUE: Transparent (as consequências de uma mudança
> devem ser óbvias); Reasonable (o custo de qualquer mudança deve ser
> proporcional ao benefício que ela traz); Usable (o código deve ser
> reutilizável em novos contextos); Exemplary (o código deve encorajar quem
> o modifica a manter as mesmas diretrizes de design)."

---

**Trecho — Espaço do Problema:**
> "A Orientação a Objetos (OO) propõe uma inversão radical dessa lógica. O
> foco primário passa a ser o 'Espaço do Problema'. [...] De acordo com
> \citeauthor{weisfeld2008object}, a grande vantagem técnica e cognitiva
> aqui é que os dados e os comportamentos que operam sobre eles estão
> unidos em uma única unidade ativa."

---

**Trecho — Encapsulamento:**
> "Segundo \citeauthor{weisfeld2008object}, esse conceito deriva do
> Princípio do Ocultamento de Informação (Information Hiding). Ocultar os
> dados não é uma medida de segurança contra 'hackers', mas sim uma medida
> de engenharia contra a fragilidade do próprio código."

---

### Fonte 2: `Teoria/Aula 1.2.tex` — "Orientação a Objetos em Java"
**Uso pretendido:** Blocos 4–9 (JVM/JIT, memória/GC, anatomia da classe em código, modificadores de acesso, `this`, primitivos vs. referências).

**Trecho — JVM e portabilidade:**
> "O processo de compilação em Java ocorre em duas etapas distintas.
> Primeiro, o compilador estático (javac) transforma o código-fonte legível
> (.java) em Bytecode (.class). [...] Segundo, no momento da execução, a
> JVM atua como um motor, lendo esse bytecode e mapeando-o para as
> instruções nativas do ambiente hospedeiro."

---

**Trecho — Alcançabilidade e GC Roots:**
> "O Garbage Collector (GC) do Java opera baseado na Teoria dos Grafos. Ele
> não rastreia o lixo, ele rastreia o que está vivo. O algoritmo parte de
> 'nós iniciais absolutos' chamados GC Roots. [...] Se um objeto [...] teve
> sua única variável de acesso destruída [...], o grafo se rompe. [...]
> Nesse momento, o objeto é declarado Inalcançável (Unreachable)."

---

**Trecho — o exemplo `Produto` (anatomia da classe):**
> "/** Representa um item comercializavel no mercado. */
> public class Produto {
>     private String nome;
>     private double preco;
>     public Produto(String nome, double preco) {
>         this.nome = nome;
>         this.setPreco(preco); // Usa accessor para validar
>     }
>     public void setPreco(double p) { if (p >= 0) this.preco = p; }
>     public double getPreco() { return this.preco; }
>     public void aplicarDesconto(double pct) {
>         if (isDescontoAceitavel(pct)) {
>             this.preco -= calcularAbatimento(pct);
>         }
>     }
>     private boolean isDescontoAceitavel(double p) { return p > 0 && p < 50; }
>     private double calcularAbatimento(double p) { return this.preco * (p/100); }
> }"

---

**Trecho — passagem de parâmetros (a regra universal):**
> "A especificação oficial da linguagem Java dita que todos os parâmetros
> são passados por valor. [...] A confusão surge porque a natureza do
> 'valor' copiado é diferente dependendo do tipo de dado."

---

**Trecho — a prova da reatribuição:**
> "Se passássemos a própria variável por referência, atribuir um `new
> Produto()` ao parâmetro destruiria a ligação da variável original com a
> televisão antiga e a faria apontar para a geladeira nova. Contudo, como o
> método recebe apenas uma cópia da referência [...] A variável original
> (p) [...] continua segurando firme o endereço 0xFA."

---

### Notas sobre as fontes

- **Docker/DevContainer/Maven**, presentes na segunda metade de
  `Aula 1.2.tex`, foram deliberadamente deixados de fora do `index.qmd`
  final (ver nota de escopo no "Plano de aula" acima) — não são citados aqui
  como fonte usada.
- Os diagramas TikZ de primitivos vs. referências em `index.qmd` são
  adaptações diretas dos `tikzpicture` já existentes em `Aula 1.2.tex`
  (mesma estrutura lógica: variável original → cópia → objeto/valor),
  recoloridos com a paleta do IC do projeto em vez das cores originais do
  material (`blue!10`/`red!10`/`green!10`).
- Os 20 blocos de V/F (3 itens cada) e as 18 questões discursivas somadas
  de `Aula 1.1.tex` + `Aula 1.2.tex` foram a base de onde os 12 blocos de
  4 itens e as 3 discursivas do `index.qmd` foram selecionados/adaptados —
  ver seção de Exercícios do `index.qmd` para a curadoria final.
