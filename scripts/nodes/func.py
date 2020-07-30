from copy import deepcopy, copy
from scripts.nodes import base
import abc


class NodeFunction(base.Node, abc.ABC):
    functions = {}
    scope_id = 0

    def __init__(self, data):
        super().__init__(data)
        print(self.name)
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
        cls.scope_id += 1
        return f"f{cls.scope_id}"

    @classmethod
    def get_sur(cls, func):
        nodes = dict(cls.nodes.items())
        for func_node in nodes.values():
            if func_node.name == func["func"]:
                _id = cls.get_new_scope()
                nodes = [func["in"], func["out"]]
                used_nodes = [func["in"], func["out"]]
                while nodes:
                    node = nodes.pop(0)
                    for n, i in sum(node.inputs, []) + sum(node.outputs, []):
                        if n not in used_nodes:
                            used_nodes.append(n)
                            nodes.append(n)

                used_nodes.pop(0)
                used_nodes.pop(0)

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
                    new_nodes.append(new_node)

                for new_node in new_nodes:
                    for iic, input_connector in enumerate(new_node.inputs):
                        for ii, ins in enumerate(input_connector):
                            if ins[0] != func["in"]:
                                new_node.inputs[iic][ii] = base.Node.nodes[ins[0].id + _id], ins[1]

                    for ioc, output_connector in enumerate(new_node.outputs):
                        for io, outs in enumerate(output_connector):
                            if outs[0] != func["out"]:
                                new_node.outputs[ioc][io] = base.Node.nodes[outs[0].id + _id], outs[1]

                for new_node in new_nodes:
                    for iic, input_connector in enumerate(new_node.inputs):
                        for ii, ins in enumerate(input_connector):
                            if ins[0] == func["in"]:
                                new_node.inputs[iic][ii:ii+1] = func_node.inputs[ins[1]]

                    for ioc, output_connector in enumerate(new_node.outputs):
                        for io, outs in enumerate(output_connector):
                            if outs[0] == func["out"]:
                                new_node.outputs[ioc][io:io+1] = func_node.outputs[outs[1]]

                for iic, input_connectors in enumerate(func_node.inputs):
                    for iin, input_node in enumerate(input_connectors):

                        for ioc, output_connector in enumerate(input_node[0].outputs):
                            for io, outs in enumerate(output_connector):
                                if outs[0] == func_node:
                                    out = []
                                    for tmp_out in func["in"].outputs[outs[1]]:
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
        for func in cls.functions.values():
            cls.get_sur(func)
