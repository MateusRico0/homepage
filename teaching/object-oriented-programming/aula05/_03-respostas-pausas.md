# Respostas das Pausas Ativas — Aula 5

> Arquivo de apoio, não publicado (prefixo `_`). Discute as perguntas
> motivadoras das pausas ativas do `index.qmd` e dá a solução dos
> respectivos V/F. O `index.qmd` publicado só contém a pergunta e os 4
> itens de V/F em cada pausa ativa (idênticos nas notas e nos slides);
> a resolução, nos slides, aparece no slide seguinte — mas nunca nas
> notas em HTML.

## Feature Envy e CBO

Um CBO baixo diz respeito só à *quantidade* de classes externas às
quais uma classe está ligada — não diz nada sobre a *qualidade* de
cada uma dessas ligações. É perfeitamente possível uma classe ter
CBO=1 (uma única dependência) e essa única dependência ser do pior
tipo possível, o Acoplamento de Conteúdo (alterando atributos internos
de outra classe diretamente) — e uma classe com CBO=3 pode ter as três
dependências no nível ideal, o Acoplamento de Dados. Contar
dependências (CBO) e julgar a qualidade de cada uma (Escala de Myers,
o assunto do próximo bloco) são duas métricas complementares, não uma
substituindo a outra. Isso também explica por que "passar a dependência
certinho pelo construtor" (associação estruturalmente correta) não
garante nada sobre o comportamento do método: `Pedido` podia ter CBO=1
com `Carrinho` e ainda cometer Feature Envy, processando os dados do
colaborador por fora.

- ✗ Passar uma dependência via construtor garante, por si só, o
  desacoplamento lógico entre as classes — é exatamente a "falsa
  segurança" desta aula: a estrutura (como o objeto chega até você) e
  o comportamento (o que você faz com ele) são independentes; a
  primeira pode estar impecável enquanto a segunda ainda comete
  Feature Envy.
- ✔ Feature Envy é o sintoma de um método mais interessado nos dados de
  outra classe do que nos seus próprios — é a definição de Fowler para
  o *code smell*, e o diagnóstico central desta aula.
- ✔ Refatorar de Inveja de Recursos para Delegação Pura reduz o CBO da
  classe orquestradora — o exemplo `Pedido` mostrou CBO caindo de 2
  (`Carrinho` + `Produto`) para 1 (só `Carrinho`), porque a iteração
  sobre `Produto` deixou de acontecer dentro de `Pedido`.
- ✗ Um CBO baixo, isoladamente, já garante que a qualidade de cada
  dependência restante é saudável — falso: CBO é uma métrica de
  contagem, não de qualidade; uma única dependência de Conteúdo (a
  pior) ainda é pior que três dependências de Dados (a ideal).

## A Escala de Myers

O Acoplamento de Estampa ocupa o meio da escala porque evita os dois
piores pecados — não altera o estado interno de outra classe (Conteúdo)
e não depende de algo global/oculto e difícil de testar (Comum) — mas
ainda comete um erro estrutural: o receptor passa a "conhecer" mais do
objeto do que realmente precisa, herdando uma dependência transitiva
inteira só para usar uma fração dela. No exemplo de `NotificacaoEmail`,
bastava o endereço de e-mail, mas a classe acabou acoplada ao formato
inteiro de `Cliente` — renomear `Cliente` para `Usuario` já quebra o
código, mesmo que a lógica de envio de e-mail não tenha mudado nada.
Só o Acoplamento de Dados, o nível ideal, elimina esse excesso: extrai
o dado estritamente necessário *antes* de passá-lo para a frente,
tornando o serviço reutilizável por qualquer chamador, não só por
`Cliente`.

- ✔ O Acoplamento de Conteúdo, o pior nível, ocorre quando uma classe
  modifica diretamente atributos de outra — é a definição do "pecado
  original" da Escala de Myers.
- ✗ O Acoplamento Comum via métodos estáticos é fácil de testar, pois
  não exige instanciar objetos — pelo contrário: é o mais difícil de
  testar, porque a dependência estática fica "enterrada" no corpo do
  método, invisível na assinatura, e não pode ser substituída por um
  mock sem alterar o próprio código de produção.
- ✔ O Acoplamento de Estampa cria dependências transitivas: quem
  recebe o objeto herda tudo que ele conhece — é exatamente o risco
  central deste nível, ilustrado por `NotificacaoEmail` recebendo
  `Cliente` inteiro só para ler o e-mail.
- ✔ O Acoplamento de Dados é o nível ideal, pois módulos comunicam-se
  só com o estritamente necessário — é a definição do nível ideal, e o
  objetivo prático de qualquer refatoração de acoplamento.

## Inversão de Dependência

Antes do DIP, a seta de dependência apontava de cima para baixo:
`Cliente` (módulo de alto nível, regra de negócio) conhecia e dependia
diretamente de `Cartao` (módulo de baixo nível, detalhe técnico).
Qualquer mudança em `Cartao`, ou a chegada de um novo meio de
pagamento, forçava reabrir e recompilar `Cliente` — o "pesadelo da
expansão" do `if/else` em cadeia, uma violação do Princípio
Aberto/Fechado. O DIP inverte essa seta: em vez de `Cliente` depender
de `Cartao`, os dois passam a depender de uma abstração comum
(`Pagavel`). Depois da inversão, é `Cartao` (e `Pix`, e qualquer meio
de pagamento futuro) que precisa se adaptar ao contrato imposto por
`Cliente` — o alto nível deixa de "olhar para baixo" pedindo serviços
a uma implementação concreta e passa a "impor uma regra" que as
implementações concretas obedecem. Esse é o "Muro de Fronteira":
`Cliente` permanece intocado mesmo quando surge um novo meio de
pagamento (Pix, criptomoeda, o que for), porque ele nunca conheceu
nenhum deles — só conhece o contrato.

- ✔ No DIP, tanto o módulo de alto nível quanto o de baixo nível devem
  depender de uma abstração comum — é a essência do princípio: nenhum
  dos dois lados depende do outro diretamente, ambos dependem de
  `Pagavel`.
- ✔ Antes do DIP, `Cliente` (alto nível) dependia diretamente de
  `Cartao` (baixo nível) — é o problema de design descrito no início
  do bloco, a origem do "pesadelo da expansão".
- ✗ Depois do DIP, é `Cliente` que precisa se adaptar às mudanças em
  `Cartao` e `Pix` — é exatamente o oposto: depois da inversão, são
  `Cartao` e `Pix` que precisam se adaptar ao contrato imposto por
  `Cliente`; é essa troca de direção que dá nome ao princípio.
- ✔ A cadeia de `if/else` para escolher entre `Cartao`, `Pix` e
  `Boleto` é um sintoma de violação do Princípio Aberto/Fechado — cada
  novo meio de pagamento exige reabrir e recompilar `Cliente`, o
  oposto de "aberto para extensão, fechado para modificação".
