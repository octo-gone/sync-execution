from scripts import base


class NodeValueSwitch(base.Node):

    def update(self):
        pass

    def activate(self, wire):
        self.value = wire.value
        return super().activate(wire)
