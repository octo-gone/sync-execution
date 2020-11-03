import math
from svgwrite import drawing
from scripts.utils.coder import to_shape, to_library


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


class NodeSVG:
    def __init__(self, **kwargs):

        self.inputs = kwargs.get("inputs", tuple())
        self.separated_inputs = []

        self.outputs = kwargs.get("outputs", tuple())
        self.separated_outputs = []

        self.desc = kwargs.get("desc", None)
        self.user_symbol = kwargs.get("user_symbol", None)

        self.ratio = (kwargs.get("width", 1), max(self.adjust_ratio(self.inputs), self.adjust_ratio(self.outputs)))
        if self.desc:
            self.ratio = (self.ratio[0], max(2, self.ratio[1]))

        self.label = kwargs.get("label", None)
        self.sync_name = kwargs.get("sync_name", self.label)
        self.time = kwargs.get("time", None)
        self.inner = kwargs.get("inner", None)

        self.inputs_label = kwargs.get("inputs_label", None)
        self.outputs_label = kwargs.get("outputs_label", None)

        self.icon = kwargs.get("icon", None)

        self.bg_color = "#%02x%02x%02x" % kwargs.get("bg_color", (255, 255, 255))
        self.border_color = "#%02x%02x%02x" % kwargs.get("border_color", (0, 0, 0))
        self.inputs_color = kwargs.get("inputs_color", ())
        self.outputs_color = kwargs.get("outputs_color", ())

        self.border_width = kwargs.get("border_width", 0.8)

        self.desc_size = kwargs.get("desc_size", 8)
        self.adds_size = kwargs.get("adds_size", 6)
        self.inner_size = kwargs.get("inner_size", 8)

        self.auto_inner_size = True

    @staticmethod
    def adjust_ratio(values):
        sep_values = [[]]
        sep_i = 0
        for value in values:
            if value not in ("sep",):
                sep_values[sep_i].append(value)
            else:
                sep_i += 1
                sep_values.append([])
        sum_height = 0
        for value in sep_values:
            height = 0
            for v in value:
                if v in SMALL + EMPTY:
                    height += 1 / 3
                if v in BIG:
                    height += 2 / 3
            height += 1 / 3
            sum_height += math.ceil(height)

        return sum_height

    def draw_node(self, path):

        side = 40
        stroke_width = self.border_width  # 0.4
        size = self.ratio[0] * side, self.ratio[1] * side

        file_path = f"{path}{self.label}.svg"
        draw = drawing.Drawing(file_path, size=size)

        draw.add(draw.rect(insert=(0, 0),
                           size=size,
                           stroke=self.border_color,
                           stroke_width=0.5,
                           fill=self.bg_color))
        r = 1 / 6

        def draw_connectors(inout, orientation, connectors_color):
            label_centers = []
            node_connectors = []
            if len(inout):
                sep_connectors = [[]]
                sep_i = 0
                for value in inout:
                    if value not in SEPARATORS:
                        sep_connectors[sep_i].append(value)
                    else:
                        sep_i += 1
                        sep_connectors.append([])
                last_height = 0
                actual_counter = 0
                for _, value in enumerate(sep_connectors):
                    height = 0
                    for v in value:
                        if v in SMALL + EMPTY:
                            height += 1 / 3
                        if v in BIG:
                            height += 2 / 3
                    height += 1 / 3
                    offset = (math.ceil(height) - height) / 2
                    height = last_height
                    for v in value:
                        height += 1 / 3
                        if connectors_color:
                            color = colors[connectors_color[actual_counter]]
                            color = "#%02x%02x%02x" % color
                        elif v not in EMPTY:
                            color = colors[v]
                            color = "#%02x%02x%02x" % color
                        else:
                            color = self.bg_color

                        if v in BIG + TRIANGLE + SQUARE + CUT_SQUARE:
                            if v in RECTANGLE:
                                if orientation:
                                    points = ((0, (offset + height - r) * side),
                                              (r * side, (offset + height - r) * side),
                                              (r * side, (offset + height + 3 * r) * side),
                                              (0, (offset + height + 3 * r) * side),
                                              (0, (offset + height - r) * side))
                                else:
                                    points = ((size[0], (offset + height - r) * side),
                                              (size[0] - r * side, (offset + height - r) * side),
                                              (size[0] - r * side, (offset + height + 3 * r) * side),
                                              (size[0], (offset + height + 3 * r) * side),
                                              (size[0], (offset + height - r) * side))
                            elif v in SQUARE:
                                if orientation:
                                    points = ((0, (offset + height - r) * side),
                                              (r * side, (offset + height - r) * side),
                                              (r * side, (offset + height + r) * side),
                                              (0, (offset + height + r) * side),
                                              (0, (offset + height - r) * side))
                                else:
                                    points = ((size[0], (offset + height - r) * side),
                                              (size[0] - r * side, (offset + height - r) * side),
                                              (size[0] - r * side, (offset + height + r) * side),
                                              (size[0], (offset + height + r) * side),
                                              (size[0], (offset + height - r) * side))
                            elif v in CUT_RECTANGLE:
                                if orientation:
                                    points = ((0, (offset + height - r) * side),
                                              (r * side, (offset + height + 3 * r) * side),
                                              (0, (offset + height + 3 * r) * side),
                                              (0, (offset + height - r) * side))
                                else:
                                    points = ((size[0], (offset + height - r) * side),
                                              (size[0] - r * side, (offset + height + 3 * r) * side),
                                              (size[0], (offset + height + 3 * r) * side),
                                              (size[0], (offset + height - r) * side))
                            elif v in CUT_SQUARE:
                                if orientation:
                                    points = ((0, (offset + height - r) * side),
                                              (r * side, (offset + height + r) * side),
                                              (0, (offset + height + r) * side),
                                              (0, (offset + height - r) * side))
                                else:
                                    points = ((size[0], (offset + height - r) * side),
                                              (size[0] - r * side, (offset + height + r) * side),
                                              (size[0], (offset + height + r) * side),
                                              (size[0], (offset + height - r) * side))
                            else:
                                if orientation:
                                    points = ((0, (offset + height - r) * side),
                                              (r * side, (offset + height) * side),
                                              (0, (offset + height + r) * side),
                                              (0, (offset + height - r) * side))
                                else:
                                    points = ((size[0], (offset + height - r) * side),
                                              (size[0] - r * side, (offset + height) * side),
                                              (size[0], (offset + height + r) * side),
                                              (size[0], (offset + height - r) * side))
                            draw.add(draw.polygon(points,
                                                  fill=color,
                                                  stroke="black",
                                                  stroke_width=stroke_width))

                            if v in BIG:
                                if v in RECTANGLE:
                                    node_connectors += [offset + height + r * (ic / 2) for ic in range(-1, 6)]
                                elif v in CUT_RECTANGLE:
                                    node_connectors += [offset + height + r * (ic / 2) for ic in range(1, 6)]
                                height += 1 / 3
                            else:
                                node_connectors.append(offset + height)

                        if v in ROUND:
                            radius = r * side
                            if orientation:
                                center = (0, (offset + height) * side)
                                points = ((center[0], center[1] - radius),
                                          (center[0], center[1] + radius))
                            else:
                                center = (size[0], (offset + height) * side)
                                points = ((center[0], center[1] + radius),
                                          (center[0], center[1] - radius))
                            svg_path = f"M {points[0][0]} {points[0][1]} A {radius} {radius} " \
                                       f"0 0 1 {points[1][0]} {points[1][1]}"
                            draw.add(draw.path(d=svg_path,
                                               fill=color,
                                               stroke=self.border_color,
                                               stroke_width=stroke_width))
                            node_connectors.append(offset + height)

                        if v not in EMPTY:
                            label_centers.append((offset + height))
                            actual_counter += 1
                    height += 0.3
                    last_height = math.ceil(height)
            return label_centers, node_connectors

        inputs_label_centers, input_connectors = draw_connectors(self.inputs, True, self.inputs_color)
        outputs_label_centers, output_connectors = draw_connectors(self.outputs, False, self.outputs_color)

        inner = self.inner.split("\n")
        if len(inner) == 2:
            if (len(inner[0]) > 5 or len(inner[1]) > 5) and self.auto_inner_size:
                self.inner_size -= max(len(inner[0]), len(inner[1])) - 5

            draw.add(draw.text(inner[0],
                               insert=(20 * self.ratio[0], 19),
                               text_anchor="middle",
                               style=f"font-size:{self.inner_size}px;font-family:Courier;font-weight:bold;"))
            draw.add(draw.text(inner[1],
                               insert=(20 * self.ratio[0], 25),
                               text_anchor="middle",
                               style=f"font-size:{self.inner_size}px;font-family:Courier;font-weight:bold;"))
        else:
            if len(inner[0]) > 5 and self.auto_inner_size:
                self.inner_size -= len(inner[0]) - 5

            draw.add(draw.text(inner[0],
                               insert=(20 * self.ratio[0], 22),
                               text_anchor="middle",
                               style=f"font-size:{self.inner_size}px;font-family:Courier;font-weight:bold;"))

        if self.desc:
            draw.add(draw.text(self.desc,
                               insert=(20 * self.ratio[0], 62),
                               text_anchor="middle",
                               style=f"font-size:{self.desc_size}px;font-family:Courier;font-weight:bold;"))

        if self.user_symbol:
            draw.add(draw.text(self.user_symbol[0],
                               insert=(side * self.ratio[0] - 3, 6),
                               text_anchor="middle",
                               style=f"font-size:{self.adds_size}px;font-family:Courier;font-weight:bold;"))

        if self.time:
            draw.add(draw.text(self.time,
                               insert=(side * self.ratio[0] - 2, side * self.ratio[1] - 2),
                               text_anchor="end",
                               style=f"font-size:{self.adds_size}px;font-family:Courier;font-weight:bold;"))

        draw.add(draw.rect(insert=(0, 0),
                           size=size,
                           stroke=self.border_color,
                           stroke_width=2 * stroke_width,
                           fill="none"))

        connectors = []
        for i in input_connectors:
            connectors.append([0, i / self.ratio[1]])
        for i in output_connectors:
            connectors.append([1, i / self.ratio[1]])
        points_style = f"points={connectors};"
        style = "verticalLabelPosition=top;labelBackgroundColor=none;verticalAlign=bottom;aspect=fixed;" \
                "imageAspect=0;fontFamily=Courier;fontSize=8;labelPosition=center;align=center;spacing=-1;" \
                f"fontStyle=1;syncNodeName={self.sync_name};"
        draw.save()

        with open(file_path, "r") as xml:
            encoded_svg = to_shape(xml.read())
        shape = f"""<mxGraphModel><root><mxCell id="0"/><mxCell id="1" parent="0"/><mxCell id="2" value="" style="shape=image;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;aspect=fixed;imageAspect=0;image=data:image/svg+xml,{encoded_svg};{points_style+style}" vertex="1" parent="1"><mxGeometry width="{size[0]}" height="{size[1]}" as="geometry"/></mxCell></root></mxGraphModel>"""
        encoded_shape = to_library(shape).decode("utf-8")
        drawio_node_json = {
            "xml": encoded_shape,
            "w": size[0],
            "h": size[1],
            "aspect": "fixed",
            "title": self.label.title()
        }

        return drawio_node_json, file_path, points_style+style


class NodeFunctionSVG:
    def __init__(self, **kwargs):
        self.node = NodeSVG(**kwargs)
        output_node_kwargs = dict(tuple(kwargs.items()))
        output_node_kwargs["outputs"] = ("ctrl",)
        output_node_kwargs["outputs_label"] = ("ctrl",)
        output_node_kwargs["outputs_color"] = ()
        output_node_kwargs["inputs"] = self.node.outputs
        output_node_kwargs["inputs_label"] = self.node.outputs_label
        output_node_kwargs["inputs_color"] = self.node.outputs_color
        output_node_kwargs["desc"] = "out"
        output_node_kwargs["label"] = f"function output {output_node_kwargs['label']}"

        input_node_kwargs = dict(tuple(kwargs.items()))
        input_node_kwargs["inputs"] = ("ctrl",)
        input_node_kwargs["inputs_label"] = ("ctrl",)
        input_node_kwargs["inputs_color"] = ()
        input_node_kwargs["outputs"] = self.node.inputs
        input_node_kwargs["outputs_label"] = self.node.inputs_label
        input_node_kwargs["outputs_color"] = self.node.inputs_color
        input_node_kwargs["desc"] = "in"
        input_node_kwargs["label"] = f"function input {input_node_kwargs['label']}"

        self.node.label = f"function {kwargs['label']}"
        self.node.sync_name = f"function {kwargs['label']}"
        self.input_node = NodeSVG(**input_node_kwargs)
        self.output_node = NodeSVG(**output_node_kwargs)

    def draw_node(self, path):
        a = self.node.draw_node(path)
        b = self.input_node.draw_node(path)
        c = self.output_node.draw_node(path)
        return a, b, c
