from scripts.nodes import base
from scripts.utils import exceptions, logger, utils
from scripts.nodes.base import ACTIVE, WAITING, INACTIVE


class NodeRun(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.state = ACTIVE

    def update_waiting(self):
        pass

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodeStop(base.Node):
    def update_waiting(self):
        raise exceptions.StopSync("Stop")

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodeWait(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.variant = all if self.desc_value != "any" else any
        self.active_sources = None

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE

    def update_waiting(self):
        if self.variant(map(lambda x: x is not None, self.active_sources)):
            self.state = ACTIVE

    def set_state(self, state, input_index, **kwargs):
        if (state == WAITING) ^ (self.variant == any and self.state == ACTIVE):
            if self.active_sources is None:
                self.active_sources = [None for _ in range(len(self.inputs[0]))]
            self.active_sources[list(map(lambda x: x[0], self.inputs[0])).index(kwargs["obj"])] = True
            self.state = WAITING


class NodeMerge(base.Node):

    def update_active(self):
        self.set_active(0)
        self.output_values[0] = self.get_value(1)
        self.state = INACTIVE

    def update_waiting(self):
        self.state = ACTIVE

    def set_state(self, state, input_index, **kwargs):
        if state == WAITING and self.get_actual_input(input_index) == 0:
            self.state = state


class NodeCtrl(base.Node):
    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE

    def update_waiting(self):
        self.state = ACTIVE


class NodeDelay(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.delay_counter = None

    def update_active(self):
        self.set_active(0)
        self.delay_counter = None
        self.state = INACTIVE

    def update_waiting(self):
        if self.delay_counter is None:
            self.delay_counter = self.get_value(1)
        if self.delay_counter is not None:
            self.delay_counter -= 1
            if self.delay_counter <= 0:
                self.state = ACTIVE

    def set_state(self, state, input_index, **kwargs):
        if state == WAITING and self.get_actual_input(input_index) == 0:
            self.state = WAITING


class NodeTimer(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.timer_counter = None

    def update_active(self):
        self.set_active(0)
        self.timer_counter = None
        self.state = INACTIVE

    def update_waiting(self):
        if self.timer_counter is not None:
            self.timer_counter += 1

    def set_state(self, state, input_index, **kwargs):
        if state == WAITING and self.get_actual_input(input_index) == 0:
            self.state = WAITING
            self.timer_counter = 0
        if state == WAITING and self.get_actual_input(input_index) == 1:
            self.state = ACTIVE
            self.output_values[0] = self.timer_counter


class NodeError(base.Node):

    def update_waiting(self):
        logger.log_error(f"node 'err' raised exception '{self.desc_value}'")

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE
