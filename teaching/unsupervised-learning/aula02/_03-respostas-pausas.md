# Respostas das Pausas Ativas — Aula 2

> Arquivo de apoio, não publicado (prefixo `_`). Discute as 7 perguntas
> motivadoras das pausas ativas do `index.qmd` e dá a solução dos
> respectivos V/F. Antes, essa seção vivia dentro do `index.qmd`
> publicado (`# Respostas da Aula`) — movida para cá a pedido do
> usuário ("as respostas da aula estão no material, deveriam estar
> separadas"). O `index.qmd` agora só contém a pergunta em cada pausa
> ativa, nunca a resolução.
>
> (Os 12 blocos de V/F da seção Exercícios do `index.qmd` **não** são
> discutidos aqui — ficam para o aluno resolver por conta, com
> justificativa disponível só ao professor em `_02-solucoes.md`.)

## O que quebra quando $d$ cresce

Mesmo com $N>d$, $\hat\Sigma$ tem $d(d+1)/2$ parâmetros — cresce
quadraticamente, então a qualidade da estimativa por dimensão cai
conforme $d$ aumenta. Mas o problema não é só de contagem: é
geométrico (bloco da maldição da dimensionalidade). E nenhum método
escapa por completo — $k$-NN e KDE sofrem sua própria versão, mais
adiante.

- ✔ Mais parâmetros que dados por direção degrada a estimativa.
- ✗ Só contagem de parâmetros, sem geometria.
- ✗ $k$-NN livre de qualquer maldição.
- ✔ Intuição de baixa dimensão falha em alta dimensão.

## Por que as duas curvas do preview concordam

Concordam porque são duas contas diferentes para a mesma pergunta —
"quantos pacientes parecidos há perto de $x$?" — uma fixando o número
de vizinhos e medindo a distância, a outra fixando a distância (via
peso decrescente) e somando quantos contribuem. Os blocos seguintes
mostram que vêm, de fato, da mesma identidade matemática ($K/(NV)$).

- ✔ Concordam por responderem à mesma pergunta de formas opostas.
- ✗ Concordariam do mesmo jeito ordenando por prontuário em vez de por
  proximidade — as duas contas dependem inteiramente da posição real
  em `radius_mean`, não da ordem de listagem.
- ✗ Todos com o mesmo valor, curvas ainda diferentes nesse ponto — as
  duas disparariam juntas nesse caso extremo (máxima concentração
  possível).
- ✔ As duas usam a posição de cada paciente no eixo.

## O que quebra primeiro quando distâncias deixam de discriminar

Quebra os dois — ordenação de vizinhos fica instável, e estimativas de
densidade baseadas em distância perdem poder discriminativo. Adicionar
dimensões de ruído piora isso; não existe "sempre melhora" com mais
dimensões.

- ✔ Ordem dos $k$ vizinhos fica sensível a ruído.
- ✔ Contraste zero → escolha por proximidade tão informativa quanto
  aleatória.
- ✗ Mais dimensões de ruído sempre melhora a estimativa.
- ✔ $e_p(r)=r^{1/p}$ cresce para 1 conforme $p$ aumenta.

## A tensão interna de $K/(NV)$

Não é uma contradição: é um trade-off, resolvido de formas diferentes
por $k$-NN (adaptando $V$) e KDE (fixando $V=h^D$ e aceitando o
trade-off via escolha de $h$).

- ✔ $V$ pequeno para densidade quase constante.
- ✔ $V$ grande para $K$ confiável.
- ✗ Nenhum valor de $V$ funciona na prática.
- ✔ Cada rota resolve a tensão de um jeito diferente.

## O limite $K=N$ no $k$-NN

$K=N$ borra tudo — o análogo exato do $h\to\infty$ do KDE. $K=1$ em
ponto coincidente diverge. A suavização adaptativa (item c) é a
propriedade central que distingue $k$-NN de KDE no bloco de comparação.

- ✔ $d_N(\mathbf{x})$ quase constante, densidade quase uniforme.
- ✔ $K=1$ em ponto coincidente diverge.
- ✔ Variação de $d_K$ menor em região densa que na cauda.
- ✗ Não integrar a 1 impede comparação relativa.

## O limite $h\to\infty$ no KDE

$h\to\infty$ borra tudo (análogo a $K=N$); $h\to 0$ vira soma de
deltas. O mesmo $h$ absoluto suaviza proporcionalmente mais um conjunto
concentrado que um espalhado — por isso $h$ deveria, idealmente, se
adaptar à escala dos dados.

- ✔ $h\to\infty$ borra tudo, análogo a $K=N$.
- ✔ $h\to 0$ vira soma de deltas.
- ✗ Mesmo $h$ fixo dá o mesmo grau de suavização relativa em escalas
  diferentes.
- ✔ $h$ equivalente a $\Delta$ do histograma.

## Concordância entre métodos independentes

Dois métodos com mecanismos de suavização diferentes concordando sobre
uma estrutura é evidência de que ela é real, não um artefato de
escolha de método — a lógica central por trás de usar $k$-NN e KDE lado
a lado.

- ✔ Concordância entre KDE e $k$-NN sugere estrutura real.
- ✔ KDE suaviza demais na fronteira, $k$-NN se adapta.
- ✔ Nenhum herda a restrição $N>d$ (mas ambos herdam outra versão da
  maldição).
- ✔ Comparação relativa continua válida sem normalizar.
