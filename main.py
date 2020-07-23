from scripts import parser, run

file = "examples/test.drawio"
n, w = parser.parse(file)
run.run(n, w)
