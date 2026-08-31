# Soluções — Questões de Verdadeiro/Falso (Aula 4)

> Arquivo de apoio, não publicado (prefixo `_`). Contém a resposta e a
> justificativa de cada item das 12 questões de V/F do `index.qmd`. O
> `index.qmd` publicado continua sem solução — este arquivo existe só
> para conferência do professor/monitor, seguindo a metodologia de
> criação de questões definida em `../../CLAUDE.md`.

### A Classe Deus (God Class) — item (a)

**Heurística:** Aplicação

**Afirmação:** ✔ É identificada por centralizar lógicas de múltiplos atores (financeiro, infraestrutura, UI) num único arquivo.

**Resposta:** Verdadeiro

**Justificativa:** É a descrição direta do `Pedido` do início da aula, que reúne cálculo (negócio), impostos, formatação, persistência e e-mail — cinco responsabilidades de atores/departamentos diferentes num único arquivo.

### A Classe Deus (God Class) — item (b)

**Heurística:** Aplicação

**Afirmação:** ✔ O "Teste do E" ajuda a diagnosticá-la: se a classe faz X E Y, provavelmente tem responsabilidades demais.

**Resposta:** Verdadeiro

**Justificativa:** É a heurística apresentada na aula para detectar violações do SRP — precisar de "E" (ou "OU") para descrever a classe numa frase é o sinal de alerta.

### A Classe Deus (God Class) — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Uma Classe Deus facilita a manutenção, pois toda a lógica fica concentrada num só lugar.

**Resposta:** Falso

**Justificativa:** É o oposto do que a aula demonstra — concentrar tudo aumenta a fragilidade (mudar imposto, banco ou layout do recibo, todos exigem alterar `Pedido`), o acoplamento com infraestrutura e a carga cognitiva; "concentrado" não é sinônimo de "fácil de manter".

### A Classe Deus (God Class) — item (d)

**Heurística:** Aplicação

**Afirmação:** ✔ Testar isoladamente uma responsabilidade de uma Classe Deus costuma exigir efeitos colaterais indesejados (e-mail, banco).

**Resposta:** Verdadeiro

**Justificativa:** É um dos quatro problemas listados na aula — testar o cálculo do total de um `Pedido` que também salva no banco e envia e-mail dispara, na prática, esses efeitos colaterais reais.

### Coesão e Acoplamento — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se duas classes com métodos completamente distintos (sem nenhum atributo em comum) fossem fundidas numa única classe apenas para reduzir o número de arquivos do projeto, essa fusão aumentaria a coesão do sistema.

**Resposta:** Falso

**Justificativa:** Fundir métodos que não compartilham nenhum atributo é exatamente o cenário de LCOM alto (interseção de uso vazia) discutido com `GestorDeUsuario` — a fusão não cria nenhuma relação lógica entre as responsabilidades, apenas empilha duas classes de baixa coesão dentro de uma única caixa.

### Coesão e Acoplamento — item (b)

**Heurística:** Limite

**Afirmação:** ✗ No limite em que uma classe `A` depende de tantos detalhes internos de uma classe `B` que qualquer mudança em `B` obriga a reescrever `A`, dizemos que `A` e `B` têm acoplamento muito baixo.

**Resposta:** Falso

**Justificativa:** Esse cenário extremo é a própria definição operacional de acoplamento muito ALTO — o vínculo entre `A` e `B` é tão forte que `B` não pode evoluir livremente sem quebrar `A`; baixo acoplamento seria o oposto, `A` permanecendo estável mesmo com mudanças internas em `B`.

### Coesão e Acoplamento — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Numa oficina mecânica organizada em bancadas por especialidade (uma para motor, uma para elétrica, uma para funilaria), cada bancada guardando só as ferramentas da sua especialidade é uma analogia de alta coesão, assim como a caixa de ferramentas só com chaves de fenda desta aula.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma estrutura da analogia da aula (caixa só com chaves de fenda = alta coesão) transferida para um novo domínio: cada bancada concentra ferramentas relacionadas à mesma especialidade, sem misturar propósitos diferentes.

### Coesão e Acoplamento — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Duas classes podem ter baixo acoplamento entre si mesmo que cada uma, isoladamente, tenha baixíssima coesão.

**Resposta:** Verdadeiro

**Justificativa:** Coesão é uma propriedade interna de uma única classe (o quanto suas responsabilidades pertencem juntas); acoplamento é uma propriedade da relação entre duas classes. As duas métricas costumam melhorar juntas na prática ao se aplicar o SRP, mas são logicamente independentes — nada impede, em princípio, duas classes de baixa coesão internas e baixo acoplamento mútuo.

### SRP e o Teste do "E" — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Se uma classe tiver apenas um único método público, isso já garante que ela respeita o SRP.

**Resposta:** Falso

**Justificativa:** O número de métodos públicos não mede razões de mudança — um único método público pode esconder múltiplas responsabilidades misturadas internamente, como o antigo `Pedido.finalizarPedido()`, que num só método fazia cálculo, processamento de pagamento e notificação por e-mail.

### SRP e o Teste do "E" — item (b)

**Heurística:** Aplicação

**Afirmação:** ✔ Se a descrição de uma classe exige a conjunção "E", ela provavelmente viola o SRP.

**Resposta:** Verdadeiro

**Justificativa:** É o próprio Teste do "E" apresentado na aula como heurística de diagnóstico do SRP.

### SRP e o Teste do "E" — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Aplicar o SRP significa que uma classe só pode ter um único método público.

**Resposta:** Falso

**Justificativa:** SRP fala de razões de mudança, não de contagem de métodos; uma classe coesa pode legitimamente ter vários métodos públicos relacionados (como `Conta.debitar()`/`creditar()`), desde que todos sirvam à mesma responsabilidade e à mesma razão de mudança.

### SRP e o Teste do "E" — item (d)

**Heurística:** Aplicação

**Afirmação:** ✔ `Pedido` que calcula total, processa pagamento e envia e-mail no mesmo método viola o SRP.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente o exemplo `finalizarPedido()` apresentado como violação — calcular, processar pagamento e notificar são três razões de mudança independentes misturadas no mesmo método.

### Injeção de Dependência — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se `Pedido` continuasse criando `new CartaoDeCredito()` e `new ServicoEmail()` dentro do próprio construtor, mas guardasse essas instâncias em atributos privados corretamente encapsulados, isso já seria suficiente para obter os ganhos de testabilidade da Injeção de Dependência.

**Resposta:** Falso

**Justificativa:** O ganho de testabilidade vem de quem decide a implementação concreta, não de onde ou como a referência é guardada. Criar as dependências com `new` dentro do próprio construtor continua acoplando `Pedido` a classes concretas específicas e impede substituí-las por mocks no teste — encapsular o atributo não resolve esse problema.

### Injeção de Dependência — item (b)

**Heurística:** Aplicação

**Afirmação:** ✔ A injeção via construtor garante que o objeto nunca exista sem suas dependências essenciais.

**Resposta:** Verdadeiro

**Justificativa:** É o ganho central apresentado — se o construtor exige `Pagavel` e `ServicoEmail` como parâmetros, é impossível instanciar um `Pedido` sem esses colaboradores.

### Injeção de Dependência — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ A DI aumenta o acoplamento, pois obriga o objeto a conhecer quem o instanciou.

**Resposta:** Falso

**Justificativa:** A DI reduz o acoplamento com implementações concretas — `Pedido` conhece apenas o contrato `Pagavel`/`ServicoEmail`, não uma classe concreta específica; e o objeto não precisa saber "quem o instanciou", apenas recebe as dependências já prontas.

### Injeção de Dependência — item (d)

**Heurística:** Aplicação

**Afirmação:** ✔ Sem DI, testar `Pedido.finalizar()` isoladamente, sem efeitos colaterais reais, é muito mais difícil.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente o problema que motiva a refatoração — sem DI, testar a lógica de orquestração exigiria cobrar um cartão de verdade ou enviar um e-mail real.

### A Teoria do Ator no SRP — item (a)

**Heurística:** Transferência

**Afirmação:** ✗ Numa fintech em que o mesmo microsserviço calcula o score de crédito (usado pelo time de Risco) e também formata esse score para exibição no app do cliente (usado pelo time de Produto), esse serviço, pela Teoria do Ator, tem apenas uma razão para mudar, pois lida com um único conceito: "score de crédito".

**Resposta:** Falso

**Justificativa:** Mesma estrutura do exemplo `Funcionario` (CFO vs. RH): "score de crédito" é um conceito, mas dois atores diferentes (Risco e Produto) solicitam mudanças por motivos independentes — um ajusta o modelo de risco, o outro ajusta o layout de exibição. Pela Teoria do Ator, isso são duas razões de mudança, não uma.

### A Teoria do Ator no SRP — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Misturar lógica solicitada pelo RH e pelo Financeiro na mesma classe é seguro, pois são setores diferentes.

**Resposta:** Falso

**Justificativa:** É exatamente o oposto — serem setores diferentes é o que torna a mistura arriscada: uma mudança de layout de relatório solicitada pelo RH força recompilar e re-testar a lógica de folha de pagamento do Financeiro, mesmo sem nenhuma relação de negócio entre as duas.

### A Teoria do Ator no SRP — item (c)

**Heurística:** Aplicação

**Afirmação:** ✔ O conflito de atores é uma fonte comum de "quebras colaterais" em classes com múltiplas razões de mudança.

**Resposta:** Verdadeiro

**Justificativa:** É a consequência prática destacada no exemplo `Funcionario` — misturar as lógicas acopla os ciclos de lançamento de departamentos diferentes.

### A Teoria do Ator no SRP — item (d)

**Heurística:** Limite

**Afirmação:** ✔ No limite em que uma empresa tem um único departamento responsável por todas as decisões de negócio (sem separação entre financeiro, RH, produto etc.), a Teoria do Ator deixaria de fazer qualquer distinção útil entre classes, pois haveria apenas um ator possível para todo o sistema.

**Resposta:** Verdadeiro

**Justificativa:** A Teoria do Ator identifica razões de mudança por quem solicita a mudança; se só existe um ator possível na organização inteira, todas as classes compartilhariam, por esse critério, a mesma "razão para mudar" — o poder discriminador da teoria só aparece quando há múltiplos atores reais e distintos, como CFO e RH no exemplo da aula.

### A Métrica LCOM — item (a)

**Heurística:** Limite

**Afirmação:** ✗ No limite em que todo método de uma classe usa exatamente os mesmos atributos que todos os outros métodos, o LCOM dessa classe seria o mais alto possível.

**Resposta:** Falso

**Justificativa:** É o oposto — se todo método usa o mesmo conjunto de atributos, a interseção de uso entre os métodos é máxima, então a falta de coesão é mínima: o LCOM seria o mais BAIXO possível, indicando uma classe bem coesa (o antônimo do exemplo `GestorDeUsuario`, em que a interseção de uso era vazia).

### A Métrica LCOM — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Um LCOM alto indica uma classe muito coesa e bem projetada.

**Resposta:** Falso

**Justificativa:** LCOM significa *Lack of Cohesion in Methods* — um valor alto indica FALTA de coesão, não o contrário; é o sinal de que a classe deveria ser dividida, como no exemplo `GestorDeUsuario`.

### A Métrica LCOM — item (c)

**Heurística:** Aplicação

**Afirmação:** ✔ Se metade dos métodos usa o atributo A e a outra metade usa só o atributo B, a classe deveria ser dividida.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente o cenário de `GestorDeUsuario` (`nome` usado só por `salvarNome()`, `ipConexao` usado só por `logAcesso()`) — interseção de uso vazia, o código "implorando" para virar duas classes (`RepositorioUsuario` e `AuditoriaAcesso`).

### A Métrica LCOM — item (d)

**Heurística:** Aplicação

**Afirmação:** ✔ LCOM é uma forma de provar matematicamente que uma classe é, na prática, duas classes disfarçadas.

**Resposta:** Verdadeiro

**Justificativa:** É a conclusão apresentada na aula sobre a métrica — uma prova quantitativa de falta de coesão, complementando o julgamento qualitativo do Teste do "E".

### O Lado Sombrio do SRP — item (a)

**Heurística:** Transferência

**Afirmação:** ✗ Num sistema de e-commerce em que adicionar um novo campo obrigatório ("CPF do comprador") ao formulário de checkout exige editar 20 classes de uma linha cada (uma para nome, uma para e-mail, uma para CPF etc.), esse cenário ilustra a Cirurgia de Espingarda, e a solução recomendada pela aula é sempre criar ainda mais classes minúsculas para isolar o novo campo.

**Resposta:** Falso

**Justificativa:** O cenário descrito é, sim, Cirurgia de Espingarda — mas a solução da aula vai na direção OPOSTA: agrupar o que muda junto e pelos mesmos motivos, consolidando campos relacionados (como os dados do comprador) numa única classe coesa (`DadosComprador`), em vez de fragmentar ainda mais.

### O Lado Sombrio do SRP — item (b)

**Heurística:** Aplicação

**Afirmação:** ✔ O Modelo Anêmico é uma consequência possível da aplicação fanática e sem pragmatismo do SRP.

**Resposta:** Verdadeiro

**Justificativa:** É um dos dois riscos do "lado sombrio" apresentados na aula — retirar toda a responsabilidade do objeto em nome da separação de responsabilidades reduz a classe a um contêiner passivo.

### O Lado Sombrio do SRP — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O SRP proíbe que uma classe como `Conta` gerencie seu próprio saldo internamente.

**Resposta:** Falso

**Justificativa:** É o oposto — a aula argumenta que assegurar a integridade do próprio saldo é a responsabilidade primária de `Conta`; o SRP equilibrado (Modelo Rico) mantém `debitar()`/`creditar()` dentro da própria classe.

### O Lado Sombrio do SRP — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como o SRP recomenda alta coesão, uma classe `Conta` que gerencia tanto `debitar()` quanto `creditar()` sobre o mesmo saldo já é, por si só, uma violação leve do SRP, pois tem dois métodos que alteram o mesmo estado.

**Resposta:** Falso

**Justificativa:** Dois métodos que operam sobre o mesmo atributo, pelo mesmo motivo de negócio (preservar a integridade do saldo), não são duas razões de mudança — são a mesma razão exercida de duas formas. É exatamente o exemplo de "Modelo Rico" equilibrado da aula, o oposto de uma violação.

### Associação: Dependência ("Usa um") — item (a)

**Heurística:** Limite

**Afirmação:** ✗ Se um método recebesse um objeto como parâmetro e o armazenasse permanentemente num atributo da classe logo na primeira linha do método, essa relação continuaria sendo classificada como Dependência.

**Resposta:** Falso

**Justificativa:** Guardar a referência permanentemente como atributo é justamente o que transforma a relação em Agregação (ou Composição) — o traço definidor de Dependência é não persistir a referência para uso futuro, usando o objeto apenas durante a execução do método.

### Associação: Dependência ("Usa um") — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O objeto usado numa dependência costuma ser guardado como atributo de longo prazo.

**Resposta:** Falso

**Justificativa:** É o oposto — na Dependência, o objeto normalmente é recebido como parâmetro e não guardado; o vínculo é passageiro, como usar e devolver uma caneta emprestada do balcão.

### Associação: Dependência ("Usa um") — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Um método de uma API de pagamentos que recebe um objeto `ContextoDeAuditoria` só para registrar um log da chamada atual, sem guardar essa referência para uso posterior, exemplifica o mesmo tipo de vínculo fraco (Dependência) visto em `Carrinho.confereTotal()`.

**Resposta:** Verdadeiro

**Justificativa:** Mesma estrutura transferida para outro domínio: uso temporário de um objeto recebido como parâmetro, sem armazená-lo como atributo — a marca definidora da Dependência.

### Associação: Dependência ("Usa um") — item (d)

**Heurística:** Aplicação

**Afirmação:** ✔ `Carrinho.confereTotal(ArrayList<Produto> itens)` recebendo a lista como parâmetro é um exemplo de dependência.

**Resposta:** Verdadeiro

**Justificativa:** É o próprio exemplo de código da aula — a lista é usada só para conferir o total, sem ser guardada em `this.itens`.

### Associação: Agregação ("Tem um") — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se, no exemplo do `Carrinho` e dos `Produto`, destruir o carrinho (`carrinho = null`) também apagasse os `Produto` do catálogo do sistema, essa relação ainda seria corretamente chamada de Agregação.

**Resposta:** Falso

**Justificativa:** A marca definidora de Agregação é justamente a parte sobrevivendo à destruição do todo (o `Produto` continua existindo no catálogo); se destruir o `Carrinho` também apagasse os `Produto`, a relação teria as propriedades de Composição, não de Agregação.

### Associação: Agregação ("Tem um") — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Se um `Carrinho` for destruído, os `Produto` que ele referenciava também são destruídos.

**Resposta:** Falso

**Justificativa:** É o oposto — a aula é explícita: "Se o carrinho for destruído, o Smartphone ainda existe no catálogo!"; ciclos de vida independentes são a essência da Agregação.

### Associação: Agregação ("Tem um") — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Vários objetos "todo" diferentes podem referenciar o mesmo objeto "parte" simultaneamente.

**Resposta:** Verdadeiro

**Justificativa:** Como a Agregação não implica posse exclusiva, o mesmo `Produto` do catálogo pode estar, ao mesmo tempo, referenciado por vários `Carrinho` de clientes diferentes — diferente da Composição, em que a posse é exclusiva.

### Associação: Agregação ("Tem um") — item (d)

**Heurística:** Aplicação

**Afirmação:** ✔ É uma forma de posse mais fraca do que a Composição.

**Resposta:** Verdadeiro

**Justificativa:** A escala de força estrutural apresentada na aula vai de Dependência (mais fraca) a Agregação a Composição (mais forte); Agregação permite ciclos de vida independentes, enquanto Composição os atrela.

### Associação: Composição ("É parte de") — item (a)

**Heurística:** Limite

**Afirmação:** ✗ No limite em que um objeto "parte" de uma Composição pudesse ser compartilhado por dois objetos "todo" diferentes ao mesmo tempo, a relação continuaria sendo, por definição, uma Composição.

**Resposta:** Falso

**Justificativa:** Posse exclusiva do todo sobre a parte é o traço definidor de Composição; se a parte passasse a ser compartilhada por dois todos, ela deixaria de ter um único proprietário, e a relação teria as propriedades de Agregação, não mais de Composição.

### Associação: Composição ("É parte de") — item (b)

**Heurística:** Transferência

**Afirmação:** ✔ Num sistema de RH em que cada `Funcionario` tem seu próprio `HistoricoDisciplinar`, criado apenas quando o funcionário é contratado e apagado quando o funcionário é desligado do sistema, essa relação seria mais bem classificada como Composição do que como Agregação.

**Resposta:** Verdadeiro

**Justificativa:** Mesma estrutura de ciclo de vida atrelado vista em `Cliente`/`Cartao` (nasce e morre com o todo), aplicada a um domínio novo — `HistoricoDisciplinar` não tem sentido de existir fora do `Funcionario` que o originou.

### Associação: Composição ("É parte de") — item (c)

**Heurística:** Aplicação

**Afirmação:** ✔ Um `Documento` e suas `Pagina` são um exemplo clássico de Composição.

**Resposta:** Verdadeiro

**Justificativa:** É o exemplo citado na aula para ilustrar Composição — as páginas não têm sentido de existir fora do documento a que pertencem.

### Associação: Composição ("É parte de") — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ A escolha entre Agregação e Composição é sempre puramente sintática, nunca uma decisão de negócio.

**Resposta:** Falso

**Justificativa:** É o oposto do argumento central da aula — a sintaxe de declarar `private Cartao cartao` é idêntica nos dois casos; o que decide é uma regra de domínio de negócio, como o que deve acontecer aos dados do cartão quando a conta do cliente é excluída.

### Delegação — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se um método `pagar()` delegasse ao `Cartao` a operação de processar o valor, mas antes disso navegasse por `this.cartao.getBanco().getGerente()` só para registrar um log, essa navegação extra ainda seria uma delegação limpa, sem qualquer violação de Demeter.

**Resposta:** Falso

**Justificativa:** Navegar até `getBanco().getGerente()` atravessa fronteiras de objetos que não são amigos diretos de `Cliente` (nem mesmo de `Cartao`), recriando o naufrágio de código dentro do próprio método — o fato de o método também delegar corretamente a operação principal ao `Cartao` não perdoa essa navegação extra.

### Delegação — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ `joao.getCartao().processar(500.0)` é um exemplo correto de delegação.

**Resposta:** Falso

**Justificativa:** É o oposto — é o exemplo do "naufrágio de código"/violação de Demeter que a aula usa como ponto de partida a ser corrigido, não um exemplo de delegação correta.

### Delegação — item (c)

**Heurística:** Aplicação

**Afirmação:** ✔ `joao.pagar(500.0)`, delegando internamente ao `Cartao`, corrige a violação de Demeter do exemplo anterior.

**Resposta:** Verdadeiro

**Justificativa:** É a correção apresentada — o chamador passa a falar só com `Cliente` (um amigo direto de si mesmo), que por sua vez delega ao seu próprio `Cartao`.

### Delegação — item (d)

**Heurística:** Aplicação

**Afirmação:** ✔ A delegação é o mecanismo que torna a composição uma alternativa flexível à herança.

**Resposta:** Verdadeiro

**Justificativa:** É a síntese apresentada no final do bloco — Associação (ter) somada a Delegação (usar) torna a composição tão poderosa quanto a herança, porém mais flexível.

### Tell, Don't Ask e a Síntese da Aula — item (a)

**Heurística:** Transferência

**Afirmação:** ✗ Num sistema de estoque em que, antes de vender um produto, o código lê `produto.getQuantidade()` e `produto.getQuantidadeMinima()` para decidir por fora se a venda é permitida, esse padrão está alinhado com "Tell, Don't Ask", da mesma forma que `pedido.clientePodePagar()` está.

**Resposta:** Falso

**Justificativa:** É o oposto — sondar dois atributos por fora para decidir é exatamente o padrão *Ask* que a aula contrasta com *Tell*; o equivalente alinhado com `pedido.clientePodePagar()` seria um método como `produto.podeVender(quantidade)`, que decide internamente e devolve só a resposta.

### Tell, Don't Ask e a Síntese da Aula — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Associação, SRP e Delegação são princípios independentes, sem nenhuma relação entre si.

**Resposta:** Falso

**Justificativa:** É o oposto da síntese da aula — Associação define a estrutura (quem contém quem), SRP orienta como dividir responsabilidades entre essas estruturas, e Delegação é o comportamento que torna essa divisão funcional; os três se encaixam na mesma arquitetura viva.

### Tell, Don't Ask e a Síntese da Aula — item (c)

**Heurística:** Aplicação

**Afirmação:** ✔ Um sistema bem decomposto reduz a carga cognitiva ao permitir raciocinar sobre uma responsabilidade por vez.

**Resposta:** Verdadeiro

**Justificativa:** É um dos benefícios centrais do SRP e da decomposição em especialistas discutidos ao longo da aula — evita a "carga cognitiva alta" citada como problema da Classe Deus.

### Tell, Don't Ask e a Síntese da Aula — item (d)

**Heurística:** Aplicação

**Afirmação:** ✔ Delegar ao especialista certo permite trocar sua implementação sem que o orquestrador precise mudar.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma lógica de estabilidade de contrato vista com `Pagavel` — trocar `Cartao` por outro meio de pagamento, ou alterar a lógica interna do especialista, não afeta quem apenas delega a ele.
