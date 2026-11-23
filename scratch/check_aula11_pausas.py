with open("teaching/optimization-linear-algebra/aula11/index.qmd", "r", encoding="utf-8") as f:
    text = f.read()

import re
pausas = re.findall(r'(## .*?Pausa.*?\n(?:.*?\n){1,40}?(?=## |\Z))', text)
for i, p in enumerate(pausas[:6]):
    print(f"--- AULA 11 PAUSA {i+1} ---")
    print(p)
