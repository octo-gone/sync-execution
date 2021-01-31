from scripts.utils import utils, exceptions, logger
from scripts.nodes import base, func
from scripts import loader
import random


class NodeGen:
    """
    Interim class that automatically sets node class from data
    """
    nodes = None

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

        if node_name in loader.node_aliases:
            return loader.node_aliases[node_name](data)

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
    if "run" not in map(lambda x: x.name, base.Node.nodes.values()) and \
            "unit test" not in map(lambda x: x.name, base.Node.nodes.values()):
        logger.log_error("no 'start' node")
    logger.log_success("program started")
    for utils.iteration in range(limit):
        try:
            nodes = list(base.Node.nodes.values())
            random.shuffle(nodes)
            for node in nodes:
                node.update(base.INACTIVE)
            for node in nodes:
                node.update(base.WAITING)
            for node in nodes:
                node.update(base.ACTIVE)
        except exceptions.StopSync:
            logger.log_success("program stopped via node 'stop'")
            utils.iteration = -1
            break
    if utils.iteration != -1:
        active_nodes = []
        for node in base.Node.nodes.values():
            if node.state == base.WAITING:
                active_nodes.append(node)
        logger.log_error(f"iteration overstepped the limit\n{active_nodes}")
    if base.Node.ut_send:
        logger.log_error("value input expected")
    elif base.Node.ut_catch:
        logger.log_error(f"expected value '{base.Node.ut_catch}'")
