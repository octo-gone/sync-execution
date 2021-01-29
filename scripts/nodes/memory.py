from scripts.utils import utils, logger
from scripts.nodes import base
from scripts.nodes.base import ACTIVE, WAITING, INACTIVE


# keywords in sync for types
value_types = {
    "$int": int,
    "$real": float,
    "$bool": bool,
    "$char": utils.Char,
    "$number": utils.Number,
    "$num": utils.Number,
    "$string": str,
    "$str": str,
    "$any": utils.coercion
}


class NodeConst(base.Node):
    """
    Class for node 'constant'. Node with output that based on
    node description (desc_value). It understands several
    keywords and math constants (Pi).
    """
    aliases = ("const",)

    def __init__(self, data):
        """
        Class constructor. Updates description (desc_value) if value_type is not None.
        Creates variables:
            value_type - data type that node operates with.

        :param dict data: node information
        """
        super().__init__(data)
        self.value_type = None
        for value_type in value_types.keys():
            if self.desc_value.endswith(value_type):
                self.value_type = value_types[value_type]
                self.desc_value = self.desc_value[:-len(value_type)]
                break

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.
        """
        pass

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.
        """
        pass

    def update_inactive(self):
        """
        Update function, runs if state is INACTIVE.

        Function generates value from description (desc_value)
        and saves with specified type to output.
        """
        value = self.desc_value
        if utils.program_values(value, True):
            value = utils.program_values(value)
        if self.value_type is not None:
            self.set_value(self.value_type(value), 0)
        else:
            if value.startswith("'") and value.endswith("'"):
                self.set_value(utils.Char(value[1:-1]), 0)
            elif value.startswith('"') and value.endswith('"'):
                self.set_value(str(value[1:-1]), 0)
            else:
                self.set_value(utils.coercion(value), 0)


class NodeConstCtrl(NodeConst, base.Node):
    """
    Class for node 'constant with ctrl'. Node with output that based on
    node description (desc_value). It understands several
    keywords and math constants (Pi). Activates by input signal.
    """
    aliases = ("const ctrl",)

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function generates value from description (desc_value)
        and saves with specified type to output.
        """
        value = self.desc_value
        if value.startswith("'") and value.endswith("'"):
            self.set_value(utils.Char(value[1:-1]), 0)
        elif value.startswith('"') and value.endswith('"'):
            self.set_value(str(value[1:-1]), 0)
        else:
            self.set_value(utils.coercion(value), 0)
        self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeVar(base.Node):
    """
    Class for node 'variable'. Node that manages variable with
    ability to set value to variable and get value from variable.
    """
    aliases = ("var",)

    def __init__(self, data):
        """
        Class constructor. Updates description (desc_value) if value_type is not None.
        Creates variables:
            value_type - data type that node operates with.

        :param dict data: node information
        """
        super().__init__(data)
        self.value_type = None
        for value_type in value_types.keys():
            if self.desc_value.endswith(value_type):
                self.value_type = value_types[value_type]
                self.desc_value = self.desc_value[:self.desc_value.index("$")]
                break

    def update_inactive(self):
        """
        Update function, runs if state is INACTIVE.

        If variable was created then function sets value to output.
        """
        var_name = f"{self.scope}$" + self.desc_value
        if var_name in self.variables:
            value = self.variables[var_name]
            if self.value_type is not None:
                self.set_value(self.value_type(value), 0)
            else:
                self.set_value(utils.coercion(value), 0)

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If input signal has value then node switches to set mode and saves value to variable.

        If input has no signal value then function tries to
        take value from variable and set it to output.
        """
        value = self.get_value(0)
        var_name = f"{self.scope}$" + self.desc_value
        if value is None:
            if var_name in self.variables:
                value = self.variables[var_name]
                if self.value_type is not None:
                    self.set_value(self.value_type(value), 0)
                else:
                    self.set_value(utils.coercion(value), 0)
        else:
            if self.value_type is not None:
                value = self.value_type(value)
                self.set_value(self.value_type(value), 0)
            else:
                value = utils.coercion(value)
                self.set_value(utils.coercion(value), 0)
            self.variables[var_name] = value
        self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeVarGet(base.Node):
    """
    Class for node 'variable get'. Node that manages variable with
    ability to get value from variable.
    """
    aliases = ("var get",)

    def __init__(self, data):
        """
        Class constructor. Updates description (desc_value) if value_type is not None.
        Creates variables:
            value_type - data type that node operates with.

        :param dict data: node information
        """
        super().__init__(data)
        self.value_type = None
        for value_type in value_types.keys():
            if self.desc_value.endswith(value_type):
                self.value_type = value_types[value_type]
                self.desc_value = self.desc_value[:self.desc_value.index("$")]
                break

    def update_inactive(self):
        """
        Update function, runs if state is INACTIVE.

        If variable was created then function gets value to output.
        """
        var_name = f"{self.scope}$" + self.desc_value
        if var_name in self.variables:
            value = self.variables[var_name]
            if self.value_type is not None:
                self.set_value(self.value_type(value), 0)
            else:
                self.set_value(utils.coercion(value), 0)

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function tries to take value from variable and set it to output.
        """
        var_name = f"{self.scope}$" + self.desc_value
        if var_name in self.variables:
            value = self.variables[var_name]
            if self.value_type is not None:
                self.set_value(self.value_type(value), 0)
            else:
                self.set_value(utils.coercion(value), 0)
        self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeVarSet(base.Node):
    """
    Class for node 'variable set'. Node that manages variable with
    ability to set value to variable.
    """
    aliases = ("var set",)

    def __init__(self, data):
        """
        Class constructor. Updates description (desc_value) if value_type is not None.
        Creates variables:
            value_type - data type that node operates with.

        :param dict data: node information
        """
        super().__init__(data)
        self.value_type = None
        for value_type in value_types.keys():
            if self.desc_value.endswith(value_type):
                self.value_type = value_types[value_type]
                self.desc_value = self.desc_value[:self.desc_value.index("$")]
                break

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function saves value to variable.
        """
        value = self.get_value(0)
        var_name = f"{self.scope}$" + self.desc_value
        if self.value_type is not None:
            value = self.value_type(value)
        else:
            value = utils.coercion(value)
        self.variables[var_name] = value
        self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE
