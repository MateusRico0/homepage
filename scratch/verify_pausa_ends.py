with open("teaching/optimization-linear-algebra/aula12/index.qmd", "r", encoding="utf-8") as f:
    text = f.read()

end_markers = [
    "# Bloco 2: O Gradiente Acelerado de Nesterov (NAG)",
    "# Bloco 3: Otimizador Adam — A Fusão do Momento com a Escala Adaptativa",
    "# Bloco 4: A Cirurgia Crítica — Do $L_2$ Regularization ao AdamW",
    "## O Que Fica em Aberto"
]

for idx, marker in enumerate(end_markers, start=1):
    pos = text.find(marker)
    print(f"End marker {idx} '{marker[:30]}...': pos={pos}")
