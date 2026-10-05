# Progresso — Computing and Society

Estado aprovado + vocabulário, para dar continuidade entre aulas. O histórico de correções está no git (a versão longa anterior deste arquivo foi até o commit `1d4a4fc`).

**Fontes** (`_fontes/`): Maciel & Viterbo (2020, `CSV1-3.pdf`; o Vol. 2 começa no Cap. 9, a numeração continua do Vol. 1), Van de Poel & Royakkers (2011, `EthEng.pdf`), Steen (2022, `EthTech.pdf`), Varshney (2022, *Trustworthy ML* — confira a página pelo cabeçalho do PDF, porque o sumário está deslocado), LGPD (Lei 13.709/2018, texto compilado). Nas Aulas 6 e 7 entra também material autoral do professor (palestra "Bias is Learned, Fairness is Taught"; Raimundo, 2025).
**Particularidades da disciplina:** humanidades/ética, sem chunks Python (só prosa, casos e diagramas). Diagramas em TikZ, nunca Mermaid. Extensões e sínteses nossas são marcadas como tais no texto.

## Estado das aulas

| Pasta | Aula | Estratégia | Casos-fio | Estado |
|---|---|---|---|---|
| `aula01` | 1 — Computação como sistema sociotécnico | — | Challenger | publicada |
| `aula02` | 2 — O que é ética, e o Ciclo Ético | — | Ford Pinto | publicada |
| `aula03` | 3 — Domínios da computação e responsabilidade profissional | — | códigos ACM/IEEE; conselho profissional (CREA) | publicada |
| `aula04` | 4 — Dimensões humanas, sociais e éticas da engenharia de software | — | Lei de Conway, requisitos, *dark patterns* | publicada |
| `aula05` | 5 — Pesquisa qualitativa, teste A/B e tecnologia persuasiva | A/B | seguradora | publicada |
| `aula06` | 6 — Dados, viés e discriminação algorítmica (LGPD) | A | Amazon (abertura), seguradora da Aula 5 | publicada (reescrita em 2026-09-21) |
| `aula07` | 7 — Fairness algorítmica: definições, métricas e mitigação | A | empréstimo; três danos documentados | publicada; título diverge do index (ver Pendências) |
| `aula08` | 8 — Arquitetura, energia e custo material da infraestrutura digital | A | Scala AI City / Tekoa Pekuruty (Eldorado do Sul); Querétaro, Módulo Penco, LEAF/Pará | publicada (recuperada da antiga `aula06` em 2026-10-05) |
| — | 9–15 | — | — | não iniciadas |

## Fio condutor

- **1:** tecnologia, pessoas, organizações e cultura se moldam mutuamente. Mapa de atores; a responsabilidade do engenheiro é menor (um entre muitos) e maior (considerar quem não está na sala). **Ponte:** como raciocinar sobre o que é certo fazer?
- **2:** quatro teorias normativas (consequencialismo, deontologia, virtudes, cuidado) + Ciclo Ético em 5 fases (formulação, análise, opções, avaliação, reflexão). **Ponte:** códigos profissionais como fonte institucional.
- **3:** o que os códigos (ACM/IEEE) dizem, para que servem e o que um conselho de profissão faz; a Informática deveria ter um conselho?
- **4:** a prática de engenharia de software como processo social: Lei de Conway, elicitação de requisitos, *dark patterns* (mecanismo deliberado).
- **5:** métodos de pesquisa com usuário, teste A/B e tecnologia persuasiva; método e métrica já mudam o produto.
- **6:** o dado de treino é a sociedade: quatro espaços (construto, observado, bruto, preparado) × três validades × cinco vieses (Varshney, cap. 4). A cegueira de atributo não resolve. LGPD: princípios do art. 6º × vieses (síntese nossa); histórico do art. 20. Métricas de fairness e mitigação ficaram, por decisão do usuário, para a Aula 7.
- **7:** atributo sensível $Z$; injustiça individual × de grupo; paridade demográfica × igualdade de oportunidade; teorema da impossibilidade; fairness rawlsiana (princípio da diferença, M²FGB); fairness de longo prazo com rótulos seletivos. **Ponte:** o custo material de onde esse cálculo roda (Aula 8).
- **8:** a "nuvem" tem peso: energia, água e minerais (TI Verde, Tabela 14.1 de Maciel & Viterbo) recaem sobre territórios concretos. Caso-fio Scala AI City; soberania digital (4 dimensões e seu paradoxo), policrise, zona de sacrifício digital (inclusão predatória) × redlining; colonialismo verde (LEAF/Pará, CLPI); Brundtland, justiça intra/intergeracional, ciclo de vida; síntese em ética territorial. **Ponte:** a Parte 2 termina com quem *não* estava na sala; a Aula 9 (Parte 3) pergunta quem *está* — gênero e diversidade na equipe.

## Vocabulário (termos que as aulas seguintes podem usar sem redefinir)

| Termo | Significado | Aula |
|---|---|---|
| sistema sociotécnico | tecnologia + pessoas + organizações + cultura, moldando-se mutuamente | 1 |
| consequencialismo, deontologia, ética das virtudes, ética do cuidado | as quatro teorias normativas | 2 |
| Ciclo Ético | método de 5 fases para estruturar (não automatizar) o raciocínio moral | 2 |
| código de ética profissional, conselho de profissão | fonte institucional de orientação e o órgão que lhe dá força | 3 |
| Lei de Conway; *dark pattern* | a arquitetura copia o organograma; design que induz o usuário contra o próprio interesse | 4 |
| teste A/B, tecnologia persuasiva | experimento controlado com usuários; design para mudar comportamento | 5 |
| espaço do construto/observado/bruto/preparado | as quatro etapas do dado (Varshney) | 6 |
| validade de construto/externa/interna | onde cada viés quebra a medição | 6 |
| viés social, de representação, temporal, de preparação, envenenamento | os cinco vieses (Varshney, cap. 4) | 6 |
| controlador, titular, ANPD | papéis da LGPD | 6 |
| atributo sensível $Z$; cegueira de atributo | variável protegida; retirá-la não remove a informação (proxies) | 6–7 |
| paridade demográfica, igualdade de oportunidade | métricas de grupo concorrentes | 7 |
| teorema da impossibilidade | as métricas de grupo não podem valer juntas em geral | 7 |
| fairness rawlsiana | melhorar o pior grupo em vez de igualar | 7 |
| rótulos seletivos | só se observa o desfecho de quem foi aprovado | 7 |
| TI Verde; Verde Por Software × Verde No Software | práticas para reduzir o impacto ambiental da TI; software como ferramenta de sustentabilidade × software ele mesmo sustentável | 8 |
| soberania digital (infraestrutural, de dados, regulatória, epistêmica) | autoridade de um Estado sobre sua arquitetura digital; paradoxo: autonomia exige capital estrangeiro | 8 |
| policrise | crises (clima, energia, sociedade) causalmente entrelaçadas | 8 |
| zona de sacrifício digital × redlining digital | inclusão predatória (território como sítio de extração) × exclusão do serviço | 8 |
| colonialismo verde; CLPI | compensar emissões comprando crédito em território alheio; Consentimento Livre, Prévio e Informado (Convenção 169 da OIT) | 8 |
| justiça intra/intergeracional; poluidor-pagador | divisão justa dentro da/entre gerações; quem causa o dano repara | 8 |
| análise de ciclo de vida | impacto em extração, produção, uso e descarte (e-waste) | 8 |
| ética territorial | território como ecossistema + modo de vida, não só jurisdição | 8 |

## Pendências

- **Index da disciplina** (tem alterações não commitadas): a Lesson 7 chama-se "Automated Decision-Making, Optimization, AI, and Risk", mas a `aula07` trata de Fairness algorítmica; as Lessons 9–13 aparecem duplicadas.
- **Pontes desatualizadas pela renumeração:** `aula04` ("Ponte para a Aula 6" deveria ser Aula 5); `aula05` ainda chama a próxima de "Aula 6" e a descreve como arquitetura (hoje é Dados e Viés).
- **Leituras com capítulo errado na ementa (não corrigidas):** numa lição da Parte 3 (a entrada duplicada), o Cap. 10 de Maciel & Viterbo entrou no lugar de uma citação inexistente, sem conferir se o conteúdo serve.
- **Quantidade de testes:** Aulas 1–4 têm 12 testes (a regra é 6–10).
- **Render de projeto:** o `quarto render` falhava numa etapa final (`site_libs`/`publications`), fora do conteúdo das aulas. Conferir se ainda acontece.
- **Nomes legados:** `_03-respostas-pausas.md` (Aulas 1–5).
