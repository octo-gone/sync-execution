from abc import abstractmethod, ABC
from scripts.utils import nodes_v4 as nodes_info


# the limit imposed on the number of connected wires
one_connection = ("int", "real", "obj", "char", "ctrl", "bool", "any", "number", "dir_mult_s", "dir_mult")
unlimited_connections = ("mult", "mult_s")

# separation by drawio connection count
one_connector = ("int", "real", "obj", "char", "ctrl", "bool", "any", "number", "mult_s", "dir_mult_s")
seven_connectors = ("mult", )
five_connectors = ("dir_mult", )

ACTIVE = "active"
INACTIVE = "inactive"
WAITING = "waiting"


class Node:
    variables = {}
    nodes = {}

    def __init__(self, data):
        self.id = data["id"]
        self.nodes[self.id] = self
        self.raw_data = data

        self.name = data["node_name"]
        self.desc_value = data["value"]

        self.inputs = [[] for _ in range(len(data["inputs"]))]
        self.outputs = [[] for _ in range(len(data["outputs"]))]

        self.input_values = None
        self.output_values = None

        self.input_connectors = data["inputs"]
        self.output_connectors = data["outputs"]

        self.actual_inputs = None

        self.state = INACTIVE
        self.sub_state = None

        self.scope = 0
        self.pos = float(data["x"]), float(data["y"])
        self.size = float(data["width"]), float(data["height"])

    def get_actual_input(self, input_index):
        for key, value in self.actual_inputs.items():
            if input_index in value:
                return key

    def get_actual_state(self):
        sub_state = "_" + self.sub_state if self.sub_state is not None else ""
        return f"{self.state}{sub_state}"

    def __del__(self):
        if self.id in self.nodes:
            self.nodes.pop(self.id)

    def reset(self, *args, **kwargs):
        self.__class__.__init__(self, self.raw_data, *args, **kwargs)
        self.update_connections()

    def update_connections(self):
        for i in range(len(self.inputs)):
            wires = Wire.get_nodes_from_input(self, i)
            self.inputs[i] = wires

        offset = 0
        ins = []
        if str(self.name).startswith("function"):
            inputs_info = self.raw_data["inputs_names"]
            outputs_info = self.raw_data["outputs_names"]
        else:
            inputs_info = nodes_info.nodes_info[self.name]["inputs"]
            outputs_info = nodes_info.nodes_info[self.name]["outputs"]

        self.actual_inputs = {}
        for i, v in enumerate(inputs_info):
            if v in one_connector:
                ins.append(sum(self.inputs[offset:offset+1], []))
                self.actual_inputs[i] = tuple(range(offset, offset+1))
                offset += 1
            if v in seven_connectors:
                ins.append(sum(self.inputs[offset:offset+7], []))
                self.actual_inputs[i] = tuple(range(offset, offset+7))
                offset += 7
            if v in five_connectors:
                ins.append(sum(self.inputs[offset:offset+5], []))
                self.actual_inputs[i] = tuple(range(offset, offset+5))
                offset += 5
        for i, v in enumerate(ins):
            if inputs_info[i] in one_connection and len(v) > 1:
                raise ValueError("wrong connection count")

        self.inputs = ins

        for i in range(len(self.outputs)):
            self.outputs[i] = Wire.get_nodes_from_output(self, i)

        offset = 0
        outs = []
        self.output_values = []
        for i in outputs_info:
            if i in one_connector:
                outs.append(sum(self.outputs[offset:offset + 1], []))
                offset += 1
            if i in seven_connectors:
                outs.append(sum(self.outputs[offset:offset + 7], []))
                offset += 7
            if i in five_connectors:
                outs.append(sum(self.outputs[offset:offset + 5], []))
                offset += 5

        self.outputs = outs
        self.output_values = []
        for _ in self.outputs:
            self.output_values.append(None)

    def get_value(self, input_index, mult=False):
        if mult:
            values = []
            for input_node, output_index in self.inputs[input_index]:
                values.append(input_node.output_values[output_index])
            return values
        for input_node, output_index in self.inputs[input_index]:
            return input_node.output_values[output_index]

    def set_active(self, output_index):
        for output_node, input_index in self.outputs[output_index]:
            output_node.set_state(WAITING, input_index, obj=self, output_index=output_index)

    def set_state(self, state, input_index, **kwargs):
        self.state = state

    def update(self, state):
        if len({self.state, state, WAITING}) == 1:
            self.update_waiting()
        if len({self.state, state, ACTIVE}) == 1:
            self.update_active()
        if len({self.state, state, INACTIVE}) == 1:
            self.update_inactive()

    @abstractmethod
    def update_active(self):
        pass

    @abstractmethod
    def update_waiting(self):
        pass

    def update_inactive(self):
        pass


class Wire:
    wires = []

    def __init__(self, data):
        self.wires.append(self)
        self.raw_data = data

        if data["source"] in Node.nodes:
            self.source = Node.nodes[data["source"]]
        else:
            raise ValueError("no source node")

        if data["target"] in Node.nodes:
            self.target = Node.nodes[data["target"]]
        else:
            raise ValueError("no target node")

        self.exit = data["exitX"], data["exitY"]
        self.entry = data["entryX"], data["entryY"]

        if self.exit[0] == self.entry[0]:
            raise ValueError("wrong connection")
        if self.exit[0] == 0:
            self.exit, self.entry = self.entry, self.exit
            self.target, self.source = self.source, self.target

        self.entry_connector = self.target.input_connectors.index(self.entry[1])
        self.exit_connector = self.source.output_connectors.index(self.exit[1])

        self.active_ctrl = False
        self.value = None

    def __del__(self):
        if self in self.wires:
            self.wires.pop(self.wires.index(self))

    @classmethod
    def get_nodes_from_input(cls, node, input_num):
        nodes = []
        for wire in cls.wires:
            if wire.target == node and wire.entry_connector == input_num:
                nodes.append((wire.source, wire.exit_connector))
        return nodes

    @classmethod
    def get_nodes_from_output(cls, node, output_num):
        nodes = []
        for wire in cls.wires:
            if wire.source == node and wire.exit_connector == output_num:
                nodes.append((wire.target, wire.entry_connector))
        return nodes


class Scope:
    scopes = []

    def __init__(self, data):
        self.pos = float(data["x"]), float(data["y"])
        self.size = float(data["width"]), float(data["height"])
        self.id = data["id"]
        self.value = data["value"]
        self.scopes.append(self)
        self.scope = len(self.scopes)

    @classmethod
    def check_contains(cls, node):
        for scope in cls.scopes:
            if scope.check_bbox(node):
                break

    def check_bbox(self, node):
        if self.pos[0] < node.pos[0] and self.pos[1] < node.pos[1]:
            if (self.pos[0] + self.size[0]) > (node.pos[0] + node.size[0]) and \
               (self.pos[1] + self.size[1]) > (node.pos[1] + node.size[1]):
                node.scope = self.scope
                return True
        return False

#
# class NodeFunction(Node, ABC):
#     functions = {}
#     scope_id = 0
#
#     def __init__(self, data):
#         super().__init__(data)
#         if self.name.startswith("function input"):
#             if " ".join(self.name.split(" ")[2:]) not in self.functions:
#                 self.functions[" ".join(self.name.split(" ")[2:])] = {}
#             self.functions[" ".join(self.name.split(" ")[2:])]["in"] = self
#         elif self.name.startswith("function output"):
#             if " ".join(self.name.split(" ")[2:]) not in self.functions:
#                 self.functions[" ".join(self.name.split(" ")[2:])] = {}
#             self.functions[" ".join(self.name.split(" ")[2:])]["out"] = self
#         else:
#             if " ".join(self.name.split(" ")[1:]) not in self.functions:
#                 self.functions[" ".join(self.name.split(" ")[1:])] = {}
#             self.functions[" ".join(self.name.split(" ")[1:])]["func"] = self
#
#     @classmethod
#     def get_new_scope(cls):
#         cls.scope_id += 1
#         return f"f{cls.scope_id}"
#
#     @classmethod
#     def get_sur(cls, func):
#         _id = cls.get_new_scope()
#         # while len(nodes):
#         #     for n, i in sum(node.inputs, []) + sum(node.outputs, []):
#         #         if n not in used_nodes:
#         #             used_nodes.append(n)
#         #             nodes.append(n)
#         nodes = dict(cls.nodes.items())
#         for func_node in nodes.values():
#             if func_node.name == func["func"].name:
#                 # for output_node in func["in"].outputs:
#                 nodes = [func["in"], func["out"]]
#                 used_nodes = [func["in"], func["out"]]
#                 while nodes:
#                     node = nodes.pop(0)
#                     for n, i in sum(node.inputs, []) + sum(node.outputs, []):
#                         if n not in used_nodes:
#                             used_nodes.append(n)
#                             nodes.append(n)
#
#                 used_nodes.pop(0)
#                 used_nodes.pop(0)
#                 created_nodes = []
#                 for u_node in used_nodes:
#                     data = u_node.raw_data
#                     data["id"] = data["id"] + _id
#                     new_node = u_node.__class__(data)
#                     new_node.scope = _id
#                     created_nodes.append(new_node)
#
#                 for u_node in used_nodes:
#                     for wire in Wire.wires:
#                         if wire.target == u_node or wire.source == u_node:
#                             raw_data = dict(wire.raw_data.items())
#                             raw_data["id"] += _id
#                             if raw_data["target"] != func["out"].id:
#                                 raw_data["target"] = wire.raw_data["target"] + _id
#                             if raw_data["source"] != func["in"].id:
#                                 raw_data["source"] = wire.raw_data["source"] + _id
#                             else:
#                                 print(raw_data["entryY"], u_node)
#                                 for i, iv in enumerate(func_node.inputs):
#                                     for j, jv in enumerate(iv):
#                                         print(jv[0].id, raw_data["target"])
#                                         # print(i, jv, jv[0].outputs, jv[0].output_connectors[jv[1]])
#                                         # print(func["in"].outputs)
#                             Wire(raw_data)
#
#                 # for node in created_nodes:
#                 #     node.update_connections()
#                 #     print(name, node.inputs)
#                 #
#                 # for i, iv in enumerate(func_node.inputs):
#                 #     for j, jv in enumerate(iv):
#                 #         print(i, jv, jv[0].outputs, jv[0].output_connectors[jv[1]])
#                 #         # print(func["in"].outputs)
#
#                 # for i, v in enumerate(func["in"].outputs):
#                 #     print(func["in"].output_connectors[i])
#                 # print(func["in"].outputs)
#                 # print(node.inputs)
#                 # print(, sum(node.outputs, []))
#                 # for used in used_nodes:
#                 #     d = used.raw_data
#                 #     d["id"] += f"+_{cls.get_new_scope()}"
#                 # print(node.raw_data, node.inputs, node.outputs)
#
#     @classmethod
#     def init_function(cls):
#         for func in cls.functions.values():
#             cls.get_sur(func)
#             # if "func" not in func:
#             #     continue
#             # for node in cls.nodes.values():
#             #     if node.name == func["func"].name:
#             #         print(node.name)
