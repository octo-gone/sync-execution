import math
from svgwrite import drawing


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

small_connectors = ("int", "real", "obj", "char", "ctrl", "bool", "any", "number", "mult_s", "dir_mult_s")
triangle_connectors = ("int", "real", "ctrl", "bool", "any", "number")
round_connectors = ("obj", "char")
big_connectors = ("mult", "dir_mult")
rectangle_connectors = ("mult",)
cut_rectangle_connectors = ("dir_mult",)
separators = ("sep",)
empty_connectors = ("empty",)

square_connectors = ("mult_s", )
cut_square_connectors = ("dir_mult_s", )


class NodeSVG:
    colors = colors
    small_connectors = small_connectors
    triangle_connectors = triangle_connectors
    round_connectors = round_connectors
    big_connectors = big_connectors
    rectangle_connectors = rectangle_connectors
    cut_rectangle_connectors = cut_rectangle_connectors
    separators = separators
    empty_connectors = empty_connectors

    square_connectors = square_connectors
    cut_square_connectors = cut_square_connectors

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

        self.border_width = kwargs.get("border_width", 10)

        self.label_size = kwargs.get("label_size", 40)
        self.time_size = kwargs.get("description_size", 30)
        self.inner_size = kwargs.get("inner_size", 70)

    def adjust_ratio(self, values):
        sep_values = [[]]
        sep_i = 0
        for value in values:
            if value not in ("sep", ):
                sep_values[sep_i].append(value)
            else:
                sep_i += 1
                sep_values.append([])
        sum_height = 0
        for value in sep_values:
            height = 0
            for v in value:
                if v in self.small_connectors + self.empty_connectors:
                    height += 1/3
                if v in self.big_connectors:
                    height += 2/3
            height += 1/3
            sum_height += math.ceil(height)

        return sum_height

    def draw_node(self, path):

        side = 40
        stroke_width = 0.8  # 0.4
        size = self.ratio[0]*side, self.ratio[1]*side

        file_path = f"{path}{self.label}.svg"
        draw = drawing.Drawing(file_path, size=size)

        draw.add(draw.rect(insert=(0, 0), size=size, stroke=self.border_color, stroke_width=0.5, fill=self.bg_color))
        r = 1 / 6

        def draw_connectors(inout, orientation, connectors_color):
            label_centers = []
            node_connectors = []
            if len(inout):
                sep_connectors = [[]]
                sep_i = 0
                for value in inout:
                    if value not in self.separators:
                        sep_connectors[sep_i].append(value)
                    else:
                        sep_i += 1
                        sep_connectors.append([])
                last_height = 0
                actual_counter = 0
                for _, value in enumerate(sep_connectors):
                    height = 0
                    for v in value:
                        if v in self.small_connectors + self.empty_connectors:
                            height += 1 / 3
                        if v in self.big_connectors:
                            height += 2 / 3
                    height += 1 / 3
                    offset = (math.ceil(height) - height)/2
                    height = last_height
                    for v in value:
                        height += 1 / 3
                        if connectors_color:
                            color = self.colors[connectors_color[actual_counter]]
                            color = "#%02x%02x%02x" % color
                        elif v not in self.empty_connectors:
                            color = self.colors[v]
                            color = "#%02x%02x%02x" % color
                        else:
                            color = self.bg_color

                        if v in self.big_connectors + self.triangle_connectors + \
                                self.square_connectors + self.cut_square_connectors:
                            if v in self.rectangle_connectors:
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
                            elif v in self.square_connectors:
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
                            elif v in self.cut_rectangle_connectors:
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
                            elif v in self.cut_square_connectors:
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
                                              (r*side, (offset+height)*side),
                                              (0, (offset+height+r)*side),
                                              (0, (offset+height-r)*side))
                                else:
                                    points = ((size[0], (offset + height - r) * side),
                                              (size[0]-r*side, (offset+height)*side),
                                              (size[0], (offset+height+r)*side),
                                              (size[0], (offset+height-r)*side))
                            draw.add(draw.polygon(points, fill=color, stroke="black", stroke_width=stroke_width))

                            if v in self.big_connectors:
                                if v in self.rectangle_connectors:
                                    node_connectors += [offset + height + r * (ic / 2) for ic in range(-1, 6)]
                                elif v in self.cut_rectangle_connectors:
                                    node_connectors += [offset + height + r * (ic / 2) for ic in range(1, 6)]
                                height += 1 / 3
                            else:
                                node_connectors.append(offset + height)

                        if v in self.round_connectors:
                            radius = r * side
                            if orientation:
                                center = (0, (offset + height) * side)
                                points = ((center[0], center[1] - radius),
                                          (center[0], center[1] + radius))
                            else:
                                center = (size[0], (offset + height) * side)
                                points = ((center[0], center[1] + radius),
                                          (center[0], center[1] - radius))
                            path = f"M {points[0][0]} {points[0][1]} A {radius} {radius} " \
                                   f"0 0 1 {points[1][0]} {points[1][1]}"
                            draw.add(draw.path(d=path, fill=color, stroke=self.border_color, stroke_width=stroke_width))
                            node_connectors.append(offset + height)

                        if v not in self.empty_connectors:
                            label_centers.append((offset + height))
                            actual_counter += 1
                    height += 0.3
                    last_height = math.ceil(height)
            return label_centers, node_connectors

        inputs_label_centers, input_connectors = draw_connectors(self.inputs, True, self.inputs_color)
        outputs_label_centers, output_connectors = draw_connectors(self.outputs, False, self.outputs_color)
        inner_text = draw.text(self.inner, insert=(20, 22), text_anchor="middle",
                               style="font-size:8px; font-family:Courier;font-weight:bold;")
        draw.add(inner_text)

        if self.desc:
            desc_text = draw.text(self.desc, insert=(20, 62), text_anchor="middle",
                                  style="font-size:8px; font-family:Courier;font-weight:bold;")
            draw.add(desc_text)

        if self.user_symbol:
            desc_text = draw.text(self.user_symbol[0], insert=(side*self.ratio[0]-3, 6), text_anchor="middle",
                                  style="font-size:6px; font-family:Courier;font-weight:bold;")
            draw.add(desc_text)

        if self.time:
            desc_text = draw.text(self.time, insert=(side*self.ratio[0]-2, side*self.ratio[1]-2),
                                  text_anchor="end", style="font-size:6px; font-family:Courier;font-weight:bold;")
            draw.add(desc_text)

        draw.add(draw.rect(insert=(0, 0), size=size, stroke=self.border_color,
                           stroke_width=2*stroke_width, fill="none"))

        connectors = []
        for i in input_connectors:
            connectors.append([0, i/self.ratio[1]])
        for i in output_connectors:
            connectors.append([1, i/self.ratio[1]])
        points_style = f"points={connectors};"
        style = "verticalLabelPosition=top;labelBackgroundColor=none;verticalAlign=bottom;aspect=fixed;" \
                "imageAspect=0;fontFamily=Courier;fontSize=8;labelPosition=center;align=center;spacing=-1;" \
                f"fontStyle=1;syncNodeName={self.sync_name};"
        draw.save()
        return file_path, points_style + style


class NodeFunctionSVG:
    def __init__(self, **kwargs):
        self.node = NodeSVG(**kwargs)
        output_node_kwargs = dict(tuple(kwargs.items()))
        output_node_kwargs["outputs"] = ("ctrl", )
        output_node_kwargs["outputs_label"] = ("ctrl", )
        output_node_kwargs["outputs_color"] = ()
        output_node_kwargs["inputs"] = self.node.outputs
        output_node_kwargs["inputs_label"] = self.node.outputs_label
        output_node_kwargs["inputs_color"] = self.node.outputs_color
        output_node_kwargs["desc"] = "out"
        output_node_kwargs["label"] = f"function output {output_node_kwargs['label']}"

        input_node_kwargs = dict(tuple(kwargs.items()))
        input_node_kwargs["inputs"] = ("ctrl", )
        input_node_kwargs["inputs_label"] = ("ctrl", )
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
