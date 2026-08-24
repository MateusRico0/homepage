# Fontes usadas — Aula 2

> Mesmo padrão da Aula 1: fonte primária é `Teoria/Aula 2.tex` (material de
> aula do próprio professor). Citações aos livros-base foram herdadas como
> já estavam no material, não reconferidas contra os PDFs nesta sessão.

### Fonte 1: `Teoria/Aula 2.tex` — "Objetos como Máquinas de Estado"
**Uso pretendido:** aula inteira.

**Trecho — struct vs. agente ativo:**
> "A Orientação a Objetos inverte essa lógica. Em Java, a classe não
> apenas agrupa os dados, mas também contém as funções (métodos) que têm
> o direito de alterar esses dados. [...] Essa união indissociável entre
> dados e as regras que os governam é o que chamamos de encapsulamento
> forte \citep{bloch2008effective}."

**Trecho — Modelo Anêmico:**
> "O verdadeiro design rico (Rich Domain Model) exige que evitemos
> setters genéricos sempre que possível. A mudança de estado deve ser
> provocada por métodos verbais que denotem uma intenção clara de
> negócio (pagar(), enviar(), cancelar())."

**Trecho — DFA e o objeto:**
> "A grande revelação do Design Orientado a Objetos é que todo objeto bem
> projetado é a implementação física de uma Máquina de Estados
> Encapsulada. [...] Ref: Hopcroft, Motwani & Ullman, 'Introduction to
> Automata Theory, Languages, and Computation'."

**Trecho — construtor como base da indução:**
> "Base da Indução (n=0): O construtor C(args) tem o dever arquitetural
> de garantir que o novo objeto o satisfaça o ∈ V desde o seu primeiro
> milissegundo de vida na memória Heap. [...] Passo Indutivo (n ⟹ n+1):
> Dado um objeto que já se encontra em um estado sₙ ∈ V, qualquer método
> público m(sₙ) invocado sobre ele deve obrigatoriamente resultar em um
> estado subsequente sₙ₊₁ ∈ V."

**Trecho — CQS:**
> "O princípio CQS dita que qualquer método público de uma classe deve
> pertencer exclusivamente a um destes dois papéis [...] Ref:
> \citeauthor{meyer1988object}, 'Object-Oriented Software Construction' e
> \citeauthor{fowler2002patterns}."

**Trecho — kit de exceções (Bloch):**
> "\citet{bloch2008effective} defende fortemente a reutilização das
> exceções padrão do Java, pois elas fornecem um vocabulário universal
> que qualquer programador da equipe entenderá imediatamente."

**Trecho — equals/hashCode:**
> "Joshua Bloch no Effective Java explica que classes que representam
> 'Valores de Negócio' [...] exigem que o desenvolvedor sobrescreva o
> comportamento herdado da classe Object. [...] A regra fundamental aqui
> é o contrato inseparável entre o equals() e o hashCode()."

---

## Notas sobre as fontes

- Duas referências aparecem pela primeira vez nesta aula, fora dos 5
  livros-base já symlinkados em `_fontes/`: Hopcroft, Motwani & Ullman
  ("Introduction to Automata Theory...", citada só para a definição de
  DFA) e Meyer/Fowler (CQS, Design by Contract). Não foram adicionados
  PDFs para essas — são citações pontuais de uma ideia, não fontes
  usadas em profundidade ao longo da disciplina.
- O diagrama de estados do `Produto` (CADASTRADO/DISPONÍVEL/ESGOTADO) no
  `index.qmd` é uma adaptação em TikZ do diagrama já existente em
  `Aula 2.tex` (mesmos três estados e transições), recolorido com a
  paleta do IC.
