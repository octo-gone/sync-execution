from scripts import base


class NodeIf(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.condition = None

    def update(self):
        pass

    def reset(self):
        self.condition = None

    def deactivate(self, wire):
        if self.condition is not None:
            if wire in self.outputs[0] and self.condition:
                return super().deactivate(wire)
            elif wire in self.outputs[1] and not self.condition:
                return super().deactivate(wire)
            else:
                return False
        else:
            self.call_all()

    def activate(self, wire):
        if wire in self.inputs[1]:
            self.condition = bool(wire.value)
            return False
        return super().activate(wire)
