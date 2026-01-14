from ..utils import run

def stage_all():
    run("git add .")
    print("[OK] staged all")

def commit(msg):
    r = run(f'git commit -m "{msg}"')
    print(r.stdout)
