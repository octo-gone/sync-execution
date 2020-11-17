from scripts.nodes import base
from scripts.utils import exceptions, logger, utils
from scripts.nodes.base import ACTIVE, WAITING, INACTIVE


class NodeCount16(base.Node):
    name = "count 16"
    desc = {
        'inner': 'C16',
        'label': 'count 16',
        'inputs': ('ctrl', 'ctrl'),
        'outputs': ('int',),
        'tooltip': {
            'label': 'Count 16 (+/-)',
            'desc': 'Счетчик 16',
            'input': [
                ('Вход', 'Увеличивающий вход'),
                ('Вход', 'Уменьшающий вход'),
            ],
            'outputs': [
                ('Выход', 'Значение'),
            ],
            'adds': 'Счетчик с пересчетом 16, где один входной порт увеличивает, а другой уменьшает',
        }
    }

    def __init__(self, data):
        super().__init__(data)
        self.count = 0
        self.operation = None

    def update_waiting(self):
        if self.operation == "+":
            new_value = (self.count + 1) % 16
            self.set_value(new_value, 0)
            self.count = new_value
        elif self.count == 0:
            new_value = 15
            self.set_value(new_value, 0)
            self.count = new_value
        else:
            new_value = self.count - 1
            self.set_value(new_value, 0)
            self.count = new_value
        self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE

    def set_state(self, state, input_index, **kwargs):
        if input_index == 0:
            self.operation = "+"
        else:
            self.operation = "-"
        self.state = state
