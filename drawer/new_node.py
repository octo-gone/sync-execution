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
        'inner': 'Len',
        'label': 'length',

        'label_size': 40,  # optional
        'description_size': 30,  # optional
        'inner_size': 70,  # optional

        'bg_color': (255, 255, 255),  # optional
        'border_color': (0, 0, 0),  # optional
        'border_width': 10,  # optional

        'width': 1  # optional
    },
}


nodes_info = {
    'random int': {
        'inputs': ('int', 'int'),
        'outputs': ('int', ),
        'inner': 'R-Int',
        'label': 'random int',
    },
    'random num': {
        'inputs': ('number', 'number'),
        'outputs': ('number', ),
        'inner': 'R-Num',
        'label': 'random num',
    },
    'random': {
        'inputs': ('ctrl', ),
        'outputs': ('real', ),
        'inner': 'Rand',
        'label': 'random',
    }
}

for node_info in nodes_info.values():
    node = gen.NodeSVG(**node_info)
    file_path, style = node.draw_node("generated/")
    print(style)
    input()
