// Transforma o sumário nativo do Quarto (#TOC, "Nesta página") num
// painel de acordeão colapsável ("Nesta aula").
document.addEventListener("DOMContentLoaded", function () {
  // Move os links "Slides" e "Lista de aulas" (ícones, ver styles.css)
  // pra dentro do cabeçalho de metadados da aula, como colunas extras ao
  // lado de Autor e Data de Publicação — pedido explícito do usuário, no
  // lugar de botões soltos logo abaixo do cabeçalho. Anexados como
  // filhos DIRETOS de .quarto-title-meta (não dentro do <div> da data)
  // pra virarem caixas quadradas iguais às outras duas (ver
  // `.quarto-title-meta > a.see-all` em styles.css). Roda antes/
  // independente do resto do script (acordeão do TOC), que não existe
  // em toda página. Esta página só tem esses dois links `.see-all` (as
  // páginas com o pílula "SEE ALL" da home não carregam este script).
  var titleMeta = document.querySelector(".quarto-title-meta");
  if (titleMeta) {
    document.querySelectorAll("a.see-all").forEach(function (link) {
      var oldParagraph = link.parentElement;
      titleMeta.appendChild(link);
      // O <p> que embrulhava o link fica vazio depois do appendChild
      // acima (que MOVE o nó, não copia) — remove pra não sobrar um
      // espaço em branco onde o botão costumava estar.
      if (
        oldParagraph &&
        oldParagraph.tagName === "P" &&
        oldParagraph.childNodes.length === 0
      ) {
        oldParagraph.remove();
      }
    });
  }

  var toc = document.getElementById("TOC");
  if (!toc) return;

  var header = toc.querySelector("#toc-title");
  var body = toc.querySelector("ul");
  if (!header || !body) return;

  header.textContent = "Nesta aula";
  header.setAttribute("role", "button");
  header.setAttribute("tabindex", "0");
  header.setAttribute("aria-expanded", "true");
  header.classList.add("toc-accordion-open");

  var icon = document.createElement("i");
  icon.className = "bi bi-chevron-down toc-accordion-icon";
  icon.setAttribute("aria-hidden", "true");
  header.appendChild(icon);

  function toggle() {
    var opening = header.getAttribute("aria-expanded") !== "true";
    header.setAttribute("aria-expanded", String(opening));
    body.style.display = opening ? "" : "none";
    header.classList.toggle("toc-accordion-open", opening);
  }

  header.addEventListener("click", toggle);
  header.addEventListener("keydown", function (e) {
    if (e.key === "Enter" || e.key === " ") {
      e.preventDefault();
      toggle();
    }
  });
});
