#!/usr/bin/env python3
"""Preview desacoplado da atualização, pra usar em paralelo com agentes.

Problema que resolve: `quarto preview` injeta live-reload no navegador e,
a cada render, navega a aba pra a última página renderizada — muito
disruptivo quando um agente (Claude Code) está editando/renderizando
várias páginas em sequência nos bastidores, porque a aba do usuário pula
de página em página sozinha, sem nenhuma ação do próprio usuário.

Este script builda o site (`quarto render`), sobe um servidor HTTP
totalmente estático (sem live-reload, sem navegação automática) servindo
_site/ na porta 2222, e observa o projeto por mudanças (polling simples
por mtime, sem dependências externas) — quando detecta uma, re-renderiza
só o que for preciso. O navegador só vê a atualização no próximo F5
manual do usuário: acesso ao site e atualização do conteúdo ficam
desvinculados, como pedido.

Uso: ./deploy.sh --watch   (ou: python3 preview-watch.py)
Ctrl+C encerra o servidor e a observação juntos.
"""
import http.server
import os
import socketserver
import subprocess
import sys
import threading
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = os.path.join(ROOT, "_site")
PORT = int(os.environ.get("PREVIEW_PORT", "2222"))

# Diretórios nunca observados: saída do próprio build (_site), cache de
# execução (_freeze), extensões pandoc (raramente mudam), e as pastas de
# ferramenta/ambiente (tudo com "." na frente já cai fora por padrão).
EXCLUDE_DIRS = {"_site", "_freeze", "_extensions"}
WATCH_EXTS = {".qmd", ".py", ".scss", ".css", ".js", ".yml", ".yaml", ".html", ".lua"}
# Arquivos cuja mudança pode afetar mais de uma página — força um render
# completo do projeto em vez de renderizar só o arquivo que mudou.
GLOBAL_FILES = {"_quarto.yml", "styles.css", "custom.scss", "lesson-theme.scss"}
POLL_INTERVAL = 1.5


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def snapshot():
    state = {}
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [
            d for d in dirnames if d not in EXCLUDE_DIRS and not d.startswith(".")
        ]
        for fn in filenames:
            if os.path.splitext(fn)[1] in WATCH_EXTS:
                p = os.path.join(dirpath, fn)
                try:
                    state[p] = os.path.getmtime(p)
                except OSError:
                    pass
    return state


def is_global(path):
    base = os.path.basename(path)
    if base in GLOBAL_FILES:
        return True
    # Scripts de pre-render (publications/generate_*.py, teaching/
    # generate_lesson_nav.py) e módulos compartilhados (src/ de uma
    # disciplina) afetam mais de uma página de saída.
    if base.startswith("generate_") and base.endswith(".py"):
        return True
    parts = os.path.relpath(path, ROOT).split(os.sep)
    if "src" in parts[:-1]:
        return True
    return False


def run_render(cmd):
    # Mesma falha intermitente de fim-de-render já observada com
    # `quarto render` neste projeto (ver deploy.sh) — tenta de novo antes
    # de reportar erro de verdade.
    for attempt in (1, 2, 3):
        result = subprocess.run(cmd, cwd=ROOT)
        if result.returncode == 0:
            return True
        log(f"⚠️  render falhou (tentativa {attempt}/3, código {result.returncode})")
    return False


def render_full():
    log("🔄 mudança em arquivo compartilhado — renderizando o site completo...")
    ok = run_render(["quarto", "render"])
    log("✅ site atualizado." if ok else "❌ render completo falhou 3x — confira o erro acima.")


def render_files(files):
    rel = [os.path.relpath(f, ROOT) for f in files]
    log(f"🔄 renderizando: {', '.join(rel)}")
    ok = run_render(["quarto", "render"] + files)
    log("✅ atualizado." if ok else "❌ falhou — rode `quarto render <arquivo>` manualmente pra ver o erro completo.")


def watch_loop():
    log("👀 observando mudanças no projeto (Ctrl+C encerra tudo)...")
    prev = snapshot()
    while True:
        time.sleep(POLL_INTERVAL)
        cur = snapshot()
        changed = [p for p in cur if cur.get(p) != prev.get(p)]
        if not changed:
            prev = cur
            continue
        only_qmd = all(p.endswith(".qmd") for p in changed)
        if only_qmd and not any(is_global(p) for p in changed):
            render_files(changed)
        else:
            render_full()
        prev = snapshot()


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=SITE_DIR, **kwargs)

    def log_message(self, fmt, *args):
        pass  # silencioso — só as mensagens de render acima importam aqui


def serve():
    with Server(("", PORT), QuietHandler) as httpd:
        log(f"🌐 servindo _site/ em http://localhost:{PORT} (estático, sem live-reload nem navegação automática)")
        httpd.serve_forever()


def main():
    log("🚀 render inicial completo...")
    if not run_render(["quarto", "render"]):
        log("❌ render inicial falhou — corrija o erro antes de continuar.")
        sys.exit(1)
    threading.Thread(target=serve, daemon=True).start()
    try:
        watch_loop()
    except KeyboardInterrupt:
        log("👋 encerrando.")


if __name__ == "__main__":
    main()
