## Resumo — Aula 12: Design Ético: Conflitos de Valores e Trade-offs

Ao longo das Aulas 1 a 11, exploramos a computação como um sistema sociotécnico, dissecamos as correntes éticas normativas (Aula 2), a dimensão humana da engenharia de software (Aula 4), as armadilhas da tecnologia persuasiva (Aula 5), as fontes de viés e discriminação algorítmica (Aulas 6 e 7) e os mecanismos da economia da atenção e microtargeting (Aula 11). Contudo, um desafio persistente angustia engenheiros e designers no cotidiano profissional: **saber que valores morais importam não é suficiente quando valores legítimos entram em conflito direto na tomada de decisão técnica**.

Esta aula inaugura o Eixo 4 da disciplina (*Técnicas de Computação Humanística*), equipando os estudantes com arcabouços metodológicos formais para analisar, ponderar e mediar conflitos de valores no ciclo de desenvolvimento de software. Em vez de tratar dilemas éticos como "problemas puramente técnicos de otimização" ou, inversamente, como "meras opiniões subjetivas", articulamos a metodologia do **Design Sensível a Valores (*Value Sensitive Design* - VSD)**, proposta por Batya Friedman e Peter Kahn, e a teoria de **Hierarquia de Valores e Árvores de Valores (*Value Trees*)**, formulada por Ibo van de Poel.

Iniciamos dissecando a natureza dos conflitos de valores em sistemas digitais (conflitos entre valores distintos, como Privacidade versus Segurança, e conflitos distributivos entre diferentes grupos de stakeholders). Em seguida, detalhamos a tríade integradora do VSD: as investigações **Conceitual** (mapeamento de stakeholders diretos e indiretos e definição moral de valores), **Empírica** (pesquisa de campo sobre as práticas, percepções e prioridades humanas) e **Técnica** (auditoria das propriedades estruturais do software que facilitam ou obstruem valores). No Bloco 3, resolvemos o abismo entre a filosofia moral e o código-fonte através da **Hierarquia de Valores** de Van de Poel, demonstrando como decompor valores abstratos em normas prescritivas intermediárias e, finalmente, em **requisitos técnicos de design mensuráveis e testáveis**. No Bloco 4, exploramos estratégias formais para mediação de *trade-offs* (consequencialista, deontológica e *satisficing* de Herbert Simon) e destacamos a maior contribuição da engenharia responsável: a busca por **soluções inovadoras de design (*innovative design solutions*)**, que reformulam a arquitetura do sistema para dissolver falsas dicotomias (como a Privacidade Diferencial e o Aprendizado Federado fizeram entre privacidade e utilidade estatística).

**Objetivos:**
1. Compreender a natureza intrínseca dos conflitos de valores em sistemas de software e desconstruir a falácia do reducionismo técnico em dilemas éticos de engenharia.
2. Aplicar as três investigações do Design Sensível a Valores (Conceitual, Empírica e Técnica) de modo iterativo e integrado no ciclo de desenvolvimento de software.
3. Construir Árvores de Valores (*Value Trees*) segundo o modelo de Van de Poel, traduzindo valores humanos abstratos em normas operacionais e requisitos técnicos de design auditáveis.
4. Mapear e diferenciar impactos sobre partes interessadas diretas (*direct stakeholders*) e indiretas (*indirect stakeholders*).
5. Analisar e aplicar estratégias de mediação de *trade-offs* morais, demonstrando como a inovação conceitual em arquitetura de software pode superar aparentes impasses éticos insolúveis.

**Pré-requisitos:** O Ciclo Ético e ética normativa (Aula 2); Dimensões sociais e humanas da Engenharia de Software e Lei de Conway (Aula 4); Métricas de Fairness e trade-offs algorítmicos (Aula 7); Arquitetura de escolha e dark patterns (Aula 11).
**Estratégia Pedagógica:** A (*Outside-In*) — Parte de um dilema real de engenharia de software contemporâneo (o debate da criptografia de ponta a ponta e moderação de abusos; prontuários médicos de emergência vs. sigilo) $\to$ Formalização metodológica do VSD $\to$ Construção da Árvore de Valores de Van de Poel $\to$ Mediação de trade-offs e inovação arquitetural.
**Casos de Estudo:**
1. *Criptografia Ponta a Ponta vs. Investigação Criminal / Moderação de Danos:* Apple vs. FBI (San Bernardino) e o debate internacional sobre *client-side scanning*.
2. *Prontuário Eletrônico Unificado de Saúde:* Acesso instantâneo em socorro de emergência vs. Sigilo de dados biomédicos e discriminação securitária.
3. *Privacidade vs. Utilidade Analítica em Pesquisa:* A emergência da Privacidade Diferencial e Aprendizado Federado como inovações de design que superam o trade-off clássico.

---

## Plano de aula — Aula 12 (carga horária: ~100–110 min)

1. **Revisão e Introdução: Por Que Valores Viram Código?** (~12 min)
   - *Revisão:* Das Aulas 1 e 2 (sistemas sociotécnicos e o Ciclo Ético), Aula 4 (Engenharia de Software como escolha humana) e Aula 11 (arquiteturas de escolha e a não-neutralidade da interface).
   - *Ideia Central:* Desenvolver software é, em cada linha de código, tomar decisões sobre valores. A arquitetura do banco de dados, os protocolos de rede, as permissões de acesso e os fluxos de interface incorporam prioridades políticas e morais. O conflito ético surge não pela ausência de valores, mas pelo fato de que **valores humanos legítimos entram em rota de colisão direta**.
   - *Problema Motivador:* Um aplicativo de mensagens seguras recebe demandas judiciais para criar uma "porta dos fundos" (*backdoor*) que permita identificar redes de abuso infantil. Se atender, compromete a segurança criptográfica de milhões de ativistas e cidadãos contra governos autoritários e criminosos; se recusar, protege a privacidade de criminosos. Como engenheiros devem deliberar diante desse conflito?
   - *Roteiro (4 Perguntas Centrais):*
     1. O que é um conflito de valores em tecnologia e por que tratá-lo como "mera questão técnica" é um erro fatal?
     2. Como a metodologia tripartite do Design Sensível a Valores (VSD) investiga valores conceitual, empírica e tecnicamente?
     3. Como a Hierarquia de Valores de Van de Poel traduz aspirações morais abstratas em requisitos técnicos de engenharia?
     4. Quais são as estratégias éticas para mediar *trade-offs* e como a inovação de design pode dissolver falsas escolhas trágicas?
   - *Pausa Ativa 1.*

2. **Intuição — A Balança de Valores e a Ilusão do Ótimo Único** (~8 min)
   - Em problemas matemáticos puros, funções de custo convexas admitem um único ponto ótimo global indiscutível. Em problemas sociotécnicos, diferentes partes interessadas possuem funções de utilidade morais distintas e incomensuráveis.
   - O perigo do "cinismo tecnocrático": declarar que "tudo é um trade-off e alguém sempre sai perdendo", usando isso como desculpa para escolher a alternativa mais barata ou corporativamente conveniente.
   - O papel do engenheiro responsável: tornar os valores visíveis, explícitos, deliberados e auditáveis na arquitetura do sistema.

3. **Bloco 1: A Natureza dos Conflitos de Valores em Sistemas Computacionais** (~25 min)
   - Definição de "Valor" em tecnologia (Friedman & Hendry, 2019): *aquilo que uma pessoa ou grupo de pessoas considera importante na vida* (privacidade, segurança, autonomia, confiança, equidade, justiça, transparência, inclusão, sustentabilidade).
   - Tipologia dos Conflitos de Valores:
     - **Conflito entre valores conceituais distintos:**
       - *Privacidade vs. Segurança Pública / Vigilância.*
       - *Acurácia Preditiva Máxima vs. Equidade Estatística / Explicabilidade.*
       - *Usabilidade / Fricção Zero vs. Consentimento Informado / Deliberação Crítica.*
     - **Conflito Distributivo (entre diferentes partes interessadas):**
       - O mesmo valor alocado de forma desigual entre stakeholders diretos e indiretos (ex.: conveniência para quem pede delivery vs. segurança e dignidade para o entregador da plataforma).
   - Desconstrução da falácia do "Reducionismo Técnico": a ilusão de que atribuir pesos arbitrários e somar tudo em uma função de perda escalar resolve o conflito moral subjacente.
   - *Pausa Ativa 2.*

4. **Bloco 2: A Metodologia do Design Sensível a Valores (VSD)** (~25 min)
   - Origem: Batya Friedman, Peter Kahn e colaboradores (Universidade de Washington, década de 1990).
   - O princípio da não-neutralidade dos artefatos: a tecnologia possui tendências materiais que facilitam certas práticas sociais e inibem outras.
   - As Três Investigações Integradas e Iterativas do VSD:
     1. **Investigação Conceitual (*Conceptual Investigation*):**
        - Mapeamento explícito de *Stakeholders Diretos* (quem usa o sistema diretamente) e *Stakeholders Indiretos* (quem é afetado pelas decisões do sistema mesmo sem tocá-lo).
        - Identificação dos valores em disputa e esclarecimento filosófico de suas definições contextuais (o que significa "privacidade" em um hospital vs. em uma rede social?).
     2. **Investigação Empírica (*Empirical Investigation*):**
        - Coleta de dados com os seres humanos reais afetados: entrevistas semiestruturadas, observação participante, pesquisas de atitudes e testes contextuais.
        - Como os usuários priorizam valores em situações de tensão? Quais são as percepções de dano moral?
     3. **Investigação Técnica (*Technical Investigation*):**
        - Auditoria da arquitetura, do código, da modelagem de dados e dos algoritmos:
          - *Análise retrospectiva:* como o sistema atual suporta ou viola certos valores?
          - *Design prospectivo:* como redesenhar o protocolo, a estrutura de banco de dados e as interfaces para materializar os valores priorizados?
   - *Pausa Ativa 3.*

5. **Bloco 3: A Hierarquia de Valores de Van de Poel (Do Abstrato ao Requisito)** (~20 min)
   - O desafio prático do engenheiro: "Meu gerente pediu para o sistema ser ético e respeitar a privacidade. O que eu coloco no Jira ou no backlog da sprint?"
   - A teoria da especificação moral de Ibo van de Poel (2011):
     - **Nível 1 — Valores Fundamentais (*Values*):** Aspirações morais gerais, universais e abstratas (ex.: *Privacidade*, *Segurança*, *Sustentabilidade*).
     - **Nível 2 — Normas e Diretrizes (*Norms*):** Prescrições de ação e regras comportamentais intermediárias que contextualizam o valor (ex.: *Minimização da coleta de dados*, *Retenção temporária*, *Consentimento explícito revogável*, *Proteção contra acesso não autorizado*).
     - **Nível 3 — Requisitos Técnicos de Design (*Design Requirements*):** Especificações técnicas exatas, mensuráveis, implementáveis em código e verificáveis por testes de software (ex.: *Apagar registros da tabela `temp_tokens` após 24 horas via trigger*, *Criptografia AES-GCM-256 para o campo `cpf` no banco*, *Checkbox desmarcado por padrão na UI*, *Disponibilizar endpoint REST para exclusão de conta sob GDPR/LGPD*).
   - Construção e auditoria de **Árvores de Valores (*Value Trees*)**: conectando a folha técnica da árvore à raiz axiológica moral.
   - *Pausa Ativa 4.*

6. **Bloco 4: Estratégias de Mediação e Inovações Conceituais de Design** (~15 min)
   - Métodos clássicos de mediação de trade-offs morais:
     - *Pesagem e Balanceamento (Consequencialismo):* Avaliar impactos agregados e mitigar danos residuais.
     - *Limiares Inegociáveis (Deontologia):* Direitos fundamentais estabelecem restrições estritas que nenhum cálculo de conveniência técnica pode violar.
     - *Satisficing (Herbert Simon):* Buscar soluções que atinjam um patamar mínimo satisfatório em todos os valores essenciais, em vez de maximizar um às custas do colapso do outro.
   - **A Grande Lição do VSD: Inovação Conceitual de Design (*Innovative Design Solutions*):**
     - Muitas vezes, o trade-off é trágico apenas porque operamos sob uma premissa arquitetural ultrapassada!
     - *Exemplo Revolucionário da Computação:* O conflito clássico entre **Privacidade dos Pacientes** e **Utilidade dos Dados para Pesquisa Científica**. Durante décadas, a resposta era: "ou publicamos dados anonimizados precários, ou violamos a privacidade". A ciência da computação respondeu com inovação arquitetural: **Privacidade Diferencial (*Differential Privacy*, Dwork et al.)** e **Aprendizado Federado (*Federated Learning*)**, onde modelos são treinados localmente sem que nenhum dado bruto saia do hospital!
     - *Exemplo em Interface:* Em vez de sacrificar segurança por usabilidade, criar fluxos de **Fricção Deliberada Positiva** (*Meaningful Friction*), que confirmam ações irreversíveis sem burocratizar tarefas rotineiras.

7. **Fechamento e Síntese** (~8 min)
   - *Retomando as 4 Perguntas:* Quadro-síntese consolidando as respostas da aula.
   - *O Papel da Imaginação Moral do Engenheiro:* A ética no design não é um freio de mão que atrasa lançamentos, mas um motor de excelência técnica e inovação responsável.
   - *Ponte para a Aula 13:* Como perspectivas críticas de gênero e justiça de dados aprofundam o design técnico? $\to$ **Aula 13: Princípios de Data Feminism e Colaboração Interdisciplinar**.
