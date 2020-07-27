

class NodeFunction(Node, ABC):
    functions = {}
    scope_id = 0

    def __init__(self, data):
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
            self.functions[" ".join(self.name.split(" ")[1:])]["func"] = self

    @classmethod
    def get_new_scope(cls):
        cls.scope_id += 1
        return f"f{cls.scope_id}"

    @classmethod
    def get_sur(cls, func):
        nodes = dict(cls.nodes.items())
        for func_node in nodes.values():
            if func_node.name == func["func"].name:
                _id = cls.get_new_scope()
                nodes = [func["in"], func["out"]]
                used_nodes = [func["in"], func["out"]]
                while nodes:
                    node = nodes.pop(0)
                    for n, i in sum(node.inputs, []) + sum(node.outputs, []):
                        if n not in used_nodes:
                            used_nodes.append(n)
                            nodes.append(n)

                print(used_nodes)
                print("--")

                used_nodes.pop(0)
                used_nodes.pop(0)
                created_nodes = []
                for u_node in used_nodes:
                    data = deepcopy(u_node.raw_data)
                    data["id"] = data["id"] + _id
                    new_node = u_node.__class__(data)
                    new_node.scope = _id
                    created_nodes.append(new_node)

                connected_nodes = set()
                for u_node in used_nodes:
                    for wire in Wire.wires:
                        if wire.target == u_node or wire.source == u_node:
                            raw_data = deepcopy(wire.raw_data)
                            raw_data["id"] += _id
                            if raw_data["target"] != func["out"].id:
                                raw_data["target"] = wire.raw_data["target"] + _id
                                if raw_data["source"] != func["in"].id:
                                    raw_data["source"] = wire.raw_data["source"] + _id
                                else:
                                    continue
                            else:
                                continue
                            if (raw_data["source"], raw_data["target"]) in connected_nodes or \
                               (raw_data["target"], raw_data["source"]) in connected_nodes:
                                continue
                            connected_nodes.add((raw_data["source"], raw_data["target"]))
                            Wire(raw_data)

                for node in cls.nodes.values():
                    node.update_connections()

                for i, _input in enumerate(func_node.inputs):
                    for input_node, outputs_index in _input:
                        for output_node, input_index in copy(input_node.outputs[outputs_index]):
                            if i == input_index:
                                j = input_node.outputs[outputs_index].index((output_node, input_index))
                                input_node.outputs[outputs_index].pop(j)
                                for outs, io in func["in"].outputs[input_index]:
                                    input_node.outputs[outputs_index].append((cls.nodes[outs.id + _id], io))
                # del func_node
                # for i, _output in enumerate(func_node.outputs):
                #     for output_node, input_index in _output:
                #         for input_node, output_index in copy(output_node.inputs[input_index]):
                #             if i == output_index:
                #                 j = output_node.outputs[input_index].index((input_node, output_index))
                #                 output_node.outputs[input_index].pop(j)
                #                 for ins, ii in func["out"].inputs[output_index]:
                #                     output_node.outputs[input_index].append((cls.nodes[ins.id + _id], ii))

                # exit()
                # for node in created_nodes:
                #     node.update_connections()
                #     print(name, node.inputs)
                #
                # for i, iv in enumerate(func_node.inputs):
                #     for j, jv in enumerate(iv):
                #         print(i, jv, jv[0].outputs, jv[0].output_connectors[jv[1]])
                #         # print(func["in"].outputs)

                # for i, v in enumerate(func["in"].outputs):
                #     print(func["in"].output_connectors[i])
                # print(func["in"].outputs)
                # print(node.inputs)
                # print(, sum(node.outputs, []))
                # for used in used_nodes:
                #     d = used.raw_data
                #     d["id"] += f"+_{cls.get_new_scope()}"
                # print(node.raw_data, node.inputs, node.outputs)

    @classmethod
    def init_function(cls):
        for func in cls.functions.values():
            cls.get_sur(func)
            # if "func" not in func:
            #     continue
            # for node in cls.nodes.values():
            #     if node.name == func["func"].name:
            #         print(node.name)
