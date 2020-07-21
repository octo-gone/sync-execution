from math import pi
from scripts import exceptions
iteration = 0


def get_values(label, check=False):
    values = {
        "$iteration": iteration,
        "$pi": pi,
        "$true": True,
        "$false": False,
        "$none": "",
    }
    if check:
        return label in values
    return values[label]


# char type
class Char(str):
    def __init__(self, _):
        super().__init__()
        if len(self) != 1:
            raise ValueError


# TODO: change function to class
# number type (simple coercion)
def number(v):
    try:
        v = float(v)
        if v == int(v):
            return int(v)
        return v
    except ValueError:
        pass
    raise exceptions.WrongTypeError("type must be 'number'")


# auto typecasting
def coercion(value):
    if value is not None:
        try:
            value = float(value)
            if value == int(value):
                return int(value)
            return value
        except ValueError:
            if len(value) == 1:
                return Char(value)
            return value
    return None

