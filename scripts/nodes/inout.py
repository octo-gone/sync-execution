from scripts.nodes import base
from scripts.nodes.base import ACTIVE, WAITING, INACTIVE
from scripts.utils import utils, logger
import re


class NodePrintCtrl(base.Node):
    def update_waiting(self):
        value = self.desc_value
        if value == "$vars":
            variables = []
            for var in self.variables.items():
                if var[0].startswith(f"{self.scope}$"):
                    variables.append((var[0][len(f"{self.scope}$"):], var[1]))
            value = dict(variables)
        elif utils.program_values(value, True):
            value = utils.program_values(value)
        else:
            value = self.get_value(0)
            value = value if value is not None else self.desc_value
        print(value)
        self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodePrint(base.Node):
    def update_waiting(self):
        value = self.desc_value
        if value == "$vars":
            variables = []
            for var in self.variables.items():
                if var[0].startswith(f"{self.scope}$"):
                    variables.append((var[0][len(f"{self.scope}$"):], var[1]))
            value = dict(variables)
        elif utils.program_values(value, True):
            value = utils.program_values(value)
        else:
            value = self.get_value(0)
            value = value if value is not None else self.desc_value
        print(value)
        self.state = INACTIVE

    def update_active(self):
        self.state = INACTIVE


class NodeInput(base.Node):
    def update_waiting(self):

        pattern = r"{(?P<var>[^\{\}]+?)(?:\$(?P<type>[^\{\}]+?))?}"

        for match in re.finditer(pattern, self.desc_value):

            var_name = f"{self.scope}$" + match["var"]
            var_type = match["type"]

            if var_type is not None:
                if var_type in utils.types_default:
                    var_type = utils.types_default[var_type].__class__
                else:
                    var_type = utils.coercion

            if var_name in self.variables:
                var_value = self.variables[var_name]
                if var_type is not None:
                    var_value = var_type(var_value)
                self.desc_value = list(self.desc_value)
                self.desc_value[match.span()[0]:match.span()[1]] = list(str(var_value))
                self.desc_value = "".join(self.desc_value)

        prompt = ">>> "
        if self.desc_value:
            if self.desc_value.endswith(" "):
                prompt = self.desc_value
            else:
                prompt = self.desc_value + " "
        value = input(prompt)
        self.output_values[0] = utils.coercion(value)
        self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE

