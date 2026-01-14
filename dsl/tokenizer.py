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


    else:
        raise Exception("Unknown command")

    return tokens
