## Resumo — Aula 13: Princípios de *Data Feminism* e Colaboração Interdisciplinar

Nas Aulas 6, 7 e 12, estudamos como vieses entram no pipeline de dados, quais são os limites matemáticos das métricas de *fairness* e como o *Value Sensitive Design* (VSD) traduz valores em requisitos de engenharia. Contudo, essas abordagens costumam partir de uma pergunta técnica ("como corrigir o modelo ou balancear valores dado um problema?") sem questionar **quem detém o poder de definir o problema, escolher o que é medido e decidir quais dados sequer existem**.

Esta aula introduz os **7 princípios do *Data Feminism*** (D'Ignazio & Klein, 2020), fundamentados no feminismo interseccional, como lente analítica e prática para a ciência de dados e a computação. Em vez de tratar dados como reflexo neutro da realidade, examinamos a matriz de dominação por trás da coleta, classificação, modelagem, visualização e trabalho invisível de dados, articulando essa crítica com a **colaboração interdisciplinar** e artefatos concretos de engenharia responsável (*Datasheets for Datasets*, *Model Cards* e co-design participativo).

**Objetivos:**
1. Distinguir abordagens focadas apenas em "ética/viés no modelo" de abordagens de **justiça de dados** que analisam assimetrias estruturais de poder.
2. Compreender e aplicar os **7 princípios do *Data Feminism*** ao longo do ciclo de vida de sistemas computacionais (da formulação do problema à visualização e implantação).
3. Identificar ***missing datasets*** (conjuntos de dados ausentes) e o papel de ***counterdata*** (contra-dados) na exposição de desigualdades institucionais.
4. Reconhecer o **trabalho invisível** (*ghost work*, rotulagem, limpeza, moderação) e as implicações políticas de esquemas de classificação e binários em bancos de dados e modelos.
5. Estruturar práticas genuínas de **colaboração interdisciplinar** e documentação sociotécnica (*Datasheets for Datasets*, *Model Cards*) no desenvolvimento de software e IA.

**Pré-requisitos:** Sistema sociotécnico (Aula 1); os quatro espaços dos dados e os cinco vieses (Aula 6); atributo sensível $Z$, cegueira de atributo e teorema da impossibilidade de *fairness* (Aula 7); tecnologia persuasiva e arquitetura de escolha (Aulas 5 e 11); *Value Sensitive Design* e Hierarquia de Valores (Aula 12).
**Estratégia Pedagógica:** A (*Outside-In*) — Parte de dois casos reais contrastantes (*Gender Shades* e os contra-dados de feminicídio de Maria Salguero) $\to$ Intuição sobre objetividade situada e matriz de dominação $\to$ Os 7 princípios do *Data Feminism* mapeados no pipeline técnico $\to$ Colaboração interdisciplinar e artefatos de engenharia.
**Casos-Fio:**
1. ***Gender Shades* (Buolamwini & Gebru, 2018):** Auditoria interseccional de classificadores comerciais de gênero que expôs taxas de erro drasticamente maiores para mulheres de pele escura — revelando falhas de representatividade e poder na definição de benchmarks.
2. **Contra-dados de feminicídio (Maria Salguero, México):** Mapeamento independente construído diante da omissão e inconsistência dos registros oficiais do Estado (*missing datasets* e *counterdata*).

---

## Plano de aula — Aula 13 (carga horária: ~100–110 min)

1. **Revisão e Introdução: Quem Pergunta o Quê aos Dados?** (~12 min)
   - *Revisão:* Aulas 6–7 (vieses de representação/social e métricas de *fairness* sobre atributo sensível $Z$) e Aula 12 (VSD e Árvores de Valores).
   - *Ideia Central:* Mesmo com métricas de *fairness* e Árvores de Valores bem especificadas, permanece a pergunta anterior ao código: **quem tem poder para decidir o que é coletado, como as categorias são definidas e quais danos contam como "erro"?** O *Data Feminism* usa o feminismo interseccional para investigar e desafiar o poder na ciência de dados.
   - *Problema Motivador:* O contraste entre **super-representação/erro interseccional** no *Gender Shades* (classificadores faciais com <1% de erro para homens de pele clara e até 34,7% para mulheres de pele escura) e **ausência deliberada de dados** no mapa de feminicídios de Maria Salguero.
   - *Roteiro (4 Perguntas Centrais):*
     1. Por que "remover viés do modelo" ou aplicar VSD não basta sem examinar quem detém o poder sobre os dados?
     2. Como os 7 princípios do *Data Feminism* operam em cada etapa do pipeline computacional?
     3. O que são *missing datasets* e *counterdata*, e o que eles revelam sobre a suposta neutralidade dos dados?
     4. Como a colaboração interdisciplinar e o reconhecimento do trabalho invisível transformam a prática técnica?
   - *Pausa 1.*

2. **Intuição — A "Vista de Lugar Nenhum" e a Matriz de Dominação** (~10 min)
   - A ilusão da objetividade desincorporada (*god trick*, Donna Haraway): toda base de dados e todo gráfico são produzidos a partir de um ponto de vista situado.
   - Da **ética de dados** (foco em conformidade, acurácia, privacidade individual) para a **justiça de dados** (foco em poder estrutural e redistribuição).
   - A **Matriz de Dominação** (Patricia Hill Collins): quatro domínios de poder (estrutural, disciplinar, hegemônico e interpessoal) e como eles aparecem em sistemas computacionais.
   - Diagrama TikZ contrastando *Ética de Dados (centrada no artefato)* vs. *Justiça de Dados / Data Feminism (centrada em poder e contexto)*.

3. **Bloco 1: Os Princípios 1 a 4 — Poder, Contra-Dados, Emoção e Binários** (~25 min)
   - **Princípio 1 — Examinar o poder (*Examine Power*):** Quem financia, quem coleta, quem é alvo de vigilância? Assimetria entre quem produz dados e quem os controla.
   - **Princípio 2 — Desafiar o poder (*Challenge Power*):** O conceito de ***missing datasets*** (Mimi Onuoha) e ***counterdata*** (contra-dados): por que certos fenômenos sociais têm telemetria minuciosa e outros não têm registro algum? Caso Maria Salguero.
   - **Princípio 3 — Elevar a emoção e a corporeidade (*Elevate Emotion and Embodiment*):** Desconstrução do mito de que gráficos minimalistas e "neutros" são objetivos enquanto narrativas visuais com apelo humano são "enviesadas". Toda visualização é retórica.
   - **Princípio 4 — Repensar binários e hierarquias (*Rethink Binaries and Hierarchies*):** Do `ENUM('M', 'F')` no schema SQL à classificação binária de gênero/raça/risco; todo sistema de classificação cria fronteiras políticas e exclui quem não cabe na caixa (Bowker & Star).
   - *Pausa 2.*

4. **Bloco 2: Os Princípios 5 a 7 — Pluralismo, Contexto e Trabalho Invisível** (~25 min)
   - **Princípio 5 — Abraçar o pluralismo (*Embrace Pluralism*):** Conhecimento situado e participação de múltiplos saberes. Conexão com a sub-representação de gênero e diversidade nas equipes de TI (Maciel & Viterbo, Vol. 1, Cap. 4 e Vol. 2, Cap. 10): equipes homogêneas naturalizam suas próprias experiências como "padrão universal".
   - **Princípio 6 — Considerar o contexto (*Consider Context*):** "Os números não falam por si." Separar dados de seu contexto histórico e institucional (ex.: usar boletins policiais como proxy de criminalidade) transforma desigualdade histórica em "fato objetivo".
   - **Princípio 7 — Tornar o trabalho visível (*Make Labor Visible*):** Ocultamento do trabalho humano por trás da "automação" e da "IA mágica": anotadores de dados, moderadores de conteúdo, curadores e mantenedores (*ghost work*).
   - Diagrama/quadro TikZ mapeando os **7 Princípios ao longo do pipeline de Ciência de Dados** (Formulação $\to$ Coleta/Schema $\to$ Rotulagem $\to$ Modelagem $\to$ Visualização $\to$ Implantação).
   - *Pausa 3.*

5. **Bloco 3: Colaboração Interdisciplinar e Operacionalização Técnica** (~20 min)
   - Por que a interdisciplinaridade falha quando reduzida a "chamar um especialista de Humanas para revisar o produto pronto".
   - Práticas concretas de colaboração interdisciplinar e engenharia responsável:
     1. **Co-design e formulação conjunta do problema:** integrar cientistas sociais, juristas, profissionais do domínio e comunidades afetadas na definição do objetivo e das métricas.
     2. **Artefatos de fronteira (*boundary objects*):** *Datasheets for Datasets* (Gebru et al., 2021) e *Model Cards* (Mitchell et al., 2019) para documentar origem, lacunas, trabalho de anotação e limites de uso.
     3. **Design de recusa (*refusal*) e não-coleta:** reconhecer quando a solução ética não é "melhorar o modelo", mas não coletar o dado ou não construir o sistema.
   - *Pausa 4.*

6. **Fechamento** (~8 min)
   - *Retomando as 4 Perguntas:* quadro-síntese consolidando as respostas da aula.
   - *O Que Fica em Aberto:* tensões entre prazos industriais, incentivos comerciais e práticas participativas; quem financia e mantém contra-dados?
   - *Ponte para a Aula 14:* Se dados, modelos e documentação envolvem trabalho coletivo e poder, quem controla a propriedade, as licenças e o acesso ao código e ao conhecimento? $\to$ **Aula 14: *Commons*: Software Livre, Licenciamento e Conhecimento Aberto**.

---

## Fontes usadas — Aula 13

### Fonte 1: D'Ignazio, C. & Klein, L. F. (2020) — *Data Feminism* (MIT Press)
**Uso pretendido:** Estrutura conceitual central da aula: os 7 princípios do *Data Feminism*, conceitos de matriz de dominação (Patricia Hill Collins), objetividade situada / *god trick* (Donna Haraway), *missing datasets*, *counterdata*, visualização incorporada, repensar binários e tornar o trabalho visível.
*(Nota: obra em acesso aberto em data-feminism.mitpress.mit.edu; não há PDF local em `_fontes/` neste ambiente.)*

### Fonte 2: Maciel, C. & Viterbo, J. (2020) — *Computação e Sociedade*, Vol. 1, Cap. 4 ("Gênero e Tecnologias") e Vol. 2, Cap. 10 ("Cultura na Prática da Computação")
**Uso pretendido:** Contextualização brasileira sobre participação de gênero na computação, cultura organizacional e impacto da diversidade na concepção de sistemas sociotécnicos (Bloco 2 e Bloco 3).
*(Nota: o symlink `_fontes/Computação e Sociedade` não está montado neste ambiente, portanto não foram extraídos trechos literais com número de página.)*

### Fonte 3: Buolamwini, J. & Gebru, T. (2018) — "Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification" (*PMLR* 81)
**Uso pretendido:** Caso-fio 1 (Problema Motivador e Bloco 1): auditoria interseccional (gênero × tom de pele) demonstrando como benchmarks e classificadores comerciais falham sistematicamente para mulheres negras.

### Fonte 4: Gebru, T. et al. (2021) — "Datasheets for Datasets" (*Communications of the ACM*, 64(12)) & Mitchell, M. et al. (2019) — "Model Cards for Model Reporting" (*FAT\**)
**Uso pretendido:** Bloco 3: operacionalização da contextualização de dados, explicitação do trabalho de coleta/anotação e documentação interdisciplinar de limites de uso.
