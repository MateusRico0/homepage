# Gabarito — Aula 12

Gabarito consolidado: a solução discutida de cada pausa ativa da aula.
O gabarito das questões de Verdadeiro/Falso dos exercícios finais é
público, em `soluções.qmd`. Nunca publicado no site (prefixo `_`).

## Pausas Ativas

### Pausa 1 — O Antipadrão do Status e a Fragilidade de Evolução

**Pergunta motivadora:** Se um novo requisito pedir um estado
"EM_ANALISE_DE_FRAUDE" entre "NOVO" e "PAGO" no `Pedido` do antipadrão,
quantos métodos já existentes precisam ser abertos e editados — e o
que esse número revela sobre a real causa da fragilidade do design?

**Discussão:** Três métodos precisam de edição — `pagar()`,
`cancelar()` e `enviar()` — porque todos os três verificam o campo
`status` internamente antes de decidir o que fazer. Trocar o tipo de
`status` de `String` para `enum` eliminaria o risco de um valor
inválido, mas não eliminaria a necessidade de editar os três métodos:
o problema estrutural não é o tipo do campo, é a lógica de transição
estar fisicamente espalhada por vários métodos que também carregam
regra de negócio não relacionada ao fluxo. Esse número (três, não um)
revela que a causa real da fragilidade não é "faltam mais `if`s" — é a
ausência de um único lugar responsável por decidir o fluxo.

**V/F resolvido:**
- ✗ No `Pedido` do antipadrão, inserir um novo estado exige editar apenas o método `pagar()`, já que é o único que decide a transição de "NOVO" para "PAGO".
- ✔ Um teste unitário que verifica "cancelar um pedido já pago dispara estorno" precisa, antes de chamar `cancelar()`, montar um `Pedido` cujo campo `status` já esteja manualmente ajustado para `"PAGO"`.
- ✗ Se o tipo do campo `status` fosse trocado de `String` para um `enum` Java, isso sozinho eliminaria a necessidade de abrir `pagar()`, `cancelar()` e `enviar()` ao adicionar um estado novo.
- ✔ A fragilidade de evolução do `Pedido` do antipadrão nasce do fato de a lógica de transição de estado estar fisicamente distribuída dentro de vários métodos que também contêm lógica de negócio não relacionada ao fluxo.

---

### Pausa 2 — Strategy vs. State: Mesma Topologia, Intenções Diferentes

**Pergunta motivadora:** Se alguém disser que o State Pattern é apenas
"um Strategy com nomes diferentes", por que essa afirmação, apesar de
a topologia de classes ser quase idêntica, erra o ponto central da
intenção arquitetural de cada padrão?

**Discussão:** A afirmação confunde "mesma forma de classes" com
"mesma intenção arquitetural". No Strategy, a troca de implementação é
decidida por um agente **externo** ao Contexto — o código cliente que
chama `setEstrategia(...)`; a estratégia concreta nunca se
autossubstitui. No State, é o próprio objeto de estado atual —
`EstadoNovo`, por exemplo — quem decide e executa a transição para
`EstadoPago` como efeito colateral de processar uma operação de
negócio (`pagar()`), sem que nenhum código cliente externo precise
invocar a troca. A estrutura de classes (interface + implementações)
é necessária, mas não suficiente, para definir o padrão: o que
diferencia os dois é *quem* decide qual implementação está ativa e
*quando* essa decisão acontece — não o número de métodos da interface.

**V/F resolvido:**
- ✗ Em um `CalculadoraDeFrete` que usa Strategy, é o próprio objeto `FreteExpresso` injetado que decide, sozinho e sem intervenção externa, substituir-se por `FreteGratis` durante a execução do sistema.
- ✔ Num `Pedido` usando State, é fisicamente o objeto `EstadoNovo` — e não um código cliente externo chamando `pedido.setEstrategia(new EstadoPago())` — quem invoca a transição para `EstadoPago` como consequência de `pagar()` ter sido chamado.
- ✗ Se um `ConcreteState` do padrão State fosse instanciado e injetado manualmente por código cliente externo antes de qualquer operação de negócio ocorrer no Contexto, essa prática ainda preservaria integralmente a intenção arquitetural original do State Pattern.
- ✗ O fato de tanto Strategy quanto State definirem uma interface implementada por múltiplas classes concretas é suficiente, por si só, para classificá-los como o mesmo padrão de projeto sob nomes diferentes.

---

### Pausa 3 — O Dilema da Herança no Adapter

**Pergunta motivadora:** Se o `LogAdapter` decidisse estender
(`extends`) `LogServicoLegado` em vez de compô-lo por injeção, que
capacidade futura o sistema perderia especificamente quando o
fornecedor lançasse uma nova subclasse de `LogServicoLegado`?

**Discussão:** O sistema perderia a capacidade de reaproveitar
automaticamente a nova subclasse. Um Object Adapter (composição)
continua funcionando sem alteração nenhuma quando o objeto injetado no
construtor é substituído por uma subclasse do legado — ele trata o
legado, e qualquer subclasse dele, como uma caixa preta acessada só
pela API pública, via polimorfismo. Um Class Adapter (`extends`), por
outro lado, está preso via herança a uma única classe-mãe fixa em
tempo de compilação; uma nova subclasse do fornecedor exigiria
escrever um segundo Adapter dedicado só para ela. A mesma composição
que garante essa flexibilidade também é o que permite, em teste
automatizado, substituir o legado real por um objeto simulado (*mock*)
sem alterar o `LogAdapter` — vantagem que a herança anularia.

**V/F resolvido:**
- ✔ Um `LogAdapter` construído por composição (Object Adapter) continua funcionando corretamente mesmo que o objeto injetado no construtor seja, na verdade, uma subclasse de `LogServicoLegado` lançada pelo fornecedor depois que o `LogAdapter` já havia sido escrito.
- ✔ Um `LogAdapter` que estendesse `LogServicoLegado` (Class Adapter) precisaria ser reescrito ou duplicado para conseguir adaptar especificamente uma nova subclasse do legado, mesmo que essa subclasse só adicionasse um método novo sem alterar `registrarLogNoArquivo`.
- ✔ Trocar `LogServicoLegado legado` por uma injeção via construtor no `LogAdapter` (em vez de herança) é o que permite substituir, em um teste automatizado, o legado real por uma versão simulada (*mock*) sem alterar o código do `LogAdapter`.
- ✗ Se `LogServicoLegado` expusesse um método `protected` usado internamente por suas próprias subclasses, um `LogAdapter` implementado como Object Adapter teria acesso direto a esse método da mesma forma que um Class Adapter teria.
