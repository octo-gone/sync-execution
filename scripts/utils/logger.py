import ctypes
from scripts.utils import utils
import os


# add color support for console
if os.name == 'nt':
    kernel32 = ctypes.WinDLL('kernel32')
    hStdOut = kernel32.GetStdHandle(-11)
    mode = ctypes.c_ulong()
    kernel32.GetConsoleMode(hStdOut, ctypes.byref(mode))
    mode.value |= 4
    kernel32.SetConsoleMode(hStdOut, mode)


class Color:
    """Simple class for wrapping console coloring."""

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
        """
        Function that changes foreground color
        by adding special sequences inside text.
        """
        if color in cls.colors:
            color = cls.colors[color]
        return "\33[38;5;" + str(color) + "m" + text + "\33[0m"

    @classmethod
    def background(cls, text, color):
        """
        Function that changes background color
        by adding special sequences inside text.
        """
        if color in cls.colors:
            color = cls.colors[color]
        return "\33[48;5;" + str(color) + "m" + text + "\33[0m"

    @classmethod
    def colored(cls, text, fg=None, bg=None):
        """
        Function that changes background and foreground color by adding
        special sequences inside text (using background and foreground functions).
        """
        if bg is not None:
            text = cls.background(text, bg)
        if fg is not None:
            text = cls.foreground(text, fg)
        return text

    @classmethod
    def colored_input(cls, prompt, fg="yellow", bg=None, fake=None):
        fg = "\33[38;5;" + str(cls.colors[fg]) + "m" if fg is not None else ""
        bg = "\33[48;5;" + str(cls.colors[bg]) + "m" if bg is not None else ""
        italic = "\33[3m"
        if fake is not None:
            print(prompt + fg + bg + italic + fake)
            value = fake
        else:
            value = input(prompt + fg + bg + italic)
        print("\33[0m", end="")
        return value


def log_error(message):
    """Prints information colored with red color (error)."""
    print(Color.colored(f"{utils.iteration}: {message}", fg="red"))
    input("Press ENTER to exit...")
    exit()


def log_warning(message):
    """Prints information colored with yellow color (warning)."""
    print(Color.colored(f"{utils.iteration}: {message}", fg="yellow"))


def log_success(message):
    """Prints information colored with green color (success)."""
    print(Color.colored(f"{utils.iteration}: {message}", fg="green"))


def log_message(message):
    """Prints information."""
    print(Color.colored(f"{utils.iteration}: {message}"))

