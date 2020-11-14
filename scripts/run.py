from scripts.utils import utils, exceptions, logger
from scripts.nodes import base, control, inout, memory, construction, logic, misc, mathematic, func, struct
from scripts.nodes import user_nodes
import sys
import inspect


class NodeGen:
    """
    Interim class that automatically sets node class from data
    """
    user_classes = inspect.getmembers(sys.modules[user_nodes.__name__], inspect.isclass)

    def __new__(cls, data):
        """
        Function runs before the constructor and selects suitable class.
        If node is function (function input or output) method
        will run special nodes class constructor.

        :param dict data: node information
        """
        node_name = data["node_name"]
        if str(node_name).startswith("function"):
            return func.NodeFunction(data)

        for class_name, class_constr in cls.user_classes:
            if node_name == class_constr.name:
                return class_constr(data)

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
        if node_name == "error":
            return control.NodeError(data)

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

        if node_name == "array create":
            return struct.NodeArrayCreate(data)
        if node_name == "array get":
            return struct.NodeArrayGet(data)
        if node_name == "array set":
            return struct.NodeArraySet(data)
        if node_name == "array get and set":
            return struct.NodeArrayGetSet(data)
        if node_name == "list create":
            return struct.NodeListCreate(data)
        if node_name == "list get":
            return struct.NodeListGet(data)
        if node_name == "list set":
            return struct.NodeListSet(data)
        if node_name == "list get and set":
            return struct.NodeListGetSet(data)
        if node_name == "list remove":
            return struct.NodeListRemove(data)
        if node_name == "length":
            return struct.NodeLen(data)
        if node_name == "matrix create":
            return struct.NodeMatrixCreate(data)
        if node_name == "matrix get":
            return struct.NodeMatrixGet(data)
        if node_name == "matrix set":
            return struct.NodeMatrixSet(data)
        if node_name == "matrix get and set":
            return struct.NodeMatrixGetSet(data)
        if node_name == "dict create":
            return struct.NodeDictCreate(data)
        if node_name == "dict insert":
            return struct.NodeDictInsert(data)
        if node_name == "dict find":
            return struct.NodeDictFind(data)
        if node_name == "dict insert and find":
            return struct.NodeDictInsertFind(data)
        if node_name == "dict remove":
            return struct.NodeDictRemove(data)

        if node_name == "for":
            return construction.NodeFor(data)
        if node_name == "for ext":
            return construction.NodeForExt(data)
        if node_name == "if":
            return construction.NodeIf(data)
        if node_name == "while":
            return construction.NodeWhile(data)
        if node_name == "counter":
            return construction.NodeCounter(data)
        if node_name == "foreach":
            return construction.NodeForeach(data)
        if node_name == "split string":
            return construction.NodeSplitString(data)

        if node_name in ("and", "or", "not and", "not or", "equal"):
            return logic.NodeLogicA(data)
        if node_name in ("greater", "greater or equal", "less", "less or equal", "not equal", "xor"):
            return logic.NodeLogicB(data)
        if node_name == "in":
            return logic.NodeIn(data)
        if node_name == "bool":
            return logic.NodeBool(data)

        if node_name == "value switch":
            return misc.NodeValueSwitch(data)
        if node_name == "get type":
            return misc.NodeGetType(data)
        if node_name == "type":
            return misc.NodeType(data)
        if node_name == "random":
            return misc.NodeRandom(data)
        if node_name == "random int":
            return misc.NodeRandomInt(data)
        if node_name == "random num":
            return misc.NodeRandomNum(data)
        if node_name == "random seed":
            return misc.NodeRandomSeed(data)

        if node_name == "join":
            return misc.NodeJoin(data)
        if node_name == "concatenate":
            return misc.NodeConcatenate(data)
        if node_name == "format":
            return misc.NodeFormat(data)

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
        if node_name == "div":
            return mathematic.NodeDiv(data)
        if node_name == "mod":
            return mathematic.NodeMod(data)

        logger.log_warning(f"no function node found with name '{node_name}'")
        return base.Node(data)


def create_structure(n, w, s):
    """
    Function creates instances of nodes, wires, functions and scopes.

    :param n: list of nodes information
    :param w: list of wires information
    :param s: list of scope information
    """
    utils.iteration = 0

    for scope in s:
        base.Scope(scope)

    for node in n:
        NodeGen(node)

    for wire in w:
        base.Wire(wire)

    for node in base.Node.nodes.values():
        node.update_connections()
        base.Scope.check_contains(node)

    func.NodeFunction.init_function()


def run(n, w, s, limit=10 ** 5):
    """
    Function iteratively launches nodes update functions for
    different states: INACTIVE, WAITING and ACTIVE. If node stop
    or similar generates exception StopSync, then function stops
    iteration, otherwise if the iteration exceeds the limit
    function stops updating.

    :param n: list of nodes information
    :param w: list of wires information
    :param s: list of scope information
    :param limit: limit number of updates
    """
    create_structure(n, w, s)
    if "run" not in map(lambda x: x.name, base.Node.nodes.values()):
        logger.log_error("no 'start' node")
    logger.log_success("program started")
    for utils.iteration in range(limit):
        try:
            for node in base.Node.nodes.values():
                node.update(base.INACTIVE)
            for node in base.Node.nodes.values():
                node.update(base.WAITING)
            for node in base.Node.nodes.values():
                node.update(base.ACTIVE)
        except exceptions.StopSync:
            logger.log_success("program stopped via node 'stop'")
            utils.iteration = -1
            break
    if utils.iteration != -1:
        logger.log_error("iteration overstepped the limit")
