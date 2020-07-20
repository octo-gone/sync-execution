from scripts.nodes import memory, misc, inout, construction, logic, control, mathematics
from scripts import nodes_info, base, utils


# node auto init
class NodeGen:
    def __new__(cls, data):
        node_name = data["node_name"]

        if node_name == "run":
            return control.NodeRun(data)
        if node_name == "stop":
            return control.NodeStop(data)
        if node_name == "wait":
            return control.NodeWait(data)
        if node_name == "delay":
            return control.NodeDelay(data)
        if node_name == "timer":
            return control.NodeTimer(data)
        if node_name == "ctrl":
            return control.NodeCtrl(data)
        if node_name == "merge":
            return control.NodeMerge(data)

        if node_name == "print ctrl":
            return inout.NodePrintCtrl(data)
        if node_name == "print":
            return inout.NodePrint(data)
        if node_name == "input":
            return inout.NodeInput(data)

        if node_name == "const ctrl":
            return memory.NodeConstCtrl(data)
        if node_name == "const int ctrl":
            return memory.NodeConstCtrl(data, int)
        if node_name == "const number ctrl":
            return memory.NodeConstCtrl(data, utils.number)
        if node_name == "const real ctrl":
            return memory.NodeConstCtrl(data, float)
        if node_name == "const char ctrl":
            return memory.NodeConstCtrl(data, utils.Char)
        if node_name == "const":
            return memory.NodeConst(data)
        if node_name == "const int":
            return memory.NodeConst(data, int)
        if node_name == "const number":
            return memory.NodeConst(data, utils.number)
        if node_name == "const real":
            return memory.NodeConst(data, float)
        if node_name == "const char":
            return memory.NodeConst(data, utils.Char)
        if node_name == "var":
            return memory.NodeVar(data)
        if node_name == "var int":
            return memory.NodeVar(data, int)
        if node_name == "var number":
            return memory.NodeVar(data, utils.number)
        if node_name == "var real":
            return memory.NodeVar(data, float)
        if node_name == "var char":
            return memory.NodeVar(data, utils.Char)
        if node_name == "array":
            return memory.NodeArray(data)

        if node_name == "abs":
            return mathematics.NodeAbs(data)
        if node_name == "add":
            return mathematics.NodeAdd(data)
        if node_name == "add int":
            return mathematics.NodeAdd(data, int)
        if node_name == "add number":
            return mathematics.NodeAdd(data, utils.number)
        if node_name == "add real":
            return mathematics.NodeAdd(data, float)
        if node_name == "dec":
            return mathematics.NodeDec(data)
        if node_name == "div":
            return mathematics.NodeDivide(data, "div")
        if node_name == "divide":
            return mathematics.NodeDivide(data, "divide")
        if node_name == "divide number":
            return mathematics.NodeDivide(data, "divide", coercion=True)
        if node_name == "exp":
            return mathematics.NodeExp(data)
        if node_name == "exp number":
            return mathematics.NodeExp(data, True)
        if node_name == "inc":
            return mathematics.NodeInc(data)
        if node_name == "int":
            return mathematics.NodeInt(data)
        if node_name == "inv":
            return mathematics.NodeInv(data)
        if node_name == "mod":
            return mathematics.NodeDivide(data, "mod")
        if node_name == "mult":
            return mathematics.NodeMult(data)
        if node_name == "mult int":
            return mathematics.NodeMult(data, int)
        if node_name == "mult number":
            return mathematics.NodeMult(data, utils.number)
        if node_name == "mult real":
            return mathematics.NodeMult(data, float)
        if node_name == "round":
            return mathematics.NodeRound(data)
        if node_name == "sub":
            return mathematics.NodeSub(data)
        if node_name == "sub int":
            return mathematics.NodeSub(data, int)
        if node_name == "sub number":
            return mathematics.NodeSub(data, utils.number)
        if node_name == "sub real":
            return mathematics.NodeSub(data, float)

        if node_name == "and":
            return logic.NodeComparisonA(data, "and")
        if node_name == "general and":
            return logic.NodeComparisonA(data, "and")
        if node_name == "equal":
            return logic.NodeComparisonA(data, "equal")
        if node_name == "general equal":
            return logic.NodeComparisonA(data, "equal")
        if node_name == "greater":
            return logic.NodeComparisonB(data, "greater")
        if node_name == "greater or equal":
            return logic.NodeComparisonB(data, "greater or equal")
        if node_name == "less":
            return logic.NodeComparisonB(data, "less")
        if node_name == "less or equal":
            return logic.NodeComparisonB(data, "less or equal")
        if node_name == "not":
            return logic.NodeNot(data)
        if node_name == "not equal":
            return logic.NodeComparisonB(data, "not equal")
        if node_name == "or":
            return logic.NodeComparisonA(data, "or")
        if node_name == "general or":
            return logic.NodeComparisonA(data, "or")
        if node_name == "xor":
            return logic.NodeComparisonB(data, "xor")

        if node_name == "value switch":
            return misc.NodeValueSwitch(data)

        if node_name == "if":
            return construction.NodeIf(data)

        return base.Node(data)


# the limit imposed on the number of connected wires
one_connection = ("int", "real", "obj", "char", "ctrl", "bool", "any", "number", "dir_mult_s", "dir_mult")
unlimited_connections = ("mult", "mult_s")

# separation by drawio connection count
one_connector = ("int", "real", "obj", "char", "ctrl", "bool", "any", "number", "mult_s", "dir_mult_s")
seven_connectors = ("mult", )
five_connectors = ("dir_mult", )


# main program
def create_structure(n, w, limit=10**5):
    utils.iteration = 0
    for node in n:
        NodeGen(node)

    for wire in w:
        base.Wire(wire)

    for node in base.Node.nodes.values():
        for i in range(len(node.inputs)):

            wires = base.Wire.get_wire_from_input(node, i)
            node.inputs[i] = wires

        offset = 0
        ins = []
        inputs_info = nodes_info.nodes_info[node.name]["inputs"]
        for i in inputs_info:
            if i in one_connector:
                ins.append(sum(node.inputs[offset:offset+1], []))
                offset += 1
            if i in seven_connectors:
                ins.append(sum(node.inputs[offset:offset+7], []))
                offset += 7
            if i in five_connectors:
                ins.append(sum(node.inputs[offset:offset+5], []))
                offset += 5
        for i, v in enumerate(ins):
            if inputs_info[i] in one_connection and len(v) > 1:
                raise utils.InputsCountError(f"expected zero or one connection not {len(v)}")

        node.inputs = ins

        for i in range(len(node.outputs)):
            node.outputs[i] = base.Wire.get_wire_from_output(node, i)

        offset = 0
        outs = []
        outputs_info = nodes_info.nodes_info[node.name]["outputs"]
        for i in outputs_info:
            if i in one_connector:
                outs.append(sum(node.outputs[offset:offset + 1], []))
                offset += 1
            if i in seven_connectors:
                outs.append(sum(node.outputs[offset:offset + 7], []))
                offset += 7
            if i in five_connectors:
                outs.append(sum(node.outputs[offset:offset + 5], []))
                offset += 5

        node.outputs = outs

    run = True
    if "run" not in list(map(lambda x: x.name, base.Node.nodes.values())):
        run = False
    while run:
        utils.iteration += 1
        try:
            for wire in base.Wire.wires:
                wire.update_give()
            for node in base.Node.nodes.values():
                node.update()
            for wire in base.Wire.wires:
                wire.update_take()
            for node in base.Node.nodes.values():
                node.post_update()
        except control.StopSync:
            # TODO: upgrade error catch
            run = False
        if utils.iteration >= limit:
            run = False
