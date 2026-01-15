class ASTNode:
    def __init__(self, command, args=None):
        self.command = command
        self.args = args or []

def parse(tokens):
    if not tokens:
        return None

    first = tokens[0].type

    # start feature X
    if first == "START":
        return ASTNode("START_FEATURE", [tokens[2].value])

    # finish feature X
    if first == "FINISH":
        return ASTNode("FINISH_FEATURE", [tokens[2].value])

    # push
    if first == "PUSH":
        return ASTNode("PUSH")

    # pull
    if first == "PULL":
        return ASTNode("PULL")
    
    # status
    if first == "STATUS":
        return ASTNode("STATUS")

    # stage all
    if first == "STAGE":
        return ASTNode("STAGE_ALL")

    # commit "message"
    if first == "COMMIT":
        # everything after commit is the message
        msg = " ".join([t.value for t in tokens[1:]]).strip('"')
        return ASTNode("COMMIT", [msg])

    # log
    if first == "LOG":
        return ASTNode("LOG")

    if first == "INIT":
        return ASTNode("INIT")

    if first == "CREATE":
        name = tokens[2].value
        visibility = tokens[3].value if len(tokens) > 3 else "public"
        return ASTNode("CREATE_GITHUB", [name, visibility])

    if first == "CONNECT":
        print(tokens)
        return ASTNode("CONNECT_GITHUB", [tokens[2].value])

    if first == "PUBLISH":
        return ASTNode("PUBLISH")
    
    if first == "DISCARD":
        return ASTNode("DISCARD", [tokens[1].value])
    
    if first == "UNDO" and tokens[1].type == "COMMIT":
        return ASTNode("UNDO_COMMIT")

    if first == "FORCE" and tokens[1].type == "RESET":
        if len(tokens) > 2:
            return ASTNode("FORCE_RESET", [tokens[2].value])
        return ASTNode("FORCE_RESET")


    raise Exception("Unknown command")
