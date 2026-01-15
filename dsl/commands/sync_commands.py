from ..utils import run

def push():
    run("git push")
    print("[OK] pushed")

def pull():
    run("git pull")
    print("[OK] pulled")

def discard_all():
    run("git restore .")
    print("[OK] Discarded all local changes")

def discard_file(path):
    run(f"git restore {path}")
    print(f"[OK] Discarded changes in {path}")

def force_reset(commit="HEAD~1"):
    run(f"git reset --hard {commit}")
    run("git push --force")
    print("[OK] Force reset & pushed to remote")

