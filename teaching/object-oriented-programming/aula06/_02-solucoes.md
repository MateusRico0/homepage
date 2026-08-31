# Soluções — Questões de Verdadeiro/Falso (Aula 6)

> Arquivo de apoio, não publicado (prefixo `_`). Contém a resposta e a
> justificativa de cada item das 12 questões de V/F do `index.qmd`. O
> `index.qmd` publicado continua sem solução — este arquivo existe só
> para conferência do professor/monitor, seguindo a metodologia de
> criação de questões definida em `../../CLAUDE.md`.

### Interface como Contrato de Comportamento — item (a)

**Heurística:** Transferência

**Afirmação:** ✔ Numa interface `Voador` usada tanto por uma classe `Passaro` quanto por uma classe `Drone`, o contrato exige apenas o método `voar()` — nada nele obriga as duas classes a compartilharem qualquer atributo interno.

**Resposta:** Verdadeiro

**Justificativa:** É a definição de interface como Contrato de Comportamento aplicada a um domínio novo: `Passaro` e `Drone` não têm nenhum dado em comum (um bate asas, o outro usa motores), mas a interface só exige que ambos saibam `voar()` — o contrato é sobre o que fazem, nunca sobre o que guardam.

### Interface como Contrato de Comportamento — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Métodos de interface, em Java, terminam com corpo de implementação obrigatório.

**Resposta:** Falso

**Justificativa:** Métodos abstratos de interface terminam em `;`, sem corpo — é exatamente a ausência de implementação que caracteriza a interface como abstração pura. (Métodos `default`/`static`/`private`, vistos mais adiante na aula, são a exceção que tem corpo, mas não são obrigatórios.)

### Interface como Contrato de Comportamento — item (c)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se uma classe implementasse apenas dois dos três métodos declarados por uma interface, deixando o terceiro sem corpo e sem a própria classe ser declarada `abstract`, o código ainda compilaria normalmente, desde que `@Override` estivesse presente nos dois métodos implementados.

**Resposta:** Falso

**Justificativa:** Java exige que toda classe concreta (não `abstract`) implemente *todos* os métodos abstratos do contrato. `@Override` nos dois métodos feitos não compensa o terceiro ausente — o compilador rejeita a classe até que ela implemente o método restante ou seja declarada `abstract`.

### Interface como Contrato de Comportamento — item (d)

**Heurística:** Limite

**Afirmação:** ✗ No limite em que a anotação `@Override` é removida de um método que de fato sobrescreve um método da interface, o comportamento em tempo de execução (qual método é chamado) muda.

**Resposta:** Falso

**Justificativa:** `@Override` é puramente uma verificação em tempo de compilação — ela avisa o compilador para confirmar que o método realmente sobrescreve algo do contrato. Removê-la não altera em nada o *dispatch* em tempo de execução; o método continua sendo chamado exatamente da mesma forma.

### Interface como Tipo Puro — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ A interface é chamada de "Tipo Puro" porque não impõe hierarquia de herança de estrutura.

**Resposta:** Verdadeiro

**Justificativa:** Diferente da herança de classes, que compartilha "DNA" (estrutura, estado, implementação da classe-mãe), a interface funciona como um "crachá": qualquer classe, de qualquer hierarquia, pode assinar o contrato sem herdar nenhuma estrutura de dados.

### Interface como Tipo Puro — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Duas classes de famílias completamente diferentes podem compartilhar o mesmo tipo, desde que implementem a mesma interface.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente o caso de `Pix` (lógica de QR Code) e `CartaoDeCredito` (lógica de criptografia de chip) apresentado na aula: sem nada em comum em termos de dados, ambos são do tipo `Pagavel` para o `CheckoutController`.

### Interface como Tipo Puro — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Numa aplicação que precisa que tanto uma classe `VeiculoEletrico` quanto uma classe `Gerador` (duas famílias completamente diferentes de objetos) sejam tratadas como `Recarregavel`, implementar uma interface comum resolveria isso sem exigir que ambas compartilhem uma superclasse.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma lógica do "crachá" aplicada a um domínio novo: `VeiculoEletrico` e `Gerador` não precisam de nenhuma superclasse em comum — basta que ambos implementem `Recarregavel` para serem tratados como o mesmo tipo por quem só precisa recarregá-los.

### Interface como Tipo Puro — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Herança de classe e implementação de interface são exatamente o mesmo mecanismo em Java.

**Resposta:** Falso

**Justificativa:** São mecanismos deliberadamente diferentes: herança de classe (`extends`) compartilha estrutura/estado/implementação e é limitada a uma única superclasse; implementação de interface (`implements`) só compartilha um contrato de comportamento e permite múltiplas interfaces por classe.

### Interfaces Modernas: Default, Static, Private — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se, em vez de usar `default`, a nova funcionalidade `processarComLog` fosse adicionada como um método abstrato comum na interface `Pagavel`, todas as classes existentes que já implementam `Pagavel` (como `Pix`) continuariam compilando sem nenhuma alteração.

**Resposta:** Falso

**Justificativa:** Um novo método abstrato quebra toda classe já existente que implementa a interface, porque nenhuma delas o implementou ainda — todas parariam de compilar até serem atualizadas. É exatamente esse problema de retrocompatibilidade que o método `default` resolve, fornecendo uma implementação padrão que as classes legadas herdam automaticamente.

### Interfaces Modernas: Default, Static, Private — item (b)

**Heurística:** Limite

**Afirmação:** ✗ No limite em que uma interface só contém métodos `static` (nenhum método abstrato, nenhum `default`), ainda seria possível instanciar essa interface diretamente com `new`, já que ela não teria mais nenhum método pendente de implementação.

**Resposta:** Falso

**Justificativa:** Interfaces nunca podem ser instanciadas com `new` em Java, independentemente de quantos métodos abstratos restam — essa é uma regra da linguagem sobre o que uma interface *é* (um tipo, não uma classe concreta), não uma consequência de haver ou não métodos pendentes de implementação.

### Interfaces Modernas: Default, Static, Private — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Métodos `private` em interfaces (Java 9+) servem para compartilhar lógica auxiliar entre métodos `default`.

**Resposta:** Verdadeiro

**Justificativa:** É o papel dos métodos `private` de interface: organizam código interno (como a validação usada por `processarComLog`) sem expor esse detalhe como parte do contrato público, evitando duplicação entre diferentes métodos `default` da mesma interface.

### Interfaces Modernas: Default, Static, Private — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ A introdução de `default methods` obriga todas as classes legadas a serem recompiladas e alteradas manualmente.

**Resposta:** Falso

**Justificativa:** É exatamente o oposto do propósito dos métodos `default`: eles permitem evoluir a interface sem quebrar implementações legadas, porque toda classe existente herda automaticamente o comportamento padrão sem precisar de nenhuma alteração manual.

### O Paradoxo do Mutador Cego — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Uma interface pode orquestrar transições de estado, mesmo sem possuir atributos de instância próprios.

**Resposta:** Verdadeiro

**Justificativa:** É a definição do Mutador Cego: um método `default` como `aplicarJuros` orquestra a mudança de estado chamando `getSaldo()`/`setSaldo()` (implementados pela classe concreta), sem que a interface precise guardar nada por conta própria.

### O Paradoxo do Mutador Cego — item (b)

**Heurística:** Transferência

**Afirmação:** ✔ Numa interface `ValidadorDeSenha` com um método `default validar()` que aplica regras de comprimento e complexidade chamando `getSenhaAtual()` (abstrato), a classe concreta que armazena a senha real desempenha o papel dos "músculos", enquanto a interface continua sendo o "cérebro" da regra.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma divisão de trabalho vista em `aplicarJuros`/`Pix`, transposta para um domínio novo: a interface concentra a regra de validação (o "cérebro"), e a classe concreta concentra o armazenamento real da senha (os "músculos"), sem que a interface precise saber onde ou como esse dado é guardado.

### O Paradoxo do Mutador Cego — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O método `default aplicarJuros` sabe exatamente onde e como o saldo está fisicamente armazenado.

**Resposta:** Falso

**Justificativa:** É o oposto do padrão Mutador Cego: `aplicarJuros` só chama `getSaldo()`/`setSaldo()` sem saber se o saldo mora numa variável privada, num banco de dados ou num serviço remoto — a interface age "às cegas", confiando que a classe concreta implementou esses dois métodos corretamente.

### O Paradoxo do Mutador Cego — item (d)

**Heurística:** Limite

**Afirmação:** ✗ No limite em que só existe uma única classe implementando `Pagavel` em todo o sistema, centralizar `aplicarJuros` como `default` na interface, em vez de deixá-lo como método comum daquela única classe, ainda traria o mesmo ganho de evitar duplicação de código.

**Resposta:** Falso

**Justificativa:** O ganho de DRY do método `default` só se materializa quando existem *múltiplas* implementações compartilhando a mesma regra. Com uma única classe implementando `Pagavel`, não há nada para duplicar — o método poderia estar tanto na interface quanto na própria classe sem qualquer diferença prática de duplicação.

### Interface vs. Classe Abstrata — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se uma interface Java declarasse um atributo `public static final int LIMITE = 10`, isso contradiria a regra de que interfaces não podem ter estado.

**Resposta:** Falso

**Justificativa:** A tabela da aula já prevê essa exceção: interfaces podem ter atributos `public static final` (constantes de tipo, compartilhadas por todas as instâncias, sem estado mutável por objeto). O que permanece proibido é o atributo de *instância* — algo que cada objeto guardaria com um valor próprio e mutável.

### Interface vs. Classe Abstrata — item (b)

**Heurística:** Transferência

**Afirmação:** ✔ Numa aplicação de jogos em que uma classe `PersonagemVoador` precisa herdar atributos físicos comuns de uma classe abstrata `Personagem` e, ao mesmo tempo, prometer comportamentos de `Voador` e de `Nadador`, ela pode declarar `extends Personagem implements Voador, Nadador` na mesma linha.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente a combinação prevista na tabela: herança de classe é única (`extends` só aceita uma classe abstrata), mas implementação de interface é múltipla (`implements` aceita várias) — as duas coisas podem coexistir na mesma declaração.

### Interface vs. Classe Abstrata — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Interfaces definem uma identidade ("o que é"); classes abstratas definem um papel ("o que faz").

**Resposta:** Falso

**Justificativa:** É o mapeamento invertido: segundo a tabela da aula, é a classe abstrata que define uma *identidade* ("o que é" um objeto, com estado compartilhado), e a interface que define um *papel*/capacidade ("o que faz", sem nenhum estado). Trocar os dois é a armadilha central deste item.

### Interface vs. Classe Abstrata — item (d)

**Heurística:** Transferência

**Afirmação:** ✔ Num sistema bancário em que `ContaCorrente` e `ContaPoupanca` compartilham o atributo protegido `saldo` e a lógica de validação de saque, mas cada uma tem regras de rendimento completamente diferentes, uma classe abstrata `ContaBancaria` (não uma interface) é a ferramenta mais adequada para compartilhar esse estado protegido.

**Resposta:** Verdadeiro

**Justificativa:** É a diretriz de design da aula aplicada a um caso concreto: como há estrutura de dados (`saldo`) e comportamento comum a proteger e compartilhar entre as duas contas, a classe abstrata é a ferramenta certa — uma interface não poderia guardar `saldo` como atributo de instância.

### Tipos como Comportamento — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ O tipo de um objeto orientado a objetos é definido pelas mensagens às quais ele responde, não pelo que ele guarda.

**Resposta:** Verdadeiro

**Justificativa:** É a tese central do bloco "Tipos são comportamento, não DNA": ao declarar `Pagavel p`, o que importa é que `p` sabe responder a `criarCobranca()`/`pagamentoConfirmado()`, não que tipo de dado ele guarda por dentro.

### Tipos como Comportamento — item (b)

**Heurística:** Transferência

**Afirmação:** ✔ Numa hierarquia de coleções, `ArrayList` e `HashMap` não compartilham nenhuma superclasse de dados em comum além de `Object`, mas ambas poderiam implementar uma interface `Limpavel` com um método `limpar()`, tornando-as do mesmo tipo `Limpavel` para quem só precisa chamar esse método.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma lógica de `Pix`/`CartaoDeCredito` aplicada a classes reais do Java: apesar de estruturas internas completamente diferentes (lista vs. tabela hash), ambas podem ser tratadas como o mesmo tipo `Limpavel` por qualquer código que só precise invocar esse comportamento.

### Tipos como Comportamento — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Declarar uma variável como `Pagavel` informa ao compilador exatamente qual classe concreta ela contém.

**Resposta:** Falso

**Justificativa:** O tipo declarado (`Pagavel`) é só o contrato mínimo garantido pelo compilador; a classe concreta real por trás da variável (`Pix`, `Boleto`, `Cartao`) só é conhecida em tempo de execução — é justamente essa lacuna que o Polimorfismo, na próxima aula, formaliza.

### Tipos como Comportamento — item (d)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se o `CheckoutController` declarasse a variável `formaEscolhida` como `Pix` em vez de `Pagavel`, mesmo que hoje só `Pix` fosse usado na prática, isso já eliminaria a vantagem de programar para a abstração caso um `Cripto implements Pagavel` surgisse amanhã.

**Resposta:** Verdadeiro

**Justificativa:** Declarar o tipo concreto em vez da abstração amarra o `CheckoutController` a `Pix` especificamente; se `Cripto` surgir depois, o controlador precisaria ser reescrito, exatamente o retrabalho que programar para `Pagavel` evita.

### Os Limites do Sistema de Tipos — item (a)

**Heurística:** Limite

**Afirmação:** ✔ No limite em que o parâmetro fosse declarado como um tipo customizado `ValorMonetario` (em vez de `double` primitivo) que só pudesse ser construído com valores positivos, a validação de negócio migraria do corpo do método para o próprio sistema de tipos, em tempo de compilação.

**Resposta:** Verdadeiro

**Justificativa:** Se `ValorMonetario` só puder ser instanciado com valores válidos (validação no construtor do próprio tipo), então é impossível construir uma instância inválida em primeiro lugar — a checagem deixa de ser uma exceção lançada em tempo de execução e passa a ser garantida estruturalmente antes mesmo de o método ser chamado.

### Os Limites do Sistema de Tipos — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Um preço negativo passado para `criarCobranca(double valor)` é rejeitado automaticamente pelo compilador.

**Resposta:** Falso

**Justificativa:** O compilador só verifica que o argumento é sintaticamente um `double` — um `-50.0` é um `double` perfeitamente válido do ponto de vista do compilador. É por isso que a validação semântica (`valor <= 0`) precisa ser feita explicitamente em tempo de execução, com uma exceção.

### Os Limites do Sistema de Tipos — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Num sistema de reservas de voos que aceita um parâmetro `int quantidadeAssentos`, um valor negativo passa a validação de tipo do compilador da mesma forma que um valor positivo — a mesma lacuna do sistema de tipos vista para o valor de pagamento desta aula se repete aqui.

**Resposta:** Verdadeiro

**Justificativa:** A mesma lacuna estrutural se repete em qualquer domínio: o compilador garante o tipo (`int`), nunca a validade semântica do valor dentro desse tipo — reservar `-3` assentos "compila" tão bem quanto reservar `3`.

### Os Limites do Sistema de Tipos — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Uma exceção é uma forma de o objeto dizer "recebi o tipo certo, mas os dados violam minhas regras".

**Resposta:** Verdadeiro

**Justificativa:** É a síntese do papel da exceção nesta aula: ela entra em cena exatamente quando o sistema de tipos já foi satisfeito (o `double` foi recebido) mas o valor, semanticamente, viola uma regra de negócio que o tipo sozinho não conseguia expressar.

### Fail-Fast e o Erro de Silenciar — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Retornar `null`, `0` ou `false` para sinalizar erro é uma boa prática recomendada nesta aula.

**Resposta:** Falso

**Justificativa:** É exatamente o oposto do que a aula defende: retornar um valor "de ajuda" para sinalizar erro é descrito como o maior pecado em Orientação a Objetos, porque só empurra o problema para um ponto distante e sem relação óbvia com a causa original.

### Fail-Fast e o Erro de Silenciar — item (b)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se, em vez de lançar a exceção imediatamente ao detectar `valor <= 0`, o método `criarCobranca` apenas registrasse o erro num log interno e continuasse a execução normalmente até o fim, isso ainda seria uma aplicação válida da filosofia Fail-Fast.

**Resposta:** Falso

**Justificativa:** Fail-Fast significa interromper o fluxo no exato momento da violação, não continuar executando e só deixar um rastro em log. Continuar a execução normalmente após detectar a violação é justamente o "erro de silenciar" disfarçado de log — o problema segue adiante sem ser contido.

### Fail-Fast e o Erro de Silenciar — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Falhas silenciosas tendem a se manifestar mais tarde, em pontos distantes da causa raiz do problema.

**Resposta:** Verdadeiro

**Justificativa:** É a consequência prática do "erro de silenciar": um `null` retornado hoje só vira um `NullPointerException` quando alguém, mais tarde e em outro lugar do código, tentar usá-lo — sem relação evidente com o método original que causou o problema.

### Fail-Fast e o Erro de Silenciar — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Lançar uma exceção no ponto exato da violação facilita o rastreamento via *stack trace*.

**Resposta:** Verdadeiro

**Justificativa:** Ao interromper o fluxo imediatamente, a exceção captura o *stack trace* no ponto exato da causa, preservando a informação necessária para o diagnóstico — o benefício direto de agir Fail-Fast em vez de silenciar o erro.

### Try-Catch como Barreira de Contenção — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ O bloco `try-catch` no `CheckoutController` protege a experiência do usuário contra falhas de baixo nível.

**Resposta:** Verdadeiro

**Justificativa:** É a função de uma barreira de contenção bem posicionada: capturar a exceção lançada por um componente de baixo nível (`Pix`, `Cartao`) e traduzi-la numa resposta controlada para o usuário, em vez de deixar o sistema quebrar de forma bruta.

### Try-Catch como Barreira de Contenção — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Segundo a diretriz desta aula, componentes de baixo nível devem capturar e silenciar suas próprias exceções.

**Resposta:** Falso

**Justificativa:** É o inverso da diretriz explícita da aula: componentes de baixo nível devem *lançar* exceções (ser honestos sobre a falha); são os componentes de alto nível que devem decidir como reagir — capturar e silenciar no próprio nível baixo reintroduziria o "erro de silenciar".

### Try-Catch como Barreira de Contenção — item (c)

**Heurística:** Limite

**Afirmação:** ✗ No limite em que não existe nenhum componente de alto nível entre o objeto que lança a exceção e o usuário final (a exceção se propaga direto até a interface), a aplicação da diretriz desta aula ainda garantiria uma mensagem de erro tratada e amigável para o usuário.

**Resposta:** Falso

**Justificativa:** A diretriz depende de existir alguém no alto nível para capturar e traduzir a exceção; sem esse componente intermediário, a exceção se propaga sem tratamento até o usuário, tipicamente como uma tela de erro bruta (*stack trace* cru), não uma mensagem tratada.

### Try-Catch como Barreira de Contenção — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Um `catch` bem posicionado evita que uma falha externa (rede, banco) derrube o fluxo principal do sistema.

**Resposta:** Verdadeiro

**Justificativa:** É a essência da barreira de contenção: falhas vindas de fatores externos ao controle direto do sistema são contidas no ponto certo, evitando que se propaguem e interrompam o funcionamento do restante da aplicação.

### Novos Contratos: Notificação, Desconto, Logística — item (a)

**Heurística:** Transferência

**Afirmação:** ✔ Numa aplicação de streaming de vídeo que hoje só grava logs de erro em arquivo local, trocar para uma interface `Logavel` implementada por um adaptador de nuvem seguiria a mesma lógica de `Notificavel`: o consumidor do log não precisa mudar uma linha.

**Resposta:** Verdadeiro

**Justificativa:** É o mesmo padrão de `Notificavel` (o canal deixa de importar) aplicado a um domínio novo: programar contra `Logavel`, e não contra "arquivo local" especificamente, é o que permite trocar a implementação de destino sem tocar em quem gera os logs.

### Novos Contratos: Notificação, Desconto, Logística — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Um `double desconto` isolado, sem uma interface `EstrategiaDesconto`, já protege contra valores absurdos como 500%.

**Resposta:** Falso

**Justificativa:** Um `double` sozinho aceita qualquer valor numérico, incluindo `5.0` (500%) — é exatamente a lacuna que motiva encapsular a regra numa interface `EstrategiaDesconto` com validação própria, em vez de confiar num primitivo isolado.

### Novos Contratos: Notificação, Desconto, Logística — item (c)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se, em vez de uma interface `ServicoLogistico`, o `Pedido` chamasse diretamente uma classe concreta `TransportadoraCorreios` para gerar o código de rastreio, trocar de transportadora no futuro não exigiria nenhuma alteração em `Pedido`.

**Resposta:** Falso

**Justificativa:** Sem a interface, `Pedido` ficaria fisicamente acoplado a `TransportadoraCorreios` — trocar de transportadora exigiria editar `Pedido` diretamente, o mesmo problema de acoplamento a classes concretas visto no DIP da Aula 5. A interface é justamente o que evita essa dependência direta.

### Novos Contratos: Notificação, Desconto, Logística — item (d)

**Heurística:** Limite

**Afirmação:** ✗ No limite em que um método de interface declara `throws Exception` (a superclasse mais genérica possível) em vez de uma exceção específica como `CarrierUnavailableException`, a cláusula do contrato continua igualmente informativa sobre como e por que o método pode falhar.

**Resposta:** Falso

**Justificativa:** Uma exceção genérica (`Exception`) não comunica nada específico sobre o motivo da falha, enquanto `CarrierUnavailableException` já indica, pelo próprio nome, a natureza do problema — quanto mais genérica a exceção declarada, menos informativa é a cláusula do contrato para quem precisa tratá-la.

### Exceção como Cláusula de Contrato — item (a)

**Heurística:** Transferência

**Afirmação:** ✔ Numa API de pagamento internacional que declara `throws CurrencyConversionException`, isso avisa ao consumidor da API que a conversão de moeda pode falhar por fatores fora do controle do próprio método (ex.: serviço de cotação indisponível), da mesma forma que `criarCobranca` avisa sobre falhas de validação.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma função de cláusula de contrato, só que sinalizando uma falha de origem externa (dependência de terceiros) em vez de uma falha de validação de entrada — em ambos os casos, o `throws` avisa formalmente que o método pode não cumprir sua promessa.

### Exceção como Cláusula de Contrato — item (b)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se um método lançasse uma exceção apenas para simular uma falha que nunca ocorre de fato na prática, isso ainda seria consistente com a ideia de exceção como "honestidade sobre um risco real".

**Resposta:** Falso

**Justificativa:** A "honestidade" da exceção pressupõe um risco real de falha que o método está comunicando ao consumidor do contrato. Declarar uma exceção para uma falha que nunca ocorre de fato é ruído no contrato, não honestidade — é o inverso do propósito descrito na aula.

### Exceção como Cláusula de Contrato — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Num sistema de pagamento que, ao receber uma `IllegalArgumentException` de um valor inválido, registra o erro, notifica o usuário e continua processando os próximos pedidos da fila sem interromper o serviço inteiro, isso demonstra o mesmo ato de resiliência descrito nesta aula para o tratamento de exceções.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente o papel do alto nível descrito na aula: capturar a exceção lançada pelo baixo nível e decidir como reagir (registrar, notificar, seguir adiante) sem que a falha de um pedido derrube o processamento dos demais — resiliência do sistema como um todo.

### Exceção como Cláusula de Contrato — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Uma vez capturada, uma exceção deve sempre ser ignorada silenciosamente para não incomodar o usuário.

**Resposta:** Falso

**Justificativa:** É o "erro de silenciar" reaparecendo depois do `catch`: capturar a exceção só para descartá-la sem reação nenhuma reproduz o mesmo problema de esconder a falha, só que uma etapa depois. A diretriz da aula é decidir como reagir, não ignorar.

### Síntese: Contratos e Responsabilidade — item (a)

**Heurística:** Limite

**Afirmação:** ✗ No limite em que `Pedido` dependesse de dez interfaces diferentes em vez de três, o princípio de que `Pedido` "não sabe como", só "confia no contrato", deixaria de valer, porque o número de dependências já seria alto demais para manter esse desacoplamento.

**Resposta:** Falso

**Justificativa:** O princípio de "não saber como" é sobre o *tipo* de dependência (uma abstração, não uma implementação concreta), não sobre a *quantidade* de dependências. Mesmo com dez interfaces, `Pedido` continuaria confiando nos contratos sem conhecer nenhum detalhe de implementação — o número alto poderia levantar uma preocupação de CBO (Aula 5), mas não invalida o encapsulamento garantido pelas interfaces.

### Síntese: Contratos e Responsabilidade — item (b)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se `EstrategiaDesconto` não declarasse `throws` nem lançasse nenhuma exceção em caso de valor inválido, apenas retornando `0` (desconto nulo) silenciosamente, `Pedido` ainda estaria recebendo a mesma garantia de honestidade do contrato que as demais interfaces desta aula oferecem.

**Resposta:** Falso

**Justificativa:** Retornar `0` silenciosamente em vez de lançar uma exceção é exatamente o "erro de silenciar" da aula — quebra a garantia de honestidade que as outras interfaces (`Notificavel`, `ServicoLogistico`) mantêm ao declarar explicitamente suas possíveis falhas via `throws`.

### Síntese: Contratos e Responsabilidade — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Programar contra interfaces e proteger regras com exceções são práticas independentes, sem relação entre si.

**Resposta:** Falso

**Justificativa:** As duas práticas se combinam na mesma aula: a interface define o "o quê" (o contrato de comportamento), e a exceção guarda os limites que o "o quê" não consegue expressar sozinho — juntas, formam o padrão "interface + exceção" repetido em `Notificavel`, `EstrategiaDesconto` e `ServicoLogistico`.

### Síntese: Contratos e Responsabilidade — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Esse design permite trocar implementações concretas em tempo de execução sem alterar o núcleo do sistema.

**Resposta:** Verdadeiro

**Justificativa:** É o resultado prático de programar contra interfaces: `Pedido` nunca conhece `Pix`, `Boleto` ou qualquer implementação específica de `Notificavel`/`EstrategiaDesconto`/`ServicoLogistico` — pode-se trocar qualquer uma delas sem tocar em `Pedido`, o mesmo ganho estrutural do DIP na Aula 5, agora viabilizado tecnicamente por interfaces.
