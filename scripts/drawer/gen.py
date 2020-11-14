import math
from svgwrite import drawing
import os
from scripts.utils.coder import to_shape, to_library
from scripts.drawer.config import *
import textwrap
import html


def generate_tooltip(tooltip, is_function=False):
    def add_label(label, wrap):
        return f"<b>{textwrap.fill(label, width=wrap)}</b>"

    def add_io_element(io_name, io_desc, wrap):
        return f"<b style='padding-left:15px;' >{io_name}:</b> {textwrap.fill(io_desc, width=wrap)}"

    def add_desc(desc, wrap):
        return f"<span style='padding-left:15px'> {textwrap.fill(desc, width=wrap)}</span>"

    def add_input_label():
        return f"<b style='color:darkgreen'>Входы:</b>"

    def add_output_label():
        return f"<b style='color:darkred'>Выходы:</b>"

    def add_adds(adds, wrap):
        if is_function:
            if adds.strip().endswith('.'):
                adds = adds.strip() + " " + TOOLTIP_ADDS_FUNCTION
            else:
                adds = adds.strip() + ". " + TOOLTIP_ADDS_FUNCTION
        text = textwrap.fill(adds, width=wrap)
        color = "#%02x%02x%02x" % TOOLTIP_KEYWORDS_COLOR
        for keyword in TOOLTIP_KEYWORDS:
            text = f"<span style='color:{color}'>{keyword}</span>".join(text.split(keyword))
        return f"\n<i style='color:#333'>{text}</i>"

    tooltip_html = []

    label = tooltip.get('label')
    desc = tooltip.get('desc')
    adds = tooltip.get('adds')
    inputs = tooltip.get('inputs')
    outputs = tooltip.get('outputs')
    word_wrap = tooltip.get('word_wrap', TOOLTIP_WRAP_LENGTH)

    tooltip_html.append(add_label(label, word_wrap))
    if desc:
        tooltip_html.append(add_desc(desc, word_wrap))
    if inputs:
        tooltip_html.append(add_input_label())
        for i, iv in enumerate(inputs):
            tooltip_html.append(add_io_element(i+1, iv[1], word_wrap))
    if outputs:
        tooltip_html.append(add_output_label())
        for i, iv in enumerate(outputs):
            tooltip_html.append(add_io_element(i+1, iv[1], word_wrap))
    if adds:
        tooltip_html.append(add_adds(adds, word_wrap))
    a = "\n".join(map(html.escape, tooltip_html))
    b = html.escape("<span style='font-size:medium;font-family:Courier'>") + a + html.escape("</span>")
    return "&#xA;".join(b.split('\n'))


class NodeSVG:
    def __init__(self, is_function=False, **kwargs):
        self.is_function = is_function

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

        self.bg_color = "#%02x%02x%02x" % kwargs.get("bg_color", NODE_BACKGROUND_COLOR)
        self.border_color = "#%02x%02x%02x" % kwargs.get("border_color", NODE_BORDER_COLOR)
        self.inputs_color = kwargs.get("inputs_color", ())
        self.outputs_color = kwargs.get("outputs_color", ())

        self.border_width = kwargs.get("border_width", NODE_BORDER_WIDTH)

        self.desc_size = kwargs.get("desc_size", NODE_DESC_FONTSIZE)
        self.adds_size = kwargs.get("adds_size", NODE_ADDS_FONTSIZE)
        self.inner_size = kwargs.get("inner_size", NODE_INNER_FONTSIZE)

        self.side = NODE_SIZE

        self.tooltip = kwargs.get("tooltip", None)

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

        try:
            os.makedirs(path)
        except FileExistsError:
            pass

        size = self.ratio[0] * self.side, self.ratio[1] * self.side

        file_path = f"{path}{self.sync_name}.svg"
        draw = drawing.Drawing(file_path, size=size)

        draw.add(draw.rect(insert=(0, 0),
                           size=size,
                           fill=self.bg_color))

        inputs_label_centers, input_connectors = self.draw_connectors(draw, self.inputs, True, self.inputs_color)
        outputs_label_centers, output_connectors = self.draw_connectors(draw, self.outputs, False, self.outputs_color)

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
                               insert=(self.side * self.ratio[0] - 3, 6),
                               text_anchor="middle",
                               style=f"font-size:{self.adds_size}px;font-family:Courier;font-weight:bold;"))

        if self.time:
            draw.add(draw.text(self.time,
                               insert=(self.side * self.ratio[0] - 2, self.side * self.ratio[1] - 2),
                               text_anchor="end",
                               style=f"font-size:{self.adds_size}px;font-family:Courier;font-weight:bold;"))

        draw.add(draw.rect(insert=(0, 0),
                           size=size,
                           stroke=self.border_color,
                           stroke_width=2 * self.border_width,
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
        if self.is_function:
            style += f"syncInputs={list(self.inputs)};syncOutputs={list(self.outputs)};"
        draw.save()

        with open(file_path, "r") as xml:
            encoded_svg = to_shape(xml.read())

        if self.tooltip:
            tooltip = generate_tooltip(self.tooltip, self.is_function)
            shape = f"""<mxGraphModel><root><mxCell id="0"/><mxCell id="1" parent="0"/><UserObject label="" tooltip="{tooltip}" id="2"><mxCell style="shape=image;image=data:image/svg+xml,{encoded_svg};{points_style+style}" vertex="1" parent="1"><mxGeometry width="{size[0]}" height="{size[1]}" as="geometry"/></mxCell></UserObject></root></mxGraphModel>"""
        else:
            shape = f"""<mxGraphModel><root><mxCell id="0"/><mxCell id="1" parent="0"/><mxCell id="2" value="" style="shape=image;image=data:image/svg+xml,{encoded_svg};{points_style+style}" vertex="1" parent="1"><mxGeometry width="{size[0]}" height="{size[1]}" as="geometry"/></mxCell></root></mxGraphModel>"""
        encoded_shape = to_library(shape).decode("utf-8")
        drawio_node_json = {
            "xml": encoded_shape,
            "w": size[0],
            "h": size[1],
            "aspect": "fixed",
            "title": self.label.title()
        }

        return drawio_node_json, file_path, points_style+style

    def draw_connectors(self, draw, inout, orientation, connectors_color):
        size = self.ratio[0] * self.side, self.ratio[1] * self.side
        r = 1 / 6
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
                                points = ((0, (offset + height - r) * self.side),
                                          (r * self.side, (offset + height - r) * self.side),
                                          (r * self.side, (offset + height + 3 * r) * self.side),
                                          (0, (offset + height + 3 * r) * self.side),
                                          (0, (offset + height - r) * self.side))
                            else:
                                points = ((size[0], (offset + height - r) * self.side),
                                          (size[0] - r * self.side, (offset + height - r) * self.side),
                                          (size[0] - r * self.side, (offset + height + 3 * r) * self.side),
                                          (size[0], (offset + height + 3 * r) * self.side),
                                          (size[0], (offset + height - r) * self.side))
                        elif v in SQUARE:
                            if orientation:
                                points = ((0, (offset + height - r) * self.side),
                                          (r * self.side, (offset + height - r) * self.side),
                                          (r * self.side, (offset + height + r) * self.side),
                                          (0, (offset + height + r) * self.side),
                                          (0, (offset + height - r) * self.side))
                            else:
                                points = ((size[0], (offset + height - r) * self.side),
                                          (size[0] - r * self.side, (offset + height - r) * self.side),
                                          (size[0] - r * self.side, (offset + height + r) * self.side),
                                          (size[0], (offset + height + r) * self.side),
                                          (size[0], (offset + height - r) * self.side))
                        elif v in CUT_RECTANGLE:
                            if orientation:
                                points = ((0, (offset + height - r) * self.side),
                                          (r * self.side, (offset + height + 3 * r) * self.side),
                                          (0, (offset + height + 3 * r) * self.side),
                                          (0, (offset + height - r) * self.side))
                            else:
                                points = ((size[0], (offset + height - r) * self.side),
                                          (size[0] - r * self.side, (offset + height + 3 * r) * self.side),
                                          (size[0], (offset + height + 3 * r) * self.side),
                                          (size[0], (offset + height - r) * self.side))
                        elif v in CUT_SQUARE:
                            if orientation:
                                points = ((0, (offset + height - r) * self.side),
                                          (r * self.side, (offset + height + r) * self.side),
                                          (0, (offset + height + r) * self.side),
                                          (0, (offset + height - r) * self.side))
                            else:
                                points = ((size[0], (offset + height - r) * self.side),
                                          (size[0] - r * self.side, (offset + height + r) * self.side),
                                          (size[0], (offset + height + r) * self.side),
                                          (size[0], (offset + height - r) * self.side))
                        else:
                            if orientation:
                                points = ((0, (offset + height - r) * self.side),
                                          (r * self.side, (offset + height) * self.side),
                                          (0, (offset + height + r) * self.side),
                                          (0, (offset + height - r) * self.side))
                            else:
                                points = ((size[0], (offset + height - r) * self.side),
                                          (size[0] - r * self.side, (offset + height) * self.side),
                                          (size[0], (offset + height + r) * self.side),
                                          (size[0], (offset + height - r) * self.side))
                        draw.add(draw.polygon(points,
                                              fill=color,
                                              stroke="black",
                                              stroke_width=self.border_width))

                        if v in BIG:
                            if v in RECTANGLE:
                                node_connectors += [offset + height + r * (ic / 2) for ic in range(-1, 6)]
                            elif v in CUT_RECTANGLE:
                                node_connectors += [offset + height + r * (ic / 2) for ic in range(1, 6)]
                            height += 1 / 3
                        else:
                            node_connectors.append(offset + height)

                    if v in ROUND:
                        radius = r * self.side
                        if orientation:
                            center = (0, (offset + height) * self.side)
                            points = ((center[0], center[1] - radius),
                                      (center[0], center[1] + radius))
                        else:
                            center = (size[0], (offset + height) * self.side)
                            points = ((center[0], center[1] + radius),
                                      (center[0], center[1] - radius))
                        svg_path = f"M {points[0][0]} {points[0][1]} A {radius} {radius} " \
                                   f"0 0 1 {points[1][0]} {points[1][1]}"
                        draw.add(draw.path(d=svg_path,
                                           fill=color,
                                           stroke=self.border_color,
                                           stroke_width=self.border_width))
                        node_connectors.append(offset + height)

                    if v not in EMPTY:
                        label_centers.append((offset + height))
                        actual_counter += 1
                height += 0.3
                last_height = math.ceil(height)
        return label_centers, node_connectors


class NodeFunctionSVG:
    def __init__(self, **kwargs):
        self.node = NodeSVG(**kwargs, is_function=True)
        output_node_kwargs = dict(tuple(kwargs.items()))
        output_node_kwargs["outputs"] = ()
        output_node_kwargs["outputs_label"] = ()
        output_node_kwargs["outputs_color"] = ()
        output_node_kwargs["inputs"] = self.node.outputs
        output_node_kwargs["inputs_label"] = self.node.outputs_label
        output_node_kwargs["inputs_color"] = self.node.outputs_color
        output_node_kwargs["desc"] = "out"
        output_node_kwargs["label"] = f"function output {output_node_kwargs['label']}"
        output_node_kwargs["sync_name"] = output_node_kwargs["label"]

        input_node_kwargs = dict(tuple(kwargs.items()))
        input_node_kwargs["inputs"] = ()
        input_node_kwargs["inputs_label"] = ()
        input_node_kwargs["inputs_color"] = ()
        input_node_kwargs["outputs"] = self.node.inputs
        input_node_kwargs["outputs_label"] = self.node.inputs_label
        input_node_kwargs["outputs_color"] = self.node.inputs_color
        input_node_kwargs["desc"] = "in"
        input_node_kwargs["label"] = f"function input {input_node_kwargs['label']}"
        input_node_kwargs["sync_name"] = input_node_kwargs["label"]

        self.node.label = f"function {kwargs['label']}"
        self.node.sync_name = f"function {kwargs['label']}"
        self.input_node = NodeSVG(**input_node_kwargs, is_function=True)
        self.output_node = NodeSVG(**output_node_kwargs, is_function=True)

    def draw_node(self, path):
        a = self.node.draw_node(path)
        b = self.input_node.draw_node(path)
        c = self.output_node.draw_node(path)
        return a, b, c
