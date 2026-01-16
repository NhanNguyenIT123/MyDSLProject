from .utils import run

def is_clean():
    status = run("git status --porcelain", capture=True)
    return status == ""

def ensure_clean():
    if not is_clean():
        print("[ERROR] Working tree dirty! Commit first.")
        return False
    return True
