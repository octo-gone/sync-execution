from scripts import xml_parser, run

file = "test.drawio"
n, w = xml_parser.parse(file)
run.create_structure(n, w)
