from scripts import parser, run


file = "examples/test.drawio"
run.run(*parser.parse(file))
input("Press ENTER to exit.")
