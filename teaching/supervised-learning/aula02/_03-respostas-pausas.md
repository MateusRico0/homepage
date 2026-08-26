# Respostas das Pausas Ativas — Aula 2

> Arquivo de apoio, não publicado (prefixo `_`). Discute as perguntas
> motivadoras das pausas ativas do `index.qmd` e dá a solução dos
> respectivos V/F. O `index.qmd` publicado só contém a pergunta em
> cada pausa ativa, nunca a resolução (mesmo padrão já estabelecido em
> `unsupervised-learning/aula02`).
>
> (Os 12 blocos de V/F da seção Exercícios do `index.qmd`, se/quando
> existirem, não são discutidos aqui — ficam para o aluno resolver por
> conta, com justificativa disponível só ao professor em
> `_02-solucoes.md`.)

## O que sobrevive da Aula 1

A regra de decisão em si (decidir pela classe de densidade conjunta
maior) sobrevive intacta — sua prova nunca dependeu de haver só duas
classes. O que muda de verdade não é a lógica da regra, é a
dificuldade prática de **estimar** $p(\mathbf{x}\mid\mathcal{C}_k)$
quando $\mathbf{x}$ deixa de ser um número e vira um vetor de muitas
dimensões — um problema qualitativamente novo, não só "mais do mesmo
em maior escala". E generalizar a teoria da decisão para qualquer
função de perda não invalida o caso 2 classes/perda 0-1 da Aula 1: ele
continua sendo um caso particular da versão geral.

- ✔ A prova da Aula 1 nunca usou $K=2$ como hipótese — vale, passo a
  passo, também para $K=5$ classes.
- ✗ Estimar $p(\mathbf{x}\mid\mathcal{C}_k)$ em $\mathbb{R}^{50}$ não é
  "a mesma dificuldade em maior escala" — a maldição da
  dimensionalidade (retomada nesta aula e formalizada na Aula 3 de
  `unsupervised-learning`) é uma dificuldade qualitativamente
  diferente, não apenas quantitativa.
- ✔ A matriz de perda $2\times 2$ da Aula 1 é exatamente o caso
  particular da teoria geral de função de perda (duas classes, perda
  fixa) que esta aula formaliza.
- ✗ Um modelo generativo "sonhar" (gerar dados plausíveis) é uma
  propriedade sobre a **estrutura** do modelo (ele representa
  $p(\mathbf{x}\mid\mathcal{C}_k)$ explicitamente), não uma garantia
  sobre desempenho discriminativo — um modelo discriminativo bem
  ajustado pode classificar melhor que um generativo mal especificado,
  e vice-versa.
