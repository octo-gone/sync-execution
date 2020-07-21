from scripts import base
from scripts import exceptions


class NodeIf(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.condition = None

    def update(self):
        pass

    def reset(self):
        self.condition = None

    def deactivate(self, wire):
        if self.condition is not None:
            if wire in self.outputs[0] and self.condition:
                return super().deactivate(wire)
            elif wire in self.outputs[1] and not self.condition:
                return super().deactivate(wire)
            else:
                return False
        else:
            self.call_all()

    def activate(self, wire):
        if wire in self.inputs[1]:
            self.condition = bool(wire.value)
            return False
        return super().activate(wire)


class NodeForeach(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.start = False
        self.start_iter = False
        self.end = False
        self.iteration = None
        self.next = False
        self.deactivate_next = False

    def update(self):
        if not self.input_values:
            self.input_values = [None for _ in range(len(self.inputs[1]))]
        if self.active:

            if self.start_iter:
                if self.next:
                    self.iteration += 1
                #     if len(self.inputs[1]) == 0:
                #         while self.iteration < len(self.input_values) and self.input_values[self.iteration] is None:
                #             self.iteration += 1
                if self.iteration >= len(self.input_values):
                    self.end = True
            else:
                if len(self.inputs[1]) == 0:
                    if self.desc_value not in self.variables:
                        raise exceptions.NodeMemoryError(f"no array named '{self.desc_value}'")
                    if self.variables[self.desc_value]["data"] != "array":
                        raise exceptions.NodeMemoryError(f"no array named '{self.desc_value}'")
                    self.input_values = self.variables[self.desc_value]["values"]
                    self.start_iter = True
                    self.next = True
                elif all(map(lambda x: x is not None, self.input_values)):
                    self.start_iter = True
                    self.next = True
                else:
                    self.call_all()

            print(self.iteration, self.start, self.start_iter, self.input_values, self.next)
            input()

    def reset(self):
        self.start = False
        self.end = False
        self.iteration = None
        self.input_values = None
        self.next = False
        self.deactivate_next = False

    def activate(self, wire):
        if wire in self.inputs[0]:
            self.start = True
            self.iteration = 0
        if wire in self.inputs[1]:
            self.input_values[self.inputs[1].index(wire)] = wire.value
        if wire in self.inputs[2]:
            if not self.start:
                raise exceptions.WrongInputError("next iteration impossible if iteration not started")
            self.next = True
        return super().activate(wire)

    def post_update(self):
        if self.deactivate_next:
            self.next = False
        return super().post_update()

    def deactivate(self, wire):
        if wire in self.outputs[0] and self.end:
            return super().deactivate(wire)
        if wire in self.outputs[1] and not self.end and self.next:
            self.value = self.input_values[self.iteration]
            self.deactivate_next = True
            return True
        return False
