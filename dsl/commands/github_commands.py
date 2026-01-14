import requests
from dotenv import load_dotenv
import os
from ..utils import run

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = os.getenv("GITHUB_USERNAME")

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def init_repo():
    run("git init")
    run("git branch -M main")
    print("[OK] Local git initialized")

def create_github_repo(name, visibility="public"):
    data = {
        "name": name,
        "private": (visibility == "private")
    }

    r = requests.post(
        "https://api.github.com/user/repos",
        json=data,
        headers=headers
    )

    if r.status_code == 201:
        print(f"[OK] GitHub repo created: {name}")
    elif r.status_code == 422:
        print("[WARN] Repo already exists on GitHub")
    else:
        print("[ERROR] Failed:", r.json())

def connect_github(name):
    url = f"https://github.com/{USERNAME}/{name}.git"
    run(f"git remote add origin {url}")
    print(f"[OK] Connected remote: {url}")

def publish():
    run("git add .")
    run('git commit -m "Initial commit"')
    run("git push -u origin main")
    print("[OK] Project published to GitHub")
