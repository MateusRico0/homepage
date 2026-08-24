// Move o bloco de navegação entre aulas (gerado por
// generate_lesson_nav.py, injetado via include-after-body como um
// <template>) para dentro da barra lateral do TOC — logo depois do
// sumário da própria aula, na mesma coluna, em vez de aparecer solto no
// fim do <body>.
document.addEventListener("DOMContentLoaded", function () {
  var tpl = document.getElementById("lesson-nav-data");
  var sidebar = document.getElementById("quarto-margin-sidebar");
  if (!tpl || !sidebar) return;
  sidebar.appendChild(tpl.content.cloneNode(true));
});
