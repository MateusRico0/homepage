# Respostas das Pausas Ativas — Aula 3

> Arquivo de apoio, não publicado (prefixo `_`). Discute as perguntas
> motivadoras das pausas ativas do `index.qmd` e dá a solução dos
> respectivos V/F. O `index.qmd` publicado só contém a pergunta e os
> itens em cada pausa ativa, nunca a resolução.

## Interface, Implementação e Evolução

Se `Carrinho` tivesse um *getter* para `precoCusto` e calculasse a margem por fora, a lógica de margem deixaria de estar contida dentro de `Produto` e passaria a se repetir em toda classe que precisasse exibir ou usar um preço de venda. Quando a regra de margem mudasse — como de fato mudou, da fórmula simples para a fórmula com limiar de R\$ 1000 — seria preciso caçar e atualizar cada cópia dessa lógica espalhada pelo sistema, em vez de alterar um único método (`calcularPrecoDeVenda()`) por trás de uma assinatura que nunca muda. É exatamente o efeito cascata que o design de caixa preta existe para evitar.

- ✔ A interface define o "O Quê" um objeto promete fazer; a implementação é o "Como", escondido do cliente — é a definição central desta aula.
- ✔ Trocar a implementação interna de um método, mantendo sua assinatura, não deveria exigir mudanças no código cliente — é exatamente o benefício da estabilidade de contrato.
- ✗ `ItemCarrinho.subtotal()` deveria ler diretamente o atributo `precoBase` de `Produto` para ser mais eficiente — isso violaria o encapsulamento; `subtotal()` deve perguntar via `getPreco()`.
- ✔ Encapsular `calcularPrecoDeVenda()` dentro de `Produto` centraliza a política de margem num único lugar do sistema — é o mesmo argumento da seção de "Design de Caixa Preta", mudança de regra sem efeito cascata.

## Lei de Demeter e Tell, Don't Ask

Contar pontos é uma heurística sintática, e heurísticas sintáticas quebram em dois sentidos. Primeiro, uma cadeia longa pode ser inofensiva se todos os objetos atravessados forem "amigos" legítimos — uma *fluent interface* de configuração (`builder.comNome("x").comIdade(20).construir()`) tem vários pontos e nenhuma violação, porque cada chamada retorna o próprio objeto que está sendo configurado. Segundo, uma única navegação (`pedido.getCarteira()`) já pode violar a lei se `Carteira` não for um "amigo" direto de quem está chamando. "Fronteira invadida" acerta a causa real: o problema é depender da estrutura interna de um objeto que não deveria ser alcançado diretamente, não o número de pontos na linha.

- ✔ A Lei de Demeter recomenda que um objeto interaja apenas com seus "amigos próximos" — é a própria definição da lei.
- ✗ `pedido.getCliente().getCarteira().getSaldo()` é um exemplo saudável de reuso de getters — é o exemplo clássico de violação (*train wreck*).
- ✔ *Feature Envy* é o sintoma de uma classe mais interessada nos dados de outra do que nos próprios — é a definição do *code smell*.
- ✔ A cura técnica para o naufrágio de código é criar métodos de delegação, como `pedido.clientePodePagar()` — delegação em cadeia é exatamente a solução apresentada.

## Programando para Abstrações

Se `Checkout.finalizar` recebesse `CartaoDeCredito` em vez de `Pagavel`, o erro de compilação ao surgir `Pix` não seria um acidente de sintaxe — seria o compilador confirmando, mecanicamente, que o design amarrou uma operação de negócio (finalizar uma compra) a uma identidade de classe específica, em vez de a uma capacidade funcional (saber responder `isPagamentoValido()`). É o mesmo diagnóstico de acoplamento forte discutido ao longo da aula: exigir "ser um `CartaoDeCredito`" quando o que realmente importa é "saber validar um pagamento". A cura é sempre elevar o nível de abstração do parâmetro para o contrato que expressa a capacidade necessária.

- ✔ `Checkout.finalizar(Pagavel metodo)` aceita qualquer classe futura que implemente `Pagavel`, sem recompilação — é o próprio benefício do Plug-and-Play.
- ✗ Um erro de compilação ao tentar passar `Boleto` onde se espera `CartaoDeCredito` é sempre culpa do compilador, não do design — é um diagnóstico de acoplamento forte no design, não um bug do compilador.
- ✔ Programar para o tipo concreto (`CartaoDeCredito`) em vez da interface (`Pagavel`) aumenta o acoplamento do sistema — exigir a classe concreta é o próprio sintoma de acoplamento forte.
- ✔ Uma interface bem desenhada funciona como um "encaixe universal", indiferente à identidade concreta de quem a implementa — é a analogia do "padrão USB-C" desta seção.
