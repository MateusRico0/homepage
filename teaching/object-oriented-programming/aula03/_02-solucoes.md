# Soluções — Questões de Verdadeiro/Falso (Aula 3)

> Arquivo de apoio, não publicado (prefixo `_`). Contém a resposta e a
> justificativa de cada item das 12 questões de V/F do `index.qmd`. O
> `index.qmd` publicado continua sem solução — este arquivo existe só
> para conferência do professor/monitor, seguindo a metodologia de
> criação de questões definida em `../../CLAUDE.md`.

### Do Fabricante ao Arquiteto — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se um projetista dedicasse todo o cuidado de design a otimizar cada classe isoladamente — sem nunca considerar como as mensagens fluem entre elas — o sistema resultante seria tão sustentável quanto um projetado com atenção à rede de colaboradores.

**Resposta:** Falso

**Justificativa:** A aula argumenta exatamente o contrário: peças perfeitas isoladamente (alta qualidade interna) que não se encaixam bem são "o caminho mais rápido para o fracasso". A sustentabilidade de um sistema depende de como os objetos colaboram (mensagens, contratos), não apenas da qualidade interna de cada classe tomada isoladamente.

### Do Fabricante ao Arquiteto — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Um sistema robusto pode ser visto como um amontoado de classes que expõem seus dados livremente.

**Resposta:** Falso

**Justificativa:** Expor dados livremente é o oposto do "arquiteto de sistemas" descrito na aula — é a intimidade técnica/acoplamento por "fofoca" que o design por contratos busca eliminar. Um sistema robusto é uma rede de colaboradores especializados que se comunicam por mensagens, não um amontoado de estruturas de dados abertas.

### Do Fabricante ao Arquiteto — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Projetar por "encaixes" (interfaces) permite ignorar o "como" interno de cada peça no rascunho do sistema.

**Resposta:** Verdadeiro

**Justificativa:** É o benefício direto da separação interface/implementação transferido para o processo de design: ao definir primeiro os encaixes (contratos) entre as peças, o arquiteto desenha a estrutura do sistema sem precisar fixar, naquele momento, os detalhes de implementação de cada classe — esses detalhes ficam encapsulados e podem ser definidos depois.

### Do Fabricante ao Arquiteto — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ A maturidade de design é atingida ao definir as mensagens entre objetos antes de escrever a lógica interna dos métodos.

**Resposta:** Verdadeiro

**Justificativa:** É a essência do salto de "fabricante de peças" para "arquiteto de sistemas": pensar primeiro em quem fala com quem e o que cada mensagem promete (o contrato) evita desenhar classes que sabem demais sobre os vizinhos; a lógica interna é um detalhe de implementação que pode evoluir livremente depois que o contrato está definido.

### Colaboração e Baixo Acoplamento — item (a)

**Heurística:** Transferência

**Afirmação:** ✔ Um objeto especialista deve, preferencialmente, não conhecer a existência de seu orquestrador.

**Resposta:** Verdadeiro

**Justificativa:** No exemplo `Produto`/`ItemCarrinho`/`Carrinho`, `Produto` é inteiramente autônomo e não conhece `Carrinho` nem nenhuma interface de usuário — essa é a definição de baixo acoplamento: o especialista deve servir a qualquer orquestrador (vitrine, estoque, relatório fiscal) sem sequer saber quem o está usando.

### Colaboração e Baixo Acoplamento — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ `ItemCarrinho.subtotal()` deve acessar diretamente o atributo `precoBase` de `Produto`.

**Resposta:** Falso

**Justificativa:** Isso violaria o encapsulamento estudado nas Aulas 1-2. No código da aula, `ItemCarrinho` "pergunta" ao produto via `getPreco()`, nunca acessa `precoBase` diretamente — perguntar via método é o que permite ao `Produto` mudar sua implementação interna sem quebrar `ItemCarrinho`.

### Colaboração e Baixo Acoplamento — item (c)

**Heurística:** Aplicação

**Afirmação:** ✔ `Carrinho.calcularTotal()` usa delegação, sem conhecer a lógica interna de `ItemCarrinho`.

**Resposta:** Verdadeiro

**Justificativa:** `calcularTotal()` apenas percorre a lista e chama `item.subtotal()` — ele orquestra, mas não sabe como o subtotal é calculado internamente; confia apenas no contrato de que existe um método `subtotal()`.

### Colaboração e Baixo Acoplamento — item (d)

**Heurística:** Transferência

**Afirmação:** ✔ Dividir responsabilidades entre especialistas evita a criação de "Objetos Deus".

**Resposta:** Verdadeiro

**Justificativa:** A aula argumenta que concentrar toda a inteligência numa única classe "gerente" é o erro do Modelo Anêmico em escala de sistema; dividir em `Produto`/`ItemCarrinho`/`Carrinho` especialistas é exatamente o que evita que uma única classe cresça sem limite (o Objeto Deus) e permite testar cada peça isoladamente.

### Interface como Contrato — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Se um método público de `ValidadorFinanceiro` passar a ter bugs ocasionais depois de uma refatoração puramente interna, isso já é evidência de que a separação entre interface e implementação falhou naquele ponto.

**Resposta:** Falso

**Justificativa:** Bugs na implementação são um problema de qualidade/correção do código interno, não uma quebra da fronteira interface/implementação. Essa fronteira "falha" quando o cliente precisa conhecer o "como" para usar ou contornar o problema — se `Compra` continua chamando só `isValido()` sem precisar saber da lógica interna, a fronteira permanece intacta mesmo havendo um bug a corrigir.

### Interface como Contrato — item (b)

**Heurística:** Aplicação

**Afirmação:** ✔ Alterar a implementação de um método, mantendo sua assinatura, não deveria exigir recompilar o cliente.

**Resposta:** Verdadeiro

**Justificativa:** É o argumento central do bloco: `Compra` é agnóstica quanto à complexidade de `isValido()`; trocar o algoritmo de validação por outro (ou o gateway por REST/gRPC) não exige que `Compra` seja recompilada, pois a assinatura pública permanece idêntica.

### Interface como Contrato — item (c)

**Heurística:** Aplicação

**Afirmação:** ✔ O acoplamento físico — conhecer as entranhas de outra classe — é uma das maiores causas de fragilidade.

**Resposta:** Verdadeiro

**Justificativa:** A aula identifica exatamente essa falha como a mais recorrente em sistemas complexos: quando a fronteira interface/implementação é rompida, uma mudança de baixo nível provoca falhas em cascata em módulos que não deveriam nem saber que a troca aconteceu.

### Interface como Contrato — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Uma interface bem desenhada deve expor o máximo possível da estrutura interna, para facilitar o reuso.

**Resposta:** Falso

**Justificativa:** É o oposto do que a aula defende — uma boa interface expõe o mínimo necessário (o "Quê"), escondendo a estrutura interna (o "Como"). Expor estrutura interna aumenta o acoplamento físico e a fragilidade; não é isso que viabiliza reuso seguro.

### Design de Caixa Preta — item (a)

**Heurística:** Aplicação

**Afirmação:** ✔ Atributos privados garantem que a interface pública seja a única via de interação com o objeto.

**Resposta:** Verdadeiro

**Justificativa:** É o mecanismo do encapsulamento (herdado das Aulas 1-2) aplicado aqui: com `precoCusto` privado, qualquer interação com `Produto` só pode passar pelos métodos públicos, como `calcularPrecoDeVenda()`.

### Design de Caixa Preta — item (b)

**Heurística:** Aplicação

**Afirmação:** ✔ Ocultar a implementação permite que regras de negócio voláteis mudem sem efeito cascata.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente a prova apresentada com `calcularPrecoDeVenda()`: a fórmula de margem mudou drasticamente da V1 para a V2 (incluindo um limiar de preço), mas como o contrato (assinatura) permaneceu o mesmo, o impacto no resto do sistema foi zero.

### Design de Caixa Preta — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Proteger o estado interno é dispensável se o programador garantir que ninguém chamará os métodos errado.

**Resposta:** Falso

**Justificativa:** Isso confia na disciplina do programador em vez de no compilador/design — exatamente o tipo de risco que o encapsulamento existe para eliminar estruturalmente. "Confiar que ninguém vai usar errado" não escala à medida que o sistema cresce e não é uma alternativa válida à proteção real do estado.

### Design de Caixa Preta — item (d)

**Heurística:** Aplicação

**Afirmação:** ✔ `calcularPrecoDeVenda()` pode mudar de fórmula internamente sem afetar quem já chama esse método.

**Resposta:** Verdadeiro

**Justificativa:** É a demonstração central do bloco — a V2 mudou a lógica (limiar de R\$ 1000, duas margens diferentes) mas manteve a mesma assinatura pública, então nenhum código cliente precisou mudar.

### A Lei de Demeter — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se `getCEPDeEntrega()` fosse reescrito para retornar o próprio objeto `Endereco` em vez do CEP já extraído, e o chamador então fizesse `pedido.getCEPDeEntrega().getCep()`, isso continuaria respeitando a Lei de Demeter tanto quanto a versão atual.

**Resposta:** Falso

**Justificativa:** O ganho de Demeter num método de delegação está em devolver o resultado já processado (um booleano, um CEP), não em ainda expor um objeto interno para navegação. Se `getCEPDeEntrega()` devolvesse `Endereco`, o chamador voltaria a fazer `.get().get()`, recriando o próprio "naufrágio de código" que a delegação deveria eliminar.

### A Lei de Demeter — item (b)

**Heurística:** Aplicação

**Afirmação:** ✔ O objetivo é impedir que o conhecimento sobre a hierarquia interna do sistema se espalhe sem controle.

**Resposta:** Verdadeiro

**Justificativa:** É a motivação da lei: cada ponto extra numa cadeia como `pedido.getCliente().getCarteira().getSaldo()` é uma promessa de que o código vai quebrar quando a estrutura intermediária mudar — Demeter contém esse espalhamento de conhecimento estrutural.

### A Lei de Demeter — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ "Falar com estranhos" (objetos obtidos navegando por outros objetos) aumenta a resiliência do código.

**Resposta:** Falso

**Justificativa:** É o oposto — "falar com estranhos" é a própria definição da violação (o "naufrágio de código"); aumenta a fragilidade, pois qualquer mudança na estrutura intermediária (como troca de `Carteira` por ApplePay) quebra o código que a atravessou diretamente.

### A Lei de Demeter — item (d)

**Heurística:** Aplicação

**Afirmação:** ✔ Um método de delegação, como `getCEPDeEntrega()`, é uma forma correta de respeitar a lei.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente a "cura" apresentada — delegação em cadeia guiada por *Tell, Don't Ask*, em que o objeto que detém os dados internos responde à pergunta certa por fora, sem que o chamador precise navegar pela estrutura interna.

### O Naufrágio de Código (Train Wreck) — item (a)

**Heurística:** Aplicação

**Afirmação:** ✔ É identificado por longas cadeias de chamadas, como `a.getB().getC().getD()`.

**Resposta:** Verdadeiro

**Justificativa:** É a assinatura visual do problema apresentada na aula, como em `pedido.getCliente().getCarteira().getSaldo()` — uma cadeia de `.get()` atravessando várias fronteiras de objeto.

### O Naufrágio de Código (Train Wreck) — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O problema real é puramente estético — o excesso de pontos polui a leitura do código.

**Resposta:** Falso

**Justificativa:** A aula é explícita: "o problema não é a quantidade de pontos — é a invasão de fronteiras"; o risco é estrutural (fragilidade a mudanças na estrutura intermediária), não estético (legibilidade).

### O Naufrágio de Código (Train Wreck) — item (c)

**Heurística:** Aplicação

**Afirmação:** ✔ Cada nível de navegação profunda é uma fronteira de objeto invadida.

**Resposta:** Verdadeiro

**Justificativa:** Cada `.get()` na cadeia atravessa a fronteira de um objeto diferente que não é "amigo próximo" de quem originou a chamada — exatamente a violação que a Lei de Demeter proíbe.

### O Naufrágio de Código (Train Wreck) — item (d)

**Heurística:** Aplicação

**Afirmação:** ✔ Se a estrutura intermediária (ex.: `Carteira`) mudar, o código que a navegou diretamente quebra.

**Resposta:** Verdadeiro

**Justificativa:** É a consequência prática destacada no exemplo do ApplePay: se `Checkout` navegasse até `Carteira` diretamente, trocar a carteira física por um aplicativo quebraria esse código; com delegação (`Checkout` fica cego para a existência de `Carteira`), o código permanece intocado.

### Tell, Don't Ask na Prática — item (a)

**Heurística:** Aplicação

**Afirmação:** ✔ Em vez de investigar o saldo do cliente para autorizar a venda, o sistema deve pedir ao `Pedido` que se valide.

**Resposta:** Verdadeiro

**Justificativa:** É o padrão `pedido.clientePodePagar()` do bloco: em vez de sondar (*Ask*) o saldo por fora, o chamador dá um comando/pergunta de alto nível (*Tell*) ao objeto que sabe como resolver isso internamente.

### Tell, Don't Ask na Prática — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ "Perguntar" por dados para decidir por fora é uma prática que fortalece o encapsulamento.

**Resposta:** Falso

**Justificativa:** É o oposto — "perguntar" por dados para decidir por fora é a prática *Ask* que a aula associa à violação de Demeter e ao *Feature Envy*; decidir por fora com dados de outro objeto enfraquece o encapsulamento, não o fortalece.

### Tell, Don't Ask na Prática — item (c)

**Heurística:** Aplicação

**Afirmação:** ✔ Mover a lógica para onde os dados residem evita que classes se tornem "fofoqueiras".

**Resposta:** Verdadeiro

**Justificativa:** É a cura apresentada para *Feature Envy* — mover o comportamento para a classe que detém o dado evita que uma classe externa precise "espiar" e operar sobre dados que não são seus.

### Tell, Don't Ask na Prática — item (d)

**Heurística:** Aplicação

**Afirmação:** ✔ `pedido.clientePodePagar()` é um exemplo de "Tell": o `Pedido` decide internamente como verificar isso.

**Resposta:** Verdadeiro

**Justificativa:** O chamador (`Checkout`) apenas invoca `clientePodePagar()` e recebe uma resposta; toda a lógica de como verificar o saldo (delegando ao `Cliente`) fica encapsulada dentro de `Pedido` — o chamador nunca "pergunta" pelos dados brutos.

### Delegação e Feature Envy — item (a)

**Heurística:** Transferência

**Afirmação:** ✗ Num sistema de RH que calcula bônus a partir do `Departamento` de um `Funcionario`, se o método `calcularBonus()` vive dentro de `Funcionario` mas lê `this.departamento.getMultiplicador()` internamente, isso já configura uma violação de delegação, pois `Funcionario` está "chamando" um método de outro objeto.

**Resposta:** Falso

**Justificativa:** Chamar um método de um colaborador direto (um atributo próprio, um "amigo") não é violação — é exatamente a definição de delegação em cadeia usada em `Carrinho.calcularTotal()` e em `Pedido.clientePodePagar()`. A violação ocorreria se `Funcionario` navegasse além de `Departamento` (ex.: `this.departamento.getEmpresa().getTabela()...`), atravessando uma fronteira que não é a de um amigo direto.

### Delegação e Feature Envy — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Um "orquestrador" como `Carrinho` deve calcular pessoalmente o subtotal de cada item, para garantir precisão.

**Resposta:** Falso

**Justificativa:** É o oposto do design apresentado — `Carrinho` não calcula nada sozinho, ele delega a cada `ItemCarrinho` o cálculo do próprio subtotal; fazer isso "pessoalmente" recriaria acoplamento e um Objeto Deus, sem qualquer ganho real de precisão.

### Delegação e Feature Envy — item (c)

**Heurística:** Aplicação

**Afirmação:** ✔ *Feature Envy* é o sintoma de uma classe mais interessada nos dados de outra do que nos próprios.

**Resposta:** Verdadeiro

**Justificativa:** É a própria definição do *code smell* apresentada na aula, associada ao naufrágio de código (`getCliente().getCarteira().getSaldo()`).

### Delegação e Feature Envy — item (d)

**Heurística:** Aplicação

**Afirmação:** ✔ A cura para *Feature Envy* é mover o método para a classe que de fato detém os dados necessários.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente a cura descrita — "mover o comportamento para onde os dados residem" — que resulta em métodos de delegação como `clientePodePagar()`.

### Programar para Abstrações — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Programar para um tipo genérico (`Pagavel`) em vez de uma classe concreta (`Boleto`) aumenta a rigidez.

**Resposta:** Falso

**Justificativa:** É o oposto do argumento da aula — programar para a interface aumenta a flexibilidade (Plug-and-Play), permitindo que `Pix` seja adicionado sem alterar `Checkout`; é programar para o tipo concreto que aumenta a rigidez, como mostra o erro de compilação do exemplo.

### Programar para Abstrações — item (b)

**Heurística:** Aplicação

**Afirmação:** ✔ O uso de tipos genéricos permite que o sistema aceite novos componentes sem alterar o código já existente.

**Resposta:** Verdadeiro

**Justificativa:** É a demonstração central do bloco: `Checkout.finalizar(Pagavel metodo)` aceita `Boleto`, `CartaoDeCredito` e, no futuro, `Pix`, sem qualquer alteração no código de `Checkout`.

### Programar para Abstrações — item (c)

**Heurística:** Aplicação

**Afirmação:** ✔ Referenciar objetos por suas interfaces é uma recomendação central para promover flexibilidade.

**Resposta:** Verdadeiro

**Justificativa:** É a analogia do "padrão USB-C" da aula — um encaixe universal, indiferente à identidade concreta de quem o implementa, é o que torna sistemas flexíveis e extensíveis.

### Programar para Abstrações — item (d)

**Heurística:** Aplicação

**Afirmação:** ✔ Um `Checkout` que recebe `Pagavel` funciona com qualquer classe futura que implemente esse contrato.

**Resposta:** Verdadeiro

**Justificativa:** É o próprio benefício do Plug-and-Play demonstrado: assim que `Pix implements Pagavel` existir, `Checkout.finalizar(Pagavel)` já sabe processá-lo, sem recompilação.

### O Erro de Tipagem como Diagnóstico — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Um erro de compilação ao passar `Boleto` onde se espera `CartaoDeCredito` é sempre um bug do compilador.

**Resposta:** Falso

**Justificativa:** A aula é explícita: esse erro "não é só uma falha sintática — é um diagnóstico de acoplamento forte"; o compilador está corretamente reportando uma limitação de design, não cometendo um bug.

### O Erro de Tipagem como Diagnóstico — item (b)

**Heurística:** Aplicação

**Afirmação:** ✔ Esse erro pode revelar que o sistema exige uma identidade específica em vez de uma capacidade funcional.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente a leitura proposta pela aula: o erro mostra que o parâmetro exige a classe `CartaoDeCredito` especificamente, quando deveria exigir apenas a capacidade de `isPagamentoValido()`.

### O Erro de Tipagem como Diagnóstico — item (c)

**Heurística:** Aplicação

**Afirmação:** ✔ A solução típica é generalizar o parâmetro para uma interface que ambas as classes implementem.

**Resposta:** Verdadeiro

**Justificativa:** É a solução apresentada — trocar o parâmetro de `CartaoDeCredito` para `Pagavel`, que ambas as classes (e futuras) podem implementar.

### O Erro de Tipagem como Diagnóstico — item (d)

**Heurística:** Aplicação

**Afirmação:** ✔ Elevar o nível de abstração do parâmetro reduz o acoplamento entre `Checkout` e os métodos de pagamento.

**Resposta:** Verdadeiro

**Justificativa:** É a conclusão do bloco anterior aplicada aqui: ao depender de `Pagavel` em vez de uma classe concreta, `Checkout` deixa de conhecer detalhes de qualquer meio de pagamento específico.

### Custo de Mudança e o Princípio TRUE — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Um sistema pode ser "Razoável" segundo o princípio TRUE mesmo que o custo de adicionar uma funcionalidade simples cresça proporcionalmente ao tamanho total do código já escrito, contanto que o código seja bem documentado.

**Resposta:** Falso

**Justificativa:** "Razoável" mede a relação entre o custo de uma mudança e o benefício/escala da própria mudança, não o tamanho acumulado do código já existente. Um custo que cresce com o tamanho total do sistema (em vez de com a complexidade da mudança em si) é sintoma de acoplamento alto — documentação não substitui contratos estáveis e baixo acoplamento como solução real para esse problema.

### Custo de Mudança e o Princípio TRUE — item (b)

**Heurística:** Aplicação

**Afirmação:** ✔ Um código é "Razoável" quando o custo de uma mudança é proporcional ao benefício que ela traz.

**Resposta:** Verdadeiro

**Justificativa:** É a definição de "Razoável" dentro do princípio TRUE — o custo de implementar algo não deveria ser desproporcional ao valor que essa mudança entrega.

### Custo de Mudança e o Princípio TRUE — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O design de caixa preta aumenta o custo de mudança, pois esconde erros atrás de interfaces.

**Resposta:** Falso

**Justificativa:** É o oposto — o design de caixa preta (interface estável, implementação oculta) reduz o custo de mudança, permitindo que a implementação evolua sem efeito cascata. "Esconder erros" confunde ocultar detalhes de implementação com mascarar bugs, que são coisas diferentes.

### Custo de Mudança e o Princípio TRUE — item (d)

**Heurística:** Aplicação

**Afirmação:** ✔ Contratos estáveis e baixo acoplamento evitam que o custo de uma nova funcionalidade cresça exponencialmente.

**Resposta:** Verdadeiro

**Justificativa:** É a tese geral da aula: quando cada objeto conhece apenas o contrato de seus colaboradores, adicionar ou trocar peças (como um novo `Pagavel`) não exige tocar em cascata em outras partes do sistema, mantendo o custo de mudança controlado.

### O Papel do Orquestrador — item (a)

**Heurística:** Aplicação

**Afirmação:** ✔ `Carrinho` atua como "maestro": coordena especialistas em vez de fazer o trabalho de cada um.

**Resposta:** Verdadeiro

**Justificativa:** É a metáfora central do bloco de colaboração — `Carrinho.calcularTotal()` orquestra chamando `item.subtotal()` de cada `ItemCarrinho`, sem calcular preços ou impostos por conta própria.

### O Papel do Orquestrador — item (b)

**Heurística:** Aplicação

**Afirmação:** ✔ A fronteira entre `Carrinho` e `ItemCarrinho` é respeitada quando o `Carrinho` soma subtotais já calculados.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente o que o código de `calcularTotal()` faz — soma os valores retornados por `item.subtotal()`, sem recalcular ou acessar os dados internos de `ItemCarrinho`.

### O Papel do Orquestrador — item (c)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se `ItemCarrinho` mudar sua fórmula de subtotal, `Carrinho` precisa ser reescrito para acompanhar.

**Resposta:** Falso

**Justificativa:** É exatamente o que o design por contrato evita — enquanto `ItemCarrinho.subtotal()` mantiver a mesma assinatura, `Carrinho` não precisa saber nem se importar com como o subtotal é calculado internamente; é o mesmo argumento de estabilidade de contrato do bloco "Design de Caixa Preta".

### O Papel do Orquestrador — item (d)

**Heurística:** Aplicação

**Afirmação:** ✔ Um bom orquestrador permanece estável mesmo quando a lógica interna de um especialista evolui.

**Resposta:** Verdadeiro

**Justificativa:** É a consequência direta de depender de contratos (o "O Quê") em vez de implementações (o "Como") — o orquestrador só é afetado se a assinatura do contrato mudar, não quando a lógica interna do especialista evolui.
