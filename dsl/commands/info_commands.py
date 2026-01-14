from ..utils import run

def status():
    r = run("git status")
    print(r.stdout)

def log():
    r = run("git --no-pager log --oneline -10")
    print(r.stdout)
