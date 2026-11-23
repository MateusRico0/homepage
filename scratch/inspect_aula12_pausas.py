with open("teaching/optimization-linear-algebra/aula12/index.qmd", "r", encoding="utf-8") as f:
    text = f.read()

import re
pausas = re.findall(r'(## Pausa.*?\n(?:.*?\n){1,35}?(?=## |\Z))', text)
for i, p in enumerate(pausas):
    print(f"--- PAUSA {i+1} ---")
    print(p[:400])
    print("...")
