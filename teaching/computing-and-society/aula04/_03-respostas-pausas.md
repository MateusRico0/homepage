# Respostas das Pausas Ativas — Aula 4

> Arquivo não publicado (`_03-respostas-pausas.md`) — nunca deve ser
> incluído no `index.qmd`. As notas em HTML publicadas contêm só a
> pergunta provocadora e o V/F sem resolução; os slides RevealJS
> mostram o V/F resolvido (✔/✗), mas sem a discussão longa abaixo.

---

## Pausa 1 (Bloco 1 — Abertura): Cinco pessoas, cinco fases: coincidência?

**Discussão da pergunta provocadora:** Não é coincidência. O número de
fases do compilador (5 para COBOL, 3 para ALGOL) resultou diretamente
do número de pessoas alocadas a cada subtarefa (5 e 3) — não de
nenhuma exigência técnica externa. O mecanismo: dentro de cada
subequipe, a comunicação é mais fácil (mesma sala, mesmo contexto
diário); entre subequipes, mais cara. Ao dividir o trabalho de
construção em fases, cada subequipe tende a criar fronteiras de fase
que correspondem às fronteiras de comunicação que já tem internamente —
e o número "natural" de fronteiras internas de uma equipe de N pessoas
tende a corresponder, grosso modo, ao número de subgrupos de
comunicação que a própria equipe forma. Esse é exatamente o fenômeno
que o Bloco 3 formaliza como Lei de Conway.

**V/F — resolução:**

- ✗ Se a organização tivesse alocado quatro pessoas para cada
  compilador, o número de fases ainda teria sido determinado apenas
  pela dificuldade técnica intrínseca de cada linguagem. **Falso** — o
  próprio exemplo mostra o oposto: foi a divisão de pessoas (5 e 3),
  não a dificuldade técnica isolada, que se refletiu no número de
  fases.
- ✔ Com uma única pessoa construindo os dois compiladores, o fenômeno
  deixaria de se manifestar da mesma forma. **Verdadeiro** — sem
  subdivisão em subequipes, não há fronteira de comunicação interna
  para o software copiar.
- ✔ O mesmo padrão se aplicaria a duas squads de e-commerce (carrinho e
  checkout). **Verdadeiro** — é a mesma lógica estrutural, transposta
  para outro domínio, mesmo sem intenção deliberada de arquitetar
  assim.
- ✗ Os exemplos militares provam que a estrutura organizacional sempre
  produz sistemas de pior qualidade. **Falso** — o artigo fala de
  correspondência estrutural (a arquitetura copia o organograma), não
  de qualidade superior ou inferior; são dimensões diferentes.

---

## Pausa 2 (Bloco 2 — Mapa de Papéis): O jogo do telefone dos requisitos

**Discussão da pergunta provocadora:** Não se deveria esperar a mesma
resposta de todos — e nenhuma delas é "a certa" isoladamente. Cada
papel (PM, UX, dev, QA, SRE) enxerga uma parte real e legítima do
problema, mas nenhum enxerga o quadro completo. O PM vê prioridade de
negócio; o UX vê fluxo de interação; o QA vê casos-limite; o SRE vê
comportamento sob carga. A "resposta certa" sobre o que o usuário quer
não existe como um dado único a ser extraído — ela é reconstruída, de
forma incompleta, a cada tradução. Isso não é motivo para desistir do
processo, mas para reconhecer explicitamente onde a informação se perde
e criar mecanismos (ex.: voltar a checar com o usuário original em
pontos-chave) para mitigar isso.

**V/F — resolução:**

- ✗ Um único generalista acumulando todos os papéis eliminaria por
  completo o risco de perda de informação entre etapas. **Falso** — o
  risco de perda por tradução diminui, mas não desaparece: um único
  ponto de decisão traz seu próprio viés e limite de capacidade,
  trocando um tipo de risco por outro.
- ✔ No limite de uma única etapa entre usuário e código (zero
  intermediários), a lógica de tradução deixaria de se aplicar.
  **Verdadeiro** — sem etapas intermediárias, não há mais tradução
  ocorrendo, e portanto o mecanismo de perda/adição de informação por
  tradução não tem onde atuar.
- ✔ A mesma lógica se aplicaria a uma cadeia de atendimento médico
  (paciente → recepção → enfermeiro → médico). **Verdadeiro** — é a
  mesma estrutura de tradução em cadeia, em outro domínio.
- ✗ Logo, sistemas deveriam sempre minimizar o número de papéis
  envolvidos, sem exceção. **Falso** — cada papel especializado também
  agrega expertise que um generalista não teria; a lição é sobre o
  custo real da tradução, não uma recomendação de eliminá-la a
  qualquer custo.

---

## Pausa 3 (Bloco 3 — Lei de Conway): Consertar código, ou organograma?

**Discussão da pergunta provocadora:** Reescrever só o código, sem
tocar na organização das equipes, tende a ser uma solução temporária.
A pressão estrutural descrita pela Lei de Conway (premissa b: minimizar
custo de comunicação alinhando equipes a módulos) continua atuando
depois da reescrita — se as mesmas pessoas continuam precisando se
comunicar com a mesma frequência, ao longo do tempo a arquitetura tende
a "voltar" a espelhar o organograma antigo, por meio de pequenas
decisões técnicas sucessivas que, individualmente, parecem razoáveis,
mas que no agregado recriam a fronteira antiga. Por isso a "Manobra
Inversa de Conway" propõe mudar primeiro (ou junto) a estrutura das
equipes.

**V/F — resolução:**

- ✔ Se comunicação fosse grátis e instantânea (premissa b removida), a
  pressão de espelhamento desapareceria, mesmo que os módulos ainda
  precisassem trocar informação. **Verdadeiro** — a premissa (a)
  (necessidade de comunicação) sozinha não gera a pressão de
  espelhamento; é a combinação com a premissa (b) (minimizar custo de
  comunicação) que a gera. Sem custo de comunicação, não há pressão
  para alinhar equipes a módulos.
- ✔ Com uma única equipe indivisa construindo tudo, a Lei de Conway
  deixaria de fazer qualquer previsão sobre a arquitetura. **Verdadeiro**
  — sem subdivisão, não há organograma interno a ser espelhado.
- ✗ A Manobra Inversa bastaria ser aplicada só reescrevendo código em
  módulos separados, sem alterar a estrutura das equipes. **Falso** — é
  exatamente o oposto do que a manobra propõe: mudar a estrutura do
  time é o passo-chave, não uma opção descartável.
- ✗ Uma organização bem comunicada entre todas as equipes produzirá
  necessariamente uma arquitetura tecnicamente superior. **Falso** — a
  lei prevê correspondência estrutural entre comunicação e arquitetura,
  não superioridade técnica; comunicação e qualidade técnica são
  dimensões diferentes.

---

## Pausa 4 (Bloco 4 — Requisitos como Processo Social): Quem é "o usuário", de fato?

**Discussão da pergunta provocadora:** "O usuário" entrevistado numa
elicitação de requisitos tende a ser quem já tem acesso ao processo:
quem tem tempo livre para responder pesquisas, quem fala o idioma da
equipe, quem sabe usar os canais formais de contato (formulário,
e-mail, atendimento). Grupos sem esse acesso — por barreira de idioma,
de letramento digital, de tempo, ou simplesmente por não serem
considerados "o público-alvo" — tendem a ficar de fora, mesmo quando
são diretamente afetados pelo sistema. O caso do DGEI é o exemplo mais
extremo: a comunidade afetada tinha o conhecimento (viveu o problema),
mas não tinha acesso ao processo formal de registro — por isso precisou
criar seu próprio "requisito" (o mapa) por fora do canal institucional.

**V/F — resolução:**

- ✔ Com poder de voz igual na negociação, a lista final ainda poderia
  refletir quem já detém mais poder, se a coleta inicial não mudasse.
  **Verdadeiro** — a assimetria pode entrar antes mesmo da negociação,
  já na seleção de quem é convidado a participar como "usuário".
  Igualar o poder de voz na mesa não corrige quem nunca chegou à mesa.
- ✔ Se instituições mantivessem registro completo e preciso, a prática
  de contra-dados do DGEI perderia sua função motivadora específica.
  **Verdadeiro** — a motivação relatada no caso era exatamente a
  ausência desse registro; removendo a causa, a motivação específica
  desaparece (embora outras razões para produção de dados comunitários
  possam existir).
- ✔ A mesma lógica do DGEI se aplicaria a um backlog de bugs baseado só
  em tickets de usuários que sabem preencher um formulário técnico.
  **Verdadeiro** — mesmo mecanismo de exclusão por barreira de acesso
  ao canal formal de report.
- ✗ Logo, toda coleta institucional deveria ser abandonada em favor
  exclusivo de contra-dados comunitários. **Falso** — Data Feminism
  propõe quatro pontos de partida complementares (Coletar, Analisar,
  Imaginar, Ensinar); não defende o abandono da coleta institucional,
  mas sua complementação crítica.

---

## Pausa 5 (Bloco 5 — Dark Patterns): Quem decide o quanto de fricção você sente?

**Discussão da pergunta provocadora:** A diferença de fricção entre
inscrever-se (1–2 cliques) e cancelar (múltiplas telas, várias opções)
não é limitação técnica — a mesma equipe capaz de construir o primeiro
fluxo é, tecnicamente, capaz de construir o segundo com a mesma
simplicidade. O que muda entre os dois fluxos é a métrica que a equipe
de produto escolheu otimizar: se o sucesso do fluxo de cancelamento é
medido por "quantos usuários desistem no meio do caminho" (uma métrica
de retenção), o incentivo estrutural aponta para mais fricção, não
menos. Voltando à tabela de papéis do Bloco 2: é o papel de
"Stakeholder de negócio" que tem o poder de vetar/alterar um fluxo "por
razões que nada têm a ver com o usuário" — aqui, esse poder abstrato
ganha um mecanismo concreto e um nome (Obstrução).

**V/F — resolução:**

- ✔ Se a métrica interna fosse "tempo até a resolução do pedido do
  usuário" em vez de "taxa de retenção mensal", o incentivo estrutural
  para alongar o fluxo desapareceria. **Verdadeiro** — é a mesma lógica
  de todo o bloco: a métrica otimizada determina o incentivo estrutural
  sobre o design do fluxo.
- ✗ Toda tela de confirmação antes de cancelar é, por definição, um
  exemplo de Obstrução. **Falso** — uma confirmação isolada pode ser
  proteção legítima contra erro do usuário; o que caracteriza o padrão
  é a assimetria deliberada entre os dois fluxos (inscrição vs.
  cancelamento), não a mera existência de uma etapa de confirmação.
- ✔ A mesma lógica se aplicaria a um contrato de aluguel com assinatura
  digital instantânea, mas rescisão só por carta registrada em
  cartório. **Verdadeiro** — mesma estrutura de assimetria entre entrar
  e sair, em outro domínio contratual.
- ✗ Como o caso da FTC terminou em acordo bilionário, toda decisão de
  design que aumenta retenção é necessariamente um dark pattern ilegal.
  **Falso** — o caso girou em torno de engano e obstrução deliberada
  documentados, não da otimização de retenção em si; um produto que
  retém usuários por ser genuinamente melhor não configura o padrão.

---

## Pausa 6 (Bloco 6 — Artefato Concreto): O que faltou entre a reunião e o código?

**Discussão da pergunta provocadora:** Faltaram, no mínimo, dois passos
concretos entre a intenção declarada em reunião e a proteção real do
sistema: (1) transformar "acessível a baixa visão" num Requisito
Não-Funcional testável (ex.: contraste mínimo mensurável), o que dá um
critério objetivo de sucesso/fracasso; e (2) um gate de CI que
verifique automaticamente esse critério a cada mudança, bloqueando
deploys que o violem. Uma decisão de reunião, sozinha, é só intenção;
mesmo documentada como uma ADR, ela preserva o raciocínio da decisão
original, mas não impede, por si só, que uma mudança futura a quebre —
só um mecanismo automatizado no processo faz isso.

**V/F — resolução:**

- ✗ Uma ADR sozinha, sem NFR testável antes, já bastaria para construir
  automaticamente um gate de CI que impeça regressão. **Falso** — um
  gate automatizado precisa de um critério mensurável de
  aprovação/reprovação, que é justamente o que o NFR testável fornece;
  a ADR documenta a decisão e seu raciocínio, mas não substitui esse
  critério.
- ✗ Um gate de CI com critério tão frouxo que qualquer código passa
  ainda cumpriria a função de "impedir regressão". **Falso** — um
  critério que nunca bloqueia nada não protege o compromisso na
  prática, mesmo existindo formalmente como "gate".
- ✔ A mesma cadeia (compromisso → NFR → ADR → gate) se aplicaria a
  reduzir viés discriminatório num sistema de contratação. **Verdadeiro**
  — mesma estrutura de tradução, aplicada a um compromisso diferente.
- ✗ Como um NFR testável é mensurável, todo compromisso ético não
  perfeitamente quantificável deve ser descartado como requisito.
  **Falso** — a tradução em NFR é uma simplificação parcial do valor,
  não uma exigência de quantificação perfeita; por isso o VSD é
  iterativo, revisitando o requisito quando necessário.

---

## Pausa 7 (Bloco 7 — Fechamento): O que mais deixa marca sem ninguém decidir?

**Discussão da pergunta provocadora:** Vários candidatos plausíveis:
onde a equipe está localizada (fusos horários limitam janelas de
comunicação síncrona, o que pode empurrar a arquitetura para módulos
mais desacoplados, quase como uma versão geográfica da Lei de Conway);
como o orçamento é dividido entre times (um módulo com mais
investimento tende a receber mais atenção arquitetural, mesmo sem
nenhuma decisão técnica explícita nesse sentido); e a duração dos
ciclos de planejamento (sprints muito curtos podem empurrar decisões de
arquitetura para o que é mais rápido de entregar, não o que é mais
sustentável). Em todos os casos, o padrão é o mesmo desta aula: uma
decisão que parece "de gestão", não "de engenharia", deixa uma marca
concreta e previsível no sistema técnico final.

**V/F — resolução:**

- ✔ Se a elicitação fosse perfeitamente neutra (sem assimetria de
  poder), a conexão com Data Feminism apresentada hoje perderia sua
  motivação central. **Verdadeiro** — a conexão existe precisamente
  porque a elicitação carrega assimetria de poder; sem essa premissa, a
  conexão não teria razão de ser feita.
- ✔ Com um time responsável por cada módulo E por cada fronteira entre
  módulos, o problema de requisito "cair no buraco" deixaria de ocorrer
  pelo mecanismo discutido. **Verdadeiro** — dono explícito de cada
  fronteira é exatamente a condição que neutraliza esse mecanismo
  específico.
- ✔ A tese de hoje (processo → consequência técnica) se estende à Aula
  5 (arquitetura → consequência material/ambiental). **Verdadeiro** — é
  a ponte deliberada entre as duas aulas: em ambos os casos, uma
  escolha que parece "só de processo/design" tem efeito concreto fora
  do código em si.
- ✗ Logo, toda falha técnica deve ser explicada primariamente por
  causas organizacionais, nunca por erros técnicos comuns. **Falso** —
  a aula acrescenta uma lente sociotécnica adicional; não elimina
  explicações técnicas comuns (bugs, escolhas de algoritmo) como causas
  legítimas de falha.
