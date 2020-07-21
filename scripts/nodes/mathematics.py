from scripts import base, utils
from scripts import exceptions


class NodeAbs(base.Node):
    def update(self):
        if self.active:
            if isinstance(self.value, (int, float)):
                self.value = abs(self.value)
            else:
                raise exceptions.WrongTypeError("type must be number")

    def activate(self, wire):
        if wire.value is not None:
            self.value = wire.value
        return super().activate(wire)

    def reset(self):
        pass


class NodeAdd(base.Node):
    def __init__(self, data, check_type=None):
        super().__init__(data)
        self.check_type = check_type

    def update(self):
        if not self.input_values:
            self.input_values = [None for _ in range(len(sum(self.inputs, [])))]
        if self.active:
            if all(map(lambda x: x is not None, self.input_values)):
                self.value = self.check_type(sum(self.input_values))
            else:
                self.call_all()

    def activate(self, wire):
        if self.check_type:
            try:
                self.input_values[sum(self.inputs, []).index(wire)] = self.check_type(wire.value)
            except ValueError:
                raise exceptions.WrongTypeError(f"type must be '{self.check_type}'")
        else:
            self.input_values[sum(self.inputs, []).index(wire)] = utils.coercion(wire.value)
        return super().activate(wire)

    def deactivate(self, wire):
        if self.value is not None:
            return super().deactivate(wire)
        return False

    def reset(self):
        self.value = None
        self.input_values = None


class NodeDec(base.Node):
    def update(self):
        if self.active:
            if isinstance(self.value, (int, float)):
                self.value = self.value - 1
            else:
                raise exceptions.WrongTypeError("type must be number")

    def activate(self, wire):
        if wire.value is not None:
            self.value = utils.coercion(wire.value)
        return super().activate(wire)

    def reset(self):
        pass


class NodeDivide(base.Node):
    def __init__(self, data, op="divide", coercion=False):
        super().__init__(data)
        self.dividend = None
        self.divider = None
        self.op = op
        self.coercion = coercion

    def update(self):
        if len(sum(self.inputs, [])) != 2:
            raise exceptions.InputsCountError("wrong inputs count")
        if self.active:
            if self.dividend is not None and self.divider is not None:
                if self.op == "div":
                    self.value = int(self.dividend // self.divider)
                if self.op == "mod":
                    self.value = self.dividend % self.divider
                if self.op == "divide" and self.coercion:
                    self.value = utils.coercion(self.dividend / self.divider)
                elif self.op == "divide":
                    self.value = self.dividend / self.divider
            else:
                self.call_all()

    def activate(self, wire):
        if wire in self.inputs[0]:
            self.dividend = utils.coercion(wire.value)
        if wire in self.inputs[1]:
            self.divider = utils.coercion(wire.value)
        return super().activate(wire)

    def deactivate(self, wire):
        if self.value is not None:
            return super().deactivate(wire)
        return False

    def reset(self):
        self.dividend = None
        self.divider = None
        self.value = None


class NodeExp(base.Node):
    def __init__(self, data, coercion=False):
        super().__init__(data)
        self.coercion = coercion
        self.base = None
        self.exp = None

    def update(self):
        if len(sum(self.inputs, [])) != 2:
            raise exceptions.InputsCountError("wrong inputs count")
        if self.active:
            if self.base is not None and self.exp is not None:
                if self.coercion:
                    self.value = utils.coercion(self.base ** self.exp)
                else:
                    self.value = self.base ** self.exp
            else:
                self.call_all()

    def activate(self, wire):
        if wire in self.inputs[0]:
            self.base = utils.coercion(wire)
        if wire in self.inputs[1]:
            self.exp = utils.coercion(wire)
        return super().activate(wire)

    def deactivate(self, wire):
        if self.value is not None:
            return super().deactivate(wire)
        return False

    def reset(self):
        self.base = None
        self.exp = None
        self.value = None


class NodeInc(base.Node):
    def update(self):
        if self.active:
            if isinstance(self.value, (int, float)):
                self.value = self.value + 1
            else:
                raise exceptions.WrongTypeError("type must be number")

    def activate(self, wire):
        if wire.value is not None:
            self.value = utils.coercion(wire.value)
        return super().activate(wire)

    def reset(self):
        pass


class NodeInt(base.Node):
    def update(self):
        if self.active:
            if isinstance(self.value, (int, float)):
                self.value = int(self.value)
            else:
                raise exceptions.WrongTypeError("type must be number")

    def activate(self, wire):
        if wire.value is not None:
            self.value = utils.coercion(wire.value)
        return super().activate(wire)

    def reset(self):
        pass


class NodeInv(base.Node):
    def update(self):
        if self.active:
            if isinstance(self.value, (int, float)):
                self.value = -self.value
            else:
                raise exceptions.WrongTypeError("type must be number")

    def activate(self, wire):
        if wire.value is not None:
            self.value = utils.coercion(wire.value)
        return super().activate(wire)

    def reset(self):
        pass


class NodeMult(base.Node):
    def __init__(self, data, check_type=None):
        super().__init__(data)
        self.check_type = check_type

    def reset(self):
        self.input_values = None
        self.value = None

    def update(self):
        if not self.input_values:
            self.input_values = [None for _ in range(len(sum(self.inputs, [])))]
        if not self.check_type and len(sum(self.inputs, [])) != 2:
            raise exceptions.InputsCountError("wrong inputs count")
        if self.active:
            if all(map(lambda x: x is not None, self.input_values)):
                self.value = 1
                for v in self.input_values:
                    self.value *= v
                if self.check_type:
                    self.value = self.check_type(self.value)
            else:
                self.call_all()

    def activate(self, wire):
        if self.check_type:
            try:
                self.input_values[sum(self.inputs, []).index(wire)] = self.check_type(wire.value)
            except ValueError:
                raise exceptions.WrongTypeError(f"type must be '{self.check_type}'")
        else:
            self.input_values[sum(self.inputs, []).index(wire)] = utils.coercion(wire.value)
        return super().activate(wire)

    def deactivate(self, wire):
        if self.value is not None:
            return super().deactivate(wire)
        return False


class NodeRound(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.v = None
        self.pres = None

    def reset(self):
        self.v = None
        self.pres = None
        self.value = None

    def update(self):
        if not len(self.inputs[1]):
            self.pres = 0
        if len(sum(self.inputs, [])) < 1:
            raise exceptions.InputsCountError("wrong inputs count")
        if self.active:
            if self.v is not None and self.pres is not None:
                self.value = utils.coercion(round(self.v, self.pres))

    def activate(self, wire):
        if wire in self.inputs[0]:
            self.v = utils.coercion(wire.value)
        if wire in self.inputs[1]:
            self.pres = utils.coercion(wire.value)
        return super().activate(wire)

    def deactivate(self, wire):
        if self.value is not None:
            return super().deactivate(wire)
        return False


class NodeSub(base.Node):
    def __init__(self, data, check_type=None):
        super().__init__(data)
        self.check_type = check_type
        self.minuend = None
        self.subtrahend = None

    def reset(self):
        self.minuend = None
        self.subtrahend = None
        self.value = None

    def update(self):
        if len(sum(self.inputs, [])) != 2:
            raise exceptions.InputsCountError("wrong inputs count")
        if self.active:
            if self.minuend is not None and self.subtrahend is not None:
                if self.check_type:
                    self.value = self.check_type(self.minuend - self.subtrahend)
                else:
                    self.value = utils.coercion(self.minuend) - utils.coercion(self.subtrahend)

    def activate(self, wire):
        if wire in self.inputs[0]:
            self.minuend = wire.value
        if wire in self.inputs[1]:
            self.subtrahend = wire.value
        return super().activate(wire)

    def deactivate(self, wire):
        if self.value is not None:
            return super().deactivate(wire)
        return False
