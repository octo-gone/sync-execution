from scripts.utils import utils, logger
from scripts.nodes import base
from scripts.nodes.base import ACTIVE, WAITING, INACTIVE
from copy import copy


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


class NodeArrayCreate(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.value_type = None
        for value_type in value_types.keys():
            if self.desc_value.endswith(value_type):
                self.value_type = value_types[value_type]
                self.desc_value = self.desc_value[:self.desc_value.index("$")]
                break
        self.value_type = int if self.value_type is None else self.value_type

    def update_waiting(self):
        array_len = self.get_value(0)
        if self.desc_value is not None and array_len is not None:
            self.struct_variables[self.desc_value] = {
                "structure": "array",
                "len": int(array_len),
                "type": self.value_type,
                "values": [copy(utils.types_default[utils.types[self.value_type]]) for _ in range(int(array_len))]
            }
            self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodeArrayGet(base.Node):
    def update_waiting(self):
        if self.desc_value in self.struct_variables:
            if self.struct_variables[self.desc_value]["structure"] == "array":
                array_index = self.get_value(0)
                if array_index in range(self.struct_variables[self.desc_value]["len"]):
                    self.output_values[0] = self.struct_variables[self.desc_value]["values"][array_index]
        self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodeArraySet(base.Node):
    def update_waiting(self):

        if self.desc_value in self.struct_variables:
            if self.struct_variables[self.desc_value]["structure"] == "array":
                if self.get_value(0) is not None and self.get_value(1) is not None:
                    array_index = self.get_value(0)
                    array_value = self.get_value(1)
                    if array_index in range(self.struct_variables[self.desc_value]["len"]):
                        array_value = self.struct_variables[self.desc_value]["type"](array_value)
                        self.struct_variables[self.desc_value]["values"][array_index] = array_value
                    self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodeArrayGetSet(base.Node):
    def update_waiting(self):
        array_value = None
        if self.desc_value in self.struct_variables:
            if self.struct_variables[self.desc_value]["structure"] == "array":
                if self.get_value(0) is not None:
                    if (self.get_value(1) is not None) or not self.inputs[1]:
                        array_index = self.get_value(0)
                        if array_index in range(self.struct_variables[self.desc_value]["len"]):
                            if self.inputs[1]:
                                array_value = self.get_value(1)
                                array_value = self.struct_variables[self.desc_value]["type"](array_value)
                                self.struct_variables[self.desc_value]["values"][array_index] = array_value
                            self.output_values[0] = self.struct_variables[self.desc_value]["values"][array_index]
                    if not self.inputs[1]:
                        self.state = ACTIVE
                    elif array_value is not None:
                        self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodeListCreate(base.Node):
    def update_waiting(self):
        if self.desc_value is not None:
            self.struct_variables[self.desc_value] = {
                "structure": "list",
                "values": []
            }
            self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodeListGet(base.Node):
    def update_waiting(self):
        if self.desc_value in self.struct_variables:
            if self.struct_variables[self.desc_value]["structure"] == "list":
                array_index = self.get_value(0)
                if array_index in range(len(self.struct_variables[self.desc_value]["values"])):
                    self.output_values[0] = self.struct_variables[self.desc_value]["values"][array_index]
        self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodeListSet(base.Node):
    def update_waiting(self):
        if self.desc_value in self.struct_variables:
            if self.struct_variables[self.desc_value]["structure"] == "list":
                if not self.inputs[0]:
                    array_value = self.get_value(1)
                    self.struct_variables[self.desc_value]["values"].append(array_value)
                    self.state = ACTIVE
                elif self.get_value(0) is not None and self.get_value(1) is not None:
                    array_index = self.get_value(0)
                    array_value = self.get_value(1)
                    if array_index in range(len(self.struct_variables[self.desc_value]["values"])):
                        self.struct_variables[self.desc_value]["values"][array_index] = array_value
                    self.struct_variables[self.desc_value]["values"].append(array_value)
                    self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodeListGetSet(base.Node):
    def update_waiting(self):
        array_value = None
        if self.desc_value in self.struct_variables:
            if self.struct_variables[self.desc_value]["structure"] == "list":
                if not self.inputs[0]:
                    array_value = self.get_value(1)
                    self.struct_variables[self.desc_value]["values"].append(array_value)
                    self.state = ACTIVE
                elif self.get_value(0) is not None:
                    if (self.get_value(1) is not None) or not self.inputs[1]:
                        array_index = self.get_value(0)
                        if array_index in range(len(self.struct_variables[self.desc_value]["values"])):
                            if self.inputs[1]:
                                array_value = self.get_value(1)
                                self.struct_variables[self.desc_value]["values"][array_index] = array_value
                            self.output_values[0] = self.struct_variables[self.desc_value]["values"][array_index]
                    if not self.inputs[1]:
                        self.state = ACTIVE
                    elif array_value is not None:
                        self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodeLen(base.Node):
    def update_waiting(self):
        if self.desc_value in self.struct_variables:
            if self.struct_variables[self.desc_value]["structure"] in ("list", "array"):
                self.output_values[0] = len(self.struct_variables[self.desc_value]["values"])
        self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodeMatrixCreate(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.value_type = None
        for value_type in value_types.keys():
            if self.desc_value.endswith(value_type):
                self.value_type = value_types[value_type]
                self.desc_value = self.desc_value[:self.desc_value.index("$")]
                break
        self.value_type = int if self.value_type is None else self.value_type

    def update_waiting(self):
        size_x = self.get_value(1)
        size_y = self.get_value(0)
        if self.desc_value is not None and size_x is not None and size_y is not None:
            self.struct_variables[self.desc_value] = {
                "structure": "matrix",
                "size": (int(size_x), int(size_y)),
                "type": self.value_type,
                "values": [[copy(utils.types_default[utils.types[self.value_type]]) for _ in range(int(size_x))]
                           for _ in range(int(size_y))]
            }
            self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodeMatrixGet(base.Node):
    def update_waiting(self):
        if self.desc_value in self.struct_variables:
            struct = self.struct_variables[self.desc_value]
            if struct["structure"] == "matrix" and self.get_value(0) is not None and self.get_value(1) is not None:
                mat_index_x = self.get_value(1)
                mat_index_y = self.get_value(0)
                if mat_index_x in range(struct["size"][0]) and \
                   mat_index_y in range(struct["size"][1]):
                    self.output_values[0] = struct["values"][mat_index_y][mat_index_x]
                self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodeMatrixSet(base.Node):
    def update_waiting(self):
        if self.desc_value in self.struct_variables:
            struct = self.struct_variables[self.desc_value]
            if struct["structure"] == "matrix":
                if self.get_value(0) is not None and self.get_value(1) is not None and self.get_value(2) is not None:
                    mat_value = self.get_value(2)
                    mat_index_x = self.get_value(1)
                    mat_index_y = self.get_value(0)
                    if mat_index_x in range(struct["size"][0]) and \
                       mat_index_y in range(struct["size"][1]):
                        mat_value = struct["type"](mat_value)
                        self.struct_variables[self.desc_value]["values"][mat_index_y][mat_index_x] = mat_value
                    self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodeMatrixGetSet(base.Node):
    def update_waiting(self):
        mat_value = None
        if self.desc_value in self.struct_variables:
            struct = self.struct_variables[self.desc_value]
            if struct["structure"] == "array":
                if self.get_value(0) is not None and self.get_value(1) is not None:
                    if (self.get_value(2) is not None) or not self.inputs[2]:
                        mat_index_x = self.get_value(1)
                        mat_index_y = self.get_value(0)
                        if mat_index_x in range(struct["size"][0]) and \
                           mat_index_y in range(struct["size"][1]):
                            if self.inputs[1]:
                                mat_value = self.get_value(2)
                                mat_value = struct["type"](mat_value)
                                self.struct_variables[self.desc_value]["values"][mat_index_y][mat_index_x] = mat_value
                            self.output_values[0] = struct["values"][mat_index_y][mat_index_x]
                    if not self.inputs[1]:
                        self.state = ACTIVE
                    elif mat_value is not None:
                        self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE

