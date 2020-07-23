from math import pi
from numbers import Real
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


class Number(Real):

    def __round__(self, ndigits=None):
        return Number(self.value.__round__(ndigits))

    def __floordiv__(self, other):
        return Number(self.value.__floordiv__(other))

    def __rfloordiv__(self, other):
        return Number(self.value.__rfloordiv__(other))

    def __mod__(self, other):
        return Number(self.value.__mod__(other))

    def __rmod__(self, other):
        return Number(self.value.__rmod__(other))

    def __lt__(self, other) -> bool:
        if type(other) is Number:
            return self.value.__lt__(other.value)
        return self.value.__lt__(other)

    def __le__(self, other) -> bool:
        if type(other) is Number:
            return self.value.__le__(other.value)
        return self.value.__le__(other)

    def __radd__(self, other):
        return Number(self.value.__radd__(other))

    def __neg__(self):
        return Number(self.value.__neg__())

    def __pos__(self):
        return Number(self.value.__pos__())

    def __mul__(self, other):
        return Number(self.value.__mul__(other))

    def __rmul__(self, other):
        return Number(self.value.__rmul__(other))

    def __div__(self, other):
        return Number(self.value.__div__(other))

    def __rdiv__(self, other):
        return Number(self.value.__rdiv__(other))

    def __truediv__(self, other):
        return Number(self.value.__truediv__(other))

    def __rtruediv__(self, other):
        return Number(self.value.__rtruediv__(other))

    def __pow__(self, exponent):
        return Number(self.value.__pow__(exponent))

    def __rpow__(self, base):
        return Number(self.value.__rpow__(base))

    def __hash__(self) -> int:
        return hash(self.value)

    def __float__(self) -> float:
        return float(self.value)

    def __init__(self, value):
        self.value = self.number_coercion(value)

    def __str__(self):
        return str(self.number_coercion(self.value))

    def __abs__(self):
        return Number(self.value.__abs__())

    def __add__(self, other):
        return Number(self.value.__add__(other))

    def __ceil__(self):
        return Number(self.value.__ceil__())

    def __eq__(self, other):
        if type(other) is Number:
            return self.value == other.value
        return self.value.__eq__(other)

    def __floor__(self):
        return Number(self.value.__floor__())

    def __trunc__(self):
        return Number(self.value.__trunc__())

    def __ge__(self, other) -> bool:
        if type(other) is Number:
            return self.value.__ge__(other.value)
        return self.value.__ge__(other)

    def __gt__(self, other) -> bool:
        if type(other) is Number:
            return self.value.__gt__(other.value)
        return self.value.__gt__(other)

    def __iadd__(self, other):
        return Number(self.value + other)

    def __isub__(self, other):
        return Number(self.value - other)

    def __imul__(self, other):
        return Number(self.value * other)

    @staticmethod
    def number_coercion(value):
        if isinstance(coercion(value), (int, float)):
            return round(coercion(value), 14)
        raise ValueError(f"invalid literal for Number: '{value}'")


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

