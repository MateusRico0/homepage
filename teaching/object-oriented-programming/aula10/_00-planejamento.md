## Resumo — Aula 10

Fonte: `_fontes/material/Teoria/Aula 8.tex` (1115 linhas — arquivo
completo, ao contrário das Aulas 8–9, que dividiram `Aula 7.tex` ao
meio). Esta aula cobre as quatro primeiras seções reais do `.tex`: (1)
**A Ilusão e o Custo da Herança** — a fusão estrutural do `extends`, a
"ilusão da produtividade" (herdar só para ganhar métodos de graça), o
acoplamento estrutural como o vínculo mais rígido da OO, a distinção
Herança de Estado vs. Comportamento, e o peso físico da herança de
estado na Heap (a "Subclasse Gorda"); (2) **O Colapso da Hierarquia** —
um cenário de e-commerce onde dois eixos de variação de negócio
(Logística: Físico/Digital; Fiscalidade: Nacional/Importado) forçam uma
explosão combinatória de subclasses, e a proibição de herança múltipla
de classes em Java (Problema do Diamante) fecha qualquer saída por
herança; (3) **A Era da Composição e Modularidade** — o princípio do GoF
("favoreça composição sobre herança"), a virada de *is-a* para *has-a*,
a teoria da quase-decomponibilidade de Herbert Simon, a analogia
eletrodoméstico integrado vs. modular, testabilidade/desenvolvimento
paralelo, e os tipos de composição (Agregação vs. Associação) com o
princípio do Especialista da Informação; (4) **O que fazer então?** — o
labirinto de `if/else` para meios de pagamento, a tentativa fracassada
de resolver por herança (`PedidoPix`/`PedidoCartao`, confundindo
identidade com papel), e a resolução via padrão **Strategy**
(interface `Pagavel`, injeção de dependência, delegação, topologia
Context/Strategy/ConcreteStrategy, Late Binding/VTable revisitado, e o
Princípio Aberto/Fechado em ação).

**Pré-requisitos:** Aula 7 (Late Binding, VTable, polimorfismo de
inclusão), Aula 8 (Herança como fusão de DNA, critério herança-vs-
composição: DNA + necessidade polimórfica, Problema da Classe Base
Frágil via o exemplo `GerenciadorDeCobrancas`/bug de contagem dupla,
interface `Pagavel` com `Pix`/`Cartao`/`Boleto` como **subclasses** de
`MeioPagamentoBase`), Aula 9 (LSP, substituibilidade, taxonomia de
exceções). O dicionário de notações já traz "É-UM"/DNA, VTable/Late
Binding, e a interface `Pagavel` com implementações `Pix`/`Cartao`/
`Boleto` — só que, nas Aulas 8–9, essas três classes eram tratadas como
especializações **por herança**; esta aula usa deliberadamente a mesma
família de classes (`Pagavel`, `Pix`, `Cartao`, `Boleto`) para mostrar a
alternativa **por composição** (Strategy), fechando o contraste em vez
de introduzir um domínio novo.

**Decisão de escopo (divide em aula10 + aula11 futura):** `Aula 8.tex`
tem 1115 linhas — comparável em tamanho aos arquivos `Aula 6.tex` e
`Aula 7.tex`, que já haviam sido divididos em duas aulas do site cada.
As quatro seções cobertas nesta aula (Ilusão/Custo da Herança → Colapso
da Hierarquia → Composição/Modularidade → Strategy) formam um arco
fechado com começo, meio e fim: um problema concreto (explosão
combinatória), o princípio que o resolve (composição) e a solução de
engenharia nomeada (Strategy). Estimando ~10 min de abertura + 6 blocos
de conteúdo (15–25 min cada) + ~10 min de fechamento, o total fica em
~125–135 min, dentro da faixa 90–140 já calibrada pelas 9 aulas
publicadas — não é necessário nem recomendável espremer as duas seções
finais do `.tex` (`Padrões de Projeto`, linhas 806–917, e `Conclusão`,
linhas 917–943) neste mesmo arquivo. Essas duas seções restantes —
origem histórica dos padrões (Christopher Alexander), o marco GoF de
1994, o que padrões NÃO são, o vocabulário arquitetural/linguagem
ubíqua, e a visão geral das três famílias (Criação/Estrutural/
Comportamento) — ficam para uma **Aula 11** futura, que também deve
absorver a atualização das Lessons 10/11 do esboço genérico da
disciplina (`Creational and Structural Patterns` / `Behavioral
Patterns`), já que o conteúdo real não separa os padrões dessa forma:
Strategy (comportamental) já é ensinado nesta Aula 10, então a Aula 11
cobre a visão panorâmica das três famílias, não uma família isolada.
**Nada do `.tex` fica de fora do arco Herança→Composição→Strategy**:
apenas as duas seções finais (vocabulário geral de padrões) migram para
a Aula 11.

**Estratégia Pedagógica:** Estratégia B (Inside-Out com Problema-Fio) —
o problema-fio é o sistema de e-commerce evoluindo em eixos de negócio
independentes (logística, fiscalidade, meio de pagamento): primeiro a
herança tenta resolver cada eixo e colide consigo mesma (o Colapso da
Hierarquia), depois a composição resolve exatamente o mesmo problema
sem colisão (o Strategy). Não é uma aula de "modelo/algoritmo" isolado
(o que pediria Estratégia A) — é a evolução de uma única linguagem de
modelagem (herança) sendo abandonada em favor de outra (composição)
diante da mesma necessidade de negócio.

## Plano de aula — Aula 10 (carga horária estimada: ~130min)

1. **Abertura: Revisão e Introdução** (~10 min) — revisão de Herança
   (Aula 8: DNA + necessidade polimórfica) e LSP/substituibilidade
   (Aula 9); ideia-ponte: herança modela muito bem *um* eixo de
   variação — o que acontece quando o negócio tem *dois ou mais* eixos
   independentes ao mesmo tempo? Roteiro explícito (4 perguntas);
   problema motivador com o e-commerce evoluindo.
2. **A Fusão Estrutural e o Peso da Herança de Estado** (~18 min) — a
   promessa do *is-a*, a "ilusão da produtividade" (`PedidoInternacional
   extends Pedido` só para ganhar métodos de graça), o acoplamento
   estrutural como o vínculo mais rígido da OO, Herança de Estado
   (rígida, `protected double saldo`) vs. Herança de Comportamento
   (fluida, interfaces), e o peso físico na Heap — a "Subclasse Gorda"
   (`Ebook extends ProdutoBase`, carregando `pesoFisico`/
   `dimensoesPacote` que nunca usa). Referência breve (não re-explicada
   em profundidade) à Classe Base Frágil já vista na Aula 8.
3. **O Colapso da Hierarquia: Explosão Combinatória** (~22 min) — a
   classe `Produto` limpa inicial, a primeira especialização
   (`ProdutoFisico`/`ProdutoDigital`), o novo requisito fiscal
   (Nacional/Importado) sem lugar honesto na árvore, a explosão
   forçada (`FisicoNacional`, `FisicoImportado`, `DigitalNacional`,
   `DigitalImportado` — e um terceiro eixo levaria a 8), diagrama TikZ
   da matriz de explosão; a tentativa de herança múltipla
   (`extends ProdutoFisico, ProdutoImportado`) e por que Java proíbe
   (Problema do Diamante), diagrama TikZ da bifurcação impossível; o
   diagnóstico — herança serve para taxonomia estrita e imutável, não
   para *features* que variam de forma independente. **Pausa ativa 1.**
4. **A Era da Composição: Princípio, *Is-a* para *Has-a* e
   Quase-Decomponibilidade** (~15 min) — a regra de ouro do GoF
   ("favoreça composição sobre herança"), por que ela preserva
   encapsulamento e permite flexibilidade dinâmica; a mudança de
   *is-a* (identidade fixa) para *has-a* (orquestrador delegando a
   especialistas); a teoria de Herbert Simon (sistemas complexos são
   hierarquias quase-decomponíveis, elos internos fortes e elos
   externos fracos); a analogia do eletrodoméstico integrado (TV/VCR)
   vs. modular (som), aplicada à troca de API de uma transportadora.
5. **Tipos de Composição e Fronteiras de Domínio** (~15 min) —
   Agregação (Todo-Parte, `Carrinho`/`Produto`, ciclos de vida
   independentes) vs. Associação (colaboração livre, `Cliente`/
   `CartaoDeCredito`); testabilidade cirúrgica e desenvolvimento
   paralelo como payoffs concretos da composição; o princípio do
   Especialista da Informação e o risco de misturar domínios
   (`Produto` não deve mandar e-mail nem gerar PDF). **Pausa ativa 2.**
6. **O Desafio do Checkout: do Labirinto de Condicionais à Herança
   Fracassada** (~15 min) — o novo requisito (Pix/Cartão/Boleto no
   checkout); a abordagem ingênua (`if/else` dentro de
   `processarPagamento`, *code smell*, falta de coesão, fragilidade
   cruzada); a tentativa por herança (`PedidoPix extends Pedido`,
   `PedidoCartao extends Pedido`) e por que ela confunde identidade
   (o que o Pedido *é*) com papel (o que ele *usa*
   temporariamente) — o aprisionamento estático quando o cliente muda
   de meio de pagamento no último segundo.
7. **O Padrão Strategy: Composição, Delegação e o Princípio
   Aberto/Fechado** (~25 min) — a interface `Pagavel` como fronteira do
   contrato; injeção de dependência (construtor/setter) trocando a
   herança rígida por uma peça acoplável em tempo de execução;
   execução via delegação (`Pedido` pede, `Pagavel` executa); a
   topologia formal do GoF (Context/Strategy/ConcreteStrategy),
   diagrama TikZ; recapitulação breve de Late Binding/VTable já visto
   nas Aulas 7 e 9, agora aplicado à escolha de estratégia; o OCP em
   ação — adicionar `PagamentoCriptomoeda` sem tocar em `Pedido`.
   **Pausa ativa 3.**
8. **Fechamento** (~10 min) — retomar as 4 perguntas da abertura; ponte
   para a Aula 11 (o vocabulário geral de Padrões de Projeto: origem
   histórica, o marco GoF, o que padrões NÃO são, e as três famílias —
   Criação/Estrutural/Comportamento — vistas de cima, já que Strategy,
   um representante comportamental, acabou de ser construído em
   detalhe).

## Fontes usadas — Aula 10

### Fonte 1: `Teoria/Aula 8.tex`, linhas 54–56 e 60–69 (a fusão estrutural e a ilusão da produtividade)

**Uso pretendido:** abrir o Bloco 2, ancorando a promessa do *is-a* e o
erro semântico de herdar só por conveniência.

**Trecho:**
> "Quando declaramos que B extends A, não estamos apenas permitindo que
> B utilize métodos de A; estamos fundindo as estruturas de ambas as
> classes em uma única entidade lógica, compartilhando o mesmo 'DNA'."

**Trecho — ilusão da produtividade:**
> "É profundamente tentador utilizar a palavra-chave extends unicamente
> para 'ganhar' métodos prontos e evitar a duplicação de lógica [...]
> Essa 'Ilusão da Produtividade' esconde um erro semântico grave. O uso
> de extends puramente para reaproveitamento de código é uma violação
> arquitetural."

---

### Fonte 2: `Teoria/Aula 8.tex`, linhas 117–124 e 128–139 (Herança de Estado vs. Comportamento; a Subclasse Gorda)

**Uso pretendido:** fundamentar a distinção estado/comportamento e o
exemplo de custo físico de memória do Bloco 2.

**Trecho:**
> "Herança de Comportamento (Interfaces): É a forma mais fluida e
> adaptável. O filho assume apenas a responsabilidade de honrar um
> contrato [...] Herança de Estado (Classes): É invasiva e rígida. O
> filho herda campos físicos de memória [...] retirando do filho a
> autonomia sobre sua própria composição interna."

**Trecho — Subclasse Gorda:**
> "Se instanciarmos milhares de objetos Ebook, teremos milhares de
> bytes desperdiçados em atributos que são semanticamente irrelevantes
> para produtos puramente digitais. Este é um cenário clássico onde o
> design incorreto da hierarquia gera 'objetos gordos'."

---

### Fonte 3: `Teoria/Aula 8.tex`, linhas 268–279 e 317–332 (o dilema tributário e a explosão combinatória)

**Uso pretendido:** núcleo do Bloco 3 — o cenário de negócio que força
a explosão de subclasses.

**Trecho:**
> "A Explosão Combinatória: Tentar criar especializações como
> ProdutoFisicoImportado e ProdutoDigitalImportado entra em choque
> direto com a separação logística já estabelecida. Se amanhã
> adicionarmos um terceiro eixo, como 'Assinaturas' ou 'Categorias
> Promocionais', o número de subclasses explodirá em um produto
> cartesiano de possibilidades."

**Trecho — permutação forçada:**
> "Esta escalada é insustentável. Se adicionarmos uma terceira dimensão
> de variação [...] o número de classes salta instantaneamente de
> quatro para oito, e a tendência é um crescimento exponencial."

---

### Fonte 4: `Teoria/Aula 8.tex`, linhas 336–353 (o limite da linguagem: Problema do Diamante)

**Uso pretendido:** fundamentar a segunda metade do Bloco 3 — por que
Java fecha até a saída de herança múltipla.

**Trecho:**
> "O Java proíbe a herança múltipla de classes para evitar o famoso
> Problema do Diamante, que gera ambiguidades severas na resolução de
> métodos e conflitos de estado na memória. Sem a possibilidade de
> herdar as regras de 'Físico' e de 'Importado' simultaneamente de
> fontes limpas, somos arquiteturalmente forçados a realizar o
> anti-padrão de copiar e colar o comportamento tributário."

---

### Fonte 5: `Teoria/Aula 8.tex`, linhas 371–379 (o princípio fundacional do GoF)

**Uso pretendido:** abrir o Bloco 4 com a regra de ouro e sua
justificativa estrutural.

**Trecho:**
> "Favoreça a composição de objetos sobre a herança de classes [...]
> Encapsulamento Preservado: [...] a composição interage com objetos
> através de suas interfaces públicas, mantendo o interior de cada
> classe como uma 'caixa preta' protegida [...] Flexibilidade
> Dinâmica: [...] a composição permite montar e alterar comportamentos
> complexos conectando objetos menores em tempo de execução."

---

### Fonte 6: `Teoria/Aula 8.tex`, linhas 394–396 e 401–406 (Herbert Simon e a analogia modular)

**Uso pretendido:** fundamentar a teoria da quase-decomponibilidade e a
analogia eletrodoméstico integrado vs. modular no Bloco 4.

**Trecho:**
> "A Teoria de Herbert Simon: Sistemas complexos e estáveis quase
> sempre assumem a forma de uma hierarquia construída a partir de
> subsistemas fundamentais e mais simples. Quase Decomponibilidade: [...]
> os elos internos de uma peça são muito mais fortes do que as
> dependências entre peças distintas."

**Trecho — analogia:**
> "Se um televisor tem um VCR embutido na mesma carcaça, a quebra de
> uma engrenagem do vídeo cassete obriga você a levar a TV inteira para
> o conserto [...] Em um aparelho de som modular, se o CD Player queima,
> você o desconecta e troca, enquanto as caixas de som e o amplificador
> permanecem operacionais."

---

### Fonte 7: `Teoria/Aula 8.tex`, linhas 447–452 e 456–459 (tipos de composição e o Especialista da Informação)

**Uso pretendido:** núcleo do Bloco 5.

**Trecho:**
> "Agregação (Has-a / Tem-Um): Relação de Todo-Parte. O 'Todo' agrupa os
> elementos, mas não é dono absoluto de suas vidas [...] Associação
> (Uses-a / Usa-Um): Relação de colaboração livre onde as entidades
> possuem vidas completamente autônomas."

**Trecho — Especialista da Informação:**
> "A responsabilidade de uma tarefa deve recair exclusivamente sobre a
> classe que possui os dados necessários para resolvê-la [...] O
> Produto [...] não deve assumir a responsabilidade de se conectar a um
> servidor para despachar e-mails ou formatar relatórios em PDF."

---

### Fonte 8: `Teoria/Aula 8.tex`, linhas 504–517 e 527–530 (o labirinto de condicionais e a herança fracassada)

**Uso pretendido:** abrir o Bloco 6 — o problema-fio do checkout.

**Trecho — if/else:**
> "Explosão de Complexidade: O método cresce indefinidamente a cada
> novo meio de pagamento integrado [...] Fragilidade: Qualquer
> manutenção na regra do Pix arrisca quebrar a rotina do Cartão de
> Crédito."

**Trecho — herança fracassada:**
> "Identidade vs. Papel: O pagamento não define o que o Pedido é. Ele é
> apenas um evento que ocorre em seu ciclo de vida [...] Se
> instanciarmos um PedidoPix na memória e, no último segundo, o cliente
> decidir pagar com Cartão, a arquitetura falha."

---

### Fonte 9: `Teoria/Aula 8.tex`, linhas 703–712 e 767–771 (a topologia do Strategy e o OCP)

**Uso pretendido:** núcleo do Bloco 7 — a definição formal do padrão e
seu payoff arquitetural.

**Trecho — topologia:**
> "O padrão Strategy define uma família de algoritmos, encapsula cada
> um deles e os torna intercambiáveis [...] Context (Pedido): [...]
> Strategy (Pagavel): [...] ConcreteStrategy (Pix, Cartao): As
> implementações específicas do contrato."

**Trecho — OCP:**
> "Aberto para Extensão: Podemos adicionar Criptomoedas, Wallets ou
> sistemas alienígenas de pagamento amanhã, apenas criando uma nova
> classe. Fechado para Modificação: A classe Pedido não precisa ser
> alterada, não sofre recompilação e não tem o risco de quebrar o que
> já funciona."

---

### Notas sobre as fontes

- Fonte primária, como em todas as aulas desta disciplina: o próprio
  `.tex` do curso, não os 5 livros-base symlinkados em `_fontes/` — não
  há, nesta sessão, uma página específica já verificada nesses PDFs
  para os pontos exatos tratados aqui (explosão combinatória, Simon,
  Strategy), então nenhuma citação a eles foi incluída, seguindo o
  mesmo critério já registrado na Aula 9.
- `\section*{Exercícios de Fixação: Aula 8}` do próprio `.tex` (linhas
  945–1108: 25 blocos de V/F de 3 itens no formato `( )` + 15
  discursivas) foi lida como pool de referência temática, mas **não
  reaproveitada verbatim** — a maioria dos itens ali é de formato
  definicional ("X é considerado Y", "a Agregação define uma relação
  de..."), que o `CLAUDE.md` desta disciplina proíbe explicitamente. Os
  8 blocos de V/F e as 3 discursivas desta aula são **originais**,
  construídos a partir das 4 heurísticas exigidas, usando os mesmos
  temas do `.tex` como ponto de partida, não como texto-fonte.
- As duas seções finais do `.tex` (`Padrões de Projeto`, linhas
  806–917, e `Conclusão`, linhas 917–943) **não foram usadas nesta
  aula** — ver a "Decisão de escopo" acima. Ficam registradas aqui como
  ponto de partida exato para uma Aula 11 futura.
- Esta aula reaproveita deliberadamente a interface `Pagavel` e as
  classes `Pix`/`Cartao`/`Boleto` já usadas nas Aulas 8–9 (lá, como
  subclasses de `MeioPagamentoBase`) para construir a alternativa por
  composição/Strategy — não é uma coincidência de nomenclatura, é o
  contraste pedagógico central da aula: a mesma família de classes,
  resolvida de duas formas estruturalmente diferentes.
