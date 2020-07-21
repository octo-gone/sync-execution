from scripts import base, utils


class NodeMemoryError(Exception):
    pass


class NodeConstCtrl(base.Node):
    def __init__(self, data, check_type=None):
        super().__init__(data)
        self.check_type = check_type
        self.callable = True

    def update(self):
        if self.active:
            if self.desc_value == "$iteration":
                self.value = utils.iteration
            elif self.check_type:
                try:
                    self.value = self.check_type(self.desc_value)
                except ValueError:
                    raise utils.WrongTypeError(f"type must be '{self.check_type}'")
            else:
                self.value = utils.coercion(self.desc_value)

    def prepare_value(self):
        if self.desc_value == "$iteration":
            self.value = utils.iteration
        elif self.check_type:
            try:
                self.value = self.check_type(self.desc_value)
            except ValueError:
                raise utils.WrongTypeError(f"type must be '{self.check_type}'")
        else:
            self.value = utils.coercion(self.desc_value)


class NodeConst(base.Node):
    def __init__(self, data, check_type=None):
        super().__init__(data)
        self.check_type = check_type
        self.callable = True

    def update(self):
        pass

    def prepare_value(self):
        if self.desc_value == "$iteration":
            self.value = utils.iteration
        elif self.check_type:
            try:
                self.value = self.check_type(self.desc_value)
            except ValueError:
                raise utils.WrongTypeError(f"type must be '{self.check_type}'")
        else:
            self.value = utils.coercion(self.desc_value)


class NodeVar(base.Node):
    def __init__(self, data, check_type=None):
        super().__init__(data)
        self.check_type = check_type
        self.callable = True

    def update(self):
        if self.active:
            if f"{self.desc_value}" not in self.variables:
                raise NodeMemoryError(f"no variable named '{self.desc_value}'")
            if self.variables[f"{self.desc_value}"]["data"] != "var":
                raise NodeMemoryError(f"wrong variable data '{self.variables[f'{self.desc_value}']['data']}'")
            if self.variables[f"{self.desc_value}"]["type"] is not None:
                if self.variables[f"{self.desc_value}"]["type"] != self.check_type:
                    raise utils.WrongTypeError(f"variable type must be '{self.check_type}'")
            if self.check_type:
                try:
                    value = self.variables[f"{self.desc_value}"]["value"]
                    if self.variables[f"{self.desc_value}"]["type"]:
                        value = self.variables[f"{self.desc_value}"]["type"](value)
                    self.value = self.check_type(value)
                except ValueError:
                    raise utils.WrongTypeError(f"type must be '{self.check_type}'")
            else:
                value = self.variables[f"{self.desc_value}"]["value"]
                if self.variables[f"{self.desc_value}"]["type"]:
                    value = self.variables[f"{self.desc_value}"]["type"](value)
                self.value = utils.coercion(value)

    def prepare_value(self):
        if f"{self.desc_value}" not in self.variables:
            raise NodeMemoryError(f"no variable named {self.desc_value}")
        if self.variables[f"{self.desc_value}"]["data"] != "var":
            raise NodeMemoryError(f"wrong variable data '{self.variables[f'{self.desc_value}']['data']}'")
        if self.check_type:
            try:
                value = self.variables[f"{self.desc_value}"]["value"]
                if self.variables[f"{self.desc_value}"]["type"]:
                    value = self.variables[f"{self.desc_value}"]["type"](value)
                self.value = self.check_type(value)
            except ValueError:
                raise utils.WrongTypeError(f"type must be '{self.check_type}'")
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
                    raise utils.WrongTypeError(f"type must be '{self.check_type}'")
            else:
                self.variables[f"{self.desc_value}"] = {
                    "data": "var",
                    "type": None,
                    "value": utils.coercion(wire.value)
                }
        return super().activate(wire)


class NodeArray(base.Node):
    types = [int, utils.number, float, utils.Char]

    def __init__(self, data):
        super().__init__(data)
        self.array_type = None
        self.array_len = None

    def update(self):
        if self.active:
            if self.array_type is not None and self.array_len is not None:
                self.variables[f"{self.desc_value}"] = {
                    "data": "array",
                    "name": f"{self.desc_value}",
                    "len": self.array_len,
                    "type": self.array_type,
                    "values": [None for _ in range(self.array_len)]
                }
            else:
                self.call_all()

    def activate(self, wire):
        if wire in self.inputs[0]:
            if wire.value not in self.types:
                self.array_type = type(wire.value)
            else:
                self.array_type = wire.value
        if wire in self.inputs[1]:
            self.array_len = int(wire.value)
        return super().activate(wire)

