import math
import os
from scripts.utils.coder import to_shape, to_library
from scripts.drawer.config import *
from scripts.constants import *
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

    def add_adds(a, wrap):
        if is_function:
            if a.strip().endswith('.'):
                a = a.strip() + " " + TOOLTIP_ADDS_FUNCTION
            else:
                a = a.strip() + ". " + TOOLTIP_ADDS_FUNCTION
        text = textwrap.fill(a, width=wrap)
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
            tooltip_html.append(add_io_element(i + 1, iv[1], word_wrap))
    if outputs:
        tooltip_html.append(add_output_label())
        for i, iv in enumerate(outputs):
            tooltip_html.append(add_io_element(i + 1, iv[1], word_wrap))
    if adds:
        tooltip_html.append(add_adds(adds, word_wrap))
    tooltip = "\n".join(map(html.escape, tooltip_html))
    escaped = html.escape("<span style='font-size:medium;font-family:Courier'>") + tooltip + html.escape("</span>")
    return "&#xA;".join(escaped.split('\n'))


def adjust_ratio(values):
    sep_values = [[]]
    sep_i = 0
    for v in values:
        if v[0] != SEPARATOR:
            sep_values[sep_i].append(v)
        else:
            sep_i += 1
            sep_values.append([])

    sum_height = 0
    for value in sep_values:
        height = 0
        for variant, *v in value:
            if variant == SINGLE or SMALL in v:
                height += 1 / 3
            else:
                height += 2 / 3
        height += 1 / 3
        sum_height += math.ceil(height)

    return sum_height


class NodeSVG:
    def __init__(self, is_function=False, **kwargs):
        self.is_function = is_function

        self.inputs = kwargs.get("inputs", tuple())
        self.separated_inputs = []

        self.outputs = kwargs.get("outputs", tuple())
        self.separated_outputs = []

        self.desc = kwargs.get("desc", None)
        self.user_symbol = kwargs.get("user_symbol", None)

        self.ratio = (kwargs.get("width", 1), max(adjust_ratio(self.inputs), adjust_ratio(self.outputs)))
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

    def draw_node(self, path):

        try:
            os.makedirs(path)
        except FileExistsError:
            pass

        size = self.ratio[0] * self.side, self.ratio[1] * self.side

        file_path = f"{path}{self.sync_name}.svg"

        svg = '<?xml version="1.0" encoding="utf-8" ?>' \
              f'<svg baseProfile="full" height="{size[1]}" version="1.1" width="{size[0]}" ' \
              'xmlns="http://www.w3.org/2000/svg" xmlns:ev="http://www.w3.org/2001/xml-events" ' \
              'xmlns:xlink="http://www.w3.org/1999/xlink"><defs/>'

        svg += f'<rect fill="{self.bg_color}" height="100%" width="100%" x="0" y="0"/>'

        s1, inputs_label_centers, input_connectors = self.draw_connectors(self.inputs, True)
        s2, outputs_label_centers, output_connectors = self.draw_connectors(self.outputs, False)

        svg += s1 + s2

        inner = self.inner.split("\n")
        if len(inner) == 2:
            if (len(inner[0]) > 5 or len(inner[1]) > 5) and self.auto_inner_size:
                self.inner_size -= max(len(inner[0]), len(inner[1])) - 5

            svg += f'<text font-weight="bold" font-size="{self.inner_size}px" font-family="Courier" ' \
                   f'text-anchor="middle" x="{20 * self.ratio[0]}" y="{19}">{inner[0]}</text>'
            svg += f'<text font-weight="bold" font-size="{self.inner_size}px" font-family="Courier" ' \
                   f'text-anchor="middle" x="{20 * self.ratio[0]}" y="{25}">{inner[1]}</text>'
        else:
            if len(inner[0]) > 5 and self.auto_inner_size:
                self.inner_size -= len(inner[0]) - 5
            svg += f'<text font-weight="bold" font-size="{self.inner_size}px" font-family="Courier" ' \
                   f'text-anchor="middle" x="{20 * self.ratio[0]}" y="{22}">{inner[0]}</text>'

        if self.desc:
            svg += f'<text font-weight="bold" font-size="{self.desc_size}px" font-family="Courier" ' \
                   f'text-anchor="middle" x="{20 * self.ratio[0]}" y="{62}">{self.desc}</text>'

        if self.user_symbol:
            svg += f'<text font-weight="bold" font-size="{self.adds_size}px" font-family="Courier" ' \
                   f'text-anchor="middle" x="{self.side * self.ratio[0] - 3}" y="{6}">{self.user_symbol[0]}</text>'

        if self.time:
            svg += f'<text font-weight="bold" font-size="{self.adds_size}px" font-family="Courier" ' \
                   f'text-anchor="end" x="{self.side * self.ratio[0] - 2}" ' \
                   f'y="{self.side * self.ratio[1] - 2}">{self.time}</text>'

        svg += f'<rect fill="none" height="100%" stroke="{self.border_color}" ' \
               f'stroke-width="{2 * self.border_width}" width="100%" x="0" y="0"/>'

        connectors = []
        for i in input_connectors:
            connectors.append([0, i / self.ratio[1]])
        for i in output_connectors:
            connectors.append([1, i / self.ratio[1]])
        points_style = f"points={connectors};"

        style = "verticalLabelPosition=top;labelBackgroundColor=none;verticalAlign=bottom;aspect=fixed;" \
                "imageAspect=0;fontFamily=Courier;fontSize=8;labelPosition=center;align=center;spacing=-1;" \
                f"fontStyle=1;syncNodeName={self.sync_name};resizable=0;"
        if self.is_function:
            style += f"syncInputs={list(self.inputs)};syncOutputs={list(self.outputs)};"

        svg += "</svg>"
        with open(file_path, "w") as svg_file:
            svg_file.write(svg)

        encoded_svg = to_shape(svg)

        if self.tooltip:
            tooltip = generate_tooltip(self.tooltip, self.is_function)
            shape = f'<mxGraphModel><root><mxCell id="0"/><mxCell id="1" parent="0"/><UserObject label="" ' \
                    f'tooltip="{tooltip}" id="2">' \
                    f'<mxCell style="shape=image;image=data:image/svg+xml,{encoded_svg};{points_style + style}" ' \
                    f'vertex="1" parent="1"><mxGeometry width="{size[0]}" height="{size[1]}" as="geometry"/>' \
                    f'</mxCell></UserObject></root></mxGraphModel>'
        else:
            shape = f'<mxGraphModel><root><mxCell id="0"/><mxCell id="1" parent="0"/><mxCell id="2" value="" ' \
                    f'style="shape=image;image=data:image/svg+xml,{encoded_svg};{points_style + style}" ' \
                    f'vertex="1" parent="1"><mxGeometry width="{size[0]}" height="{size[1]}" as="geometry"/>' \
                    f'</mxCell></root></mxGraphModel>'
        encoded_shape = to_library(shape).decode("utf-8")
        drawio_node_json = {
            "xml": encoded_shape,
            "w": size[0],
            "h": size[1],
            "aspect": "fixed",
            "title": self.label.title()
        }

        return drawio_node_json, file_path, points_style + style

    def draw_connectors(self, inout, orientation):
        svg = ""
        size = self.ratio[0] * self.side, self.ratio[1] * self.side
        r = 1 / 6
        label_centers = []
        node_connectors = []
        if len(inout):
            sep_connectors = [[]]
            sep_i = 0
            for value in inout:
                if value[0] != SEPARATOR:
                    sep_connectors[sep_i].append(value)
                else:
                    sep_i += 1
                    sep_connectors.append([])
            last_height = 0
            actual_counter = 0
            for value in sep_connectors:
                height = 0
                for variant, *v in value:
                    if variant in SINGLE or SMALL in v:
                        height += 1 / 3
                    else:
                        height += 2 / 3
                height += 1 / 3
                offset = (math.ceil(height) - height) / 2
                height = last_height
                for v in value:
                    variant = v[0]
                    con_type = None
                    other = v[1:]
                    if len(v) > 1:
                        con_type = v[1]
                        other = v[2:]
                        if con_type not in colors:
                            other = v[1:]
                            con_type = None
                    height += 1 / 3
                    if con_type:
                        color = "#%02x%02x%02x" % colors[con_type]
                    else:
                        color = "#%02x%02x%02x" % colors["any"]
                    if (variant == SINGLE and con_type not in ROUND) or variant == MULTIPLE:
                        if variant == SINGLE:
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
                        else:
                            if SMALL in other:
                                if DIRECTED in other:
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
                            else:
                                if DIRECTED in other:
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
                                else:
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
                        svg_points = ""
                        svg_points += " ".join(" ".join(map(str, p)) for p in points)
                        svg += f'<polygon fill="{color}" points="{svg_points}" ' \
                               f'stroke="{self.border_color}" stroke-width="{self.border_width}"/>'

                        if variant == MULTIPLE and SMALL not in other:
                            if DIRECTED in other:
                                node_connectors += [offset + height + r * (ic / 2) for ic in range(1, 6)]
                            else:
                                node_connectors += [offset + height + r * (ic / 2) for ic in range(-1, 6)]
                            height += 1 / 3
                        else:
                            node_connectors.append(offset + height)

                    if con_type in ROUND:
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
                        svg += f'<path fill="{color}" d="{svg_path}" ' \
                               f'stroke="{self.border_color}" stroke-width="{self.border_width}"/>'
                        node_connectors.append(offset + height)
                    if variant != EMPTY:
                        label_centers.append((offset + height))
                        actual_counter += 1
                height += 0.3
                last_height = math.ceil(height)
        return svg, label_centers, node_connectors


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
