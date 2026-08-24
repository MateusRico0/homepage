# Fontes usadas — Aula 4

> Mesmo padrão das aulas anteriores: fonte primária é `Teoria/Aula 4.tex`.
> Citações herdadas do material original, não reconferidas contra os PDFs
> nesta sessão.

### Fonte 1: `Teoria/Aula 4.tex` — "Decomposição e Responsabilidade"
**Uso pretendido:** aula inteira.

**Trecho — Classe Deus:**
> "O termo God Class (ou Objeto Onisciente) refere-se a uma classe que
> 'sabe demais' ou 'faz demais'. [...] transforma o que deveria ser um
> ecossistema de objetos colaborativos em um modelo procedural
> disfarçado."

**Trecho — SRP (Robert C. Martin):**
> "Uma classe deve ter uma, e apenas uma, razão para mudar. [...] Ref:
> Robert C. Martin, 'Agile Software Development, Principles, Patterns,
> and Practices'."

**Trecho — Teoria do Ator:**
> "A Atualização de Martin: 'Um módulo deve ser responsável perante um, e
> apenas um, ator.' [...] A verdadeira fonte de mudança em sistemas de
> software não são os algoritmos, mas as pessoas."

**Trecho — Injeção de Dependência:**
> "O Princípio de Hollywood: 'Não nos ligue, nós ligamos para você'. [...]
> Ref: \citeauthor{fowler2004inversion}, 'Inversion of Control Containers
> and the Dependency Injection pattern'."

**Trecho — LCOM:**
> "LCOM (Lack of Cohesion in Methods): [...] Se metade dos métodos usa o
> atributo A, e a outra metade usa apenas o atributo B, a classe não é
> coesa."

**Trecho — o lado sombrio do SRP:**
> "Cirurgia de Espingarda (Shotgun Surgery): Quando a separação é
> excessiva, implementar uma única regra de negócio exige que o
> desenvolvedor abra e modifique 15 classes minúsculas diferentes."

**Trecho — tipos de associação:**
> "Dependência (Uses-a): Vínculo temporário e fraco. Agregação (Has-a):
> Vínculo estrutural de todo-parte, mas com vidas independentes.
> Composição (Is-part-of): Vínculo estrutural vitalício e indissociável."

---

## Notas sobre as fontes

- Uma referência nova aparece aqui, fora dos 5 livros-base: Fowler,
  "Inversion of Control Containers and the Dependency Injection pattern"
  (citação pontual sobre DI, não um livro symlinkado em `_fontes/`).
- Os exemplos de código (`Pedido`, `RelatorioVendas`, `Funcionario`,
  `GestorDeUsuario`, `Carrinho`/`Produto`, `Cliente`/`Cartao`) foram
  reaproveitados quase literalmente do `.tex` original no `index.qmd`.
