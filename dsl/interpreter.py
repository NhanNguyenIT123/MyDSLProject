from .commands.git_commands import *

def execute(ast):
    if ast.command == "START_FEATURE":
        start_feature(ast.args[0])

    elif ast.command == "FINISH_FEATURE":
        finish_feature(ast.args[0])

    elif ast.command == "PUSH":
        push()

    elif ast.command == "PULL":
        pull()

    else:
        print("Unknown AST Command")
