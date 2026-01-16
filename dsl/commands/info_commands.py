from ..utils import run

def status():
    output = run("git status", capture=True)
    print(output)

def log():
    output = run("git --no-pager log --oneline -10", capture=True)
    print(output)
