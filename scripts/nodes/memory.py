from scripts.utils import utils
from scripts.nodes import base
from scripts.nodes.base import ACTIVE, WAITING, INACTIVE

value_types = {
    "$int": int,
    "$real": float,
    "$bool": bool,
    "$char": utils.Char,
    "$number": utils.Number,
    "$num": utils.Number,
    "$string": str,
    "$any": utils.coercion
}


class NodeConst(base.Node):
    def update_active(self):
        pass

    def update_waiting(self):
        pass

    def __init__(self, data):
        super().__init__(data)
        self.value_type = None
        for value_type in value_types.keys():
            if self.desc_value.endswith(value_type):
                self.value_type = value_types[value_type]
                self.desc_value = self.desc_value[:-len(value_type)]
                break

    def update_inactive(self):
        value = self.desc_value
        if utils.program_values(value, True):
            value = utils.program_values(value)
        if self.value_type is not None:
            self.output_values[0] = self.value_type(value)
        else:
            self.output_values[0] = utils.coercion(value)


class NodeConstCtrl(NodeConst):
    def update_waiting(self):
        value = self.desc_value
        if utils.program_values(value, True):
            value = utils.program_values(value)
        if self.value_type is not None:
            self.output_values[0] = self.value_type(value)
        else:
            self.output_values[0] = utils.coercion(value)
        self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodeVar(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.value_type = None
        for value_type in value_types.keys():
            if self.desc_value.endswith(value_type):
                self.value_type = value_types[value_type]
                self.desc_value = self.desc_value[:self.desc_value.index("$")]
                break

    def update_inactive(self):
        var_name = f"{self.scope}$" + self.desc_value
        if var_name in self.variables:
            value = self.variables[var_name]
            if self.value_type is not None:
                self.output_values[0] = self.value_type(value)
            else:
                self.output_values[0] = utils.coercion(value)

    def update_waiting(self):
        value = self.get_value(0)
        if value is None:
            var_name = f"{self.scope}$" + self.desc_value
            if var_name in self.variables:
                value = self.variables[var_name]
                if self.value_type is not None:
                    self.output_values[0] = self.value_type(value)
                else:
                    self.output_values[0] = utils.coercion(value)
        else:
            var_name = f"{self.scope}$" + self.desc_value
            if self.value_type is not None:
                value = self.value_type(value)
            else:
                value = utils.coercion(value)
            self.variables[var_name] = value
        self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodeVarGet(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.value_type = None
        for value_type in value_types.keys():
            if self.desc_value.endswith(value_type):
                self.value_type = value_types[value_type]
                self.desc_value = self.desc_value[:self.desc_value.index("$")]
                break

    def update_inactive(self):
        var_name = f"{self.scope}$" + self.desc_value
        if var_name in self.variables:
            value = self.variables[var_name]
            if self.value_type is not None:
                self.output_values[0] = self.value_type(value)
            else:
                self.output_values[0] = utils.coercion(value)

    def update_waiting(self):
        var_name = f"{self.scope}$" + self.desc_value
        if var_name in self.variables:
            value = self.variables[var_name]
            if self.value_type is not None:
                self.output_values[0] = self.value_type(value)
            else:
                self.output_values[0] = utils.coercion(value)
        self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodeVarSet(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.value_type = None
        for value_type in value_types.keys():
            if self.desc_value.endswith(value_type):
                self.value_type = value_types[value_type]
                self.desc_value = self.desc_value[:self.desc_value.index("$")]
                break

    def update_waiting(self):
        value = self.get_value(0)
        var_name = f"{self.scope}$" + self.desc_value
        if self.value_type is not None:
            value = self.value_type(value)
        else:
            value = utils.coercion(value)
        self.variables[var_name] = value
        self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE
