## Resumo — Aula 3: Computing, Its Domains, and Professional Responsibility

**Revisão de estrutura (2026-08-25), a pedido do usuário** — feedback
direto: a versão anterior misturava a abstração "o que é um código, pra
que serve" com o conteúdo concreto dos códigos, cedo demais, e nunca
chegava a explicar o que um conselho de profissão de fato *faz* antes de
debater se a Informática deveria ter um. Reestruturada assim: primeiro
os códigos em si (concretamente, o que dizem); depois a função de um
conselho de profissão; só então o debate de regular ou não a Informática
— agora também comparado com o que outros países fazem (EUA, Canadá,
Reino Unido). O bloco de limites dos códigos (autointeresse, vagueza,
"pode-se viver pelo código") continua — o usuário disse que é
interessante — só que reposicionado para depois desses três blocos, não
antes.

**Segunda revisão (mesma data), a pedido do usuário, a partir dos
slides de uma versão anterior desta disciplina (ano passado)** — quatro
mudanças, detalhadas nos blocos abaixo:

1. Tirar os **Dez Mandamentos** do Bloco 2 ("são bem tocos" — feedback
   literal do usuário). No lugar, aprofundar **ACM Code of Ethics** e
   **IEEE-CS/ACM Software Engineering Code**, com o mesmo nível de
   detalhe (estrutura + cláusulas numeradas + gloss "na prática") que os
   slides do ano passado tinham.
2. **LGPD/GDPR entra junto do bloco de conselho de profissão** (Bloco
   3), não como tópico separado — a lógica do usuário: ambos são
   "formas judicializadas de regular a atuação", só que por mecanismos
   diferentes (conselho regula *quem* pode exercer; lei de proteção de
   dados regula *como* a atuação deve ocorrer, independente de quem
   exerce).
3. No Bloco 5 (limites dos códigos), explicitar a crítica de que
   **autorregulação por código tem sido historicamente usada como
   estratégia para evitar regulação de fato** (governamental/judicial)
   — feedback à parte do usuário, chegou depois do resto.
4. ~~Incluir o framework geral de tomada de decisão moral de Ruggiero
   como ponte para o Landon & Landon do Bloco 6~~ — **decidido: fora
   desta aula** (ver ressalva de fonte abaixo; o usuário optou por não
   incluir, já que não está em nenhuma das fontes da disciplina). Bloco
   6 permanece sem mudança de conteúdo.

**Verificação de fontes desta segunda revisão** (Etapa de precisão de
conteúdo, CLAUDE.md) — busquei nos cinco PDFs de `_fontes/` (CSV1, CSV2,
CSV3 = Maciel & Viterbo Vols. 1–3; EthEng = Van de Poel & Royakkers;
EthTech = Steen, *Ethics for people who work in tech*, já presente como
link simbólico, usado até agora só en passant):

- **ACM Code / IEEE-CS/ACM Code:** a estrutura de 3 partes do código da
  ACM (princípios éticos gerais / responsabilidades profissionais /
  princípios de liderança) **está** resumida em EthTech, p. 88 — mas só
  como parágrafo-resumo com 1–2 exemplos por parte, não as cláusulas
  numeradas (1.1–1.4, 2.1/2.2/2.5, 3.4/3.7) que vieram dos slides do ano
  passado. O mesmo vale para os 8 princípios do IEEE-CS/ACM SE Code
  (PUBLIC, CLIENT AND EMPLOYER, ... SELF): EthEng só cita o preâmbulo do
  código numa questão de estudo (p. 62), não os 8 princípios. As
  cláusulas numeradas em si só existem no **texto oficial dos próprios
  códigos** (acm.org/code-of-ethics; o SE Code conjunto IEEE-CS/ACM).
  **Tratamento proposto:** citar os códigos como fonte primária/oficial
  diretamente (mesmo tratamento já dado, neste mesmo plano, ao
  NCEES/Engineers Canada/BCS do Bloco 4 — sinalizado explicitamente como
  fonte primária, não uma citação literal dos dois livros-texto), usando
  EthTech e EthEng para a moldura pedagógica (por que os códigos existem,
  a ligação com ética do dever).
- **LGPD/GDPR:** GDPR aparece duas vezes em CSV2 (Maciel & Viterbo Vol.
  2) — no capítulo de diferenças culturais em design (consentimento
  claro, sem "termos e condições" ilegíveis) e no capítulo de
  e-Democracia (§12, GDPR/LGPD citados dentro da lista de requisitos de
  Shapiro (2018), sob "Propriedade e privacidade de dados"). Os **seis
  princípios específicos** (Finalidade, Adequação e Necessidade,
  Transparência, Segurança e Prevenção, Não Discriminação,
  Responsabilização) vêm do **Art. 6º da própria Lei 13.709/2018** — de
  novo, fonte primária/legal, no mesmo espírito de já termos citado a
  Lei 5.194/1966 Art. 6º diretamente no Bloco 3.
- **Autorregulação para evitar regulação:** **achado direto** em Van de
  Poel & Royakkers, §2.3.1 "Codes of conduct and self-interest" (EthEng):
  *"Codes of conduct are a form of self-regulation. Sometimes, they are
  primarily formulated for reasons of self-interest, for example to
  improve one's image to the outside world, to avoid government
  regulation or to silence dissident voices."* — mais o caso Tozer (ACEA
  expulsou um engenheiro por criticar publicamente uma decisão da
  prefeitura) e a definição de *window-dressing*. Isso já embasa (e
  reforça) o bullet de "autointeresse" que o Bloco 5 já tinha.
- **Framework de Ruggiero (tomada de decisão moral):** **não encontrado
  em nenhum dos 5 PDFs de `_fontes/`.** Não é conteúdo de Maciel &
  Viterbo, Van de Poel & Royakkers, nem Steen — aparenta vir de uma obra
  diferente (provável: Vincent Ryan Ruggiero, sobre pensamento crítico
  em ética), que não está entre as fontes desta disciplina. **Decisão
  do usuário: deixar de fora desta aula.** Bloco 6 permanece com o
  conteúdo original (Snowden + Landon & Landon + Ciclo Ético), sem essa
  camada extra.

As duas primeiras aulas construíram o vocabulário conceitual (sistema
sociotécnico, mapa de atores, teorias éticas normativas, Ciclo Ético) —
mas nenhuma delas tratou de como a **profissão de computação**, como
instituição concreta, tenta traduzir esse vocabulário em regras
praticáveis do dia a dia. Esta aula faz essa ponte: parte de um caso
real (BART) em que engenheiros foram demitidos por seguirem o código de
ética profissional que os protegia só no papel; mostra concretamente o
que códigos de conduta reais dizem; explica o que um conselho de
profissão de fato faz; usa os dois para entender por que a Informática
não tem nenhum dos dois no Brasil — nem código oficial, nem conselho —,
comparando com o que acontece (ou não) em outros países; revisita os
limites conhecidos dos códigos de conduta em geral; e fecha com uma
provocação (o caso Snowden) e uma ponte para a Aula 4.

**Pré-requisitos:** Aula 1 (mapa de atores, responsabilidade
compartilhada) e Aula 2 (teorias éticas, Ciclo Ético — retomado ao final
desta aula em comparação com um processo análogo de 5 passos proposto
por Maciel & Viterbo, Cap. 7).

**Objetivos de aprendizagem** (do `index.md`, Lesson 3):
- **Objectives:** Mapear o campo da computação, discutir a relevância e
  aplicação de códigos de ética profissionais (ACM, SBC, IEEE), e
  examinar o escopo das responsabilidades profissionais ativas e
  passivas perante a sociedade.
- **Expected Competencies:** Capacidade de alinhar práticas técnicas a
  códigos de ética profissionais estabelecidos e avaliar responsabilidade
  individual em cenários de falha de software ou dano social.

**Leitura recomendada:** Maciel & Viterbo (2020), Vol. 1, Cap. 1 "A
Formação em Computação", Cap. 5 "Regulamentação da Profissão", e Cap. 7
"Ética Profissional em Computação"; Van de Poel & Royakkers (2011), Cap.
2 "Codes of Conduct" (sem mudança desta revisão).

**Fontes novas/primárias nesta revisão (não são citação literal dos
livros-texto da disciplina) — sinalizadas explicitamente como tal no
texto da aula, nunca misturadas com as citações literais de Maciel &
Viterbo / Van de Poel & Royakkers / Steen:**

- **ACM Code of Ethics and Professional Conduct** — texto oficial
  ([acm.org/code-of-ethics](https://www.acm.org/code-of-ethics)),
  estrutura em 3 partes: 1. General Ethical Principles (1.1–1.7, ex.:
  1.1 contribute to society and human well-being, 1.4 be fair and take
  action not to discriminate), 2. Professional Responsibilities (2.1–
  2.9, ex.: 2.1 strive for high quality, 2.2 maintain high standards of
  competence, 2.5 give comprehensive evaluation of computer systems and
  their impacts), 3. Professional Leadership Principles (3.1–3.7, ex.:
  3.4 ensure fair participation of, and fair treatment of, all members
  of the organization, 3.7 recognize and take special care of systems
  that become integrated into the infrastructure of society). Cada item
  usado na aula recebe um gloss "na prática" concreto.
- **IEEE-CS/ACM Software Engineering Code of Ethics and Professional
  Practice** — texto oficial (o mesmo cujo preâmbulo já é citado em
  EthEng, p. 62), 8 princípios: PUBLIC, CLIENT AND EMPLOYER, PRODUCT,
  JUDGMENT, MANAGEMENT, PROFESSION, COLLEAGUES, SELF — cada um também
  com gloss "na prática".
- **Lei 13.709/2018 (LGPD), Art. 6º** — os princípios que regem o
  tratamento de dados pessoais no Brasil: Finalidade; Adequação e
  Necessidade (minimização); Livre Acesso e Transparência; Segurança e
  Prevenção; Não Discriminação; Responsabilização e Prestação de
  Contas. Usado ao lado do GDPR europeu (2018), já mencionado em CSV2 —
  Maciel & Viterbo, Vol. 2, cap. de e-Democracia (§12) e cap. de
  diferenças culturais em design.
- **Comparação internacional de regulamentação (Bloco 4, sem mudança
  nesta revisão):**

- NCEES/NSPE (EUA): o exame de licenciamento profissional (PE) específico
  para *Software Engineering* foi criado em 2013 (por NSPE, IEEE-USA,
  IEEE Computer Society e o Texas Board of Professional Engineers) e
  **descontinuado em 2019** por baixa demanda — só 81 candidatos ao todo
  em 5 aplicações, abaixo do mínimo de 50 novos examinandos em duas
  aplicações consecutivas que a NCEES exige para manter um exame ativo.
  ([NCEES](https://ncees.org/ncees-discontinuing-pe-software-engineering-exam/),
  [NSPE](https://www.nspe.org/career-growth/pe-magazine/may-2018/ncees-ends-software-engineering-pe-exam))
- Engineers Canada / Alberta: no Canadá, o título "*engineer*" é
  legalmente protegido por reguladores provinciais (ex.: APEGA, em
  Alberta) — usar "*software engineer*" sem licença tem sido, na
  prática, uma zona cinzenta contestada; em 2024, Alberta moveu-se para
  **abrir uma exceção legal** permitindo o uso do título "*software
  engineer*" sem licença da APEGA.
  ([Engineers Canada](https://engineerscanada.ca/news-and-events/news/engineering-regulators-reiterate-licensure-requirements-for-those-using-software-engineer-and-other-it-titles),
  [CBC](https://www.cbc.ca/news/canada/edmonton/alberta-software-engineer-amendment-1.7019743))
- Reino Unido: os títulos de engenharia (*Chartered Engineer*,
  *Incorporated Engineer* etc.) são protegidos por carta régia via o
  Engineering Council — mas, separadamente, existe também o
  **Chartered IT Professional (CITP)**, um título voluntário concedido
  pela British Computer Society (BCS) a profissionais de TI que atendem
  certos critérios — sem exigir licença compulsória para atuar na área.
  ([Wikipedia — Chartered IT Professional](https://en.wikipedia.org/wiki/Chartered_IT_Professional),
  [BCS](https://www.bcs.org/membership-and-registrations/get-registered/chartered-it-professional/))

**Leitura pedagógica desses três casos:** nenhum país "resolveu" essa
questão de um jeito limpo. Os EUA tentaram formalizar um caminho de
licenciamento tipo engenharia para software especificamente, e ele
morreu por desinteresse voluntário (poucos escolheram fazer a prova,
porque a maioria do trabalho em software nunca exigiu isso
legalmente). O Canadá tem a proteção de título mais forte dos três — e
por isso mesmo enfrenta a tensão mais aguda, com uma província
recuando ao vivo, em 2024. O Reino Unido tem uma terceira via: um título
voluntário (CITP) que empresta prestígio sem exigir licença — mais perto
do meio-termo entre "regulamentação plena" e "nada", uma opção que nem
o Brasil nem os EUA adotaram para computação. Isso não fecha o debate
brasileiro; mostra que ele é uma versão local de uma pergunta sem
resposta óbvia em nenhum lugar.

## Plano de aula — Aula 3 (carga horária nominal: ~75–85min)

> Cresceu bastante em relação à versão anterior (~60–65min): o
> aprofundamento em ACM/IEEE-CS (Bloco 2), a segunda metade de
> LGPD/GDPR (Bloco 3) e a expansão do Bloco 5 somam ~20min. Se a carga
> horária real da disciplina for menor, os candidatos naturais a cortar
> ao vivo são a seleção de cláusulas do ACM/IEEE-CS (usar menos
> exemplos "na prática") e a checklist prática de LGPD/GDPR — não a
> comparação internacional do Bloco 4, que já é compacta. Mesma
> ressalva de sempre: o professor escolhe, ao vivo, quanto detalhar.

1.  **Abertura: um código que não protegeu quem o seguiu** (~5–8 min,
    sem mudança de conteúdo) — O caso **BART**: três engenheiros
    demitidos em 1972 depois de alertar a diretoria sobre falhas de
    segurança; o IEEE interveio sem sucesso; um acidente confirmou o
    alerta 3 semanas depois. **Pergunta de abertura:** se seguir o
    código profissional não protege quem o segue, para que serve um
    código de conduta?

2.  **Os códigos de conduta, concretamente** (~20–25 min — **cresceu**
    em relação à versão anterior por causa da profundidade nova em ACM
    e IEEE-CS/ACM, a pedido do usuário; nos slides, mais extenso ainda,
    não um resumo — mesmo padrão de densidade dos slides do ano
    passado) — Abrir com cláusulas da **NSPE** e da **FEANI** (Van de
    Poel & Royakkers, competência e segurança pública) como aquecimento
    — códigos mais curtos, mais fáceis de ler por extenso. Em seguida,
    o núcleo do bloco: **ACM Code of Ethics**, nas suas 3 partes
    (princípios éticos gerais, responsabilidades profissionais,
    princípios de liderança — estrutura confirmada em EthTech, p. 88),
    com uma seleção de cláusulas numeradas (1.1, 1.4, 2.1, 2.2, 2.5, 3.4,
    3.7) e um gloss "na prática" para cada uma — ex.: 2.5 ("dar uma
    avaliação abrangente de sistemas e seus impactos, incluindo
    riscos") na prática significa não vender um sistema de reconhecimento
    facial escondendo sua taxa de erro por subgrupo demográfico. Depois,
    o **IEEE-CS/ACM Software Engineering Code**, nos seus 8 princípios
    (PUBLIC, CLIENT AND EMPLOYER, PRODUCT, JUDGMENT, MANAGEMENT,
    PROFESSION, COLLEAGUES, SELF), de novo com gloss "na prática" —
    reconectando com o caso BART da abertura (PUBLIC é exatamente o
    princípio que os engenheiros do BART invocaram). Só depois de ver o
    conteúdo real dos quatro códigos, introduzir a distinção
    **profissional vs. corporativo** (o IEEE do caso BART é profissional)
    e os **três objetivos possíveis** — aspiracional, consultivo,
    disciplinar — como lente para classificar o que acabamos de ler
    (nenhum dos códigos de computação citados é disciplinar, por falta
    de conselho — gancho para o Bloco 3).

3.  **Formas judicializadas de regular a atuação: conselho de profissão
    e proteção de dados** (~12–15 min — **bloco expandido**: já era
    novo nesta revisão, agora ganha uma segunda metade) — Primeira
    metade, sem mudança de conteúdo: o que um conselho como o **CREA**
    (engenharia), **CRM** (medicina) ou **OAB** (direito) de fato faz:
    registra profissionais, fiscaliza o exercício da profissão, e tem
    **poder legal** de impedir quem não é registrado de exercer (Lei
    5.194/1966, Art. 6º, já citada na aula anterior — reaproveitar). A
    diferença central para o Bloco 2: um conselho é o que torna um
    código **disciplinar** de fato — sem ele, "disciplinar" no papel não
    tem força nenhuma. Segunda metade, **nova**: **LGPD (Brasil) e GDPR
    (UE)** como uma *outra* forma de regulação judicializada da atuação
    em computação — mas por um mecanismo diferente do conselho: em vez
    de licenciar *quem* pode exercer, a lei regula diretamente *como* a
    atuação deve ocorrer (qualquer pessoa pode processar dados, mas só
    de certas formas), com multas e sanções reais como mecanismo de
    força — o análogo funcional do "poder legal" do conselho. Os seis
    princípios do Art. 6º da LGPD (Finalidade, Adequação e Necessidade,
    Transparência, Segurança e Prevenção, Não Discriminação,
    Responsabilização) mapeados lado a lado com o GDPR europeu (CSV2,
    Maciel & Viterbo Vol. 2). Fechar com uma checklist prática de
    perguntas que um profissional pode se fazer diante de um sistema que
    coleta dados pessoais (ex.: "Para que finalidade específica este dado
    está sendo coletado — e só esse dado, ou mais do que o necessário?",
    "O titular teria como saber, em linguagem simples, o que está sendo
    feito com o dado dele?"), sinalizada como material pedagógico do
    professor, não citação literal. Preparar o terreno para a pergunta
    do Bloco 4: a Informática tem, hoje, um conselho de profissão? (Não.
    Uma lei geral de dados que constrange sua atuação? Sim — regulação
    judicializada parcial, por um dos dois mecanismos, não pelo outro.)

4.  **Regular ou não a Informática — no Brasil e no mundo** (~15–18
    min, bloco existente + comparação internacional nova) — Mapear:
    de mais de 2400 ocupações reconhecidas no Brasil, só ~68 são
    regulamentadas, e a Informática não está entre elas, apesar de
    tentativas desde 1978. Vantagens/desvantagens já argumentadas no
    livro-fonte (custo de anuidades, redução da multidisciplinaridade
    histórica, vs. falta de garantia de qualidade). **Novo:** e em
    outros países? EUA (exame de licenciamento PE para software criado
    em 2013, descontinuado em 2019 por desinteresse voluntário), Canadá
    (título de "engenheiro" protegido por lei — e por isso mesmo uma
    tensão real e recente sobre "software engineer", com Alberta
    abrindo uma exceção em 2024), Reino Unido (título voluntário
    Chartered IT Professional da BCS, sem licença obrigatória).
    Conclusão: não é uma esquisitice brasileira — é uma pergunta sem
    resposta limpa em lugar nenhum.

5.  **Os limites conhecidos dos códigos** (~12–15 min, bloco existente,
    reposicionado para depois dos Blocos 2–4, **conteúdo expandido**:
    a crítica de autointeresse agora inclui explicitamente a relação
    com regulação de fato, a pedido do usuário) — Agora que já vimos
    códigos reais, o que um conselho faz, e que a regulamentação é um
    problema aberto globalmente, revisitar os limites que valem mesmo
    onde HÁ conselho e código oficial: **autointeresse, *window-
    dressing*, e código como substituto de regulação real** — citação
    literal de Van de Poel & Royakkers, §2.3.1: *"Codes of conduct are a
    form of self-regulation. Sometimes, they are primarily formulated
    for reasons of self-interest, for example to improve one's image to
    the outside world, **to avoid government regulation** or to silence
    dissident voices"* (tradução livre na aula) — com o caso **Tozer**
    (engenheiro expulso da ACEA australiana por criticar publicamente
    uma decisão de saneamento da prefeitura) como ilustração de código
    usado para silenciar dissenso, e o caso Google na China para
    *window-dressing*. **Callback explícito ao Bloco 3:** é exatamente
    o contraste entre autorregulação por código (voluntária, sem força
    de lei) e regulação judicializada (conselho, LGPD/GDPR — com multa,
    sanção, poder de excluir do exercício) que explica por que uma
    empresa prefere manter um código de ética bonito a apoiar uma lei
    de proteção de dados com dentes de verdade. **Vagueza e
    contradições potenciais** (lealdade crítica vs. acrítica;
    inconsistência entre NSPE/FEANI/IEEE sobre confidencialidade);
    **pode-se viver pelo código?** (BART reaberto). Fechar com: nenhuma
    dessas críticas invalida os códigos — só mostra que são ponto de
    partida, não substituto, para o julgamento moral (nem para a
    regulação de fato).

6.  **Fechamento: um caso para aplicar, e ponte** (~8–10 min, sem
    mudança de conteúdo — Ruggiero descartado, ver Resumo acima) — O
    caso **Snowden** como provocação final, sem solução óbvia;
    comparação breve entre o processo de deliberação de Landon & Landon
    e o Ciclo Ético da Aula 2; ponte para a Aula 4 (Parte 2 do curso:
    impactos ambientais e materiais da computação).

---

**Pontos abertos para sua aprovação antes de eu regerar a aula
completa:**

- A ordem proposta (BART → códigos concretos [ACM/IEEE-CS aprofundados]
  → conselhos + LGPD/GDPR → regular ou não [Brasil + mundo] → limites
  dos códigos [com a crítica de autorregulação-para-evitar-regulação] →
  Snowden/fechamento) bate com o que você tinha em mente?
- A comparação internacional (EUA/Canadá/Reino Unido, Bloco 4) é de
  fontes web, não dos dois livros-fonte da disciplina — happy para
  seguir assim, citando como tal, ou prefere que eu tente achar algo
  equivalente nos livros-fonte primeiro (não encontrei nada lá sobre
  regulação internacional da profissão de computação, já busquei)?
- ACM Code e IEEE-CS/ACM Code: ok citar o texto oficial dos códigos
  diretamente como fonte primária (mesmo tratamento do Bloco 4), já que
  as cláusulas numeradas específicas não estão nos livros-texto da
  disciplina, só resumidas em EthTech?
