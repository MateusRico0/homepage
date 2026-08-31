# Respostas das Pausas Ativas — Aula 8

> Arquivo de apoio, não publicado (prefixo `_`). Discute as perguntas
> motivadoras das pausas ativas do `index.qmd` e dá a solução dos
> respectivos V/F. O `index.qmd` publicado só contém a pergunta e os
> itens em cada pausa ativa, nunca a resolução.

## Quando Herdar

O critério certo é comportamental, não sintático: a pergunta não é "dá para reaproveitar métodos herdando?" (quase sempre dá), mas "esse objeto precisa ser tratado, em algum lugar do sistema, como se fosse o tipo base?". `GerenciadorDeCobrancas` nunca precisa ser passado onde se espera uma `ListaDeContatos` — ele só quer os métodos de manipulação de array já prontos. Isso é "usar uma lista". Já `Pix`, `Cartao` e `Boleto` precisam, sim, ser tratados como `MeioPagamentoBase` (armazenados numa mesma coleção, percorridos polimorficamente) — isso é "ser um" meio de pagamento. A composição resolve o primeiro caso sem os efeitos colaterais da herança: métodos indesejados do pai (como limpar a lista inteira) não vazam para o filho, e o compilador não aceita mais o gerenciador em lugares que esperam uma lista.

- ✔ Herdar apenas para reaproveitar métodos, sem uma relação "É-UM" real, é um design frágil — é o "erro da herança por conveniência".
- ✔ `GerenciadorDeCobrancas extends ListaDeContatos` expõe métodos do pai que talvez nunca devessem ser públicos no filho — é a quebra de encapsulamento citada no exemplo.
- ✔ Uma especialização legítima precisa compartilhar o DNA do pai e ser tratada polimorficamente como ele — são os dois requisitos cumulativos da especialização legítima.
- ✗ Uma subclasse que não adiciona comportamento nem refina invariantes ainda agrega valor arquitetural por existir — sem adicionar nada, é um "objeto zumbi" que só polui a taxonomia.

## Classes Abstratas e Herança de Estado

A diferença está em o que cada mecanismo herda. Métodos são comportamento: a JVM despacha a chamada via Late Binding olhando o objeto real, então "recusar" o método do pai e fornecer outro no lugar (`@Override`) é só redirecionar esse despacho para uma implementação diferente — o mecanismo já existe para escolher entre implementações. Atributos são estado: a estrutura física de uma instância (quais campos e em que posição relativa da memória) é decidida a partir do layout completo da classe, incluindo tudo o que foi herdado, no momento da compilação/carregamento da classe. Não existe um mecanismo equivalente de "não alocar este campo" porque o processo de alocação não pergunta, campo por campo, se o filho vai usá-lo — ele simplesmente segue o layout herdado por completo.

- ✔ Uma classe abstrata pode ter métodos concretos e métodos abstratos ao mesmo tempo — é a definição de "protocolo de estado parcial".
- ✗ O compilador permite instanciar diretamente uma classe abstrata com `new`, desde que todos os métodos existam — o compilador proíbe `new` numa classe abstrata, completa ou não.
- ✔ Herdar um atributo é uma alocação de memória física compulsória em cada instância do filho — é o custo da "herança de estado" descrito nesta aula.
- ✔ Não existe, em Java, uma sintaxe para um filho "recusar" um campo herdado do pai — diferente de métodos (que aceitam `@Override`), atributos são herdados sem opção de recusa.

## Template Method e Inversão de Controle

Se `Pix` pudesse sobrescrever `realizarPagamento()` inteiro, o sistema perderia exatamente a garantia que motiva o padrão: que validação, criação da cobrança específica e registro de log acontecem sempre, nessa ordem, para qualquer meio de pagamento. Nada impediria `Pix` de esquecer o `registrarLog()`, ou de inverter a ordem entre validar e processar — cada subclasse ficaria livre para reintroduzir os mesmos bugs que o esqueleto centralizado na base foi desenhado para eliminar. O ganho do Template Method não é só "código compartilhado"; é o controle de que a sequência de passos é imutável e centralizada num único lugar (a base, via `final`), com a Inversão de Controle garantindo que é sempre a base quem decide quando chamar o gancho do filho — nunca o contrário.

- ✔ Se `realizarPagamento()` não fosse `final`, uma subclasse poderia pular a validação ou o registro de log — é exatamente o risco de não travar o método com `final`.
- ✔ O gancho `criarCobrancaEspecifica()` é o único ponto que cada subclasse precisa conhecer para se especializar — é o propósito do gancho: isolar o detalhe técnico.
- ✗ No Template Method, é o filho quem decide a ordem em que validação, especialização e log acontecem — é o pai quem dita a ordem; o filho só preenche a lacuna.
- ✔ A Inversão de Controle aqui significa que a base chama o filho, e não o contrário — é a essência do Princípio de Hollywood aplicado aqui.
