import ctypes
from scripts.utils import utils


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
    def colored(cls, text, fg=None, bg=None):
        if bg is not None:
            text = cls.background(text, bg)
        if fg is not None:
            text = cls.foreground(text, fg)
        return text


def log_error(message):
    print(Color.colored(f"[ ERR ] [ ITERATION {utils.iteration} ] {message}", fg="red"))
    exit()


def log_warning(message):
    print(Color.colored(f"[ WAR ] [ ITERATION {utils.iteration} ] {message}", fg="yellow"))


def log_success(message):
    print(Color.colored(f"[ SCS ] [ ITERATION {utils.iteration} ] {message}", fg="green"))


def log_message(message):
    print(Color.colored(f"[ MSG ] [ ITERATION {utils.iteration} ] {message}"))

