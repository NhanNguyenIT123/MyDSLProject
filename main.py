from dsl.tokenizer import tokenize
from dsl.parser import parse
from dsl.interpreter import execute

print("Git DSL Ready!")
print("Type 'exit' to quit")

while True:
    command = input(">> ")

    if command.lower() == "exit":
        break

    tokens = tokenize(command)
    ast = parse(tokens)
    execute(ast)
