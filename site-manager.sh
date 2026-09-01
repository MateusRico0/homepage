#!/bin/bash
#
# Substitui o fluxo antigo (Hugo) por Quarto:
#   --render             -> renderiza só o que mudou desde o último --render
#                           bem-sucedido (marcador .last-render — ver
#                           preview-watch.py). Se um --watch já estiver
#                           rodando, pede a ELE pra renderizar agora (via
#                           sentinela — ver preview-watch.py) em vez de subir
#                           um segundo processo concorrente.
#   --render-all         -> força um `quarto render` completo do site
#                           inteiro, sem checar o que mudou. Mesma
#                           cooperação com um --watch já rodando que
#                           --render tem. Use antes de publicar de verdade,
#                           ou se desconfiar que o incremental deixou algo
#                           pra trás.
#   --watch              -> servidor estático na porta 2222 servindo _site/
#                           (sem live-reload nem navegação automática — ver
#                           preview-watch.py) + observação contínua do
#                           projeto, renderizando incrementalmente sempre
#                           que algo muda.
#   --clean              -> apaga _freeze/ e _site/ (e o marcador
#                           .last-render, pra forçar o próximo render a ser
#                           completo). NUNCA roda sozinho — só quando esse
#                           comando é passado explicitamente. _freeze/ vai
#                           pro git de propósito (cache de execução, ver
#                           .gitignore), então isso apaga conteúdo versionado
#                           da árvore de trabalho — recuperável com
#                           `git checkout -- _freeze`, mas destrutivo pra
#                           qualquer mudança local ainda não commitada nele.
#   --update-server      -> entra no servidor via SSH, atualiza a pasta do
#                           site com o que estiver na branch main, e roda
#                           --render lá (incremental).
#   --update-server-all  -> igual --update-server, mas roda --render-all lá
#                           (completo).
#
# A main agora é protegida no GitHub: merges acontecem por Pull Request pela
# própria interface do GitHub, não por push direto daqui. Este script não
# faz mais commit/push — só builda localmente e/ou puxa a main já mesclada
# no servidor (e renderiza lá).
#
# Uso:
#   ./site-manager.sh --render                      # renderiza só o que mudou desde o último --render
#   ./site-manager.sh --render-all                  # força renderizar o site inteiro
#   ./site-manager.sh --watch                       # servidor estático + auto-rebuild, sem navegar a aba
#   ./site-manager.sh --clean                       # apaga _freeze/, _site/ e o marcador de último render
#   ./site-manager.sh --update-server               # atualiza o servidor com a main e renderiza lá (incremental)
#   ./site-manager.sh --update-server-all           # atualiza o servidor com a main e renderiza lá (completo)
#   ./site-manager.sh --render-all --update-server-all  # renderiza tudo local e atualiza+renderiza tudo no servidor
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

do_watch() {
  echo "👀 Subindo o preview desacoplado (porta 2222, sem live-reload/navegação automática)..."
  uv run python3 preview-watch.py
}

do_clean() {
  echo "🧹 Apagando _freeze/, _site/ e o marcador .last-render..."
  rm -rf _freeze _site .last-render
  echo "✅ Limpo — o próximo --render ou --watch vai fazer um render completo do zero."
}

remote_pull() {
  echo "🌐 Atualizando o servidor ($SSH_HOST, pasta $REMOTE_DIR) com a main..."
  ssh "$SSH_HOST" -t "cd $REMOTE_DIR && git checkout main && git pull origin main"
}

# PATH do servidor não tem quarto/uv por padrão (instalados sem root em
# ~/tools e ~/.local/bin, ver investigação de viabilidade) — precisa
# declarar aqui, já que cada `ssh host 'comando'` é um shell novo, sem
# o PATH de nenhuma sessão interativa anterior.
REMOTE_PATH_EXPORT='export PATH="$HOME/tools/quarto-1.10.18/bin:$HOME/.local/bin:$PATH"'

do_update_server() {
  remote_pull
  echo "🚀 Renderizando (incremental) no servidor..."
  ssh "$SSH_HOST" -t "cd $REMOTE_DIR && $REMOTE_PATH_EXPORT && uv run ./site-manager.sh --render"
  echo "✅ Publicado."
}

do_update_server_all() {
  remote_pull
  echo "🚀 Renderizando (completo) no servidor..."
  ssh "$SSH_HOST" -t "cd $REMOTE_DIR && $REMOTE_PATH_EXPORT && uv run ./site-manager.sh --render-all"
  echo "✅ Publicado."
}

if [[ $# -eq 0 ]]; then
  echo "Uso: $0 [--render] [--render-all] [--watch] [--clean] [--update-server] [--update-server-all]"
  exit 1
fi

RENDER=false
RENDER_ALL=false
WATCH=false
CLEAN=false
UPDATE_SERVER=false
UPDATE_SERVER_ALL=false

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
    --watch)
      WATCH=true
      shift
      ;;
    --clean)
      CLEAN=true
      shift
      ;;
    --update-server)
      UPDATE_SERVER=true
      shift
      ;;
    --update-server-all)
      UPDATE_SERVER_ALL=true
      shift
      ;;
    *)
      echo "Opção desconhecida: $1"
      exit 1
      ;;
  esac
done

# --clean primeiro: se vier combinado com --render/--render-all na mesma
# chamada, o render que vier a seguir já parte do zero.
if [[ "$CLEAN" == true ]]; then
  do_clean
fi

if [[ "$RENDER_ALL" == true ]]; then
  do_render_all
elif [[ "$RENDER" == true ]]; then
  do_render
fi

if [[ "$UPDATE_SERVER_ALL" == true ]]; then
  do_update_server_all
elif [[ "$UPDATE_SERVER" == true ]]; then
  do_update_server
fi

# --watch por último e sempre em primeiro plano: fica bloqueado servindo
# até Ctrl+C, então não faz sentido combinar com passos que viriam depois.
if [[ "$WATCH" == true ]]; then
  do_watch
fi
