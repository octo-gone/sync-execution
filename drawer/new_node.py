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
    'matrix create': {
        'inputs': ('int', 'int', ),
        'inputs_label': ('len y', 'len x', ),
        'outputs': ('ctrl', ),
        'outputs_label': ('ctrl', ),
        'inner': 'Mtx',
        'label': 'matrix create'
    },
    'matrix set': {
        'inputs': ('int', 'int', 'sep', 'any'),
        'inputs_label': ('index y', 'index x', 'sep', 'value'),
        'outputs': ('ctrl', ),
        'outputs_label': ('ctrl', ),
        'inner': 'M-Set',
        'label': 'matrix set'
    },
    'matrix get': {
        'inputs': ('int', 'int'),
        'inputs_label': ('index y', 'index x'),
        'outputs': ('any', ),
        'outputs_label': ('value', ),
        'inner': 'M-Get',
        'label': 'matrix get'
    },
    'matrix get and set': {
        'inputs': ('int', 'int', 'sep', 'any'),
        'inputs_label': ('index y', 'index x', 'sep', 'value'),
        'outputs': ('any', ),
        'outputs_label': ('value', ),
        'inner': 'M-GS',
        'label': 'matrix get and set'
    },
}

for node_info in nodes_info.values():
    node = gen.NodeSVG(**node_info)
    file_path, style = node.draw_node("generated/")
    print(style)
    input()
