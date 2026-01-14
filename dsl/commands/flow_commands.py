from ..utils import run
from ..validator import ensure_clean

def start_feature(name):
    run(f"git checkout -b feature/{name}")
    print(f"[OK] Created and switched to feature/{name}")

def finish_feature(name):
    if not ensure_clean():
        return
    
    run("git checkout main")
    run(f"git merge feature/{name}")
    print(f"[OK] merged feature/{name} into main")
