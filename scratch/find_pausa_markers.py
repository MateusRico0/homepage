with open("teaching/optimization-linear-algebra/aula12/index.qmd", "r", encoding="utf-8") as f:
    text = f.read()

import re

for i in [1, 2, 3, 4]:
    pattern = rf'::: \{{.content-visible when-format="html" unless-format="revealjs"\}}\s*\n## Pausa {i}:'
    m = re.search(pattern, text)
    if m:
        print(f"Pausa {i} HTML start: {m.start()}")
    else:
        print(f"Pausa {i} HTML start NOT FOUND")

