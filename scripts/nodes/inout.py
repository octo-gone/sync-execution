from scripts.nodes import base
from scripts.nodes.base import ACTIVE, WAITING, INACTIVE
from scripts.utils import utils


class NodePrintCtrl(base.Node):
    def update_waiting(self):
        value = self.desc_value
        if utils.program_values(value, True):
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
        if utils.program_values(value, True):
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
        prompt = "$: "
        if self.desc_value:
            prompt = self.desc_value
        value = input(prompt)
        self.output_values[0] = utils.coercion(value)
        self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE

