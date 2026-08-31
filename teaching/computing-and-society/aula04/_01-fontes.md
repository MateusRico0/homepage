# Fontes usadas — Aula 4

> Trechos literais extraídos lendo diretamente as páginas do PDF (não
> reescritos de memória).
>
> - `../_fontes/conway1968.pdf`: artigo completo (4 páginas, Datamation,
>   abril de 1968) — baixado diretamente do site oficial do autor
>   (melconway.com/Home/pdf/committees.pdf) e symlinkado em `_fontes/`.
>   Numeração impressa da revista = numeração do PDF (offset 0); o
>   artigo em si vai das pp. 28 a 31.
> - `../_fontes/datafeminism_cap2.pdf`: Cap. 2 de *Data Feminism*
>   (D'Ignazio & Klein, 2020) — edição de acesso aberto publicada pela
>   MIT Press (financiada pelo MIT Libraries Experimental Collections
>   Fund, sem paywall), baixada de um mirror legítimo hospedado por um
>   curso da Rutgers University (`sites.rutgers.edu/critical-ai/`) e
>   symlinkada em `_fontes/`. Numeração impressa do livro = numeração do
>   PDF do capítulo extraído (offset 0; a primeira página lida já mostra
>   "50" impresso = página 2 do PDF do capítulo, ou seja, offset **+2**
>   dentro deste PDF de capítulo isolado — cuidado ao citar página: usar
>   sempre o número impresso do livro, que aparece no rodapé de cada
>   página).
> - **Marc Steen (2022), Cap. 18 "Value Sensitive Design"**
>   (`../_fontes/EthTech.pdf`, já symlinkado, offset +9 confirmado nas
>   Aulas 1–3, reconfirmado nesta sessão): lido por completo por esta
>   sessão pela primeira vez nesta disciplina — a ementa original da
>   Lesson 4 citava "Chapter 5", que não existe com esse conteúdo no
>   livro real (ver correção na Fonte 7 abaixo).
> - **⚠️ Ian Sommerville (2015/2016), *Software Engineering*, 10ª ed.,
>   Caps. 1 e 4 — SEM citação literal nesta aula.** Busquei
>   exaustivamente por uma fonte gratuita e legítima (site do autor,
>   Pearson, editoras universitárias) e não encontrei nenhuma — as
>   únicas cópias do texto completo disponíveis online (ex.: um PDF
>   hospedado em `archive.org` sob um acervo de curso de outra
>   universidade) são cópias não autorizadas do livro comercial, que
>   optei por não usar. Os blocos 2 e 4 desta aula usam os conceitos
>   amplamente documentados e consolidados desses dois capítulos
>   (camadas de um sistema sociotécnico; o processo clássico de
>   Engenharia de Requisitos em 4 etapas — elicitação, análise e
>   negociação, especificação, validação) como conhecimento geral,
>   **sinalizado explicitamente como tal no `index.qmd`**, nunca
>   misturado com citação literal — conforme a regra de precisão de
>   conteúdo do `CLAUDE.md`. Fica pendente linkar o PDF real em
>   `_fontes/` caso o usuário tenha acesso a uma cópia legítima.

---

### Fonte 1: Conway (1968), "How Do Committees Invent?", p. 31 ("systems image their design groups")

**Uso pretendido:** o exemplo concreto do compilador COBOL/ALGOL para
o Bloco 1 (Abertura) e o núcleo do Bloco 3 (Lei de Conway) — a citação
central da tese do artigo.

**Trecho:**
> "Examples. A contract research organization had eight people who were
> to produce a COBOL and an ALGOL compiler. After some initial estimates
> of difficulty and time, five people were assigned to the COBOL job and
> three to the ALGOL job. The resulting COBOL compiler ran in five
> phases, the ALGOL compiler ran in three."
>
> "Two military services were directed by their Commander-in-Chief to
> develop a common weapon system to meet their respective needs. After
> great effort they produced a copy of their organization chart."

---

### Fonte 2: Conway (1968), "How Do Committees Invent?", p. 29 ("design organization criteria")

**Uso pretendido:** premissa formal da Lei de Conway (Bloco 3) — por
que a comunicação necessária entre subsistemas força a arquitetura a
espelhar a organização.

**Trecho:**
> "Given any design team organization, there is a class of design
> alternatives which cannot be effectively pursued by such an
> organization because the necessary communication paths do not exist.
> Therefore, there is no such thing as a design group which is both
> organized and unbiased."

---

### Fonte 3: Conway (1968), "How Do Committees Invent?", p. 31 ("conclusion")

**Uso pretendido:** síntese formal da Lei de Conway, para o passo final
do passo-a-passo do Bloco 3, e a "Manobra Inversa de Conway" (implicação
prática).

**Trecho:**
> "The basic thesis of this article is that organizations which design
> systems (in the broad sense used here) are constrained to produce
> designs which are copies of the communication structures of these
> organizations. [...] Primarily, we have found a criterion for the
> structuring of design organizations: a design effort should be
> organized according to the need for communication."

---

### Fonte 4: D'Ignazio & Klein (2020), *Data Feminism*, Cap. 2, p. 53

**Uso pretendido:** núcleo do Bloco 4 (elicitação de requisitos como
processo social) — a citação central de que dados/requisitos nunca são
neutros ou "crus".

**Trecho:**
> "Data are always the product of unequal social relations — relations
> affected by centuries of history. As computer scientist Ben Green
> states, 'Although most people talk about machine learning's ability to
> predict the future, what it really does is predict the past.'"

---

### Fonte 5: D'Ignazio & Klein (2020), *Data Feminism*, Cap. 2, p. 53

**Uso pretendido:** definição dos "quatro pontos de partida" do
capítulo — usada para estruturar a ponte entre o Bloco 3 (Conway) e o
Bloco 4 (requisitos), e o próprio bloco 4 (o ponto "Collect").

**Trecho:**
> "Taking action can itself take many forms, and in this chapter we
> offer four starting points: (1) Collect: Compiling counterdata—in the
> face of missing data or institutional neglect—offers a powerful
> starting point [...]. (2) Analyze: Challenging power often requires
> demonstrating inequitable outcomes across groups, and new
> computational methods are being developed to audit opaque algorithms
> and hold institutions accountable. (3) Imagine: We cannot only focus on
> inequitable outcomes, because then we will never get to the root cause
> of injustice. [...] (4) Teach: The identities of data scientists
> matter, so how might we engage and empower newcomers to the field
> [...]?"

---

### Fonte 6: D'Ignazio & Klein (2020), *Data Feminism*, Cap. 2, pp. 49–50 (caso DGEI)

**Uso pretendido:** caso concreto para ilustrar "quem constrói o mapa
de requisitos decide o que existe e o que fica de fora" (Bloco 4) — o
caso do Detroit Geographic Expedition and Institute (DGEI), 1971.

**Trecho:**
> "In 1971, the Detroit Geographic Expedition and Institute (DGEI)
> released a provocative map, *Where Commuters Run Over Black Children
> on the Pointes-Downtown Track*. [...] The people who lived along the
> deadly route had long recognized the magnitude of the problem, as well
> as its profound impact on the lives of their friends and neighbors.
> But gathering data in support of this truth turned out to be a major
> challenge. No one was keeping detailed records of these deaths, nor
> was anyone making even more basic information about what had happened
> publicly available. 'We couldn't get that information,' explains
> Gwendolyn Warren, the Detroit-based organizer who headed the unlikely
> collaboration."

---

### Fonte 7: Steen (2022), Cap. 18, "Value Sensitive Design", pp. 154–156

**Correção da ementa:** a Lesson 4 do `index.qmd` (texto fornecido pelo
usuário) cita "Chapter 5: Value Sensitive Design and Responsible
Innovation" — esse título não corresponde à estrutura real do livro
(confirmado no sumário, PDF pp. 8–9 impressas): Value Sensitive Design
é o **Capítulo 18** (p. 154) e Responsible Innovation é o **Capítulo
19** (p. 162), dois capítulos distintos, não um "Capítulo 5" único —
mesmo padrão de citação a corrigir já visto nas Lessons 1 e 2 do
`../index.qmd` (ex.: "Chapter 6: Ethical Reflection, Inquiry, and
Deliberation" corrigido para o Cap. 16 real). Nenhuma leitura deste
capítulo tinha sido feita ainda nesta disciplina; excertos extraídos
nesta sessão.

**Uso pretendido:** ponte do Bloco 5 (de compromisso ético a artefato
de engenharia concreto) — a ligação literal entre "investigação
empírica de valores" e "requisito (tentativo) do sistema" é exatamente
o passo que o Bloco 5 formaliza com um exemplo guiado (NFR → ADR →
gate de CI).

**Trecho:**
> "*Value Sensitive Design* (VSD) puts values centre stage. It is a
> method that enables people to explicitly discuss, explore, and
> negotiate values, carefully and systematically. VSD aims to enable
> diverse stakeholders to express their values and to combine these
> productively during the innovation process." (p. 154)
>
> "A complete version of VSD consists of three types of investigations,
> which can be combined in an iterative process: empirical, conceptual,
> and technological investigations. *Empirical investigations* involve
> studying the values that are at play in a particular project, for
> example, by conducting interviews or workshops with relevant
> stakeholders. [...] These investigations result in (tentative)
> requirements for the system that is being developed." (pp. 155–156)
