import gen


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


nodes_info = {
    'random seed': {
        'inputs': ('any', ),
        'inputs_label': ('value', ),
        'outputs': ('ctrl',),
        'outputs_label': ('ctrl',),
        'inner': 'R-Seed',
        'label': 'random seed'
    },
}

for i, node_info in enumerate(nodes_info.values()):
    node = gen.NodeSVG(**node_info)
    file_path, style = node.draw_node("generated/")
    print(style)
    if i + 1 != len(nodes_info.values()):
        input()
