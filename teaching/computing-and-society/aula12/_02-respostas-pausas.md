# Respostas e Guia Docente — Pausas da Aula 12

Este documento reúne as resoluções detalhadas, a análise dos dilemas éticos abertos e o gabarito comentado dos testes conceituais (Verdadeiro ou Falso) das quatro Pausas da **Aula 12: Design Ético: Conflitos de Valores e Trade-offs**.

---

## Pausa 1: Conflitos de Valores e a Falácia do Reducionismo Técnico

### 1. Resolução da Pergunta Aberta
*Cenário:* Uma equipe de desenvolvimento de um mensageiro instantâneo com criptografia de ponta a ponta recebe uma ordem judicial para inserir uma "porta dos fundos" (*backdoor*) que permita a interceptação de comunicações de suspeitos de crimes graves. A diretoria da empresa sugere resolver o conflito "tecnicamente", criando uma chave-mestra sob custódia de um comitê de segurança.
1. Quais valores humanos fundamentais estão em rota de colisão direta nesse caso?
2. Por que a proposta da diretoria de criar uma "chave-mestra" incorre na falácia do reducionismo técnico?

- **Valores Morais em Conflito:**
  - De um lado: **Privacidade, Autonomia Individual, Confidencialidade e Segurança Cibernética Sistêmica** de centenas de milhões de cidadãos, jornalistas, ativistas e empresas que dependem da inviolabilidade matemática da criptografia para proteção contra governos autoritários, cibercriminosos e espionagem industrial.
  - Do outro lado: **Segurança Pública, Justiça Criminal e Proteção de Vítimas Vulneráveis**, com a capacidade de órgãos de investigação coletarem provas contra crimes hediondos e terrorismo.

- **A Falácia do Reducionismo Técnico:**
  A proposta de criar uma "chave-mestra" pressupõe ingenuamente que é possível introduzir uma vulnerabilidade controlada que "apenas as pessoas autorizadas e benevolentes" consigam explorar.

  - *No plano da segurança computacional:* Qualquer vulnerabilidade deliberadamente inserida na arquitetura de um protocolo criptográfico enfraquece o sistema para todos. Não existe backdoor que responda exclusivamente a mandados judiciais; agentes estatais hostis e criminosos descobrirão e explorarão a mesma brecha.
  - *No plano ético:* O reducionismo técnico finge que um dilema político-moral fundamental (o equilíbrio entre soberania do Estado e direitos civis fundamentais) pode ser "resolvido" adicionando uma linha de código ou um módulo de autenticação. A decisão de comprometer ou manter a criptografia é uma escolha axiológica irremediável sobre qual valor prevalecerá na sociedade.

### 2. Gabarito Comentado dos Testes Conceituais (V/F)

*   **(A) Verdadeiro.** Conflitos de valores em tecnologia envolvem bens humanos legítimos que não podem ser maximizados simultaneamente dentro de uma mesma arquitetura computacional tradicional.
*   **(B) Falso.** A falácia do reducionismo técnico consiste exatamente em acreditar que dilemas morais complexos podem ser convertidos em meros problemas de otimização matemática com uma métrica técnica única e sem julgamento de valor.
*   **(C) Verdadeiro.** Em sistemas sociotécnicos, os conflitos podem ser axiológicos (entre valores diferentes, como privacidade vs. segurança) ou distributivos (quando o mesmo valor beneficia um grupo às custas do prejuízo de outro).
*   **(D) Falso.** Escolhas de arquitetura de software nunca são neutras; mesmo a decisão de "não escolher" e manter a arquitetura padrão favorece silenciosamente certos valores em detrimento de outros.

---

## Pausa 2: A Metodologia do Design Sensível a Valores (VSD)

### 1. Resolução da Pergunta Aberta
*Cenário:* O Ministério da Saúde decide implantar um Prontuário Eletrônico Unificado em nuvem que integra exames, diagnósticos e históricos médicos de todos os cidadãos do país.
1. Quem são as partes interessadas diretas (*direct stakeholders*) e indiretas (*indirect stakeholders*) desse sistema?
2. Como as investigações Conceitual, Empírica e Técnica do VSD operam para guiar esse projeto?

- **Mapeamento de Stakeholders:**
  - *Stakeholders Diretos:* Médicos, enfermeiros, recepcionistas, técnicos de laboratório e os próprios pacientes que acessam o portal para consultar exames.
  - *Stakeholders Indiretos:* Familiares de pacientes inconscientes em emergências, companhias seguradoras de saúde, empregadores que podem discriminar funcionários com base em diagnósticos vazados, e a sociedade em geral (que se beneficia de dados agregados para vigilância epidemiológica).

- **Aplicação da Tríade Metodológica do VSD:**
  - *Investigação Conceitual:* Mapear valores essenciais contextuais. O que significa "Privacidade" para um paciente com doença estigmatizante (ex.: HIV, saúde mental)? O que significa "Segurança e Eficiência" para um médico de UTI que atende uma vítima de trauma desacordada e precisa saber o tipo sanguíneo em 30 segundos?
  - *Investigação Empírica:* Conduzir pesquisas e entrevistas de campo: os médicos realmente preenchem formulários de consentimento complexos no meio de emergências? Como os pacientes vulneráveis reagem ao saber que seus dados estão centralizados? Quais são as violações de privacidade mais temidas?
  - *Investigação Técnica:* Projetar a arquitetura: criar um modelo de controle de acesso baseado em papéis (*RBAC*) com privilégio de emergência temporário (*Break-the-Glass*), no qual um médico acessa o prontuário sem senha prévia do paciente, mas essa ação dispara um log imutável, auditoria obrigatória e notificação ao paciente.

### 2. Gabarito Comentado dos Testes Conceituais (V/F)

*   **(A) Verdadeiro.** O VSD estabelece uma metodologia integradora e iterativa que combina investigações conceituais (filosóficas), empíricas (sociais/humanas) e técnicas (arquitetura e código).
*   **(B) Verdadeiro.** Stakeholders indiretos são aqueles que não interagem fisicamente com a interface do software, mas sofrem os impactos distributivos e morais das decisões automatizadas pelo sistema.
*   **(C) Falso.** A investigação empírica do VSD busca compreender como os valores humanos são percebidos, vividos e priorizados na prática pelas pessoas afetadas, e não apenas testar a usabilidade e velocidade da interface.
*   **(D) Falso.** A investigação técnica do VSD analisa criticamente como as propriedades estruturais da tecnologia (modelagem de dados, algoritmos, protocolos) suportam ou inibem valores morais específicos.

---

## Pausa 3: A Hierarquia de Valores de Van de Poel (Árvores de Valores)

### 1. Resolução da Pergunta Aberta
*Cenário:* Uma equipe de desenvolvimento ágil recebe a diretiva do Product Owner: *"O nosso aplicativo deve respeitar rigorosamente a Privacidade dos usuários"*.
Construa uma Árvore de Valores (*Value Tree*) segundo a metodologia de Ibo van de Poel, decompondo esse valor abstrato em normas intermediárias e requisitos técnicos de design mensuráveis.

- **Nível 1: Valor Fundamental Abstrato:**
  - *Privacidade* (Autonomia informacional e controle sobre os próprios dados).

- **Nível 2: Normas e Diretrizes Operacionais:**
  1. *Minimização de Dados:* Coletar estritamente o necessário para a execução do serviço.
  2. *Retenção Limitada:* Descartar dados que perderam sua finalidade operacional.
  3. *Segurança no Armazenamento:* Impedir vazamentos e acessos indevidos a dados sensíveis.
  4. *Transparência e Autonomia do Usuário:* Permitir inspeção e revogação de consentimento a qualquer momento.

- **Nível 3: Requisitos Técnicos de Design (Backlog / Testes de Software):**
  - *Para Minimização:* O formulário de cadastro não deve conter campos de gênero, estado civil ou data de nascimento completa se o app for um leitor de texto.
  - *Para Retenção:* Implementar rotina assíncrona diária (`cron job`) no banco de dados que executa `DELETE FROM user_tracking_logs WHERE created_at < NOW() - INTERVAL '30 days'`.
  - *Para Segurança:* Campos de senha e dados sensíveis devem ser criptografados com algoritmo Argon2id ou bcrypt com fator de custo calibrado.
  - *Para Autonomia:* Disponibilizar endpoint `POST /api/user/delete-account` que anonimiza ou remove em cascata todas as chaves estrangeiras vinculadas ao ID do usuário em conformidade com o Art. 18 da LGPD.

### 2. Gabarito Comentado dos Testes Conceituais (V/F)

*   **(A) Verdadeiro.** A Árvore de Valores de Van de Poel organiza a especificação em três camadas lógicas: Valores morais fundamentais $\to$ Normas de ação intermediárias $\to$ Requisitos técnicos de design específicos e auditáveis.
*   **(B) Falso.** Um requisito de design no nível inferior da árvore deve ser concreto, mensurável e testável por critérios de engenharia de software (como asserções em testes unitários ou auditorias de banco de dados).
*   **(C) Verdadeiro.** É comum que diferentes valores no topo da árvore gerem normas concorrentes que colidem no nível dos requisitos técnicos, exigindo deliberação explícita de trade-offs.
*   **(D) Falso.** O modelo de Árvore de Valores não visa eliminar a tomada de decisão ética, mas torná-la transparente, rastreável e fundamentada entre a intenção moral e o código implementado.

---

## Pausa 4: Mediação de Trade-offs e Inovação Conceitual de Design

### 1. Resolução da Pergunta Aberta
*Cenário:* Um consórcio hospitalar quer compartilhar dados de tomografias com pesquisadores de inteligência artificial para treinar um modelo de diagnóstico precoce de câncer. O dilema clássico impõe: se os hospitais compartilharem as imagens brutas, violam o sigilo médico de milhares de pacientes; se os hospitais censurarem ou borrarem as imagens para proteger a privacidade, a acurácia diagnóstica do modelo de IA despenca.
Como a ciência da computação utilizou a **inovação conceitual de design (*innovative design solutions*)** para superar essa falsa dicotomia?

- **A Superação pela Inovação Arquitetural:**
  Em vez de aceitar o dilema estático de "perder privacidade ou perder utilidade médica", a computação desenvolveu duas inovações de design fundamentais:
  1. **Aprendizado Federado (*Federated Learning*, McMahan et al., 2017):**
     Em vez de enviar os dados dos pacientes para um servidor central, os hospitais mantêm os prontuários e imagens em seus servidores locais protegidos. O modelo de inteligência artificial viaja até os hospitais, treina localmente nos dados protegidos, e envia apenas as matrizes de gradientes (atualizações de pesos) de volta ao coordenador central. Os dados brutos nunca saem da instituição de saúde!
  2. **Privacidade Diferencial (*Differential Privacy*, Dwork et al., 2006):**
     Adiciona ruído calibrado (ex.: mecanismo de Laplace ou Gaussiano) às atualizações agregadas dos gradientes, garantindo matematicamente que a presença ou ausência de qualquer paciente específico no dataset não possa ser inferida estatisticamente, mesmo por um invasor com poder computacional ilimitado.

- **Lição Pedagógica:**
  O trade-off aparente foi dissolvido através de **imaginação moral aliada à excelência de engenharia de software**: a nova arquitetura alcançou alta utilidade clínica com garantias formais estritas de privacidade!

### 2. Gabarito Comentado dos Testes Conceituais (V/F)

*   **(A) Verdadeiro.** A abordagem de satisficing (Herbert Simon) busca identificar soluções de design que satisfaçam patamares mínimos aceitáveis para todos os valores em conflito, em vez de maximizar um valor provocando o colapso do outro.
*   **(B) Verdadeiro.** Uma das maiores contribuições do VSD é encorajar a busca por inovações conceituais de design (*innovative design solutions*) que reformulam a arquitetura do sistema para superar trade-offs aparentes.
*   **(C) Falso.** O Aprendizado Federado e a Privacidade Diferencial demonstram que é possível treinar modelos de inteligência artificial com alto desempenho preditivo preservando o sigilo de dados confidenciais através de arquiteturas descentralizadas.
*   **(D) Falso.** Em muitos dilemas éticos existem restrições deontológicas e direitos humanos inalienáveis (como o consentimento e a dignidade humana) que não podem ser sacrificados por meros cálculos de conveniência de mercado.
