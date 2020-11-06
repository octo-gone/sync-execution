from copy import deepcopy, copy
from scripts.nodes import base
from scripts.utils import logger
import abc


class NodeFunction(base.Node, abc.ABC):
    """
    Class for function creation constructions. It has several class variables:
        functions - list of all functions (input, output and last processed function node);
        scope_id - special for function nodes scope (updates after initialization of new function node).
    """
    functions = {}
    scope_id = 0

    def __init__(self, data):
        """
        Class constructor. Saves node to list of all functions with
        information about type of function node (input, output or node itself).

        :param dict data: node information
        """
        super().__init__(data)
        if self.name.startswith("function input"):
            if " ".join(self.name.split(" ")[2:]) not in self.functions:
                self.functions[" ".join(self.name.split(" ")[2:])] = {}
            self.functions[" ".join(self.name.split(" ")[2:])]["in"] = self
        elif self.name.startswith("function output"):
            if " ".join(self.name.split(" ")[2:]) not in self.functions:
                self.functions[" ".join(self.name.split(" ")[2:])] = {}
            self.functions[" ".join(self.name.split(" ")[2:])]["out"] = self
        else:
            if " ".join(self.name.split(" ")[1:]) not in self.functions:
                self.functions[" ".join(self.name.split(" ")[1:])] = {}
            self.functions[" ".join(self.name.split(" ")[1:])]["func"] = self.name

    @classmethod
    def get_new_scope(cls):
        """Generates new scope."""
        cls.scope_id += 1
        return f"f{cls.scope_id}"

    @classmethod
    def change_sur(cls, func):
        """
        Main function that creates all nodes that would be used in function node.

        General explanation:
            Function takes function node (not input or output creation node).
            Function creates clones of all nodes that connected to input
            or output function creation nodes (further 'IOF'). In Sync IOF marked as 'in' and 'out'.
            After creation function updates inputs and outputs of nodes that connected to IOF. New input
            and output nodes function takes from nodes that connected to function node.

        1. Function creates new scope for nodes in function;
        2. Function searches for nodes that connected to IOF;
        3. Since there is no need to take IOF into account function deletes them;
        4. For each chosen node function creates copy of node by using deepcopy of some data
            4.1 Function updates id with using scope;
            4.2 Function uses class initializer with new data;
            4.3 Function copy inputs and outputs (not deepcopy, because you only need to copy wrap of objects);
            4.4 Function changes scope of node and add node to list of new nodes.
        5. For each new node that not connected to IOF function changes connected nodes
            by taking new node from their id with scope addition.
            It is possible cause function copied ids before with only adding scope.
            Function also copies input or output index of node;
        6. Fore each new node that connected to IOF function changes connected nodes
            by copying all nodes which relate to function node to connection. That means that
            function will copy all connections from function node to any connection that goes from or into IOF;
        7. Since updating inputs and outputs is not enough function updates outputs for input nodes of function node
            and inputs for output nodes. This is required because each node describes both input and output,
            so describing this for nodes inside function will not be enough. It is need to change inputs and outputs
            for nodes that connected to function node. From this goes naming of method - function changes surrounding.

        :param dict func: list of input, output (and last processed node) of function
        """
        nodes = dict(cls.nodes.items())
        for func_node in nodes.values():
            if func_node.name == func["func"]:
                # 1
                _id = cls.get_new_scope()
                # 2
                _nodes = [func["in"], func["out"]]
                used_nodes = [func["in"], func["out"]]
                while _nodes:
                    node = _nodes.pop(0)
                    if node == func["in"]:
                        sample = sum(node.outputs, [])
                    elif node == func["out"]:
                        sample = sum(node.inputs, [])
                    else:
                        sample = sum(node.inputs, []) + sum(node.outputs, [])
                    for n, i in sample:
                        if n not in used_nodes:
                            used_nodes.append(n)
                            _nodes.append(n)
                # 3
                used_nodes.pop(0)
                used_nodes.pop(0)
                # 4
                new_nodes = []
                for node in used_nodes:
                    d = deepcopy(node.raw_data)
                    d["id"] += _id
                    new_node = node.__class__(d)
                    new_node.outputs = copy(node.outputs)
                    new_node.inputs = copy(node.inputs)
                    new_node.output_values = copy(node.output_values)
                    new_node.actual_inputs = copy(node.actual_inputs)
                    new_node.scope = _id
                    if new_node.desc_value == '$desc':
                        new_node.desc_value = func_node.desc_value
                    new_nodes.append(new_node)
                # 5
                for new_node in new_nodes:
                    for iic, input_connector in enumerate(new_node.inputs):
                        for ii, ins in enumerate(input_connector):
                            if ins[0] != func["in"]:
                                new_node.inputs[iic][ii] = base.Node.nodes[ins[0].id + _id], ins[1]
                    for ioc, output_connector in enumerate(new_node.outputs):
                        for io, outs in enumerate(output_connector):
                            if outs[0] != func["out"]:
                                new_node.outputs[ioc][io] = base.Node.nodes[outs[0].id + _id], outs[1]
                # 6
                for new_node in new_nodes:
                    for iic, input_connector in enumerate(new_node.inputs):
                        for ii, ins in enumerate(input_connector):
                            if ins[0] == func["in"]:
                                new_node.inputs[iic][ii:ii+1] = func_node.inputs[func_node.get_actual_input(ins[1])]
                    for ioc, output_connector in enumerate(new_node.outputs):
                        for io, outs in enumerate(output_connector):
                            if outs[0] == func["out"]:
                                new_node.outputs[ioc][io:io+1] = func_node.outputs[outs[1]]
                # 7
                for iic, input_connectors in enumerate(func_node.inputs):
                    for iin, input_node in enumerate(input_connectors):
                        for ioc, output_connector in enumerate(input_node[0].outputs):
                            for io, outs in enumerate(output_connector):
                                if outs[0] == func_node:
                                    out = []
                                    for tmp_out in func["in"].outputs[func["in"].get_actual_output(outs[1])]:
                                        out.append((base.Node.nodes[tmp_out[0].id + _id], tmp_out[1]))
                                    input_node[0].outputs[ioc][io:io + 1] = out

                for ioc, output_connector in enumerate(func_node.outputs):
                    for ion, output_node in enumerate(output_connector):
                        for iic, input_connector in enumerate(output_node[0].inputs):
                            for ii, ins in enumerate(input_connector):
                                if ins[0] == func_node:
                                    _in = []
                                    for tmp_out in func["out"].inputs[ins[1]]:
                                        _in.append((base.Node.nodes[tmp_out[0].id + _id], tmp_out[1]))
                                    output_node[0].inputs[iic][ii:ii + 1] = _in

    @classmethod
    def init_function(cls):
        """Function runs updating surrounding for each function (not function node)"""
        for func in cls.functions.values():
            cls.change_sur(func)
