from scripts.nodes import base
from scripts.utils import exceptions, logger, utils
from scripts.nodes.base import ACTIVE, WAITING, INACTIVE


class NodeExample(base.Node):
    name = "example"

    def __init__(self, data):
        super().__init__(data)

    def update_waiting(self):
        self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE

    def set_state(self, state, input_index, **kwargs):
        if state == WAITING:
            self.state = state

