from scripts.nodes import base
from scripts.utils import utils, logger
from scripts.nodes.base import ACTIVE, WAITING, INACTIVE


class NodeAbs(base.Node):
    def update_waiting(self):
        if self.get_value(0) is not None:
            self.output_values[0] = abs(self.get_value(0))
            self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodeAdd(base.Node):
    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE

    def update_waiting(self):
        if all(map(lambda x: x is not None, self.get_value(0, True))):
            self.output_values[0] = sum(self.get_value(0, True))
            self.state = ACTIVE


class NodeDec(base.Node):
    def update_waiting(self):
        if self.get_value(0) is not None:
            self.output_values[0] = self.get_value(0) - 1
            self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodeDivision(base.Node):
    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE

    def update_waiting(self):
        if self.get_value(0) is not None and self.get_value(1) is not None:
            self.output_values[0] = self.get_value(0) / self.get_value(1)
            self.state = ACTIVE


class NodeExp(base.Node):
    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE

    def update_waiting(self):
        if self.get_value(0) is not None and self.get_value(1) is not None:
            self.output_values[0] = self.get_value(0) ** self.get_value(1)
            self.state = ACTIVE


class NodeInc(base.Node):
    def update_waiting(self):
        if self.get_value(0) is not None:
            self.output_values[0] = self.get_value(0) + 1
            self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodeTrunc(base.Node):
    def update_waiting(self):
        if self.get_value(0) is not None:
            self.output_values[0] = int(self.get_value(0))
            self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodeInv(base.Node):
    def update_waiting(self):
        if self.get_value(0) is not None:
            self.output_values[0] = int(self.get_value(0))
            self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE


class NodeMult(base.Node):
    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE

    def update_waiting(self):
        if all(map(lambda x: x is not None, self.get_value(0, True))):
            m = 1
            for v in self.get_value(0, True):
                m *= v
            self.output_values[0] = m
            self.state = ACTIVE


class NodeRound(base.Node):
    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE

    def update_waiting(self):
        pres = self.get_value(1) if self.inputs[1] else 0
        if self.get_value(0) is not None and pres is not None:
            self.output_values[0] = round(self.get_value(0), pres)
            self.state = ACTIVE


class NodeSub(base.Node):
    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE

    def update_waiting(self):
        if self.get_value(0) is not None and self.get_value(1) is not None:
            self.output_values[0] = self.get_value(0) - self.get_value(1)
            self.state = ACTIVE
