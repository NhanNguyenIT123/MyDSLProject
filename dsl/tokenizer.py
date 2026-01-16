class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

def tokenize(command):
    parts = command.strip().split()

    if not parts:
        return []

    tokens = []

    first = parts[0].lower()

    if first == "start":
        tokens.append(Token("START", "start"))
        tokens.append(Token("FEATURE", "feature"))
        tokens.append(Token("IDENT", parts[2]))

    elif first == "finish":
        tokens.append(Token("FINISH", "finish"))
        tokens.append(Token("FEATURE", "feature"))
        tokens.append(Token("IDENT", parts[2]))

    elif first == "push":
        tokens.append(Token("PUSH", "push"))

    elif first == "pull":
        tokens.append(Token("PULL", "pull"))

    elif first == "status":
        tokens.append(Token("STATUS", "status"))

    elif first == "stage":
        tokens.append(Token("STAGE", "stage"))

    elif first == "commit":
        tokens.append(Token("COMMIT", "commit"))
        for p in parts[1:]:
            tokens.append(Token("TEXT", p))

    elif first == "log":
        tokens.append(Token("LOG", "log"))

    elif first == "init":
        tokens.append(Token("INIT","init"))

    elif first == "create":
        tokens.append(Token("CREATE","create"))
        tokens.append(Token("TEXT", parts[1]))   # github
        tokens.append(Token("TEXT", parts[2].strip('"')))
        if len(parts) > 3:
            tokens.append(Token("TEXT", parts[3]))

    elif first == "connect":
        tokens.append(Token("CONNECT", "connect"))
        tokens.append(Token("TEXT", parts[1]))              # github
        tokens.append(Token("TEXT", parts[2].strip('"')))   # repo name

    elif first == "publish":
        tokens.append(Token("PUBLISH","publish"))

    elif first == "discard":
        tokens.append(Token("DISCARD", "discard"))
        if len(parts) > 1:
            tokens.append(Token("IDENT", parts[1]))
        else:
            tokens.append(Token("IDENT", "all"))

    elif first == "undo":
        tokens.append(Token("UNDO", "undo"))
        if len(parts) > 1 and parts[1].lower() == "commit":
            tokens.append(Token("COMMIT", "commit"))
        else:
            raise Exception("Expected: undo commit")
    
    elif first == "force":
        tokens.append(Token("FORCE", "force"))
        if len(parts) > 1 and parts[1].lower() == "reset":
            tokens.append(Token("RESET", "reset"))
            if len(parts) > 2:
                tokens.append(Token("IDENT", parts[2]))  # commit hash / HEAD~1
        else:
            raise Exception("Expected: force reset [commit]")

    else:
        raise Exception("Unknown command")

    return tokens
