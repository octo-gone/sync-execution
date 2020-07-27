from scripts.nodes import base
from scripts.nodes.base import ACTIVE, WAITING, INACTIVE
from scripts.utils import utils


READY = "ready"
ITERATION = "iteration"
BOUND = "bound"
NEXT = "next"


class NodeFor(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.value_type = utils.Number
        self.start = False
        self.iteration = self.value_type(0)
        self.bound = None

    def update_active(self):
        if self.bound is not None:
            if self.iteration >= self.bound:
                self.set_active(0)
                self.start = False
                self.iteration = self.value_type(0)
                self.output_values[1] = None
                self.bound = None
                self.sub_state = None
                self.state = INACTIVE
        if self.sub_state == READY:
            self.sub_state = ITERATION
            self.output_values[1] = self.value_type(self.iteration)
            self.set_active(1)
            self.state = WAITING

    def update_waiting(self):
        if self.sub_state == BOUND:
            self.bound = self.value_type(self.get_value(1))
            if self.bound is not None and self.start:
                self.sub_state = READY
        if self.sub_state == READY:
            self.state = ACTIVE
        if self.sub_state == NEXT:
            self.iteration += self.value_type(self.get_value(2))
            self.sub_state = READY
            self.state = ACTIVE

    def set_state(self, state, input_index, **kwargs):
        if state == WAITING:
            if self.get_actual_input(input_index) == 0:
                self.start = True
                self.bound = None if self.inputs[1] else -1
            if self.sub_state is None:
                self.sub_state = BOUND
            if self.sub_state == ITERATION and self.get_actual_input(input_index) == 3:
                self.sub_state = NEXT
            self.state = WAITING


class NodeForExt(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.value_type = utils.Number
        self.start = False
        self.iteration = None
        self.bound = None

    def update_active(self):
        if self.bound:
            if self.iteration >= self.bound:
                self.set_active(0)
                self.start = False
                self.bound = None if self.inputs[1] else -1
                self.iteration = None if self.inputs[2] else self.value_type(0)
                self.output_values[1] = None
                self.sub_state = None
                self.state = INACTIVE
        if self.sub_state == READY:
            self.sub_state = ITERATION
            self.output_values[1] = self.value_type(self.iteration)
            self.set_active(1)
            self.state = WAITING

    def update_waiting(self):
        if self.sub_state == BOUND:
            self.bound = self.value_type(self.get_value(1)) if self.inputs[1] else -1
            self.iteration = self.value_type(self.get_value(2)) if self.inputs[2] else 0

            if self.bound is not None and self.start is not None:
                self.sub_state = READY
        if self.sub_state == READY:
            self.state = ACTIVE
        if self.sub_state == NEXT:
            self.iteration += self.get_value(3)
            self.sub_state = READY
            self.state = ACTIVE

    def set_state(self, state, input_index, **kwargs):
        if state == WAITING:
            if self.get_actual_input(input_index) == 0:
                self.start = True
                self.bound = self.value_type(self.get_value(1)) if self.inputs[1] else -1
                self.iteration = self.value_type(self.get_value(2)) if self.inputs[2] else 0
            if self.sub_state is None:
                self.sub_state = BOUND
            if self.sub_state == ITERATION and self.get_actual_input(input_index) == 3:
                self.sub_state = NEXT
            self.state = WAITING


class NodeIf(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.condition = None

    def update_active(self):
        if self.condition:
            self.condition = None
            self.set_active(0)
        else:
            self.condition = None
            self.set_active(1)

    def update_waiting(self):
        if self.sub_state == READY:
            if len(self.inputs) != 0:
                self.condition = bool(self.get_value(1))
            self.sub_state = None
            self.state = ACTIVE
        else:
            self.condition = bool(self.get_value(1))

    def set_state(self, state, input_index, **kwargs):
        if state == WAITING:
            if self.get_actual_input(input_index) == 0:
                if len(self.inputs) == 0:
                    self.condition = False
                self.sub_state = READY
            self.state = WAITING


class NodeWhile(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.start = False

    def update_active(self):
        if self.get_value(1) is not None and not self.get_value(1):
            self.set_active(0)
            self.start = False
            self.sub_state = None
            self.state = INACTIVE
        if self.sub_state == READY:
            self.sub_state = ITERATION
            self.set_active(1)
            self.state = WAITING

    def update_waiting(self):
        if self.sub_state == BOUND:
            if self.start:
                self.sub_state = READY
        if self.sub_state == READY:
            self.state = ACTIVE
        if self.sub_state == NEXT:
            self.sub_state = READY
            self.state = ACTIVE

    def set_state(self, state, input_index, **kwargs):
        if state == WAITING:
            if self.get_actual_input(input_index) == 0:
                self.start = True
            if self.sub_state is None:
                self.sub_state = BOUND
            if self.sub_state == ITERATION and self.get_actual_input(input_index) == 2:
                self.sub_state = NEXT
            self.state = WAITING


class NodeCounter(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.value_type = int
        self.start = False
        self.iteration = self.value_type(0)
        self.bound = None

    def update_active(self):
        if self.bound is not None:
            if self.iteration >= self.bound:
                self.set_active(0)
                self.start = False
                self.iteration = self.value_type(0)
                self.output_values[1] = None
                self.bound = None
                self.sub_state = None
                self.state = INACTIVE
        if self.sub_state == READY:
            self.sub_state = ITERATION
            self.output_values[1] = self.value_type(self.iteration)
            self.set_active(1)
            self.state = WAITING

    def update_waiting(self):
        if self.sub_state == BOUND:
            self.bound = self.value_type(self.get_value(1))
            if self.bound is not None and self.start:
                self.sub_state = READY
        if self.sub_state == READY:
            self.state = ACTIVE
        if self.sub_state == NEXT:
            self.iteration += 1
            self.sub_state = READY
            self.state = ACTIVE

    def set_state(self, state, input_index, **kwargs):
        if state == WAITING:
            if self.get_actual_input(input_index) == 0:
                self.start = True
                self.bound = None if self.inputs[1] else -1
            if self.sub_state is None:
                self.sub_state = BOUND
            if self.sub_state == ITERATION and self.get_actual_input(input_index) == 3:
                self.sub_state = NEXT
            self.state = WAITING


class NodeForeach(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.variant = all if self.desc_value != "any" else any
        self.start = False
        self.iteration = 0
        self.bound = None
        self.values = None

    def update_active(self):
        if self.bound is not None:
            if self.iteration >= self.bound:
                self.set_active(0)
                self.start = False
                self.iteration = 0
                self.output_values[1] = None
                self.bound = None
                self.sub_state = None
                self.state = INACTIVE
        if self.sub_state == READY:
            self.sub_state = ITERATION
            self.output_values[1] = self.values[self.iteration]
            self.set_active(1)
            self.state = WAITING

    def update_waiting(self):
        if self.sub_state == BOUND:
            if self.variant(map(lambda x: x is not None, self.get_value(1, True))):
                self.values = []
                for value in self.get_value(1, True):
                    if value is not None:
                        self.values.append(value)
                self.bound = len(self.values)
            if self.bound is not None and self.start:
                self.sub_state = READY
        if self.sub_state == READY:
            self.state = ACTIVE
        if self.sub_state == NEXT:
            self.iteration += 1
            self.sub_state = READY
            self.state = ACTIVE

    def set_state(self, state, input_index, **kwargs):
        if state == WAITING:
            if self.get_actual_input(input_index) == 0:
                self.start = True
                self.bound = None
            if self.sub_state is None:
                self.sub_state = BOUND
            if self.sub_state == ITERATION and self.get_actual_input(input_index) == 3:
                self.sub_state = NEXT
            self.state = WAITING
