# Soluções — Questões de Verdadeiro/Falso (Aula 8)

> Arquivo de apoio, não publicado (prefixo `_`). Contém a resposta e a
> justificativa de cada item das 12 questões de V/F do `index.qmd`. O
> `index.qmd` publicado continua sem solução — este arquivo existe só
> para conferência do professor/monitor, seguindo a metodologia de
> criação de questões definida em `../../CLAUDE.md`. Primeira
> resolução destes itens — nunca haviam sido resolvidos antes.

### Herança como Identidade ("É-UM") — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ A herança estabelece uma relação de identidade mais profunda que a associação — a relação "É-UM".

**Resposta:** Verdadeiro

**Justificativa:** É a distinção central do bloco: associação é uma referência externa entre objetos independentes; herança é incorporação física de estrutura, uma relação de identidade — o filho não só se relaciona com o pai, ele *é* uma especialização do pai.

### Herança como Identidade ("É-UM") — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O filho, ao herdar, assina apenas o contrato do pai, sem incorporar sua estrutura interna.

**Resposta:** Falso

**Justificativa:** É o oposto do que a aula descreve: herdar não é "assinar um contrato" (isso é o papel das interfaces) — é incorporação física. Quando `Cartao` é instanciado, a Heap contém tanto os atributos definidos localmente quanto os herdados de `MeioPagamentoBase`.

### Herança como Identidade ("É-UM") — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Num sistema onde `Cartao` herda de `MeioPagamentoBase`, e `Cartao` também guarda uma referência a um objeto `Endereco` como atributo, o acoplamento entre `Cartao` e `Endereco` é tão forte quanto o acoplamento entre `Cartao` e `MeioPagamentoBase`.

**Resposta:** Falso

**Justificativa:** Herança é incorporação física e acoplamento vitalício (o filho carrega a estrutura do pai); guardar uma referência a `Endereco` é apenas associação/composição, um acoplamento mais fraco e mais fácil de trocar — os dois tipos de relação não têm a mesma força, mesmo aparecendo na mesma classe.

### Herança como Identidade ("É-UM") — item (d)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Herança de atributos significa que o filho fisicamente possui, na memória, os campos definidos no pai.

**Resposta:** Verdadeiro

**Justificativa:** É a "incorporação física" descrita na aula: ao instanciar `Cartao`, a Heap aloca tanto o campo local (`limite`) quanto o campo herdado (`idCobranca`) — não existe uma versão "mais leve" da instância que omita o que veio do pai.

### O Modificador `protected` — item (a)

**Heurística:** Transferência

**Afirmação:** ✔ `protected` permite que subclasses manipulem o estado herdado sem expô-lo ao resto do sistema.

**Resposta:** Verdadeiro

**Justificativa:** É a definição operacional de `protected` usada na aula: o estado fica acessível dentro da família de classes (pai e filhos), mas continua oculto para qualquer código externo à hierarquia.

### O Modificador `protected` — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ `protected` é equivalente, em termos de encapsulamento, a `private`.

**Resposta:** Falso

**Justificativa:** `protected` ainda vaza o estado para toda a linhagem de subclasses ("encapsulamento de linhagem"), enquanto `private` não vaza para ninguém fora da própria classe — não são equivalentes; é exatamente essa diferença que motiva blindar atributos críticos com `private`.

### O Modificador `protected` — item (c)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Se `MeioPagamentoBase` alterar de `protected` para `private` o atributo `idCobranca`, todo `Cartao`, `Pix` e `Boleto` que acessava esse atributo diretamente (sem usar um método) para de compilar.

**Resposta:** Verdadeiro

**Justificativa:** `private` bloqueia o acesso até para subclasses; qualquer subclasse que dependia do acesso direto ao campo `protected` perde a compilação — é o custo de "blindar a base" mencionado na aula, e por isso a transição para `private` exige, ao mesmo tempo, expor um método de acesso controlado.

### O Modificador `protected` — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Sem `final` no método de transição, uma subclasse pode ignorar a validação do pai livremente.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente o exemplo de `alterarStatus()` da aula: sem `final`, `Cartao` pode sobrescrever o método e ignorar a checagem de invariante do pai, tratando a validação como uma mera "sugestão".

### O Problema da Classe Base Frágil — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se `MeioPagamentoBase.processarLote()` for reescrito para não chamar mais `processarPagamento()` internamente (processando os valores diretamente, sem delegar), o `Cartao` que sobrescreve ambos os métodos passará a contar corretamente, sem nenhuma mudança no código do `Cartao`.

**Resposta:** Verdadeiro

**Justificativa:** Como a contagem duplicada vinha da chamada interna do pai a um método sobrescrito, remover essa chamada interna faz o `totalTransacoes` do `Cartao` "corrigir-se" sozinho — sem que uma única linha do `Cartao` tenha sido tocada, ilustrando como o filho está à mercê de decisões internas do pai que ele nem vê.

### O Problema da Classe Base Frágil — item (b)

**Heurística:** Transferência

**Afirmação:** ✔ O bug de contagem dupla em `processarLote` surge porque o polimorfismo desvia a chamada interna para o método sobrescrito do filho.

**Resposta:** Verdadeiro

**Justificativa:** `super.processarLote()` chama `processarPagamento()` internamente; por polimorfismo/Late Binding, essa chamada é desviada para a versão sobrescrita em `Cartao`, que incrementa o contador de novo — daí o resultado 6 em vez de 3.

### O Problema da Classe Base Frágil — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Esse tipo de erro costuma ser detectado pelo compilador antes da execução.

**Resposta:** Falso

**Justificativa:** É justamente o oposto — o compilador não enxerga esse tipo de dependência semântica entre métodos; o bug só se manifesta em runtime, ao observar o valor incorreto de `totalTransacoes`, o que torna o Problema da Classe Base Frágil especialmente perigoso.

### O Problema da Classe Base Frágil — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Invariantes que vivem apenas na lógica implícita do pai são as mais perigosas de se violar sem perceber.

**Resposta:** Verdadeiro

**Justificativa:** É a síntese do bloco: como essas regras não aparecem na assinatura dos métodos nem no sistema de tipos, nenhuma ferramenta automática avisa quando elas são violadas — só a leitura cuidadosa do código do pai revela o risco.

### Herança por Conveniência vs. Especialização Legítima — item (a)

**Heurística:** Transferência

**Afirmação:** ✗ Uma classe `RelatorioFinanceiro` que precisa apenas do método `formatarMoeda()` de uma classe utilitária `FormatadorNumerico` deveria herdar de `FormatadorNumerico` para ganhar acesso a esse método.

**Resposta:** Falso

**Justificativa:** Precisar de um único método utilitário não estabelece uma relação "É-UM" nem exige tratamento polimórfico — é o caso clássico de herdar por conveniência; a solução correta é composição (guardar uma referência a `FormatadorNumerico`) ou, em Java, um método utilitário `static`.

### Herança por Conveniência vs. Especialização Legítima — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ `GerenciadorDeCobrancas extends ListaDeContatos` é um exemplo de especialização legítima.

**Resposta:** Falso

**Justificativa:** É exatamente o exemplo de "herança por conveniência" dado na aula: o gerenciador *usa* uma lista, não *é* uma lista — não há relação "É-UM" real, só reaproveitamento de métodos prontos.

### Herança por Conveniência vs. Especialização Legítima — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Uma classe `RegistroDeAuditoria` que estende `MeioPagamentoBase` só para reaproveitar o atributo `idCobranca`, mas nunca é armazenada numa `List<Pagavel>` nem passada onde se espera um `Pagavel`, ainda é uma especialização legítima, desde que implemente corretamente `criarCobranca()`.

**Resposta:** Falso

**Justificativa:** Implementar o método exigido não basta — especialização legítima exige as duas condições simultâneas (compartilhar o DNA *e* precisar de tratamento polimórfico); se `RegistroDeAuditoria` nunca é tratado como um `Pagavel` em lugar algum do sistema, falta a segunda condição, e a herança aqui é só reuso de estrutura disfarçado.

### Herança por Conveniência vs. Especialização Legítima — item (d)

**Heurística:** Transferência

**Afirmação:** ✔ A composição é a alternativa correta quando a relação real é "usa um", não "é um".

**Resposta:** Verdadeiro

**Justificativa:** É a correção proposta na aula para o erro de `GerenciadorDeCobrancas extends ListaDeContatos`: trocar a herança por uma referência privada à lista, guardando a relação de uso sem os riscos de vazamento de métodos e de identidade incoerente.

### Invariantes Invisíveis — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Se `MeioPagamentoBase` documentar explicitamente, em um comentário Javadoc, que `validar()` deve sempre rodar antes de `processar()`, essa dependência de ordem deixa de ser uma invariante invisível.

**Resposta:** Falso

**Justificativa:** Um comentário Javadoc não é verificado pelo compilador nem pela JVM — a dependência de ordem continua vivendo só na convenção/documentação, não na assinatura ou no tipo; ela só deixaria de ser "invisível" de fato se fosse imposta estruturalmente (por exemplo, com um Template Method `final`).

### Invariantes Invisíveis — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Se o pai espera que um método nunca retorne `null`, uma subclasse pode alterar essa semântica livremente sem risco.

**Resposta:** Falso

**Justificativa:** É exatamente a armadilha de "semântica de retorno" descrita na aula: se o filho sobrescreve o método e passa a retornar `null`, todo código do pai (ou de terceiros) que confiava na garantia de "nunca `null`" quebra com `NullPointerException`, longe da causa real.

### Invariantes Invisíveis — item (c)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se `Cartao.alterarStatus()` sobrescrever o método do pai e esquecer de chamar `super.alterarStatus()`, mas ainda assim atualizar corretamente o campo `status` com sua própria lógica, o objeto nunca fica num estado inconsistente.

**Resposta:** Falso

**Justificativa:** Mesmo que o filho atualize `status` "corretamente" à primeira vista, ele pula qualquer lógica adicional que o pai executasse em `super.alterarStatus()` (validações, contadores, notificações) — é exatamente esse tipo de omissão que gera a "máquina de estado zumbi": o objeto parece vivo e funcional, mas seu ciclo de vida lógico ficou incompleto.

### Invariantes Invisíveis — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Adicionar a anotação `@Deprecated` a um método do pai é suficiente para transformar uma invariante antes invisível (como um pressuposto de ordem) numa restrição verificada pelo compilador.

**Resposta:** Falso

**Justificativa:** `@Deprecated` é só um aviso informativo ao desenvolvedor (geralmente sinalizado pelo IDE); não é verificado pelo compilador como uma regra e não impõe ordem de chamada nenhuma — continua sendo, na prática, uma convenção que vive fora do sistema de tipos.

### A Base como Guardiã — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Atributos que regem invariantes críticos devem ser `private` na classe base, não `protected`.

**Resposta:** Verdadeiro

**Justificativa:** É a primeira medida de "blindagem" descrita na aula: `protected` ainda vaza para a família; só `private` garante que nenhuma subclasse corrompa o atributo diretamente, forçando o acesso pelos métodos controlados do pai.

### A Base como Guardiã — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Métodos `final` impedem que subclasses sobrescrevam e subvertam a validação da base.

**Resposta:** Verdadeiro

**Justificativa:** É a segunda medida de blindagem: travar com `final` o método de transição de estado impede que uma subclasse faça exatamente o que `Cartao` fez no exemplo da fragilidade — sobrescrever e ignorar a checagem de invariante.

### A Base como Guardiã — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Métodos-gancho (`protected abstract`) delegam ao filho só o detalhe técnico, sem expor o fluxo inteiro.

**Resposta:** Verdadeiro

**Justificativa:** É o papel do gancho na base-guardiã: o filho implementa apenas o pedaço que exige conhecimento especializado (`executarProcessamento()`), enquanto o restante do fluxo (validação, ordem dos passos) permanece protegido na base.

### A Base como Guardiã — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Blindar a base dessa forma torna a integridade do sistema dependente do acerto individual de cada subclasse.

**Resposta:** Falso

**Justificativa:** É o oposto do propósito da blindagem: ao tornar os atributos críticos `private`, os métodos de transição `final` e os detalhes técnicos ganchos `abstract`, a integridade do sistema passa a depender da base (um único ponto de controle), não do acerto individual de cada subclasse.

### Classes Abstratas — item (a)

**Heurística:** Transferência

**Afirmação:** ✔ Uma classe abstrata pode ter métodos concretos, resolvendo parte do comportamento do objeto.

**Resposta:** Verdadeiro

**Justificativa:** É a metáfora do chassi: rodas, bancos e suspensão (métodos concretos, como `validarValor()`) já vêm prontos; só o "motor" (o método `abstract`) falta.

### Classes Abstratas — item (b)

**Heurística:** Transferência

**Afirmação:** ✔ O compilador impede a instanciação direta de uma classe abstrata via `new`.

**Resposta:** Verdadeiro

**Justificativa:** O compilador age como "inspetor de fábrica" e rejeita a instanciação de qualquer classe abstrata, completa ou não — `new MeioPagamentoBase(100.0)` nem compila, mesmo que todos os métodos concretos existam.

### Classes Abstratas — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Uma classe abstrata é uma limitação técnica sem nenhum propósito arquitetural além de "não poder instanciar".

**Resposta:** Falso

**Justificativa:** É o oposto do que a aula defende: uma classe abstrata é um compromisso arquitetural — a "máquina semi-acabada" que força as subclasses a completar o "motor" — não uma limitação técnica arbitrária.

### Classes Abstratas — item (d)

**Heurística:** Transferência

**Afirmação:** ✔ O método `abstract` de uma classe abstrata representa a parte "sem motor" da máquina semi-acabada.

**Resposta:** Verdadeiro

**Justificativa:** É a aplicação direta da metáfora do chassi ao elemento sintático `abstract`: o método sem corpo é exatamente o "buraco" que cada subclasse concreta precisa preencher com seu próprio motor.

### Herança de Estado vs. Comportamento — item (a)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Uma classe `Pix` que implementa `Pagavel` (mas não estende nenhuma classe) e nunca armazena `idCobranca` como atributo, gerando-o sob demanda dentro do próprio método `getIdCobranca()`, ainda cumpre corretamente o contrato da interface.

**Resposta:** Verdadeiro

**Justificativa:** Como interfaces herdam só comportamento (a assinatura do método), o filho é livre para decidir como implementá-lo — inclusive sem guardar estado algum; isso é exatamente o que a aula descreve como a "fluidez" da herança de comportamento, em contraste com a rigidez da herança de estado.

### Herança de Estado vs. Comportamento — item (b)

**Heurística:** Cenário contrafactual

**Afirmação:** ✗ Se `MeioPagamentoBase` tiver um atributo `logsInternos` que o `Pix` nunca usa, é possível, em Java, fazer com que instâncias de `Pix` simplesmente não aloquem espaço para esse campo na Heap.

**Resposta:** Falso

**Justificativa:** Não existe, em Java, uma forma de uma subclasse "recusar" um campo herdado — toda instância de `Pix` carrega `logsInternos` na Heap, use ou não; herdar estado é compulsório, diferente da liberdade que existe ao herdar comportamento via interface.

### Herança de Estado vs. Comportamento — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Existe uma sintaxe padrão em Java para um filho "recusar" um atributo herdado que ele não usa.

**Resposta:** Falso

**Justificativa:** É a mesma conclusão do item anterior: herança de estado é alocação compulsória; não há palavra-chave ou anotação padrão em Java que permita a um filho "deserdar" um campo do pai.

### Herança de Estado vs. Comportamento — item (d)

**Heurística:** Transferência

**Afirmação:** ✔ Mudar o tipo de um atributo herdado (de `String` para `UUID`, por exemplo) pode exigir revisar todas as subclasses.

**Resposta:** Verdadeiro

**Justificativa:** Se `idCobranca` mudar de `String` para `UUID`, toda subclasse que o acessa diretamente (via `protected`) precisa ser revista e ajustada — é o custo de longo prazo da herança de estado mencionado na aula.

### Template Method: o Esqueleto — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ O método principal do Template Method costuma ser marcado como `final` para travar a ordem dos passos.

**Resposta:** Verdadeiro

**Justificativa:** É a própria assinatura de `realizarPagamento()` no exemplo da aula: `final` impede que qualquer subclasse sobrescreva o método e altere a ordem validação → especialização → log.

### Template Method: o Esqueleto — item (b)

**Heurística:** Caso limite/extremo

**Afirmação:** ✗ Se `MeioPagamentoBase` tivesse dois métodos-gancho abstratos (`criarCobrancaEspecifica()` e `validarRegrasEspecificas()`), uma subclasse poderia implementar apenas um dos dois e ainda assim compilar normalmente.

**Resposta:** Falso

**Justificativa:** Uma classe concreta em Java é obrigada a implementar todos os métodos abstratos herdados; deixar um método-gancho sem implementação impede a compilação (a menos que a própria subclasse também seja declarada `abstract`) — o compilador garante que nenhum gancho fique "aberto".

### Template Method: o Esqueleto — item (c)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se cada subclasse pudesse sobrescrever o método principal livremente, a ordem de validação e log deixaria de ser garantida.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente o risco de não travar `realizarPagamento()` com `final`: sem essa trava, nada impede um `Pix` de esquecer o log, ou um `Boleto` de pular a validação, cada um implementando sua própria ordem.

### Template Method: o Esqueleto — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O Template Method reduz a previsibilidade do sistema, pois cada filho decide sua própria sequência de passos.

**Resposta:** Falso

**Justificativa:** É o oposto: no Template Method é o pai quem decide a sequência (fixada pelo `final`), e o filho só preenche a lacuna do gancho — é justamente essa centralização que aumenta a previsibilidade.

### Inversão de Controle e o Princípio de Hollywood — item (a)

**Heurística:** Transferência

**Afirmação:** ✔ Se um framework de testes chama automaticamente o método `setUp()` de uma classe de teste antes de cada teste, sem que o desenvolvedor precise chamá-lo manualmente, esse framework está aplicando o mesmo Princípio de Hollywood do Template Method.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma Inversão de Controle: o framework (equivalente ao "pai") controla o fluxo e decide quando chamar o código do desenvolvedor (`setUp()`), em vez do desenvolvedor chamar o framework — "não nos ligue, nós ligamos para você" se aplica a qualquer arquitetura onde o controle do fluxo principal foi invertido, não só ao Template Method dentro de uma única hierarquia de classes.

### Inversão de Controle e o Princípio de Hollywood — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Um script procedural que lê um arquivo, chama uma função de parsing de uma biblioteca, e depois decide o que fazer com o resultado, já está aplicando Inversão de Controle, porque delega parte do trabalho para código de terceiros (a biblioteca).

**Resposta:** Falso

**Justificativa:** Delegar uma tarefa pontual para uma função de biblioteca não é Inversão de Controle — o script continua no comando, decidindo quando e como chamar a biblioteca; IoC exige o contrário: o framework/base retém o fluxo principal e decide quando chamar o código do desenvolvedor, como o Template Method faz com o gancho.

### Inversão de Controle e o Princípio de Hollywood — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ No Template Method, é o filho quem decide quando delegar a execução de volta para o pai.

**Resposta:** Falso

**Justificativa:** É o inverso: é o pai quem retém o controle do fluxo (`realizarPagamento()` é `final` e vive na base) e decide, num ponto fixo dessa sequência, quando desviar para o gancho do filho — o filho nunca decide "voltar" para o pai.

### Inversão de Controle e o Princípio de Hollywood — item (d)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Um Template Method com um único método-gancho, mas que impõe quinze passos obrigatórios e inalteráveis entre a validação e a chamada do gancho, seria um exemplo do risco de "camisa de força" mencionado na aula, mesmo respeitando a sintaxe do padrão corretamente.

**Resposta:** Verdadeiro

**Justificativa:** O padrão continuar sintaticamente correto (`final` + `abstract`) não impede que o esqueleto seja mal projetado na prática; se os passos fixos forem excessivos ou inadequados para alguns dos filhos, o Template Method se torna uma camisa de força mesmo estando implementado "certo" tecnicamente — o risco é de design, não de sintaxe.

### Vantagens e Riscos do Template Method — item (a)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Se uma nova subclasse `Cripto` for adicionada ao sistema um ano depois da aula, sem que o desenvolvedor releia a documentação do Template Method, o passo de `registrarLog()` ainda vai rodar corretamente para ela.

**Resposta:** Verdadeiro

**Justificativa:** É a garantia de previsibilidade do padrão: como o esqueleto é `final` e vive na classe base, `registrarLog()` roda para toda subclasse, presente ou futura, independentemente de o desenvolvedor da subclasse conhecer ou lembrar dessa regra — a garantia está na estrutura, não na disciplina do programador.

### Vantagens e Riscos do Template Method — item (b)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se `Pix`, `Boleto` e `Cartao` cada um sobrescrevesse seu próprio método `realizarPagamento()` completo (em vez de usar o esqueleto da base), mudar a regra de log exigiria editar três lugares em vez de um.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente o custo de não usar Template Method: sem um esqueleto centralizado na base, cada subclasse duplica a lógica de log, e uma mudança na regra precisa ser replicada em cada uma — o ganho de manutenibilidade do padrão vem de centralizar essa lógica compartilhada num único lugar.

### Vantagens e Riscos do Template Method — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Exige que o desenvolvedor de cada subclasse conheça o fluxo inteiro do algoritmo, não só seu gancho.

**Resposta:** Falso

**Justificativa:** É o oposto — a "limitação do erro" listada como vantagem na aula é justamente que o desenvolvedor da subclasse só precisa conhecer o gancho que vai implementar, sem precisar entender ou tocar no fluxo geral controlado pela base.

### Vantagens e Riscos do Template Method — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ É um mecanismo de Inversão de Controle: a base chama o filho, não o contrário.

**Resposta:** Verdadeiro

**Justificativa:** É a definição de IoC aplicada ao Template Method — o "Princípio de Hollywood" resumido na aula: a base retém o fluxo e chama o gancho do filho no momento certo, nunca o contrário.

### Síntese: Herança como Ferramenta de Especialização — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Herança bem usada exige DNA compartilhado real, não apenas o desejo de reaproveitar código.

**Resposta:** Verdadeiro

**Justificativa:** É a síntese da distinção entre herança por conveniência e especialização legítima que atravessa a aula inteira: reaproveitar código sozinho nunca justifica `extends`.

### Síntese: Herança como Ferramenta de Especialização — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Uma subclasse `PixPremium` que estende `Pix` apenas para renomear o método `criarCobranca()` para `criarCobrancaPremium()`, sem adicionar nenhum campo ou comportamento novo, e mantendo o mesmo contrato, é uma especialização legítima porque ainda compartilha o DNA do pai.

**Resposta:** Falso

**Justificativa:** Compartilhar o DNA é só uma das duas condições; renomear um método sem adicionar valor nem justificar tratamento polimórfico diferenciado é o próprio "objeto zumbi" descrito na aula — a subclasse existe, mas não agrega nada à taxonomia, só a polui.

### Síntese: Herança como Ferramenta de Especialização — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Blindar a base (atributos `private`, métodos `final`, ganchos `abstract`) reduz o risco de Classe Base Frágil.

**Resposta:** Verdadeiro

**Justificativa:** É a conexão entre os dois blocos centrais da aula: as três medidas de blindagem existem precisamente para impedir os tipos de violação silenciosa de invariante que caracterizam o Problema da Classe Base Frágil.

### Síntese: Herança como Ferramenta de Especialização — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O acoplamento gerado pela herança é, em geral, mais fraco do que o gerado por composição simples.

**Resposta:** Falso

**Justificativa:** É o oposto do que a aula estabelece desde a abertura: a herança é "o acoplamento mais forte da Orientação a Objetos", justamente por incorporar estrutura física, e não apenas guardar uma referência externa como a composição.
