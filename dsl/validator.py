from .utils import run

def is_clean():
    r = run("git status --porcelain")
    return r.stdout.strip() == ""

def ensure_clean():
    if not is_clean():
        print("[ERROR] Working tree dirty! Commit first.")
        return False
    return True
