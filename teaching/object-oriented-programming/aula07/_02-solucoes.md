# Soluções — Questões de Verdadeiro/Falso (Aula 7)

> Arquivo de apoio, não publicado (prefixo `_`). Contém a resposta e a
> justificativa de cada item das 12 questões de V/F do `index.qmd`. O
> `index.qmd` publicado continua sem solução — este arquivo existe só
> para conferência do professor/monitor, seguindo a metodologia de
> criação de questões definida em `../../CLAUDE.md`. Primeira
> resolução destes itens — nunca haviam sido resolvidos antes.

### O que é Polimorfismo — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Duas classes que implementam métodos com o mesmo nome, mas sem relação de herança ou interface comum entre elas, já caracterizam polimorfismo, pois cada uma se comporta de forma diferente.

**Resposta:** Falso

**Justificativa:** Polimorfismo exige uma referência de tipo comum (`Pagavel`, por exemplo) através da qual o mesmo ponto de chamada produz comportamentos diferentes dependendo do objeto real. Dois métodos de mesmo nome em classes não relacionadas, sem supertipo compartilhado, não passam pelo mecanismo de despacho polimórfico — são apenas nomes coincidentes, sem nenhum `forma.metodo()` cuja resolução dependa do objeto em runtime.

### O que é Polimorfismo — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ O objetivo prático do polimorfismo é reduzir o acoplamento e aumentar a extensibilidade do sistema.

**Resposta:** Verdadeiro

**Justificativa:** É o benefício central discutido na aula — o polimorfismo de inclusão permite que o código cliente dependa apenas do supertipo (`Pagavel`), reduzindo o acoplamento a implementações concretas e permitindo estender o sistema com novas classes sem alterar o código existente (OCP).

### O que é Polimorfismo — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ `pagamentoConfirmado()` pode se comportar como consulta de API no `Pix` e como verificação de data no `Boleto`.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente o que o polimorfismo de inclusão permite — a mesma assinatura definida no contrato `Pagavel` pode ser implementada de formas radicalmente diferentes em cada subtipo, sem que o código cliente precise saber qual delas está rodando.

### O que é Polimorfismo — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O código que chama a operação precisa conhecer os detalhes de implementação de quem a executa.

**Resposta:** Falso

**Justificativa:** É o oposto: o polimorfismo permite que o código cliente conheça apenas o contrato (`Pagavel`/`criarCobranca()`), sem qualquer conhecimento dos detalhes internos de `Pix`, `Boleto` ou `Cartao` — esse desacoplamento é o ponto central do mecanismo.

### Late Binding (Dynamic Dispatch) — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se a interface `Pagavel` não declarasse `criarCobranca()`, mas todas as classes que a implementam (`Pix`, `Cartao`) declarassem esse método por conta própria, a chamada `forma.criarCobranca(total)` ainda compilaria normalmente.

**Resposta:** Falso

**Justificativa:** O compilador decide se a chamada compila olhando apenas o tipo declarado da variável (`Pagavel`), não as implementações concretas. Se o método não está na interface, a chamada não compila, mesmo que toda implementação real o possua — o compilador não "adivinha" o que as subclasses declaram.

### Late Binding (Dynamic Dispatch) — item (b)

**Heurística:** Transferência

**Afirmação:** ✔ Num sistema de plugins em que cada plugin implementa a interface comum `Processador`, é possível adicionar um plugin novo, compilado separadamente, sem recompilar o núcleo do sistema — graças ao mesmo mecanismo que decide, em `Pagavel`, qual `criarCobranca()` roda.

**Resposta:** Verdadeiro

**Justificativa:** O Late Binding é o que permite essa flexibilidade: o núcleo só precisa conhecer a interface `Processador` em tempo de compilação; qual implementação concreta roda é decidido pela JVM em tempo de execução, olhando o objeto real — o mesmo mecanismo de `Pagavel`/`criarCobranca()`.

### Late Binding (Dynamic Dispatch) — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ A JVM decide olhando o tipo declarado da variável, não o objeto real na memória.

**Resposta:** Falso

**Justificativa:** É o inverso do que a aula descreve: o compilador (não a JVM) olha o tipo declarado da variável só para checar a existência do método; a JVM, em tempo de execução, decide com base no objeto real alocado na Heap — trocar esses dois papéis é o erro clássico de confundir Static e Dynamic Binding.

### Late Binding (Dynamic Dispatch) — item (d)

**Heurística:** Transferência

**Afirmação:** ✔ Late Binding é o que permite trocar a implementação injetada sem que o código cliente perceba.

**Resposta:** Verdadeiro

**Justificativa:** Como o código cliente só depende do tipo declarado (a interface), substituir a implementação concreta injetada não exige nenhuma alteração no código cliente — é o Late Binding sustentando a troca de "motor" mencionada na aula.

### Polimorfismo Universal — item (a)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Uma nova classe que implemente `Pagavel` depois que o sistema já estiver em produção pode ser usada em qualquer lugar que espere um `Pagavel`, sem exigir recompilação do código cliente existente.

**Resposta:** Verdadeiro

**Justificativa:** É a essência do Polimorfismo de Inclusão/OCP: o cliente depende só da interface; uma implementação futura, ainda inexistente hoje, já é compatível automaticamente, sem qualquer alteração no código que manipula `Pagavel`.

### Polimorfismo Universal — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O Polimorfismo Paramétrico exige que todos os tipos usados pertençam à mesma hierarquia de herança.

**Resposta:** Falso

**Justificativa:** É exatamente o oposto — o que caracteriza o Polimorfismo Paramétrico (Generics) é funcionar sobre tipos completamente não relacionados (`Produto`, `Cliente`), sem exigir hierarquia de herança comum; essa é a diferença estrutural em relação ao Polimorfismo de Inclusão.

### Polimorfismo Universal — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Um método genérico `ordenar(List<T> lista)` que funciona tanto para `List<Produto>` quanto para `List<Cliente>` deixaria de compilar se `Produto` e `Cliente` não implementassem uma interface `Comparable` em comum.

**Resposta:** Verdadeiro

**Justificativa:** O Polimorfismo Paramétrico dispensa hierarquia de herança entre os tipos usados como argumento de `T`, mas se o próprio algoritmo genérico depende de uma operação específica (comparar), essa exigência precisa vir de algum contrato comum (`Comparable<T>`) — Generics sem herança entre os dados não elimina a necessidade de contratos quando o algoritmo depende de uma operação.

### Polimorfismo Universal — item (d)

**Heurística:** Cenário contrafactual

**Afirmação:** ✗ Um sistema que usa apenas Polimorfismo Ad-hoc (sobrecarga e coerção) já suporta, em princípio, um número infinito de tipos diferentes sem precisar editar código existente.

**Resposta:** Falso

**Justificativa:** É o oposto do Polimorfismo Universal: o Ad-hoc é resolvido cedo, pelo compilador, sobre um conjunto finito e pré-determinado de tipos (cada versão sobrecarregada precisa ser escrita manualmente) — um tipo novo sempre exige voltar e editar o código, violando o OCP.

### Polimorfismo Ad-hoc — item (a)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Um método `enviar(String email)` e um método `enviar(int codigo)` na mesma classe `Notificador` configuram sobrecarga, mesmo que um deles nunca seja chamado em nenhum lugar do sistema.

**Resposta:** Verdadeiro

**Justificativa:** A sobrecarga é decidida pela assinatura (nome + tipos de parâmetro) declarada, não pelo uso em tempo de execução; um método sobrecarregado nunca chamado ainda é, sintaticamente, um caso válido de sobrecarga — a resolução é inteiramente estática, independente de uso.

### Polimorfismo Ad-hoc — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ A sobrecarga é considerada um polimorfismo verdadeiramente dinâmico e extensível.

**Resposta:** Falso

**Justificativa:** A aula chama a sobrecarga de "polimorfismo aparente" justamente porque ela é estática (Early Binding) e não extensível — um tipo novo exige reescrever a classe, violando o OCP.

### Polimorfismo Ad-hoc — item (c)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se dois métodos sobrecarregados `enviar(String email)` e `enviar(Object dado)` puderem ambos aceitar um argumento do tipo `String`, o compilador escolhe sempre a versão mais genérica (`Object`), para reduzir o número de conversões implícitas.

**Resposta:** Falso

**Justificativa:** A resolução de sobrecarga em Java escolhe a assinatura mais específica compatível com o argumento (aqui, `enviar(String email)`), não a mais genérica — o compilador prioriza o "melhor encaixe" de tipo, o oposto do que a afirmação propõe.

### Polimorfismo Ad-hoc — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ A coerção de `int` para `double` numa expressão aritmética pode ser desativada em tempo de execução dependendo do valor concreto da variável, da mesma forma que o Late Binding decide em runtime qual método roda.

**Resposta:** Falso

**Justificativa:** A coerção é resolvida em tempo de compilação, de forma fixa e sintática — não existe decisão em runtime nem dependência do valor da variável; diferente do Late Binding, que de fato decide dinamicamente com base no objeto real.

### Binding Estático vs. Dinâmico — item (a)

**Heurística:** Transferência

**Afirmação:** ✔ Um IDE que sugere automaticamente, enquanto o código é digitado, qual método `enviar()` sobrecarregado será chamado, está inspecionando o comportamento do Static Binding, não do Dynamic Binding.

**Resposta:** Verdadeiro

**Justificativa:** Como a sobrecarga é resolvida em tempo de compilação (Static Binding), o IDE consegue determinar qual versão roda apenas analisando o código-fonte estaticamente, sem executar o programa — o mesmo não seria possível para Dynamic Binding, cuja decisão depende do objeto real em runtime.

### Binding Estático vs. Dinâmico — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Métodos `static` e `private` em Java são resolvidos via Dynamic Binding.

**Resposta:** Falso

**Justificativa:** `static` e `private` são resolvidos via Static Binding — não podem ser sobrescritos polimorficamente; é por isso que a tabela da aula os lista como exemplos de Early Binding, ao lado da sobrecarga.

### Binding Estático vs. Dinâmico — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ O Dynamic Binding é o que sustenta o desacoplamento e a extensibilidade típicos da Orientação a Objetos.

**Resposta:** Verdadeiro

**Justificativa:** É a conclusão central da tabela Static vs. Dynamic Binding: o desacoplamento total e a extensibilidade vêm do Dynamic Binding, que permite trocar a implementação real sem alterar o código cliente; o Static Binding, ao contrário, prioriza performance sobre flexibilidade.

### Binding Estático vs. Dinâmico — item (d)

**Heurística:** Transferência

**Afirmação:** ✔ A Injeção de Dependência se apoia no Dynamic Binding para trocar implementações sem alterar o código cliente.

**Resposta:** Verdadeiro

**Justificativa:** A DI só funciona porque o código cliente depende de um tipo abstrato (interface); a substituição real da implementação injetada é resolvida em runtime pela JVM via Dynamic Binding — o mesmo mecanismo de despacho tardio discutido para `Pagavel`.

### O Fim do "Mar de IFs" — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Uma cadeia de `if/else` que verifica, dentro de um método de log genérico, se o parâmetro é `null` antes de gravá-lo, é um sintoma da mesma violação de OCP que a cadeia de `if/else` sobre tipos de pagamento.

**Resposta:** Falso

**Justificativa:** A meta-regra da aula é específica sobre `if`/`switch`/`instanceof` que verificam o *tipo de um objeto de negócio* para decidir o comportamento; uma checagem de nulidade é uma validação defensiva comum, não um sintoma de polimorfismo mal aproveitado — nem todo `if` viola o OCP.

### O Fim do "Mar de IFs" — item (b)

**Heurística:** Contrafactual

**Afirmação:** ✔ Com polimorfismo, adicionar um novo meio de pagamento não exige alterar o código do controlador.

**Resposta:** Verdadeiro

**Justificativa:** É a consequência direta do polimorfismo de inclusão programado contra a interface `Pagavel`: o controlador nunca precisa saber quantos ou quais tipos concretos existem — a mesma linha `formaEscolhida.criarCobranca(total)` já cobre o tipo novo.

### O Fim do "Mar de IFs" — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O uso de `instanceof` para decidir o comportamento com base no tipo concreto é incentivado pelo polimorfismo.

**Resposta:** Falso

**Justificativa:** É o oposto — precisar de `instanceof` para decidir comportamento por tipo é justamente o sintoma de que o polimorfismo não foi aproveitado; a meta-regra da aula trata isso como um sinal de alerta, não como algo incentivado.

### O Fim do "Mar de IFs" — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Delegar a decisão para o próprio objeto substitui a necessidade de perguntar "qual é o seu tipo?".

**Resposta:** Verdadeiro

**Justificativa:** É a mudança central do bloco: em vez de perguntar o tipo e ramificar externamente, o polimorfismo delega a decisão para dentro do próprio objeto (`forma.criarCobranca()`), que já sabe como se comportar.

### O Princípio Aberto/Fechado (OCP) — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Um sistema está "aberto para extensão" quando comportamentos novos entram via novas classes, não via edição das antigas.

**Resposta:** Verdadeiro

**Justificativa:** É a metade "aberta" do OCP: extensão via composição/novas implementações da interface, nunca via reabertura do código que já funciona.

### O Princípio Aberto/Fechado (OCP) — item (b)

**Heurística:** Transferência

**Afirmação:** ✔ Estar "fechado para modificação" significa que o código cliente não precisa ser retestado ao aceitar um novo ator.

**Resposta:** Verdadeiro

**Justificativa:** Se o código do `CheckoutController` de fato não muda uma linha ao aceitar `Cripto`, a suíte de testes já existente sobre esse código continua válida sem necessidade de retestá-lo — é uma consequência prática direta de "fechado para modificação".

### O Princípio Aberto/Fechado (OCP) — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Programar para interfaces, em vez de classes concretas, é o mecanismo que viabiliza o cumprimento do OCP.

**Resposta:** Verdadeiro

**Justificativa:** É o mecanismo técnico por trás do princípio: sem depender de uma interface (`Pagavel`), o código cliente teria que conhecer cada classe concreta, e o OCP não seria sustentável.

### O Princípio Aberto/Fechado (OCP) — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O OCP recomenda revisar e reescrever o código cliente a cada novo comportamento adicionado ao sistema.

**Resposta:** Falso

**Justificativa:** É exatamente o oposto do que o OCP recomenda — o princípio existe para que o código cliente permaneça intocado ao acomodar novos comportamentos, via novas classes que implementam o contrato existente.

### Substitutibilidade — item (a)

**Heurística:** Transferência

**Afirmação:** ✔ A substitutibilidade é a capacidade de trocar implementações concretas por uma abstração comum sem impacto perceptível.

**Resposta:** Verdadeiro

**Justificativa:** É a propriedade que sustenta o polimorfismo de inclusão: qualquer `Pagavel` concreto pode ocupar o lugar de outro sem que o código que o manipula perceba a diferença.

### Substitutibilidade — item (b)

**Heurística:** Transferência

**Afirmação:** ✔ `CheckoutController` trata `Pix`, `Boleto` e `Cartao` de forma uniforme através da "lente" do tipo `Pagavel`.

**Resposta:** Verdadeiro

**Justificativa:** É a aplicação concreta da substitutibilidade ao exemplo da aula: o controlador nunca enxerga `Pix`/`Boleto`/`Cartao` diretamente, só a interface comum.

### Substitutibilidade — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Para usar `criarCobranca()`, o controlador precisa saber qual classe concreta está por trás da referência.

**Resposta:** Falso

**Justificativa:** É o oposto do que a substitutibilidade garante — o controlador chama `criarCobranca()` sem nunca precisar saber qual classe concreta implementa `Pagavel` naquele momento.

### Substitutibilidade — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ A substitutibilidade é o que permite ao sistema aceitar novos meios de pagamento sem alterar o núcleo.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma ideia do OCP aplicada à substitutibilidade: como qualquer `Pagavel` é intercambiável, o núcleo do sistema (o `CheckoutController`) nunca precisa mudar para acomodar um tipo novo.

### O Problema dos *Raw Types* — item (a)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Sem Generics, uma coleção Java podia armazenar referências genéricas do tipo `Object`.

**Resposta:** Verdadeiro

**Justificativa:** É o caso-limite de ausência total de restrição de tipo: sem Generics, `Object` é o único "contrato" da coleção, aceitando qualquer referência, o que é exatamente o problema que motiva a introdução de Generics.

### O Problema dos *Raw Types* — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O risco de inserir um objeto incompatível numa lista sem Generics é detectado imediatamente pelo compilador.

**Resposta:** Falso

**Justificativa:** É o oposto — o erro só é detectado tardiamente, no momento em que o item incompatível é efetivamente usado como se fosse do tipo esperado (geralmente via `ClassCastException`), não no momento da inserção.

### O Problema dos *Raw Types* — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Recuperar dados de uma coleção não parametrizada exigia *casting* manual, sujeito a `ClassCastException`.

**Resposta:** Verdadeiro

**Justificativa:** Sem a "etiqueta de tipo" dos Generics, todo item recuperado de uma coleção `Object` precisa de um cast explícito para o tipo esperado, e esse cast pode falhar em runtime se o item real for de outro tipo.

### O Problema dos *Raw Types* — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ A detecção tardia de um erro de tipo é o principal risco prático dos *raw types*.

**Resposta:** Verdadeiro

**Justificativa:** É a síntese do bloco: o problema central não é a possibilidade do erro em si, mas o fato de ele só se manifestar muito depois da causa real (a inserção), dificultando o diagnóstico.

### Generics como Etiqueta de Segurança — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ `List<Pagavel>` desloca a detecção de erros de tipo do tempo de execução para o tempo de compilação.

**Resposta:** Verdadeiro

**Justificativa:** É o ganho central de Generics: o compilador passa a rejeitar a inserção de um tipo incompatível na própria linha do `add`, em vez de deixar o erro estourar depois, como `ClassCastException`.

### Generics como Etiqueta de Segurança — item (b)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Generics elimina a necessidade de *casting* manual na leitura de itens de uma coleção parametrizada.

**Resposta:** Verdadeiro

**Justificativa:** Como o compilador já sabe, pela declaração `List<Pagavel>`, que todo item é um `Pagavel`, o cast antes exigido na leitura passa a ser inserido automaticamente pelo compilador (elidido no bytecode gerado) — não resta nenhum cast manual explícito no código-fonte.

### Generics como Etiqueta de Segurança — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Generics reduz a legibilidade do código, pois exige mais caracteres na declaração de tipos.

**Resposta:** Falso

**Justificativa:** É o oposto do que a aula afirma: `List<Pagavel>` diz mais sobre a intenção do código do que `List` sozinho — a legibilidade aumenta, mesmo que a declaração use mais caracteres.

### Generics como Etiqueta de Segurança — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Proibir a inserção de tipos incompatíveis é uma das formas como Generics aumenta a robustez do sistema.

**Resposta:** Verdadeiro

**Justificativa:** É a primeira das quatro vantagens práticas listadas na aula: mover a detecção de erro para o tempo de compilação torna o sistema mais robusto, ao custo zero de flexibilidade real.

### Polimorfismo Paramétrico e Identidade — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ O Polimorfismo Paramétrico usa variáveis de tipo (como `<T>`) mantendo a segurança de tipos estáticos.

**Resposta:** Verdadeiro

**Justificativa:** É a combinação que caracteriza Generics: flexibilidade de um algoritmo único para qualquer tipo, sem abrir mão da checagem de tipos em tempo de compilação — diferente de uma solução baseada em `Object`, que sacrificaria essa segurança.

### Polimorfismo Paramétrico e Identidade — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Diferente do Polimorfismo de Inclusão, o Paramétrico não exige que os tipos usados pertençam à mesma árvore de herança.

**Resposta:** Verdadeiro

**Justificativa:** É a distinção estrutural central entre os dois polimorfismos universais: Inclusão depende de uma hierarquia comum (`implements`/`extends`); Paramétrico funciona sobre qualquer tipo, relacionado ou não.

### Polimorfismo Paramétrico e Identidade — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Um `Repositorio<T>` genérico centraliza a lógica de infraestrutura sem duplicar código para cada entidade.

**Resposta:** Verdadeiro

**Justificativa:** É uma aplicação de Generics a um padrão de projeto comum (o Repositório) não citado literalmente na aula, mas coerente com a "reutilização" listada como uma das quatro vantagens práticas de Generics.

### Polimorfismo Paramétrico e Identidade — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Recuperar um item de um `Repositorio<T>` obriga o desenvolvedor a fazer um *cast* manual para o tipo concreto.

**Resposta:** Falso

**Justificativa:** É o oposto do ganho de Generics: o compilador já sabe, pela declaração `Repositorio<T>`, o tipo de retorno — não é necessário nenhum cast manual explícito.

### Síntese: Contrato, Polimorfismo e Segurança de Tipo — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Interfaces definem o contrato; Polimorfismo de Inclusão o torna substituível; Generics protege coleções desses contratos.

**Resposta:** Verdadeiro

**Justificativa:** É a síntese correta dos três papéis discutidos na aula: cada ferramenta cobre uma camada diferente do mesmo problema — comunicação entre objetos sem acoplamento nem perda de segurança de tipo.

### Síntese: Contrato, Polimorfismo e Segurança de Tipo — item (b)

**Heurística:** Transferência

**Afirmação:** ✔ O uso conjunto de interfaces, polimorfismo e Generics é o que sustenta sistemas verdadeiramente *Plug-and-Play*.

**Resposta:** Verdadeiro

**Justificativa:** Um sistema Plug-and-Play precisa aceitar peças novas sem recompilar o núcleo (OCP/polimorfismo) e sem perder segurança de tipo nas coleções que as manipulam (Generics) — a combinação das três ferramentas é o que viabiliza essa propriedade.

### Síntese: Contrato, Polimorfismo e Segurança de Tipo — item (c)

**Heurística:** Caso limite/extremo

**Afirmação:** ✗ Um sistema bem desenhado com essas três ferramentas ainda pode exigir `if`s de tipo em pontos centrais do fluxo.

**Resposta:** Falso

**Justificativa:** Se `if`s de tipo sobre objetos de negócio ainda aparecem em pontos centrais do fluxo, é sinal de que o polimorfismo não foi bem aproveitado nesse ponto — um sistema bem desenhado com as três ferramentas delega essas decisões para dentro dos próprios objetos, não para checagens de tipo no fluxo principal.

### Síntese: Contrato, Polimorfismo e Segurança de Tipo — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ A meta comum às três ferramentas é mover decisões e erros para o momento mais cedo e mais seguro possível do ciclo de vida do software.

**Resposta:** Verdadeiro

**Justificativa:** É o fio que une os três tópicos da aula: interfaces fixam o contrato em compilação, polimorfismo resolve comportamento sem `if`s frágeis, e Generics move erros de coleção do runtime para a compilação — todas movem risco para mais cedo no ciclo de vida.
