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
    variables = {}

    def __init__(self, data, check_type=None):
        super().__init__(data)
        self.check_type = check_type
        self.callable = True

    def update(self):
        if self.active:
            if f"{self.desc_value}" not in self.variables:
                raise NodeMemoryError(f"no variable names {self.desc_value}")
            if self.check_type:
                try:
                    self.value = self.check_type(self.variables[f"{self.desc_value}"])
                except ValueError:
                    raise utils.WrongTypeError(f"type must be '{self.check_type}'")
            else:
                self.value = utils.coercion(self.variables[f"{self.desc_value}"])

    def prepare_value(self):
        if self.check_type:
            try:
                self.value = self.check_type(self.variables[f"{self.desc_value}"])
            except ValueError:
                raise utils.WrongTypeError(f"type must be '{self.check_type}'")
        else:
            self.value = utils.coercion(self.variables[f"{self.desc_value}"])

    def activate(self, wire):
        if wire in self.inputs[0] and wire.value is not None:
            if self.check_type:
                try:
                    self.variables[f"{self.desc_value}"] = self.check_type(wire.value)
                except ValueError:
                    raise utils.WrongTypeError(f"type must be '{self.check_type}'")
            else:
                self.variables[f"{self.desc_value}"] = utils.coercion(wire.value)
        return super().activate(wire)


class NodeArray(base.Node):
    variables = {}
    types = [int, utils.number, float, utils.Char]

    def __init__(self, data):
        super().__init__(data)
        self.array_type = None
        self.array_len = None
        self.callable = True

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
                # TODO: change array accessibility
                self.value = self.variables[f"{self.desc_value}"]
            else:
                self.call_all()

    def prepare_value(self):
        if f"{self.desc_value}" not in self.variables:
            raise NodeMemoryError(f"no array named {self.desc_value}")
        self.value = self.variables[f"{self.desc_value}"]

    def activate(self, wire):
        if wire in self.inputs[0]:
            if wire.value not in self.types:
                self.array_type = type(wire.value)
            else:
                self.array_type = wire.value
        if wire in self.inputs[1]:
            self.array_len = int(wire.value)
        return super().activate(wire)

    def deactivate(self, wire):
        if self.value is not None:
            return super().deactivate(wire)
        return False
