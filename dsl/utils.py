import subprocess

def run(cmd, capture=False):
    if capture:
        result = subprocess.run(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip()
    else:
        subprocess.run(cmd, shell=True)
        return None
