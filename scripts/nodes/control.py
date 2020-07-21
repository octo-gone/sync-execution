from scripts import base, utils
from scripts import exceptions


class NodeRun(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.run = False

    def update(self):
        if not self.run:
            self.active = True
            self.run = True

    def reset(self):
        pass


class NodeStop(base.Node):
    def update(self):
        if self.active:
            raise exceptions.StopSync("node 'stop' terminate program")

    def reset(self):
        pass


class NodeWait(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.desc_value = "all" if not self.desc_value else self.desc_value
        self.send_active = False

    def reset(self):
        self.send_active = False
        self.input_values = None

    def update(self):
        if not self.input_values:
            self.input_values = [None for _ in range(len(sum(self.inputs, [])))]
        if self.active:
            if self.desc_value == "any" and any(self.input_values):
                self.send_active = True
            elif self.desc_value == "all" and all(self.input_values):
                self.send_active = True

    def activate(self, wire):
        if not self.input_values:
            self.input_values = [None for _ in range(len(sum(self.inputs, [])))]
        self.input_values[sum(self.inputs, []).index(wire)] = wire.active_ctrl
        return super().activate(wire)

    def deactivate(self, wire):
        if self.send_active:
            return super().deactivate(wire)
        return False


class NodeDelay(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.delay_counter = None
        self.start = False

    def update(self):
        if not self.input_values:
            self.input_values = [None for _ in range(len(sum(self.inputs, [])))]
        if self.active:
            if self.delay_counter is not None:
                if self.start and self.delay_counter > 0:
                    self.delay_counter -= 1
            else:
                self.call_all()

    def activate(self, wire):
        if wire in self.inputs[0]:
            self.start = wire.active_ctrl
        if wire in self.inputs[1]:
            self.delay_counter = wire.value
            if wire.value <= 0:
                raise base.NodeInputError("delay must be positive integer")
        return super().activate(wire)

    def deactivate(self, wire):
        if self.delay_counter is not None:
            if self.start and self.delay_counter <= 0:
                self.start = False
                return super().deactivate(wire)
        return False

    def reset(self):
        self.delay_counter = None
        self.start = False


class NodeTimer(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.counter = 0
        self.start = False
        self.end = False
        self.input_values = None

    def reset(self):
        self.counter = 0
        self.start = False
        self.end = False
        self.input_values = None

    def update(self):
        if len(self.inputs) != 2:
            raise exceptions.InputsCountError("wrong inputs count")
        if self.active:
            if self.start:
                self.counter += 1

    def activate(self, wire):
        if wire in self.inputs[0]:
            self.start = wire.active_ctrl
        if wire in self.inputs[1]:
            self.end = wire.active_ctrl
        return super().activate(wire)

    def deactivate(self, wire):
        if self.start and self.end:
            self.start = False
            self.end = False
            self.value = self.counter - 1
            self.counter = 0
            return super().deactivate(wire)
        return False


class NodeCtrl(base.Node):
    def update(self):
        if self.active:
            self.value = None

    def reset(self):
        pass

    def activate(self, wire):
        if wire in self.inputs[0]:
            self.value = None
        return super().activate(wire)


class NodeMerge(base.Node):
    def update(self):
        if self.active:
            if self.value is None:
                self.call_all()

    def activate(self, wire):
        if wire in self.inputs[1]:
            self.value = wire.value
        return super().activate(wire)

    def deactivate(self, wire):
        if self.value is not None:
            return super().deactivate(wire)
        return False

    def reset(self):
        self.value = None
