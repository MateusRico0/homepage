// Transforma o sumário nativo do Quarto (#TOC, "Nesta página") e a
// navegação entre aulas (.lesson-nav, "Aulas do curso" — injetada por
// lesson-nav.js antes deste script rodar) num acordeão de dois painéis:
// "Nesta aula" (aberto por padrão) e "Outras aulas" (fechado por
// padrão) — abrir um fecha o outro. Quando a disciplina só tem uma
// aula (sem .lesson-nav), o TOC ainda fica colapsável, só sem par.
document.addEventListener("DOMContentLoaded", function () {
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
