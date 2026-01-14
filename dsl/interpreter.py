from .commands.flow_commands import *
from .commands.commit_commands import *
from .commands.sync_commands import *
from .commands.info_commands import *
from .commands.github_commands import *

def execute(ast):
    if ast.command == "START_FEATURE":
        start_feature(ast.args[0])

    elif ast.command == "FINISH_FEATURE":
        finish_feature(ast.args[0])

    elif ast.command == "PUSH":
        push()

    elif ast.command == "PULL":
        pull()

    elif ast.command == "STATUS":
        status()

    elif ast.command == "STAGE_ALL":
        stage_all()

    elif ast.command == "COMMIT":
        commit(ast.args[0])

    elif ast.command == "LOG":
        log()
    
    elif ast.command == "INIT":
        init_repo()

    elif ast.command == "CREATE_GITHUB":
        create_github_repo(ast.args[0], ast.args[1])

    elif ast.command == "CONNECT_GITHUB":
        connect_github(ast.args[0])

    elif ast.command == "PUBLISH":
        publish()

    else:
        print("Unknown AST Command")
