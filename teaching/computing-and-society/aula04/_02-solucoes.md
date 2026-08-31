# Soluções — Exercícios de V/F, Aula 4

> Arquivo não publicado (`_02-solucoes.md`) — nunca deve ser incluído no
> `index.qmd`. As questões ficam sem solução no material do aluno; este
> arquivo é só para conferência do professor.

---

## Papéis da indústria e a cadeia de tradução de um pedido do usuário — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Se uma organização substituísse toda a cadeia de papéis (PM, dev, QA, UX, SRE) por um único generalista responsável por tudo, a qualidade final do sistema aumentaria necessariamente, porque eliminaria qualquer perda de informação entre etapas.

**Resposta:** Falso

**Justificativa:** Concentrar todos os papéis numa única pessoa reduz o
número de traduções (e, portanto, algumas perdas de informação
específicas de tradução), mas troca isso por outro custo: a ausência de
expertise especializada (um generalista não tem o mesmo conhecimento
profundo de UX, de testes ou de operações que profissionais dedicados
teriam) e um único ponto de falha cognitivo (viés e limites de
capacidade de uma só pessoa, sem checagem cruzada). O erro é tratar "menos
tradução" como sinônimo automático de "melhor qualidade" — a aula
discute um trade-off, não uma dominância estrita.

---

## Papéis da indústria e a cadeia de tradução de um pedido do usuário — item (b)

**Heurística:** Limite

**Afirmação:** ✔ No limite em que um time de operações/SRE nunca é consultado antes do lançamento de uma funcionalidade, os requisitos de confiabilidade em produção (ex.: comportamento sob picos de tráfego) tendem a ser descobertos só depois do incidente, não antes dele.

**Resposta:** Verdadeiro

**Justificativa:** A tabela de papéis da aula atribui exatamente a
SRE/Operações a tradução de "requisitos de confiabilidade em produção".
Se esse papel nunca é consultado antes do lançamento, essa tradução
específica simplesmente não ocorre a tempo — o requisito de
confiabilidade só se manifesta quando o sistema já está em produção e
falha sob carga, ou seja, via incidente real, não via antecipação.

---

## Papéis da indústria e a cadeia de tradução de um pedido do usuário — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ A mesma lógica de "cada papel intermediário traduz e potencialmente distorce um pedido" se aplicaria a uma cadeia de aprovação de crédito bancário em que o gerente de agência resume o pedido do cliente para um analista de risco, que por sua vez resume para um comitê de crédito.

**Resposta:** Verdadeiro

**Justificativa:** O mecanismo discutido na aula — cada elo de uma
cadeia de comunicação vê e transmite apenas parte do quadro original —
não é específico de engenharia de software; é uma propriedade geral de
qualquer cadeia de tradução com múltiplos elos humanos, incluindo o
exemplo bancário proposto.

---

## Papéis da indústria e a cadeia de tradução de um pedido do usuário — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como um pedido "simples" do usuário passa por várias traduções antes de virar código, isso prova que usuários finais deveriam sempre ser excluídos do processo de definição técnica, já que sua visão inicial do problema é, por definição, imprecisa.

**Resposta:** Falso

**Justificativa:** A aula não argumenta que a visão do usuário deveria
ser excluída — pelo contrário, o problema apontado é que o usuário
tende a perder voz ao longo da cadeia de tradução. Concluir "excluir o
usuário" inverte a lição: o ponto é reconhecer e mitigar a perda de
informação entre etapas, não eliminar a fonte original do pedido.

---

## Lei de Conway — premissas — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se a premissa de que "organizações minimizam custo de comunicação alinhando equipes a subsistemas" fosse falsa para uma empresa específica (ela deliberadamente mantém equipes desalinhadas dos módulos, mesmo a um custo de comunicação maior), essa empresa poderia, em princípio, produzir uma arquitetura que não espelha seu organograma.

**Resposta:** Verdadeiro

**Justificativa:** A Lei de Conway depende das duas premissas juntas.
Removendo a premissa (b) — a pressão para minimizar custo de
comunicação alinhando equipes a módulos —, a força que empurra a
arquitetura a espelhar o organograma desaparece, mesmo que a premissa
(a) (necessidade de comunicação para construir uma interface) continue
valendo.

---

## Lei de Conway — premissas — item (b)

**Heurística:** Limite

**Afirmação:** ✔ No limite em que duas partes de um sistema não precisam trocar absolutamente nenhuma informação entre si para funcionar (interface totalmente independente), a premissa de que "construir uma interface exige comunicação entre quem constrói cada parte" deixa de impor qualquer restrição sobre como as equipes devem se organizar.

**Resposta:** Verdadeiro

**Justificativa:** A premissa (a) só gera pressão organizacional quando
existe, de fato, uma interface a ser negociada entre as duas partes. No
limite de independência total (zero troca de informação necessária), não
há interface para coordenar, e portanto a premissa não impõe restrição
nenhuma sobre a organização das equipes.

---

## Lei de Conway — premissas — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ A afirmação de Conway de que "não existe uma coisa como um grupo de design que seja ao mesmo tempo organizado e imparcial" se aplicaria a um comitê acadêmico dividido em subcomissões temáticas, no sentido de que a divisão em subcomissões já impede certas propostas interdisciplinares de serem seguidas com a mesma facilidade que propostas dentro do tema de uma única subcomissão.

**Resposta:** Verdadeiro

**Justificativa:** A tese de Conway é justamente que qualquer
organização de um grupo de design cria caminhos de comunicação
privilegiados para certas alternativas e barreiras para outras — a
divisão em subcomissões temáticas é exatamente esse tipo de estrutura,
que favorece propostas dentro de um tema e dificulta as que cruzam
fronteiras temáticas.

---

## Lei de Conway — premissas — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como a Lei de Conway é sobre comunicação organizacional, ela implica que empresas totalmente remotas, sem escritório físico compartilhado, estão estruturalmente imunes ao fenômeno, já que não há organograma físico a ser espelhado.

**Resposta:** Falso

**Justificativa:** A Lei de Conway trata da estrutura de comunicação —
quem se reporta a quem, quem participa de quais canais e reuniões — não
de proximidade física. Equipes remotas continuam tendo fronteiras de
comunicação (times, canais de chat, fusos horários de sobreposição) que
produzem a mesma pressão estrutural sobre a arquitetura.

---

## Lei de Conway — a Manobra Inversa — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se uma empresa reorganizasse suas equipes para espelhar a arquitetura de microsserviços desejada, mas nunca reescrevesse uma linha do código monolítico existente, a Manobra Inversa de Conway prevê que, ainda assim, alguma pressão estrutural em direção à arquitetura desejada teria sido criada.

**Resposta:** Verdadeiro

**Justificativa:** A manobra atua justamente sobre a premissa (b): ao
reorganizar as equipes primeiro, cria-se a pressão de comunicação que
tende a empurrar a arquitetura, ao longo do tempo, na direção desejada —
mesmo que nenhuma linha de código tenha sido tocada ainda no momento da
reorganização.

---

## Lei de Conway — a Manobra Inversa — item (b)

**Heurística:** Limite

**Afirmação:** ✗ No limite em que uma reorganização de equipe é revertida imediatamente após ser anunciada (dura um dia), o efeito estrutural da Manobra Inversa de Conway sobre a arquitetura tenderia a ser equivalente ao de uma reorganização que se mantém por anos.

**Resposta:** Falso

**Justificativa:** O mecanismo da manobra depende da pressão de
comunicação se acumular ao longo do tempo, moldando decisões técnicas
sucessivas. Uma reorganização que dura um dia não tem tempo de gerar
esse acúmulo de pressão — o efeito estrutural tende a ser próximo de
zero, não equivalente a uma reorganização de anos.

---

## Lei de Conway — a Manobra Inversa — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ A lógica da Manobra Inversa se aplicaria a uma universidade que quer estimular pesquisa interdisciplinar entre departamentos historicamente isolados: criar um programa/comitê formal que force comunicação regular entre pesquisadores de áreas diferentes, antes de esperar que os artigos produzidos sejam naturalmente interdisciplinares.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma lógica estrutural: mudar primeiro os
canais/estruturas de comunicação (aqui, entre departamentos
acadêmicos) para depois obter o resultado desejado (produção
interdisciplinar), em vez de esperar que o resultado surja
espontaneamente sem tocar na estrutura organizacional que o impede.

---

## Lei de Conway — a Manobra Inversa — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como a Manobra Inversa de Conway propõe mudar a estrutura do time para mudar a arquitetura, isso significa que mudanças de código feitas sem qualquer mudança organizacional são sempre inúteis para alterar a arquitetura de um sistema.

**Resposta:** Falso

**Justificativa:** A manobra argumenta que mudar a estrutura do time é
frequentemente **necessário para sustentar** uma mudança de arquitetura
no longo prazo, não que mudanças de código isoladas sejam sempre
inúteis — elas podem funcionar temporariamente ou parcialmente; o risco
é a pressão estrutural empurrar a arquitetura de volta ao formato
antigo com o tempo, não que a mudança de código não tenha efeito algum.

---

## O caso concreto do compilador e o organograma militar (Conway, 1968) — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se, no exemplo do compilador, a organização tivesse decidido alocar as oito pessoas por competência técnica individual (não por linguagem-alvo), sem formar dois subgrupos distintos, o resultado ainda seria necessariamente um compilador com exatamente cinco fases para COBOL e três para ALGOL.

**Resposta:** Falso

**Justificativa:** O ponto central do exemplo é que o número de fases
(5 e 3) resultou da divisão de pessoas em dois subgrupos de tamanhos
5 e 3. Uma alocação diferente (por competência individual, sem
subgrupos por linguagem) não geraria, pelo mesmo mecanismo, essa
correspondência específica de 5 e 3 fases — o resultado dependeria de
como as novas fronteiras de comunicação, se existirem, se formassem.

---

## O caso concreto do compilador e o organograma militar (Conway, 1968) — item (b)

**Heurística:** Limite

**Afirmação:** ✔ No limite em que as duas forças militares do segundo exemplo tivessem, na verdade, uma única cadeia de comando compartilhada desde o início (sem duplicação de organograma), o resultado descrito no artigo — "produziram uma cópia de seu organograma" — não teria correspondência para reproduzir, pois não haveria dois organogramas distintos.

**Resposta:** Verdadeiro

**Justificativa:** O fenômeno relatado depende de existirem dois
organogramas distintos a serem espelhados no sistema resultante. Se
desde o início houvesse uma única cadeia de comando compartilhada, não
haveria duplicação organizacional para o sistema "copiar" — o próprio
enunciado do fenômeno perde sua condição de aplicação.

---

## O caso concreto do compilador e o organograma militar (Conway, 1968) — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ O padrão do exemplo do compilador se aplicaria a uma faculdade que divide o desenvolvimento de um sistema acadêmico em dois subgrupos — um para o módulo de matrícula e outro para o módulo de notas — sem qualquer canal formal de comunicação entre eles.

**Resposta:** Verdadeiro

**Justificativa:** É uma aplicação direta do mesmo mecanismo: dois
subgrupos sem comunicação formal entre si tendem a produzir uma
interface malformada ou inconsistente entre os módulos de matrícula e
de notas, pela mesma lógica do exemplo do compilador COBOL/ALGOL.

---

## O caso concreto do compilador e o organograma militar (Conway, 1968) — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como o artigo de Conway é de 1968 e trata de compiladores e sistemas de armas, isso significa que sua tese não tem aplicação a equipes de desenvolvimento de software ágil e distribuído da atualidade, que usam metodologias muito diferentes das de 1968.

**Resposta:** Falso

**Justificativa:** A tese de Conway é sobre a relação estrutural entre
comunicação organizacional e arquitetura resultante — um mecanismo
independente da metodologia de desenvolvimento usada. É, inclusive, um
dos motivos pelos quais o artigo continua sendo citado décadas depois,
incluindo em discussões contemporâneas sobre microsserviços e squads
ágeis.

---

## Elicitação de requisitos como processo social — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se o processo clássico de Engenharia de Requisitos (elicitação, análise e negociação, especificação, validação) fosse conduzido exclusivamente com stakeholders de negócio, sem nenhum usuário final envolvido em nenhuma etapa, o resultado ainda poderia ser tecnicamente "completo" segundo as quatro etapas, mesmo sendo socialmente incompleto.

**Resposta:** Verdadeiro

**Justificativa:** As quatro etapas descrevem uma estrutura de processo,
não uma garantia de representatividade social. É possível executar
todas as quatro etapas de forma tecnicamente "completa" (documentos
produzidos, validação feita) sem que nenhum usuário final tenha
participado — exatamente o ponto que a reinterpretação da aula, à luz
de Data Feminism, chama atenção.

---

## Elicitação de requisitos como processo social — item (b)

**Heurística:** Limite

**Afirmação:** ✔ No limite em que a etapa de "validação" do processo de Engenharia de Requisitos é realizada apenas com os mesmos stakeholders que participaram da elicitação original, essa validação tenderia a confirmar os mesmos pontos cegos já presentes desde o início, em vez de corrigi-los.

**Resposta:** Verdadeiro

**Justificativa:** Se a validação usa exatamente o mesmo conjunto de
participantes da elicitação, ela não introduz nenhuma nova perspectiva
capaz de revelar o que ficou de fora — ela só confirma que a
especificação está de acordo com quem já havia sido consultado, sem
checar quem não foi.

---

## Elicitação de requisitos como processo social — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ A ideia de que a elicitação de requisitos é um processo social, não uma extração neutra, se aplicaria a uma pesquisa de satisfação de usuários feita apenas por e-mail, em um serviço cujos usuários mais vulneráveis têm menos acesso a e-mail do que os demais.

**Resposta:** Verdadeiro

**Justificativa:** É um caso direto do mesmo mecanismo: o canal de
coleta (e-mail) já filtra quem consegue participar, de forma
correlacionada com vulnerabilidade social — exatamente o tipo de
assimetria que a aula discute ao dizer que "quem é entrevistado como o
usuário" não é uma escolha neutra.

---

## Elicitação de requisitos como processo social — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como a etapa de "análise e negociação" do processo de Engenharia de Requisitos existe justamente para resolver conflitos entre requisitos, isso garante, por construção, que grupos sem poder de voz no processo terão seus requisitos igualmente representados nessa negociação.

**Resposta:** Falso

**Justificativa:** A etapa de negociação resolve conflitos entre
requisitos que **já chegaram à mesa** — ela não garante que todos os
grupos afetados tenham conseguido colocar seus requisitos nessa mesa
em primeiro lugar. A existência de uma etapa formal de negociação não
resolve a assimetria de acesso que ocorre antes dela, na elicitação.

---

## Data Feminism — os quatro pontos de partida — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se o ponto de partida "Imaginar" não existisse no *framework* de Data Feminism, e a ação ficasse restrita a "Coletar" e "Analisar", o texto ainda argumentaria que isso seria suficiente para alcançar a raiz da injustiça, e não só documentar resultados desiguais.

**Resposta:** Falso

**Justificativa:** A própria citação da aula diz explicitamente que
"não podemos focar apenas em resultados desiguais, porque, se assim
for, nunca chegaremos à causa raiz da injustiça" — essa é justamente a
função de "Imaginar". Sem esse ponto de partida, "Coletar" e "Analisar"
sozinhos documentariam desigualdade, mas não atacariam sua causa raiz.

---

## Data Feminism — os quatro pontos de partida — item (b)

**Heurística:** Limite

**Afirmação:** ✗ No limite em que uma equipe de dados só pratica "Analisar" (auditar algoritmos para provar resultados desiguais) e nunca pratica "Coletar", "Imaginar" ou "Ensinar", segundo a lógica dos quatro pontos de partida, essa equipe ainda estaria atacando a causa raiz da injustiça, não só demonstrando sua existência.

**Resposta:** Falso

**Justificativa:** Mesma lógica do item anterior, em sua forma extrema:
"Analisar" isoladamente demonstra a existência de resultados desiguais
(um passo necessário, mas não suficiente); atacar a causa raiz é
explicitamente a função atribuída a "Imaginar" no texto.

---

## Data Feminism — os quatro pontos de partida — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ O ponto de partida "Ensinar" — sobre quem são as pessoas que fazem ciência de dados — se aplicaria à composição de um time de desenvolvimento de um aplicativo de saúde voltado a gestantes, no sentido de que a ausência de qualquer mulher no time é relevante para a discussão, mesmo que o time tenha alta competência técnica.

**Resposta:** Verdadeiro

**Justificativa:** "Ensinar" trata explicitamente de quem são as
identidades das pessoas que fazem ciência de dados/constroem sistemas
— competência técnica não neutraliza a relevância de quem está, ou não,
representado num time que constrói algo para um público específico.

---

## Data Feminism — os quatro pontos de partida — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como os quatro pontos de partida de Data Feminism são apresentados como formas de "tomar ação", isso significa que qualquer um dos quatro, isoladamente, é sempre suficiente para resolver uma injustiça de dados, sem precisar dos outros três.

**Resposta:** Falso

**Justificativa:** O texto apresenta os quatro como pontos de partida
complementares, cada um atacando uma dimensão diferente do problema
(dado ausente, resultado desigual, causa raiz, composição de quem
produz dados) — não como alternativas isoladamente suficientes.

---

## O caso do DGEI e a lógica de contra-dados — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se as autoridades de Detroit já mantivessem, em 1971, um registro público e detalhado dos atropelamentos na rota Pointes-Downtown, a motivação central do DGEI para produzir seu próprio mapa — "Where Commuters Run Over Black Children" — deixaria de existir da forma descrita no caso.

**Resposta:** Verdadeiro

**Justificativa:** O próprio trecho citado diz que "ninguém mantinha
registros detalhados dessas mortes" — essa ausência específica é a
motivação central relatada no caso. Removendo a premissa (ausência de
registro oficial), a motivação relatada desaparece.

---

## O caso do DGEI e a lógica de contra-dados — item (b)

**Heurística:** Limite

**Afirmação:** ✔ No limite em que uma comunidade afetada por um problema não tem absolutamente nenhum meio de registrar ou comunicar sua própria experiência (nem mapas, nem relatos orais, nem qualquer forma de testemunho), a prática de produzir contra-dados, no sentido do caso DGEI, não teria como ocorrer.

**Resposta:** Verdadeiro

**Justificativa:** Contra-dados, no caso DGEI, foram construídos a
partir do conhecimento vivido e do testemunho da comunidade (ex.:
Gwendolyn Warren). No limite absoluto em que nenhum meio de registro ou
testemunho existisse, não haveria base nenhuma, nem informal, a partir
da qual produzir esse registro alternativo.

---

## O caso do DGEI e a lógica de contra-dados — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ A lógica de "compilar contra-dados diante da negligência institucional", do caso DGEI, se aplicaria a um grupo de trabalhadores de plataforma (ex.: entregadores) que cria sua própria planilha compartilhada de acidentes de trabalho, na ausência de qualquer registro oficial da empresa que os contrata.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma estrutura do caso DGEI, transposta para
outro domínio: uma comunidade afetada, sem acesso a um registro
institucional que deveria existir, cria seu próprio registro alternativo
como forma de tornar visível um problema real.

---

## O caso do DGEI e a lógica de contra-dados — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como Gwendolyn Warren afirma que "não conseguiam obter aquela informação" das autoridades, isso prova que toda ausência de dado institucional é sempre proposital, nunca resultado de limitação de recursos ou de outras causas não intencionais.

**Resposta:** Falso

**Justificativa:** O caso relatado não afirma, nem a aula argumenta,
que toda ausência de dado é deliberada — apenas que, nesse caso
específico, a ausência teve um efeito concreto de invisibilizar um
problema real. Generalizar "toda ausência é sempre proposital"
extrapola o que o caso, por si só, sustenta.

---

## O processo clássico de Engenharia de Requisitos (conhecimento consolidado) — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se a etapa de "especificação" produzisse um documento tecnicamente impecável, mas baseado em uma etapa de "elicitação" que ouviu apenas um subconjunto não representativo dos usuários, o documento de especificação ainda seria, no sentido usado nesta aula, um retrato fiel das necessidades de todos os usuários do sistema.

**Resposta:** Falso

**Justificativa:** A qualidade técnica da especificação (clareza,
consistência formal) não corrige um problema de representatividade
introduzido na etapa anterior — um documento pode ser tecnicamente
impecável e, ainda assim, não representar fielmente as necessidades de
quem não foi ouvido na elicitação.

---

## O processo clássico de Engenharia de Requisitos (conhecimento consolidado) — item (b)

**Heurística:** Limite

**Afirmação:** ✗ No limite em que as quatro etapas (elicitação, análise e negociação, especificação, validação) são executadas em sequência estritamente linear, sem nenhuma iteração ou retorno a uma etapa anterior, o processo ainda seria capaz de corrigir um requisito mal levantado na elicitação, caso ele só seja percebido como problemático durante a validação.

**Resposta:** Falso

**Justificativa:** Sem a possibilidade de retorno a uma etapa anterior,
um problema identificado só na validação não tem como ser corrigido
dentro do próprio processo — a correção exigiria voltar à elicitação
(ou análise), o que a sequência estritamente linear, por definição,
não permite.

---

## O processo clássico de Engenharia de Requisitos (conhecimento consolidado) — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ A sequência de quatro etapas do processo clássico de Engenharia de Requisitos poderia, em princípio, ser aplicada à elaboração de uma nova política pública, substituindo "requisitos de software" por "demandas da população" em cada etapa.

**Resposta:** Verdadeiro

**Justificativa:** A estrutura lógica das quatro etapas — coletar
demandas, negociar entre demandas conflitantes, formalizar em um
documento, validar com quem foi consultado — não depende de o produto
final ser software; é uma estrutura de processo de decisão coletiva
aplicável, com adaptações, a outros domínios como políticas públicas.

---

## O processo clássico de Engenharia de Requisitos (conhecimento consolidado) — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como o processo de Engenharia de Requisitos tem uma etapa chamada "análise e negociação", isso garante que qualquer conflito de interesse entre stakeholders será resolvido de forma justa entre as partes envolvidas.

**Resposta:** Falso

**Justificativa:** O nome formal da etapa não garante um resultado
justo — a negociação ainda ocorre dentro de uma estrutura de poder
desigual entre os participantes presentes à mesa (e, como discutido, só
entre quem conseguiu chegar até ela).

---

## Value Sensitive Design (Steen, Cap. 18) — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se a investigação empírica de valores (entrevistas, workshops com stakeholders) do Value Sensitive Design fosse pulada, e o processo começasse direto pela investigação técnica/tecnológica (de que forma o sistema pode ser construído), os requisitos resultantes ainda emergiriam da mesma forma descrita no Cap. 18 de Steen, como resultado das investigações empíricas.

**Resposta:** Falso

**Justificativa:** O trecho citado atribui explicitamente a origem dos
requisitos (tentativos) às investigações empíricas. Pular essa etapa e
começar pela investigação tecnológica inverteria a lógica do método —
os requisitos não teriam mais essa origem específica descrita no texto.

---

## Value Sensitive Design (Steen, Cap. 18) — item (b)

**Heurística:** Limite

**Afirmação:** ✔ No limite em que apenas um único stakeholder (ex.: o cliente pagante) tem seus valores investigados no processo de Value Sensitive Design, a expressão "permitir que diversos stakeholders expressem seus valores e os combinem produtivamente" deixaria de descrever o que está ocorrendo nesse processo.

**Resposta:** Verdadeiro

**Justificativa:** A definição de VSD citada na aula depende
explicitamente da pluralidade de stakeholders envolvidos ("diversos
interessados"). Reduzir a investigação a um único stakeholder elimina
essa característica central, ainda que o nome "Value Sensitive Design"
continue sendo usado.

---

## Value Sensitive Design (Steen, Cap. 18) — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ A lógica de Value Sensitive Design — investigar empiricamente os valores em jogo antes de especificar requisitos — se aplicaria ao design de um sistema de triagem hospitalar, no sentido de entrevistar enfermeiros e pacientes sobre o que consideram justo antes de programar a lógica de priorização.

**Resposta:** Verdadeiro

**Justificativa:** É uma aplicação direta do mesmo método a um domínio
não discutido na aula: investigar empiricamente valores (o que
enfermeiros e pacientes consideram justo) antes de transformar isso em
requisito técnico de priorização.

---

## Value Sensitive Design (Steen, Cap. 18) — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como o Value Sensitive Design combina investigações empíricas, conceituais e tecnológicas, isso significa que, uma vez completado o processo uma única vez no início do projeto, os requisitos de valores resultantes permanecem válidos e não precisam ser revisitados, mesmo com mudanças de contexto.

**Resposta:** Falso

**Justificativa:** O próprio trecho citado descreve as três
investigações como combináveis "em um processo iterativo" — a
iteratividade é uma característica explícita do método, o oposto de
"completar uma única vez e nunca revisitar".

---

## A cadeia NFR → ADR → gate de CI — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se um compromisso ético fosse traduzido diretamente em uma Decisão de Arquitetura (ADR), sem antes passar por um Requisito Não-Funcional (NFR) testável, ainda seria possível, a partir só da ADR, construir automaticamente um gate de CI que impeça regressão desse compromisso.

**Resposta:** Falso

**Justificativa:** Um gate de CI automatizado precisa de um critério de
aprovação/reprovação concreto e verificável — exatamente o que o NFR
testável fornece. Uma ADR documenta uma decisão e seu raciocínio, mas
não define, por si só, o critério mensurável necessário para
automatizar um teste de regressão.

---

## A cadeia NFR → ADR → gate de CI — item (b)

**Heurística:** Limite

**Afirmação:** ✗ No limite em que um gate de CI testa uma condição tão frouxa que praticamente qualquer código passa por ele sem alteração de comportamento, esse gate ainda cumpriria, na prática, a função de "impedir regressão" descrita nesta aula.

**Resposta:** Falso

**Justificativa:** A função de um gate de CI, como descrita na aula, é
efetivamente bloquear regressões reais. Um critério tão frouxo que
nunca bloqueia nada não cumpre essa função — ele existe formalmente,
mas não protege o compromisso de fato, esvaziando o propósito do
mecanismo.

---

## A cadeia NFR → ADR → gate de CI — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ A cadeia de tradução (compromisso → NFR testável → decisão de arquitetura → porta de processo) se aplicaria a um compromisso corporativo de reduzir vieses discriminatórios em um sistema de contratação, na forma de um NFR sobre taxas de erro por subgrupo, uma ADR sobre qual métrica de justiça adotar, e um gate de CI que bloqueia deploys que piorem essa métrica.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma estrutura de tradução (valor abstrato →
métrica testável → decisão documentada → porta de processo
automatizada) aplicada a um compromisso diferente (não discriminação em
vez de acessibilidade), preservando a lógica de cada etapa.

---

## A cadeia NFR → ADR → gate de CI — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como um Requisito Não-Funcional testável é, por definição, mensurável, isso significa que qualquer compromisso ético que não possa ser perfeitamente quantificado deve ser descartado como requisito de engenharia.

**Resposta:** Falso

**Justificativa:** A aula explicitamente aponta que transformar um
valor em NFR é uma simplificação necessária, não uma tradução perfeita
— a métrica captura uma parte operacionalizável do valor, sem esgotá-lo.
Não conseguir quantificar perfeitamente um compromisso não implica
descartá-lo; implica reconhecer que a tradução em NFR é parcial e pode
precisar de revisão (daí a natureza iterativa do VSD).

---

## Conway e requisito sem dono: a mesma "queda no buraco" — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se todo requisito de um sistema tivesse, desde sua criação, uma equipe explicitamente designada como responsável por sua fronteira (mesmo que essa fronteira cruze múltiplos módulos), o mecanismo de "requisito cai no buraco entre equipes" discutido nesta aula deixaria de se aplicar a esse requisito específico.

**Resposta:** Verdadeiro

**Justificativa:** O mecanismo de "queda no buraco" depende
especificamente da ausência de um dono claro da fronteira. Com um dono
explícito designado, mesmo para uma fronteira que cruza módulos, essa
condição de ausência deixa de existir, e o mecanismo não se aplica.

---

## Conway e requisito sem dono: a mesma "queda no buraco" — item (b)

**Heurística:** Limite

**Afirmação:** ✗ No limite em que um requisito de acessibilidade afeta igualmente todos os módulos de um sistema (nenhum módulo é mais responsável por ele do que outro), a analogia com uma "interface técnica sem dono" feita nesta aula se tornaria menos aplicável, e não mais, a esse requisito.

**Resposta:** Falso

**Justificativa:** É o oposto: um requisito transversal, que afeta
igualmente todos os módulos sem que nenhum se sinta especificamente
responsável por ele, é exatamente o caso de maior risco de "cair no
buraco" — ninguém o assume como "seu", precisamente porque é de
"todos" e, na prática, de ninguém. A analogia se torna mais aplicável,
não menos.

---

## Conway e requisito sem dono: a mesma "queda no buraco" — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ A mesma lógica de "responsabilidade sem dono claro leva a negligência estrutural" se aplicaria à manutenção de um código legado compartilhado por várias equipes, nenhuma das quais o considera "seu" módulo principal.

**Resposta:** Verdadeiro

**Justificativa:** É uma aplicação direta do mesmo mecanismo — ausência
de um dono claro de uma responsabilidade compartilhada tende a produzir
negligência estrutural, seja para um requisito ético (Bloco 5) ou para
código legado técnico.

---

## Conway e requisito sem dono: a mesma "queda no buraco" — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como a Lei de Conway trata de módulos técnicos e o Bloco 5 trata de requisitos éticos, a analogia entre os dois é apenas estética/retórica, sem nenhum mecanismo causal real em comum entre as duas situações.

**Resposta:** Falso

**Justificativa:** O mecanismo causal é o mesmo em ambos os casos:
ausência de comunicação/responsabilidade clara sobre uma fronteira
compartilhada leva a um resultado malformado ou negligenciado nessa
fronteira, seja ela uma interface entre módulos técnicos ou um
requisito ético entre equipes. A analogia é estrutural, não só
estética.

---

## Síntese da aula e a ponte para a Aula 5 — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se a Engenharia de Software fosse, de fato, uma sequência neutra de passos puramente técnicos (como a aula argumenta que não é), a existência da Lei de Conway como fenômeno replicável ao longo de décadas seria mais difícil de explicar.

**Resposta:** Verdadeiro

**Justificativa:** A Lei de Conway só faz sentido como fenômeno
replicável porque a estrutura social/organizacional de quem constrói
o sistema deixa marca real no resultado técnico. Se a engenharia fosse
puramente técnica e neutra em relação à organização humana por trás
dela, não haveria razão estrutural para esse padrão se repetir ao longo
de décadas e contextos diferentes.

---

## Síntese da aula e a ponte para a Aula 5 — item (b)

**Heurística:** Limite

**Afirmação:** ✔ No limite em que uma equipe de desenvolvimento segue rigorosamente todo o processo de tradução ético descrito no Bloco 5 (NFR, ADR, gate de CI) para todo compromisso social identificado, essa equipe ainda poderia produzir um sistema com uma arquitetura que espelha disfuncionalmente seu organograma, pelo mecanismo do Bloco 3.

**Resposta:** Verdadeiro

**Justificativa:** Os dois mecanismos discutidos na aula são
independentes entre si: seguir bem o processo de tradução ética (Bloco
5) não neutraliza a pressão estrutural de comunicação que rege a
arquitetura geral do sistema (Bloco 3) — são dois fenômenos distintos
que podem ocorrer, ou não, de forma simultânea e independente.

---

## Síntese da aula e a ponte para a Aula 5 — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ A tese central desta aula — de que decisões de processo e organização têm consequência técnica — se estenderia, pela mesma lógica, ao argumento da Aula 5 de que decisões de arquitetura (quantos serviços, onde rodam) têm consequência material e ambiental — em ambos os casos, uma escolha aparentemente "só de processo/design" tem efeito concreto fora do código em si.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente a ponte que fecha a aula: a mesma
lógica estrutural — uma decisão que parece "de processo" ou "de design"
tem consequência concreta fora do próprio código — se estende do
domínio organizacional (Aula 4) para o domínio material/ambiental
(Aula 5).

---

## Síntese da aula e a ponte para a Aula 5 — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como esta aula mostrou dois mecanismos pelos quais a prática social de construir software afeta o resultado técnico, conclui-se que qualquer falha técnica de um sistema deve ser explicada primariamente por causas organizacionais, nunca por erros técnicos comuns (bugs, escolhas de algoritmo etc.).

**Resposta:** Falso

**Justificativa:** A aula acrescenta uma lente sociotécnica adicional —
mostra que fatores organizacionais também explicam parte dos
resultados técnicos — mas não elimina nem substitui explicações
técnicas comuns e legítimas (bugs, escolhas de algoritmo, limitações de
hardware etc.) como causas de falha. Generalizar para "sempre
organizacional, nunca técnico" é uma falsa dicotomia.
