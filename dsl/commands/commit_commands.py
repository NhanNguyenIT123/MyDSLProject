from ..utils import run

def stage_all():
    run("git add .")
    print("[OK] staged all")

def commit(msg):
    r = run(f'git commit -m "{msg}"')
    print(r.stdout)

def undo_commit():
    run("git reset --soft HEAD~1")
    print("[OK] Last commit undone (soft reset)")
