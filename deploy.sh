#!/bin/bash
#
# Substitui o fluxo antigo (Hugo) por Quarto:
#   --render         -> equivalente a `hugo` (build do site) -> `quarto render`
#   --preview        -> equivalente a `hugo server` -> `quarto preview`, na
#                       porta 2222
#   --watch          -> mesma porta 2222, mas SEM live-reload nem navegação
#                       automática (ver preview-watch.py) — usar quando um
#                       agente estiver editando/renderizando páginas nos
#                       bastidores, pra não ficar levando a aba do navegador
#                       pra outra página sozinho a cada render
#   --update-server  -> entra no servidor via SSH e atualiza a pasta do site
#                       (antes "Hugo", agora "homepage") com o que estiver na
#                       branch main
#
# A main agora é protegida no GitHub: merges acontecem por Pull Request pela
# própria interface do GitHub, não por push direto daqui. Este script não
# faz mais commit/push — só builda localmente e/ou puxa a main já mesclada
# no servidor.
#
# Uso:
#   ./deploy.sh --render                  # só renderiza o site localmente
#   ./deploy.sh --preview                 # sobe o preview local na porta 2222
#   ./deploy.sh --watch                   # servidor estático + auto-rebuild, sem navegar a aba
#   ./deploy.sh --update-server           # atualiza o servidor com a main
#   ./deploy.sh --render --update-server  # renderiza local e atualiza o servidor

set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"

SSH_HOST="mraimundo@ssh.ic.unicamp.br"
REMOTE_DIR="homepage"

do_render() {
  echo "🚀 Renderizando o site (quarto render)..."
  # O quarto tem uma falha conhecida e intermitente neste projeto: um erro
  # de "rename"/"stat" no fim do render, mesmo com o site inteiro já
  # construído corretamente (visto repetidamente nesta sessão) — tentamos
  # de novo automaticamente antes de desistir de verdade.
  local attempt
  for attempt in 1 2 3; do
    if quarto render; then
      echo "✅ Site renderizado (_site/)."
      return 0
    fi
    echo "⚠️  Falha na tentativa $attempt/3 (pode ser a falha conhecida do quarto ao final do render) — tentando de novo..."
  done
  echo "❌ Render falhou 3 vezes seguidas. Confira o erro acima."
  return 1
}

do_preview() {
  echo "👀 Subindo o preview local (porta 2222)..."
  quarto preview --port 2222 --no-browser
}

do_watch() {
  echo "👀 Subindo o preview desacoplado (porta 2222, sem live-reload/navegação automática)..."
  python3 preview-watch.py
}

do_update_server() {
  echo "🌐 Atualizando o servidor ($SSH_HOST, pasta $REMOTE_DIR) com a main..."
  ssh "$SSH_HOST" -t "cd $REMOTE_DIR && git checkout main && git pull origin main"
  echo "✅ Publicado."
}

if [[ $# -eq 0 ]]; then
  echo "Uso: $0 [--render] [--preview] [--update-server]"
  exit 1
fi

RENDER=false
PREVIEW=false
WATCH=false
UPDATE_SERVER=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --render)
      RENDER=true
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

if [[ "$RENDER" == true ]]; then
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
