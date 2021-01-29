from scripts import parser, run

modules = {
    "scripts.nodes.control",
    "scripts.nodes.inout",
    "scripts.nodes.memory",
    "scripts.nodes.construction",
    "scripts.nodes.logic",
    "scripts.nodes.misc",
    "scripts.nodes.mathematic",
    "scripts.nodes.struct",
    "external_modules.user_nodes"
}


file = "script.drawio"
run.run(*parser.parse(file), m=modules)
input("Press ENTER to exit...")
