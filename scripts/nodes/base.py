from abc import abstractmethod
from scripts.utils import nodes_v8 as nodes_info
from scripts.utils import logger

# the limit imposed on the number of connected wires
one_connection = ("int", "real", "obj", "char", "ctrl", "bool", "any", "number", "dir_mult_s", "dir_mult")
unlimited_connections = ("mult", "mult_s")

# separation by drawio connection count
one_connector = ("int", "real", "obj", "char", "ctrl", "bool", "any", "number", "mult_s", "dir_mult_s")
seven_connectors = ("mult", )
five_connectors = ("dir_mult", )

# basic states
ACTIVE = "active"
INACTIVE = "inactive"
WAITING = "waiting"


class Node:
    """
    Create a new node object from the given data. Node has
    some abstract methods, therefore it is better to use
    this class as parent class for specific node.
    """
    variables = {}
    struct_variables = {}
    nodes = {}

    def __init__(self, data):
        """
        Node constructor. Attribute takes dictionary with
        several descriptive parameters:
            id - identifier in xml scheme;
            node_name - name in sync language;
            value - description entered in scheme;
            inputs/outputs - input/output connectors position on node (list of floats);
            x/y/width/height - position and size of node in scheme.

        :param dict data: information about node
        """
        self.id = data["id"]
        self.nodes[self.id] = self
        self.raw_data = data

        self.name = data["node_name"]
        self.desc_value = data["value"]

        print(data["inputs"], data["outputs"])
        self.inputs = [[] for _ in range(len(data["inputs"]))]
        self.outputs = [[] for _ in range(len(data["outputs"]))]

        self.input_values = None
        self.output_values = None

        self.input_connectors = data["inputs"]
        self.output_connectors = data["outputs"]

        self.actual_inputs = None
        self.actual_outputs = None

        self.state = INACTIVE
        self.sub_state = None

        self.scope = 0
        self.pos = float(data["x"]), float(data["y"])
        self.size = float(data["width"]), float(data["height"])

    def get_actual_input(self, input_index):
        """
        Function converts input index from scheme to node
        input index. This is required, since multiple inputs
        on the diagram can come to a single node input.

        :param int input_index: index in scheme
        :return int: index in node
        """
        for key, value in self.actual_inputs.items():
            if input_index in value:
                return key

    def get_actual_output(self, output_index):
        """
        Function converts output index from scheme to node
        output index. This is required, since multiple outputs
        on the diagram can come to a single node output.

        :param int output_index: index in scheme
        :return int: index in node
        """
        for key, value in self.actual_outputs.items():
            if output_index in value:
                return key

    def get_actual_state(self):
        """
        Function generates string with state from base
        state and additional state.

        :return str: <base_state>_<sub_state>
        """
        sub_state = "_" + self.sub_state if self.sub_state is not None else ""
        return f"{self.state}{sub_state}"

    def __del__(self):
        """
        Removes node from the dictionary of all nodes.
        """
        if self.id in self.nodes:
            self.nodes.pop(self.id)

    def update_connections(self):
        """
        Function generates information about the connections
        of node inputs and inputs on the diagram. Checks whether
        the connection is correct. Creates relations between
        nodes, this requires working with the class Wire.
        """
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

        self.actual_outputs = {}
        offset = 0
        for i, v in enumerate(outputs_info):
            if v in one_connector:
                self.actual_outputs[i] = tuple(range(offset, offset + 1))
                offset += 1
            if v in seven_connectors:
                self.actual_outputs[i] = tuple(range(offset, offset + 7))
                offset += 7
            if v in five_connectors:
                self.actual_outputs[i] = tuple(range(offset, offset + 5))
                offset += 5

        for i, v in enumerate(ins):
            if inputs_info[i] in one_connection and len(v) > 1:
                logger.log_error(f"wrong input connections count in node '{self.name}/{self.id}'")

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
        """
        Function prepares and returns values from
        other nodes connected to this node. If the node inputs
        can connect more than one wire, the function will
        combine values from all nodes into a list.

        :param int input_index: actual input of node
        :param bool mult: consider the input as multiple input or not
        :return: value from input
        """
        if mult:
            values = []
            for input_node, output_index in self.inputs[input_index]:
                values.append(input_node.output_values[output_index])
            return values
        for input_node, output_index in self.inputs[input_index]:
            return input_node.output_values[output_index]

    def set_active(self, output_index):
        """
        Function runs set_state for all nodes connected to the specified output.

        :param int output_index: actual output of node
        """
        for output_node, input_index in self.outputs[output_index]:
            output_node.set_state(WAITING, input_index, obj=self, output_index=output_index)

    def set_state(self, state, input_index, **kwargs):
        """
        Changes state. Can be redefined.

        :param str state: new state
        :param int input_index: index of input from which the state change is requested
        :param kwargs: additional arguments if needed (obj and output_index)
        """
        self.state = state

    def update(self, state):
        """
        Function selects the update type depending on the current state.

        :param str state: update state
        """
        if len({self.state, state, WAITING}) == 1:
            self.update_waiting()
        if len({self.state, state, ACTIVE}) == 1:
            self.update_active()
        if len({self.state, state, INACTIVE}) == 1:
            self.update_inactive()

    @abstractmethod
    def update_active(self):
        """
        Abstract function. It runs if state is ACTIVE
        """
        pass

    @abstractmethod
    def update_waiting(self):
        """
        Abstract function. It runs if state is WAITING
        """
        pass

    def update_inactive(self):
        """
        Abstract function. It runs if state is INACTIVE
        """
        pass


class Wire:
    wires = []

    def __init__(self, data):
        self.wires.append(self)
        self.raw_data = data

        self.source = Node.nodes.get(data["source"], None)
        self.target = Node.nodes.get(data["target"], None)

        if self.source is None and self.target is None:
            logger.log_warning("no source and target nodes found")
        if self.source is None:
            logger.log_error(f"no source node found for wire with target '{self.target.name}/{self.target.id}'")
        if self.target is None:
            logger.log_error(f"no target node found for wire with source '{self.source.name}/{self.source.id}'")

        self.exit = data["exitX"], data["exitY"]
        self.entry = data["entryX"], data["entryY"]

        if self.exit[0] == self.entry[0]:
            logger.log_error(f"wrong wire connection from node '{self.source.name}/{self.source.id}' "
                             f"to node '{self.target.name}/{self.target.id}'")

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
