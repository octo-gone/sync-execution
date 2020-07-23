from scripts.utils import utils
from scripts.nodes import base, control, inout, memory, construction, logic, misc, mathematic
from scripts.utils import exceptions


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
        if node_name == "merge":
            return control.NodeMerge(data)
        if node_name == "ctrl":
            return control.NodeCtrl(data)
        if node_name == "delay":
            return control.NodeDelay(data)
        if node_name == "timer":
            return control.NodeTimer(data)

        if node_name == "print ctrl":
            return inout.NodePrintCtrl(data)
        if node_name == "print":
            return inout.NodePrint(data)
        if node_name == "input":
            return inout.NodeInput(data)

        if node_name == "const":
            return memory.NodeConst(data)
        if node_name == "const ctrl":
            return memory.NodeConstCtrl(data)

        if node_name == "var":
            return memory.NodeVar(data)
        if node_name == "var set":
            return memory.NodeVarSet(data)
        if node_name == "var get":
            return memory.NodeVarGet(data)

        if node_name == "for":
            return construction.NodeFor(data, utils.Number)
        if node_name == "for ext":
            return construction.NodeForExt(data, utils.Number)
        if node_name == "if":
            return construction.NodeIf(data)
        if node_name == "while":
            return construction.NodeWhile(data)

        if node_name in ("and", "or", "equal"):
            return logic.NodeLogicA(data)
        if node_name in ("greater", "greater or equal", "less", "less or equal", "not equal", "xor"):
            return logic.NodeLogicB(data)

        if node_name == "value switch":
            return misc.NodeValueSwitch(data)

        if node_name == "abs":
            return mathematic.NodeAbs(data)
        if node_name == "add":
            return mathematic.NodeAdd(data)
        if node_name == "dec":
            return mathematic.NodeDec(data)
        if node_name == "division":
            return mathematic.NodeDivision(data)
        if node_name == "exp":
            return mathematic.NodeExp(data)
        if node_name == "inc":
            return mathematic.NodeInc(data)
        if node_name == "trunc":
            return mathematic.NodeTrunc(data)
        if node_name == "inv":
            return mathematic.NodeInv(data)
        if node_name == "mult":
            return mathematic.NodeMult(data)
        if node_name == "round":
            return mathematic.NodeRound(data)
        if node_name == "sub":
            return mathematic.NodeSub(data)

        return base.Node(data)


# main program
def create_structure(n, w):
    utils.iteration = 0
    for node in n:
        NodeGen(node)

    for wire in w:
        base.Wire(wire)

    for node in base.Node.nodes.values():
        node.update_connections()

    # for node in base.Node.nodes.values():
    #     print(node.id, node.name, node.inputs, node.outputs)


def run(n, w, limit=10**5):
    create_structure(n, w)
    print("- program -")
    for utils.iteration in range(limit):
        try:
            for node in base.Node.nodes.values():
                node.update(base.INACTIVE)
            # print("--")
            for node in base.Node.nodes.values():
                # if node.state == base.WAITING:
                #     print(node.name, node.id, node.get_actual_state())
                node.update(base.WAITING)
            # print("--")
            for node in base.Node.nodes.values():
                node.update(base.ACTIVE)
            # for node in base.Node.nodes.values():
            #     print(node.id, node.name, node.get_actual_state())
            # print("--")
        except exceptions.StopSync:
            print("- stop -")
            break
    print("- end -")
    print("variables:", base.Node.variables)
