from scripts import base, utils
from scripts import exceptions


class NodeConstCtrl(base.Node):
    def __init__(self, data, check_type=None):
        super().__init__(data)
        self.check_type = check_type
        self.callable = True

    def update(self):
        if self.active:
            if utils.get_values(self.desc_value, check=True):
                self.desc_value = utils.get_values(self.desc_value)
            if self.check_type:
                try:
                    self.value = self.check_type(self.desc_value)
                except ValueError:
                    raise exceptions.WrongTypeError(f"type must be '{self.check_type}'")
            else:
                self.value = utils.coercion(self.desc_value)

    def reset(self):
        pass

    def prepare_value(self):
        if self.desc_value == "$iteration":
            self.value = utils.iteration
        elif self.check_type:
            try:
                self.value = self.check_type(self.desc_value)
            except ValueError:
                raise exceptions.WrongTypeError(f"type must be '{self.check_type}'")
        else:
            self.value = utils.coercion(self.desc_value)


class NodeConst(base.Node):
    def __init__(self, data, check_type=None):
        super().__init__(data)
        self.check_type = check_type
        self.callable = True

    def update(self):
        pass

    def reset(self):
        pass

    def prepare_value(self):
        if utils.get_values(self.desc_value, check=True):
            self.desc_value = utils.get_values(self.desc_value)
        if self.check_type:
            try:
                self.value = self.check_type(self.desc_value)
            except ValueError:
                raise exceptions.WrongTypeError(f"type must be '{self.check_type}'")
        else:
            self.value = utils.coercion(self.desc_value)


class NodeVar(base.Node):
    def __init__(self, data, check_type=None):
        super().__init__(data)
        self.check_type = check_type
        self.callable = True

    def update(self):
        if self.active:
            if len(self.outputs[0]) == 0:
                self.active = False
            if f"{self.desc_value}" not in self.variables:
                raise exceptions.NodeMemoryError(f"no variable named '{self.desc_value}'")
            if self.variables[f"{self.desc_value}"]["data"] != "var":
                raise exceptions.NodeMemoryError(f"wrong variable data "
                                                 f"'{self.variables[f'{self.desc_value}']['data']}'")
            if self.variables[f"{self.desc_value}"]["type"] is not None:
                if self.variables[f"{self.desc_value}"]["type"] != self.check_type:
                    raise exceptions.WrongTypeError(f"variable type must be '{self.check_type}'")
            if self.check_type:
                try:
                    value = self.variables[f"{self.desc_value}"]["value"]
                    if self.variables[f"{self.desc_value}"]["type"]:
                        value = self.variables[f"{self.desc_value}"]["type"](value)
                    self.value = self.check_type(value)
                except ValueError:
                    raise exceptions.WrongTypeError(f"type must be '{self.check_type}'")
            else:
                value = self.variables[f"{self.desc_value}"]["value"]
                if self.variables[f"{self.desc_value}"]["type"]:
                    value = self.variables[f"{self.desc_value}"]["type"](value)
                self.value = utils.coercion(value)

    def reset(self):
        pass

    def prepare_value(self):
        if f"{self.desc_value}" not in self.variables:
            raise exceptions.NodeMemoryError(f"no variable named {self.desc_value}")
        if self.variables[f"{self.desc_value}"]["data"] != "var":
            raise exceptions.NodeMemoryError(f"wrong variable data '{self.variables[f'{self.desc_value}']['data']}'")
        if self.check_type:
            try:
                value = self.variables[f"{self.desc_value}"]["value"]
                if self.variables[f"{self.desc_value}"]["type"]:
                    value = self.variables[f"{self.desc_value}"]["type"](value)
                self.value = self.check_type(value)
            except ValueError:
                raise exceptions.WrongTypeError(f"type must be '{self.check_type}'")
        else:
            value = self.variables[f"{self.desc_value}"]["value"]
            if self.variables[f"{self.desc_value}"]["type"]:
                value = self.variables[f"{self.desc_value}"]["type"](value)
            self.value = utils.coercion(value)

    def activate(self, wire):
        if wire in self.inputs[0] and wire.value is not None:
            if self.check_type:
                try:
                    self.variables[f"{self.desc_value}"] = {
                        "data": "var",
                        "type": self.check_type,
                        "value": self.check_type(wire.value)
                    }
                except ValueError:
                    raise exceptions.WrongTypeError(f"type must be '{self.check_type}'")
            else:
                self.variables[f"{self.desc_value}"] = {
                    "data": "var",
                    "type": None,
                    "value": utils.coercion(wire.value)
                }
        if wire in self.inputs[0] and wire.value is None:
            if f"{self.desc_value}" not in self.variables:
                raise exceptions.NodeMemoryError(f"no variable named {self.desc_value}")
            self.value = self.variables[f"{self.desc_value}"]
        return super().activate(wire)


class NodeArray(base.Node):
    types = [int, utils.number, float, utils.Char]
    default_values = {
        int: 0,
        utils.number: 0,
        float: 0.0,
        utils.Char: "",
        str: "",
        bool: False,
    }

    def __init__(self, data):
        super().__init__(data)
        self.array_type = None
        self.array_len = None
        self.default_value = None

    def reset(self):
        self.array_type = None
        self.array_len = None
        self.default_value = None

    def update(self):
        if self.active:
            if self.array_type is not None and self.array_len is not None:
                self.variables[f"{self.desc_value}"] = {
                    "data": "array",
                    "name": f"{self.desc_value}",
                    "len": self.array_len,
                    "type": self.array_type,
                    "values": [self.default_value for _ in range(self.array_len)]
                }
            else:
                self.call_all()

    def activate(self, wire):
        if wire in self.inputs[0]:
            if wire.value not in self.types:
                self.array_type = type(wire.value)
                if self.array_type in self.types:
                    self.default_value = self.default_values[type(wire.value)]
                else:
                    self.default_value = wire.value
            else:
                self.array_type = wire.value
                self.default_value = self.default_values[wire.value]
        if wire in self.inputs[1]:
            self.array_len = int(wire.value)
        return super().activate(wire)

    def deactivate(self, wire):
        if self.array_type is not None and self.array_len is not None:
            return super().deactivate(wire)
        return False


class NodeArrayGS(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.index = None
        self.set_value = None
        self.get_value = False

    def reset(self):
        self.index = None
        self.set_value = None
        self.get_value = False
        self.value = None

    def update(self):
        if self.active:
            # print(self.index)
            if f"{self.desc_value}" not in self.variables:
                raise exceptions.NodeMemoryError(f"no variable named '{self.desc_value}'")
            if len(self.inputs[1]) == 1 and self.set_value is None:
                self.call_back(self.inputs[1][0])
            if self.index is not None:
                if len(self.inputs[1]) == 0:
                    self.value = self.variables[f"{self.desc_value}"]["values"][self.index]
                    self.set_value = self.variables[f"{self.desc_value}"]["values"][self.index]
                elif self.set_value is not None:
                    # print(self.set_value, self.value, self.index)
                    value_type = self.variables[f"{self.desc_value}"]["type"]
                    self.variables[f"{self.desc_value}"]["values"][self.index] = value_type(self.set_value)
                    self.value = self.variables[f"{self.desc_value}"]["values"][self.index]
            else:
                if self.set_value is not None:
                    self.call_back(self.inputs[0][0])
                else:
                    self.call_all()

    def activate(self, wire):

        if wire in self.inputs[0]:
            self.index = int(wire.value)

        if wire in self.inputs[1]:
            self.set_value = wire.value

        return super().activate(wire)

    def deactivate(self, wire):
        if (self.value is not None) or self.get_value:
            return super().deactivate(wire)
        return False
