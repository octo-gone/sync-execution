from scripts import parser, run


file = "script.drawio"
run.run(*parser.parse(file))
input("Press ENTER to exit...")
