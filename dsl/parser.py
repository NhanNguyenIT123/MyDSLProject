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

    raise Exception("Unknown command")
