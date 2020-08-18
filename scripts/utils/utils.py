from numbers import Real
import math
import sys


iteration = 0


def program_values(label, check=False):
    """
    Function checks does label belongs to keywords or returns value of keyword.

    :param str label: keyword
    :param bool check: if True function only checks whether the string belongs to keywords
    :return: value of keyword.
    """
    values = {
        "$iteration": iteration,
        "$min": -sys.maxsize,
        "$max": sys.maxsize,
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
    """
    Class for type 'char' based on class 'str' and
    redefines only initialization in which checks length of value.
    """

    def __init__(self, _):
        """
        Class constructor. If length of saved to variable value more than 1
        then function raises exception.
        """
        super().__init__()
        if len(self) > 1:
            raise ValueError(f"char most length is 1, not {len(self)}")


# auto typecasting
def coercion(value):
    """
    Function that auto typecast input value.

    If value is None then function skips typecasting.
    If value is bool then function just return value without changes.
    If value is convertible to int or float then function return numeric type.
    If value is string or similar then function tries to return char type.
    If none of conversions worked then function return unchanged value.

    :param value: input value
    :return: value
    """
    if value is not None:
        if isinstance(value, bool):
            return value
        try:
            value = float(value)
            if value == int(value):
                return int(value)
            return value
        except ValueError:
            if isinstance(value, str) and len(value) == 1:
                return Char(value)
            return value
    return None


class Number(Real):
    """Class for type 'number'."""

    def __repr__(self):
        return f"Number({self.value})"

    def __round__(self, ndigits=None):
        return self.__class__(self.value.__round__(ndigits))

    def __floordiv__(self, other):
        return self.__class__(self.value.__floordiv__(other))

    def __rfloordiv__(self, other):
        return self.__class__(self.value.__rfloordiv__(other))

    def __mod__(self, other):
        return self.__class__(self.value.__mod__(other))

    def __rmod__(self, other):
        return self.__class__(self.value.__rmod__(other))

    def __lt__(self, other) -> bool:
        if type(other) is Number:
            return self.value.__lt__(other.value)
        return self.value.__lt__(other)

    def __le__(self, other) -> bool:
        if type(other) is Number:
            return self.value.__le__(other.value)
        return self.value.__le__(other)

    def __radd__(self, other):
        return self.__class__(self.value.__radd__(other))

    def __neg__(self):
        return self.__class__(self.value.__neg__())

    def __pos__(self):
        return self.__class__(self.value.__pos__())

    def __mul__(self, other):
        return self.__class__(self.value.__mul__(other))

    def __rmul__(self, other):
        return self.__class__(self.value.__rmul__(other))

    def __div__(self, other):
        return self.__class__(self.value.__div__(other))

    def __rdiv__(self, other):
        return self.__class__(self.value.__rdiv__(other))

    def __truediv__(self, other):
        return self.__class__(self.value.__truediv__(other))

    def __rtruediv__(self, other):
        return self.__class__(self.value.__rtruediv__(other))

    def __pow__(self, exponent, modulo=None):
        if modulo is None:
            return self.__class__(self.value ** exponent)
        else:
            return self.__class__(pow(self.value, exponent, modulo))

    def __rpow__(self, base):
        return self.__class__(self.value.__rpow__(base))

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
        return self.__class__(self.value.__abs__())

    def __add__(self, other):
        return self.__class__(self.value.__add__(other))

    def __ceil__(self):
        return self.__class__(self.value.__ceil__())

    def __eq__(self, other):
        if type(other) is Number:
            return self.value == other.value
        return self.value.__eq__(other)

    def __floor__(self):
        return self.__class__(self.value.__floor__())

    def __trunc__(self):
        return self.__class__(self.value.__trunc__())

    def __ge__(self, other) -> bool:
        if type(other) is Number:
            return self.value.__ge__(other.value)
        return self.value.__ge__(other)

    def __gt__(self, other) -> bool:
        if type(other) is Number:
            return self.value.__gt__(other.value)
        return self.value.__gt__(other)

    def __iadd__(self, other):
        return self.__class__(self.value + other)

    def __isub__(self, other):
        return self.__class__(self.value - other)

    def __imul__(self, other):
        return self.__class__(self.value * other)

    @staticmethod
    def number_coercion(value):
        """
        Function returns converts value to 'int' and returns it if it has no value
        after floating point otherwise returns 'float' value.

        :param value: numeric value
        :return: typecasted value
        """
        if isinstance(coercion(value), (int, float)):
            return round(coercion(value), 14)
        raise ValueError(f"invalid literal for Number: '{value}'")


# conversion from Python types to Sync types
types = {
    int: "int",
    float: "real",
    Number: "num",
    Char: "char",
    bool: "bool",
    str: "str"
}

# conversion from Sync types to Python types (with default value)
types_default = {
    "int": int(0),
    "real": float(0),
    "number": Number(0),
    "num": Number(0),
    "char": Char(""),
    "bool": False,
    "str": str("")
}
