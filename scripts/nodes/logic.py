from scripts.utils import utils, logger
from scripts.nodes import base
from scripts.nodes.base import ACTIVE, WAITING, INACTIVE


class NodeLogicA(base.Node):
    """
    Class for nodes 'and', 'or', 'not and', 'not or', 'equal'.
    Operators with multiple input.
    """

    def __init__(self, data):
        """
        Class constructor. Creates variables:
            variant - mode of node:
                all - node waits all signals from inputs;
                any - node waits first signal from inputs.

        :param dict data: node information
        """
        super().__init__(data)
        self.variant = all if self.desc_value != "any" else any

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If all items (or any - at least one item) from input are not None
        then function evaluates operation. Before evaluation function clears
        list of values from None.
        """
        if self.variant(map(lambda x: x is not None, self.get_value(0, True))):
            values = list(filter(lambda x: x is not None, self.get_value(0, True)))
            if self.name == "and":
                self.set_value(all(values), 0)
            elif self.name == "or":
                self.set_value(any(values), 0)
            elif self.name == "not and":
                self.set_value(not all(values), 0)
            elif self.name == "nor or":
                self.set_value(not any(values), 0)
            elif self.name == "equal":
                self.set_value(len(set(values)) == 1, 0)
            self.state = ACTIVE


class NodeLogicB(base.Node):
    """
    Class for nodes 'greater', 'greater or equal', 'less', 'less or equal', 'not equal', 'xor'.
    Operators with two inputs.
    """

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If both inputs have value then function evaluates operation.
        """
        if self.get_value(0) is not None and self.get_value(1) is not None:
            if self.name == "greater":
                self.set_value(self.get_value(0) > self.get_value(1), 0)
            if self.name == "greater or equal":
                self.set_value(self.get_value(0) >= self.get_value(1), 0)
            if self.name == "less":
                self.set_value(self.get_value(0) < self.get_value(1), 0)
            if self.name == "less or equal":
                self.set_value(self.get_value(0) <= self.get_value(1), 0)
            if self.name == "not equal":
                self.set_value(self.get_value(0) != self.get_value(1), 0)
            if self.name == "xor":
                self.set_value(bool(self.get_value(0)) ^ bool(self.get_value(1)), 0)
            self.state = ACTIVE


class NodeIn(base.Node):
    """
    Class for node 'in' or 'contains'. Node checks whether
    value is in list or in structure variable.
    """

    def __init__(self, data):
        """
        Class constructor. Creates variables:
            variant - mode of node:
                all - node waits all signals from inputs;
                any - node waits first signal from inputs.

        :param dict data: node information
        """
        super().__init__(data)
        self.variant = all if self.desc_value != "any" else any

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If node has no input nodes then function compares
        description of node (desc_value) to exist structure variables.
        If description has name of structure variables then function
        checks whether value is in list of values (or keys for dict).

        If node has input then based on mode (all or any) function
        checks whether value matches with something in list of input values.
        """
        if not self.inputs[0]:
            self.set_value(False, 0)
            if self.desc_value in self.struct_variables:
                struct = self.struct_variables[self.desc_value]
                if struct["structure"] in ("list", "array"):
                    values = self.struct_variables[self.desc_value]["values"]
                    if self.get_value(1) in values:
                        self.set_value(True, 0)
                elif struct["structure"] in ("dict", ):
                    values = self.struct_variables[self.desc_value]["values"].keys()
                    if self.get_value(1) in values:
                        self.set_value(True, 0)
            self.state = ACTIVE
        elif self.variant(map(lambda x: x is not None, self.get_value(0, True))):
            self.set_value(False, 0)
            for value in self.get_value(0, True):
                if self.get_value(1) == value:
                    self.set_value(True, 0)
                    break
            self.state = ACTIVE

    def set_state(self, state, input_index, **kwargs):
        """
        Change state function, runs when other nodes are trying to activate current node.

        If activation received from 'value' input (not from multiple input) then
        function change node state.
        """
        if state == WAITING and self.get_actual_input(input_index) == 1:
            self.state = state


class NodeBool(base.Node):
    """
    Class for node 'bool'. Node converts any value to boolean value.
    """

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If value is None then output value will be False.

        Else value converts to boolean with rules similar to next rules:
            1, 0.54, 504, True -> True
            0, None, False - False
            '' -> False (Empty string or char)
            'some text' -> True
        """
        if self.get_value(0) is None:
            self.set_value(False, 0)
        else:
            self.set_value(bool(self.get_value(0)), 0)
        self.state = ACTIVE
