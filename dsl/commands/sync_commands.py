from ..utils import run
from ..validator import is_clean

def push():
    run("git push")
    print("[OK] pushed")

def pull():
    run("git pull")
    print("[OK] pulled")

def discard_all():
    if is_clean():
        print("[INFO] Nothing to discard")
        return

    run("git restore .")
    run("git clean -fd")
    print("[OK] Discarded all local changes (tracked + untracked)")

def discard_file(path):
    status = run("git status --porcelain", capture=True)

    if not status:
        print("[INFO] Working tree clean")
        return

    lines = status.splitlines()
    matched = [l for l in lines if l.endswith(path)]

    if not matched:
        print(f"[INFO] {path} has no changes")
        return

    entry = matched[0]

    if entry.startswith("??"):
        run(f"git clean -f {path}")
        print(f"[OK] Deleted untracked file {path}")
    else:
        run(f"git restore {path}")
        print(f"[OK] Discarded changes in {path}")

def force_reset(commit="HEAD~1"):
    run(f"git reset --hard {commit}")
    run("git push --force")
    print("[OK] Force reset & pushed to remote")

