import re

path = "teaching/optimization-linear-algebra/aula12/index.qmd"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

print("File loaded, total length:", len(text))
