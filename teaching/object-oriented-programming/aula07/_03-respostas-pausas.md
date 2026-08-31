# Respostas das Pausas Ativas — Aula 7

> Arquivo de apoio, não publicado (prefixo `_`). Discute as perguntas
> motivadoras das pausas ativas do `index.qmd` e dá a solução dos
> respectivos V/F. O `index.qmd` publicado só contém a pergunta e os
> itens em cada pausa ativa, nunca a resolução.

## Taxonomia do Polimorfismo

A sobrecarga é resolvida inteiramente pelo compilador, olhando a assinatura declarada de cada chamada — não o objeto real em tempo de execução. Por isso ela é chamada de "polimorfismo aparente": embora existam várias versões do método `enviar`, qual delas roda já está decidido antes do programa começar a executar, e um tipo de contato novo (por exemplo, uma notificação por WhatsApp) obriga a voltar e escrever mais uma versão sobrecarregada — o comportamento não "emerge" do objeto manipulado, foi encaixado a dedo pelo programador. Isso é o inverso do polimorfismo de inclusão, em que o mesmo `forma.criarCobranca()` produz comportamentos diferentes sem que o código chamador saiba, ou precise saber, qual implementação está por trás.

- ✔ O polimorfismo ad-hoc funciona apenas sobre um conjunto finito e delimitado de tipos — é a definição de ad-hoc.
- ✔ A sobrecarga (overloading) é resolvida pelo compilador em tempo de compilação, com base nos argumentos passados — é *Early Binding*.
- ✔ O polimorfismo de inclusão é resolvido em tempo de execução, olhando o objeto real na memória — é *Late Binding*, o pilar do desacoplamento em OO.
- ✗ A sobrecarga de métodos resolve completamente o problema da extensibilidade prevista pelo OCP — pelo contrário, é considerada "polimorfismo aparente", que não resolve extensibilidade.

## OCP e Substitutibilidade

Nada muda no `CheckoutController`. A nova classe `Cripto` só precisa implementar `Pagavel`; o controlador continua chamando `formaEscolhida.criarCobranca(total)` exatamente como antes, sem saber que `Cripto` existe. É a demonstração mais concreta do OCP dentro da aula: "aberto para extensão" significa que o sistema cresce por adição de classes novas, nunca por edição do código que já funciona — e é exatamente esse fechamento que garante que os testes já escritos para o `CheckoutController` continuam válidos sem revisão.

- ✗ Adicionar `Cripto implements Pagavel` exige alterar o código do `CheckoutController` — é exatamente o ponto: nenhuma linha do controlador muda.
- ✔ "Aberto para extensão" significa que novos comportamentos entram por novas classes, não por edição das antigas — é a definição de "aberto para extensão".
- ✔ Precisar de `instanceof` para decidir o que fazer com um objeto de negócio é sinal de que o polimorfismo não foi bem aproveitado — é a meta-regra prática desta aula.
- ✔ A substitutibilidade é o que permite ao `CheckoutController` tratar `Pix`, `Boleto` e `Cripto` de forma idêntica — é a substitutibilidade via `Pagavel`.

## Generics e o Fim do Mar de IFs

Generics é uma instância do Polimorfismo Universal Paramétrico: o mesmo algoritmo de lista (armazenar, iterar, ordenar) funciona identicamente para `List<Pagavel>`, `List<Produto>` ou `List<Cliente>`, sem que essas classes precisem compartilhar nenhuma relação de herança entre si. Isso contrasta com o Polimorfismo de Inclusão, que depende inteiramente de uma hierarquia comum (`implements Pagavel`) para funcionar — Generics dispensa esse parentesco porque o "encaixe" não está na estrutura das classes armazenadas, está no próprio mecanismo da coleção, que passa a impor a etiqueta de tipo em tempo de compilação em vez de aceitar qualquer `Object`.

- ✔ Sem Generics, um erro de tipo numa coleção só é detectado quando o item incompatível é efetivamente usado, não quando é inserido — é a "detecção tardia" descrita nesta aula.
- ✔ `List<Pagavel>` impede, em tempo de compilação, que um objeto incompatível seja adicionado à lista — é o ganho central de Generics.
- ✗ Generics é uma forma de Polimorfismo Ad-hoc, resolvida da mesma forma que a sobrecarga de métodos — Generics é Polimorfismo Universal Paramétrico, resolvido de forma bem diferente da sobrecarga.
- ✔ Precisar de um `if` para verificar o tipo concreto de um objeto de negócio é um sintoma de violação do OCP — é a meta-regra do bloco anterior.
