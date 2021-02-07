import re
import os
import math
from scripts.utils import nodes_v11 as nodes_info
from scripts.utils import logger
from scripts.utils import coder
from scripts.constants import *
from scripts import loader
from xml.sax.saxutils import unescape

# half of distance between small connectors
r = 1/6


def get_ratio(values):
    """Return size of node from inputs or outputs"""
    sep_values = [[]]
    sep_i = 0
    for value in values:
        if value[0] != SEPARATOR:
            sep_values[sep_i].append(value)
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


def get_connectors(inout):
    """Return possible connectors position"""
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
            offset = (math.ceil(height) - height)/2
            height = last_height
            for v in value:
                variant = v[0]
                other = v[1:]
                height += 1 / 3
                if variant == SINGLE or variant == MULTIPLE:
                    if variant == MULTIPLE and SMALL not in other:
                        if DIRECTED in other:
                            node_connectors += [offset + height + r * (ic / 2) for ic in range(1, 6)]
                        else:
                            node_connectors += [offset + height + r * (ic / 2) for ic in range(-1, 6)]
                        height += 1 / 3
                    else:
                        node_connectors.append(offset + height)
                if v[0] != EMPTY:
                    label_centers.append((offset + height))
                    actual_counter += 1
            height += 0.3
            last_height = math.ceil(height)
    return node_connectors


diagram_pattern = r"<diagram[^>]*?>(?P<diagram>.*?)<\/diagram>"

# patterns for parsing
node_pattern = r"(<UserObject.*?)?(?(1)<mxCell[^<]*?syncNodeName=.*?;.*?</mxCell>.*?</UserObject>|<mxCell[^<]*?syncNodeName=.*?;.*?</mxCell>)"
scope_pattern = r"<mxCell[^<]*?syncName=scope;.*?</mxCell>"
wire_pattern = r"<mxCell[^<]*?source.*?target.*?</mxCell>"

# patterns for node
id_pattern = r"id=\"(?P<id>.*?)\""
node_name_pattern = r"syncNodeName=(?P<node_name>.*?);"
image_pattern = r"image=data:image/svg\+xml,(?P<img>.*?);"
value_pattern = r"(UserObject.*)?(?(1)label=\"(?P<value0>.*?)\"|value=\"(?P<value1>.*?)\")"

# patterns for function
points_pattern = r"points=(?P<points>\[[0-9.\[\], ]*?\]);"
inputs_pattern = r"syncInputs=(?P<inputs>\[.*?\]);"
outputs_pattern = r"syncOutputs=(?P<outputs>\[.*?\]);"

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

    for alias, node_class in loader.node_aliases.items():
        if alias not in nodes_info.nodes_info:
            nodes_info.nodes_info.update({
                alias: node_class.desc
            })

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            data = unescape("".join(file.read().split("\n")))
            data = "'".join(data.split("&#39;"))
    elif not file_path:
        logger.log_error(f"no file to run")
    else:
        logger.log_error(f"file with name \"{file_path}\" not found")

    res = ""
    for diag in re.finditer(diagram_pattern, data):
        res += coder.from_library(diag['diagram'])

    data = res
    if not data:
        logger.log_error("no data in diagram")

    nodes = []
    wires = []

    for node in re.finditer(node_pattern, data):
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
        node = node.group()
        if not str(re.search(patterns["node_name"], node).group("node_name")).startswith("function"):
            for key in patterns.keys():
                res = re.search(patterns[key], node)
                if key == "value":
                    patterns[key] = res.group("value0") if res.group("value0") is not None else res.group("value1")
                else:
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
                    if key == "value":
                        patterns[key] = res.group("value0") if res.group("value0") else res.group("value1")
                    else:
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
