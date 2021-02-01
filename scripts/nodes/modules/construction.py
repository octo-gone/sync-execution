from scripts.nodes import base
from scripts.nodes.base import ACTIVE, WAITING, INACTIVE
from scripts.utils import utils, logger


READY = "ready"
ITERATION = "iteration"
BOUND = "bound"
NEXT = "next"


class NodeFor(base.Node):
    """
    Class for node 'for'. Basic loop with start 0,
    settable upper boundary and changeable increment.
    Substates:
        READY - ready to activate next node;
        ITERATION - ready to start new iteration and waits activation from 'increment' input;
        BOUND - waits init values for iteration (bound);
        NEXT - received signal from 'increment' input.
    """
    aliases = ("for", )

    def __init__(self, data):
        """
        Class constructor. Creates variables:
            value_type - data type that node operates with;
            start - state describing whether node is running or not;
            iteration - current value of iteration;
            bound - upper boundary value.

        :param dict data: node information
        """
        super().__init__(data)
        self.value_type = utils.Number
        self.start = False
        self.iteration = self.value_type(0)
        self.bound = None

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        If boundary value is not None, then node checks if bound
        value is exceeded. If exceeded then resets node and activates next nodes.

        If node is ready to activate next node then activates corresponding
        output and sets output_values of this output to current iteration (with coercion).
        """
        if self.bound is not None:
            if self.iteration >= self.bound:
                self.set_active(0)
                self.start = False
                self.iteration = self.value_type(0)
                self.set_value(None, 1)
                self.bound = None
                self.sub_state = None
                self.state = INACTIVE
        if self.sub_state == READY:
            self.sub_state = ITERATION
            self.set_value(self.value_type(self.iteration), 1)
            self.set_active(1)
            self.state = WAITING

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If node waits bound (BOUND state) then node tries to get value from corresponding input.

        If node is ready to activate next node then it sets state to ACTIVE.

        If node received signal from 'increment' input then it adds value
        from input to iteration and sets sub_state to READY.
        """
        if self.sub_state == BOUND:
            self.bound = self.value_type(self.get_value(1))
            if self.bound is not None and self.start:
                self.sub_state = READY
        if self.sub_state == READY:
            self.state = ACTIVE
        if self.sub_state == NEXT:
            self.iteration += self.value_type(self.get_value(2))
            self.sub_state = READY
            self.state = ACTIVE

    def set_state(self, state, input_index, **kwargs):
        """
        Change state function, runs when other nodes are trying to activate current node.

        If input is 'start' then node checks connection to 'bound' input and sets
        start condition to True. If there is no bound then bound value sets to -1.

        If node is ready to start new iteration and signal is from
        'increment' input then node changes sub_state to NEXT.
        """
        if state == WAITING:
            if input_index == 0:
                self.start = True
                self.bound = None if self.inputs[1] else -1
            if self.sub_state is None:
                self.sub_state = BOUND
            if self.sub_state == ITERATION and input_index == 3:
                self.sub_state = NEXT
            self.state = WAITING


class NodeForExt(base.Node):
    """
    Class for node 'for extended'. Loop with settable start,
    settable upper boundary and changeable increment.
    Substates:
        READY - ready to activate next node;
        ITERATION - ready to start new iteration and waits activation from 'increment' input;
        BOUND - waits init values for iteration;
        NEXT - received signal from 'increment' input.
    """
    aliases = ("for ext",)

    def __init__(self, data):
        """
        Class constructor. Creates variables:
            value_type - data type that node operates with;
            start - state describing whether node is running or not;
            iteration - current value of iteration;
            bound - upper boundary value.

        :param dict data: node information
        """
        super().__init__(data)
        self.value_type = utils.Number
        self.start = False
        self.iteration = None
        self.bound = None

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        If boundary value is not None, then node checks if bound
        value is exceeded. If exceeded then resets node and activates next nodes.

        If node is ready to activate next node then activates corresponding
        output and sets output_values of this output to current iteration (with coercion).
        """
        if self.bound is not None:
            if self.iteration >= self.bound:
                self.set_active(0)
                self.start = False
                self.bound = None if self.inputs[1] else -1
                self.iteration = None if self.inputs[2] else self.value_type(0)
                self.set_value(None, 1)
                self.sub_state = None
                self.state = INACTIVE
        if self.sub_state == READY:
            self.sub_state = ITERATION
            self.set_value(self.value_type(self.iteration), 1)
            self.set_active(1)
            self.state = WAITING

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If node waits bound or start value (BOUND state)
        then node tries to get values from corresponding inputs.

        If node is ready to activate next node then it sets state to ACTIVE.

        If node received signal from 'increment' input then it adds value
        from input to iteration and sets sub_state to READY.
        """
        if self.sub_state == BOUND:
            self.bound = self.value_type(self.get_value(1)) if self.inputs[1] else -1
            self.iteration = self.value_type(self.get_value(2)) if self.inputs[2] else 0
            if self.bound is not None and self.start is not None:
                self.sub_state = READY
        if self.sub_state == READY:
            self.state = ACTIVE
        if self.sub_state == NEXT:
            self.iteration += self.get_value(3)
            self.sub_state = READY
            self.state = ACTIVE

    def set_state(self, state, input_index, **kwargs):
        """
        Change state function, runs when other nodes are trying to activate current node.

        If input is 'start' then node checks connection to 'bound' input and sets
        start condition to True. If there is no bound then
        bound value sets to -1. If there is no iteration then iteration value sets to 0.

        If node is ready to start new iteration and signal is from
        'increment' input then node changes sub_state to NEXT.
        """
        if state == WAITING:
            if input_index == 0:
                self.start = True
                self.bound = self.value_type(self.get_value(1)) if self.inputs[1] else -1
                self.iteration = self.value_type(self.get_value(2)) if self.inputs[2] else 0
            if self.sub_state is None:
                self.sub_state = BOUND
            if self.sub_state == ITERATION and input_index == 3:
                self.sub_state = NEXT
            self.state = WAITING


class NodeIf(base.Node):
    """
    Class for node 'if'. Logic switch.
    Substates:
        READY - ready to activate next node;
    """
    aliases = ("if",)

    def __init__(self, data):
        """
        Class constructor. Creates variables:
            condition - upper boundary value.

        :param dict data: node information
        """
        super().__init__(data)
        self.condition = None

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        If condition is True then activates 'true' input else 'false' input.
        """
        if self.condition:
            self.condition = None
            self.set_active(0)
        else:
            self.condition = None
            self.set_active(1)
        self.state = INACTIVE

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Each update checks value from 'condition' input and
        if sub_state equals READY resets sub_state and sets state to ACTIVE.
        """
        if self.sub_state == READY:
            if len(self.inputs[1]) != 0:
                self.condition = bool(self.get_value(1))
            self.sub_state = None
            self.state = ACTIVE
        else:
            self.condition = bool(self.get_value(1))

    def set_state(self, state, input_index, **kwargs):
        """
        Change state function, runs when other nodes are trying to activate current node.

        If signal received from 'ctrl' input then sub_state changes to READY.
        """
        if state == WAITING:
            if input_index == 0:
                if len(self.inputs[1]) == 0:
                    self.condition = False
                self.sub_state = READY
            self.state = WAITING


class NodeWhile(base.Node):
    """
    Class for node 'while'. Condition loop.
    Substates:
        READY - ready to activate next node;
        ITERATION - ready to start new iteration and waits activation from 'next' input;
        BOUND - waits condition for iteration;
        NEXT - received signal from 'next' input.
    """
    aliases = ("while",)

    def __init__(self, data):
        """
        Class constructor. Creates variables:
            start - state describing whether node is running or not.

        :param dict data: node information
        """
        super().__init__(data)
        self.start = False

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        If condition value is False or driven to False, but not None
        then it resets and deactivates node and activate next node.
        """
        if self.get_value(1) is not None and not self.get_value(1):
            self.set_active(0)
            self.start = False
            self.sub_state = None
            self.state = INACTIVE
        if self.sub_state == READY:
            self.sub_state = ITERATION
            self.set_active(1)
            self.state = WAITING

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If node received signal from 'next' input
        then it sets sub_state to READY and state to ACTIVE.
        """
        if self.sub_state == BOUND:
            if self.start:
                self.sub_state = READY
        if self.sub_state == READY:
            self.state = ACTIVE
        if self.sub_state == NEXT:
            self.sub_state = READY
            self.state = ACTIVE

    def set_state(self, state, input_index, **kwargs):
        """
        Change state function, runs when other nodes are trying to activate current node.

        If input is 'start' then node change start value to True.

        If node is ready to start new iteration and signal is from
        'next' input then node changes sub_state to NEXT.
        """
        if state == WAITING:
            if input_index == 0:
                self.start = True
            if self.sub_state is None:
                self.sub_state = BOUND
            if self.sub_state == ITERATION and input_index == 2:
                self.sub_state = NEXT
            self.state = WAITING


class NodeCounter(base.Node):
    """
    Class for node 'counter'. Simplified 'for' loop with constant increment (equal 1),
    start 0 and settable upper boundary and.
    Substates:
        READY - ready to activate next node;
        ITERATION - ready to start new iteration and waits activation from 'next' input;
        BOUND - waits init values for iteration;
        NEXT - received signal from 'next' input.
    """
    aliases = ("counter",)

    def __init__(self, data):
        """
        Class constructor. Creates variables:
            value_type - data type that node operates with (int for counter);
            start - state describing whether node is running or not;
            iteration - current value of iteration;
            bound - upper boundary value.

        :param dict data: node information
        """
        super().__init__(data)
        self.value_type = int
        self.start = False
        self.iteration = self.value_type(0)
        self.bound = None

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        If boundary value is not None, then node checks if bound
        value is exceeded. If exceeded then resets node and activates next nodes.

        If node is ready to activate next node then activates corresponding
        output and sets output_values of this output to current iteration (with coercion).
        """
        if self.bound is not None:
            if self.iteration >= self.bound:
                self.set_active(0)
                self.start = False
                self.iteration = self.value_type(0)
                self.set_value(None, 1)
                self.bound = None
                self.sub_state = None
                self.state = INACTIVE
        if self.sub_state == READY:
            self.sub_state = ITERATION
            self.set_value(self.value_type(self.iteration), 1)
            self.set_active(1)
            self.state = WAITING

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If node waits bound or start value (BOUND state)
        then node tries to get values from corresponding inputs.

        If node is ready to activate next node then it sets state to ACTIVE.

        If node received signal from 'increment' input then it adds 1
        to iteration and sets sub_state to READY.
        """
        if self.sub_state == BOUND:
            self.bound = self.value_type(self.get_value(1))
            if self.bound is not None and self.start:
                self.sub_state = READY
        if self.sub_state == READY:
            self.state = ACTIVE
        if self.sub_state == NEXT:
            self.iteration += 1
            self.sub_state = READY
            self.state = ACTIVE

    def set_state(self, state, input_index, **kwargs):
        """
        Change state function, runs when other nodes are trying to activate current node.

        If input is 'start' then node checks connection to 'bound' input and sets
        start condition to True. If there is no bound then
        bound value sets to -1. If there is no iteration then iteration value sets to 0.

        If node is ready to start new iteration and signal is from
        'increment' input then node changes sub_state to NEXT.
        """
        if state == WAITING:
            if input_index == 0:
                self.start = True
                self.bound = None if self.inputs[1] else -1
            if self.sub_state is None:
                self.sub_state = BOUND
            if self.sub_state == ITERATION and input_index == 3:
                self.sub_state = NEXT
            self.state = WAITING


class NodeForeach(base.Node):
    """
    Class for node 'foreach'. Specialized loop which iterates on
    list of values from inputs (or structured variables).
    Substates:
        READY - ready to activate next node;
        ITERATION - ready to start new iteration and waits activation from 'next' input;
        BOUND - waits condition for iteration;
        NEXT - received signal from 'next' input.
    """
    aliases = ("foreach",)

    def __init__(self, data):
        """
        Class constructor. Creates variables:
            variant - method to wait for data:
                all - waits data from all input nodes;
                any - waits first not None value from inputs nodes.
            values - list of data;
            value_type - data type that node operates with;
            start - state describing whether node is running or not;
            iteration - current value of iteration;
            bound - upper boundary value.

        :param dict data: node information
        """
        super().__init__(data)
        self.variant = all if self.desc_value != "any" else any
        self.start = False
        self.iteration = 0
        self.bound = None
        self.values = None

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        If boundary value is not None, then node checks if bound
        value is exceeded. If exceeded then resets node and activates next nodes.

        If node is ready to activate next node then activates corresponding
        output and sets output_values of this output to value in
        list of values with index equal to iteration.
        """
        if self.bound is not None:
            if self.iteration >= self.bound:
                self.set_active(0)
                self.start = False
                self.iteration = 0
                self.set_value(None, 1)
                self.bound = None
                self.sub_state = None
                self.state = INACTIVE
        if self.sub_state == READY:
            self.sub_state = ITERATION
            self.set_value(self.values[self.iteration], 1)
            self.set_active(1)
            self.state = WAITING

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If node waits bound or start value (BOUND state)
        then node checks number of 'value' inputs. If 'value' inputs are empty then
        function tries to get structured variable and sets values variable
        to values from 'list', 'array' or list of keys from 'dict'.

        If node is ready to activate next node then it sets state to ACTIVE.

        If node received signal from 'increment' input then it adds 1
        to iteration and sets sub_state to READY.
        """
        if self.sub_state == BOUND:
            if not self.inputs[1]:
                var_name = f"{self.scope}$" + self.desc_value
                if var_name in self.struct_variables:
                    struct = self.struct_variables[var_name]
                    if struct["structure"] in ("list", "array"):
                        self.values = self.struct_variables[var_name]["values"]
                    elif struct["structure"] in ("dict", ):
                        self.values = self.struct_variables[var_name]["values"].keys()
                self.bound = len(self.values)
            elif self.variant(map(lambda x: x is not None, self.get_value(1, True))):
                self.values = []
                for value in self.get_value(1, True):
                    if value is not None:
                        self.values.append(value)
                self.bound = len(self.values)
            if self.bound is not None and self.start:
                self.sub_state = READY
        if self.sub_state == READY:
            self.state = ACTIVE
        if self.sub_state == NEXT:
            self.iteration += 1
            self.sub_state = READY
            self.state = ACTIVE

    def set_state(self, state, input_index, **kwargs):
        """
        Change state function, runs when other nodes are trying to activate current node.

        If input is 'start' then function sets start condition to True.

        If node is ready to start new iteration and signal is from
        'increment' input then node changes sub_state to NEXT.
        """
        if state == WAITING:
            if input_index == 0:
                self.start = True
                self.bound = None
            if self.sub_state is None:
                self.sub_state = BOUND
            if self.sub_state == ITERATION and input_index == 3:
                self.sub_state = NEXT
            self.state = WAITING


class NodeSplitString(base.Node):
    """
    Class for node 'split string'. Similar to 'foreach' node,
    but input is only one string.
    Substates:
        READY - ready to activate next node;
        ITERATION - ready to start new iteration and waits activation from 'next' input;
        BOUND - waits condition for iteration;
        NEXT - received signal from 'next' input.
    """
    aliases = ("split string",)

    def __init__(self, data):
        """
        Class constructor. Creates variables:
            values - list of data;
            start - state describing whether node is running or not;
            iteration - current value of iteration;
            bound - upper boundary value.

        :param dict data: node information
        """
        super().__init__(data)
        self.start = False
        self.iteration = 0
        self.bound = None
        self.values = None

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        If boundary value is not None, then node checks if bound
        value is exceeded. If exceeded then resets node and activates next nodes.

        If node is ready to activate next node then activates corresponding
        output and sets output_values of this output to value in
        list of values with index equal to iteration.
        """
        if self.bound is not None:
            if self.iteration >= self.bound:
                self.set_active(0)
                self.start = False
                self.iteration = 0
                self.set_value(None, 1)
                self.bound = None
                self.sub_state = None
                self.state = INACTIVE
        if self.sub_state == READY:
            self.sub_state = ITERATION
            self.set_value(self.values[self.iteration], 1)
            self.set_active(1)
            self.state = WAITING

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If node waits bound or start value (BOUND state)
        then node checks 'value' input. If 'value' input has string then
        values variable take split of string.

        If node is ready to activate next node then it sets state to ACTIVE.

        If node received signal from 'increment' input then it adds 1
        to iteration and sets sub_state to READY.
        """
        if self.sub_state == BOUND:
            if self.get_value(0) is not None:
                self.values = str(self.get_value(0)).split()
                self.bound = len(self.values)
            if self.bound is not None and self.start:
                self.sub_state = READY
        if self.sub_state == READY:
            self.state = ACTIVE
        if self.sub_state == NEXT:
            self.iteration += 1
            self.sub_state = READY
            self.state = ACTIVE

    def set_state(self, state, input_index, **kwargs):
        """
        Change state function, runs when other nodes are trying to activate current node.

        If input is 'start' then function sets start condition to True.

        If node is ready to start new iteration and signal is from
        'increment' input then node changes sub_state to NEXT.
        """
        if state == WAITING:
            if input_index == 0:
                self.start = True
                self.bound = None
            if self.sub_state is None:
                self.sub_state = BOUND
            if self.sub_state == ITERATION and input_index == 2:
                self.sub_state = NEXT
            self.state = WAITING
