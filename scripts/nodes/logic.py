from scripts.utils import utils, logger
from scripts.nodes import base
from scripts.nodes.base import ACTIVE, WAITING, INACTIVE


class NodeLogicA(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.variant = all if self.desc_value != "any" else any

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE

    def update_waiting(self):
        if self.variant(map(lambda x: x is not None, self.get_value(0, True))):
            values = list(filter(lambda x: x is not None, self.get_value(0, True)))
            if self.name == "and":
                self.output_values[0] = all(values)
            elif self.name == "or":
                self.output_values[0] = any(values)
            elif self.name == "not and":
                self.output_values[0] = not all(values)
            elif self.name == "not or":
                self.output_values[0] = not any(values)
            elif self.name == "equal":
                self.output_values[0] = len(set(values)) == 1
            self.state = ACTIVE


class NodeLogicB(base.Node):

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE

    def update_waiting(self):
        if self.get_value(0) is not None and self.get_value(1) is not None:
            if self.name == "greater":
                self.output_values[0] = self.get_value(0) > self.get_value(1)
            if self.name == "greater or equal":
                self.output_values[0] = self.get_value(0) >= self.get_value(1)
            if self.name == "less":
                self.output_values[0] = self.get_value(0) < self.get_value(1)
            if self.name == "less or equal":
                self.output_values[0] = self.get_value(0) <= self.get_value(1)
            if self.name == "not equal":
                self.output_values[0] = self.get_value(0) != self.get_value(1)
            if self.name == "xor":
                self.output_values[0] = bool(self.get_value(0)) ^ bool(self.get_value(1))
            self.state = ACTIVE


class NodeIn(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.variant = all if self.desc_value != "any" else any

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE

    def update_waiting(self):
        if not self.inputs[0]:
            self.output_values[0] = False
            if self.desc_value in self.struct_variables:
                struct = self.struct_variables[self.desc_value]
                if struct["structure"] in ("list", "array"):
                    values = self.struct_variables[self.desc_value]["values"]
                    if self.get_value(1) in values:
                        self.output_values[0] = True
                elif struct["structure"] in ("dict", ):
                    values = self.struct_variables[self.desc_value]["values"].keys()
                    if self.get_value(1) in values:
                        self.output_values[0] = True
            self.state = ACTIVE
        elif self.variant(map(lambda x: x is not None, self.get_value(0, True))):
            self.output_values[0] = False
            for value in self.get_value(0, True):
                if self.get_value(1) == value:
                    self.output_values[0] = True
                    break
            self.state = ACTIVE

    def set_state(self, state, input_index, **kwargs):
        if state == WAITING and self.get_actual_input(input_index) == 1:
            self.state = state


class NodeBool(base.Node):
    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE

    def update_waiting(self):
        if self.get_value(0) is None:
            self.output_values[0] = False
        else:
            self.output_values[0] = bool(self.get_value(0))
        self.state = ACTIVE
