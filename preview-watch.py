#!/usr/bin/env python3
"""Preview desacoplado da atualização, pra usar em paralelo com agentes.

Problema que resolve: `quarto preview` injeta live-reload no navegador e,
a cada render, navega a aba pra a última página renderizada — muito
disruptivo quando um agente (Claude Code) está editando/renderizando
várias páginas em sequência nos bastidores, porque a aba do usuário pula
de página em página sozinha, sem nenhuma ação do próprio usuário.

Modo padrão (sem argumentos): builda o site (incremental — ver
"Render incremental" abaixo), sobe um servidor HTTP totalmente estático
(sem live-reload, sem navegação automática) servindo _site/ na porta
2222, e observa o projeto por mudanças (polling simples por mtime, sem
dependências externas) — quando detecta uma, re-renderiza só o que for
preciso. O navegador só vê a atualização no próximo F5 manual do
usuário: acesso ao site e atualização do conteúdo ficam desvinculados,
como pedido.

Render incremental: em vez de "qualquer arquivo global muda -> renderiza
o site inteiro", cada arquivo alterado é classificado (ver
CLASSIFY_HELP abaixo) e só o subconjunto de páginas realmente afetado é
renderizado — a maioria das mudanças (uma aula, uma pessoa, um projeto)
afeta só 1-2 páginas, não as 200+ do site inteiro.

Modos de linha de comando (usados por site-manager.sh):
  python3 preview-watch.py            # modo live: render incremental + servidor + observação contínua
  python3 preview-watch.py --once     # um único render incremental (desde o último) e sai, sem servidor
  python3 preview-watch.py --render-all  # um render completo forçado e sai, sem servidor

--once e --render-all cooperam com um serviço --watch já rodando em vez de
falhar ou disputar um segundo `quarto render`: pedem o render (incremental
ou completo, respectivamente) AO serviço já de pé, via sentinela
(.render-once / .render-all — ver request_from_running_service()), e só
retornam depois que ele termina.

Ctrl+C encerra o servidor e a observação juntos (modo live).
"""
import fcntl
import http.server
import os
import re
import shutil
import socketserver
import subprocess
import sys
import threading
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = os.path.join(ROOT, "_site")
PORT = int(os.environ.get("PREVIEW_PORT", "2222"))
LOCK_PATH = os.path.join(ROOT, ".preview-watch.lock")
LAST_RENDER_MARKER = os.path.join(ROOT, ".last-render")
RENDER_ALL_TRIGGER = ".render-all"
RENDER_ONCE_TRIGGER = ".render-once"

# Diretórios nunca observados: saída do próprio build (_site), cache de
# execução (_freeze), extensões pandoc (raramente mudam), e as pastas de
# ferramenta/ambiente (tudo com "." na frente já cai fora por padrão).
EXCLUDE_DIRS = {"_site", "_freeze", "_extensions"}
WATCH_EXTS = {".qmd", ".py", ".scss", ".css", ".js", ".yml", ".yaml", ".html", ".lua"}

# --- Classificação de arquivos não-.qmd (CLASSIFY_HELP) --------------------
#
# Nem todo arquivo fora de uma página específica precisa de um render
# completo do site — a maioria afeta só um subconjunto bem definido:
#
# COPY_ONLY: referenciado como link/script EXTERNO (<link>, <script src>)
# em vez de colado dentro do HTML — não passa pela compilação de tema do
# Quarto, então uma mudança não muda o conteúdo renderizado de nenhuma
# página. Só precisa ser copiado pra dentro de _site/, sem chamar
# `quarto render` de jeito nenhum.
COPY_ONLY_FILES = {"styles.css"}

# LESSON_ONLY_GLOBAL: colado dentro do HTML de toda aula
# (include-after-body/include-in-header) ou usado no tema (theme: [...])
# só das aulas — muda o conteúdo renderizado das ~19 aulas, nunca de
# publicações/projetos/pessoas. Dispara um render das aulas (os dois
# formatos, HTML e RevealJS), não do site inteiro.
LESSON_ONLY_GLOBAL_FILES = {
    "lesson-theme.scss",
    "logos-footer.html",
    "bootstrap-icons-header.html",
    "toc-accordion.js",
    "lesson-toc-accordion.html",
}

# TRUE_GLOBAL: afeta o tema/comportamento de toda página do site (não só
# das aulas) — esses sim justificam um render completo automático.
TRUE_GLOBAL_FILES = {"_quarto.yml", "custom.scss", "band-sections.lua", "participants.lua", "links.lua"}

# Únicos .html legitimamente editados à mão na árvore-fonte (os três
# partials acima) — qualquer outro .html fora de _site/ é sempre saída
# de render perdida, nunca autoria manual (ver o filtro em snapshot()).
HTML_PARTIALS = {"logos-footer.html", "bootstrap-icons-header.html", "lesson-toc-accordion.html"}

LESSON_QMD_RE = re.compile(r"^teaching/[^/]+/aula\d+/index\.qmd$")
DISCIPLINE_SRC_RE = re.compile(r"^teaching/([^/]+)/src/")

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
            # Arquivo com "_" na frente (ex.: _lesson-nav.html) é sempre
            # gerado por um pre-render script, nunca editado à mão (é a
            # própria convenção do Quarto — ver teaching/CLAUDE.md) — sem
            # excluir, o próprio render regenerava esses arquivos e o
            # watcher se via disparando outro render sozinho.
            if fn.startswith("_") and fn not in (RENDER_ALL_TRIGGER, RENDER_ONCE_TRIGGER):
                continue
            ext = os.path.splitext(fn)[1]
            if fn not in (RENDER_ALL_TRIGGER, RENDER_ONCE_TRIGGER) and ext not in WATCH_EXTS:
                continue
            if ext == ".html" and fn not in HTML_PARTIALS:
                # .html solto na árvore-fonte nunca é editado à mão neste
                # projeto — só existe de verdade dentro de _site/ (já
                # ignorado). Um .html aqui só pode ser saída de render
                # perdida fora de _site/ (já visto ao vivo: uma corrida
                # entre dois `quarto render` concorrentes gravou
                # index.html/people/*.html direto na árvore-fonte). Sem
                # este filtro, esse arquivo perdido vira "mudança" a cada
                # poll, e o watcher entra num loop se auto-disparando pra
                # sempre — foi exatamente essa a causa de um segundo loop
                # infinito real já visto em produção aqui, além do já
                # corrigido em publications/_retreiver/person_bibliography.py.
                continue
            p = os.path.join(dirpath, fn)
            try:
                state[p] = os.path.getmtime(p)
            except OSError:
                pass
    return state


def find_lesson_files(discipline_filter=None):
    lessons = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [
            d for d in dirnames if d not in EXCLUDE_DIRS and not d.startswith(".")
        ]
        if "index.qmd" not in filenames:
            continue
        rel_dir = os.path.relpath(dirpath, ROOT).replace(os.sep, "/")
        m = re.match(r"^teaching/([^/]+)/aula\d+$", rel_dir)
        if m and (discipline_filter is None or m.group(1) == discipline_filter):
            lessons.append(os.path.join(dirpath, "index.qmd"))
    return lessons


def find_discipline_index_files():
    # teaching/<disciplina>/index.qmd (a página pública do curso, uma por
    # disciplina) — não confundir com teaching/<disciplina>/aulaNN/index.qmd
    # (find_lesson_files acima). Usado só quando toc-accordion.js muda: esse
    # script também roda nessas páginas agora (relocaliza o link do ícone
    # do PDD pra dentro de .quarto-title-meta, igual faz com Slides/Lista de
    # aulas nas aulas), então uma mudança nele precisa re-renderizá-las.
    files = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [
            d for d in dirnames if d not in EXCLUDE_DIRS and not d.startswith(".")
        ]
        if "index.qmd" not in filenames:
            continue
        rel_dir = os.path.relpath(dirpath, ROOT).replace(os.sep, "/")
        if re.match(r"^teaching/[^/]+$", rel_dir):
            files.append(os.path.join(dirpath, "index.qmd"))
    return files


def run_render(cmd):
    # Mesma falha intermitente de fim-de-render já observada com
    # `quarto render` neste projeto (ver site-manager.sh) — tenta de novo antes
    # de reportar erro de verdade.
    for attempt in (1, 2, 3):
        result = subprocess.run(cmd, cwd=ROOT)
        if result.returncode == 0:
            return True
        log(f"⚠️  render falhou (tentativa {attempt}/3, código {result.returncode})")
    return False


def touch_marker():
    with open(LAST_RENDER_MARKER, "w") as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S"))


def render_full():
    log("🔄 renderizando o site completo...")
    ok = run_render(["quarto", "render"])
    log("✅ site atualizado." if ok else "❌ render completo falhou 3x — confira o erro acima.")
    if ok:
        touch_marker()
    return ok


def render_lessons(files):
    files = sorted(set(files))
    rel = [os.path.relpath(f, ROOT) for f in files]
    log(f"🔄 renderizando aula(s) — HTML + slides: {', '.join(rel)}")
    # Sem --to explícito, `quarto render <arquivo>` só gera o formato
    # padrão (o primeiro listado no front matter, normalmente html) —
    # cada aula tem DOIS formatos de saída (notas + slides) do mesmo
    # index.qmd, então sem isso o RevealJS ficava desatualizado toda vez
    # que uma aula mudava via render incremental.
    ok = run_render(["quarto", "render"] + files + ["--to", "html"])
    ok = run_render(["quarto", "render"] + files + ["--to", "revealjs"]) and ok
    log("✅ atualizado." if ok else "❌ falhou — rode `quarto render <arquivo>` manualmente pra ver o erro completo.")
    return ok


def render_files(files):
    files = sorted(set(files))
    rel = [os.path.relpath(f, ROOT) for f in files]
    log(f"🔄 renderizando: {', '.join(rel)}")
    ok = run_render(["quarto", "render"] + files)
    log("✅ atualizado." if ok else "❌ falhou — rode `quarto render <arquivo>` manualmente pra ver o erro completo.")
    return ok


def copy_static(files):
    for p in files:
        rel = os.path.relpath(p, ROOT)
        dest = os.path.join(SITE_DIR, rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy2(p, dest)
        log(f"📄 copiado direto (sem render — é um <link>/<script> externo): {rel}")


def plan_and_render(changed):
    """Classifica os arquivos mudados e renderiza só o necessário.
    Retorna True se tudo deu certo (ou não havia nada a fazer)."""
    changed = list(changed)
    basenames = {os.path.basename(p) for p in changed}

    if RENDER_ONCE_TRIGGER in basenames:
        log(f"🔄 {RENDER_ONCE_TRIGGER} tocado — render incremental pedido explicitamente.")
        sentinel_path = os.path.join(ROOT, RENDER_ONCE_TRIGGER)
        # exclude=... evita que o snapshot() interno de
        # run_incremental_since_marker() veja a própria sentinela (ainda
        # no disco neste ponto) como "mudada" e reentre neste mesmo
        # bloco — ver o docstring do parâmetro. A sentinela só é apagada
        # DEPOIS que o render termina (não antes), pra
        # request_render_once_from_running_service() continuar esperando
        # até o render de verdade acabar, e não só até a sentinela sumir.
        ok = run_incremental_since_marker(exclude={sentinel_path})
        try:
            os.remove(sentinel_path)
        except OSError:
            pass
        return ok

    if RENDER_ALL_TRIGGER in basenames:
        log(f"🔄 {RENDER_ALL_TRIGGER} tocado — render completo pedido explicitamente.")
        ok = render_full()
        # Apaga a sentinela depois de processar: é como `--render-all`
        # (rodando num terminal separado, sem conseguir a trava porque
        # este serviço já está de pé) sabe que o pedido foi atendido —
        # ver request_render_all_from_running_service().
        try:
            os.remove(os.path.join(ROOT, RENDER_ALL_TRIGGER))
        except OSError:
            pass
        return ok

    if any(os.path.basename(p) in TRUE_GLOBAL_FILES for p in changed):
        return render_full()

    copy_only = [p for p in changed if os.path.basename(p) in COPY_ONLY_FILES]
    remaining = [p for p in changed if p not in copy_only]

    needs_all_lessons = any(
        os.path.basename(p) in LESSON_ONLY_GLOBAL_FILES for p in remaining
    )
    remaining = [
        p for p in remaining if os.path.basename(p) not in LESSON_ONLY_GLOBAL_FILES
    ]

    # toc-accordion.js também roda nas páginas de disciplina (índice do
    # curso), não só nas aulas — ver find_discipline_index_files(). Checa
    # o basename ANTES do filtro de LESSON_ONLY_GLOBAL_FILES acima, que já
    # tirou o arquivo de `remaining` nesse ponto.
    needs_discipline_index = "toc-accordion.js" in basenames

    lesson_targets = set(find_lesson_files()) if needs_all_lessons else set()
    other_targets = find_discipline_index_files() if needs_discipline_index else []

    for p in remaining:
        rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
        if LESSON_QMD_RE.match(rel):
            lesson_targets.add(p)
            continue
        if rel.endswith(".qmd"):
            other_targets.append(p)
            continue
        m = DISCIPLINE_SRC_RE.match(rel)
        if m:
            # Módulo Python compartilhado entre as aulas de UMA
            # disciplina (teaching/<disciplina>/src/*.py) — afeta só as
            # aulas dessa disciplina, não o site inteiro.
            lesson_targets.update(find_lesson_files(m.group(1)))
            continue
        base = os.path.basename(p)
        if base.startswith("generate_") and base.endswith(".py"):
            # Script de pre-render — roda antes de QUALQUER render e
            # pode afetar múltiplas páginas de formas não-óbvias (ex.:
            # que seções aparecem em qual perfil). Edição rara; mais
            # seguro tratar como afetando o site inteiro.
            return render_full()
        # Qualquer outro tipo de arquivo não previsto explicitamente
        # acima — mais seguro que "esquecer" de renderizar algo.
        return render_full()

    ok = True
    if copy_only:
        copy_static(copy_only)
    if lesson_targets:
        ok = render_lessons(lesson_targets) and ok
    if other_targets:
        ok = render_files(other_targets) and ok
    if ok:
        touch_marker()
    return ok


def watch_loop():
    log("👀 observando mudanças no projeto (Ctrl+C encerra tudo)...")
    prev = snapshot()
    for trigger in (RENDER_ALL_TRIGGER, RENDER_ONCE_TRIGGER):
        sentinel = os.path.join(ROOT, trigger)
        if sentinel in prev:
            # A sentinela já existia antes deste primeiro snapshot (ex.:
            # alguém pediu --render-all/--render bem durante o render de
            # startup deste serviço, que roda ANTES do watch_loop existir
            # — pode levar bem mais que POLL_INTERVAL num projeto deste
            # tamanho). Sem este check, ela já nasce "de sempre" no
            # baseline acima e o diff de mtime nunca a veria como
            # mudança — quem pediu ficaria esperando pra sempre.
            log(f"🔄 {trigger} já estava pendente antes deste serviço começar a observar — processando agora.")
            plan_and_render([sentinel])
            prev = snapshot()
    while True:
        time.sleep(POLL_INTERVAL)
        cur = snapshot()
        changed = [p for p in cur if cur.get(p) != prev.get(p)]
        if not changed:
            prev = cur
            continue
        plan_and_render(changed)
        # Usa o snapshot de ANTES do render (`cur`), não um novo
        # snapshot tirado depois — um render (mesmo de um arquivo só)
        # pode levar vários segundos, e qualquer edição feita NESSE
        # meio-tempo (num arquivo diferente do que disparou o render)
        # já teria seu mtime novo "engolido" por um snapshot pós-render,
        # nunca mais sendo detectada como mudança. Bug real: editar dois
        # arquivos em sequência rápida fazia o segundo nunca ser
        # renderizado, silenciosamente.
        prev = cur


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


def try_acquire_lock():
    """Trava de instância única, sem bloquear — `flock` é liberada
    automaticamente pelo kernel quando o processo termina (mesmo com
    kill -9), então não há risco de lock "presa" sobrevivendo a um
    processo morto, diferente de checar só a existência de um arquivo
    de PID. Duas instâncias rodando ao mesmo tempo já causaram dois
    incidentes reais aqui: um loop de render se auto-disparando por
    horas, e uma corrida entre dois `quarto render` concorrentes que
    chegou a gravar HTML direto na árvore-fonte (fora de _site/). Vale
    pros três modos (live, --once, --render-all): nunca é seguro dois
    desses rodando juntos.

    Retorna o file handle (mantenha a referência viva — fechar o fd
    libera a trava) se conseguiu, ou None se já tem outro processo
    rodando (o chamador decide o que fazer — nem sempre é um erro:
    --once e --render-all cooperam com um serviço --watch já de pé em
    vez de falhar, ver main_once()/main_render_all())."""
    lock_file = open(LOCK_PATH, "w")
    try:
        fcntl.flock(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        lock_file.close()
        return None
    lock_file.write(str(os.getpid()))
    lock_file.flush()
    return lock_file


def run_incremental_since_marker(exclude=frozenset()):
    """Usado por --once e pelo arranque do modo live: renderiza só o que
    mudou desde o último render bem-sucedido (marcador .last-render). Sem
    marcador (primeira vez), não há como saber o que mudou — faz um
    render completo e cria o marcador.

    `exclude` existe só pro caso do RENDER_ONCE_TRIGGER em
    plan_and_render(): a sentinela .render-once ainda está no disco nesse
    ponto (só é apagada depois que o render termina, pra manter o
    contrato de request_render_once_from_running_service() de esperar o
    render de verdade acabar) — sem excluí-la aqui, o snapshot() abaixo a
    veria como "mudada" e reentraria em plan_and_render() com ela de
    novo, infinitamente (RecursionError visto ao vivo antes deste
    parâmetro existir)."""
    if not os.path.exists(LAST_RENDER_MARKER):
        log("🚀 sem .last-render (primeira vez) — render completo inicial...")
        return render_full()
    marker_time = os.path.getmtime(LAST_RENDER_MARKER)
    cur = snapshot()
    changed = [p for p, mtime in cur.items() if mtime > marker_time and p not in exclude]
    if not changed:
        log("✅ nada mudou desde o último render — nada a fazer.")
        touch_marker()
        return True
    log(f"🚀 render incremental — {len(changed)} arquivo(s) mudado(s) desde o último render...")
    return plan_and_render(changed)


def request_from_running_service(trigger, description, timeout=1200):
    """Usado por --once e --render-all quando a trava já está com outro
    processo (o serviço --watch, presumivelmente): em vez de competir por
    um segundo `quarto render`, pede o render (incremental ou completo,
    conforme `trigger`) AO serviço já rodando, tocando a sentinela
    correspondente — o watch_loop dele detecta no próximo poll (até
    POLL_INTERVAL de atraso), interrompe a escuta pra atender o pedido, e
    volta a escutar sozinho depois (ver os blocos RENDER_ONCE_TRIGGER/
    RENDER_ALL_TRIGGER em plan_and_render()). Essa função só espera esse
    ciclo terminar, pra manter o mesmo contrato de antes pra quem chama
    (ex.: site-manager.sh): só retorna depois do render terminar, com
    sucesso/falha refletido no código de saída."""
    sentinel = os.path.join(ROOT, trigger)
    t0 = time.time()
    open(sentinel, "w").close()
    waited = 0.0
    while os.path.exists(sentinel):
        if waited >= timeout:
            log(f"❌ o serviço não processou o pedido em {timeout}s — algo travou; confira o log do serviço.")
            return False
        time.sleep(2)
        waited += 2
    ok = os.path.exists(LAST_RENDER_MARKER) and os.path.getmtime(LAST_RENDER_MARKER) >= t0
    log(f"✅ {description} concluído pelo serviço." if ok else f"❌ {description} falhou no serviço — confira o log dele.")
    return ok


def request_render_once_from_running_service(timeout=1200):
    return request_from_running_service(RENDER_ONCE_TRIGGER, "render incremental", timeout)


def request_render_all_from_running_service(timeout=1200):
    return request_from_running_service(RENDER_ALL_TRIGGER, "render completo", timeout)


def main_watch():
    lock = try_acquire_lock()
    if lock is None:
        log(
            f"ℹ️  já existe um serviço preview-watch.py rodando (lock em {LOCK_PATH}) "
            f"— acesse http://localhost:{PORT}, ele já está de pé. Não inicio um segundo."
        )
        sys.exit(0)
    # O servidor sobe ANTES do render inicial (não depois): _site/ já
    # existe de builds anteriores na maioria dos restarts (o script
    # cai/reinicia, o computador dorme, etc.), então não faz sentido
    # deixar a porta inacessível refazendo um render que agora, com o
    # render incremental, já costuma ser rápido mesmo — o site antigo já
    # serve enquanto o novo termina em paralelo.
    threading.Thread(target=serve, daemon=True).start()
    run_incremental_since_marker()
    try:
        watch_loop()
    except KeyboardInterrupt:
        log("👋 encerrando.")


def main_once():
    lock = try_acquire_lock()
    if lock is None:
        log("ℹ️  serviço --watch já rodando — pedindo a ele um render incremental (sem subir um segundo processo) e aguardando terminar...")
        sys.exit(0 if request_render_once_from_running_service() else 1)
    ok = run_incremental_since_marker()
    sys.exit(0 if ok else 1)


def main_render_all():
    lock = try_acquire_lock()
    if lock is None:
        log("ℹ️  serviço --watch já rodando — pedindo a ele um render completo (sem subir um segundo processo) e aguardando terminar...")
        sys.exit(0 if request_render_all_from_running_service() else 1)
    ok = render_full()
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    if "--once" in sys.argv:
        main_once()
    elif "--render-all" in sys.argv:
        main_render_all()
    else:
        main_watch()
