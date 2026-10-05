## Resumo — Aula 7: Fairness Algorítmica — Definições, Métricas e Mitigação

A Aula 6 mostrou **de onde vêm** os vieses que uma decisão automatizada herda: os
quatro espaços de Varshney (construto, observado, bruto, preparado), os cinco
vieses (social, de representação, temporal, de preparação, de envenenamento) e
os direitos da LGPD sobre tratamento de dados — mas terminou deixando
explicitamente de fora as **métricas de fairness e as estratégias de mitigação
algorítmica**, "para a aula seguinte" (ver `../_progresso.md`, seção "Aula 6
(renumerada)"). Esta é essa aula: sai de "o dado está enviesado" para "como
medir matematicamente se uma decisão é injusta, e o que fazer a respeito".

O eixo narrativo central é a palestra do próprio professor, **"Bias is Learned,
Fairness is Taught"** (Marcos M. Raimundo, Instituto de Computação — UNICAMP),
usada com o mesmo tratamento de autenticidade autoral já estabelecido na Aula 6
com o artigo de Nascimento & Raimundo: não como mais uma citação de rodapé, mas
como o fio que atravessa a aula inteira, com nome explícito. A aula também
conecta, na síntese, com três publicações do próprio grupo de pesquisa do
professor (M²FGB, ensemble de Pareto-ótimos, fairness de longo prazo com
rótulos seletivos) — mostrando aos alunos que os conceitos formais
apresentados não são só didáticos, são pesquisa ativa acontecendo no próprio
Instituto de Computação.

**Mudança de escopo desta aula em relação à ementa atual do `../index.qmd`:**
a Lesson 7 hoje descrita lá ("Automated Decision-Making, Optimization, AI, and
Risk" — opacidade, XAI, gestão de risco) muda para **fairness algorítmica**
(definições, métricas, trade-offs, mitigação), decisão confirmada explicitamente
pelo usuário nesta sessão. Isso será refletido na Etapa 5 (atualização do
`../index.qmd`), depois de aprovada a aula — só peço confirmação do texto
exato da nova entrada antes de aplicar, como o processo já prevê.

**Estado da pasta `aula07/` encontrado nesta sessão (a limpar como parte desta
sessão):** `index.qmd` já continha um rascunho sobre Risco/XAI/Accountability,
mas informal — sem separação HTML/slides, sem citação literal de fonte, sem
TikZ, com pausas ativas fora do padrão do `../../CLAUDE.md`. Os outros quatro
arquivos da pasta (`_00-plano-aula.md` antigo, `_01-fontes.md`,
`_03-respostas-pausas.md`, `exercicios.qmd`, `soluções.qmd`) são **sobras da
Aula 6 antiga** (Scala AI City/arquitetura), duplicadas de uma renumeração —
a Aula 6 já tem sua própria cópia corrente e atualizada dessas informações em
`../aula06/`. Este plano os substitui todos.

**Pré-requisitos:** o dicionário de notações da Aula 6 (espaço do
construto/observado/bruto/preparado; vieses social/representação/temporal/
preparação/envenenamento) é pressuposto — a Revisão da Abertura o retoma, sem
reexplicar cada viés em detalhe (já coberto lá), só o suficiente para ligar
"dado enviesado" a "decisão automatizada discriminatória".

**Estratégia Pedagógica:** Estratégia A (*Outside-In*) — a própria palestra-base
já é estruturada assim (três casos reais de dano antes de qualquer formalismo:
COMPAS, Amazon, saúde), e a disciplina já usou essa estratégia com sucesso
nas Aulas 4 e 6 quando há um caso concreto rico o bastante para funcionar como
problema motivador completo.

## Plano de aula — Aula 7 (carga horária nominal: ~90–95min)

1. **Abertura — Da Origem do Viés à Decisão que Discrimina** (~10 min) —
   Revisão cuidadosa da Aula 6 (os quatro espaços e os cinco vieses de
   Varshney, em 1-2 frases cada, lembrando o porquê, não só o nome). Ideia
   central (Ausubel): até aqui, viés era um problema de *entrada* (o dado já
   vem torto); hoje ele vira um problema de *decisão* — e decisão se pode
   medir, formalizar e corrigir. Roteiro explícito (4 perguntas, ver abaixo).
   Problema motivador: os três casos reais da palestra-base — COMPAS
   (justiça criminal), Amazon (recrutamento), algoritmo de saúde — cada um
   com a métrica de dano relatada na fonte original. Pausa ativa 1.

2. **Intuição — Como uma Máquina "Aprende" uma Decisão** (~10 min) —
   O princípio de máxima verossimilhança como o motor comum por trás dos
   três casos da Abertura: $\max_f P_f(Y\mid X)$ (probabilidade condicional
   do resultado $Y$ dado a evidência $X$). Exemplo-fio: empréstimo bancário
   ($X$ = salário, dívida, posse de imóvel; $Y$ = bom/mau pagador). Sem
   código — só a leitura da fórmula e o que cada símbolo significa, no
   registro de prosa já usado nesta disciplina.

3. **O Dado Sensível $Z$ e a Falha da "Cegueira Deliberada"** (~10 min) —
   Introduz $Z$ (atributo sensível: raça, gênero etc.) como só mais um dado
   que a máquina usa se ajudar a prever $Y$. "Fairness through unawareness"
   (remover $Z$ explicitamente) falha porque o modelo reconstrói $Z$ a
   partir de proxies correlacionados (ex.: CEP) — ponte direta com o bloco
   de proxies/quase-identificadores já visto na Aula 6, agora aplicado à
   decisão, não só ao dado. Fecha com a pergunta que o próximo bloco
   responde: então como definir injustiça sem depender de "esconder" $Z$?
   Pausa ativa 2.

4. **Definindo (In)Justiça com Probabilidade: as Muitas Faces do Fairness**
   (~18 min) — Bloco mais denso, desenvolvimento matemático *principled*
   (premissa → passo a passo, sem fórmula pronta caindo do céu):
   desigualdade de injustiça individual ($P(Y{=}0\mid X, Z{=}\text{branco}) >
   P(Y{=}0\mid X, Z{=}\text{preto})$); disparidade de utilidade/*group
   fairness* ($\Delta = |\mathbb{E}[U\mid Z{=}0] - \mathbb{E}[U\mid Z{=}1]|$);
   **Paridade Demográfica** vs. **Igualdade de Oportunidade** (as duas
   equações, com a crítica de cada uma vinda diretamente da fonte); **Teorema
   da Impossibilidade** (nomeado formalmente: fora de casos muito
   restritos, é matematicamente impossível satisfazer todas as métricas de
   fairness ao mesmo tempo — escolher uma é uma escolha ética, não só
   técnica). Pausa ativa 3.

5. **Fairness Rawlsiana: Melhorando a Vida de Quem Está Pior** (~10 min) —
   Do "igualar" ao "maximizar o mínimo": o Princípio da Diferença de John
   Rawls, traduzido para linguagem de ML como um objetivo *maximin*
   ($\max_f \min_z \mathbb{E}[U\mid Z{=}z]$). Conecta com pesquisa do
   próprio grupo: **M²FGB** (Pereira, Valdrighi & Raimundo, 2025) — gradient
   boosting com termo de fairness min-max. Nota de autoria explícita, mesmo
   padrão da Aula 6.

6. **Fairness de Longo Prazo: o Problema dos Rótulos Seletivos** (~10 min) —
   Fairness estática/pontual não basta por causa de *feedback loops*:
   decisão de hoje ($t$) molda o dado de amanhã ($t{+}1$) — ex.: conceder
   um empréstimo hoje melhora o score de crédito futuro do cliente; negar
   impede esse ciclo positivo. O desafio dos **rótulos seletivos**: só
   observamos o resultado (pagou/não pagou) de quem recebeu decisão
   positiva. Conecta com **Long-term Fairness with Selective Labels**
   (Valdrighi, Valera & Raimundo, ICML 2026) — nossa contribuição para
   provar limites de discriminação mesmo sobre clientes cujo rótulo nunca
   observamos. Pausa ativa 4.

7. **Viés em Modelos de Imagem e Linguagem: Raça como Construto Social**
   (~12 min) — Dois exemplos da própria palestra: (a) *stereotipagem
   ocupacional* em modelos de linguagem (continuação de história sobre
   "cirurgiã"/"babá" e o pronome default que o modelo escolhe) e (b) a
   "brancura como padrão invisível" em legendagem de imagens — conecta
   diretamente com a pesquisa do grupo, **"When AI Describes Race?"**
   (Braz da Silva Segundo & Raimundo, 2026): modelos legendam pessoas não
   brancas explicitamente ("um homem negro sorri") mas tratam pessoas
   brancas como o padrão não marcado ("uma mulher de cabelo loiro"),
   reforçando a ideia de que outras raças são um desvio do "normal". Fecha
   nomeando que a IA não modela raça diretamente, mas o **construto social**
   aprendido dos dados — abrindo, sem aprofundar tecnicamente (fora do
   escopo desta disciplina), que esse construto pode ser localizado e
   manipulado no espaço latente do modelo. **Pendência de fonte, sinalizada
   abaixo.**

8. **Fechamento: Fairness Não É Plugin** (~10 min) — Síntese: ferramentas de
   fairness prontas ("toolkits"), aplicadas sem entendimento profundo, criam
   dívida técnica perigosa; definir fairness num contexto específico exige
   modelagem matemática rigorosa, não só debate filosófico — mas o desafio
   real é achar quem tenha o conhecimento técnico profundo *e* saiba
   colaborar com especialistas de domínio, cientistas sociais e eticistas
   para traduzir valores humanos num objetivo matemático válido (ponte para
   a tese da disciplina inteira: computação como prática sociotécnica, não
   neutra). Retomar as 4 perguntas da Abertura, uma frase cada. Ponte para a
   Aula 8: hoje vimos o risco dentro do modelo/decisão; a próxima aula muda
   de escala de novo, do algoritmo para o hardware que o sustenta — o custo
   material e energético da infraestrutura por trás de cada decisão
   automatizada que vimos hoje.

## Fontes usadas — Aula 7

### Fonte central: "Bias is Learned, Fairness is Taught" (Raimundo, 2025)

Palestra do professor desta disciplina, Instituto de Computação — UNICAMP
(`main_complete.tex`, extraído do zip `_Presentations____Fairness_is_Taught.zip`,
`_fontes/Computação e Sociedade/`). Trechos citados literalmente, em inglês
(tradução só no `index.qmd`, conforme `../../CLAUDE.md`):

**Casos reais de dano (Bloco 1):**
> "Criminal Justice (COMPAS): An algorithm used across the U.S. to predict
> recidivism was found to be twice as likely to falsely flag Black defendants
> as high-risk compared to white defendants with similar profiles."
> "Employment (Amazon): An AI recruiting tool was scrapped after it was
> discovered to be systematically penalizing resumes that included the word
> 'women's,' effectively discriminating against female candidates."
> "Healthcare: A widely used algorithm systematically underestimated the
> health needs of the sickest Black patients, leading to millions receiving
> less care than equally sick white patients."
>
> Fontes citadas na própria palestra (secundárias, sem PDF nesta sessão —
> mesmo tratamento dado ao caso Amazon na Aula 6): Angwin, Larson, Mattu &
> Kirchner (2016), "Machine Bias", *ProPublica*; Dastin (2018), "Amazon
> scraps secret AI recruiting tool that showed bias against women",
> *Reuters*; Obermeyer et al. (2019), "Dissecting racial bias in an
> algorithm used to manage the health of populations", *Science*.

**Máxima verossimilhança e exemplo do empréstimo (Bloco 2):**
> "Find the model f(x) that makes the data we've observed (X) the most
> likely." [...] "Evidence (X): A person's financial data. Salary = \$2300,
> Debt = \$5000, Owns a house [...] Outcome (Y): Will they be a good payer?"

**Dado sensível e cegueira deliberada (Bloco 3):**
> "Even if we explicitly remove Z from the data, the model can often
> reconstruct it from other correlated variables (proxies like zip code, for
> example). This is known as the failure of 'fairness through unawareness'."

**Definições de (in)justiça (Bloco 4):**
> "P(Y=0 | X, Z=white) > P(Y=0 | X, Z=black)" [...] "Δ = |E[U(Yt,At)|Z=0] −
> E[U(Yt,At)|Z=1]|" [...] "Demographic Parity: [...] Critique: Ignores
> whether individuals are actually qualified." [...] "Equal Opportunity:
> [...] Critique: Says nothing about how unqualified people are treated."
> [...] "Except in highly constrained cases, it is mathematically impossible
> to satisfy all major fairness metrics simultaneously."

**Fairness Rawlsiana (Bloco 5):**
> "Social and economic inequalities are to be arranged so that they are...
> to the greatest benefit of the least-advantaged members of society."
> (John Rawls, citado na palestra) [...] "max_f (min_z E[U | Z=z])"

**Fairness de longo prazo (Bloco 6):**
> "Decisions made today (t) affect the data of tomorrow (t+1)." [...]
> "Challenge of Selective Labels: We only see the outcome (e.g., loan
> repayment) for those who received a positive decision."

**Viés em imagem/linguagem e raça como construto (Bloco 7):**
> "The model is statistically more likely to continue the story using
> masculine pronouns ('He...')" [prompt sobre cirurgião] [...] "they will
> describe a white person simply as 'a woman with blonde hair,' treating
> whiteness as the invisible norm." [...] "AI don't model race directly but
> the social construct learned from data."

**Fechamento (Bloco 8):**
> "Fairness is not a plugin. Simply applying off-the-shelf 'fairness
> toolkits' without deep understanding creates a dangerous technical debt."
> [...] "The critical challenge is finding experts who possess this deep
> technical knowledge and can effectively collaborate with domain experts,
> social scientists, and ethicists."

**Uso pretendido:** eixo narrativo de toda a aula — cada bloco do plano acima
usa um trecho específico como base, traduzido no `index.qmd`.

---

### Fonte 2: M²FGB — Pereira, Valdrighi & Raimundo (2025)

"M²FGB: A Min-Max Gradient Boosting Framework for Subgroup Fairness",
*Proceedings of the 2025 ACM Conference on Fairness, Accountability, and
Transparency* (`publications/group/m2fgb-...qmd`, já publicado no site).

**Trecho (abstract, único texto disponível nesta sessão):**
> "we consider applying subgroup justice concepts to gradient-boosting
> machines [...] Our approach expanded gradient-boosting methodologies to
> explore a broader range of objective functions, which combines
> conventional losses [...] and a min-max fairness term."

**Uso pretendido:** Bloco 5, como aplicação concreta e publicada do objetivo
*maximin* recém-formalizado — nota de autoria explícita (mesmo padrão da
Aula 6).

---

### Fonte 3: Long-term Fairness with Selective Labels — Valdrighi, Valera & Raimundo (2026)

*Forty-third International Conference on Machine Learning* (ICML 2026)
(`publications/group/long-term-fairness-with-selective-labels.qmd`).

**Trecho (abstract):**
> "labels [...] are selective labels as they are only revealed based on
> positive decisions [...] we introduce a novel framework that leverages
> both the observed data and a label predictor model to estimate the true
> fairness measure value."

**Uso pretendido:** Bloco 6, como a pesquisa que resolve formalmente o
problema dos rótulos seletivos introduzido pela palestra-base.

---

### Fonte 4: When AI Describes Race? — Braz da Silva Segundo & Raimundo (2026)

*Algorithmic Fairness Across Alignment Procedures and Agentic Systems*
(`publications/mraimundo/when-ai-describes-race-unveiling-racial-bias-in-vision-langu.qmd`).

**Trecho (abstract):**
> "certain racial groups are disproportionately referenced, with the white
> race often being treated as the default while other races receive
> explicit mentions at varying rates."

**Uso pretendido:** Bloco 7, como o estudo publicado que fundamenta
empiricamente (com um dataset brasileiro, TSE) o fenômeno de "brancura como
padrão" já introduzido pela palestra-base.

---

## Pendência a resolver antes da Etapa 3 (montagem do `index.qmd`)

**Bloco 7 — exemplo de manipulação de espaço latente (raça editável em
imagens geradas).** A palestra-base traz uma tabela de imagens
(`figs/latents/latents_man_*.png`) mostrando um rosto gerado com a raça
alterada progressivamente ($\alpha=0$ a $\alpha=0.5$) via manipulação do
vetor de embedding, mas **não cita um paper específico** para esse
experimento no `.tex` — não é o mesmo trabalho de "Towards a Geometric
Theory of Fairness" (que é sobre detectar mode collapse via variedade de
Grassmann, tema diferente). Preciso confirmar com você: essa manipulação de
espaço latente é de um paper específico (publicado ou em andamento, mesmo
que ainda não esteja no site) que eu deva citar, ou é melhor eu tratar esse
exemplo como ilustração conceitual da própria palestra, sem citação de paper
à parte (mesmo tratamento dado ao *loop* de retroalimentação de policiamento
preditivo na Aula 6, marcado lá como "extensão nossa")?

## Pendência sobre a ementa da disciplina (Etapa 5, só depois da aula aprovada)

Com a mudança de tema, as duas leituras hoje listadas para a Lesson 7 no
`../index.qmd` (Van de Poel & Royakkers, Cap. 6 "Ethical Aspects of Technical
Risks"; Steen, Cap. 5 "Value Sensitive Design and Responsible Innovation")
não cobrem fairness. Steen Cap. 5 ainda tem uma ponte de conteúdo genuína (o
bloco de Fechamento desta aula, sobre traduzir valores humanos em objetivo
técnico, é essencialmente Value Sensitive Design aplicado) — posso propor
mantê-lo como leitura complementar. Van de Poel Cap. 6 (risco técnico) perde
a conexão direta com o novo tema — não tenho, na biblioteca desta disciplina,
nenhum capítulo específico de fairness para substituí-lo (livros como
*Fairness and Machine Learning*, fairmlbook.org, e *The Ethical Algorithm*,
já citados na página do curso `ai-ethics`, não têm PDF disponível nesta
sessão). Proposta: citar a própria palestra "Bias is Learned, Fairness is
Taught" como leitura/assistida principal da Lesson 7. Decidimos isso na
Etapa 5, não agora.
