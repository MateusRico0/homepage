## Resumo — Aula 5: Understanding and Steering Users — Qualitative Research, A/B Testing, and Persuasive Technology

As Aulas 1–4 tratam sistemas de software como prática sociotécnica: o
mapa de atores (Aula 1), a ética normativa e o Ciclo Ético (Aula 2), a
responsabilidade profissional e os códigos de conduta (Aula 3), e — na
aula imediatamente anterior — os mecanismos estruturais (Lei de Conway,
elicitação de requisitos) e o mecanismo *deliberado* (Bloco 5 da Aula 4,
*dark patterns*) pelos quais o processo de construção de software deixa
marca, boa ou má, no resultado final. A Aula 4 fechou mostrando que a
fricção que o usuário sente pode nascer de ausência estrutural (Blocos
3–4) ou de presença deliberada (Bloco 5) — mas nunca explicou **com que
ferramentas concretas** uma equipe de produto decide, no dia a dia, o
que construir e como avaliar se "funcionou". Esta aula assume esse
degrau que faltava: apresenta o **kit de ferramentas metodológico** que
sustenta qualquer decisão de produto digital — pesquisa qualitativa
(entrevistas, *contextual inquiry*, teste de usabilidade/*think-aloud*)
e experimentação quantitativa (teste A/B, métricas de funil e
engajamento) — e mostra que esse mesmo kit é estruturalmente de **duplo
uso**: pode servir para entender genuinamente o usuário, ou para
desenhar o comportamento dele a favor de uma métrica de negócio, contra
o próprio interesse do usuário. A aula ancora essa bifurcação em dois
pontos: o *framework* de captologia de B.J. Fogg (2003) — computadores
desenhados deliberadamente para mudar o que pensamos e fazemos — e o
caso Kramer, Guillory & Hancock (2014), o experimento de contágio
emocional em massa no Facebook, que é simultaneamente um exemplo
canônico do *método* (um teste A/B controlado em escala massiva) e da
*bifurcação ética* (consentimento informado, comparado às normas
acadêmicas usuais de um comitê de ética/IRB).

**Pré-requisitos:** Aula 4, Bloco 2 (mapa de papéis da indústria — em
particular o papel de "Stakeholder de negócio", que pode "vetar ou
alterar o pedido por razões que nada têm a ver com o usuário") e Bloco
5 (*dark patterns* — a taxonomia de Gray et al. 2018 e o caso
Amazon/FTC). Esta aula **não repete** essa taxonomia nem esse caso —
apenas faz uma ponte de uma frase a partir deles (ver Revisão, abaixo).
A relação entre os dois é de nível: a Aula 4 mostrou *o resultado*
(interface deliberadamente hostil); esta aula mostra *o método de
pesquisa e experimentação* que está, estruturalmente, por trás de
qualquer decisão desse tipo — seja ela a favor ou contra o usuário.

**Objetivos de aprendizagem** (do `../index.qmd`, Lesson 5, texto já
aprovado pelo usuário — tratado como contrato de escopo, não reescrito
nesta etapa):
- **Objectives:** Introduce the core methodological toolkit computing
  professionals use to study how people interact with software —
  qualitative methods (interviews, contextual inquiry, usability/
  think-aloud testing) and quantitative experimentation (A/B testing,
  funnel and engagement metrics) — and examine the double-edged nature
  of this same toolkit: it can be deployed to genuinely understand user
  needs, or to engineer user behavior toward outcomes that serve the
  product/business rather than the user (persuasive technology,
  "captology," dark patterns).
- **Expected Competencies:** Ability to design and critically evaluate
  qualitative and quantitative user-research methods (including basic
  validity concerns in A/B testing — sample size, novelty effects,
  metric gaming); ability to look at a given feature or interface and
  identify whether its instrumentation is oriented toward understanding
  the user or steering the user's behavior; ability to recognize common
  persuasive/deceptive design techniques and the ethical stakes of
  experimenting on users without their knowledge or consent.

**Leitura recomendada** (do `../index.qmd`, Lesson 5): B.J. Fogg (2003),
*Persuasive Technology: Using Computers to Change What We Think and Do*;
Kramer, Guillory & Hancock (2014), "Experimental evidence of
massive-scale emotional contagion through social networks", *PNAS*;
Harry Brignull, *Deceptive Patterns*.

**⚠️ Sobre a terceira leitura (Brignull) e a Aula 4:** a taxonomia de
*dark patterns* de Brignull cobriria o mesmo terreno já ensinado em
profundidade na Aula 4, Bloco 5 (que usa Gray et al. 2018 como fonte
primária de taxonomia, com o mesmo vocabulário — Insistência, Obstrução,
Sonegação, Interferência de Interface, Ação Forçada). Repetir essa
taxonomia aqui, a partir de uma segunda fonte, duplicaria conteúdo já
dado. Por decisão editorial desta sessão (dentro do espírito da regra
de precisão de conteúdo do `../../CLAUDE.md` — não inflar a aula com
material redundante só porque está na ementa), o `index.qmd` desta aula
usa Brignull apenas como **uma frase de ponte** de volta à Aula 4,
nunca como fonte de uma seção nova. Nenhum trecho de Brignull é citado
literalmente nesta aula.

**Fontes de acesso resolvidas nesta sessão:** diferente da Aula 4 (onde
Sommerville e Gray et al. ficaram sem citação literal por falta de
acesso), **as duas fontes centrais desta aula foram lidas por completo,
com acesso legítimo e citação literal**:
- B.J. Fogg (2003) — cópia já existente em
  `_fontes/Computação e Sociedade/IHC/Persuasive Technology_...pdf`
  (biblioteca pessoal do usuário, symlinkada via o diretório
  `_fontes/Computação e Sociedade/`). Lida a Introdução completa (pp.
  1–9), a seção "The Emergence of Captology" (p. 5), e o Capítulo 9,
  "The Ethics of Persuasive Technology" (pp. 211–218).
- Kramer, Guillory & Hancock (2014) — cópia já existente na mesma
  pasta (`_fontes/Computação e Sociedade/IHC/kramer-et-al-2014-....pdf`).
  Artigo lido **por completo** (3 páginas, PNAS, vol. 111, no. 24, pp.
  8788–8790) — o próprio artigo confirma, em seu rodapé, "Freely
  available online through the PNAS open access option", então não há
  ressalva de acesso a fazer aqui, diferente do padrão de sinalização
  usado para outras fontes desta disciplina.

## Estratégia Pedagógica

Sem rótulo formal de Estratégia A/B (convenção já estabelecida nesta
disciplina de humanidades — ver Aula 4). A lógica de progressão é:
caso motivador (retomando a fricção deliberada da Aula 4) → método
qualitativo → método quantitativo (com suas armadilhas de validade) →
o *framework* que nomeia o duplo uso (captology) → o caso mundo-real
que amarra método e ética num só exemplo (Kramer et al.) → síntese
prática (como reconhecer, na frente de uma tela, se a instrumentação
por trás dela quer entender ou dirigir você).

## Plano de aula — Aula 5 (carga horária nominal: ~75–85min)

1. **Abertura — Da Fricção Deliberada ao Método Que a Produz** (~8 min)
   — Revisão: a Aula 4 mostrou que a fricção contra o usuário pode ser
   deliberada (Bloco 5, *dark patterns*) — alguém, no papel de
   "Stakeholder de negócio", escolhe otimizar contra o interesse do
   usuário. Ideia central (Ausubel): toda decisão desse tipo — a favor
   ou contra o usuário — nasce de um **método concreto** de pesquisa e
   experimentação; hoje abrimos essa caixa-preta. Roteiro explícito (5
   perguntas, ver abaixo). Problema motivador: como uma equipe de
   produto realmente "sabe" que uma mudança de tela é boa — o que
   exatamente ela mede, e o que essa medida pode esconder? Pausa ativa
   fechando o bloco.

2. **O Kit de Ferramentas Qualitativo** (~12 min) — Entrevistas
   estruturadas/semiestruturadas; *contextual inquiry* (observar o
   usuário no próprio ambiente de uso, para capturar processos tácitos
   que ele não sabe descrever); teste de usabilidade com protocolo
   *think-aloud* (o usuário verbaliza o raciocínio enquanto usa o
   sistema, revelando pontos de confusão em tempo real). O que cada
   técnica revela que as outras não revelam — e por que nenhuma delas,
   sozinha, escala para milhões de usuários (gancho para o Bloco 3).

3. **Experimentação Quantitativa: Teste A/B e Métricas de Funil**
   (~15 min) — Mecânica de um teste A/B (grupo controle vs. grupo
   tratamento, aleatorização, variável de resposta); métricas de funil
   (taxa de conversão em cada etapa de um fluxo) e de engajamento
   (tempo de sessão, retenção). Três armadilhas reais de validade:
   tamanho de amostra e poder estatístico (um efeito real pode não ser
   detectável com poucos usuários); efeito novidade (um ganho de
   métrica pode refletir só a novidade da mudança, não seu valor real,
   e se dissipar com o tempo); *metric gaming*/problema da métrica-proxy
   (otimizar uma métrica fácil de medir pode não otimizar o objetivo
   real que ela deveria representar).

4. **Fogg e a Captologia: Quando o Método Vira Máquina de Persuasão**
   (~15 min) — B.J. Fogg (2003) define tecnologia persuasiva e cunha
   "captology" (*computers as persuasive technologies*); as seis
   vantagens que computadores têm sobre persuasores humanos (persistem,
   permitem anonimato, manipulam grandes volumes de dado, usam várias
   modalidades, escalam, podem ir a lugares que humanos não vão); as
   seis preocupações éticas únicas da tecnologia persuasiva (Cap. 9) —
   a novidade mascara a intenção persuasiva; explora a reputação
   positiva do computador; persistência proativa; controle das
   possibilidades interativas; afeta emoções sem ser afetado por elas;
   não pode assumir responsabilidade. Ponte: o mesmo kit dos Blocos 2–3
   (pesquisa qualitativa + teste A/B) é exatamente a maquinaria que a
   captologia formaliza — o Bloco 5 mostra o caso mundo-real onde essa
   maquinaria é, ao mesmo tempo, ciência e experimento em pessoas reais.

5. **O Caso Kramer, Guillory & Hancock (2014): Consentimento em Xeque**
   (~15 min) — O experimento de contágio emocional em massa no
   Facebook (N = 689.003): manipulação controlada da quantidade de
   conteúdo emocional no *News Feed*, medindo o efeito na própria
   produção de conteúdo emocional dos usuários — um teste A/B, na
   íntegra, com hipótese, grupos de controle e significância
   estatística. A bifurcação ética: os autores tratam a concordância
   com a Política de Uso de Dados do Facebook como consentimento
   informado ("constituting informed consent for this research") — bem
   diferente do consentimento informado explícito e específico exigido
   por um comitê de ética acadêmico (IRB) para pesquisa com seres
   humanos. O artigo recebeu, posteriormente, uma "Editorial Expression
   of Concern" da própria PNAS sobre exatamente esse ponto.

6. **Síntese: Entender ou Direcionar?** (~10 min) — Um checklist prático
   para ler a instrumentação por trás de uma tela: que métrica está
   sendo otimizada, e ela representa o benefício do usuário ou do
   negócio? O usuário sabe que está sendo estudado/testado? Existe uma
   saída simétrica àquela oferecida na entrada (ponte de uma frase de
   volta à Aula 4, Bloco 5, sem repetir a taxonomia)? Fecha reforçando
   que o mesmo método (A/B testing, pesquisa de usuário) não é bom nem
   mau em si — a bifurcação está na intenção e na métrica escolhida,
   não na técnica.

7. **Fechamento e Ponte para a Aula 6** (~8 min) — Retomar as cinco
   perguntas da abertura, uma frase cada. O que fica em aberto: hoje
   vimos que decisões de *método* (o que medir, como interpretar)
   mudam o comportamento do usuário — mas essa mesma lógica de "uma
   escolha aparentemente técnica tem consequência fora do código" se
   estende, na Aula 6, para um domínio bem diferente: decisões de
   arquitetura (quantos serviços, onde rodam, como escalam) têm um
   custo material e ambiental real, não só comportamental.
