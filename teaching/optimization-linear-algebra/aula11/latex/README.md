# Slides da Aula 11 em LaTeX Beamer

Este diretório contém a versão completa e autocontida dos slides da **Aula 11: Otimização de Segunda Ordem (Método de Newton) e Precondicionamento Diagonal** em **LaTeX Beamer**.

Projetado para ser 100% independente do Quarto: qualquer docente ou colega pode abrir, editar e compilar diretamente no Overleaf, TeXShop, VS Code (LaTeX Workshop) ou terminal.

---

## Estrutura do Diretório

```
teaching/optimization-linear-algebra/aula11/latex/
├── slides.tex          # Código-fonte LaTeX Beamer com todos os 43 slides
├── README.md           # Este guia de uso
└── figures/            # Figuras e logotipos incluídos na apresentação
    ├── UNICAMP.png
    ├── IC.png
    ├── basin_deformation.png    # Deformação métrica da bacia elíptica
    └── adagrad_vs_rmsprop.png   # Dinâmica comparada AdaGrad vs. RMSProp
```

---

## Como Compilar

### 1. No Overleaf
1. Crie um projeto novo ("Blank Project").
2. Arraste ou faça upload de:
   - `slides.tex`
   - A pasta `figures/` com todas as imagens.
3. Clique em **Recompile** (utilize o compilador padrão `pdfLaTeX`).

### 2. No Terminal (Linux / macOS / Windows com TeX Live / MacTeX / MiKTeX)
Basta executar:

```bash
pdflatex slides.tex
pdflatex slides.tex   # segunda passada para acertar os números de slides no rodapé
```

---

## Características do Template

* **Formato Widescreen:** Configurado em proporção 16:9 (`aspectratio=169`), idêntico aos projetores modernos e aos slides web.
* **Identidade Visual Unicamp / IC:** Paleta com azul marinho (`#182B49`), ciano (`#0284C7`), verde (`#10B981`) e rodapé elegante com número de slide e identificação institucional.
* **Caixas de Destaque (Callouts):** Mapeadas para blocos nativos do Beamer (`block`, `exampleblock`, `alertblock`) com cantos arredondados e cores do tema (`calloutnote`, `callouttip`, `calloutwarning`, `calloutimportant`), garantindo compilação instantânea e limpa em qualquer distribuição.
* **Pausas Interativas:** Itens de Verdadeiro ou Falso formatados com comandos limpos `\qmark`, `\cmark` e `\xmark`.

