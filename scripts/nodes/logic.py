from scripts import base, utils
from scripts import exceptions


class NodeComparisonA(base.Node):
    def __init__(self, data, op="and"):
        super().__init__(data)
        self.op = op

    def reset(self):
        self.value = None

    def update(self):
        if not self.input_values:
            self.input_values = [None for _ in range(len(sum(self.inputs, [])))]
        if self.active:
            if self.op == "and":
                if all(map(lambda x: x is not None, self.input_values)):
                    self.value = all(self.input_values)
                else:
                    self.call_all()
            if self.op == "or":
                if any(self.input_values):
                    self.value = any(self.input_values)
                elif all(map(lambda x: x is not None, self.input_values)):
                    self.value = any(self.input_values)
                else:
                    self.call_all()
            if self.op == "equal":
                if all(map(lambda x: x is not None, self.input_values)):
                    self.value = len(set(self.input_values)) == 1
                else:
                    self.call_all()

    def activate(self, wire):
        self.input_values[sum(self.inputs, []).index(wire)] = wire.value
        return super().activate(wire)

    def deactivate(self, wire):
        if self.value is not None:
            return super().deactivate(wire)
        return False


class NodeComparisonB(base.Node):
    def __init__(self, data, op="greater"):
        super().__init__(data)
        self.a = None
        self.b = None
        self.op = op

    def reset(self):
        self.value = None
        self.a = None
        self.b = None

    def update(self):
        if len(sum(self.inputs, [])) != 2:
            raise exceptions.InputsCountError("wrong inputs count")
        if self.active:
            if self.a is not None and self.b is not None:
                if self.op == "greater":
                    self.value = self.a > self.b
                if self.op == "greater or equal":
                    self.value = self.a >= self.b
                if self.op == "less":
                    self.value = self.a < self.b
                if self.op == "less or equal":
                    self.value = self.a <= self.b
                if self.op == "not equal":
                    self.value = self.a != self.b
                if self.op == "xor":
                    self.value = bool(self.a) ^ bool(self.b)
            else:
                self.call_all()

    def activate(self, wire):
        if wire in self.inputs[0]:
            self.a = wire.value
        if wire in self.inputs[1]:
            self.b = wire.value
        return super().activate(wire)

    def deactivate(self, wire):
        if self.value is not None:
            return super().deactivate(wire)
        return False


class NodeNot(base.Node):
    def update(self):
        if self.active:
            self.value = not self.value

    def activate(self, wire):
        self.value = bool(wire.value)
        return super().activate(wire)

    def reset(self):
        pass
