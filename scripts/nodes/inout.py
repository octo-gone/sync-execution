from scripts.nodes import base
from scripts.nodes.base import ACTIVE, WAITING, INACTIVE
from scripts.utils import utils, logger
from xml.sax import saxutils
import re


class NodePrintCtrl(base.Node):
    """
    Class for node 'print with ctrl'. Print (output) node with subsequent activation.
    """
    aliases = ("print ctrl",)

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function takes value from description (desc_value). If this value
        is a keyword ($vars and utils.program_values) then it generates
        corresponding output. Otherwise function takes value from input.

        After preparations function prints value and sets state to ACTIVE.
        """
        value = self.desc_value
        if value == "$vars":
            variables = []
            for var in self.variables.items():
                if var[0].startswith(f"{self.scope}$"):
                    variables.append((var[0][len(f"{self.scope}$"):], var[1]))
            value = dict(variables)
        elif utils.program_values(value, True):
            value = utils.program_values(value)
        elif value.endswith("$var"):
            for var in self.variables.items():
                if var[0].startswith(f"{self.scope}$"):
                    if var[0][len(f"{self.scope}$"):] == value[:-4]:
                        value = var[1]
                        break
        else:
            value = self.get_value(0)
            value = value if value is not None else self.desc_value
        print(f"{utils.iteration}:", value)
        self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodePrint(base.Node):
    """
    Class for node 'print'. Print (output) node.
    """
    aliases = ("print",)

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function takes value from description (desc_value). If this value
        is a keyword ($vars and utils.program_values) then it generates
        corresponding output. Otherwise function takes value from input.

        After preparations function prints value and sets state to ACTIVE.
        """
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
        print(f"{utils.iteration}:", value)
        self.state = INACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node.
        """
        self.state = INACTIVE


class NodeInput(base.Node):
    """
    Class for node 'input'. Input node with settable prompt for user.
    It is possible to show value from program inside of prompt by using format string.
    """
    aliases = ("input",)

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Prompt is value from node description (desc_value).
        Function tries to find construction of type {<var name>$<type>} in prompt.

        If it was found then function tries to generate string
        version of value from variable.

        If description wasn't changed then function takes '>>> ' (default) as prompt otherwise desc_value.

        After taking value from input, function saves it to output and changes state to ACTIVE.
        """
        pattern = r"{(?P<var>[^\{\}]+?)(?:\$(?P<type>[^\{\}]+?))?}"
        self.desc_value = saxutils.unescape(self.desc_value)
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
        prompt = f"{utils.iteration}: " + prompt
        if utils.colored_input is not False:
            value = logger.Color.colored_input(prompt, utils.colored_input)
        else:
            value = input(prompt)
        self.set_value(utils.coercion(value), 0)
        self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE

