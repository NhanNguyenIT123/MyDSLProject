from ..utils import run

def push():
    run("git push")
    print("[OK] pushed")

def pull():
    run("git pull")
    print("[OK] pulled")

def discard_all():
    run("git restore .")
    run("git clean -fd")
    print("[OK] Discarded all local changes (tracked + untracked)")

def discard_file(path):
    result = run(f"git status --porcelain {path}", capture=True)

    if not result:
        print(f"[INFO] {path} has no changes")
        return

    if result.startswith("??"):
        run(f"git clean -f {path}")
    else:
        run(f"git restore {path}")

    print(f"[OK] Discarded {path}")

def force_reset(commit="HEAD~1"):
    run(f"git reset --hard {commit}")
    run("git push --force")
    print("[OK] Force reset & pushed to remote")

