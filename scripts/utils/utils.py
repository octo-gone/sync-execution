from numbers import Real
import math
import ctypes


iteration = 0


def program_values(label, check=False):
    values = {
        "$iteration": iteration,
        "$pi": math.pi,
        "$true": True,
        "$false": False,
        "$none": "",
        "$sep": "- - -",
    }
    if check:
        return label in values
    return values[label]


# char type
class Char(str):
    def __init__(self, _):
        super().__init__()
        if len(self) > 1:
            raise ValueError(f"char most length is 1, not {len(self)}")


# auto typecasting
def coercion(value):
    if value is not None:
        if isinstance(value, bool):
            return value
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

    def __int__(self) -> int:
        return int(self.value)

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


types = {
    int: "int",
    float: "real",
    Number: "num",
    Char: "char",
    bool: "bool",
    str: "str"
}

types_default = {
    "int": int(0),
    "real": float(0),
    "number": Number(0),
    "num": Number(0),
    "char": Char(""),
    "bool": False,
    "str": str("")
}


# add color support for console
kernel32 = ctypes.WinDLL('kernel32')
hStdOut = kernel32.GetStdHandle(-11)
mode = ctypes.c_ulong()
kernel32.GetConsoleMode(hStdOut, ctypes.byref(mode))
mode.value |= 4
kernel32.SetConsoleMode(hStdOut, mode)


class Color:
    colors = {
        "red": 1,
        "green": 2,
        "yellow": 3,

        "blue": 4,
        "light blue": 12,
        "cyan": 14,

        "purple": 5,
        "magenta": 15,

        "peach": 9,

        "grey": 7,
        "dark grey": 8
    }

    @classmethod
    def foreground(cls, text, color):
        if color in cls.colors:
            color = cls.colors[color]
        return "\33[38;5;" + str(color) + "m" + text + "\33[0m"

    @classmethod
    def background(cls, text, color):
        if color in cls.colors:
            color = cls.colors[color]
        return "\33[48;5;" + str(color) + "m" + text + "\33[0m"

    @classmethod
    def colored(cls, text, fg, bg=None):
        if bg is not None:
            text = cls.background(text, bg)
        return cls.foreground(text, fg)
