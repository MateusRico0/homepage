## Resumo — Aula 4

Fonte: `_fontes/material/Teoria/Aula 4.tex` ("Decomposição e
Responsabilidade"). Depois de proteger o objeto (Aulas 1–2) e a
comunicação entre objetos (Aula 3), esta aula ataca um problema que nem
encapsulamento nem Lei de Demeter resolvem sozinhos: uma classe pode ter
o estado perfeitamente protegido e ainda assim fazer coisas demais (a
"Classe Deus"). Cobre SRP (com o "Teste do E", a Teoria do Ator de Robert
Martin, e a métrica LCOM), o risco oposto de fragmentação excessiva
(Cirurgia de Espingarda, Modelo Anêmico), os três tipos de associação
(Dependência/Agregação/Composição) e a Delegação como motor que torna a
composição tão poderosa quanto a herança.

**Pré-requisitos:** Aulas 1–3 completas (encapsulamento, máquina de
estados, interfaces, Lei de Demeter).

## Plano de aula — Aula 4 (carga horária: 140min)

1. **Abertura: a falsa sensação de segurança** (~10 min) — Encapsulamento
   e Demeter protegem *como* um objeto interage, não dizem *o que* ele
   deve fazer. Uma classe pode respeitar as duas regras e ainda ser uma
   "Classe Deus".
2. **A Classe Deus (`Pedido` com 5 responsabilidades)** (~15 min) —
   cálculo, imposto, formatação, persistência, e-mail, todos na mesma
   classe; os quatro problemas: fragilidade, acoplamento com
   infraestrutura, dificuldade de reuso, carga cognitiva.
3. **Coesão e acoplamento: as duas métricas de qualidade** (~15 min) —
   coesão = foco interno ("faça uma coisa e a faça bem"); acoplamento =
   vínculo externo; o santo graal: alta coesão, baixo acoplamento.
4. **SRP e o Teste do E** (~15 min) — "uma classe deve ter uma, e apenas
   uma, razão para mudar"; a heurística: se a frase que descreve a classe
   tem "E", ela tem responsabilidades demais.
5. **Refatoração: DI e delegação como cura** (~20 min) — extrair
   `ServicoEmail` e usar `Pagavel` (já visto na Aula 3); Injeção de
   Dependência via construtor; o ganho imediato: testabilidade (mocks),
   reuso, manutenibilidade.
6. **SRP avançado: a Teoria do Ator e a métrica LCOM** (~15 min) — a
   atualização de Robert Martin ("responsável perante um, e apenas um,
   ator"); LCOM como prova matemática de baixa coesão.
7. **O lado sombrio do SRP: fragmentação e anemia** (~15 min) — Cirurgia
   de Espingarda (uma mudança exige tocar 15 classes minúsculas); Modelo
   Anêmico como consequência do SRP levado ao fanatismo; a regra de
   equilíbrio: agrupe o que muda junto, pelos mesmos motivos.
8. **Tipos de Associação: Dependência, Agregação, Composição** (~20 min)
   — os três níveis de força estrutural, com exemplos do próprio projeto
   (`Carrinho`/`Produto`, `Cliente`/`Cartao`).
9. **Delegação: o motor da composição** (~15 min) — o `Cliente.pagar()`
   corrigindo a violação de Demeter da Aula 3; "Tell, Don't Ask" fechando
   o ciclo SRP + Associação + Delegação.
10. **Fechamento e ponte** (~5 min) — Ponte para a Aula 5: a delegação de
    hoje usou interfaces já prontas (`Pagavel`); a próxima aula formaliza
    a interface como contrato e introduz testes automatizados (JUnit).

## Fontes usadas — Aula 4

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

### Notas sobre as fontes

- Uma referência nova aparece aqui, fora dos 5 livros-base: Fowler,
  "Inversion of Control Containers and the Dependency Injection pattern"
  (citação pontual sobre DI, não um livro symlinkado em `_fontes/`).
- Os exemplos de código (`Pedido`, `RelatorioVendas`, `Funcionario`,
  `GestorDeUsuario`, `Carrinho`/`Produto`, `Cliente`/`Cartao`) foram
  reaproveitados quase literalmente do `.tex` original no `index.qmd`.
