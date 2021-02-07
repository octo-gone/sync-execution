from scripts.drawer import gen_svg
import json

example_node = {
    'len': {
        'inputs': (
            ('single', 'ctrl'),  # ('single'|'multiple', [<type>, ['small', ['directed']]])
        ),
        'inputs_label': (
            'ctrl',
        ),  # optional (used in png descriptions)

        'outputs': (
            ('single', 'int'),  # ('single'|'multiple', [<type>, ['small', ['directed']]])
        ),
        'outputs_label': (
            'input 1',
        ),  # optional (used in png descriptions)

        'user_symbol': '&',  # optional
        'time': '~',  # optional

        'sync_name': 'length',  # optional
        'inner': 'Len',  # <6 symbols preferred or <12 if the separated with \n
        'label': 'length',
        'desc': 'in',  # optional

        'desc_size': 6,  # optional
        'adds_size': 6,  # optional
        'inner_size': 8,  # optional

        'bg_color': (255, 255, 255),  # optional
        'border_color': (0, 0, 0),  # optional
        'border_width': 0.5,  # optional

        'width': 1,  # optional

        'tooltip': {  # optional
            'label': 'Label',
            'desc': 'Node description',  # optional
            'inputs': [  # optional
                ('Input 1', 'input 1 desc'),
                ('Input 2', 'input 2 desc'),
            ],
            'outputs': [  # optional
                ('Output 1', 'output 1 desc'),
                ('Output 2', 'output 2 desc'),
            ],
            'adds': 'Node additional description',  # optional
            'word_wrap': 30  # optional
        }
    },
}


def generate_library(name, nodes: list, svg_folder="resources/generated/svg/", lib_folder="resources/libraries/"):
    svg_folder = svg_folder if svg_folder.endswith('/') else svg_folder + '/'
    lib_folder = lib_folder if lib_folder.endswith('/') else lib_folder + '/'

    library_data = "<mxlibrary>[{}]</mxlibrary>"
    n = []
    for i, node_info in enumerate(nodes):
        json_node, file_path, style = gen_svg.NodeSVG(**node_info).draw_node(svg_folder)
        n.append(json.dumps(json_node))

    with open(f"{lib_folder}{name}.drawio", 'w') as file:
        file.write(library_data.format(",".join(n)))


def generate_node(n, svg_folder="resources/generated/svg/"):
    svg_folder = svg_folder if svg_folder.endswith('/') else svg_folder + '/'
    json_node, file_path, style = gen_svg.NodeSVG(**n).draw_node(svg_folder)
    print(f"Image saved to '{file_path}'")
    print(f"Style for draw.io: {style}")


def generate_function(n, svg_folder="resources/generated/svg/", lib_folder="resources/libraries/"):
    svg_folder = svg_folder if svg_folder.endswith('/') else svg_folder + '/'
    lib_folder = lib_folder if lib_folder.endswith('/') else lib_folder + '/'

    library_data = "<mxlibrary>[{}]</mxlibrary>"
    ns = list(map(lambda x: json.dumps(x[0]), gen_svg.NodeFunctionSVG(**n).draw_node(svg_folder)))
    name = n.get('label', 'test')
    with open(f"{lib_folder}{name}.drawio", 'w') as file:
        file.write(library_data.format(",".join(ns)))


def generate_png_description(n):
    from scripts.drawer import gen_png
    gen_png.NodePNG(**n).draw_node()


def generate_png_descriptions(ns=None):
    from scripts.utils.nodes_v11 import base_nodes_info, structure_nodes_info

    if ns:
        for n in ns:
            generate_png_description(n)
    for n in list(base_nodes_info.values()) + list(structure_nodes_info.values()):
        generate_png_description(n)


def generate_base_libs(svg_folder="resources/generated/svg/", lib_folder="resources/"):
    from scripts.utils.nodes_v11 import base_nodes_info, structure_nodes_info, \
        base_nodes_lib_order, structure_nodes_lib_order

    base_library = []
    for n in base_nodes_lib_order:
        base_library.append(base_nodes_info[n])
    generate_library("base", base_library, svg_folder, lib_folder)

    structure_library = []
    for n in structure_nodes_lib_order:
        structure_library.append(structure_nodes_info[n])
    generate_library("structure", structure_library, svg_folder, lib_folder)


if __name__ == '__main__':
    svg_save_folder = "resources/generated/svg/"
    lib_save_folder = "resources/libraries/"

    library_name = "unit_testing"
    node = {
        'inner': 't',
        'label': 'test',
        'inputs': (
            ('single', 'int'),
            ('sep', 'real'),
            ('single', 'bool'),
            ('single', 'str'),
        ),
        'inputs_label': (
            'int',
            'bool',
            'str',
        ),
        'outputs': (
            ('single', 'any'),
            ('single', 'ctrl'),
            ('single', 'num'),
            ('single', 'obj'),
        )
    }
    nodes_info = [
        node
    ]

    # generate_png_description(node)
    # generate_png_descriptions(nodes_info)
    # generate_node(node, svg_save_folder)
    # generate_function(node, svg_save_folder, lib_save_folder)
    # generate_library(library_name, nodes_info, svg_save_folder, lib_save_folder)
    # generate_base_libs(svg_save_folder, "resources/")
