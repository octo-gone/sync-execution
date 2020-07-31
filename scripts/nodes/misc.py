from scripts.nodes import base
from scripts.nodes.base import ACTIVE, WAITING, INACTIVE
from scripts.utils import utils, logger
import random


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


class NodeGetType(base.Node):
    def update_inactive(self):
        if self.desc_value in utils.types_default:
            self.output_values[1] = utils.types_default[self.desc_value]
            self.output_values[0] = type(utils.types_default[self.desc_value])
        else:
            self.output_values[0] = None
            self.output_values[1] = None

    def update_waiting(self):
        pass

    def update_active(self):
        pass


class NodeType(base.Node):
    def update_waiting(self):
        self.output_values[0] = type(self.get_value(0))
        self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodeRandom(base.Node):
    def update_waiting(self):
        self.output_values[0] = random.random()
        self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodeRandomInt(base.Node):
    def update_waiting(self):
        if self.get_value(0) is not None and self.get_value(1) is not None:
            self.output_values[0] = random.randrange(int(self.get_value(0)), int(self.get_value(1)))
            self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodeRandomNum(base.Node):
    def update_waiting(self):
        if self.get_value(0) is not None and self.get_value(1) is not None:
            self.output_values[0] = utils.Number(self.get_value(0) +
                                                 random.random() * (self.get_value(1) - self.get_value(0)))
            self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE
