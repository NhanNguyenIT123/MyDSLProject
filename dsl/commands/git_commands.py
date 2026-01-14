import git

repo = git.Repo(r"C:\Users\HP\OneDrive\PPL\Project")


def start_feature(name):
    branch_name = f"feature/{name}"
    repo.git.checkout("-b", branch_name)
    print(f"[OK] Created and switched to {branch_name}")

def finish_feature(name):
    branch_name = f"feature/{name}"
    repo.git.checkout("develop")
    repo.git.merge(branch_name)
    print(f"[OK] Merged {branch_name} into develop")

def push():
    repo.git.push()
    print("[OK] Code pushed")

def pull():
    repo.git.pull()
    print("[OK] Pulled latest changes")
