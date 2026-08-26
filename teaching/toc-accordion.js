// Transforma o sumário nativo do Quarto (#TOC, "Nesta página") e a
// navegação entre aulas (.lesson-nav, "Aulas do curso" — injetada por
// lesson-nav.js antes deste script rodar) num acordeão de dois painéis:
// "Nesta aula" (aberto por padrão) e "Outras aulas" (fechado por
// padrão) — abrir um fecha o outro. Quando a disciplina só tem uma
// aula (sem .lesson-nav), o TOC ainda fica colapsável, só sem par.
document.addEventListener("DOMContentLoaded", function () {
  // Move o link "Slides →" (com o ícone, ver styles.css) pra dentro do
  // cabeçalho de metadados da aula, como uma terceira "coluna" ao lado
  // de Autor e Data de Publicação — pedido explícito do usuário, no
  // lugar do botão solto logo abaixo do cabeçalho. Anexado como filho
  // DIRETO de .quarto-title-meta (não dentro do <div> da data) pra virar
  // uma terceira caixa quadrada igual às outras duas (ver
  // `.quarto-title-meta > a.see-all` em styles.css). Roda antes/
  // independente do resto do script (acordeão do TOC), que não existe
  // em toda página.
  var slidesLink = document.querySelector('a.see-all[href$="slides.html"]');
  var titleMeta = document.querySelector(".quarto-title-meta");
  if (slidesLink && titleMeta) {
    var oldParagraph = slidesLink.parentElement;
    titleMeta.appendChild(slidesLink);
    // O <p> que embrulhava o link fica vazio depois do appendChild acima
    // (que MOVE o nó, não copia) — remove pra não sobrar um espaço em
    // branco onde o botão costumava estar.
    if (
      oldParagraph &&
      oldParagraph.tagName === "P" &&
      oldParagraph.childNodes.length === 0
    ) {
      oldParagraph.remove();
    }
  }

  var sidebar = document.getElementById("quarto-margin-sidebar");
  var toc = document.getElementById("TOC");
  if (!sidebar || !toc) return;

  var panels = [];

  function makePanel(header, body, label) {
    if (!header || !body) return null;
    header.textContent = label;
    header.setAttribute("role", "button");
    header.setAttribute("tabindex", "0");

    var icon = document.createElement("i");
    icon.className = "bi bi-chevron-down toc-accordion-icon";
    icon.setAttribute("aria-hidden", "true");
    header.appendChild(icon);

    var panel = { header: header, body: body };

    function setOpen(open) {
      header.setAttribute("aria-expanded", String(open));
      body.style.display = open ? "" : "none";
      header.classList.toggle("toc-accordion-open", open);
    }

    function toggle() {
      var opening = header.getAttribute("aria-expanded") !== "true";
      panels.forEach(function (p) {
        p.setOpen(p === panel ? opening : false);
      });
    }

    panel.setOpen = setOpen;
    header.addEventListener("click", toggle);
    header.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        toggle();
      }
    });

    panels.push(panel);
    return panel;
  }

  var tocHeader = toc.querySelector("#toc-title");
  var tocBody = toc.querySelector("ul");
  var tocPanel = makePanel(tocHeader, tocBody, "Nesta aula");

  var lessonNav = sidebar.querySelector(".lesson-nav");
  var lessonPanel = null;
  if (lessonNav) {
    var lessonHeader = lessonNav.querySelector(".lesson-nav-title");
    var lessonBody = lessonNav.querySelector("ol");
    lessonPanel = makePanel(lessonHeader, lessonBody, "Outras aulas");
  }

  if (tocPanel) tocPanel.setOpen(true);
  if (lessonPanel) lessonPanel.setOpen(false);
});
