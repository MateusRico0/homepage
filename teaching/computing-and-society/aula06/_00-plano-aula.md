# Plano de Aula — Aula 6: Data, Bias, and Algorithmic Discrimination

**Versão 2 (2026-09-21)** — reescrita do plano anterior a pedido do usuário ("a aula está bem
superficial"), usando como fontes centrais *Trustworthy Machine Learning* (Varshney, 2022) e a
Lei nº 13.709/2018 (LGPD, texto compilado). **Fora de escopo, por pedido explícito: métricas de
fairness** (paridade estatística, igualdade de oportunidades, teorema da impossibilidade etc.) —
ficam para uma aula seguinte. Pelo mesmo motivo saem desta aula as *estratégias de mitigação
algorítmica* (reweighing, adversarial debiasing, ajuste de limiares), que só fazem sentido depois
de haver uma métrica a satisfazer.

## Resumo — Aula 6

As aulas 4 e 5 mostraram que decisões de produto deixam marcas no software: pela estrutura da
organização (Conway), pelo desenho deliberado (*dark patterns*) e pelo método de pesquisa e
experimentação (A/B, Fogg, Kramer). A Aula 5 terminou plantando uma semente: **a métrica é um
proxy**, e um proxy pode medir coisas diferentes para grupos diferentes (o caso da seguradora que
usa custo de saúde como sinônimo de necessidade de cuidado, Varshney 2022, cap. 10). Esta aula
abre essa semente. Ela responde: **de onde vem o viés que já está no dado antes de qualquer
algoritmo tocá-lo, e o que o direito brasileiro (LGPD) exige de quem coleta e usa esse dado?**

A aula tem duas metades que se encaixam. A **primeira metade** (epistemologia do dado) usa o
capítulo 4 de Varshney como esqueleto: o dado passa por quatro "espaços" (construto → observado →
bruto → preparado); em cada passagem (medição, amostragem, preparação) entra um tipo de viés
(social, de representação, temporal, de preparação, envenenamento), e cada viés ameaça um tipo de
validade (de construto, externa, interna). Isso substitui a lista genérica "histórico /
amostragem / rotulagem" do plano anterior por um modelo com fonte, que dá ao aluno um
**roteiro de auditoria** aplicável a qualquer dataset. A **segunda metade** (poder e lei) usa o
capítulo 5 de Varshney (consentimento, poder, privacidade, anonimização) e a LGPD lida artigo por
artigo: princípios (art. 6º, com destaque para o IX, não discriminação), bases legais e
consentimento (arts. 7º–9º), dados sensíveis (art. 11, incluindo o §5º, que proíbe operadoras de
planos de saúde de usar dados de saúde para seleção de riscos), anonimização (arts. 5º e 12),
direitos do titular e decisões automatizadas (arts. 18–21), e responsabilização (arts. 38, 42,
44, 50, 52, 55-J). A aula termina mostrando **o que a LGPD não cobre** (segurança pública, art.
4º, III; ausência de definição de "discriminatório") e por que "corrigir a coleta" vem antes de
"corrigir o modelo".

**Pré-requisitos:** Aula 5 (Bloco 3: método neutro / métrica não; proxy que enviesa — caso
Varshney cap. 10 pp. 133–134; caso Kramer e consentimento); Aula 4, Bloco 5 (*dark patterns* —
retomados aqui só quando o art. 9º, §1º diz que consentimento obtido com informação "enganosa ou
abusiva" é nulo); Aula 2 (Ciclo Ético, para o fechamento).

**Estratégia Pedagógica:** **Estratégia A (*Outside-In*)** — parte do caso concreto (a seguradora
da Aula 5, agora dissecada; o recrutador da Amazon; a ONG que prevê pobreza a partir de imagens
de satélite) para o modelo (os quatro espaços), depois para a norma (LGPD), e fecha com limites.

**Carga horária nominal:** ~85 min (as notas HTML vão além do que cabe em sala; os slides
cobrem a mesma história, itemizada).

## Achados sobre a versão anterior de `index.qmd` (a corrigir na Etapa 3)

Além de ser curta, a versão anterior tinha problemas de conteúdo que esta reescrita corrige:

1. **Seção "Medindo a Injustiça: Métricas de Equidade"** e **"Estratégias de Mitigação"**:
   removidas (fora de escopo, ver acima).
2. **"Caso Phulo" apresentado como fato:** é um caso **fictício** de Varshney (cap. 9,
   distribuição de shift: modelo de crédito do Bank of Bulandshahr/Wavetel). O texto anterior o
   tratava como um exemplo real e o descrevia de modo impreciso ("África Central → Índia"). Se
   for usado, será rotulado como caso ilustrativo do livro.
3. **Gender Shades:** o texto dizia que o viés vinha de "datasets de treinamento compostos
   majoritariamente por rostos brancos e masculinos". O estudo (Buolamwini & Gebru, 2018) **audita
   três classificadores comerciais** (erro de até 34,7% para mulheres de pele escura contra no
   máximo 0,8% para homens de pele clara) e documenta que os *benchmarks* de análise facial então
   usados eram de 79,6% (IJB-A) e 86,2% (Adience) de pessoas de pele clara; os dados de
   treinamento dos sistemas comerciais **não são públicos**. Reescrever com essa precisão.
4. **Amazon:** o texto dizia "em 2018 a Amazon descobriu". Segundo a reportagem original
   (Dastin, Reuters, out. 2018): o projeto começou em 2014, a equipe percebeu o problema em 2015,
   e o projeto foi encerrado por volta de 2017; a reportagem é de 2018.
5. **Art. 20 da LGPD:** o texto anterior afirmava que "o direito à revisão" e o "direito à
   explicação" tinham a redação descrita, mas não mostrava que a **redação original exigia
   revisão "por pessoa natural"**, que a MP 869/2018 e a Lei 13.853/2019 alteraram o texto (a
   expressão saiu) e que o §3º (que exigiria revisão por pessoa natural) foi **vetado**. Isso está
   visível no próprio PDF do texto compilado e muda a leitura do artigo.
6. **GDPR:** o texto anterior atribuía ao GDPR conteúdo (direito à explicação, revisão humana)
   sem fonte. Não temos o texto do GDPR em `_fontes/`; a aula só citará o que Varshney diz (p. 53:
   lei abrangente promulgada na Área Econômica Europeia em 2018) e **não fará afirmações de mérito
   sobre o GDPR**. Se o usuário quiser, uma comparação LGPD × GDPR exige trazer o texto do GDPR
   para `_fontes/`.
7. **Forma:** título em inglês no cabeçalho (ok, é o padrão do curso, mantido no `title`), mas
   sem `output-file: notas.html` no YAML, sem Pausas Ativas no formato exigido (pergunta + V/F
   `□`), slides praticamente inexistentes (o bloco RevealJS tinha ~10 linhas) e sem
   `exercicios.qmd`/`soluções.qmd`/`_02-respostas-pausas.md`.

---

## Plano de aula — Aula 6 (~85 min)

1. **Abertura — Revisão e Introdução: "O Proxy Voltou"** (~8 min)
   - *Revisão cuidadosa da Aula 5* (explicar, não só nomear): (i) o teste A/B é neutro, a
     métrica não; (ii) toda métrica é um proxy, e o proxy pode medir coisas diferentes para
     grupos diferentes (caso da seguradora: custo de saúde ≠ necessidade de cuidado para
     pacientes negros); (iii) Kramer et al.: consentimento e a assimetria de poder entre quem
     coleta e quem é coletado.
   - *Ideia Central (Ausubel):* dado não é fato bruto — é o **resultado de uma cadeia de decisões**
     (o que medir, de quem, quando, como limpar), e cada decisão pode carregar viés. A aula
     dá nome a cada elo dessa cadeia e depois pergunta o que a lei brasileira diz sobre ela.
   - *Roteiro (4 perguntas):* (1) Por que "o dado fala por si" é falso? (2) Em que ponto da
     cadeia do dado o viés entra, e como reconhecê-lo? (3) O que a LGPD exige de quem coleta e usa
     dados pessoais, e o que ela deixa de fora? (4) Corrigir o modelo ou corrigir a coleta?
   - *Problema motivador:* a seguradora da Aula 5, agora **dissecada elo por elo**; e o recrutador
     da Amazon como segundo caso. Pergunta aberta ao final: "se ninguém digitou 'raça' no modelo,
     onde o viés entrou?"
   - As Pausas Ativas 1–4 ficam nos Blocos 1–4 (a da "coluna raça" fecha o Bloco 1); a
     abertura só termina com a pergunta de sondagem acima, sem V/F.

2. **Intuição — De Onde Vem o Dado?** (~8 min) — Varshney §4.1–4.2.
   - Modalidades em uma tabela mental: estruturado (tabular, séries, eventos, grafos) ×
     semiestruturado (imagem, áudio, vídeo, texto). Consequência: em dados estruturados, auditar
     a preparação e a engenharia de atributos; em semiestruturados, auditar também o **conjunto de
     dados de fundo** do modelo-base (viés herdado).
   - Fontes de dado: coletado com propósito (censo, pesquisa, experimento), **administrativo**,
     **social**, **crowdsourcing**, aumentado. Tese central: *a maior parte do dado usado em ML é
     reaproveitada*; então a primeira pergunta é "para que este dado foi criado?".
   - Caso-fio do livro: a ONG "Unconditionally" que quer prever pobreza (imagens de satélite,
     registros de celular, transações de dinheiro móvel, censo) — mostra concretamente cada fonte.

3. **Bloco 1 — A Anatomia do Viés: Quatro Espaços, Três Validades, Cinco Vieses** (~18 min)
   — Varshney §4.3 + cap. 10 §10.2.
   - Modelo dos quatro espaços: *construto* (mundo ideal, sem viés) → **medição** → *observado* →
     **amostragem** → *bruto* → **preparação** → *preparado* (diagrama TikZ).
   - Três validades: de construto ("mede o que deveria?"), externa ("generaliza para outras
     populações?"), interna ("houve erro no processamento?").
   - Cinco vieses, cada um com o caso do livro: **social** (rótulos de telhados por
     *crowdworkers*, cozinha e alojamento contados como casa; testes de aptidão com conhecimento
     cultural tácito), **de representação** (idosos sub-representados por menor posse de celular;
     censo com poucos recenseadores), **temporal** (satélite na estação chuvosa × seca;
     *covariate shift*, *prior probability shift*, *concept drift*), **de preparação** (descartar
     linhas com valor faltante quando a falta correlaciona com atributo sensível; proxies nos
     rótulos: prisões, utilização de saúde) e **envenenamento** (imagens de casas à beira do rio
     sempre rotuladas como pobreza extrema).
   - **A seguradora dissecada** (retomada da Aula 5): em que espaço/passagem cada problema entra
     (custo como proxy = construto→observado; só membros da própria seguradora = amostragem;
     rótulos humanos passados = viés social; agregação de utilização = preparação).
   - Casos complementares com fonte secundária, rotulados como tal: Amazon (recrutador),
     Gender Shades (auditoria de classificadores comerciais). O **ciclo de retroalimentação**
     (policiamento preditivo) é uma **extensão nossa** do argumento de Varshney sobre "prisões como
     proxy de crime" (p. 48) — o livro afirma o problema do proxy, não desenha o laço; a aula
     marcará isso.
   - **Pausa Ativa 1:** "Um dataset de crédito sem coluna de raça e sem coluna de gênero está livre de
     viés?" V/F condutor com quatro itens (contrafactual, caso limite, transferência de domínio
     para outro cenário de ML, falsa dicotomia).

4. **Bloco 2 — Proxies, Atributos Protegidos e a Falsa Cegueira** (~10 min)
   — Varshney §10.1–10.2, §4.2.2, §5.2 (quase-identificadores).
   - *Atributos protegidos* não são universais: "determinados por leis, regulamentos ou outras
     políticas" de cada domínio e jurisdição (p. 132). Grupos privilegiados definidos como os que
     historicamente recebem o rótulo favorável (p. 131). *(Só o vocabulário — sem métrica.)*
   - Por que remover a coluna não basta: o proxy carrega a informação de volta. CEP, histórico de
     compras, lacunas no currículo; o exemplo canônico de saúde (utilização ≠ doença).
   - **Ponte com privacidade (síntese nossa, sinalizada):** as variáveis que servem de *proxy*
     para atributos protegidos são as mesmas que a literatura de privacidade chama de
     *quase-identificadores* (sexo, data de nascimento, CEP; Varshney p. 54). O mesmo fato
     estatístico é um problema de discriminação (o modelo "adivinha" o grupo) e um problema de
     privacidade (o registro é reidentificado).
   - **Pausa Ativa 2:** identificar proxies em três sistemas (crédito, triagem de currículos,
     precificação de seguro) e dizer qual passagem do modelo dos quatro espaços cada um viola.

5. **Bloco 3 — Poder, Consentimento e Privacidade** (~12 min) — Varshney cap. 5.
   - Caso *TraceBridge* (rastreamento de contatos no retorno ao escritório): o empregador pode
     tornar o app condição de emprego; dados centralizados, sem criptografia; identidade do
     infectado exposta. Consentimento, poder e privacidade como três eixos distintos.
   - "Dado é poder" e *data exhaust*; imagens raspadas sem consentimento explícito.
   - Anonimização: identificadores × quase-identificadores × atributos sensíveis; *k*-anonimato
     (generalização/supressão) e seus ataques (homogeneidade, conhecimento prévio); privacidade
     diferencial em uma frase (ruído em consultas); compromisso privacidade × utilidade.
   - Fecho: o argumento de que **anonimizar não é a única forma de proteger** (controles
     institucionais, computação multipartidária, criptografia homomórfica) e a regra de Varshney:
     *sem consentimento, não prosseguir*.
   - **Pausa Ativa 3** (curta): um dataset "anonimizado" só com CEP, data de nascimento e sexo
     no lugar do nome é anônimo?

6. **Bloco 4 — A Moldura Legal: LGPD Lida Artigo por Artigo** (~20 min)
   - **Ideia condutora:** a LGPD não é "uma lei de privacidade" só; o art. 6º traz princípios que
     **casam um a um** com os vieses do Bloco 1 (tabela: princípio × tipo de viés).
   - (a) *Objeto e fundamentos* (arts. 1º–2º) e *âmbito* (arts. 3º–4º), com o alerta: **o art. 4º,
     III exclui segurança pública, defesa, investigação penal** — o terreno onde o policiamento
     preditivo e o reconhecimento facial vivem está *fora* da LGPD (regido por "legislação
     específica", art. 4º, §1º). O art. 4º, II, *b* (fins acadêmicos) também é um limite.
   - (b) *Definições* (art. 5º): dado pessoal, sensível, anonimizado, consentimento, RIPD.
   - (c) *Princípios* (art. 6º): finalidade, adequação, necessidade, **qualidade dos dados** (V),
     transparência, prevenção, **não discriminação (IX)**, responsabilização.
   - (d) *Bases legais e consentimento* (arts. 7º–10): "livre, informado e inequívoco"; art. 8º,
     §2º (ônus da prova é do controlador), §4º (autorização genérica é nula), §5º (revogação);
     art. 9º, §1º (informação enganosa ⇒ consentimento nulo — retoma *dark patterns*); art. 10
     (legítimo interesse).
   - (e) *Dados sensíveis* (art. 11): consentimento específico e destacado; **§1º** (aplica-se a
     qualquer tratamento que *revele* dado sensível e possa causar dano — gancho legal para
     proxies, **leitura nossa**, a doutrina debate a extensão); **§5º** (operadoras de planos
     de saúde proibidas de usar dados de saúde para seleção de riscos) — o caso da seguradora da
     Aula 5, agora no ordenamento brasileiro.
   - (f) *Anonimização* (art. 5º, III e XI; art. 12): dado anonimizado deixa de ser pessoal, **salvo**
     se reversível "com esforços razoáveis"; art. 12, §2º (perfis comportamentais podem ser
     tratados como dado pessoal). Volta ao *k*-anonimato do Bloco 3.
   - (g) *Direitos do titular e decisão automatizada* (arts. 18–21): acesso, correção,
     anonimização/eliminação; **art. 20** (revisão de decisão "unicamente" automatizada; §1º
     "informações claras e adequadas sobre os critérios e os procedimentos", ressalvado o segredo
     comercial e industrial; §2º auditoria da ANPD "para verificação de aspectos discriminatórios";
     §3º vetado); art. 21 (dados do exercício de direitos não podem ser usados em prejuízo).
     Leitura crítica: o direito é a *revisão*, não a revisão *por humano* (a expressão saiu do
     texto); vale só para decisão *unicamente* automatizada; a lei não define "discriminatório".
     *(Explicabilidade técnica em profundidade: Aula 8.)*
   - (h) *Responsabilização* (arts. 37–44, 50, 52, 55-J): registro de operações, RIPD, dano moral
     e coletivo, inversão do ônus da prova (art. 42, §2º), governança e boas práticas, sanções (multa
     de até 2% do faturamento, limitada a R$ 50 milhões por infração), ANPD (art. 55-J).
   - **Pausa Ativa 4:** banco nega crédito por modelo automatizado; o cliente pede explicação.
     O que o art. 20 exige, o que o art. 19, II acrescenta, o que acontece se a empresa invocar
     segredo comercial, e o que **não** está garantido.

7. **Bloco 5 — Corrigir o Modelo ou Corrigir a Coleta?** (~5 min) — Varshney §4.3.6, §4.4.
   - "Alguns vieses podem ser superados coletando dados melhores ou refazendo a preparação;
     outros passam e viram incerteza epistêmica na modelagem" (o livro trata disso adiante).
     **Se todo o dado relevante é enviesado demais, a conversa é se o projeto deve prosseguir.**
   - "Nenhum conjunto de dados é completamente livre de viés": auditoria antes de treino. O
     checklist de cinco perguntas de Varshney vira o **roteiro de auditoria** que o aluno leva.
   - Ponte: *como medir a disparidade resultante, e o que fazer com ela, é o tema de uma aula
     seguinte (fairness)* — apenas anunciar, sem antecipar métricas.

8. **Fechamento e Ponte para a Aula 7** (~6 min)
   - Responder as 4 perguntas do roteiro em uma frase cada.
   - **Em aberto:** medir disparidade (aula futura sobre fairness); explicabilidade técnica
     (Aula 8); a lacuna da segurança pública.
   - **Gancho:** dados coletados, rotulados, limpos, guardados e reprocessados têm custo
     material — qual é o custo energético e ambiental dessa infraestrutura? (Aula 7.)

**Diagramas TikZ planejados:** (1) os quatro espaços com as passagens e os vieses associados;
(2) o laço de retroalimentação do policiamento preditivo (marcado como extensão); (3) mapa
"princípio da LGPD × tipo de viés".

---

> **Nota (2026-09-21, revisão pós-pedido):** a parte de *k*-anonimato, privacidade diferencial e demais técnicas de anonimização (Fonte 11, e o trecho de Fonte 10 sobre desenho do TraceBridge além de consentimento/poder) **saiu da aula** a pedido do usuário; a LGPD passou a focar nos **princípios do art. 6º** e, depois, nos pontos de maior peso (consentimento, dados sensíveis, art. 20, responsabilização). A Fonte 11 permanece abaixo apenas como registro.

> **Nota (2026-09-21, 2ª revisão):** o Bloco 2 (Proxies, Atributos Protegidos e a Falsa Cegueira), com a Pausa Ativa 3 original, foi **removido** a pedido do usuário por já estar coberto (Aula 5 e a seção de anatomia do viés). A aula final tem 5 Pausas Ativas; a antiga numeração de blocos deste plano não se aplica mais.

## Fontes usadas — Aula 6

> Trechos **literais na língua original** (inglês para Varshney; português para a LGPD). A
> tradução para português acontece só no `index.qmd` (Etapa 3). **Paginação de Varshney:** foi
> conferida contra o cabeçalho de página do PDF (não contra o sumário do livro, que está
> deslocado em relação a alguns capítulos). Para a LGPD cita-se artigo/parágrafo/inciso.

### Fonte 1: Varshney (2022), cap. 4, p. 41
**Uso pretendido:** tese da aula — auditar viés é anterior à modelagem; possibilidade de não prosseguir.

**Trecho:**
> "Appraising data sets for biases is critical for trustworthiness and is the primary focus of the
> chapter. The better job done at this stage, the less correction and mitigation of harms needs to
> be done in later stages of the lifecycle. Bias evaluation should include input from affected
> individuals of the planned machine learning system. If all possible relevant data is deemed too
> biased, a conversation with the problem owner and other stakeholders on whether to even proceed
> with the project is a must."

---

### Fonte 2: Varshney (2022), cap. 4, §4.1, pp. 42–43
**Uso pretendido:** modalidades, e a diferença de onde auditar em dados estruturados × semiestruturados.

**Trecho (p. 42):**
> "Although tabular data might look official, pristine, and flawless at first glance due to its nice
> structure, it can hide all sorts of false assumptions, errors, omissions, and biases."

**Trecho (p. 43):**
> "Any biases present in the very large background datasets carry over to models fine-tuned on a
> problem-specific dataset because of the originally opaque and uncontrollable representation
> learning leading to the foundation model. As such, with semi-structured data, it is important
> that you not only evaluate the problem-specific dataset, but also the background dataset. With
> structured datasets, it is more critical that you analyze data preparation and feature
> engineering."

---

### Fonte 3: Varshney (2022), cap. 4, §4.2.1–4.2.2, p. 44
**Uso pretendido:** "a maior parte do dado é reaproveitada"; dado administrativo e desencontro entre o rótulo desejado e o proxy disponível.

**Trecho (§4.2.1):**
> "You may think that most data used in creating machine learning systems is expressly and
> carefully collected for the purpose of the problem, but you would be blissfully wrong. In fact,
> most data used in machine learning systems is repurposed."

**Trecho (§4.2.2):**
> "The most important thing for you to be aware of with administrative data is that it might not
> exactly match the predictive problem you are trying to solve. The machine learning problem
> specification may ask for a certain label, but the administrative data may contain columns that
> can only be proxies for that desired label. This mismatch can be devastating for certain
> individuals and groups, even if it is a decent proxy on average."

---

### Fonte 4: Varshney (2022), cap. 4, §4.2.3–4.2.4, p. 45
**Uso pretendido:** dado social (participação desigual nas plataformas) e *crowdsourcing* (contexto do rotulador).

**Trecho (§4.2.3):**
> "Also, there can be large amounts of sampling biases because not all populations participate in
> social platforms to the same extent. In particular, marginalized populations may be invisible in
> some types of social data."

**Trecho (§4.2.4):**
> "They may be unfamiliar with the task or the social context of the task, which may yield biases
> in labels. For example, crowd workers may not have the context to know what constitutes a
> household in rural East Africa and may thus introduce biases in roof labeling."

---

### Fonte 5: Varshney (2022), cap. 4, §4.3 e Figura 4.3, pp. 46–47
**Uso pretendido:** o modelo dos quatro espaços, três validades e cinco vieses (esqueleto do Bloco 1).

**Trecho (legenda da Fig. 4.3, p. 46):**
> "A sequence of four spaces, each represented as a cloud. The construct space leads to the
> observed space via the measurement process. The observed space leads to the raw data space via
> the sampling process. The raw data space leads to the prepared data space via the data
> preparation process. The measurement process contains social bias, which threatens construct
> validity. The sampling process contains representation bias and temporal bias, which threatens
> external validity. The data preparation process contains data preparation bias and data
> poisoning, which threaten internal validity."

**Trecho (p. 47):**
> "There are three main kinds of validity: (1) construct validity, (2) external validity, and (3)
> internal validity. Construct validity is whether the data really measures what it ought to
> measure. External validity is whether analyzing data from a given population generalizes to
> other populations. Internal validity is whether there are any errors in the data processing."

> "The construct space is an abstract, unobserved, theoretical space in which there are no
> biases."

---

### Fonte 6: Varshney (2022), cap. 4, §4.3.1 (Viés social), p. 47
**Uso pretendido:** viés social nos rótulos e nos atributos; caso dos telhados.

**Trecho:**
> "Whether it is experts whose decision making is being automated or it is crowd workers, people's
> judgement is involved in going from labels in the construct space to labels in the observed
> space. These human judgements are subject to human cognitive biases which can lead to implicit
> social biases (associating stereotypes towards categories of people without conscious awareness)
> that yield systematic disadvantages to unprivileged individuals and groups."

> "If an aptitude test asks questions that rely on specific cultural knowledge that not all
> test-takers have, then the feature will not, in fact, be a good representation of the
> test-taker's underlying aptitude. And most of the time, this tacit knowledge will favor
> privileged groups."

> "The crowd workers had marked and labeled not only the roof of the main house of a household
> compound, but also separate structures of the same household such as a free-standing kitchen and
> free-standing sleeping quarters for young men. They had no idea that this is how households are
> laid out in this part of the world. The bias, if not caught, would have led to incorrect
> inferences of poverty."

---

### Fonte 7: Varshney (2022), cap. 4, §4.3.2–4.3.3, p. 48
**Uso pretendido:** viés de representação e viés temporal.

**Trecho (representação):**
> "A specific example of selection bias is unprivileged groups being either underrepresented or
> overrepresented in the dataset, which leads to machine learning models either ignoring their
> special characteristics to satisfy an average performance metric or focusing too much on them
> leading to systematic disadvantage. Upon appraisal of one of Unconditionally's mobile phone
> datasets, the data engineers found that senior citizens were underrepresented because mobile
> phone ownership was lower in that subpopulation."

> "Representativeness is not only a question of the presence and absence of data points, but is a
> broader concept that includes, among others, systematic differences in data quality."

**Trecho (temporal):**
> "Covariate shift refers to the distribution of the features, prior probability shift refers to
> the distribution of the labels, and concept drift refers to the conditional distribution of the
> labels given the features."

---

### Fonte 8: Varshney (2022), cap. 4, §4.3.4–4.3.5, pp. 48–49
**Uso pretendido:** viés de preparação (linhas descartadas, proxies em rótulos) e envenenamento.

**Trecho (§4.3.4):**
> "For example, the data engineers on your team must do something to rows containing missing
> values. If they follow the common practice of dropping these rows and the missingness is
> correlated with a sensitive feature, like a debt feature being missing more often for certain
> religious groups, they have introduced a new bias."

> "A sometimes overlooked bias is the use of proxies in the labels. For example, arrests are a
> problematic proxy for committing crimes. Innocent people are sometimes arrested and more arrests
> happen where there is more police presence (and police are deployed unevenly). Health care
> utilization is a problematic proxy for an individual's health status because groups utilize
> health care systems unevenly."

**Trecho (§4.3.5):**
> "For example, someone trying to swindle Unconditionally might introduce satellite images of
> households next to rivers always labeled as severe poverty to trick your model into giving more
> cash transfers to riverside communities."

---

### Fonte 9: Varshney (2022), cap. 4, §4.3.6 e §4.4, pp. 49–50
**Uso pretendido:** o checklist de auditoria e a ideia de "corrigir a coleta antes do modelo".

**Trecho (§4.3.6):**
> "The mental model of biases provides you with a checklist to go through before using a dataset
> to train a machine learning model. Have you evaluated social biases? Is your dataset
> representative? Could there be any temporal dataset shifts over time? Have any data preparation
> steps accidently introduced any subtle biases? Has someone snuck in, accessed the data, and
> changed it for their malicious purpose?"

> "What should you do if any bias is found? Some biases can be overcome by collecting better data
> or redoing preparation steps better. Some biases will slip through and contribute to epistemic
> uncertainty in the modeling phase of the machine learning lifecycle."

**Trecho (§4.4, p. 50):**
> "No matter how careful one is, there is no completely unbiased dataset. Nevertheless, the more
> effort put in to catching and fixing biases before modeling, the better."

---

### Fonte 10: Varshney (2022), cap. 5, §5.1, pp. 52–53 (a passagem "In a broad sense…" atravessa a virada da p. 52 para a p. 53)
**Uso pretendido:** consentimento, poder e privacidade no caso TraceBridge; "dado é poder"; dado reaproveitado sem consentimento.

**Trecho (p. 52):**
> "The employer holds all the power in the deployment of the app because it can require the usage
> of the app as a condition of employment without any opportunity for the employee to give
> consent. Employees also have no opportunity to provide informed consent to the use of specific
> parts of their data."

**Trecho (p. 53):**
> "In a broad sense, data is a valuable commodity. It reveals a lot about human behavior at a gross
> level, but also about the behavior of individual people. Just like other natural resources, it
> can be extracted from the vulnerable without their consent and furthermore be exploited for
> their subjugation. [...] In short, data is power."

> "Data used in machine learning is often fraught with power and consent issues because it is
> often repurposed from other uses or is so-called data exhaust: byproducts from people's digital
> activities. For example, many large-scale image datasets used for training computer vision
> models are scraped from the internet without explicit consent from the people who posted the
> images."

> "In summary, problem owners and data scientists should not have any calculus to weigh issues of
> power, consent and privacy against conveniences in data collection. For the fourth attribute of
> trust (aligned purpose), trustworthy machine learning systems require that data be used
> consensually, especially from those who could be subject to exploitation. No ifs, ands, or buts!"

---

### Fonte 11: Varshney (2022), cap. 5, §5.2, pp. 54–56
**Uso pretendido:** identificadores, quase-identificadores, atributos sensíveis; *k*-anonimato e seus ataques.

**Trecho (p. 54):**
> "There are three main categories of variables when dealing with privacy: (1) identifiers, (2)
> quasi-identifiers, and (3) sensitive attributes. Identifiers directly reveal the identity of a
> person. [...] Identifiers should be dropped from a dataset to achieve privacy, but such dropping
> is not the entire solution. In contrast, quasi-identifiers do not uniquely identify people on
> their own, but can reveal identity when linked together through a process known as
> re-identification. Examples are gender, birth date, postal code, and group membership."

**Trecho (p. 56):**
> "By means of suppressing values of quasi-identifiers (replacing the value with a null value) or
> generalizing their values (for example replacing 5-digit zip codes with only their first three
> digits), the idea of k-anonymity is to create groups of records of cardinality at least k that
> have exactly the same modified quasi-identifier values."

> "Weaknesses of k-anonymity include susceptibility to the homogeneity attack and the background
> knowledge attack. The homogeneity attack takes advantage of many records within a k-member
> cluster having the same sensitive attributes, which means that even without precise
> re-identification, the sensitive information of individuals is still revealed."

**Trecho (p. 58, privacidade × utilidade):**
> "We've reached the end of this section and haven't talked about the tradeoff of privacy with
> utility. All measures and approaches of providing privacy should be evaluated in conjunction
> with how the data is going to be used."

---

### Fonte 12: Varshney (2022), cap. 10, §10.1, pp. 131–132
**Uso pretendido:** só vocabulário — justiça distributiva, grupos privilegiados, atributos protegidos definidos por lei (**sem** entrar em métricas).

**Trecho (p. 131):**
> "Privileged groups and individuals are defined to be those who have historically been more likely
> to receive the favorable label in a machine learning binary classification task. Receiving care
> management is a favorable label because patients are given extra services to keep them healthy.
> Other favorable labels include being hired, not being fired, being approved for a loan, not being
> arrested, and being granted bail."

**Trecho (p. 132):**
> "There is no one universal set of protected attributes. They are determined from laws,
> regulations, or other policies governing a particular application domain in a particular
> jurisdiction."

---

### Fonte 13: Varshney (2022), cap. 10, §10.2, pp. 132–134
**Uso pretendido:** a seguradora dissecada; onde o viés entra na medição, amostragem e preparação; "o dado de treino é a sociedade".

**Trecho (p. 133):**
> "While it is directionally true that greater health care utilization implies a sicker patient, it
> is not true when comparing patients across populations such as whites and blacks. Blacks tend to
> be sicker for an equal level of utilization due to structural issues in the health care system.
> The same is true when looking at health care cost instead of utilization."

> "Representation bias enters claims data because it is only from Sospital's own members. This
> population may, for example, undersample blacks if Sospital offers its commercial plans
> primarily in counties with larger white populations."

**Trecho (p. 132, epígrafe):**
> "If humans didn't behave the way we do there would be no behavior data to correct. The training
> data is society." — M. C. Hammer

**Trecho (p. 134):**
> "In fairness, there are precise policy-driven notions and quantitative criteria that define the
> desired state of data and/or models that are not dependent on the data distribution you have."
>
> *(usado só para **anunciar** que a especificação quantitativa vem numa aula futura)*

---

### Fonte 14: LGPD (Lei nº 13.709/2018, texto compilado), arts. 1º–2º, 4º
**Uso pretendido:** objeto, fundamentos e as exclusões que importam (segurança pública; fins acadêmicos).

**Trecho:**
> "Art. 1º Esta Lei dispõe sobre o tratamento de dados pessoais, inclusive nos meios digitais, por
> pessoa natural ou por pessoa jurídica de direito público ou privado, com o objetivo de proteger
> os direitos fundamentais de liberdade e de privacidade e o livre desenvolvimento da
> personalidade da pessoa natural."

> "Art. 2º A disciplina da proteção de dados pessoais tem como fundamentos: I - o respeito à
> privacidade; II - a autodeterminação informativa; [...] VII - os direitos humanos, o livre
> desenvolvimento da personalidade, a dignidade e o exercício da cidadania pelas pessoas naturais."

> "Art. 4º Esta Lei não se aplica ao tratamento de dados pessoais: [...] III - realizado para fins
> exclusivos de: a) segurança pública; b) defesa nacional; c) segurança do Estado; ou d)
> atividades de investigação e repressão de infrações penais; [...]
> § 1º O tratamento de dados pessoais previsto no inciso III será regido por legislação
> específica, que deverá prever medidas proporcionais e estritamente necessárias ao atendimento do
> interesse público, observados o devido processo legal, os princípios gerais de proteção e os
> direitos do titular previstos nesta Lei."

---

### Fonte 15: LGPD, art. 5º (definições)
**Uso pretendido:** vocabulário jurídico da aula.

**Trecho:**
> "I - dado pessoal: informação relacionada a pessoa natural identificada ou identificável;
> II - dado pessoal sensível: dado pessoal sobre origem racial ou étnica, convicção religiosa,
> opinião política, filiação a sindicato ou a organização de caráter religioso, filosófico ou
> político, dado referente à saúde ou à vida sexual, dado genético ou biométrico, quando vinculado
> a uma pessoa natural;
> III - dado anonimizado: dado relativo a titular que não possa ser identificado, considerando a
> utilização de meios técnicos razoáveis e disponíveis na ocasião de seu tratamento; [...]
> XI - anonimização: utilização de meios técnicos razoáveis e disponíveis no momento do
> tratamento, por meio dos quais um dado perde a possibilidade de associação, direta ou indireta,
> a um indivíduo; [...]
> XII - consentimento: manifestação livre, informada e inequívoca pela qual o titular concorda com
> o tratamento de seus dados pessoais para uma finalidade determinada; [...]
> XVII - relatório de impacto à proteção de dados pessoais: documentação do controlador que contém
> a descrição dos processos de tratamento de dados pessoais que podem gerar riscos às liberdades
> civis e aos direitos fundamentais, bem como medidas, salvaguardas e mecanismos de mitigação de
> risco;"

---

### Fonte 16: LGPD, art. 6º (princípios)
**Uso pretendido:** tabela "princípio × viés" (núcleo do Bloco 4).

**Trecho:**
> "Art. 6º As atividades de tratamento de dados pessoais deverão observar a boa-fé e os seguintes
> princípios:
> I - finalidade: realização do tratamento para propósitos legítimos, específicos, explícitos e
> informados ao titular, sem possibilidade de tratamento posterior de forma incompatível com essas
> finalidades;
> II - adequação: compatibilidade do tratamento com as finalidades informadas ao titular, de
> acordo com o contexto do tratamento;
> III - necessidade: limitação do tratamento ao mínimo necessário para a realização de suas
> finalidades, com abrangência dos dados pertinentes, proporcionais e não excessivos em relação às
> finalidades do tratamento de dados; [...]
> V - qualidade dos dados: garantia, aos titulares, de exatidão, clareza, relevância e atualização
> dos dados, de acordo com a necessidade e para o cumprimento da finalidade de seu tratamento;
> VI - transparência: garantia, aos titulares, de informações claras, precisas e facilmente
> acessíveis sobre a realização do tratamento e os respectivos agentes de tratamento, observados os
> segredos comercial e industrial; [...]
> VIII - prevenção: adoção de medidas para prevenir a ocorrência de danos em virtude do tratamento
> de dados pessoais;
> IX - não discriminação: impossibilidade de realização do tratamento para fins discriminatórios
> ilícitos ou abusivos;
> X - responsabilização e prestação de contas: demonstração, pelo agente, da adoção de medidas
> eficazes e capazes de comprovar a observância e o cumprimento das normas de proteção de dados
> pessoais e, inclusive, da eficácia dessas medidas."

---

### Fonte 17: LGPD, arts. 7º–9º (bases legais e consentimento)
**Uso pretendido:** exigências do consentimento; ônus da prova; nulidade; retomada de *dark patterns*.

**Trecho:**
> "Art. 8º [...] § 2º Cabe ao controlador o ônus da prova de que o consentimento foi obtido em
> conformidade com o disposto nesta Lei.
> § 3º É vedado o tratamento de dados pessoais mediante vício de consentimento.
> § 4º O consentimento deverá referir-se a finalidades determinadas, e as autorizações genéricas
> para o tratamento de dados pessoais serão nulas.
> § 5º O consentimento pode ser revogado a qualquer momento mediante manifestação expressa do
> titular, por procedimento gratuito e facilitado, [...]"

> "Art. 9º [...] § 1º Na hipótese em que o consentimento é requerido, esse será considerado nulo
> caso as informações fornecidas ao titular tenham conteúdo enganoso ou abusivo ou não tenham sido
> apresentadas previamente com transparência, de forma clara e inequívoca."

---

### Fonte 18: LGPD, art. 11 (dados pessoais sensíveis)
**Uso pretendido:** proteção reforçada; §1º (revelar dado sensível); §5º (planos de saúde e seleção de riscos).

**Trecho:**
> "Art. 11. O tratamento de dados pessoais sensíveis somente poderá ocorrer nas seguintes
> hipóteses: I - quando o titular ou seu responsável legal consentir, de forma específica e
> destacada, para finalidades específicas; II - sem fornecimento de consentimento do titular, nas
> hipóteses em que for indispensável para: [...]
> § 1º Aplica-se o disposto neste artigo a qualquer tratamento de dados pessoais que revele dados
> pessoais sensíveis e que possa causar dano ao titular, ressalvado o disposto em legislação
> específica. [...]
> § 5º É vedado às operadoras de planos privados de assistência à saúde o tratamento de dados de
> saúde para a prática de seleção de riscos na contratação de qualquer modalidade, assim como na
> contratação e exclusão de beneficiários."

---

### Fonte 19: LGPD, art. 12 (anonimização)
**Uso pretendido:** limite da anonimização; perfil comportamental; ponte com *k*-anonimato.

**Trecho:**
> "Art. 12. Os dados anonimizados não serão considerados dados pessoais para os fins desta Lei,
> salvo quando o processo de anonimização ao qual foram submetidos for revertido, utilizando
> exclusivamente meios próprios, ou quando, com esforços razoáveis, puder ser revertido.
> § 1º A determinação do que seja razoável deve levar em consideração fatores objetivos, tais como
> custo e tempo necessários para reverter o processo de anonimização, de acordo com as tecnologias
> disponíveis, e a utilização exclusiva de meios próprios.
> § 2º Poderão ser igualmente considerados como dados pessoais, para os fins desta Lei, aqueles
> utilizados para formação do perfil comportamental de determinada pessoa natural, se
> identificada."

---

### Fonte 20: LGPD, arts. 18–21 (direitos do titular e decisões automatizadas)
**Uso pretendido:** o que o titular pode exigir; art. 20 lido com o histórico de redações visível no PDF (original: "por pessoa natural"; §3º vetado).

**Trecho:**
> "Art. 18. O titular dos dados pessoais tem direito a obter do controlador, em relação aos dados
> do titular por ele tratados, a qualquer momento e mediante requisição: I - confirmação da
> existência de tratamento; II - acesso aos dados; III - correção de dados incompletos, inexatos
> ou desatualizados; IV - anonimização, bloqueio ou eliminação de dados desnecessários, excessivos
> ou tratados em desconformidade com o disposto nesta Lei; [...]"

> "Art. 19. [...] II - por meio de declaração clara e completa, que indique a origem dos dados, a
> inexistência de registro, os critérios utilizados e a finalidade do tratamento, observados os
> segredos comercial e industrial, fornecida no prazo de até 15 (quinze) dias, contado da data do
> requerimento do titular."

> Redação original do art. 20 (visível no PDF): "O titular dos dados tem direito a solicitar
> revisão, por pessoa natural, de decisões tomadas unicamente com base em tratamento automatizado
> de dados pessoais que afetem seus interesses, inclusive de decisões destinadas a definir o seu
> perfil pessoal, profissional, de consumo e de crédito ou os aspectos de sua personalidade."

> Redação vigente (Lei nº 13.853/2019): "Art. 20. O titular dos dados tem direito a solicitar a
> revisão de decisões tomadas unicamente com base em tratamento automatizado de dados pessoais que
> afetem seus interesses, incluídas as decisões destinadas a definir o seu perfil pessoal,
> profissional, de consumo e de crédito ou os aspectos de sua personalidade.
> § 1º O controlador deverá fornecer, sempre que solicitadas, informações claras e adequadas a
> respeito dos critérios e dos procedimentos utilizados para a decisão automatizada, observados os
> segredos comercial e industrial.
> § 2º Em caso de não oferecimento de informações de que trata o § 1º deste artigo baseado na
> observância de segredo comercial e industrial, a autoridade nacional poderá realizar auditoria
> para verificação de aspectos discriminatórios em tratamento automatizado de dados pessoais.
> § 3º (VETADO)."

> "Art. 21. Os dados pessoais referentes ao exercício regular de direitos pelo titular não podem
> ser utilizados em seu prejuízo."

---

### Fonte 21: LGPD, arts. 38, 42, 44, 50, 52 e 55-J (responsabilização e fiscalização)
**Uso pretendido:** o lado da conta — relatório de impacto, dano, inversão do ônus da prova, governança, sanções, ANPD.

**Trecho:**
> "Art. 38. A autoridade nacional poderá determinar ao controlador que elabore relatório de impacto
> à proteção de dados pessoais, inclusive de dados sensíveis, referente a suas operações de
> tratamento de dados, nos termos de regulamento, observados os segredos comercial e industrial."

> "Art. 42. O controlador ou o operador que, em razão do exercício de atividade de tratamento de
> dados pessoais, causar a outrem dano patrimonial, moral, individual ou coletivo, em violação à
> legislação de proteção de dados pessoais, é obrigado a repará-lo. [...] § 2º O juiz, no processo
> civil, poderá inverter o ônus da prova a favor do titular dos dados quando, a seu juízo, for
> verossímil a alegação, houver hipossuficiência para fins de produção de prova ou quando a
> produção de prova pelo titular resultar-lhe excessivamente onerosa."

> "Art. 44. O tratamento de dados pessoais será irregular quando deixar de observar a legislação
> ou quando não fornecer a segurança que o titular dele pode esperar, consideradas as circunstâncias
> relevantes, entre as quais: I - o modo pelo qual é realizado; II - o resultado e os riscos que
> razoavelmente dele se esperam; III - as técnicas de tratamento de dados pessoais disponíveis à
> época em que foi realizado."

> "Art. 52. [...] II - multa simples, de até 2% (dois por cento) do faturamento da pessoa jurídica
> de direito privado, grupo ou conglomerado no Brasil no seu último exercício, excluídos os
> tributos, limitada, no total, a R$ 50.000.000,00 (cinquenta milhões de reais) por infração;"

> "Art. 55-J. Compete à ANPD: I - zelar pela proteção dos dados pessoais, nos termos da
> legislação; [...] IV - fiscalizar e aplicar sanções em caso de tratamento de dados realizado em
> descumprimento à legislação, mediante processo administrativo que assegure o contraditório, a
> ampla defesa e o direito de recurso; [...]"

---

### Fontes secundárias (fora das duas fontes fornecidas) — só para casos, rotuladas na aula

- **Dastin, J. (2018), "Amazon scraps secret AI recruiting tool that showed bias against women",
  Reuters (out. 2018).** Confirmado por busca: projeto iniciado em 2014; viés percebido em 2015;
  treinado em currículos de dez anos; penalizava "women's"; encerrado por volta de 2017.
  *(Não temos o PDF em `_fontes/`; citar como reportagem, sem trecho literal — ver decisão abaixo.)*
- **Buolamwini, J. & Gebru, T. (2018), "Gender Shades", *PMLR* 81.** Confirmado por busca:
  erros de até 34,7% (mulheres de pele escura) × máx. 0,8% (homens de pele clara) em três
  classificadores comerciais; *benchmarks* de 79,6% (IJB-A) e 86,2% (Adience) de pele clara.
  *(Não temos o PDF; usar só esses números, citados como do artigo.)*

---

## Decisões que preciso que você confirme antes de eu escrever a aula (Etapa 3)

1. **Escopo:** fora *métricas de fairness* **e** fora *estratégias de mitigação algorítmica*
   (reweighing, adversarial debiasing, limiares por grupo). Correto assim?
2. **GDPR:** sem o texto no projeto, a aula só cita o que Varshney diz (p. 53) e não compara com a
   LGPD. Quer que eu compare (você traria o texto do GDPR para `_fontes/`) ou fica só LGPD?
3. **Amazon e Gender Shades:** manter como casos secundários (rotulados, sem trecho literal), ou
   cortar e ficar só com os casos das duas fontes (seguradora, ONG *Unconditionally*, TraceBridge)?
4. **Policiamento preditivo (laço de retroalimentação):** manter como extensão nossa sinalizada,
   ou cortar (o livro só diz que "prisões são um proxy problemático")?
5. **Leitura recomendada no `../index.qmd`** (Lesson 6) hoje aponta Steen (cap. 2) e Maciel &
   Viterbo (vol. 2, cap. 10). Proponho **substituir** por Varshney caps. 4, 5 e §§10.1–10.2, mais
   a LGPD (Lei nº 13.709/2018) — mostrarei o trecho exato e só aplico com sua confirmação (regra do
   `CLAUDE.md`).
6. **Fluxo:** quer conferir as etapas intermediárias, ou posso ir direto para o `index.qmd`
   completo, `exercicios.qmd`, `soluções.qmd` e `_02-respostas-pausas.md` depois de aprovar este
   plano?
