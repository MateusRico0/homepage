# Respostas das Pausas Ativas — Aula 4

> Arquivo de apoio, não publicado (prefixo `_`). Discute as perguntas
> motivadoras das pausas ativas do `index.qmd` e dá a solução dos
> respectivos V/F. O `index.qmd` publicado só contém a pergunta e os
> itens em cada pausa ativa, nunca a resolução.

## SRP, DI e Testabilidade

Sem Injeção de Dependência, `Pedido` cria suas próprias dependências concretas internamente (`new CartaoDeCredito(...)`, `new ServicoEmail(...)`), então qualquer teste do método `finalizar()` aciona o código real de cobrança e de envio de e-mail — não há como isolar a lógica de orquestração do restante. Com DI, o construtor recebe `Pagavel` e `Notificador` já prontos, e o teste injeta *mocks* no lugar dos objetos reais: o teste passa a exercitar só a lógica de `Pedido`, sem tocar em cartão de crédito ou servidor de e-mail de verdade.

- ✔ Uma classe que exige "E" para ser descrita numa frase provavelmente viola o SRP — é o próprio Teste do "E".
- ✔ Injeção de Dependência via construtor garante que o objeto nunca nasça sem suas colaborações essenciais — é o ganho central da injeção via construtor.
- ✔ Sem DI, testar a lógica de `Pedido` exigiria disparar um e-mail real ou cobrar um cartão de verdade — é exatamente o problema resolvido pela DI.
- ✗ Usar um "Mock" no lugar de `Pagavel` real é uma violação do princípio de Injeção de Dependência — usar um Mock é a aplicação correta de DI, não uma violação.

## Tipos de Associação

A declaração `private Cartao cartao` é sintaticamente idêntica nos dois casos — nada no código em si, isolado, diz se a relação é Agregação ou Composição. O que decide é a regra de domínio sobre o que deve acontecer ao `Cartao` quando o `Cliente` é excluído: se o cartão pode continuar existindo (por exemplo, sendo transferido para outro titular), a relação é Agregação; se o cartão só faz sentido atrelado a esse cliente específico e deve ser destruído junto, é Composição. A mesma linha de código pode representar as duas relações dependendo dessa regra de negócio, não da sintaxe.

- ✔ Na Dependência, o objeto usado costuma ser recebido como parâmetro de método, não guardado como atributo — é a natureza passageira da Dependência.
- ✗ Na Agregação, destruir o "todo" implica destruir automaticamente a "parte" — na Agregação, a parte sobrevive à destruição do todo; isso é característica da Composição.
- ✔ Na Composição, a "parte" não tem sentido de existir fora do "todo" — nasce e morre com ele — é a definição central de Composição.
- ✔ A escolha entre Agregação e Composição pode depender de uma regra de negócio, não só da sintaxe do código — o exemplo do cartão de crédito privado do `Cliente` mostra exatamente isso.

## Delegação e Tell, Don't Ask

É o mesmo mecanismo da Lei de Demeter da Aula 3, não algo diferente: a delegação dentro de `pagar()` respeita a lei porque `Cliente` só fala com seu próprio `Cartao` (um "amigo" direto, alcançável sem navegar por getters intermediários). É exatamente essa delegação interna que impede quem chama `pagar()` de precisar navegar até `Cartao` — e, portanto, de violar a lei — porque quem chama nunca precisa saber que `Cartao` existe.

- ✗ `joao.getCartao().processar(500.0)` respeita a Lei de Demeter, pois `Cartao` é um atributo de `Cliente` — `Cartao` ser atributo de `Cliente` não autoriza um objeto externo a navegar até ele; isso é o "naufrágio de código".
- ✔ `joao.pagar(500.0)` é um exemplo de "Tell": o chamador diz o que quer, sem saber como é feito — é a definição de "Tell" nesta aula.
- ✔ Depois da refatoração, o código que chama `pagar()` desconhece completamente a existência de `Cartao` — é o ganho central da delegação.
- ✔ Associação (ter um objeto) e Delegação (usar esse objeto) juntas permitem trocar o `Cartao` sem afetar quem chama `pagar()` — é a síntese de Associação + Delegação apresentada nesta seção.
