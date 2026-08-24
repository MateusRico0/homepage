## Resumo — Aula 3

Fonte: `_fontes/material/Teoria/Aula 3.tex` ("Composição de Sistemas:
Contratos, Encapsulamento e Estabilidade"). Muda o nível de abstração: das
Aulas 1–2 (a anatomia de um objeto isolado) para a arquitetura de um
**sistema de objetos colaborando**. Cobre a transição de "fabricante de
peças" para "arquiteto de sistemas", o exemplo `Produto`/`ItemCarrinho`/
`Carrinho` como especialistas colaborando, a fronteira Interface vs.
Implementação, a Lei de Demeter (naufrágio de código), *Tell, Don't Ask*
como cura para o acoplamento por fofoca, e a programação para interfaces
como base de sistemas *Plug-and-Play*.

**Pré-requisitos:** Aulas 1–2 completas (encapsulamento, máquina de
estados, `this`).

## Plano de aula — Aula 3 (carga horária estimada: ~120min)

1. **Abertura: de fabricante de peças a arquiteto** (~10 min) — Até agora,
   anatomia de uma peça isolada; a partir de agora, como as peças se
   conectam. Um sistema é uma rede de colaboradores, não um amontoado de
   classes.
2. **Colaboração em ação: `Produto`, `ItemCarrinho`, `Carrinho`** (~20
   min) — Cada classe como especialista autônomo; `ItemCarrinho` não
   calcula preço, pergunta ao `Produto`; `Carrinho` orquestra via
   delegação, sem saber como o subtotal é calculado.
3. **Interface vs. Implementação: a fronteira da estabilidade** (~20 min)
   — O "O Quê" (contrato) vs. o "Como" (detalhe); exemplo
   `ValidadorFinanceiro`/`Compra` — o cliente confia na caixa preta.
4. **Encapsulamento e evolução sem regressão** (~15 min) — `Produto.
   calcularPrecoDeVenda()` V1→V2: a regra de margem muda por completo,
   zero impacto no `Carrinho`, porque a assinatura pública não mudou.
5. **A Lei de Demeter** (~20 min) — "Fale só com amigos próximos"; o
   naufrágio de código (`pedido.getCliente().getCarteira().getSaldo()`);
   cada ponto extra é uma promessa de que o código vai quebrar.
6. **Tell, Don't Ask como a cura técnica** (~15 min) — Delegação em cadeia
   (`Checkout` → `Pedido` → `Cliente`); *Feature Envy* como sintoma de
   violação.
7. **Programando para abstrações: sistemas Plug-and-Play** (~15 min) —
   Interface `Pagavel`; `Checkout.finalizar(Pagavel)` aceita qualquer
   implementação futura sem recompilar; o erro de tipagem como
   diagnóstico de acoplamento forte.
8. **Fechamento e ponte** (~5 min) — Do micro (objeto) ao macro (sistema);
   ponte para a Aula 4: decompor responsabilidades dentro de uma única
   classe (SRP) — o próximo passo depois de já saber conectar classes
   entre si.
