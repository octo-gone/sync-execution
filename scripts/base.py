from abc import abstractmethod


class WireConnectionError(Exception):
    pass


class NodeInputError(Exception):
    pass


class Node:
    variables = {}
    nodes = {}

    def __init__(self, data):
        self.id = data["id"]
        self.nodes[self.id] = self

        self.name = data["node_name"]
        self.desc_value = data["value"]

        self.inputs = [[] for _ in range(len(data["inputs"]))]
        self.outputs = [[] for _ in range(len(data["outputs"]))]

        self.input_values = None
        self.output_values = None

        self.input_connectors = data["inputs"]
        self.output_connectors = data["outputs"]

        self.value = None
        self.active = False
        self.deactivation = False

        self.callable = False

    def __del__(self):
        if self.id in self.nodes:
            self.nodes.pop(self.id)

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def reset(self):
        pass

    def post_update(self):
        if self.deactivation:
            self.reset()
            self.active = False

    def activate(self, wire):
        self.active = True
        return False

    def deactivate(self, wire):
        self.deactivation = True
        return True

    # call value back

    @staticmethod
    def call_back(wire):
        if wire.source.callable:
            wire.active_ctrl = True
            wire.value = wire.source.take_value()

    def take_value(self):
        if self.callable:
            self.prepare_value()
        if self.callable and self.value is not None:
            return self.value
        return None

    def prepare_value(self):
        pass

    def call_all(self, active=False):
        if self.active or active:
            for wire in sum(self.inputs, []):
                self.call_back(wire)


class Wire:
    wires = []

    def __init__(self, data):
        self.wires.append(self)

        if data["source"] in Node.nodes:
            self.source = Node.nodes[data["source"]]
        else:
            raise WireConnectionError("no source node")

        if data["target"] in Node.nodes:
            self.target = Node.nodes[data["target"]]
        else:
            raise WireConnectionError("no target node")

        self.exit = data["exitX"], data["exitY"]
        self.entry = data["entryX"], data["entryY"]

        if self.exit[0] == self.entry[0]:
            raise WireConnectionError("wrong connection")
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

    def update_take(self):
        if self.source.active:
            self.active_ctrl = self.source.deactivate(self)
            if self.active_ctrl:
                self.value = self.source.value

    def update_give(self):
        if self.active_ctrl:
            self.active_ctrl = self.target.activate(self)

    @classmethod
    def get_wire_from_input(cls, node, input_num):
        wires = []
        for wire in cls.wires:
            if wire.target == node and wire.entry_connector == input_num:
                wires.append(wire)
        return wires

    @classmethod
    def get_wire_from_output(cls, node, output_num):
        wires = []
        for wire in cls.wires:
            if wire.source == node and wire.exit_connector == output_num:
                wires.append(wire)
        return wires


class Plug:
    def __init__(self, value):
        self.active_ctrl = False
        self.value = value
