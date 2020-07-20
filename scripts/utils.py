iteration = 0


class WrongTypeError(Exception):
    pass


class InputsCountError(Exception):
    pass


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
    raise WrongTypeError("type must be 'number'")


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

