# Fontes usadas — Aula 1

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

**Trecho — Espaço do Problema:**
> "A Orientação a Objetos (OO) propõe uma inversão radical dessa lógica. O
> foco primário passa a ser o 'Espaço do Problema'. [...] De acordo com
> \citeauthor{weisfeld2008object}, a grande vantagem técnica e cognitiva
> aqui é que os dados e os comportamentos que operam sobre eles estão
> unidos em uma única unidade ativa."

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

**Trecho — Alcançabilidade e GC Roots:**
> "O Garbage Collector (GC) do Java opera baseado na Teoria dos Grafos. Ele
> não rastreia o lixo, ele rastreia o que está vivo. O algoritmo parte de
> 'nós iniciais absolutos' chamados GC Roots. [...] Se um objeto [...] teve
> sua única variável de acesso destruída [...], o grafo se rompe. [...]
> Nesse momento, o objeto é declarado Inalcançável (Unreachable)."

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

**Trecho — passagem de parâmetros (a regra universal):**
> "A especificação oficial da linguagem Java dita que todos os parâmetros
> são passados por valor. [...] A confusão surge porque a natureza do
> 'valor' copiado é diferente dependendo do tipo de dado."

**Trecho — a prova da reatribuição:**
> "Se passássemos a própria variável por referência, atribuir um `new
> Produto()` ao parâmetro destruiria a ligação da variável original com a
> televisão antiga e a faria apontar para a geladeira nova. Contudo, como o
> método recebe apenas uma cópia da referência [...] A variável original
> (p) [...] continua segurando firme o endereço 0xFA."

---

## Notas sobre as fontes

- **Docker/DevContainer/Maven**, presentes na segunda metade de
  `Aula 1.2.tex`, foram deliberadamente deixados de fora do `index.qmd`
  final (ver nota de escopo no `_00-plano-aula.md`) — não são citados aqui
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
