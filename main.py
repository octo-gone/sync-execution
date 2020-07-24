from scripts import parser, run

file = "examples/test.drawio"
n, w, s = parser.parse(file)
run.run(n, w, s)
