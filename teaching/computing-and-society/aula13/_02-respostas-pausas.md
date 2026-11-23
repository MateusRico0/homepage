# Roteiro de Discussão das Pausas — Aula 13: Princípios de *Data Feminism* e Colaboração Interdisciplinar

## Pausa 1 — A Auditoria de *Fairness* que Ignorou o Problema

**Dilema:** Uma *fintech* aprova seu modelo de crédito nas métricas de *fairness* (paridade demográfica e igualdade de oportunidade) sobre `sexo` e `raça`, mas usa apenas histórico de cartão de crédito e CEP residencial, sem consultar trabalhadoras informais ausentes da base.

1. **Por que o modelo passa nas métricas da Aula 7 e ainda assim perpetua exclusão?**
   - Métricas estatísticas de *fairness* avaliam disparidades *dentro* dos dados e rótulos já coletados. Elas não detectam quem ficou de fora da base histórica (*missing dataset* / exclusão financeira prévia) nem questionam se o histórico de cartão e o CEP são *proxies* estruturais de renda e classe.
2. **O que muda ao passar da *ética de dados* para a *justiça de dados*?**
   - A ética de dados pergunta como equilibrar o modelo dado o problema atual; a justiça de dados (*Data Feminism*) pergunta *antes*: quem definiu o que é "bom pagador", quem financiou o sistema e quem foi excluído da formulação do produto?

---

## Pausa 2 — O Cadastro de Entregas e o Campo `genero`

**Dilema:** Um app de entregas propõe trocar `genero ENUM('M', 'F')` por uma lista obrigatória com 15 opções de identidade de gênero, mantendo a coleta "para futuras segmentações de marketing".

1. **Ampliar para 15 opções obrigatórias resolve os Princípios 1 (*Examinar o poder*) e 4 (*Repensar binários*)?**
   - Não. Embora reduza o apagamento taxônomico, manter a coleta obrigatória de um atributo sensível sem necessidade funcional amplia a vigilância e o risco de discriminação ou vazamento (Princípio 1).
2. **Qual alternativa de modelagem é mais coerente com o *Data Feminism* e a minimização de dados?**
   - Perguntar primeiro se o serviço de entregas precisa mesmo desse atributo. Quando não há finalidade legítima essencial, a melhor decisão de engenharia é **não coletar** o campo (ou torná-lo estritamente opcional e desvinculado de perfilamento comercial).

---

## Pausa 3 — "Os Números Históricos Falam por Si"

**Dilema:** Uma rede hospitalar entrega 500 mil registros de emergência para treinar um modelo de triagem, dispensando médicos, enfermeiras e assistentes sociais porque *"os números falam por si"*.

1. **Que distorções institucionais e barreiras de acesso (Princípio 6) estão escondidas nessa tabela?**
   - A base registra apenas quem conseguiu chegar ao hospital (omitindo barreiras econômicas, geográficas e de horário), incorpora mudanças de protocolo e códigos ao longo do tempo e pode reproduzir subestimação histórica de dor ou urgência em grupos vulneráveis.
2. **Qual trabalho humano invisível (Princípio 7) produziu esses dados e manterá o sistema?**
   - O preenchimento dos prontuários sob alta pressão por enfermagem e recepção, a limpeza e padronização dos códigos clínicos e a auditoria contínua de *drift* após a implantação — trabalho frequentemente invisibilizado pela retórica da "IA autônoma".

---

## Pausa 4 — Ética na Última Semana Antes do Deploy

**Dilema:** Com acurácia global de 96,8%, uma equipe de reconhecimento facial para catracas universitárias chama uma socióloga na última semana apenas para "validar o parecer ético", recusando-se a desagregar erros por gênero/tom de pele ou documentar a rotulagem por falta de tempo.

1. **Por que a revisão apenas no fim do sprint reproduz *ethics washing* e falha tecnicamente?**
   - Porque as premissas estruturais (objetivo, base de treinamento, métricas) já foram congeladas. Uma acurácia global de 96,8% pode mascarar falhas severas em subgrupos interseccionais (como no *Gender Shades*), e a participação tardia reduz a interdisciplinaridade a um carimbo formal.
2. **O que um *Datasheet for Datasets* e um *Model Card* exigiriam antes do deploy — ou da recusa?**
   - O *Datasheet* exigiria origem e consentimento das imagens, condições de trabalho de quem rotulou, lacunas de representação e usos inadequados. O *Model Card* exigiria métricas desagregadas por subgrupos interseccionais e limites explícitos de escopo. Sem garantias mínimas, a **recusa técnica** impede o dano institucional antes do lançamento.
