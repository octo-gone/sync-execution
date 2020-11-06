colors = {
    "number": (136, 209, 201),
    "real": (163, 211, 156),
    "int": (109, 207, 246),
    "char": (255, 247, 153),
    "ctrl": (196, 113, 121),
    "obj": (246, 150, 121),
    "bool": (161, 134, 190),
    "mult": (191, 191, 191),
    "dir_mult": (191, 191, 191),
    "any": (191, 191, 191),
    "mult_s": (191, 191, 191),
    "dir_mult_s": (191, 191, 191),
    "empty": (0, 0, 0)
}

SMALL = ("int", "real", "obj", "char", "ctrl", "bool", "any", "number", "mult_s", "dir_mult_s")
BIG = ("mult", "dir_mult")

TRIANGLE = ("int", "real", "ctrl", "bool", "any", "number")
ROUND = ("obj", "char")
RECTANGLE = ("mult",)
CUT_RECTANGLE = ("dir_mult",)
SEPARATORS = ("sep",)
EMPTY = ("empty",)
SQUARE = ("mult_s",)
CUT_SQUARE = ("dir_mult_s",)

NODE_BACKGROUND_COLOR = (255, 255, 255)
NODE_BORDER_COLOR = (0, 0, 0)
NODE_BORDER_WIDTH = 0.8

NODE_DESC_FONTSIZE = 8
NODE_ADDS_FONTSIZE = 6
NODE_INNER_FONTSIZE = 8

NODE_SIZE = 40

TOOLTIP_WRAP_LENGTH = 30
TOOLTIP_KEYWORDS = ["$iteration", "$min", "$max", "$pi", "$true", "$false", "$none", "$sep", "$int", "$real", "$bool",
                    "$char", "$num", "$str", "$any"]
TOOLTIP_KEYWORDS_COLOR = (147, 107, 9)
