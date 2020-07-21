from scripts import base, utils


class NodePrintCtrl(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.init_desc_value = self.desc_value

    def update(self):
        if self.active:
            print(self.desc_value)
            # print(self.desc_value, type(self.desc_value))

    def activate(self, wire):
        if utils.get_values(self.desc_value, check=True):
            self.desc_value = utils.get_values(self.desc_value)
        elif wire.value is not None:
            self.desc_value = wire.value
        return super().activate(wire)

    def reset(self):
        self.desc_value = self.init_desc_value


class NodePrint(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.init_desc_value = self.desc_value

    def update(self):
        if self.active:
            self.active = False
            print(self.desc_value)
            self.desc_value = self.init_desc_value

    def activate(self, wire):
        if utils.get_values(self.desc_value, check=True):
            self.desc_value = utils.get_values(self.desc_value)
        elif wire.value is not None:
            self.desc_value = wire.value
        return super().activate(wire)

    def reset(self):
        pass


class NodeInput(base.Node):
    def update(self):
        if self.active:
            self.value = utils.coercion(input())

    def reset(self):
        pass
