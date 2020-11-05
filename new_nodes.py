from scripts.drawer import gen
import json


example_node = {
    'len': {
        'inputs': ('ctrl', ),
        'inputs_color': ('ctrl', ),  # optional

        'outputs': ('int', ),
        'outputs_color': ('int', ),  # optional

        'user_symbol': '&',  # optional
        'time': '~',  # optional

        'sync_name': 'length',  # optional
        'inner': 'Len',  # <6 symbols preferred
        'label': 'length',
        'desc': 'in',  # optional

        'desc_size': 6,  # optional
        'adds_size': 6,  # optional
        'inner_size': 8,  # optional

        'bg_color': (255, 255, 255),  # optional
        'border_color': (0, 0, 0),  # optional
        'border_width': 0.5,  # optional

        'width': 1  # optional
    },
}


def generate_library(name, nodes):
    library_data = "<mxlibrary>[{}]</mxlibrary>"
    n = []
    for i, node_info in enumerate(nodes.values()):
        json_node, file_path, style = gen.NodeSVG(**node_info).draw_node("resources/generated/svg/")
        n.append(json.dumps(json_node))

    with open(f"resources/generated/{name}.drawio", 'w') as file:
        file.write(library_data.format(",".join(n)))


def generate_node(node):
    json_node, file_path, style = gen.NodeSVG(**node).draw_node("resources/generated/svg/")
    print(f"Image saved to '{file_path}'")
    print(f"Style for draw.io: {style}")


if __name__ == '__main__':
    library_name = "test"
    nodes_info = {
        'random seed': {
            'inputs': ('any',),
            'inputs_label': ('value',),
            'outputs': ('ctrl',),
            'outputs_label': ('ctrl',),
            'inner': 'Random\nSeed',
            'label': 'random seed'
        },
    }
    # generate_node(nodes_info['random seed'])
    # generate_library(library_name, nodes_info)
