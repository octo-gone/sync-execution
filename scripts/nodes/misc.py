from scripts.nodes import base
from scripts.nodes.base import ACTIVE, WAITING, INACTIVE
from scripts.utils import utils


class NodeValueSwitch(base.Node):
    def update_waiting(self):
        pass

    def update_active(self):
        pass

    def set_state(self, state, input_index, **kwargs):
        if state == WAITING:
            self.output_values[0] = kwargs["obj"].output_values[kwargs["output_index"]]
            self.set_active(0)
            self.state = INACTIVE
