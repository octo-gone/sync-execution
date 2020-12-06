from scripts.nodes import base
from scripts.utils import exceptions, logger, utils
from scripts.nodes.base import ACTIVE, WAITING, INACTIVE


class NodeRun(base.Node):
    """
    Class for node 'run'. Head node that generates signal
    at the beginning of program.
    """

    def __init__(self, data):
        """
        Class constructor. Due to the fact that there is no node
        that is active at the very beginning, there is a need
        to activate this node in the constructor.

        :param dict data: node information
        """
        super().__init__(data)
        self.state = ACTIVE

    def update_waiting(self):
        """Update function, runs if state is WAITING."""
        pass

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Function activates all connected to output nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeStop(base.Node):
    """
    Class for node 'stop'. Node that stops program.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function raises exception StopSync which is possible
        to catch and report the end of the program.
        """
        raise exceptions.StopSync("Stop")

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Change state to WAITING if node state changed directly.
        """
        self.state = WAITING


class NodeWait(base.Node):
    """
    Class for node 'wait'. Node waits all signals from
    input nodes (or at least one if variant is 'any')
    """

    def __init__(self, data):
        """
        Class constructor. Creates variables:
            variant - mode of node:
                all - node waits all signals from inputs;
                any - node waits first signal from inputs.
            active_sources - list of states of inputs.

        True in active_sources means that signal has taken from input node.

        :param dict data: node information
        """
        super().__init__(data)
        self.variant = all if self.desc_value != "any" else any
        self.active_sources = None

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.active_sources = None
        self.state = INACTIVE

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If all (or any) items from active_sources are True
        then function changes state to ACTIVE.
        """
        if self.variant(map(lambda x: x is not None, self.active_sources)):
            self.state = ACTIVE

    def set_state(self, state, input_index, **kwargs):
        """
        Change state function, runs when other nodes are trying to activate current node.

        Sets True into active_sources. If variant is any and state is
        ACTIVE then function will not switch state to WAITING.
        """
        if (state == WAITING) ^ (self.variant == any and self.state == ACTIVE):
            if self.active_sources is None:
                self.active_sources = [None for _ in range(len(self.inputs[0]))]
            self.active_sources[list(map(lambda x: x[0], self.inputs[0])).index(kwargs["obj"])] = True
            self.state = WAITING


class NodeMerge(base.Node):
    """
    Class for node 'merge'. Node take value from 'value' input and
    take active signal only from 'ctrl' input.
    """

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.set_value(self.get_value(1), 0)
        self.state = INACTIVE

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Switches state to ACTIVE.
        """
        self.state = ACTIVE

    def set_state(self, state, input_index, **kwargs):
        """
        Change state function, runs when other nodes are trying to activate current node.

        Only if input_index equal to 'ctrl' input then node activates.
        """
        if state == WAITING and input_index == 0:
            self.state = state


class NodeCtrl(base.Node):
    """
    Class for node 'ctrl'. Node has constant empty output_values.
    That guarantees that only signal will be taken from previous node.
    """

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Switches state to ACTIVE.
        """
        self.state = ACTIVE


class NodeDelay(base.Node):
    """
    Class for node 'delay'. Every waiting update (if node activated)
    node reduces delay_counter. If delay_counter is equal to 0
    then node switches to ACTIVE and send signal.
    """

    def __init__(self, data):
        """
        Class constructor. Creates variables:
            delay_counter - remaining delay time.

        :param dict data: node information
        """
        super().__init__(data)
        self.delay_counter = None

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.delay_counter = None
        self.state = INACTIVE

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If node wasn't activated then function takes delay from corresponding input.

        If delay_counter has value then function reduces it by 1
        and checks for equality to zero. If delay equal or less 0 then
        function sets state to ACTIVE.
        """
        if self.delay_counter is None:
            self.delay_counter = self.get_value(1)
        if self.delay_counter is not None:
            self.delay_counter -= 1
            if self.delay_counter <= 0:
                self.state = ACTIVE

    def set_state(self, state, input_index, **kwargs):
        """
        Change state function, runs when other nodes are trying to activate current node.

        Only if input_index equal to 'ctrl' input then node activates.
        """
        if state == WAITING and input_index == 0:
            self.state = WAITING


class NodeTimer(base.Node):
    """
    Class for node 'timer'. Every waiting update (if node activated from input 'start')
    node updated timer counter. If activation signal was received
    from 'stop' input then timer return counter value.
    """

    def __init__(self, data):
        """
        Class constructor. Creates variables:
            timer_counter - variable for delay between start signal and stop signal.

        :param dict data: node information
        """
        super().__init__(data)
        self.timer_counter = None

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.timer_counter = None
        self.state = INACTIVE

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If timer_counter has value then function increases it.
        """
        if self.timer_counter is not None:
            self.timer_counter += 1

    def set_state(self, state, input_index, **kwargs):
        """
        Change state function, runs when other nodes are trying to activate current node.

        If input is 'start' then function sets timer to zero and begin counting.

        If input is 'stop' then function tries to evaluate difference between start and stop signals.
        """
        if state == WAITING and input_index == 0:
            self.state = WAITING
            self.timer_counter = 0
        if state == WAITING and input_index == 1 and self.timer_counter is not None:
            self.state = ACTIVE
            self.set_value(max(self.timer_counter - 1, 0), 0)


class NodeError(base.Node):
    """
    Class for node 'error'. If a signal was received, node
    will cause an error with information specified in the node description (desc_value).
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Log error if function runs (logger will raise exception).
        """
        logger.log_error(f"node 'error' raised exception '{self.desc_value}'")

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Change state to WAITING if node state changed directly.
        """
        self.state = WAITING


class NodeWarning(base.Node):
    """
    Class for node 'warning'. If a signal was received, node
    will cause a warning with information specified in the node description (desc_value).
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Log warning if function runs (logger will raise exception).
        """
        logger.log_warning(f"node 'warning' raised exception '{self.desc_value}'")
        self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Change state to WAITING if node state changed directly.
        """
        self.set_active(0)
        self.state = INACTIVE
