from scripts import base, utils


class NodePrintCtrl(base.Node):
    def update(self):
        if self.active:
            print(self.desc_value)
            # print(self.desc_value, type(self.desc_value))

    def activate(self, wire):
        if self.desc_value == "$iteration":
            self.desc_value = utils.iteration
        elif wire.value is not None:
            if isinstance(wire.value, dict):
                if wire.value['data'] == "array":
                    print_values = "\n".join([f"{i}\t" + f"{[v]}"[1:-1] for i, v in enumerate(wire.value['values'])])
                    self.desc_value = "array\n" + print_values
            else:
                self.desc_value = wire.value
        return super().activate(wire)


class NodePrint(base.Node):
    def update(self):
        if self.active:
            self.active = False
            print(self.desc_value)

    def activate(self, wire):
        if self.desc_value == "$iteration":
            self.desc_value = utils.iteration
        elif wire.value is not None:
            if isinstance(wire.value, dict):
                if wire.value['data'] == "array":
                    print_values = "\n".join([f"{i}\t" + f"{[v]}"[1:-1] for i, v in enumerate(wire.value['values'])])
                    self.desc_value = "array\n" + print_values
            else:
                self.desc_value = wire.value
        return super().activate(wire)


class NodeInput(base.Node):
    def update(self):
        if self.active:
            self.value = utils.coercion(input())
