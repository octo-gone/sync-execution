import ctypes
from scripts.utils import utils
from scripts.config import config
import os

show_iteration = config.get("Console", "show_iteration") == "yes"
show_additional_info = config.get("Console", "show_additional_info") == "yes"
colored = config.get("Console", "colored_console") == "yes"
show_warning = config.get("Console", "show_warning") == "yes"

# add color support for console
if os.name == 'nt' and colored:
    kernel32 = ctypes.WinDLL('kernel32')
    hStdOut = kernel32.GetStdHandle(-11)
    mode = ctypes.c_ulong()
    kernel32.GetConsoleMode(hStdOut, ctypes.byref(mode))
    mode.value |= 4
    kernel32.SetConsoleMode(hStdOut, mode)


class Color:
    """Simple class for wrapping console coloring."""

    input_color = "yellow"
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
    def colored_input(cls, prompt, fg="yellow", bg=None, value=None):

        if show_iteration:
            prompt = f"{utils.iteration}: " + prompt
        if colored:
            fg = "\33[38;5;" + str(cls.colors[fg]) + "m" if fg is not None else ""
            bg = "\33[48;5;" + str(cls.colors[bg]) + "m" if bg is not None else ""
            italic = "\33[3m"
            if value is not None:
                print(prompt + fg + bg + italic + value)
                value = value
            else:
                value = input(prompt + fg + bg + italic)
            print("\33[0m", end="")
        else:
            if value is not None:
                print(prompt + value)
            else:
                value = input(prompt)
        return value


def log_error(message):
    """Prints information colored with red color (error)."""
    message = f"{message}"
    if show_iteration:
        message = f"{utils.iteration}: " + message
    if colored:
        print(Color.colored(message, fg="red"))
    else:
        print(message)
    input("Press ENTER to exit...")
    quit()


def log_warning(message):
    """Prints information colored with yellow color (warning)."""
    message = f"{message}"
    if show_warning:
        if show_iteration:
            message = f"{utils.iteration}: " + message
        if colored:
            print(Color.colored(message, fg="yellow"))
        else:
            print(message)


def log_success(message):
    """Prints information colored with green color (success)."""
    message = f"{message}"
    if show_additional_info:
        if show_iteration:
            message = f"{utils.iteration}: " + message
        if colored:
            print(Color.colored(message, fg="green"))
        else:
            print(message)


def log_message(message):
    """Prints information."""
    message = f"{message}"
    if show_iteration:
        message = f"{utils.iteration}: " + message
    if colored:
        print(Color.colored(message))
    else:
        print(message)
