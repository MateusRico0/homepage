#!/bin/bash
#
# Wrapper fino sobre preview-watch.py:
#   --incremental -> renderiza só o que mudou desde o último render
#                    bem-sucedido (marcador .last-render — ver
#                    preview-watch.py). Se um --watch já estiver rodando,
#                    pede a ELE pra renderizar agora (via sentinela — ver
#                    preview-watch.py) em vez de subir um segundo processo
#                    concorrente.
#   --watch       -> servidor estático na porta 2222 servindo _site/ (sem
#                    live-reload nem navegação automática — ver
#                    preview-watch.py) + observação contínua do projeto,
#                    renderizando incrementalmente sempre que algo muda.
#
# Sem comando pra render completo forçado nem pra deploy/limpeza — pra
# isso, rode `quarto render` (ou `rm -rf _freeze _site`) diretamente.
#
# Uso:
#   ./site-manager.sh --incremental   # renderiza só o que mudou desde o último --incremental
#   ./site-manager.sh --watch         # servidor estático + auto-rebuild, sem navegar a aba
#
# Chamado via `uv run ./site-manager.sh ...` (não direto) garante o Python
# certo (>=3.13, ver pyproject.toml) independente do que `python3` resolve
# no PATH do shell. Todo lugar que este script invoca Python internamente
# (abaixo) já usa `uv run` por conta própria, então funciona mesmo chamado
# sem o prefixo — mas `uv run` na invocação externa é o padrão recomendado.

set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"

do_incremental() {
  echo "🚀 Renderizando o que mudou desde o último --incremental (ver .last-render)..."
  # Delega pro preview-watch.py: mesma lógica de classificação (por
  # arquivo/tipo) usada pelo --watch, e o mesmo retry automático pra
  # falha intermitente conhecida do quarto (erro de "rename"/"stat" no
  # fim do render). `uv run` garante o Python certo (ver comentário de
  # topo) mesmo que este script seja chamado sem o prefixo `uv run` por
  # fora.
  uv run python3 preview-watch.py --incremental
}

do_watch() {
  echo "👀 Subindo o preview desacoplado (porta 2222, sem live-reload/navegação automática)..."
  uv run python3 preview-watch.py
}

if [[ $# -eq 0 ]]; then
  echo "Uso: $0 [--incremental] [--watch]"
  exit 1
fi

INCREMENTAL=false
WATCH=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --incremental)
      INCREMENTAL=true
      shift
      ;;
    --watch)
      WATCH=true
      shift
      ;;
    *)
      echo "Opção desconhecida: $1"
      exit 1
      ;;
  esac
done

if [[ "$INCREMENTAL" == true ]]; then
  do_incremental
fi

# --watch por último e sempre em primeiro plano: fica bloqueado servindo
# até Ctrl+C, então não faz sentido combinar com passos que viriam depois.
if [[ "$WATCH" == true ]]; then
  do_watch
fi
