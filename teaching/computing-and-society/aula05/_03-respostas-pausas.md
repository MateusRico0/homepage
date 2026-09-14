# Respostas das Pausas Ativas — Aula 5

> Arquivo não publicado (`_03-respostas-pausas.md`) — nunca deve ser
> incluído no `index.qmd`. As notas em HTML publicadas contêm só a
> pergunta provocadora e o V/F sem resolução; os slides RevealJS
> mostram o V/F resolvido (✔/✗), mas sem a discussão longa abaixo.

---

## Pausa 1 (Bloco 1 — Abertura): O que o clique no botão não conta

**Discussão da pergunta provocadora:** Um clique é uma ação de
curtíssimo prazo — não diz nada, sozinho, sobre se o usuário realmente
queria o que acabou de fazer, nem se ficará satisfeito depois. A
métrica "cliques no botão" é, na melhor das hipóteses, um substituto
(*proxy*) da intenção real do usuário (assinar e permanecer assinante),
nunca a intenção em si. Um clique confuso ou impulsivo conta exatamente
igual a um clique deliberado nessa métrica — por isso ela pode "vender"
uma vitória que, medida de outro jeito (permanência depois de 90 dias,
por exemplo), se revelaria uma derrota. É exatamente esse ponto cego
que os Blocos 2 e 3 desenvolvem: pesquisa qualitativa entende a
intenção por trás do clique; teste A/B bem desenhado mede o resultado
além do clique imediato.

**V/F — resolução:**

- ✔ Se a métrica de sucesso fosse redefinida de "cliques no botão" para
  "assinaturas que seguem ativas 90 dias depois", uma mudança de cor
  que só confunde o usuário deixaria de parecer uma vitória.
  **Verdadeiro** — trocar a métrica para algo que captura permanência,
  não só o clique, expõe justamente esse tipo de "vitória" falsa: um
  clique confuso não se converte em assinatura ativa 90 dias depois.
- ✗ No limite em que todo usuário que clica de fato queria assinar e
  permanece assinante indefinidamente, a métrica de clique deixaria de
  ter qualquer risco de enganar. **Falso** — mesmo nesse cenário ideal
  hipotético, a métrica de clique continuaria sendo, na melhor das
  hipóteses, um substituto imperfeito da intenção real; o risco de erro
  cairia a zero *nesse caso específico*, mas isso não muda a natureza
  da métrica como proxy — o item generaliza demais ao afirmar que o
  "risco" desaparece como propriedade da métrica em si.
- ✔ A mesma lógica se aplicaria a um aplicativo de namoro que mede
  sucesso só por conversas iniciadas, sem medir se levam a encontros
  reais. **Verdadeiro** — mesma estrutura: uma métrica de ação imediata
  pode não capturar o objetivo real que ela deveria representar.
- ✗ Como a taxa de cliques subiu 8% de forma mensurável, isso já prova
  que o design é objetivamente melhor para o usuário. **Falso** — um
  aumento de cliques mede só o clique; não diz nada, sozinho, sobre se
  o resultado serviu ao interesse do usuário.

---

## Pausa 2 (Bloco 2 — Kit Qualitativo): Por que observar bate perguntar, às vezes

**Discussão da pergunta provocadora:** Um hábito automático — como um
gesto de rolagem rápido que faz alguém pular um campo obrigatório sem
perceber — não é algo que a própria pessoa costuma saber narrar numa
entrevista, precisamente porque ela nunca precisou explicar esse gesto
para ninguém; ele é tácito. Observar o preenchimento ao vivo captura
esse gesto no momento em que ele acontece, sem depender da capacidade
(ou disposição) do usuário de reconstruir e verbalizar, depois do
fato, algo que fez de forma quase automática. Isso não torna a
entrevista inútil — ela continua sendo o caminho mais direto para o
que o usuário consegue e quer articular conscientemente —, mas explica
por que a investigação contextual revela uma categoria de informação
que a entrevista, estruturalmente, tende a perder.

**V/F — resolução:**

- ✔ Se o motivo do abandono fosse um hábito automático (rolagem rápida
  pulando um campo), uma entrevista teria menos chance de revelar esse
  motivo do que observar o preenchimento ao vivo. **Verdadeiro** — um
  hábito automático e não-verbalizado é exatamente o tipo de coisa que
  a investigação contextual revela e a entrevista, dependente de
  relato consciente, tende a perder.
- ✔ No limite em que o usuário tivesse consciência perfeita e memória
  exata de cada micro-decisão, a vantagem da investigação contextual
  sobre a entrevista deixaria de existir nesse caso. **Verdadeiro** —
  sem lacuna entre o que a pessoa faz e o que ela sabe descrever, a
  vantagem específica da observação (revelar o tácito) não teria mais
  o que revelar de diferente.
- ✔ A mesma lógica se aplicaria a uma equipe de suporte técnico que
  observa operadores de caixa em vez de só entrevistá-los depois do
  expediente. **Verdadeiro** — mesma lógica de investigação
  contextual, aplicada a outro domínio de sistema (ponto de venda em
  vez de cadastro web).
- ✗ Como a investigação contextual revela o tácito que a entrevista não
  revela, entrevistas deveriam ser abandonadas sempre que a
  investigação contextual for viável. **Falso** — as duas técnicas
  revelam coisas diferentes (o dito vs. o tácito); a lição é usar a
  técnica certa para a pergunta certa, não abandonar uma em favor da
  outra.

---

## Pausa 3 (Bloco 3 — Teste A/B): Um teste A/B com só uma semana de dados

**Discussão da pergunta provocadora:** A decisão da equipe ignora a
armadilha do **efeito novidade**: um ganho de métrica observado logo
depois de uma mudança pode refletir só a curiosidade dos usuários pela
interface nova, não um valor real e duradouro. A equipe deveria ter
estendido a janela de observação — rodando o teste por mais tempo (ou,
pelo menos, monitorando a métrica após o lançamento completo) — para
verificar se o ganho de 15% persiste depois que a novidade deixa de ser
novidade. Significância estatística, sozinha, só garante que o efeito
medido *naquela janela específica* provavelmente não é ruído aleatório;
não garante que o efeito é duradouro, nem que ele reflete valor real
entregue ao usuário.

**V/F — resolução:**

- ✔ Se a equipe rodasse o mesmo teste por oito semanas e o ganho de 15%
  persistisse igual em todas elas, isso reduziria (mas não eliminaria)
  a chance de ser só efeito novidade. **Verdadeiro** — persistência do
  efeito ao longo de mais semanas é evidência (não prova definitiva)
  contra a hipótese de que é só novidade passageira.
- ✔ No limite em que um teste rodasse indefinidamente, sem nunca ser
  encerrado, o conceito de efeito novidade deixaria de ter sentido
  prático a ser medido. **Verdadeiro** — sem um "antes" (novidade) e um
  "depois" (habituação) para comparar, a própria ideia de efeito
  novidade perde onde se aplicar.
- ✔ A mesma lógica se aplicaria a um jogo para celular que vê partidas
  diárias subirem na primeira semana após uma nova mecânica, sem saber
  se isso se mantém no mês seguinte. **Verdadeiro** — mesma estrutura:
  ganho de curto prazo que ainda precisa ser checado contra
  persistência de médio prazo.
- ✗ Como o tempo de sessão subiu 15% de forma estatisticamente
  mensurável em sete dias, isso já garante que o design serve
  genuinamente ao usuário. **Falso** — um aumento estatisticamente
  significativo em sete dias não descarta efeito novidade nem os
  outros problemas de validade; significância estatística diz que o
  efeito é real *na janela medida*, não que é duradouro ou que serve ao
  usuário.

---

## Pausa 4 (Bloco 4 — Captologia): Persuadir é sempre manipular?

**Discussão da pergunta provocadora:** Sim, pela definição de Fogg, o
aplicativo de exercícios é tecnologia persuasiva — ele é desenhado
deliberadamente para mudar um comportamento (a rotina de exercícios) do
usuário, usando persistência (notificações) e dados pessoais
(histórico de treino). Mas isso, sozinho, não o torna antiético: Fogg é
explícito em dizer que o veredito depende de *como* a persuasão é
usada, não da mera presença da intenção persuasiva ou das vantagens
estruturais do computador. Um aplicativo que usa as mesmas ferramentas
(persistência, dados, interface pensada) para incentivar um hábito
genuinamente benéfico ao próprio usuário está do lado "entender e
apoiar"; o mesmo kit, usado para empurrar uma compra enganosa,
estaria do lado "manipular".

**V/F — resolução:**

- ✗ Se o mesmo app usasse notificações para empurrar, de forma
  enganosa, uma compra desnecessária, a definição de tecnologia
  persuasiva deixaria de se aplicar a ele. **Falso** — a definição de
  Fogg é sobre a *intenção de mudar atitude/comportamento*, não sobre
  se o uso é ético ou enganoso; o app continuaria sendo tecnologia
  persuasiva, só que antiética nesse uso específico.
- ✔ No limite em que um sistema nunca tivesse intenção de mudar
  atitude/comportamento de ninguém, ele deixaria de se enquadrar na
  definição de tecnologia persuasiva. **Verdadeiro** — sem nenhuma
  intenção de influenciar, falta exatamente o elemento central da
  definição de Fogg (sistema *desenhado* para mudar atitudes ou
  comportamentos).
- ✔ A mesma lógica se aplicaria a um aplicativo de meditação que usa
  lembretes diários para incentivar uma prática regular de bem-estar.
  **Verdadeiro** — mesma estrutura de tecnologia persuasiva
  (persistência, lembretes) aplicada a um objetivo diferente, ainda
  dentro do espírito de "mudar comportamento a favor do próprio
  usuário".
- ✗ Como Fogg lista seis vantagens dos computadores sobre persuasores
  humanos, qualquer app que use uma delas é, por definição, antiético.
  **Falso** — Fogg é explícito: a resposta depende de como a persuasão
  é usada, não da mera presença de vantagens estruturais
  (persistência, anonimato, escala) sobre persuasores humanos.

---

## Pausa 5 (Bloco 5 — Caso Kramer et al.): Termos de Uso bastam como consentimento?

**Discussão da pergunta provocadora:** O argumento de que a
concordância com os Termos de Uso já constitui consentimento informado
elimina exatamente os dois elementos que caracterizam o consentimento
informado no padrão acadêmico (IRB): **especificidade** (saber, antes
de participar, qual experimento concreto vai acontecer) e
**possibilidade real de recusa** (poder dizer não sem custo
desproporcional, como deixar de usar o serviço inteiro). Um documento
genérico, aceito uma vez, anos antes, para poder criar uma conta, não
tem como descrever um experimento futuro ainda não concebido no
momento da aceitação — e recusar-se a "participar" de um experimento
futuro qualquer normalmente significaria deixar de usar o serviço por
completo, o que não é uma opção de recusa real e proporcional.

**V/F — resolução:**

- ✔ Se o Facebook tivesse notificado individualmente cada participante,
  com opção real de recusar sem deixar de usar a rede, o argumento de
  "consentimento via Termos de Uso" deixaria de ser necessário.
  **Verdadeiro** — notificação específica e opção real de recusa são
  exatamente os dois elementos que faltam no argumento original;
  supridos, o argumento alternativo (Termos de Uso genéricos) deixa de
  ser necessário.
- ✗ No limite em que um usuário lesse e compreendesse cada palavra dos
  Termos de Uso antes de aceitá-los, o problema de especificidade do
  consentimento desapareceria por completo. **Falso** — compreender
  integralmente um documento genérico não resolve o problema de
  especificidade: o documento, por definição, não descreve um
  experimento futuro específico ainda não concebido no momento em que
  foi aceito.
- ✔ A mesma lógica se aplicaria a um aplicativo de e-commerce que testa
  algoritmos de precificação dinâmica amparado só nos Termos de Uso
  gerais, sem aviso individual. **Verdadeiro** — mesma estrutura:
  Termos de Uso genéricos usados para amparar uma manipulação
  experimental específica não anunciada individualmente.
- ✗ Como os usuários já haviam consentido em gerar os dados usados no
  experimento, isso significa que qualquer manipulação futura desses
  dados está automaticamente coberta. **Falso** — consentimento para
  gerar/usar dados em um serviço não é o mesmo que consentimento para
  ser sujeito de qualquer experimento futuro sobre esses dados; a aula
  distingue exatamente esses dois níveis de consentimento.

---

## Pausa 6 (Bloco 6 — Síntese): Lendo a instrumentação de um app real

**Discussão da pergunta provocadora:** O exercício pede para aplicar o
checklist da síntese (que métrica, a favor de quem, o usuário sabe,
existe saída simétrica) a um caso pessoal e concreto — não há uma
resposta fixa correta, mas o padrão comum é notar que elementos como
notificações, contadores de sequência (*streaks*) e reprodução
automática costumam estar alinhados a métricas de engajamento
(tempo de uso, retorno diário) que podem, ou não, coincidir com o
benefício real do usuário. O ponto pedagógico central é o exercício de
leitura crítica em si: perguntar explicitamente "que métrica isso
parece mover" é o primeiro passo para distinguir instrumentação que
entende de instrumentação que direciona.

**V/F — resolução:**

- ✔ Se um app de streaming medisse sucesso só por "episódios
  reproduzidos automaticamente", isso favoreceria uma métrica mais
  fácil de manipular por autoplay do que por escolha deliberada.
  **Verdadeiro** — "episódios reproduzidos automaticamente" é uma
  métrica vulnerável a autoplay, contando continuidade passiva como se
  fosse escolha ativa do usuário.
- ✔ No limite em que a métrica de negócio coincidisse perfeitamente com
  o benefício real do usuário, a pergunta "a métrica representa o
  usuário ou o negócio?" deixaria de separar os dois casos.
  **Verdadeiro** — sem divergência possível entre métrica de negócio e
  benefício do usuário, essa pergunta específica do checklist perde a
  função de distinguir os dois casos.
- ✔ A mesma lógica se aplicaria a uma plataforma de cursos online que
  mede sucesso pela conclusão de módulos, em vez de pela aplicação real
  do conteúdo. **Verdadeiro** — mesma lógica: uma métrica de conclusão
  pode divergir do objetivo real (aplicação prática do conteúdo),
  revelando a favor de quem o sistema foi otimizado.
- ✗ Como o checklist lista quatro perguntas concretas, qualquer app que
  passe nas quatro está, por definição, isento de qualquer viés a favor
  do negócio. **Falso** — o checklist orienta a leitura crítica de uma
  instrumentação; passar nas quatro perguntas reduz a suspeita de viés,
  mas não é prova formal de isenção total — julgamento caso a caso
  continua necessário.

---

## Pausa 7 (Bloco 7 — Fechamento): O que mais custa, sem ninguém decidir explicitamente?

**Discussão da pergunta provocadora:** Vários candidatos plausíveis:
onde um serviço armazena os dados dos usuários (com implicação de
custo energético e de latência, tema da Aula 6); quantos
microsserviços um sistema usa e onde cada um roda (mais serviços
geralmente significam mais infraestrutura rodando, mesmo sem nenhuma
decisão explícita de "gastar mais energia"); por quanto tempo dados
ficam retidos "só por garantia", sem necessidade concreta. Em todos os
casos, o padrão é o mesmo desta aula: uma escolha que parece "só de
engenharia" ou "só de processo" deixa uma marca concreta e mensurável
em um domínio que ninguém precisou decidir explicitamente afetar.

**V/F — resolução:**

- ✔ Se a métrica de sucesso de um streaming fosse "satisfação declarada
  pós-uso" em vez de "horas assistidas", o incentivo para autoplay
  agressivo tenderia a enfraquecer. **Verdadeiro** — trocar a métrica
  para satisfação declarada remove parte do incentivo estrutural que
  hoje empurra para autoplay agressivo como proxy de sucesso.
- ✔ No limite em que um teste A/B pudesse ser replicado infinitas
  vezes sem custo de tempo ou de usuários reais, o problema de
  tamanho de amostra/poder estatístico deixaria de ser uma preocupação
  prática. **Verdadeiro** — sem nenhum custo de replicação, o problema
  prático de amostra pequena desaparece (mesmo que o princípio
  estatístico continue existindo em teoria).
- ✔ A mesma lógica se estenderia ao argumento da Aula 6 de que decisões
  de arquitetura têm consequência material e ambiental.
  **Verdadeiro** — é exatamente a ponte para a Aula 6: escolha de
  engenharia com consequência real fora do domínio "óbvio" dela.
- ✗ Como o mesmo kit pode entender ou manipular o usuário, toda
  pesquisa de usuário e todo teste A/B deveriam ser abandonados.
  **Falso** — a aula não conclui que o kit deve ser abandonado; conclui
  que a métrica e a transparência escolhidas é que decidem o uso —
  abandonar a ferramenta descartaria também seu uso legítimo.
