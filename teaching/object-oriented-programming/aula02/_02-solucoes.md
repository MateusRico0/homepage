# Soluções — Questões de Verdadeiro/Falso (Aula 2)

> Arquivo de apoio, não publicado (prefixo `_`). Contém a resposta e a
> justificativa de cada item das 12 questões de V/F do `index.qmd`. O
> `index.qmd` publicado continua sem solução — este arquivo existe só
> para conferência do professor/monitor, seguindo a metodologia de
> criação de questões definida em `../../CLAUDE.md`.

### Estado, Comportamento e Identidade (revisitados) — item (a)

**Heurística:** Limite

**Afirmação:** Um objeto sem nenhum atributo (nenhum campo mutável) não possui Estado algum, já que não haveria nada para variar ao longo do tempo.

**Resposta:** Falso

**Justificativa:** O Estado é o conjunto de valores dos atributos num dado instante; mesmo que esse conjunto seja vazio (zero campos), ele ainda é um conjunto bem definido — só que trivial e constante. "Não ter atributos" corresponde a uma máquina de um único estado (sem transições possíveis), não à ausência de Estado. O aluno que confunde "estado invariável" com "inexistência de estado" está tratando a cardinalidade do espaço de estados como se fosse a própria noção de Estado.

### Estado, Comportamento e Identidade (revisitados) — item (b)

**Heurística:** Transferência

**Afirmação:** Usando reflection (`java.lang.reflect`), é possível alterar um atributo `private` diretamente, sem passar por nenhum método — o que mostra que "Comportamento como única via de mutação" é uma convenção de projeto, não uma barreira física imposta pela JVM.

**Resposta:** Verdadeiro

**Justificativa:** A API de reflection permite obter um `Field`, chamar `setAccessible(true)` e escrever diretamente no atributo, ignorando qualquer método da classe. Isso comprova que o encapsulamento em Java é uma garantia de nível de linguagem/API (respeitada pelo compilador e pelo acesso "normal" ao código), não uma restrição absoluta e inquebrável imposta pela JVM em tempo de execução. Quem responde que reflection "não deveria funcionar porque o campo é private" confunde a barreira de compilação com uma barreira de execução.

### Struct Passivo vs. Agente Ativo — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** Em C, uma `struct` agrupa dados e as funções que operam sobre eles na mesma unidade.

**Resposta:** Falso

**Justificativa:** Esta é exatamente a descrição do que ocorre em Java (classe = dados + métodos), atribuída erradamente a C. Em C, a `struct` só agrupa dados; as funções que a manipulam são declaradas em outro lugar, sem nenhum vínculo sintático com o tipo. Confundir os dois paradigmas é o erro central que a aula tenta prevenir: achar que "agrupar campos" já é, por si, o mesmo que "encapsulamento forte".

### Struct Passivo vs. Agente Ativo — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** Se a função que manipula uma `struct` em C for declarada `static` no mesmo arquivo-fonte da struct, ela deixa de ser "externa" e a struct passa a ter o mesmo encapsulamento forte de uma classe Java.

**Resposta:** Falso

**Justificativa:** `static` em C só restringe a *linkagem* da função a uma unidade de tradução (o próprio arquivo) — não cria nenhum vínculo do tipo "esta função pertence a este tipo" como uma classe Java tem com seus métodos. Continua não havendo nenhum mecanismo de linguagem que impeça outro código do mesmo arquivo de manipular os campos da struct diretamente, nem a struct passa a poder recusar uma mutação inválida. Restringir a visibilidade textual não é o mesmo que encapsulamento orientado a objetos.

### Struct Passivo vs. Agente Ativo — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** Basta que os atributos de uma classe Java sejam `private` para que o objeto recuse automaticamente qualquer mutação que viole suas regras internas, mesmo que o método que os altera não contenha nenhuma verificação.

**Resposta:** Falso

**Justificativa:** `private` só bloqueia o acesso *direto* ao campo vindo de fora da classe — não valida nada por si só. Se o método público que altera o atributo não contiver nenhum `if` de guarda, qualquer chamada (mesmo com dado absurdo) passa livremente através desse método. A privacidade do campo é necessária, mas não suficiente: a recusa da mutação vem da lógica de validação escrita dentro do método, não da palavra-chave `private`.

### Struct Passivo vs. Agente Ativo — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** Uma classe cujos atributos são todos `public`, mas que também oferece métodos como `pagar()` com toda a validação de regras de negócio, ainda apresenta encapsulamento forte, desde que os programadores usem apenas esses métodos por convenção, e nunca acessem os atributos diretamente.

**Resposta:** Falso

**Justificativa:** Encapsulamento forte é uma garantia *imposta pela linguagem*, não uma disciplina de equipe. Se os atributos são `public`, nada no compilador ou na JVM impede qualquer código de alterá-los diretamente, ignorando `pagar()` por completo — basta um único desenvolvedor não seguir a convenção (ou um bug, ou uma biblioteca de terceiros) para que a garantia desapareça. "Todos concordam em não fazer isso" é o oposto do que o encapsulamento existe para eliminar: a necessidade de confiar na boa vontade de quem usa a classe.

### O Modelo de Domínio Anêmico — item (a)

**Heurística:** Limite

**Afirmação:** Uma classe com atributos `private`, apenas getters e nenhum setter (os atributos só podem ser lidos, nunca alterados após a construção), ainda se qualifica como Modelo de Domínio Anêmico.

**Resposta:** Verdadeiro

**Justificativa:** O defeito do Modelo Anêmico não é ter setters especificamente — é a ausência de regra de negócio dentro da classe, a inteligência ter "vazado" para fora. Uma classe que só expõe dados sem nenhum método que decida algo por si (como `pagar()`, `vender()`) continua sendo uma "struct glorificada", mesmo sendo imutável e só de leitura. Quem responde Falso está confundindo o mecanismo mais citado do anti-padrão (setter cego) com sua causa real (zero comportamento).

### O Modelo de Domínio Anêmico — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** É considerado um design rico, pois maximiza a flexibilidade de quem consome a classe.

**Resposta:** Falso

**Justificativa:** "Flexibilidade" aqui é uma armadilha de vocabulário: dar a quem consome a classe liberdade total para ler e escrever qualquer atributo não é riqueza de design, é justamente a ausência de proteção que a aula chama de anti-padrão. Essa "flexibilidade" empurra para fora da classe a responsabilidade de manter a consistência dos dados — o oposto do que um bom design faz. O termo tecnicamente correto para essa característica ("Modelo Rico de Domínio") é o antônimo do Modelo Anêmico, não um sinônimo dele.

### O Modelo de Domínio Anêmico — item (c)

**Heurística:** Transferência

**Afirmação:** A classe `ProdutoBuilder`, cujos métodos internos (`comNome(...)`, `comPreco(...)`) apenas acumulam valores sem nenhuma validação, e cuja validação real só ocorre no método final `build()`, sofre exatamente do mesmo problema estrutural do Modelo Anêmico.

**Resposta:** Falso

**Justificativa:** No padrão Builder, os setters intermediários são deliberadamente "cegos" porque o objeto ainda está incompleto, em processo de montagem — a invariante é garantida no ponto certo, `build()`, que só devolve o objeto final se ele for válido. Isso é estruturalmente diferente do Modelo Anêmico, em que a entidade já "viva" no sistema aceita qualquer mutação a qualquer momento de sua vida útil, sem nenhum ponto central de validação. O Builder é uma técnica legítima de construção incremental; o Modelo Anêmico é um anti-padrão porque a entidade nunca protege sua própria invariante, nem na criação nem depois.

### O Modelo de Domínio Anêmico — item (d)

**Heurística:** Transferência

**Afirmação:** O design correto prefere métodos verbais de intenção (`pagar()`, `cancelar()`) a setters genéricos.

**Resposta:** Verdadeiro

**Justificativa:** Contrastando `Pedido.pagar()` (que decide internamente se a transição é legal) com `PedidoAnemico.setStatus(String s)` (que aceita qualquer string sem julgamento), fica claro que nomear o método pela intenção de negócio, em vez de pela mecânica de atribuição, é o que preserva a capacidade do objeto de guardar suas próprias regras. Um setter genérico delega a decisão para quem chama; um método de intenção mantém a decisão dentro do objeto.

### A Máquina de Estados Finita (DFA) — item (a)

**Heurística:** Limite

**Afirmação:** Um autômato com um número infinito de estados possíveis ainda seria, por definição, determinístico, desde que cada par (estado, evento) leve a exatamente um único próximo estado.

**Resposta:** Verdadeiro

**Justificativa:** Determinismo e finitude são propriedades independentes: determinismo depende só de a função de transição ser unívoca (um único próximo estado por par estado-evento), não do tamanho do conjunto de estados. Um autômato com infinitos estados, mas transição sempre única, seria determinístico — só deixaria de ser um DFA no sentido estrito, porque a definição de "Finite Automaton" exige, além do determinismo, que o conjunto de estados seja finito. O erro comum aqui é achar que "determinístico" e "finito" são a mesma exigência.

### A Máquina de Estados Finita (DFA) — item (b)

**Heurística:** Transferência

**Afirmação:** No DFA do `Produto` apresentado na aula, chamar `vender(quantidade)` com uma quantidade maior que o estoque, estando o produto em DISPONÍVEL, não corresponde a nenhuma transição definida no diagrama — por isso o método precisa lançar uma exceção em vez de deixar a máquina seguir para um estado inexistente.

**Resposta:** Verdadeiro

**Justificativa:** O diagrama de estados do `Produto` só define `vender(x<all)` (permanece em DISPONÍVEL) e `vender(all)` (vai para ESGOTADO); vender mais do que o estoque atual não tem nenhum destino previsto pela máquina. Como um DFA exige que toda combinação (estado, evento) leve a exatamente um estado, e essa combinação específica não tem destino legal no domínio de negócio, o código precisa recusar a chamada (`IllegalStateException`) em vez de deixar a máquina "vazar" para um estado matematicamente impossível (estoque negativo).

### A Máquina de Estados Finita (DFA) — item (c)

**Heurística:** Limite

**Afirmação:** Um DFA bem definido permite comportamentos "mágicos" e imprevisíveis em casos de borda.

**Resposta:** Falso

**Justificativa:** É exatamente o oposto da definição de determinismo: um DFA bem definido garante que, para cada par (estado, evento) — inclusive nos casos de borda, não só nos "normais" — existe exatamente um próximo estado conhecido. Não há espaço para comportamento "mágico"; se um caso de borda não tem transição definida, a resposta correta é recusar a operação (Fail-Fast), não improvisar um resultado imprevisível.

### A Máquina de Estados Finita (DFA) — item (d)

**Heurística:** Transferência

**Afirmação:** O determinismo de um DFA facilita a prova formal da corretude de um sistema.

**Resposta:** Verdadeiro

**Justificativa:** Assim como uma invariante de laço permite provar a corretude de um algoritmo por indução (inicialização, manutenção, término), o determinismo de uma máquina de estados garante que o comportamento do sistema para qualquer sequência de eventos é previsível e único — pré-requisito para qualquer argumento de prova formal. Se a mesma combinação (estado, evento) pudesse levar a resultados diferentes, não haveria uma única "trajetória" a se provar correta.

### A Máquina de Estados Encapsulada em Java — item (a)

**Heurística:** Transferência

**Afirmação:** Um atributo declarado `static` numa classe Java não faz parte do "nó" de estado de nenhuma instância individual da máquina, porque seu valor é compartilhado por todos os objetos daquela classe, e não isolado por instância.

**Resposta:** Verdadeiro

**Justificativa:** O mapeamento "atributos privados = estado" da aula é sobre atributos de *instância*, que pertencem a cada objeto individualmente. Um campo `static` vive associado à classe como um todo, compartilhado por todas as instâncias — mudar seu valor não corresponde à transição de estado de um objeto específico, é uma variável fora do escopo da máquina de estados de qualquer instância isolada.

### A Máquina de Estados Encapsulada em Java — item (b)

**Heurística:** Limite

**Afirmação:** Uma classe cujos únicos métodos públicos, além do construtor, são getters (nenhum método além deles), ainda define uma máquina de estados capaz de alcançar mais de um estado depois de criado o objeto.

**Resposta:** Falso

**Justificativa:** Getters são Consultas (por CQS, sem efeito colateral); se não existe nenhum Comando público, nenhuma transição está disponível depois da construção. O objeto nasce em um estado e fica congelado nele para sempre — a máquina, na prática, tem um único estado alcançável (o de nascimento), mesmo que a classe tenha múltiplos atributos que "poderiam" assumir outros valores em teoria.

### A Máquina de Estados Encapsulada em Java — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** Uma classe cujo atributo `private List<Item> itens` é exposto só por um getter que devolve a referência direta à lista (`return this.itens;`), mantém o mesmo nível de proteção contra transições ilegais que um atributo `private` bem encapsulado, já que a lista nunca é declarada `public`.

**Resposta:** Falso

**Justificativa:** Mesmo com o campo `private`, devolver a referência real do objeto mutável pelo getter permite que qualquer código externo chame `.add()`/`.remove()` na lista devolvida e altere o estado interno diretamente, sem passar por nenhuma transição validada da classe. `private` protege a *variável* (a referência), não o objeto apontado por ela — é preciso devolver uma cópia ou uma view imutável para preservar de fato a garantia da máquina de estados.

### A Máquina de Estados Encapsulada em Java — item (d)

**Heurística:** Transferência

**Afirmação:** Um método público `restaurarEstado(EstadoSerializado dump)`, que copia todos os campos de um objeto externo `dump` diretamente para os atributos `private` do objeto, sem nenhuma validação, preserva a proteção do encapsulamento, mesmo aceitando dados vindos de fora do sistema (como um arquivo ou uma requisição de rede).

**Resposta:** Falso

**Justificativa:** O encapsulamento não é sobre de onde vem o dado (arquivo, rede, outro objeto) — é sobre se o método que recebe o dado valida a transição antes de aplicá-la. Um `restaurarEstado` que copia tudo sem checar nada é estruturalmente idêntico a um setter cego: qualquer dado corrompido vindo de fora entra direto no objeto e produz um "Objeto Zumbi", exatamente o problema que o Fail-Fast e a máquina de estados existem para evitar.

### Invariantes de Classe — item (a)

**Heurística:** Limite

**Afirmação:** Durante a execução do corpo de um método público — antes de chegar à instrução `return` —, a invariante de classe pode estar temporariamente violada, desde que seja restaurada até o momento em que o método devolve o controle para quem o chamou.

**Resposta:** Verdadeiro

**Justificativa:** A garantia de invariante (base da indução + passo indutivo) é sobre os pontos *observáveis* de fora da classe: o instante logo após o construtor e o instante logo após cada método retornar. Internamente, um método pode passar por estados intermediários inconsistentes (ex.: debitar de uma conta antes de creditar em outra, num método de transferência) — o que importa é que, quando o controle volta ao chamador, a invariante já esteja restabelecida.

### Invariantes de Classe — item (b)

**Heurística:** Contrafactual

**Afirmação:** Uma propriedade derivada, como o total de um carrinho, dispensa proteção por invariante.

**Resposta:** Falso

**Justificativa:** O fato de o total ser uma propriedade *derivada* (resultado de somar os itens, não uma entrada livre) não elimina a necessidade de proteção — pelo contrário, é exatamente por isso que ela não deveria ter um `setTotal(valor)`: a única forma segura de garantir "total = soma dos itens" é que a própria classe recalcule/atualize o total dentro do método de transição oficial (`adicionarItem`). Achar que "é derivada" significa "não precisa de invariante" inverte a lógica: é precisamente a invariante que define o que "derivada" quer dizer aqui.

### Invariantes de Classe — item (c)

**Heurística:** Limite

**Afirmação:** Numa `ContaBancaria` cujo atributo `saldo` é `public`, mas que hoje é manipulada por um único módulo em todo o sistema, o risco de quebrar a invariante desaparece, pois só existe um lugar de código que precisa lembrar de checar a regra.

**Resposta:** Falso

**Justificativa:** Mesmo com um único módulo acessando o campo hoje, a invariante continua sem nenhuma proteção estrutural: nada no código impede que um segundo módulo passe a acessar `saldo` diretamente no futuro, nem impede que o próprio módulo único tenha, em algum caminho interno, um ponto que esqueça de checar a regra. "Só um lugar checando hoje" não é o mesmo que "impossível de violar" — a proteção real só existe quando a regra vive dentro do objeto, não na disciplina (atual e temporária) de quem o usa.

### Invariantes de Classe — item (d)

**Heurística:** Transferência

**Afirmação:** Centralizar a regra da invariante dentro de um único método `synchronized` do próprio objeto garante, sozinho, que a invariante nunca será violada, mesmo que a classe tenha outros métodos públicos que também alterem o mesmo atributo sem essa palavra-chave.

**Resposta:** Falso

**Justificativa:** `synchronized` só serializa chamadas ao método que a declara; se existir qualquer outro método público que também altere o mesmo atributo sem `synchronized`, duas threads podem entrelaçar suas execuções por esse outro caminho e quebrar a invariante mesmo assim. Centralizar a regra ajuda, mas só protege de fato se *todos* os pontos de mutação do atributo passarem pelo mesmo mecanismo de exclusão — não basta proteger um único método e deixar outro caminho de mutação aberto.

### O Construtor como Base da Indução — item (a)

**Heurística:** Transferência

**Afirmação:** Numa classe cujo único meio de criação para o mundo externo é um método estático de fábrica (`Produto.criar(...)`), que internamente chama um construtor `private` sem nenhuma validação, a responsabilidade de servir como "base" da indução passa a ser do método de fábrica, e não do construtor em si.

**Resposta:** Verdadeiro

**Justificativa:** O papel de "base da indução" pertence a qualquer ponto de entrada pelo qual um objeto nasce e que seja efetivamente alcançável de fora da classe. Se o construtor é `private` e não valida nada, e a única via pública é o método de fábrica, é o corpo desse método de fábrica que precisa fazer a validação Fail-Fast antes de chamar o construtor — do contrário, a garantia $o \in V$ no nascimento simplesmente não existe em lugar nenhum do código.

### O Construtor como Base da Indução — item (b)

**Heurística:** Contrafactual

**Afirmação:** Um construtor permissivo, que aceita qualquer dado, é uma boa prática para evitar exceções.

**Resposta:** Falso

**Justificativa:** É exatamente o cenário do "Objeto Zumbi": um construtor permissivo não evita problemas, apenas os posterga e os torna mais difíceis de rastrear, porque o erro vai aparecer distante da causa real, num método qualquer que assumia (sem verificar de novo) que o objeto tinha nascido válido. "Evitar exceções" trocando-as por dados corrompidos silenciosos é uma troca ruim: o construtor deve recusar ativamente, não aceitar qualquer coisa.

### O Construtor como Base da Indução — item (c)

**Heurística:** Contrafactual

**Afirmação:** Lançar uma exceção no construtor impede que um "Objeto Zumbi" passe a existir na Heap.

**Resposta:** Verdadeiro

**Justificativa:** Se o construtor lança uma exceção Fail-Fast diante de dados inválidos, a construção do objeto é interrompida — a referência nunca chega a existir de forma utilizável pelo restante do programa. É exatamente o comportamento inverso do construtor permissivo (que cria o objeto mesmo com dados ruins, gerando o zumbi); a exceção é o mecanismo que garante a base da indução ($o \in V$) ao custo de nunca permitir que $o \notin V$ exista.

### O Construtor como Base da Indução — item (d)

**Heurística:** Limite

**Afirmação:** Numa classe totalmente imutável — todos os atributos `final`, sem nenhum método que altere o estado depois da construção —, o "passo indutivo" da prova por indução é trivialmente satisfeito, pois não existe nenhuma transição capaz de levar o objeto para fora do conjunto $V$ depois do nascimento.

**Resposta:** Verdadeiro

**Justificativa:** O passo indutivo exige mostrar que todo método público, aplicado a um objeto em $s_n \in V$, resulta em $s_{n+1} \in V$. Se não existe nenhum método capaz de mutar o estado (todos os atributos são fixados no construtor e nunca mais alterados), o conjunto de "métodos que poderiam violar a invariante" é vazio, e a implicação é satisfeita por vacuidade — toda a responsabilidade de manter a validade do objeto recai inteiramente sobre a base (o construtor), sem nenhum risco introduzido depois.

### CQS: Comandos vs. Consultas — item (a)

**Heurística:** Limite

**Afirmação:** O construtor de uma classe, por ser responsável por estabelecer o estado inicial do objeto, deve ser classificado como um Comando dentro da disciplina de CQS, já que ele também determina o estado do objeto.

**Resposta:** Falso

**Justificativa:** CQS classifica métodos chamados sobre um objeto *já existente*, decidindo entre "mudar o estado observável" (Comando) e "devolver um dado sem efeito colateral" (Consulta). O construtor não se encaixa nessa dicotomia porque não há um estado anterior a preservar ou consultar — ele é a base da indução, uma categoria à parte, responsável por levar o objeto de "não-existente" para "existente e válido", não uma transição entre dois estados já dentro de $V$.

### CQS: Comandos vs. Consultas — item (b)

**Heurística:** Transferência

**Afirmação:** Um método como `StringBuilder.append(String s)`, que muda o estado do objeto e também devolve a própria instância (`return this;`) para permitir encadeamento de chamadas (`sb.append(a).append(b)`), viola a recomendação estrita do CQS de que um Comando deve retornar `void`.

**Resposta:** Verdadeiro

**Justificativa:** Pela definição estrita de CQS apresentada na aula, um Comando deve sinalizar "isto muda o mundo" retornando `void`; `append()` muda o estado (adiciona ao buffer) e ainda devolve um valor (`this`), misturando os dois papéis. Na prática, esse é um desvio deliberado e amplamente aceito (padrão *fluent interface*/encadeamento de métodos), mas continua sendo, por definição, uma violação da regra estrita ensinada aqui — o valor devolvido não é um dado de consulta independente do estado, é a própria referência mutada.

### CQS: Comandos vs. Consultas — item (c)

**Heurística:** Transferência

**Afirmação:** Uma Consulta que lança uma exceção quando chamada em condições inválidas — como `Iterator.next()`, que lança `NoSuchElementException` se chamado sem checar `hasNext()` antes — deixa de ser uma Consulta e passa a se comportar como um Comando, já que alterou o fluxo normal do programa.

**Resposta:** Falso

**Justificativa:** O critério de CQS não é "o método pode alterar o fluxo de controle", é "o método pode alterar o estado observável do objeto". Lançar uma exceção ao detectar uma pré-condição violada é o comportamento Fail-Fast esperado de qualquer método (Comando ou Consulta) — não muda saldo, estoque ou qualquer outro atributo de negócio do objeto. `Iterator.next()` continua sendo uma Consulta: ela só se recusa a devolver um dado quando não há dado válido para devolver, o que é diferente de mutar o estado.

### CQS: Comandos vs. Consultas — item (d)

**Heurística:** Limite

**Afirmação:** Chamar uma Consulta livre de efeitos colaterais um milhão de vezes em sequência deixa o estado observável do objeto exatamente igual a como estava antes da primeira chamada.

**Resposta:** Verdadeiro

**Justificativa:** Por definição, uma Consulta em conformidade com CQS não tem nenhum efeito colateral sobre o estado do objeto; se cada chamada individual não altera nada, repetir a chamada qualquer número de vezes (uma ou um milhão) não pode acumular nenhuma mudança, porque não há nenhuma mudança para acumular. Se o resultado dependesse de quantas vezes a Consulta foi chamada, ela já teria efeito colateral e deixaria de ser uma Consulta.

### Design by Contract — item (a)

**Heurística:** Limite

**Afirmação:** Um método que não tem nenhuma verificação de validade no início do seu corpo (nenhum `if` de guarda) ainda possui uma pré-condição no sentido do Design by Contract — ela apenas é a condição trivial "verdadeiro para qualquer entrada e qualquer estado".

**Resposta:** Verdadeiro

**Justificativa:** No formalismo de Design by Contract, toda operação tem uma pré-condição, mesmo que implícita; a ausência de um `if` de guarda no código não significa "sem pré-condição", significa que a pré-condição escolhida pelo autor da classe é a mais permissiva possível (aceita qualquer chamada). Confundir "nenhuma verificação escrita" com "nenhum contrato de entrada" é um erro comum — o contrato sempre existe, só varia em quão restritivo ele é.

### Design by Contract — item (b)

**Heurística:** Contrafactual

**Afirmação:** Se uma pré-condição falha, a responsabilidade recai sobre quem escreveu a classe, não sobre o chamador.

**Resposta:** Falso

**Justificativa:** É a inversão exata da regra ensinada: pré-condições são barreiras de entrada — se falham, a culpa é de quem chamou o método fora de hora ou com dado inválido. Quem escreveu a classe só é responsável por garantir a pós-condição, uma vez que as pré-condições foram satisfeitas. Trocar as duas direções de responsabilidade é o erro conceitual central de Design by Contract: o contrato tem dois lados, e cada lado responde por uma metade dele.

### Design by Contract — item (c)

**Heurística:** Limite

**Afirmação:** Um método `processarSaque(double valor)` que não contém nenhuma instrução `assert` no seu corpo não está sujeito a nenhuma pós-condição, dentro da disciplina de Design by Contract.

**Resposta:** Falso

**Justificativa:** A pós-condição é a promessa de design de que, satisfeitas as pré-condições, o método deixa o objeto num estado onde as invariantes seguem válidas; essa promessa existe independentemente de o código conter um `assert` explícito ou não. O `assert` do exemplo da aula é só uma ferramenta de verificação/documentação em tempo de execução — removê-lo não remove a obrigação de a lógica do método efetivamente preservar a invariante, só remove a checagem automática que denunciaria a falha.

### Design by Contract — item (d)

**Heurística:** Limite

**Afirmação:** Num método `transferir(ContaBancaria destino, double valor)` que debita da própria conta e credita na conta `destino`, se ele não verifica que `destino` é diferente de `this`, e um chamador passa a própria conta como destino (`contaA.transferir(contaA, 100)`), quebrando a invariante de saldo, a culpa é do autor do método `transferir`, não de quem o chamou.

**Resposta:** Verdadeiro

**Justificativa:** Pela disciplina de Design by Contract, toda restrição necessária para a pós-condição se sustentar precisa estar coberta por uma pré-condição explícita e checada; `destino != this` é exatamente esse tipo de restrição implícita que o método deveria ter validado (Fail-Fast) e não validou. Como o método não declarou nem checou essa pré-condição, o chamador não tinha como saber que aquela chamada era ilegal — a responsabilidade recai sobre quem escreveu `transferir`, por deixar uma lacuna no contrato.

### Fail-Fast e Exceções Padrão — item (a)

**Heurística:** Transferência

**Afirmação:** Diferente de um código de erro `-1` em C, uma exceção checked em Java (como `IOException`, que exige `throws` na assinatura do método) não pode ser silenciosamente ignorada pelo chamador, porque o compilador obriga o tratamento do erro.

**Resposta:** Falso

**Justificativa:** O compilador só obriga o chamador a escrever uma cláusula `catch` (ou repassar com `throws`) sintaticamente; nada impede um `catch (IOException e) {}` vazio, que descarta o erro exatamente como o `if (resultado == -1)` que ninguém verificou em C. "Ser forçado a escrever `catch`" não é o mesmo que "ser forçado a tratar o erro de verdade" — o silêncio ainda é possível, só fica um pouco mais visível no código-fonte.

### Fail-Fast e Exceções Padrão — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** `IllegalArgumentException` deve ser usada quando o objeto está no estado errado para a operação.

**Resposta:** Falso

**Justificativa:** É a troca clássica das duas exceções: `IllegalArgumentException` é sobre a *carga* (um argumento que não faz sentido no domínio, independentemente do estado do objeto); `IllegalStateException` é sobre o *momento* (o dado está correto, mas o objeto não está no estado certo para aceitar essa operação agora). A afirmação usa o jargão certo, mas atribui cada exceção à situação da outra — o tipo de erro que soa plausível para quem decorou os nomes sem entender a distinção carga vs. momento.

### Fail-Fast e Exceções Padrão — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** Se um método recebe, ao mesmo tempo, um argumento inválido (ex.: quantidade negativa) e é chamado num objeto que também está no estado errado para a operação (ex.: um carrinho já finalizado), a linguagem Java exige que a checagem de estado (`IllegalStateException`) seja sempre feita antes da checagem do argumento (`IllegalArgumentException`).

**Resposta:** Falso

**Justificativa:** Java não impõe nenhuma ordem entre as duas checagens; qual verificação vem primeiro no corpo do método é uma decisão de design de quem escreve a classe (geralmente documentada no Javadoc), não uma regra da linguagem ou da JVM. Nada impede o autor de checar o argumento antes do estado, ou vice-versa — o importante é que ambas sejam feitas antes de qualquer mutação (Fail-Fast), não a ordem relativa entre elas.

### Fail-Fast e Exceções Padrão — item (d)

**Heurística:** Limite

**Afirmação:** Chamar `Objects.requireNonNull(cliente, "...")` na última linha do corpo de um método, depois de todas as outras mutações de estado já terem sido executadas, cumpre igualmente bem o espírito do Fail-Fast, desde que a exceção ainda seja lançada antes do método retornar o controle ao chamador.

**Resposta:** Falso

**Justificativa:** O espírito do Fail-Fast é interromper o fluxo *antes* de qualquer mutação de estado acontecer, não simplesmente "antes do método retornar". Se as mutações já foram executadas quando o `requireNonNull` finalmente dispara no final do método, o objeto pode ter ficado num estado parcialmente alterado e inconsistente até esse ponto — a exceção eventualmente é lançada, mas tarde demais para evitar o dano; a checagem precisa vir antes de qualquer `this.campo = ...`, não só antes do `return`.

### Identidade Física vs. Lógica — item (a)

**Heurística:** Transferência

**Afirmação:** Para dois objetos `Integer` criados por autoboxing com o mesmo valor pequeno (`Integer a = 100; Integer b = 100;`), o operador `==` se comporta exatamente como no exemplo de `Produto` com `new` — sempre resulta em `false`, porque cada variável aponta para um objeto `Integer` diferente na Heap.

**Resposta:** Falso

**Justificativa:** Diferente de `new Produto(...)`, que sempre aloca uma instância nova, o autoboxing de valores inteiros pequenos (entre -128 e 127) reaproveita instâncias de um cache interno (`Integer.valueOf`); `a` e `b` acabam apontando para o mesmo objeto `Integer` cacheado, então `a == b` resulta em `true` — não porque `==` tenha deixado de comparar referências, mas porque, nesse caso específico, as duas referências realmente coincidem. É um contraexemplo clássico de como a suposição "cada variável tem seu próprio objeto" pode falhar silenciosamente.

### Identidade Física vs. Lógica — item (b)

**Heurística:** Transferência

**Afirmação:** Ao contrário de comparar duas instâncias de `Produto`, comparar dois valores do tipo `enum Estado` (como no exemplo `Pedido` do início da aula) com `==` — por exemplo, `this.status == Estado.PAGO` — é seguro e dá o mesmo resultado que usar `.equals()`, porque a JVM garante que cada constante do enum existe como uma única instância na Heap.

**Resposta:** Verdadeiro

**Justificativa:** Diferente de uma classe comum, onde cada `new` cria uma instância física distinta (por isso `==` costuma ser perigoso), as constantes de um `enum` são inicializadas pela JVM uma única vez cada, como singletons; toda referência a `Estado.PAGO` no programa aponta para o mesmo objeto na Heap. Por isso, `==` entre valores de enum é seguro e é, aliás, a forma idiomática recomendada em Java — aqui identidade física e identidade lógica coincidem sempre, ao contrário do `Produto` do exemplo do SKU.

### Identidade Física vs. Lógica — item (c)

**Heurística:** Contrafactual

**Afirmação:** Se um programador sobrescrever `equals()` de `Produto` para sempre devolver `true`, independentemente do objeto comparado, mas não sobrescrever `hashCode()` (mantendo o padrão herdado de `Object`, baseado no endereço), um `HashSet<Produto>` vai tratar dois `Produto` diferentes, adicionados nele, como duplicados.

**Resposta:** Falso

**Justificativa:** Um `HashSet` primeiro usa `hashCode()` para decidir em qual "balde" (bucket) colocar/procurar o objeto, e só chama `equals()` para comparar objetos que já caíram no mesmo balde. Como `hashCode()` continua sendo o padrão de `Object` (baseado no endereço físico), dois `Produto` diferentes praticamente certamente caem em buckets diferentes, e `equals()` (que sempre devolveria `true`) nunca chega a ser chamado para compará-los entre si — o `HashSet` os trata como distintos mesmo assim. É o contrato quebrado na direção oposta à usual: `equals()` diz que são iguais, mas `hashCode()` não colabora, e o resultado prático é que o `Set` "não percebe" a igualdade.

### Identidade Física vs. Lógica — item (d)

**Heurística:** Transferência

**Afirmação:** Um `TreeSet<Produto>` configurado com um `Comparator` que ordena por SKU sofre exatamente do mesmo problema de aceitar "duplicatas" de negócio que um `HashSet<Produto>` sem `equals()`/`hashCode()` sobrescritos, pois ambas as coleções dependem exclusivamente de `equals()` para decidir se dois elementos são o mesmo.

**Resposta:** Falso

**Justificativa:** Diferente de `HashSet`, que depende do par `equals()`/`hashCode()`, um `TreeSet` decide duplicidade usando exclusivamente o `Comparator` (ou `Comparable`) fornecido: dois elementos são considerados "iguais" para fins do conjunto quando `compare(a, b) == 0`, mesmo que `equals()` nunca tenha sido sobrescrito. Um `Comparator` por SKU já rejeitaria corretamente um segundo `Produto` com o mesmo SKU, sem que a classe precisasse tocar em `equals()`/`hashCode()` — uma via alternativa de resolver o mesmo problema de identidade lógica.

### O Contrato equals()/hashCode() — item (a)

**Heurística:** Contrafactual

**Afirmação:** Pelo mesmo contrato de `equals()`/`hashCode()`, se dois objetos `Produto` têm o mesmo `hashCode()`, então `equals()` entre eles deve obrigatoriamente devolver `true`.

**Resposta:** Falso

**Justificativa:** O contrato só garante a implicação numa direção: `equals()` verdadeiro implica `hashCode()` igual. A volta não vale: dois objetos podem ter o mesmo `hashCode()` (uma colisão de hash, esperada e permitida) sem serem `equals()` — é exatamente por isso que um `HashMap`/`HashSet`, depois de encontrar o balde certo pelo hash, ainda precisa chamar `equals()` para confirmar se os objetos são de fato o mesmo, em vez de confiar só na coincidência do hash.

### O Contrato equals()/hashCode() — item (b)

**Heurística:** Contrafactual

**Afirmação:** O `hashCode()` pode usar atributos completamente diferentes dos usados pelo `equals()`, sem risco.

**Resposta:** Falso

**Justificativa:** É a inversão direta da regra do contrato ("o hash deve olhar apenas para os campos do equals") e da analogia do armazém: se `equals()` compara o SKU mas `hashCode()` usa outro campo (a cor da embalagem, por exemplo), dois objetos considerados iguais por `equals()` podem cair em corredores/baldes diferentes — o sistema procura no corredor errado e afirma, silenciosamente, que o item não existe. Usar campos diferentes nos dois métodos quebra a consistência exigida pelo contrato e não é uma escolha "sem risco".

### O Contrato equals()/hashCode() — item (c)

**Heurística:** Limite

**Afirmação:** Se um `Produto` com `equals()`/`hashCode()` mal implementados for usado apenas como VALOR (não como chave) dentro de um `HashMap<Integer, Produto>`, o mesmo risco de "desaparecimento silencioso" descrito na aula para chaves se aplica igualmente a ele.

**Resposta:** Falso

**Justificativa:** O `HashMap` só consulta `hashCode()`/`equals()` do objeto usado como *chave*, para decidir em qual balde procurar e confirmar a identidade durante a busca; o *valor* é apenas armazenado e devolvido junto da chave correspondente, sem que seu próprio `equals()`/`hashCode()` participe da mecânica de localização. Um `Produto` com esses métodos mal implementados, usado como valor, continua sendo recuperado corretamente pela chave `Integer` — o problema do "corredor errado" só existe quando o objeto com o contrato quebrado é a própria chave da busca.

### O Contrato equals()/hashCode() — item (d)

**Heurística:** Transferência

**Afirmação:** IDEs modernas geram os dois métodos juntos justamente para preservar essa coerência.

**Resposta:** Verdadeiro

**Justificativa:** IDEs como IntelliJ IDEA e Eclipse oferecem geração automática de `equals()`/`hashCode()` a partir dos mesmos campos escolhidos pelo programador, precisamente para evitar o erro de escrever um sem o outro (ou de escrevê-los usando conjuntos de campos diferentes). Essa é uma aplicação prática, fora do escopo direto da aula, da mesma lição da analogia do armazém: os dois métodos formam um contrato indissociável, e ferramentas de desenvolvimento institucionalizaram essa disciplina para reduzir o erro humano.
