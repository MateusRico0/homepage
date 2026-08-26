# Soluções — Questões de Verdadeiro/Falso (Aula 3)

> Arquivo de apoio, não publicado (prefixo `_`). Contém a resposta e a
> justificativa de cada item das 12 questões de V/F do `index.qmd`. O
> `index.qmd` publicado continua sem solução — este arquivo existe só
> para conferência do professor/monitor, seguindo a metodologia de
> criação de questões definida em `../../CLAUDE.md`.

## BART e a distinção profissional/corporativo

**a.** [ ] Se o código profissional que os engenheiros do BART invocaram fosse um código corporativo da própria BART (não do IEEE), o argumento de que ele era "parte implícita do contrato de trabalho" teria a mesma força perante o empregador.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** Um código corporativo é escrito pela própria parte empregadora, que também decide se e como aplicá-lo — o argumento de "parte implícita do contrato" perde força quando quem redigiu o código é o mesmo que decide demitir. O fato de ser um código profissional, de um terceiro (o IEEE), é o que dava alguma independência ao argumento, ainda que insuficiente na prática real.

**b.** [ ] Se o acidente do sistema BART tivesse ocorrido antes da demissão dos três engenheiros, em vez de três semanas depois, isso teria, por si só, impedido legalmente a demissão.

**Heurística:** Limite
**Resposta:** Falso
**Justificativa:** Nada no caso indica que a confirmação prévia do risco de segurança geraria, por si só, proteção legal automática contra demissão sem justa causa. A vulnerabilidade legal de quem denuncia riscos internamente é um dos limites discutidos no Bloco 5, independentemente de o risco já estar confirmado ou não no momento da demissão.

**c.** [ ] Um engenheiro de software atual que reporta, via canais internos, uma falha de segurança crítica em um sistema bancário, e é demitido em seguida, está em uma posição estruturalmente análoga à dos engenheiros do BART, ainda que trabalhe décadas depois e num domínio diferente.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** A analogia estrutural é exatamente o ponto de o caso BART ser usado como abertura da aula — o mecanismo (alertar internamente, ser ignorado, sofrer retaliação) não depende do domínio técnico específico (trens vs. sistemas bancários), nem da década em que ocorre.

**d.** [ ] Como o IEEE conseguiu enviar uma carta *amicus curiae* em apoio aos engenheiros, isso significa que o código profissional do IEEE teve, no caso BART, força disciplinar real sobre o empregador.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** A intervenção do IEEE foi uma tentativa de apoio argumentativo perante o tribunal, não uma ação disciplinar com poder de fiscalização. O tribunal não aceitou o argumento da forma proposta, e os engenheiros não recuperaram o emprego — evidência do oposto de força disciplinar real.

---

## Código consultivo vs. disciplinar (taxonomia geral)

**a.** [ ] No limite em que um código aspiracional é tão detalhado e específico que deixa de haver ambiguidade sobre o que fazer em qualquer situação prática, ele automaticamente se torna um código disciplinar.

**Heurística:** Limite
**Resposta:** Falso
**Justificativa:** O que define "disciplinar" não é o grau de detalhe do texto, mas a existência de um mecanismo institucional que garanta que o comportamento de todos, de fato, atenda a essas normas. Um código pode ser extremamente detalhado e ainda ser só aspiracional/consultivo, se ninguém fiscaliza seu cumprimento.

**b.** [ ] Se o código da NSPE não tivesse nenhuma cláusula sobre segurança pública, mas a engenharia nos EUA ainda tivesse licenciamento estadual obrigatório com poder de revogar o registro, o código da NSPE continuaria, ainda assim, funcionalmente próximo de um código disciplinar.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** O que torna um código disciplinar de fato é a existência de uma estrutura de licenciamento com poder de exclusão — isso viria do sistema de licenciamento estadual em si, não do conteúdo específico do texto do código da NSPE.

**c.** [ ] Um código de conduta interno de uma startup, sem qualquer conselho externo por trás, mas com cláusula que prevê demissão por justa causa em caso de violação, deve ser classificado como disciplinar no mesmo sentido que o código de um conselho profissional.

**Heurística:** Transferência
**Resposta:** Falso
**Justificativa:** Apesar de ter uma consequência prática (demissão), o mecanismo é o de um código corporativo comum. A diferença central da aula é entre um código apoiado por uma autarquia com poder legal de impedir o exercício da profissão, e um empregador que pode demitir com base em regras internas — os dois têm "dentes", mas não são o mesmo tipo de estrutura institucional.

**d.** [ ] Todo código profissional formulado por uma associação (e não por uma empresa) é, por definição, do tipo aspiracional ou consultivo, nunca disciplinar.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** A aula usa o padrão mais comum (a maioria dos códigos profissionais é *advisory*) como generalização útil, não como regra universal. O conceito de conselho de profissão (Bloco 3) mostra justamente uma associação/autarquia cujo código é disciplinar de fato, quando ela tem poder legal de fiscalizar o exercício — CREA, CRM, OAB.

---

## O Código de Ética da ACM

**a.** [ ] Se o item 1.4 da ACM ("be fair and take action not to discriminate") não existisse no código, um sistema de triagem de currículos com taxas de erro desiguais entre grupos demográficos ainda estaria em conflito com outros princípios do mesmo código, como o 2.5.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** O item 2.5 exige avaliação abrangente dos impactos e riscos de um sistema; uma disparidade de erro entre grupos é exatamente o tipo de risco que uma avaliação completa deveria capturar e reportar, independentemente de existir uma cláusula específica sobre discriminação.

**b.** [ ] No limite em que um sistema de software nunca é usado por ninguém fora da equipe que o construiu, o princípio 3.7 deixa de ter qualquer aplicação prática a esse sistema.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** O princípio 3.7 é explicitamente condicionado à integração do sistema à infraestrutura da sociedade. Um sistema de uso estritamente interno e nunca escalado não atende a essa condição, então o princípio simplesmente não se aplica a ele — o que não significa que outros princípios do código deixem de valer.

**c.** [ ] O princípio 2.2 ("maintain high standards of professional competence") se aplicaria a um cientista de dados que implementa um modelo de risco de crédito usando uma técnica que ele não entende completamente, mesmo que o modelo "funcione" nos testes.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** Competência profissional, no sentido do código, não se reduz a "o resultado passou nos testes" — implica entender o que se está implementando bem o suficiente para avaliar seus riscos e limites, o que "funcionar nos testes" não garante.

**d.** [ ] Como a ACM é descrita como um código "mais geral" que cobre também hardware e redes, isso significa que ela não se aplica com o mesmo peso a quem trabalha exclusivamente com desenvolvimento de software de aplicação.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** "Mais geral" descreve o escopo de quem é coberto (mais amplo que só quem programa), não o peso ou a aplicabilidade do código para desenvolvedores de software — um desenvolvedor de aplicações está plenamente coberto pelo código da ACM, com o mesmo peso que qualquer outro profissional coberto.

---

## O Código da IEEE-CS/ACM (Engenharia de Software)

**a.** [ ] Se o princípio MANAGEMENT não existisse no código, e apenas os outros sete princípios permanecessem em vigor, um gestor de projeto de software ainda estaria, por meio do princípio PUBLIC, formalmente comprometido a colocar o interesse público acima da conveniência do cronograma.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** PUBLIC se aplica a todo engenheiro de software, incluindo gestores, e tem a maior precedência entre os princípios. Sua obrigação não depende da existência do princípio MANAGEMENT, que apenas acrescenta uma responsabilidade adicional específica de liderança.

**b.** [ ] No limite em que um software nunca interage diretamente com usuários finais (ex.: uma biblioteca interna usada só por outros sistemas da mesma empresa), o princípio PRODUCT deixa de ter qualquer relevância para quem a desenvolve.

**Heurística:** Limite
**Resposta:** Falso
**Justificativa:** PRODUCT não é condicionado a haver contato direto com usuário final. Uma biblioteca interna de baixa qualidade pode propagar falhas para todos os sistemas que dependem dela — a ausência de usuário final direto não isenta o padrão profissional exigido pelo princípio.

**c.** [ ] O princípio JUDGMENT dá suporte a um engenheiro de software que se recusa a certificar como "seguro" um sistema de votação eletrônica que ele avaliou como vulnerável, mesmo sob pressão do cliente que contratou a avaliação.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** É exatamente esse tipo de situação — julgamento técnico independente sob pressão comercial — que o princípio JUDGMENT ("maintain integrity and independence in their professional judgment") visa proteger.

**d.** [ ] Como o código não tem cláusula de confidencialidade explícita (diferente do NSPE), engenheiros de software cobertos por ele podem divulgar livremente qualquer informação da empresa, sem nenhuma restrição.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** A ausência de uma cláusula de confidencialidade específica não elimina outras obrigações do código, como CLIENT AND EMPLOYER (agir nos melhores interesses do cliente/empregador, consistente com o interesse público). É um caso de tensão entre princípios, não uma licença irrestrita para divulgação.

---

## Conselho de profissão: o que de fato faz

**a.** [ ] Se a Lei 5.194/1966 não previsse punição para quem exerce a engenharia sem registro no CREA, o conselho ainda teria poder de tornar disciplinar o código de ética da profissão, só por meio de recomendações morais.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** É exatamente o poder legal de impedir o exercício por quem não é registrado que transforma um conselho em algo mais que uma associação consultiva. Sem essa previsão legal, o conselho perderia o mecanismo que dá força disciplinar de fato ao código, ficando reduzido a algo mais parecido com a ACM/IEEE-CS (Bloco 2): consultivo, sem poder de exclusão do mercado.

**b.** [ ] No limite em que um conselho de profissão existisse para a Informática, mas nunca fiscalizasse ativamente o exercício (só registrasse profissionais, sem inspecionar nada), essa Informática regulamentada ainda seria estruturalmente diferente da situação atual (sem conselho nenhum).

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Mesmo sem fiscalização ativa, a mera existência do registro obrigatório já cria a possibilidade legal de impedir o exercício por quem não está registrado — uma diferença estrutural real em relação à ausência total de conselho, ainda que a fiscalização efetiva seja fraca.

**c.** [ ] Uma associação de profissionais de UX Design que emite certificados voluntários, mas não tem qualquer previsão legal de impedir alguém sem certificado de trabalhar como designer, exerce a mesma função institucional que o CREA exerce para engenharia.

**Heurística:** Transferência
**Resposta:** Falso
**Justificativa:** Falta exatamente o elemento central: poder legal de impedir o exercício por quem não é registrado/certificado. Nesse cenário, a associação de UX funciona mais como um código voluntário (tipo ACM) do que como um conselho de profissão no sentido de CREA/CRM/OAB.

**d.** [ ] Como o CREA fiscaliza engenharia e o CRM fiscaliza medicina, todo conselho de profissão no Brasil necessariamente cobre uma única profissão isolada, sem nenhuma sobreposição possível com áreas correlatas.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** O texto não afirma isso, e não é uma implicação necessária. A aula usa CREA e CRM como exemplos ilustrativos, não como prova de que "conselho" exige exclusividade estrita de área — o ponto central é a função (registro + fiscalização + poder legal), não a delimitação exata de fronteiras entre profissões.

---

## LGPD/GDPR como regulação judicializada

**a.** [ ] Se a LGPD não existisse, mas o GDPR europeu continuasse em vigor, uma empresa brasileira que só opera e trata dados de cidadãos brasileiros dentro do Brasil estaria, ainda assim, sujeita a sanções por violar princípios como os do Art. 6º da LGPD.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** Por construção da pergunta (se a LGPD "não existisse"), não haveria a lei brasileira aplicável nesse cenário. O GDPR, por si só, não se aplica automaticamente a uma empresa que não trata dados de cidadãos europeus nem opera na UE — é a existência da própria LGPD, não do GDPR, que cria essa obrigação para uma empresa nesse cenário específico.

**b.** [ ] No limite em que uma organização trata apenas dados anonimizados de forma irreversível (sem qualquer possibilidade de reidentificação), os princípios do Art. 6º da LGPD sobre dados pessoais deixam de se aplicar a esse tratamento específico.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** A LGPD regula dados pessoais; um dado genuinamente anonimizado de forma irreversível, por definição, deixa de identificar uma pessoa. A lei trata a anonimização como um dos mecanismos que retiram um dado do regime de proteção de dados pessoais.

**c.** [ ] O princípio de "transparência" (Art. 6º, VI) se aplicaria a um aplicativo de crédito que usa um modelo de "caixa-preta" para negar empréstimos, mas se recusa a fornecer ao usuário qualquer explicação inteligível sobre os fatores que levaram à negativa.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** É exatamente esse tipo de situação — informação sobre o tratamento não fornecida de forma clara e acessível ao titular — que o princípio de transparência visa coibir.

**d.** [ ] Como a LGPD e o GDPR surgiram quase ao mesmo tempo (2018) e tratam do mesmo tema, os dois são, na prática, o mesmo texto legal, só traduzido para o português.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** São leis distintas, de jurisdições distintas, ainda que com princípios convergentes — CSV2 já registra os dois como iniciativas paralelas ("no Brasil, uma lei semelhante também foi aprovada"), não como a mesma lei traduzida.

---

## Conselho vs. lei de dados: dois mecanismos, um gênero

**a.** [ ] Se a Informática brasileira ganhasse um conselho de profissão nos mesmos moldes do CREA, um desenvolvedor não registrado nesse conselho ficaria automaticamente isento das obrigações da LGPD ao tratar dados pessoais em seu trabalho.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** As obrigações da LGPD não dependem de registro em conselho nenhum — regulam a atividade de tratamento de dados, não o exercício licenciado de uma profissão. Os dois mecanismos operam em dimensões diferentes e não se substituem.

**b.** [ ] No limite extremo em que um profissional de Informática nunca trata, em toda a sua carreira, nenhum dado pessoal de terceiros (trabalha só com sistemas puramente internos e anônimos), esse profissional pode, ainda assim, estar sujeito a um eventual conselho de profissão, mas nunca estaria sujeito à LGPD.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Um conselho de profissão regularia o exercício da profissão como tal, independentemente do tipo de sistema trabalhado; a LGPD só se aplica quando há tratamento de dados pessoais — no limite proposto, essa condição nunca se realiza.

**c.** [ ] A lógica de "regular o comportamento, não a identidade de quem o exerce" que caracteriza a LGPD também se aplica, por analogia, a leis de proteção ao consumidor, que regulam como qualquer empresa deve tratar seus clientes, independentemente de haver ou não um conselho profissional de vendedores.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** É o mesmo tipo lógico de mecanismo regulatório — normas que constrangem uma prática (venda, tratamento de dados) por qualquer agente que a realize, em vez de licenciar quem pode realizá-la.

**d.** [ ] Como conselho de profissão e LGPD são as duas formas judicializadas discutidas nesta aula, não existe nenhuma outra forma possível de regular juridicamente a atuação em computação além dessas duas.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** A aula apresenta esses dois como exemplos ilustrativos do "gênero" regulação judicializada, cada um com um mecanismo diferente — não como uma lista exaustiva e fechada de todas as formas possíveis (leis setoriais específicas, normas técnicas com força regulatória, etc., também poderiam se qualificar).

---

## Regulamentação da Informática no Brasil (custos/benefícios)

**a.** [ ] Se a multidisciplinaridade histórica da Informática brasileira não tivesse existido, o argumento de que a regulamentação "reduziria a capacidade técnica multidisciplinar" perderia parte de sua força histórica.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** O argumento se apoia precisamente na observação histórica de que profissionais de formações diferentes contribuíram para construir a área. Sem esse histórico, o argumento teria menos base empírica concreta para se sustentar, ainda que pudesse ser reformulado de outra forma.

**b.** [ ] No limite em que a fiscalização de um conselho de Informática dependesse exclusivamente da posse de diploma, sem qualquer exame prático de competência, essa fiscalização ainda garantiria, por si só, que todo profissional registrado é tecnicamente competente.

**Heurística:** Limite
**Resposta:** Falso
**Justificativa:** É exatamente essa a desvantagem citada no livro-fonte — fiscalização baseada só na posse do diploma é "claramente insuficiente para a defesa da Sociedade"; diploma não é prova suficiente de competência prática continuada.

**c.** [ ] O argumento de que "conselhos não têm meios para preservar empregos nem gerar ganhos financeiros para os profissionais" se aplicaria igualmente a um cenário em que a Informática fosse regulamentada hoje, mesmo num mercado de trabalho completamente diferente do descrito no livro.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** O argumento é sobre a natureza estrutural do que um conselho de profissão pode e não pode fazer (não é um sindicato, não negocia condições de trabalho) — isso não depende das condições específicas de oferta e demanda do mercado em um momento histórico particular.

**d.** [ ] Como o livro-fonte lista várias desvantagens da regulamentação, isso significa que Maciel & Viterbo concluem que a Informática não deveria, de forma alguma, ser regulamentada.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** O próprio livro-fonte encerra a discussão dizendo que a regulamentação "pode gerar vantagens e desvantagens, as quais precisam ser avaliadas com clareza" — uma postura de apresentar o debate aberto, não uma conclusão fechada contra a regulamentação.

---

## Regulamentação da profissão em outros países (comparação internacional)

**a.** [ ] Se os EUA tivessem, desde o início, exigido licenciamento PE obrigatório (não voluntário) para atuar como engenheiro de software, é razoável esperar que o exame não teria sido descontinuado por falta de candidatos em 2019.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** O exame foi descontinuado justamente por baixa adesão voluntária (81 candidatos em 5 aplicações). Se a licença fosse legalmente obrigatória para atuar, a demanda pelo exame teria uma causa estrutural muito mais forte para se manter alta, independentemente de preferência individual.

**b.** [ ] No limite em que a totalidade dos softwares críticos de segurança pública no Canadá passasse a exigir assinatura de um "engineer" licenciado pela APEGA, sem exceções, a exceção aberta por Alberta em 2024 para o título "software engineer" deixaria de ter qualquer efeito prático relevante.

**Heurística:** Limite
**Resposta:** Falso
**Justificativa:** A exceção de Alberta trata do uso do *título*, não de quem pode assinar tecnicamente sistemas críticos. Mesmo com uma hipotética exigência plena de assinatura licenciada para sistemas críticos, a exceção de título continuaria afetando quem pode se autodenominar "software engineer" fora desse subconjunto restrito.

**c.** [ ] O modelo do Chartered IT Professional (CITP) britânico poderia, em princípio, ser adotado no Brasil por uma associação de Informática mesmo sem qualquer mudança na legislação brasileira sobre profissões regulamentadas.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** Por ser um título voluntário sem exigência legal de licença (o mesmo tipo de mecanismo do ACM/IEEE-CS), sua adoção não depende de alteração na lista de profissões regulamentadas do Brasil — qualquer associação poderia, em tese, criar e conceder um título análogo hoje.

**d.** [ ] Como o Canadá protege legalmente o título "engineer" e o Reino Unido não exige licença para "software engineer", isso prova que proteger o título de engenharia necessariamente prejudica a adoção de tecnologia de software no país que a adota.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** A aula não estabelece essa relação causal, e os dados apresentados (tensão sobre um título específico em Alberta) não permitem concluir nada sobre adoção de tecnologia em geral — é uma inferência não sustentada pelo material apresentado.

---

## Autointeresse, *window-dressing* e autorregulação para evitar regulação

**a.** [ ] Se o lema "Don't be Evil" do Google nunca tivesse sido divulgado publicamente, a decisão de censurar buscas na China ainda seria, do ponto de vista discutido na aula, um caso de conflito entre prática comercial e princípios declarados da empresa.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** Sem uma declaração pública de princípios para comparar, o caso perderia exatamente o elemento que o torna um exemplo de *window-dressing* — a lacuna entre imagem projetada e prática real. Sem o lema declarado, seria só uma decisão comercial controversa, não necessariamente um caso de inconsistência entre imagem e prática.

**b.** [ ] No limite em que uma empresa nunca comunica publicamente nenhum valor ou princípio ético, ela se torna estruturalmente imune à crítica de *window-dressing*.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** *Window-dressing* é definido, na fonte, como apresentar uma "impressão favorável que não é baseada nos fatos reais". Sem nenhuma impressão favorável declarada para comparar com a prática, não há uma lacuna a ser exposta desse tipo específico — a empresa ainda poderia ser criticada por outros motivos, só não por esse.

**c.** [ ] A lógica de código de conduta como forma de "silenciar dissidentes" (caso Tozer) se aplicaria também a uma situação em que uma empresa de tecnologia demite um funcionário por violar uma cláusula vaga de "conduta profissional" depois que ele criticou publicamente uma decisão da própria empresa.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** É estruturalmente o mesmo mecanismo — uma cláusula de conduta usada, na prática, para remover quem critica publicamente uma decisão da organização, independentemente de o "conselho" ser uma associação profissional (Tozer) ou a própria empresa empregadora.

**d.** [ ] Como a crítica de autointeresse mostra que códigos podem ser usados para evitar regulação real, conclui-se que toda regulação judicializada (como a LGPD) é sempre superior, em qualquer critério, a qualquer código de autorregulação.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** A aula não faz essa comparação de superioridade geral — mostra que os dois mecanismos têm propósitos e limites diferentes. Um código pode ser genuíno e útil como ponto de partida para julgamento moral (conclusão do Bloco 5), mesmo não tendo a força coercitiva de uma lei.

---

## Vagueza e contradições entre códigos (lealdade, confidencialidade)

**a.** [ ] Se o código do IEEE tivesse uma cláusula de confidencialidade idêntica à do NSPE, o argumento do IEEE em defesa dos engenheiros do BART — de que o código protegia a ação de alertar o público — perderia força.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** Uma cláusula de confidencialidade explícita criaria uma obrigação concorrente dentro do próprio código do IEEE, tornando o apoio à divulgação pública menos direto — parte do que tornava o argumento do IEEE relativamente forte, no caso real, é que o código do IEEE não tinha essa obrigação concorrente.

**b.** [ ] No limite em que um profissional interpreta "lealdade ao empregador" de forma absolutamente acrítica, essa interpretação é, por definição, incompatível com seguir o princípio PUBLIC de qualquer código profissional que o coloque como central.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Lealdade acrítica, por definição (Harris, Pritchard & Rabins), não admite nenhuma consideração acima dos interesses do empregador — isso exclui, por construção, dar prioridade ao interesse público quando os dois entram em conflito, que é justamente o que PUBLIC exige.

**c.** [ ] A inconsistência entre NSPE (informar autoridades) e IEEE (encorajar falar publicamente) é estruturalmente o mesmo tipo de problema que um profissional de Informática enfrentaria hoje se seu código interno dissesse "reportar internamente" enquanto uma lei de proteção ao denunciante sugerisse divulgação externa em certos casos.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** Em ambos os casos, o profissional se depara com fontes normativas distintas (dois códigos; ou um código e uma lei) que recomendam ações diferentes diante do mesmo tipo de situação — a mecânica do conflito normativo é a mesma.

**d.** [ ] Como "lealdade crítica" dá mais espaço para discordar do empregador do que "lealdade acrítica", um profissional que age com lealdade crítica nunca poderá ser acusado de deslealdade por seu empregador.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** A distinção é conceitual/normativa (qual leitura de lealdade é moralmente defensável), não uma garantia prática contra acusação. O próprio caso BART mostra profissionais agindo de forma consistente com lealdade crítica e, ainda assim, sendo tratados pelo empregador como se tivessem sido desleais.

---

## Landon & Landon vs. Ciclo Ético / limites do "viver pelo código"

**a.** [ ] No limite em que um profissional segue rigorosamente todos os cinco passos de Landon & Landon, mas nunca revisita nenhuma etapa depois de tomar sua posição final, o processo continua estruturalmente diferente do Ciclo Ético mesmo assim.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** A diferença apontada na aula não é sobre revisitar ou não na prática, mas sobre a ausência, no processo de Landon & Landon como descrito, de uma fase explícita e nomeada de reflexão final/comparação entre frameworks, equivalente à Fase 5 do Ciclo Ético — essa ausência estrutural persiste independentemente de o profissional, informalmente, decidir voltar atrás.

**b.** [ ] Se o caso Snowden tivesse ocorrido dentro de uma empresa com um conselho de profissão disciplinar e um código de ética formal e específico para o seu cargo, isso teria eliminado a necessidade de qualquer processo de deliberação como o de Landon & Landon ou o Ciclo Ético.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** Mesmo com um código disciplinar aplicável, casos como Snowden envolvem tensões de valores (segurança vs. privacidade, lealdade institucional vs. dever cívico) que um código, por si só, não resolve automaticamente — é o argumento de fechamento da aula: código é ponto de partida, não substituto, do julgamento moral.

**c.** [ ] A observação de que Landon & Landon vem de uma tradição de Sistemas de Informação, e não de ética da engenharia, sugere que seu processo de 5 passos poderia, em princípio, ser aplicado a decisões que nada têm a ver com códigos profissionais de engenharia — por exemplo, uma decisão de negócio sobre como usar dados de clientes.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** O processo (fatos → dilema e valores → interessados → alternativas → consequências) é genérico o suficiente para se aplicar a qualquer decisão com dimensão ética — não está amarrado especificamente a normas de engenharia.

**d.** [ ] Como o processo de Landon & Landon "para" em identificar consequências, sem uma fase formal de reflexão final, ele é estritamente inferior ao Ciclo Ético para qualquer uso prático.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** A própria nota de precisão da aula rejeita essa conclusão — "isso não o torna pior — é mais enxuto, mas menos preparado para lidar com desacordo entre frameworks". Menos uma fase não implica inferioridade geral; é um *trade-off* (mais simples/rápido vs. menos robusto a desacordo).
