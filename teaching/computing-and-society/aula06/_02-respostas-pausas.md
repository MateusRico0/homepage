# Respostas das Pausas Ativas — Aula 6

> Arquivo não publicado (`_02-respostas-pausas.md`) — nunca deve ser incluído no `index.qmd`. As notas em HTML publicadas contêm só a pergunta provocadora e o V/F sem resolução; os slides RevealJS mostram o V/F resolvido (✔/✗), mas sem a discussão longa abaixo.

---

## Pausa 1 (Bloco "De Onde Vem o Dado?"): Para que este dado foi criado?

**Discussão da pergunta provocadora.** A equipe do banco deveria perguntar, antes de qualquer algoritmo: (1) *Para que o dado do aplicativo de entregas foi criado?* Para operar entregas, não para medir capacidade de pagamento; o que ele oferece é, no máximo, um proxy. (2) *Quem aparece e quem não aparece?* Clientes que nunca usaram o aplicativo não têm registro; o modelo seria cego justamente para o grupo que se quer avaliar (clientes sem histórico de crédito). (3) *Há descompasso entre o rótulo que o modelo precisa (inadimplência) e o que o dado registra (pedidos, endereços)?* Sim: qualquer relação entre padrão de pedido e pagamento é indireta. (4) *O uso é compatível com o propósito informado aos clientes?* É uma pergunta de LGPD (art. 6º, I e II), que a aula retoma no Bloco 4. "Temos muito dado" não responde nenhuma delas: volume não corrige propósito nem cobertura.

**V/F — resolução.**

- ✗ **Falso.** Mesmo que as faixas de renda usassem o aplicativo em proporção igual, o dado de entregas continuaria sendo um proxy da capacidade de pagamento; o descompasso é de *propósito* (o dado foi criado para outra coisa), não só de cobertura. Erro típico: reduzir o problema de proxy a um problema de representatividade.
- ✗ **Falso.** Volume não corrige cobertura: bilhões de pedidos continuam deixando de fora quem nunca usa o aplicativo. Mais dados com o mesmo viés reforçam o viés. Erro típico: tratar o viés de amostra como ruído que a média compensa.
- ✔ **Verdadeiro.** Mesmo mecanismo: o histórico de contratações é dado administrativo, criado para registrar quem foi contratado, e é usado como proxy de "quem seria bom no cargo".
- ✗ **Falso.** O livro não conclui que dado reaproveitado seja inutilizável, e sim que é preciso avaliar o propósito original e os vieses típicos da fonte antes de usá-lo. Erro típico: extrapolar de "a maior parte do dado é reaproveitada" para "todo dado reaproveitado é inutilizável".

---

## Pausa 2 (Bloco 1 — Anatomia do Viés): Sem raça e sem gênero: livre de viés?

**Discussão.** A afirmação "livre de viés" deixa de examinar quase tudo. Remover colunas atua, no máximo, sobre uma decisão de preparação. Ela não toca (i) a **medição**: o rótulo de adimplência pode carregar decisões humanas passadas de concessão (viés social), e renda e ocupação podem medir coisas diferentes para grupos diferentes; (ii) a **amostragem**: quem é sub-representado na base continua sub-representado; (iii) o **tempo**: o modelo pode ter sido treinado antes de uma mudança de cenário; (iv) o **proxy**: o CEP e a ocupação carregam informação sobre o grupo (o CEP e a ocupação podem reconstruir o grupo). Além disso, a remoção dificulta a auditoria: sem o atributo registrado, fica mais difícil verificar se o modelo trata os grupos de forma diferente.

**V/F — resolução.**

- ✔ **Verdadeiro.** Remover colunas não toca na passagem de amostragem: um rótulo bem medido não repara uma base sem clientes de certas regiões.
- ✗ **Falso.** Cobertura completa elimina o viés de representação, mas não o social: as decisões humanas passadas de concessão, usadas como rótulo, continuam refletindo preconceito mesmo numa base completa. Erro típico: supor que completude da base elimina a influência de julgamentos humanos.
- ✗ **Falso.** O viés vem do conjunto de fundo do modelo pré-treinado (Varshney, p. 43); mexer nos metadados do ajuste fino não o alcança. Com dados semiestruturados, é preciso avaliar também o conjunto de fundo.
- ✗ **Falso.** Descartar linhas ou colunas pode *introduzir* viés de preparação (por exemplo, descartar linhas com dado ausente correlacionado ao grupo), e remover o atributo ainda impede de medir a disparidade. Erro típico: tratar a preparação como etapa que só pode melhorar o dado.

---

## Pausa 3 (Bloco 3 — Poder, Consentimento e Privacidade): Consentimento e poder no local de trabalho

**Discussão.** O consentimento não é legítimo. O uso é condição para participar do plano de saúde corporativo: o funcionário só pode aceitar, o que é o argumento de Varshney sobre o TraceBridge (o empregador que exige o uso como condição retira a oportunidade real de consentir). A finalidade "para fins de gestão" é genérica, e uma autorização genérica não é consentimento específico (na LGPD, art. 8º, § 4º, é nula). Perguntas que a equipe deveria fazer antes de coletar: (1) *Consentimento:* o funcionário foi informado do que é coletado e para quê, e pode recusar sem prejuízo? (2) *Poder:* quem decide o destino dos dados (a empresa pode rastrear pausas ou usá-los para outros fins)? (3) *Privacidade:* onde os dados ficam, quem acessa, o que é exposto (localização e batimentos cardíacos revelam saúde, dado sensível)? (4) *Necessidade:* a empresa precisa mesmo desses dados para o fim declarado? Se a resposta for insatisfatória, Varshney: sem consentimento, não prosseguir.

**V/F — resolução.**

- ✔ **Verdadeiro.** Sem coerção e com finalidade informada e limitada, cai a assimetria que tornava o consentimento vazio no TraceBridge. Ainda restam as questões de privacidade (armazenamento, acesso), que são outro eixo.
- ✔ **Verdadeiro.** Sob ameaça de desligamento não há escolha: o "consentimento" vira exigência (Varshney, p. 52).
- ✗ **Falso.** Estar acessível não é consentimento explícito; o livro trata a raspagem sem consentimento explícito como problemática (p. 53). Erro típico: confundir acessibilidade com autorização.
- ✗ **Falso.** O poder já está no uso interno: o empregador pode rastrear pausas e reuniões sem vender nada (Varshney, p. 52). Erro típico: reduzir o problema de poder à venda de dados a terceiros.

---

## Pausa 4 (Bloco 4 — LGPD): O empréstimo negado

**Discussão.** (a) O art. 20, § 1º, exige que o banco forneça, quando solicitado, informações "claras e adequadas a respeito dos critérios e dos procedimentos utilizados para a decisão automatizada". O art. 19, II, acrescenta o direito a uma declaração clara e completa que indique a origem dos dados, os critérios utilizados e a finalidade, em até 15 dias. (b) "O modelo de aprendizado profundo decidiu que você é um risco" descreve a *ferramenta*, não o *critério*: não basta. A empresa deve dizer quais informações pesaram (por exemplo, renda declarada, histórico de inadimplência, tempo de relacionamento) e o procedimento. (c) O segredo comercial e industrial é ressalvado no § 1º, mas o § 2º prevê que, se a informação é recusada com base nele, a ANPD poderá realizar auditoria para verificar aspectos discriminatórios; o titular pode ainda peticionar à ANPD (art. 18, § 1º). O cliente não fica sem recurso. (d) O que a lei **não** garante: revisão por pessoa (a expressão "por pessoa natural" saiu da redação); a definição do que é "discriminatório"; a aplicação do art. 20 a decisões em que um humano pondera o modelo com outros elementos (a letra fala em decisão "unicamente" automatizada); e o acesso ao código ou ao modelo em si.

**V/F — resolução.**

- ✔ **Verdadeiro.** A letra do art. 20 fala em decisão "unicamente" automatizada; um analista que pondera o score com outros elementos fica fora da hipótese literal. É um limite do texto.
- ✗ **Falso.** O segredo é ressalvado, mas o § 2º dá à ANPD o poder de auditar aspectos discriminatórios justamente quando o segredo é invocado, e o titular pode peticionar à autoridade.
- ✔ **Verdadeiro.** O art. 20 cita expressamente decisões "destinadas a definir o seu perfil pessoal, profissional, de consumo e de crédito"; a recusa automática de candidatos por um classificador de currículos define o perfil profissional.
- ✗ **Falso.** O § 1º pede informações "claras e adequadas"; entregar código e pesos incompreensíveis descreve a ferramenta, não o critério, e não cumpre a exigência. Erro típico: confundir disponibilizar com informar.

---

## Pausa 5 (Bloco 5 — Corrigir o Modelo ou Corrigir a Coleta?)

**Discussão.** Antes de "ajustar o modelo", vale perguntar sobre a coleta porque o problema descrito (poucos clientes da região na base) é um **viés de representação**, que entra na **amostragem**: a causa está no que foi registrado, não em como o modelo processa. Ajustar o modelo para compensar (por exemplo, pesos maiores para os poucos clientes da região) trata o sintoma, e com poucos registros a estimativa continua ruidosa e pode ainda ser diferente em *qualidade* (não só em quantidade). A ação de causa é coletar dados melhores dessa região. Se, mesmo depois da coleta melhorada, o dado continuar enviesado demais para o uso pretendido, Varshney (p. 41) diz que a conversa é sobre se o projeto deve sequer prosseguir; a pergunta não é "como compensar depois?", e sim "devemos usar este dado para esta decisão?".

**V/F — resolução.**

- ✔ **Verdadeiro.** Representação é um problema da amostragem: mais dados da região corrigem a origem; ajustar o modelo compensa o sintoma sem mudar o que foi registrado.
- ✗ **Falso.** Varshney diz o contrário: se todo dado relevante é enviesado demais, a conversa é se o projeto deve prosseguir, não como compensar depois.
- ✔ **Verdadeiro.** É o mesmo laço do policiamento preditivo (extensão nossa): o rótulo (clique) depende do que o sistema já mostrou; sem mudar a coleta do rótulo, o modelo só reforça a si mesmo.
- ✗ **Falso.** Varshney: sem consentimento, não prosseguir (p. 53); e a LGPD exige base legal válida (arts. 7º a 9º). Bom desempenho não legitima a obtenção do dado.
