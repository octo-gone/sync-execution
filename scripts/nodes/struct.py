from scripts.utils import utils, logger
from scripts.nodes import base
from scripts.nodes.base import ACTIVE, WAITING, INACTIVE
from copy import copy


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


class NodeArrayCreate(base.Node):
    """
    Class for node 'array create'. Constructor of structured variable of type 'array'.
    """

    def __init__(self, data):
        """
        Class constructor. Creates variables:
            value_type - data type of array.

        :param dict data: node information
        """
        super().__init__(data)
        self.value_type = None
        for value_type in value_types.keys():
            if self.desc_value.endswith(value_type):
                self.value_type = value_types[value_type]
                self.desc_value = self.desc_value[:self.desc_value.index("$")]
                break
        self.value_type = int if self.value_type is None else self.value_type

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function takes name of value from node description (desc_value)
        and generates name of variable based on node scope.

        If 'length' input is not empty then function creates description
        of variable and saves it to list of structured variables.

        Variable of type 'array' has next description:
            structure - name of structure (array);
            len - length of structure;
            type - type of variables in structure;
            values - list of values in structure.
        """
        desc_value = f"{self.scope}$" + self.desc_value
        array_len = self.get_value(0)
        if array_len is not None:
            self.struct_variables[desc_value] = {
                "structure": "array",
                "len": int(array_len),
                "type": self.value_type,
                "values": [copy(utils.types_default[utils.types[self.value_type]]) for _ in range(int(array_len))]
            }
            self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeArrayGet(base.Node):
    """
    Class for node 'array get'. Node that has ability to take value from array variable.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function takes name of value from node description (desc_value)
        and generates name of variable based on node scope.

        If variable name with scope is in structured variables then function
        checks that variable structure (in structured variables) matches to node.

        If variable is suitable then function tries to take array index.

        If array index is in possible range of indexes then function sets to output value from variable.
        """
        desc_value = f"{self.scope}$" + self.desc_value
        if desc_value in self.struct_variables:
            if self.struct_variables[desc_value]["structure"] == "array":
                array_index = self.get_value(0)
                if array_index in range(self.struct_variables[desc_value]["len"]):
                    self.output_values[0] = self.struct_variables[desc_value]["values"][array_index]
        self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeArraySet(base.Node):
    """
    Class for node 'array set'. Node that has ability to set value to array variable.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function takes name of value from node description (desc_value)
        and generates name of variable based on node scope.

        If variable name with scope is in structured variables then function
        checks that variable structure (in structured variables) matches to node.

        If variable is suitable then function tries to take array index.

        If array index is in possible range of indexes then function sets value to structure.
        """
        desc_value = f"{self.scope}$" + self.desc_value
        if desc_value in self.struct_variables:
            if self.struct_variables[desc_value]["structure"] == "array":
                if self.get_value(0) is not None and self.get_value(1) is not None:
                    array_index = self.get_value(0)
                    array_value = self.get_value(1)
                    if array_index in range(self.struct_variables[desc_value]["len"]):
                        array_value = self.struct_variables[desc_value]["type"](array_value)
                        self.struct_variables[desc_value]["values"][array_index] = array_value
                    self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeArrayGetSet(base.Node):
    """
    Class for node 'array get and set'. Node that has ability to take value
    from array variable and to set value to array variable.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function takes name of value from node description (desc_value)
        and generates name of variable based on node scope.

        If variable name with scope is in structured variables then function
        checks that variable structure (in structured variables) matches to node.

        If variable is suitable then function tries to take array index.

        If array index is in possible range of indexes then
        function sets value to structure variable and to output .
        """
        array_value = None
        desc_value = f"{self.scope}$" + self.desc_value
        if desc_value in self.struct_variables:
            if self.struct_variables[desc_value]["structure"] == "array":
                if self.get_value(0) is not None:
                    if (self.get_value(1) is not None) or not self.inputs[1]:
                        array_index = self.get_value(0)
                        if array_index in range(self.struct_variables[desc_value]["len"]):
                            if self.inputs[1]:
                                array_value = self.get_value(1)
                                array_value = self.struct_variables[desc_value]["type"](array_value)
                                self.struct_variables[desc_value]["values"][array_index] = array_value
                            self.output_values[0] = self.struct_variables[desc_value]["values"][array_index]
                    if not self.inputs[1]:
                        self.state = ACTIVE
                    elif array_value is not None:
                        self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeListCreate(base.Node):
    """
    Class for node 'list create'. Constructor of structured variable of type 'list'.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function takes name of value from node description (desc_value)
        and generates name of variable based on node scope.

        Function creates description of variable and
        saves it to list of structured variables.

        Variable of type 'list' has next description:
            structure - name of structure (list);
            values - list of values in structure.
        """
        desc_value = f"{self.scope}$" + self.desc_value
        self.struct_variables[desc_value] = {
            "structure": "list",
            "values": []
        }
        self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeListGet(base.Node):
    """
    Class for node 'list get'. Node that has ability to take value from list variable.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function takes name of value from node description (desc_value)
        and generates name of variable based on node scope.

        If variable name with scope is in structured variables then function
        checks that variable structure (in structured variables) matches to node.

        If variable is suitable then function tries to take list index.

        If list index is in possible range of indexes then
        function sets value from structure variable to output.
        """
        desc_value = f"{self.scope}$" + self.desc_value
        if desc_value in self.struct_variables:
            if self.struct_variables[desc_value]["structure"] == "list":
                list_index = self.get_value(0)
                if list_index in range(len(self.struct_variables[desc_value]["values"])):
                    self.output_values[0] = self.struct_variables[desc_value]["values"][list_index]
        self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeListSet(base.Node):
    """
    Class for node 'list get and set'. Node that has ability to set value to list variable.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function takes name of value from node description (desc_value)
        and generates name of variable based on node scope.

        If variable name with scope is in structured variables then function
        checks that variable structure (in structured variables) matches to node.

        If node does not have connected to 'index' input then node switches to mode 'append'
        and add input variable to the end of list.

        Otherwise function takes index and value and sets value to structure variable using them.
        """
        desc_value = f"{self.scope}$" + self.desc_value
        if desc_value in self.struct_variables:
            if self.struct_variables[desc_value]["structure"] == "list":
                if not self.inputs[0]:
                    list_value = self.get_value(1)
                    self.struct_variables[desc_value]["values"].append(list_value)
                    self.state = ACTIVE
                elif self.get_value(0) is not None and self.get_value(1) is not None:
                    list_index = self.get_value(0)
                    list_value = self.get_value(1)
                    if list_index in range(len(self.struct_variables[desc_value]["values"])):
                        self.struct_variables[desc_value]["values"][list_index] = list_value
                    self.struct_variables[desc_value]["values"].append(list_value)
                    self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeListGetSet(base.Node):
    """
    Class for node 'list get and set'. Node that has ability to take value
    from list variable and to set value to list variable.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function takes name of value from node description (desc_value)
        and generates name of variable based on node scope.

        If variable name with scope is in structured variables then function
        checks that variable structure (in structured variables) matches to node.

        If node does not have connected to 'index' input then node switches to mode 'append'
        and add input variable to the end of list.

        Otherwise function takes list index and value (if exists).

        If node does not have connected to 'value' input then node switches to mode 'get'
        and take value from memory. Else function saves input value to variable.
        """
        array_value = None
        desc_value = f"{self.scope}$" + self.desc_value
        if desc_value in self.struct_variables:
            if self.struct_variables[desc_value]["structure"] == "list":
                if not self.inputs[0]:
                    array_value = self.get_value(1)
                    self.struct_variables[desc_value]["values"].append(array_value)
                    self.state = ACTIVE
                elif self.get_value(0) is not None:
                    if (self.get_value(1) is not None) or not self.inputs[1]:
                        array_index = self.get_value(0)
                        if array_index in range(len(self.struct_variables[desc_value]["values"])):
                            if self.inputs[1]:
                                array_value = self.get_value(1)
                                self.struct_variables[desc_value]["values"][array_index] = array_value
                            self.output_values[0] = self.struct_variables[desc_value]["values"][array_index]
                    if not self.inputs[1]:
                        self.state = ACTIVE
                    elif array_value is not None:
                        self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeListRemove(base.Node):
    """
    Class for node 'list remove'. Node that has ability to remove value from list variable.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function takes name of value from node description (desc_value)
        and generates name of variable based on node scope.

        If variable name with scope is in structured variables then function
        checks that variable structure (in structured variables) matches to node.

        If variable is suitable then function tries to take list index.

        If list index is in possible range of indexes then
        function removes value from structure variable.
        """
        desc_value = f"{self.scope}$" + self.desc_value
        if desc_value in self.struct_variables:
            if self.struct_variables[desc_value]["structure"] == "list":
                list_index = self.get_value(0)
                if list_index in range(len(self.struct_variables[desc_value]["values"])):
                    self.struct_variables[desc_value]["values"].pop(list_index)
        self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeLen(base.Node):
    """
    Class for node "len" (get length). Node return length of structured variables.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function takes name of value from node description (desc_value)
        and generates name of variable based on node scope.

        If variable exists then function takes length of variables (if possible) and saves it to output.
        """
        desc_value = f"{self.scope}$" + self.desc_value
        if desc_value in self.struct_variables:
            if self.struct_variables[desc_value]["structure"] in ("list", ):
                self.output_values[0] = len(self.struct_variables[desc_value]["values"])
            if self.struct_variables[desc_value]["structure"] in ("dict", ):
                self.output_values[0] = len(self.struct_variables[desc_value]["values"].keys())
        self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeMatrixCreate(base.Node):
    """
    Class for node 'matrix create'. Constructor of structured variable of type 'matrix'.
    """

    def __init__(self, data):
        """
        Class constructor. Creates variables:
            value_type - data type of matrix.

        :param dict data: node information
        """
        super().__init__(data)
        self.value_type = None
        for value_type in value_types.keys():
            if self.desc_value.endswith(value_type):
                self.value_type = value_types[value_type]
                self.desc_value = self.desc_value[:self.desc_value.index("$")]
                break
        self.value_type = int if self.value_type is None else self.value_type

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function takes name of value from node description (desc_value)
        and generates name of variable based on node scope.

        If size values are not equal to None then function creates description
        of variable and saves it to list of structured variables.

        Variable of type 'matrix' has next description:
            structure - name of structure (matrix);
            size - number of columns and rows;
            type - type of variables in structure;
            values - nested list of values in structure.
        """
        size_x = self.get_value(1)
        size_y = self.get_value(0)
        desc_value = f"{self.scope}$" + self.desc_value
        if size_x is not None and size_y is not None:
            self.struct_variables[desc_value] = {
                "structure": "matrix",
                "size": (int(size_x), int(size_y)),
                "type": self.value_type,
                "values": [[copy(utils.types_default[utils.types[self.value_type]]) for _ in range(int(size_x))]
                           for _ in range(int(size_y))]
            }
            self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeMatrixGet(base.Node):
    """
    Class for node 'matrix get'. Node that has ability to take value from matrix variable.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function takes name of value from node description (desc_value)
        and generates name of variable based on node scope.

        If variable name with scope is in structured variables then function
        checks that variable structure (in structured variables) matches to node.

        If matrix row and column indexes fits in possible range
        then function saves value from matrix to output.
        """
        desc_value = f"{self.scope}$" + self.desc_value
        if desc_value in self.struct_variables:
            struct = self.struct_variables[desc_value]
            if struct["structure"] == "matrix" and self.get_value(0) is not None and self.get_value(1) is not None:
                mat_index_x = self.get_value(1)
                mat_index_y = self.get_value(0)
                if mat_index_x in range(struct["size"][0]) and \
                   mat_index_y in range(struct["size"][1]):
                    self.output_values[0] = struct["values"][mat_index_y][mat_index_x]
                self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeMatrixSet(base.Node):
    """
    Class for node 'matrix set'. Node that has ability to set value to matrix variable.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function takes name of value from node description (desc_value)
        and generates name of variable based on node scope.

        If variable name with scope is in structured variables then function
        checks that variable structure (in structured variables) matches to node.

        If matrix row and column indexes fits in possible range
        then function sets value to matrix.
        """
        desc_value = f"{self.scope}$" + self.desc_value
        if desc_value in self.struct_variables:
            struct = self.struct_variables[desc_value]
            if struct["structure"] == "matrix":
                if self.get_value(0) is not None and self.get_value(1) is not None and self.get_value(2) is not None:
                    mat_value = self.get_value(2)
                    mat_index_x = self.get_value(1)
                    mat_index_y = self.get_value(0)
                    if mat_index_x in range(struct["size"][0]) and \
                       mat_index_y in range(struct["size"][1]):
                        mat_value = struct["type"](mat_value)
                        self.struct_variables[desc_value]["values"][mat_index_y][mat_index_x] = mat_value
                    self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeMatrixGetSet(base.Node):
    """
    Class for node 'matrix get and set'. Node that has ability to take value
    from matrix variable and to set value to matrix variable.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function takes name of value from node description (desc_value)
        and generates name of variable based on node scope.

        If variable name with scope is in structured variables then function
        checks that variable structure (in structured variables) matches to node.

        If matrix row and column indexes fits in possible range
        then function checks inputs.

        If node does not have connected to 'value' input nodes
        then node switches to 'get' mode and save value from matrix to output.

        Otherwise function takes value from input and saves it to matrix and to output.
        """
        mat_value = None
        desc_value = f"{self.scope}$" + self.desc_value
        if desc_value in self.struct_variables:
            struct = self.struct_variables[desc_value]
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
                                self.struct_variables[desc_value]["values"][mat_index_y][mat_index_x] = mat_value
                            self.output_values[0] = struct["values"][mat_index_y][mat_index_x]
                    if not self.inputs[1]:
                        self.state = ACTIVE
                    elif mat_value is not None:
                        self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeDictCreate(base.Node):
    """
    Class for node 'dict create'. Constructor of structured variable of type 'dictionary'.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function takes name of value from node description (desc_value)
        and generates name of variable based on node scope.

        If key or value types are not acceptable then
        function raises errors. Possible types are in utils.types.

        Variable of type 'dict' has next description:
            structure - name of structure (dict);
            key_type - type of all keys in structure;
            value_type - type of all value in structure;
            values - dict of values in structure.
        """
        key_type = self.get_value(0)
        if key_type not in utils.types and key_type is not None:
            key_type = type(key_type)
            if key_type not in utils.types:
                logger.log_error(f"unaccepted type for key in node '{self.name}/{self.id}' "
                                 f"with name '{self.desc_value}'")
        value_type = self.get_value(1)
        if value_type not in utils.types and value_type is not None:
            value_type = type(value_type)
            if value_type not in utils.types:
                logger.log_error(f"unaccepted type for value in node '{self.name}/{self.id}' "
                                 f"with name '{self.desc_value}'")
        desc_value = f"{self.scope}$" + self.desc_value
        if key_type is not None and value_type is not None:
            self.struct_variables[desc_value] = {
                "structure": "dict",
                "key_type": key_type,
                "value_type": value_type,
                "values": {}
            }
            self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeDictInsert(base.Node):
    """
    Class for node 'dict insert'. Node that has ability to insert pair into dictionary variable.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function takes name of value from node description (desc_value)
        and generates name of variable based on node scope.

        If variable name with scope is in structured variables then function
        checks that variable structure (in structured variables) matches to node.

        If key and value are valid then function (inserts) changes pair to new one.
        """
        key = self.get_value(0)
        value = self.get_value(1)
        desc_value = f"{self.scope}$" + self.desc_value
        if key is not None and value is not None:
            if desc_value in self.struct_variables:
                if self.struct_variables[desc_value]["structure"] == "dict":
                    struct = self.struct_variables[desc_value]
                    self.struct_variables[desc_value]["values"][struct["key_type"](key)] = struct["value_type"](value)
            self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeDictFind(base.Node):
    """
    Class for node 'dict find'. Node that has ability to find pair and
    output value from dictionary variable.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function takes name of value from node description (desc_value)
        and generates name of variable based on node scope.

        If variable name with scope is in structured variables then function
        checks that variable structure (in structured variables) matches to node.

        If key is valid then function takes value from variable and saves it to output.
        """
        key = self.get_value(0)
        desc_value = f"{self.scope}$" + self.desc_value
        if key is not None:
            if desc_value in self.struct_variables:
                if self.struct_variables[desc_value]["structure"] == "dict":
                    struct = self.struct_variables[desc_value]
                    self.output_values[0] = struct["values"][key]
            self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeDictInsertFind(base.Node):
    """
    Class for node 'dict insert and find'. Node that has ability to insert pair
    into dictionary variable and to find pair and output value from dictionary variable.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function takes name of value from node description (desc_value)
        and generates name of variable based on node scope.

        If variable name with scope is in structured variables then function
        checks that variable structure (in structured variables) matches to node.

        If node does not have connected to 'value' input then node switches to 'get' mode.

        If node in 'get' mode and key is valid then function takes
        value from variable and saves it to output.

        If key and value are valid then function (inserts) changes
        pair to new one and saves value from it to output.
        """
        value = None
        desc_value = f"{self.scope}$" + self.desc_value
        if desc_value in self.struct_variables:
            if self.struct_variables[desc_value]["structure"] == "dict":
                struct = self.struct_variables[desc_value]
                if self.get_value(0) is not None:
                    if (self.get_value(1) is not None) or not self.inputs[1]:
                        key = struct["key_type"](self.get_value(0))
                        if self.inputs[1]:
                            value = self.get_value(1)
                            value = struct["value_type"](value)
                            self.struct_variables[desc_value]["values"][key] = value
                            self.output_values[0] = struct["values"][key]
                        if not self.inputs[1]:
                            if key in struct["values"]:
                                self.output_values[0] = struct["values"][key]
                    if not self.inputs[1]:
                        self.state = ACTIVE
                    elif value is not None:
                        self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeDictRemove(base.Node):
    """
    Class for node 'dict remove'. Node that has ability to remove pair from dictionary variable.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function takes name of value from node description (desc_value)
        and generates name of variable based on node scope.

        If variable name with scope is in structured variables then function
        checks that variable structure (in structured variables) matches to node.

        If key is valid then function takes removes pair with specified key.
        """
        key = self.get_value(0)
        desc_value = f"{self.scope}$" + self.desc_value
        if key is not None:
            if desc_value in self.struct_variables:
                if self.struct_variables[desc_value]["structure"] == "dict":
                    struct = self.struct_variables[desc_value]
                    key = struct["key_type"](key)
                    self.struct_variables[desc_value]["values"].pop(key)
            self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE
