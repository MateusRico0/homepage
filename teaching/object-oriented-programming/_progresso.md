# Progresso — Object-Oriented Programming

Estado aprovado + vocabulário, para manter a disciplina. O histórico de correções está no git (a versão longa anterior deste arquivo foi até o commit `1d4a4fc`).

**Status geral: disciplina completa.** As Aulas 1–14 cobrem todo o material de `_fontes/material/Teoria/` (`Revisão.tex` foi lido e não gerou aula nova).

**Fontes:** a fonte primária é o material já ministrado pelo professor (`_fontes/material/`, symlink para `Disciplinas/Programação Orientada a Objetos/1s2026/material`: LaTeX/Beamer, com `\begin{article}` para as notas e `\begin{frame}` para os slides). Livros-base, em symlinks: `weisfeld.pdf`, `bloch.pdf`, `metz.pdf`, `arnold-gosling.pdf`, `eckel.pdf`. Nunca copie PDFs para o repositório.
**Particularidades da disciplina:**
- **Aprovação:** o usuário dispensou a aprovação etapa a etapa nesta disciplina.
- **Código:** Java estático e proeminente, sem chunks executáveis.
- **Diagramas:** memória e estados em TikZ, com a paleta do IC.
- **Mapeamento:** o `index.qmd` tinha 12 Lessons esboçadas que não batiam 1:1 com os `.tex` reais; cada entrada foi redescrita conforme a aula foi construída.

## Estado das aulas

| Pasta | Aula | Fonte (`Teoria/`) | Estado |
|---|---|---|---|
| `aula01` | 1 — Paradigma OO e a máquina Java | `Aula 1.1.tex` + `1.2.tex` | publicada |
| `aula02` | 2 — O objeto como máquina de estados | `Aula 2.tex` | publicada |
| `aula03` | 3 — Composição de sistemas: contratos e estabilidade | `Aula 3.tex` | publicada |
| `aula04` | 4 — Decomposição e responsabilidade | `Aula 4.tex` | publicada |
| `aula05` | 5 — Acoplamento e contratos | `Aula 5.tex` | publicada |
| `aula06` | 6 — Interfaces e o contrato de comportamento | `Aula 6.tex` (1ª metade) | publicada |
| `aula07` | 7 — Polimorfismo, *binding* e generics | `Aula 6.tex` (2ª metade) | publicada |
| `aula08` | 8 — Herança: DNA, fragilidade e Template Method | `Aula 7.tex` (1ª metade) | publicada |
| `aula09` | 9 — Liskov e taxonomia de exceções | `Aula 7.tex` (2ª metade) | publicada |
| `aula10` | 10 — O colapso da herança e o padrão Strategy | `Aula 8.tex` (seções 1–4) | publicada |
| `aula11` | 11 — Vocabulário de padrões, imutabilidade e gênese segura | `Aula 8.tex` (final) + `Aula 9.tex` | publicada |
| `aula12` | 12 — State e Adapter | `Aula 9.tex`/`Aula 10.tex` | publicada |
| `aula13` | 13 — Decorator e Observer | `Aula 10.tex` | publicada |
| `aula14` | 14 — Síntese: núcleo estável, periferia volátil | `Aula 10.tex` (745–827) | publicada (encerramento, mais curta) |

**Exemplos-fio:** `Produto` do supermercado (Aulas 1–5), `Produto`/`ItemCarrinho` (composição) e, a partir da Aula 10, `Pedido` do e-commerce, que é purificado sucessivamente por Strategy, Builder, State, Decorator e Observer.

## Vocabulário (termos que as aulas seguintes usam sem redefinir)

| Termo | Aula |
|---|---|
| TRUE, custo de mudança, rigidez/fragilidade/imobilidade; estado/comportamento/identidade/encapsulamento; JVM/bytecode/JIT; Stack/Heap/GC; primitivo × referência | 1 |
| objeto como máquina de estados (DFA); Modelo Anêmico; invariante de classe; construtor Fail-Fast; CQS; Design by Contract; contrato `equals`/`hashCode` | 2 |
| sistema de objetos colaborando; Lei de Demeter | 3 |
| SRP, coesão (LCOM), composição via construtor | 4 |
| Inveja de Recursos, CBO, escala de Myers (conteúdo/comum/estampa/dados), GRASP Especialista, DIP | 5 |
| interface como contrato; métodos default/static/private ("Mutador Cego"); interface × classe abstrata; tipos como comportamento | 6 |
| polimorfismo, *late binding*, taxonomia de Cardelli-Wegner, binding estático × dinâmico, "fim do IF", OCP, generics | 7 |
| herança (`extends`), classe base frágil, classes abstratas, Template Method | 8 |
| VTable, LSP, taxonomia de exceções | 9 |
| ilusão da produtividade da herança, explosão combinatória, "favoreça composição", Strategy (Context/Strategy/ConcreteStrategy) | 10 |
| padrões GoF e as três famílias; Obsessão por Primitivos; Value Object; Builder; Factory Method | 11 |
| tríptico da estabilidade (dado, gênese, fluxo); State (≠ Strategy); Adapter; cegueira deliberada | 12 |
| Decorator (É-UM + TEM-UM, $2^N$); Observer; acoplamento de compilação × runtime | 13 |
| núcleo estável × periferia volátil; Regra de Ouro (a dependência aponta para o estável); acoplamento condicional/sintático/taxonômico/temporal | 14 |

## Pendências

- **Quantidade de testes:** Aulas 1–8 têm 12 testes (a regra é 6–10).
- **Nomes legados:** todas as aulas usam `_00-planejamento.md`/`_01-respostas.md`.
