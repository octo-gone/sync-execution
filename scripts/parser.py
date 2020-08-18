import re
import math
from scripts.utils import nodes_v9 as nodes_info
from scripts.utils import logger
from xml.sax.saxutils import unescape

# possible connectors variants
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

# half of distance between small connectors
r = 1/6


def get_ratio(values):
    """Return size of node from inputs or outputs"""
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
            if v in small_connectors + empty_connectors:
                height += 1 / 3
            if v in big_connectors:
                height += 2 / 3
        height += 1 / 3
        sum_height += math.ceil(height)

    return sum_height


def get_connectors(inout):
    """Return possible connectors position"""
    label_centers = []
    node_connectors = []
    if len(inout):
        sep_connectors = [[]]
        sep_i = 0
        for value in inout:
            if value not in separators:
                sep_connectors[sep_i].append(value)
            else:
                sep_i += 1
                sep_connectors.append([])
        last_height = 0
        actual_counter = 0
        for _, value in enumerate(sep_connectors):
            height = 0
            for v in value:
                if v in small_connectors + empty_connectors:
                    height += 1 / 3
                if v in big_connectors:
                    height += 2 / 3
            height += 1 / 3
            offset = (math.ceil(height) - height)/2
            height = last_height
            for v in value:
                height += 1 / 3

                if v in big_connectors + triangle_connectors + \
                        square_connectors + cut_square_connectors:
                    if v in big_connectors:
                        if v in rectangle_connectors:
                            node_connectors += [offset + height + r * (ic / 2) for ic in range(-1, 6)]
                        elif v in cut_rectangle_connectors:
                            node_connectors += [offset + height + r * (ic / 2) for ic in range(1, 6)]
                        height += 1 / 3
                    else:
                        node_connectors.append(offset + height)

                if v in round_connectors:
                    node_connectors.append(offset + height)

                if v not in empty_connectors:
                    label_centers.append((offset + height))
                    actual_counter += 1
            height += 0.3
            last_height = math.ceil(height)
    return node_connectors


# patterns for parsing
node_pattern = r"<mxCell[^<]*?syncNodeName=.*?;.*?</mxCell>"
scope_pattern = r"<mxCell[^<]*?syncName=scope;.*?</mxCell>"
wire_pattern = r"<mxCell[^<]*?source.*?target.*?</mxCell>"

# patterns for node
id_pattern = r"id=\"(?P<id>.*?)\""
node_name_pattern = r"syncNodeName=(?P<node_name>.*?);"
image_pattern = r"image=data:image/svg\+xml,(?P<img>.*?);"
value_pattern = r"value=\"(?P<value>.*?)\""

# patterns for function
points_pattern = r"points=(?P<points>\[[0-9.\[\], ]+?\]);"
inputs_pattern = r"syncInputs=(?P<inputs>\[.+?\]);"
outputs_pattern = r"syncOutputs=(?P<outputs>\[.+?\]);"

# general patterns
x_pattern = r"<mxGeometry.*x=\"(?P<x>.*?)\""
y_pattern = r"<mxGeometry.*y=\"(?P<y>.*?)\""
width_pattern = r"<mxGeometry.*width=\"(?P<width>.*?)\""
height_pattern = r"<mxGeometry.*height=\"(?P<height>.*?)\""

# patterns for wire
exitX_pattern = r"exitX=(?P<exitX>\d*\.?\d*)"
exitY_pattern = r"exitY=(?P<exitY>\d*\.?\d*)"
entryX_pattern = r"entryX=(?P<entryX>\d*\.?\d*)"
entryY_pattern = r"entryY=(?P<entryY>\d*\.?\d*)"
source_pattern = r"source=\"(?P<source>.*?)\""
target_pattern = r"target=\"(?P<target>.*?)\""


def parse(file_path):
    """
    Function parse uncompressed .drawio file and returns all nodes and all connected wires with description
    :param file_path: path to .drawio file
    :return: tuple (nodes, wires, scopes)
    """
    with open(file_path, "r") as file:
        data = unescape("".join(file.read().split("\n")))
        data = "'".join(data.split("&#39;"))

    nodes = []
    wires = []

    for node in re.findall(node_pattern, data):
        patterns = {
            "id": id_pattern,
            "img": image_pattern,
            "value": value_pattern,
            "x": x_pattern,
            "y": y_pattern,
            "width": width_pattern,
            "height": height_pattern,
            "node_name": node_name_pattern
        }
        if not str(re.search(patterns["node_name"], node).group("node_name")).startswith("function"):
            for key in patterns.keys():
                res = re.search(patterns[key], node)
                if res:
                    patterns[key] = res.group(key)
                else:
                    patterns[key] = None

            if patterns["node_name"] not in nodes_info.nodes_info:
                logger.log_error(f"no built-in nodes found with name '{patterns['node_name']}'")

            inputs = get_connectors(nodes_info.nodes_info[patterns["node_name"]]["inputs"])
            outputs = get_connectors(nodes_info.nodes_info[patterns["node_name"]]["outputs"])

            ratio = (1, max(get_ratio(nodes_info.nodes_info[patterns["node_name"]]["inputs"]),
                            get_ratio(nodes_info.nodes_info[patterns["node_name"]]["outputs"])))

            inputs = list(map(lambda x: round(x/ratio[1], 5), inputs))
            outputs = list(map(lambda x: round(x/ratio[1], 5), outputs))

            patterns["inputs"] = inputs
            patterns["outputs"] = outputs

            nodes.append(patterns)
        else:
            patterns["points"] = points_pattern
            patterns["inputs"] = inputs_pattern
            patterns["outputs"] = outputs_pattern
            for key in patterns.keys():
                res = re.search(patterns[key], node)
                if res:
                    patterns[key] = res.group(key)
                    if key in ("points", "inputs", "outputs"):
                        patterns[key] = eval(res.group(key))
                else:
                    patterns[key] = None
                    if key in ("points", "inputs", "outputs"):
                        patterns[key] = []

            inputs = get_connectors(patterns["inputs"])
            outputs = get_connectors(patterns["outputs"])

            ratio = (1, max(get_ratio(patterns["inputs"]),
                            get_ratio(patterns["outputs"])))

            if patterns["node_name"].startswith("function input") or \
               patterns["node_name"].startswith("function output"):
                ratio = (ratio[0], max(2, ratio[1]))

            inputs = list(map(lambda x: round(x / ratio[1], 5), inputs))
            outputs = list(map(lambda x: round(x / ratio[1], 5), outputs))

            patterns["inputs_names"] = patterns["inputs"]
            patterns["inputs"] = inputs
            patterns["outputs_names"] = patterns["outputs"]
            patterns["outputs"] = outputs

            nodes.append(patterns)

    for wire in re.findall(wire_pattern, data):
        patterns = {
            "id": id_pattern,
            "exitX": exitX_pattern,
            "exitY": exitY_pattern,
            "entryX": entryX_pattern,
            "entryY": entryY_pattern,
            "source": source_pattern,
            "target": target_pattern,
        }

        for key in patterns.keys():
            res = re.search(patterns[key], wire)
            if res:
                patterns[key] = res.group(key)
            else:
                patterns[key] = None

        for key in ["exitX", "exitY", "entryX", "entryY"]:
            if patterns[key] is None:
                logger.log_error(f"wrong connected wire found with source '{patterns['source']}' "
                                 f"and target '{patterns['target']}'")
            patterns[key] = round(float(patterns[key]), 5)

        wires.append(patterns)

    scopes = []
    for scope in re.findall(scope_pattern, data):
        patterns = {
            "id": id_pattern,
            "value": value_pattern,
            "x": x_pattern,
            "y": y_pattern,
            "width": width_pattern,
            "height": height_pattern,
        }
        for key in patterns.keys():
            res = re.search(patterns[key], scope)
            if res:
                patterns[key] = res.group(key)
            else:
                patterns[key] = None

        scopes.append(patterns)

    return nodes, wires, scopes
