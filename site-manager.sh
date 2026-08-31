#!/bin/bash
#
# Substitui o fluxo antigo (Hugo) por Quarto:
#   --render         -> renderiza só o que mudou desde o último --render
#                       bem-sucedido (marcador .last-render — ver
#                       preview-watch.py). Rápido no dia a dia; NÃO
#                       garante que TUDO esteja em dia (ver --render-all).
#   --render-all     -> força um `quarto render` completo do site inteiro,
#                       sem checar o que mudou. Use antes de publicar de
#                       verdade, ou se desconfiar que o incremental deixou
#                       algo pra trás.
#   --preview        -> equivalente a `hugo server` -> `quarto preview`, na
#                       porta 2222
#   --watch          -> mesma porta 2222, mas SEM live-reload nem navegação
#                       automática (ver preview-watch.py) — usar quando um
#                       agente estiver editando/renderizando páginas nos
#                       bastidores, pra não ficar levando a aba do navegador
#                       pra outra página sozinho a cada render. Também
#                       renderiza incrementalmente ao subir.
#   --update-server  -> entra no servidor via SSH, atualiza a pasta do site
#                       (antes "Hugo", agora "homepage") com o que estiver na
#                       branch main, e renderiza lá (uv run ./site-manager.sh
#                       --render-all) — o servidor passou a renderizar o
#                       próprio site em vez de só servir um _site/ já
#                       renderizado localmente e sincronizado via git.
#
# A main agora é protegida no GitHub: merges acontecem por Pull Request pela
# própria interface do GitHub, não por push direto daqui. Este script não
# faz mais commit/push — só builda localmente e/ou puxa a main já mesclada
# no servidor (e renderiza lá).
#
# Uso:
#   ./site-manager.sh --render                  # renderiza só o que mudou desde o último --render
#   ./site-manager.sh --render-all              # força renderizar o site inteiro
#   ./site-manager.sh --preview                 # sobe o preview local na porta 2222
#   ./site-manager.sh --watch                   # servidor estático + auto-rebuild, sem navegar a aba
#   ./site-manager.sh --update-server           # atualiza o servidor com a main e renderiza lá
#   ./site-manager.sh --render-all --update-server  # renderiza tudo local e atualiza+renderiza o servidor
#
# Chamado via `uv run ./site-manager.sh ...` (não direto) garante o Python
# certo (>=3.13, ver pyproject.toml) independente do que `python3` resolve
# no PATH do shell — foi exatamente a falta disso que quebrou os scripts de
# pre-render (`str | None`, sintaxe que o Python 3.6 do sistema do servidor
# não entende) na primeira tentativa de renderizar lá. Todo lugar que este
# script invoca Python internamente (abaixo) já usa `uv run` por conta
# própria, então funciona mesmo chamado sem o prefixo — mas `uv run` na
# invocação externa é o padrão recomendado, principalmente no servidor.

set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"

SSH_HOST="mraimundo@ssh.ic.unicamp.br"
REMOTE_DIR="homepage"

do_render() {
  echo "🚀 Renderizando o que mudou desde o último --render (ver .last-render)..."
  # Delega pro preview-watch.py: mesma lógica de classificação (por
  # arquivo/tipo) usada pelo --watch, e o mesmo retry automático pra
  # falha intermitente conhecida do quarto (erro de "rename"/"stat" no
  # fim do render). `uv run` garante o Python certo (ver comentário de
  # topo) mesmo que este script seja chamado sem o prefixo `uv run` por
  # fora.
  uv run python3 preview-watch.py --once
}

do_render_all() {
  echo "🚀 Renderizando o site inteiro (forçado)..."
  uv run python3 preview-watch.py --render-all
}

do_preview() {
  echo "👀 Subindo o preview local (porta 2222)..."
  quarto preview --port 2222 --no-browser
}

do_watch() {
  echo "👀 Subindo o preview desacoplado (porta 2222, sem live-reload/navegação automática)..."
  uv run python3 preview-watch.py
}

do_update_server() {
  echo "🌐 Atualizando o servidor ($SSH_HOST, pasta $REMOTE_DIR) com a main..."
  ssh "$SSH_HOST" -t "cd $REMOTE_DIR && git checkout main && git pull origin main"
  echo "🚀 Renderizando no servidor..."
  # PATH do servidor não tem quarto/uv por padrão (instalados sem root em
  # ~/tools e ~/.local/bin, ver investigação de viabilidade) — precisa
  # declarar aqui, já que cada `ssh host 'comando'` é um shell novo, sem
  # o PATH de nenhuma sessão interativa anterior.
  ssh "$SSH_HOST" -t "cd $REMOTE_DIR && export PATH=\"\$HOME/tools/quarto-1.10.18/bin:\$HOME/.local/bin:\$PATH\" && uv run ./site-manager.sh --render-all"
  echo "✅ Publicado."
}

if [[ $# -eq 0 ]]; then
  echo "Uso: $0 [--render] [--render-all] [--preview] [--watch] [--update-server]"
  exit 1
fi

RENDER=false
RENDER_ALL=false
PREVIEW=false
WATCH=false
UPDATE_SERVER=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --render)
      RENDER=true
      shift
      ;;
    --render-all)
      RENDER_ALL=true
      shift
      ;;
    --preview)
      PREVIEW=true
      shift
      ;;
    --watch)
      WATCH=true
      shift
      ;;
    --update-server)
      UPDATE_SERVER=true
      shift
      ;;
    *)
      echo "Opção desconhecida: $1"
      exit 1
      ;;
  esac
done

if [[ "$RENDER_ALL" == true ]]; then
  do_render_all
elif [[ "$RENDER" == true ]]; then
  do_render
fi

if [[ "$UPDATE_SERVER" == true ]]; then
  do_update_server
fi

# --preview/--watch por último e sempre em primeiro plano: ficam
# bloqueados servindo até Ctrl+C, então não faz sentido combinar com
# passos que viriam depois (e os dois juntos não fazem sentido: disputariam
# a mesma porta 2222).
if [[ "$PREVIEW" == true ]]; then
  do_preview
elif [[ "$WATCH" == true ]]; then
  do_watch
fi
