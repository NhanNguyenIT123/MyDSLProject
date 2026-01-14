from ..utils import run

def push():
    run("git push")
    print("[OK] pushed")

def pull():
    run("git pull")
    print("[OK] pulled")
