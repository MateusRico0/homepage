# Referência de conteúdo — templates e detalhes de formato

Consultado sob demanda pelas etapas do ciclo em `CLAUDE.md`. Não precisa ser relido em toda sessão.

## Esqueleto do `index.qmd` {#esqueleto}

Copie o YAML (`format:`, `jupyter: homepage`, `execute:`) e o bloco de links do topo de uma aula recente, de preferência a última aprovada da mesma disciplina.

```markdown
::: {.content-visible when-format="html" unless-format="revealjs"}
[Slides](slides.html){.see-all ...} [Lista de aulas](../index.qmd){.see-all .lesson-list-link ...}
:::

```{python}
#| echo: false
# SETUP GLOBAL — imports, paleta COR_A/COR_B/COR_NEU (mesma das aulas anteriores),
# dataset-fio, e todo cálculo cujo número aparece no texto
```

# Revisão e Introdução
## Revisão Cuidadosa: O Que a Aula N-1 Deixou Pronto   (notas)  |  ## Da Aula N-1: O Que Já Temos (slides)
## Ideia Central
## Roteiro da Aula
## Problema Motivador
## <Pausa Ativa>

# Intuição — <imagem mental>
# Bloco 1: <título>          (... uma Pausa Ativa ao fim de cada bloco)
# Bloco k: <título>

# Fechamento
## Retomando as N Perguntas
## O Que Fica em Aberto
## Ponte para a Aula N+1
[Exercícios](exercicios.qmd){.see-all .exercicios-link} [Soluções](soluções.qmd){.see-all .solucoes-link}
```

Cada `##` de conteúdo existe em duas versões intercaladas: o bloco de notas (prosa) e o bloco de slides (fragmentos), com o chunk de figura compartilhado logo depois dos dois.

## Pausa Ativa {#pausa-ativa}

Fica fora de `content-visible` (aparece nas notas e nos slides). A resposta fica só nos slides.

```markdown
## <Tema curto>

::: {.callout-tip}
## <Pergunta aberta provocadora?>

<Dica para conduzir a discussão.>
:::

::: {.callout-tip}
## <Tema do V/F>

Julgue V ou F — a questão só conta se acertar os 4 itens:

- □ Afirmação 1.
- □ Afirmação 2.
- □ Afirmação 3.
- □ Afirmação 4.
:::

::: {.content-visible when-format="revealjs"}

## <Tema curto> — Resposta

::: {.callout-tip}
## <Tema do V/F> — Resposta

- ✔ <por que é verdadeira, 1–2 linhas>.
- ✗ <o erro conceitual exato, 1–2 linhas>.
- ...
:::

::: {.fragment}
**Voltando à pergunta:** <resposta da pergunta aberta, 2–4 linhas>.
:::

:::
```

- Os V/F ajudam o raciocínio da pergunta aberta, mas testam ângulos próprios. Não repartem a resposta da aberta em itens. Os itens seguem as heurísticas de `#metodologia-vf`.
- Glifos seguros (texto puro): `□` U+25A1, `✔` U+2714, `✗` U+2717. Proibidos: `- [ ]`, `☐` U+2610 e `☒` U+2612, que o `task_lists` do Pandoc transforma em `<input type="checkbox">`.
- `_02-respostas-pausas.md` (oculto): para cada pausa, a discussão da pergunta aberta e os V/F resolvidos com justificativa.

## Slides {#slides}

- **Fragmentos:** `::: {.fragment}` (não `. . .`). A mensagem-chave do slide pode ser `::: {.fragment .callout-important}` e uma definição, `::: {.callout-note .fragment icon=false}`. Prefira itens `- ` curtos a um parágrafo denso num fragmento. Em provas, quebre as linhas com `\`.
- **Rótulos em negrito** ajudam a ler o slide sozinho: `**O que calculamos:** ...`, `**O que realmente queremos:** ...`, `**Guardar:** ...` (valores que voltam mais adiante).
- **Derivação em vários slides:** o slide de continuação começa com um fragmento "Onde o Passo k parou:" e a equação completa.
- **Slide vazio:** título + frase curta, ou texto que sobrou de uma figura que ficou no slide anterior. Há duas saídas: acrescentar conteúdo substantivo (explicação, citação, outra perspectiva) ou fundir com o vizinho.
- **Revisão de picotamento** (depois de cada bloco): leia só a lista de `##` do bloco em sequência (`grep -n '^## ' index.qmd`). Funda os slides quando (i) um slide tem um único fragmento curto e o vizinho continua a mesma ideia, (ii) uma figura está sozinha e o comentário dela mora no slide seguinte, ou (iii) 3+ slides lidos em voz alta soam como um parágrafo cortado. Ao fundir, reescreva a transição; não basta concatenar.
- **Figuras:** `::: {.fig-resize style="width: XX%; margin: 0 auto;"}` em volta de todo chunk de figura e de todo `{.tikz}`. Use 60–80% para um gráfico simples e 100% para painéis. O `figsize` do matplotlib define as proporções.

## Datasets — Hugging Face Hub {#datasets}

Todos carregam com `load_dataset(repo_id)`, sem token. O kernel `homepage` (`uv sync`) já tem `datasets`/`huggingface_hub`.

| Dataset — repo | Linhas | Uso | Observações |
|---|---|---|---|
| Adult / Census Income — `scikit-learn/adult-census-income` | 32.561 | Classificação binária, atributos mistos (NB, árvores, logística) | — |
| Breast Cancer Wisconsin — `scikit-learn/breast-cancer-wisconsin` | 569 | Classificação binária médica, 30 contínuos; fio de Sup 4 e NSup 3–5.1 (`radius_worst`, `concave points_worst`) | Descartar `id`, `Unnamed: 32` |
| Pima Indians Diabetes — `khoaguin/pima-indians-diabetes-database` | 768 | Médico, contínuo multivariado (Sup 1: `Glucose`; NSup 1: Mahalanobis) | Alvo já é `y` |
| California Housing — `gvlassis/california_housing` | 20.640 (train/val/test) | Regressão, 8 contínuos, escalas diferentes (Sup 3 e 5, álgebra) | — |
| Default of Credit Card Clients — `Lancer73/uci-credit-card-default` | 30.000 (train/val/test) | Crédito, binária, histórico de pagamento (árvores, ensembles) | — |
| German Credit — `AiresPucrs/german-credit-data` | 1.000 | Crédito, categóricos + numéricos (NB com tipos mistos) | Pequeno |
| Credit Card Fraud — `dazzle-nu/CIS435-CreditCardFraudDetection` | ~1,05 M | Anomalia com atributos interpretáveis | Subamostrar; descartar `Unnamed: 0`, `Unnamed: 23`, `6006`; muito desbalanceado |
| MNIST — `ylecun/mnist` | 60.000 treino + 10.000 teste | Imagens 28×28 (autoencoders, VAE, geração) | `load_dataset("ylecun/mnist", split="train").with_format("numpy")`; `np.asarray(ds["image"], dtype=np.float32).reshape(-1, 784) / 255` |

```python
from huggingface_hub.utils import logging as hf_logging
hf_logging.set_verbosity_error()      # sem aviso "unauthenticated requests" na saída
from datasets import disable_progress_bar, load_dataset
disable_progress_bar()                # sem barra de progresso na saída
ds = load_dataset("scikit-learn/breast-cancer-wisconsin")["train"].to_pandas()
```

Use sempre o id completo `dono/nome`: ids de um segmento só (`"mnist"`, `"gpt2"`) quebram nas versões atuais do `huggingface_hub`. Um dataset novo deve ser testado (carrega sem token? as colunas batem?) antes de entrar na aula. Se for reutilizável, acrescente-o à tabela.

## Plano de aula — template {#plano-de-aula}

```markdown
## Resumo — Aula N
[5–10 linhas: cobertura, objetivos, pré-requisitos (conferidos no dicionário de notações), dataset-fio]

**Estratégia Pedagógica:** [A (Outside-In) | B (Inside-Out com Problema-Fio)] — [justificativa em 1 linha]

## Plano de aula — Aula N (carga horária: XX min)
1. **Revisão e Introdução** (~10 min) — ...
2. **Intuição — ...** (~10 min) — ...
3. **Bloco 1: ...** (~XX min) — [o que cobre; como termina e o que o bloco seguinte resolve]
...
N. **Fechamento** (~5 min) — [Ponte para a Aula N+1]

## Fontes usadas — Aula N
### Fonte 1: PRML, §1.5.1, pp. 39–41
**Uso pretendido:** ...
**Trecho:**
> "texto literal, língua original, extraído do PDF"
```

## Exercícios e soluções {#exercicios}

**`exercicios.qmd`:**

```markdown
---
title: "Exercícios — Aula N: <título>"
subtitle: "<Disciplina>"
date: "today"
author: "Marcos M. Raimundo — Instituto de Computação, UNICAMP"
lang: pt-BR
toc: true
toc-depth: 2
format:
  html:
    include-after-body: ../../lesson-toc-accordion.html   # obrigatório: leva os links ao cabeçalho
    theme: [flatly, ../../../custom.scss, ../../lesson-theme.scss]
    number-sections: false
---

[Aula](index.qmd){.see-all .aula-link aria-label="Ver aula" title="Ver aula"}
[Soluções](soluções.qmd){.see-all .solucoes-link aria-label="Ver soluções" title="Ver soluções"}

::: {.callout-tip icon=false}
O gabarito comentado das questões de Verdadeiro/Falso está em
[`soluções.qmd`](soluções.qmd). Encontrou um erro numa questão? Corrija
diretamente neste arquivo e abra um *pull request*.
:::

## Contexto e notação
[resumo autocontido das definições/notação/exemplo que os itens usam]

## Questões discursivas

1. <enunciado autocontido>
2. ...

## Questões de Verdadeiro/Falso

::: {.callout-note icon=false}
## Teste 1 — <Tema>

- □ ...   (4 itens)
:::
```

- **Quantidade:** 2–3 discursivas e 6–10 testes (de 4 itens cada), ajustados à densidade da aula. Um teste só conta se os 4 itens estiverem certos (em prova, deixar em branco custa 20% da questão).
- **Numeração:** `Teste N — Tema`, recomeçando em 1 a cada aula, na ordem do arquivo. O prefixo "Teste" é exclusivo do V/F.
- **Autocontido:** nunca "os pontos B e C desta aula" nem notação definida só na aula. Se o item precisar dela, redefina-a em `## Contexto e notação` ou num preâmbulo curto do teste.
- **Fonte das questões:** pode reaproveitar questões de fim de capítulo, citando a origem; questões originais são sinalizadas como tais.

**`soluções.qmd`:** o mesmo YAML, com os links `[Aula](index.qmd){.see-all .aula-link}` e `[Exercícios](exercicios.qmd){.see-all .exercicios-link}`. Só os testes de V/F (as discursivas não têm gabarito publicado). Cada teste vira um par de caixas:

```markdown
::: {.callout-note icon=false}
## Teste N — <Tema>

- □ <afirmação idêntica a exercicios.qmd>.
- ...
:::

::: {.callout-tip}
## (Resposta) Teste N — <Tema>

- ✔ Verdadeiro — <por quê, apontando o erro conceitual de quem marcou F>.
- ✗ Falso — <por quê>.
:::
```

A heurística usada em cada item não aparece no arquivo.

### Metodologia dos itens de V/F {#metodologia-vf}

Vale para Pausas Ativas e Exercícios. Quem decorou sem entender a mecânica deve errar; quem entendeu acerta sem nunca ter visto a frase. Cada item nasce de uma destas heurísticas (a lista não é exaustiva):

1. **Contrafactual:** inverter uma premissa essencial e afirmar a consequência.
2. **Caso limite:** $N\to\infty$, $\lambda\to 0$, ausência total de um fator.
3. **Transferência de domínio:** um cenário que não apareceu na aula, **sempre dentro de ML** (outro modelo/arquitetura, outro dataset da tabela acima, outra técnica com a mesma estrutura matemática). Nunca física, engenharia civil, ecologia ou controle industrial.
4. **Falsa equivalência:** usa o jargão certo, mas erra a relação de causa e efeito.

**Proibido:** "o que é X"; paráfrase literal da aula; falsidade que dependa só de trocar uma palavra (sempre↔nunca); transferência para fora de ML.

## `_progresso.md` — formato {#progresso}

É lido no início de toda sessão da disciplina, então precisa ser curto (alvo: menos de 10 KB). Guarda só o que a próxima aula precisa. O histórico de correções, as validações feitas ("renderizou sem erro") e os números de verificação ficam no git ou na própria aula.

```markdown
# Progresso — <Disciplina>

**Fontes** (`_fontes/`; deslocamento página impressa → PDF): ...
**Dataset-fio / exemplos-fio:** ...
**Combinados da disciplina:** (decisões do usuário que valem para todas as aulas)

## Estado das aulas
| Pasta | Aula | Estratégia | Dataset-fio | Estado |

## Fio condutor
- **N:** o que a aula estabeleceu (1–2 linhas). **Ponte:** o que ela promete para a N+1.

## Dicionário de notações   (ou "Vocabulário", nas disciplinas não matemáticas)
| Símbolo/termo | Significado | Aula |

## Pendências
- só itens em aberto; apague o item quando for resolvido.
```
