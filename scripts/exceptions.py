

# class BaseException(Exception):
#     def __init__(self, info):
#         self.info = info
#
#     def __str__(self):
#         return f"info '{info}'"


class WrongTypeError(Exception):
    pass


class WrongInputError(Exception):
    pass


class InputsCountError(Exception):
    pass


class StopSync(Exception):
    pass


class NodeMemoryError(Exception):
    pass

