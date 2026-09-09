# Gabarito — Aula 11

Gabarito consolidado: justificativa analítica de cada item de V/F dos
exercícios finais (`index.qmd`) e a solução discutida de cada pausa
ativa da aula. Nunca publicado no site (prefixo `_`).

## Pausas Ativas

### Pausa 1 — O Vocabulário dos Padrões e as Três Famílias

**Pergunta motivadora:** Se um colega descrever uma solução como "uma
classe que traduz chamadas de uma biblioteca externa incompatível para
o formato que meu sistema espera", a que família de padrões essa
solução pertence — e por que classificá-la pela família certa importa
mais do que decorar o nome "Adapter"?

**Discussão:** A solução descrita — harmonizar duas interfaces
incompatíveis sem alterar o comportamento interno de nenhuma delas —
tem como foco a **topologia** da comunicação entre as partes, não a
distribuição de obrigações no tempo (isso seria Comportamental) nem a
gênese de objetos (isso seria Criação). É exatamente a definição de
família Estrutural. Saber a família antes do nome importa porque o
propósito arquitetural é o que orienta a decisão de projeto: um
engenheiro que reconhece "isto é um problema de topologia entre duas
interfaces" já sabe que a solução vai envolver compor objetos numa
nova fronteira comum, mesmo antes de lembrar que esse padrão específico
se chama Adapter. O nome vem depois, como atalho de comunicação — mas
o raciocínio estrutural que leva até ele é o que realmente importa.

**V/F resolvido:**
- ✔ Uma solução cujo objetivo é permitir que duas interfaces incompatíveis conversem entre si, sem alterar o comportamento interno de nenhuma das duas, se classifica na família Estrutural, não na Comportamental.
- ✗ Se um engenheiro aplicar rigorosamente a estrutura de classes de um Padrão de Projeto sobre um sistema que ainda usa variáveis globais e funções soltas (sem nenhum encapsulamento), o padrão resolverá o problema de coesão do sistema da mesma forma que resolveria num sistema já orientado a objetos.
- ✗ Uma biblioteca como o Spring, que instancia os objetos da aplicação e invoca os métodos do desenvolvedor em momentos que ela mesma decide, exemplifica a mesma relação de controle de fluxo que um Padrão de Projeto estabelece com o código do desenvolvedor.
- ✔ Dois padrões pertencentes a famílias diferentes (por exemplo, um Estrutural e um Comportamental) podem, ainda assim, ser aplicados na mesma classe simultaneamente, resolvendo problemas arquiteturais distintos e não conflitantes.

---

### Pausa 2 — Entidade vs. Value Object

**Pergunta motivadora:** Se um sistema de biblioteca representasse cada
exemplar físico de um livro como um Value Object (sem ID, igualdade por
atributo), o que quebraria no momento em que dois exemplares idênticos
do mesmo título precisassem ser rastreados separadamente (um
emprestado, outro na prateleira)?

**Discussão:** O rastreio individual quebraria porque um Value Object
é, por definição, indistinguível de outro com o mesmo conteúdo —
`equals()` compara valores, não identidade. Dois exemplares físicos com
título, autor e edição idênticos produziriam VOs "iguais" mesmo sendo
objetos físicos diferentes no mundo real, um emprestado e outro na
prateleira. A pergunta de negócio aqui — "este exemplar específico está
disponível?" — exige uma identidade persistente que sobrevive a
qualquer mudança de estado (por exemplo, de "disponível" para
"emprestado"), o que é exatamente a definição de Entidade. A correção
é modelar cada exemplar físico como uma Entidade com um identificador
próprio (um número de patrimônio, por exemplo), reservando o Value
Object para os metadados do título (nome, autor, ISBN) que de fato são
compartilhados por todos os exemplares daquela edição.

**V/F resolvido:**
- ✔ Se dois exemplares físicos de um mesmo título tiverem exatamente os mesmos atributos de valor (título, autor, edição), modelá-los como Value Objects tornaria `equals()` incapaz de distinguir qual exemplar específico está emprestado e qual está na prateleira.
- ✔ Um `Dinheiro` de R$ 50 criado numa parte do sistema é sempre `equals()` a outro `Dinheiro` de R$ 50 criado em outra parte completamente diferente do sistema, mesmo sem nenhuma relação de criação entre os dois.
- ✗ Se a classe `Aluno` permitisse alterar o valor do campo `ra` através de um método público após a construção, isso não comprometeria a modelagem de `Aluno` como Entidade, desde que `curso` continuasse mutável.
- ✔ Um sistema de reservas de assento de cinema que precisa saber se o assento B12 da sessão das 20h (especificamente aquele, não outro assento idêntico em atributos) já foi reservado se beneficia de modelar o assento como Entidade, não como Value Object.

---

### Pausa 3 — Factory Method e Acoplamento Direto

**Pergunta motivadora:** Se um novo requisito pedir notificação por
WhatsApp, por que a resposta correta nunca deveria envolver abrir e
editar os 50 pontos do sistema que hoje disparam
`NotificacaoPedidoFactory.criar(...)`?

**Discussão:** Porque nenhum desses 50 pontos conhece uma classe
concreta de notificação — todos conversam apenas com a abstração
`NotificacaoPedido`, obtida através da fábrica. Toda a decisão de "qual
classe instanciar" está confinada a um único lugar:
`NotificacaoPedidoFactory`. Para acomodar o WhatsApp, basta escrever
uma nova classe `NotificacaoPedidoWhatsApp` implementando
`NotificacaoPedido` e adicionar um novo caso no `switch` da fábrica —
nenhum dos 50 pontos de disparo muda uma linha, porque nenhum deles
jamais dependeu da classe concreta. Se a arquitetura fosse a oposta —
cada ponto de disparo decidindo por si mesmo qual classe instanciar —,
o mesmo requisito exigiria caçar e editar os 50 lugares, cada edição
sendo uma nova chance de esquecer um deles ou introduzir uma
inconsistência.

**V/F resolvido:**
- ✗ Se `ServicoDePedidos` chamasse diretamente `new NotificacaoPedidoEmail()` em vez de pedir a `NotificacaoPedidoFactory`, adicionar um novo meio de notificação ainda seria possível sem alterar nenhum código que já dispara notificações.
- ✔ Um sistema de geração de relatórios que decide, em tempo de execução, se deve instanciar `RelatorioPDF` ou `RelatorioExcel` a partir de uma preferência do usuário, centralizando essa decisão numa única classe fábrica, aplica a mesma lógica estrutural do Factory Method visto em aula.
- ✗ Se `RepositorioPedidosFactory` sempre devolvesse a mesma implementação concreta (`RepositorioPedidosMySQL`), injetar essa fábrica em vez de instanciar diretamente `RepositorioPedidosMySQL` não traria nenhum benefício arquitetural, mesmo pensando em testes automatizados futuros.
- ✗ Um `ServicoDePedidos` que recebe uma `RepositorioPedidosFactory` no construtor, mas depois usa `instanceof RepositorioPedidosMySQL` para decidir se aplica uma otimização específica daquele banco, preserva integralmente a Inversão de Dependência que a injeção da fábrica pretendia estabelecer.

---

## Exercícios de V/F

### O Vocabulário e a Natureza dos Padrões de Projeto — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Uma equipe que copia o código-fonte de um projeto anterior para reaproveitar uma solução de design, sem adaptar as classes ao novo domínio, está aplicando corretamente um Padrão de Projeto no sentido em que o GoF definiu o termo.

**Resposta:** Falso

**Justificativa:** Um Padrão de Projeto é um gabarito conceitual — a topologia de classes, responsabilidades e mensagens —, não um trecho de código para copiar e colar. Reaproveitar código-fonte literal de outro projeto, sem adaptar as classes ao novo domínio, é exatamente o antipadrão que o `CLAUDE.md` da definição do GoF alerta contra: confundir "padrão" com "biblioteca pronta".

### O Vocabulário e a Natureza dos Padrões de Projeto — item (b)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Se um engenheiro descrever uma solução dizendo apenas "implemente um Observer aqui" para um colega que também domina o vocabulário GoF, essa frase provavelmente transmite mais informação estrutural precisa do que uma explicação equivalente sem o nome do padrão.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente o argumento da "linguagem ubíqua": entre dois engenheiros que compartilham o vocabulário, uma única palavra ("Observer", "Strategy") condensa toda uma topologia de classes, responsabilidades e protocolo de comunicação que, sem o nome, exigiria um parágrafo inteiro de explicação — e ainda assim correria risco de ambiguidade.

### O Vocabulário e a Natureza dos Padrões de Projeto — item (c)

**Heurística:** Caso limite/extremo

**Afirmação:** ✗ Um sistema construído inteiramente com funções globais e variáveis compartilhadas, sem nenhuma classe ou encapsulamento, se beneficiaria da mesma forma ao aplicar a estrutura de um padrão GoF que um sistema já orientado a objetos se beneficiaria.

**Resposta:** Falso

**Justificativa:** Padrões de Projeto pressupõem que encapsulamento e troca de mensagens já estejam estabelecidos — eles não curam código procedural. Aplicar a estrutura de classes de um padrão sobre um sistema de variáveis globais e funções soltas apenas mascara o problema de fundo (a ausência de encapsulamento), sem resolvê-lo, ao contrário do que aconteceria num sistema já orientado a objetos.

### O Vocabulário e a Natureza dos Padrões de Projeto — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Um algoritmo de ordenação otimizado para grandes volumes de dados, por mais sofisticado e reutilizável que seja, não se qualifica como um Padrão de Projeto no sentido do catálogo GoF, ainda que resolva um problema recorrente.

**Resposta:** Verdadeiro

**Justificativa:** Padrões de Projeto resolvem problemas de acoplamento e coesão entre classes/objetos, não problemas algorítmicos de ordenação, criptografia ou busca — mesmo que ambos sejam soluções recorrentes e reutilizáveis, a natureza do problema resolvido é categoricamente diferente, e o `.tex` de origem faz essa distinção explicitamente.

---

### As Três Famílias de Padrões — item (a)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um padrão cujo objetivo é permitir que um objeto adicione responsabilidades novas dinamicamente, sem alterar sua classe original nem depender de herança estática, se encaixa melhor na família Estrutural do que na família de Criação.

**Resposta:** Verdadeiro

**Justificativa:** O padrão descrito (Decorator, citado em aula como exemplo de Estrutural) tem como foco a topologia — como compor objetos para formar uma estrutura maior e flexível —, não a gênese do objeto (Criação, que trata de como ele nasce) nem a comunicação no tempo (Comportamento).

### As Três Famílias de Padrões — item (b)

**Heurística:** Contrafactual

**Afirmação:** ✗ Um sistema de checkout que usa duas soluções ao mesmo tempo — uma para decidir qual meio de pagamento processar (Strategy) e outra para decidir qual classe concreta de repositório instanciar (Factory Method) — está misturando indevidamente duas famílias de padrões incompatíveis entre si.

**Resposta:** Falso

**Justificativa:** As três famílias descrevem o propósito arquitetural predominante de cada padrão isolado, não uma exclusividade mútua entre padrões de famílias diferentes num mesmo sistema. Strategy (Comportamental) e Factory Method (Criação) resolvem problemas ortogonais — um trata de comportamento intercambiável, o outro de gênese segura — e sua combinação no mesmo sistema é comum e desejável, não uma mistura indevida.

### As Três Famílias de Padrões — item (c)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Um padrão cujo foco declarado é "isolar a complexidade do operador `new` e gerenciar o ciclo de vida na Heap" pertence, por definição, à família de Criação, independentemente de também usar composição internamente.

**Resposta:** Verdadeiro

**Justificativa:** A definição de família de Criação é exatamente essa — isolar a gênese e o ciclo de vida do `new`. O fato de quase todos os 23 padrões GoF (de qualquer família) se apoiarem em composição e polimorfismo como mecânica interna não muda a classificação por propósito: o critério de família é "para que serve", não "com que mecanismo é construído".

### As Três Famílias de Padrões — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Classificar o Strategy como um padrão Comportamental (e não Estrutural) depende do fato de ele envolver uma interface implementada por múltiplas classes, e não do fato de seu propósito ser distribuir a decisão de "como fazer" no tempo de execução.

**Resposta:** Falso

**Justificativa:** É o oposto: a classificação por família depende do **propósito** (comunicação e distribuição de obrigações no tempo, no caso do Strategy), não do mecanismo estrutural usado (uma interface com múltiplas implementações). Esse mesmo mecanismo — interface com várias implementações — também aparece em padrões Estruturais e de Criação; o que decide a família é para que a variação existe, não como ela é implementada em Java.

---

### Aliasing e a Fragilidade do Estado Mutável — item (a)

**Heurística:** Caso limite/extremo

**Afirmação:** ✗ Em `Retangulo r2 = r1;`, se `Retangulo` for uma classe (não um primitivo), a variável `r2` recebe uma cópia independente dos valores de `largura` e `altura` de `r1` no momento da atribuição.

**Resposta:** Falso

**Justificativa:** Em Java, atribuir uma variável de tipo referência a outra copia o **endereço** de memória, nunca os dados. `r2` passa a apontar para o mesmo objeto `Retangulo` na Heap que `r1` já apontava — não existe uma segunda cópia independente de `largura`/`altura`.

### Aliasing e a Fragilidade do Estado Mutável — item (b)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um sistema que compartilha uma mesma instância de uma classe `Configuracao` mutável entre dois módulos independentes está estruturalmente exposto ao mesmo padrão de bug de *aliasing* descrito para o `Retangulo`, mesmo que o domínio seja diferente.

**Resposta:** Verdadeiro

**Justificativa:** O mecanismo do *aliasing* não depende do domínio (retângulos, configurações, ou qualquer outra classe) — depende apenas de duas condições: mutabilidade e uma referência compartilhada. Qualquer classe mutável compartilhada entre módulos está exposta ao mesmo risco estrutural.

### Aliasing e a Fragilidade do Estado Mutável — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Aplicar uma "Cópia Defensiva" antes de cada compartilhamento de uma referência mutável elimina o risco de *aliasing* sem nenhum custo adicional de memória ou processamento sobre o sistema.

**Resposta:** Falso

**Justificativa:** A Cópia Defensiva elimina o risco de *aliasing* naquele ponto específico, mas tem custo real e mencionado explicitamente em aula: sobrecarrega o *Garbage Collector* com objetos descartáveis extras e polui o código com lógica de clonagem repetida em cada fronteira de compartilhamento — não é uma solução "de graça".

### Aliasing e a Fragilidade do Estado Mutável — item (d)

**Heurística:** Caso limite/extremo

**Afirmação:** ✗ Se um método de uma classe imutável precisasse, para calcular seu retorno, ler o estado de outro objeto imutável passado como parâmetro, o risco de *aliasing bug* sobre esse parâmetro seria estruturalmente idêntico ao risco existente ao ler um parâmetro mutável.

**Resposta:** Falso

**Justificativa:** O risco de *aliasing bug* nasce especificamente da possibilidade de **mutação** por uma referência compartilhada. Se o objeto lido é imutável, nenhuma leitura pode alterá-lo "pelas costas" de quem mais o referencia — o cenário de corrupção silenciosa simplesmente não existe para um parâmetro imutável, ao contrário de um mutável.

---

### Entidade vs. Value Object — item (a)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um sistema bancário que precisa diferenciar duas contas correntes com saldo, titular e agência idênticos (por serem contas efetivamente distintas, uma de cada cliente) exige que `ContaCorrente` seja modelada como Entidade, não como Value Object.

**Resposta:** Verdadeiro

**Justificativa:** A necessidade de distinguir dois objetos com atributos de valor idênticos é exatamente o critério que exige identidade persistente (um número de conta, por exemplo) — a marca registrada de uma Entidade. Um Value Object, cuja igualdade é por conteúdo, tornaria as duas contas indistinguíveis.

### Entidade vs. Value Object — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Se dois objetos `Dinheiro` representarem quantias e moedas idênticas, mas tiverem sido instanciados em pontos completamente diferentes do código, `equals()` entre eles deve retornar `false`, pois cada instância ocupa um endereço de memória próprio na Heap.

**Resposta:** Falso

**Justificativa:** É exatamente o oposto do que define um Value Object: `equals()` compara **valores** (quantia e moeda), não endereços de memória. Dois `Dinheiro` com o mesmo conteúdo devem ser `equals()` independentemente de onde ou quando foram instanciados — essa é a substituibilidade que motiva o padrão.

### Entidade vs. Value Object — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Uma classe `Endereco` (rua, número, cidade, CEP) usada apenas para exibir a localização de entrega de um `Pedido`, sem que o sistema precise rastrear "este endereço específico" ao longo do tempo, é uma candidata natural a Value Object.

**Resposta:** Verdadeiro

**Justificativa:** Não há necessidade de identidade persistente aqui — o que importa é o conteúdo do endereço (rua, número, cidade, CEP), não "qual instância específica" foi usada. Dois `Endereco`s com os mesmos dados são intercambiáveis para todos os efeitos práticos, exatamente o critério de um Value Object.

### Entidade vs. Value Object — item (d)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Modelar `Aluno` como Entidade (identidade por RA) não impede que um dos seus atributos, como `Endereco`, seja internamente representado por um Value Object imutável.

**Resposta:** Verdadeiro

**Justificativa:** Entidade e Value Object não são mutuamente exclusivos dentro do mesmo grafo de objetos — uma Entidade tipicamente *contém* Value Objects como parte do seu estado mutável (o RA de `Aluno` continua sendo a identidade persistente, mas o valor do campo `endereco` pode ser trocado por uma nova instância imutável de `Endereco` sem que isso mude a identidade do `Aluno`).

---

### Obsessão por Primitivos e Anemia Semântica — item (a)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Representar uma idade humana como um `int` sem nenhuma validação adicional permite, do ponto de vista do compilador Java, que o valor `-500` seja atribuído sem qualquer erro de compilação.

**Resposta:** Verdadeiro

**Justificativa:** O tipo `int` em Java aceita qualquer valor dentro do seu intervalo numérico, sem nenhuma noção de domínio de negócio — o compilador não tem como saber que uma idade nunca deveria ser negativa. É exatamente o risco descrito em aula: erros que deveriam ser de compilação (ou ao menos de construção Fail-Fast) tornam-se, na prática, erros de runtime ou nem são detectados.

### Obsessão por Primitivos e Anemia Semântica — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Se duas partes distintas do sistema validarem o formato de um CPF de forma ligeiramente diferente (uma aceitando pontuação, outra não), isso é uma consequência esperada e inofensiva de representar CPF como `String` em vez de como um Value Object dedicado.

**Resposta:** Falso

**Justificativa:** Essa divergência de validação é exatamente o sintoma da "lógica dispersa" que a Obsessão por Primitivos causa — longe de inofensiva, ela gera inconsistência real: um CPF aceito por uma parte do sistema pode ser rejeitado por outra, produzindo comportamento imprevisível. Um Value Object `CPF` centralizaria essa validação num único lugar (o construtor), eliminando a divergência por definição.

### Obsessão por Primitivos e Anemia Semântica — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Substituir um parâmetro `double taxaDeJuros` por um Value Object `TaxaDeJuros` que valida, no construtor, que o valor está entre 0 e 1, move um erro de negócio que antes só apareceria em produção para o momento da criação do objeto.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente o mecanismo Fail-Fast do Value Object aplicado a um domínio diferente do `Email`/`Dinheiro` vistos em aula: a validação migra do ponto de uso (potencialmente distante, potencialmente em produção) para o momento da construção — se o objeto `TaxaDeJuros` existe, ele já é garantidamente válido em qualquer lugar do sistema.

### Obsessão por Primitivos e Anemia Semântica — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ A "Anemia Semântica" ocorre quando o tipo de um dado (ex.: `String`) descreve completamente o que esse dado representa para o negócio, sem nenhuma perda de informação em relação a um tipo de domínio dedicado.

**Resposta:** Falso

**Justificativa:** É a definição invertida: a Anemia Semântica ocorre exatamente quando o tipo primitivo **não** descreve o que o dado significa para o negócio — `String` diz "isto é uma sequência de caracteres", nunca "isto é um e-mail válido" ou "isto é um CPF". A perda de informação semântica é o próprio problema, não sua ausência.

---

### O Padrão Builder e a Interface Fluente — item (a)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ No `PedidoBuilder`, o fato de cada método de configuração retornar `this` é o que torna sintaticamente possível encadear `.paraCliente(...).comItem(...).comDesconto(...)` numa única expressão.

**Resposta:** Verdadeiro

**Justificativa:** Encadear chamadas de método em Java (`objeto.metodo1().metodo2()`) só é possível porque cada chamada intermediária devolve uma referência sobre a qual o próximo método pode ser invocado — no Builder, essa referência é a própria instância do Builder (`return this`), o que faz do encadeamento fluente possível.

### O Padrão Builder e a Interface Fluente — item (b)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se a validação "desconto não pode ser maior que o total" fosse movida do método `build()` para dentro de `comDesconto()`, ela continuaria funcionando corretamente mesmo que `comItem()` fosse chamado depois de `comDesconto()` na cadeia de chamadas.

**Resposta:** Falso

**Justificativa:** Se a validação estivesse dentro de `comDesconto()`, ela só teria acesso ao valor de `total` acumulado **até aquele ponto** da cadeia — se `comItem()` (que incrementa `total`) for chamado depois, a validação já executada em `comDesconto()` estaria comparando o desconto contra um total ainda incompleto. É exatamente por isso que `build()`, executado só ao final, é o único lugar correto para validações *cross-field* que dependem do estado final e completo do objeto.

### O Padrão Builder e a Interface Fluente — item (c)

**Heurística:** Contrafactual

**Afirmação:** ✗ Um `PedidoBuilder` cujo construtor da classe `Pedido` alvo fosse `public` (em vez de `private`) ainda impediria, com a mesma eficácia, que código externo criasse um `Pedido` sem passar pelas validações do `build()`.

**Resposta:** Falso

**Justificativa:** Se o construtor de `Pedido` fosse público, qualquer código externo poderia chamar `new Pedido(...)` diretamente, contornando inteiramente o `PedidoBuilder` e suas validações *cross-field*. A blindagem depende especificamente do construtor ser `private`, forçando toda instanciação a passar pelo portão único do `build()`.

### O Padrão Builder e a Interface Fluente — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ A imutabilidade do objeto `Pedido` produzido no final não exige que o próprio `PedidoBuilder`, enquanto acumula dados, também seja imutável — os dois objetos podem ter regras de mutabilidade diferentes por servirem a propósitos diferentes.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente o design discutido em aula: o `PedidoBuilder` é deliberadamente mutável (seus campos são reatribuídos a cada método de configuração) porque sua função é acumular estado temporário; o `Pedido` final é imutável porque sua função é representar um estado de negócio estável e protegido. As duas classes têm papéis diferentes e, por isso, regras de mutabilidade diferentes.

---

### Factory Method e Desacoplamento — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se `NotificacaoPedidoFactory.criar(String meio)` retornasse o tipo concreto `NotificacaoPedidoEmail` em vez da interface `NotificacaoPedido` quando o meio fosse "EMAIL", o código cliente que só espera a interface ainda compilaria sem nenhuma alteração.

**Resposta:** Falso

**Justificativa:** Embora `NotificacaoPedidoEmail` seja um subtipo de `NotificacaoPedido` (então a atribuição a uma variável do tipo interface ainda compilaria por polimorfismo), o problema real é de assinatura declarada: se o método `criar` declarasse formalmente o retorno como `NotificacaoPedidoEmail`, o `case "SMS"` do mesmo método (que devolve `NotificacaoPedidoSMS`) deixaria de compilar, pois `NotificacaoPedidoSMS` não é um `NotificacaoPedidoEmail`. Só declarar o retorno como a interface comum permite que a fábrica devolva qualquer uma das implementações.

### Factory Method e Desacoplamento — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Adicionar uma nova implementação `NotificacaoPedidoWhatsApp` exige, necessariamente, alterar tanto a fábrica quanto todos os pontos do sistema que hoje chamam `NotificacaoPedidoFactory.criar(...)`.

**Resposta:** Falso

**Justificativa:** É exatamente o benefício central do Factory Method: a nova classe mais um novo caso no `switch`/`if` da fábrica bastam. Nenhum dos pontos de chamada precisa mudar, porque todos eles já dependem apenas da interface `NotificacaoPedido`, nunca de uma classe concreta específica.

### Factory Method e Desacoplamento — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um sistema de geração de convites de evento que decide, a partir de uma preferência do organizador, se instancia um `ConviteDigital` ou um `ConviteImpresso`, centralizando essa decisão numa única classe fábrica, replica a mesma lógica estrutural do Factory Method do e-commerce.

**Resposta:** Verdadeiro

**Justificativa:** Mesma topologia — uma fábrica decide, com base num critério de negócio, qual classe concreta instanciar, devolvendo sempre a abstração comum (`Convite`) — aplicada a um domínio diferente do e-commerce.

### Factory Method e Desacoplamento — item (d)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Se a fábrica de notificações precisar de credenciais de um gateway de SMS para construir `NotificacaoPedidoSMS`, essas credenciais podem ficar inteiramente confinadas à fábrica, sem que o código cliente que chama `criar(...)` precise conhecê-las.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente o benefício de "encapsulamento de parâmetros de infraestrutura" discutido em aula: a fábrica pode gerenciar dependências específicas de cada implementação concreta (credenciais de SMTP, chaves de API de gateway) sem que o cliente que apenas pede uma `NotificacaoPedido` precise conhecer nenhum desses detalhes.

---

### Inversão de Dependência na Criação — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Um `ServicoDePedidos` que instancia `new RepositorioPedidosMySQL()` diretamente dentro de seu próprio construtor pode ser substituído, em um teste automatizado, por uma versão que usa um repositório falso (*mock*) sem nenhuma alteração no código de `ServicoDePedidos`.

**Resposta:** Falso

**Justificativa:** É exatamente o problema do acoplamento rígido: se `ServicoDePedidos` instancia `RepositorioPedidosMySQL` diretamente, não existe nenhum ponto de substituição para um *mock* sem editar o próprio código-fonte de `ServicoDePedidos` — a dependência está fundida na implementação, não injetada de fora.

### Inversão de Dependência na Criação — item (b)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Injetar uma `RepositorioPedidosFactory` no construtor de `ServicoDePedidos`, em vez de instanciar diretamente uma classe concreta, empurra o conhecimento sobre "qual banco de dados usar" para a periferia do sistema, mantendo o núcleo de negócio isolado dessa decisão.

**Resposta:** Verdadeiro

**Justificativa:** É a definição de DIP aplicada à criação: o núcleo de negócio (`ServicoDePedidos`) passa a depender só do contrato `RepositorioPedidos`, e a decisão concreta ("qual banco", "qual fornecedor") é tomada no ponto de entrada da aplicação, que injeta a fábrica apropriada — exatamente o mesmo raciocínio de fronteira aplicado a `Pagavel` na Aula 10.

### Inversão de Dependência na Criação — item (c)

**Heurística:** Caso limite/extremo

**Afirmação:** ✗ Um `ServicoDePedidos` que depende apenas da interface `RepositorioPedidos` ainda estaria violando o Princípio de Inversão de Dependência se essa interface fosse implementada por uma única classe concreta em todo o sistema.

**Resposta:** Falso

**Justificativa:** O DIP é sobre a **direção da dependência** (módulos de alto nível dependendo de abstrações, não de implementações concretas), não sobre quantas implementações concretas existem no momento. Mesmo com uma única implementação hoje, `ServicoDePedidos` já está corretamente desacoplado — pronto para uma segunda implementação (ou um *mock* de teste) sem nenhuma mudança em sua própria lógica.

### Inversão de Dependência na Criação — item (d)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ A Inversão de Dependência na criação é estruturalmente análoga à injeção da interface `Pagavel` no `Pedido` feita na Aula 10 — em ambos os casos, um módulo de alto nível passa a depender de uma abstração em vez de uma implementação concreta.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente o paralelo traçado ao final do bloco: assim como `Pedido` conhece só `Pagavel` (nunca `Pix`/`Cartao`/`Boleto` diretamente) para o comportamento de pagamento, `ServicoDePedidos` conhece só `RepositorioPedidos` (nunca `RepositorioPedidosMySQL` diretamente) para a persistência — o mesmo princípio de fronteira, aplicado uma vez ao comportamento (Strategy) e outra vez à criação (Factory Method + DIP).
