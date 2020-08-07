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
    'dict create': {
        'inputs': ('obj', 'obj'),
        'inputs_label': ('key', 'value'),
        'outputs': ('ctrl',),
        'outputs_label': ('ctrl',),
        'inner': 'Dict',
        'label': 'dict create'
    },
    'dict insert': {
        'inputs': ('any', 'any'),
        'inputs_label': ('key', 'value'),
        'outputs': ('ctrl',),
        'outputs_label': ('ctrl',),
        'inner': 'D-Ins',
        'label': 'dict insert'
    },
    'dict find': {
        'inputs': ('any', ),
        'inputs_label': ('key', ),
        'outputs': ('any',),
        'outputs_label': ('value',),
        'inner': 'D-Fnd',
        'label': 'dict find'
    },
    'dict insert and find': {
        'inputs': ('any', 'any'),
        'inputs_label': ('key', 'value'),
        'outputs': ('any',),
        'outputs_label': ('value',),
        'inner': 'D-IF',
        'label': 'dict insert and find'
    },
    'dict remove': {
        'inputs': ('any', ),
        'inputs_label': ('key', ),
        'outputs': ('ctrl',),
        'outputs_label': ('ctrl',),
        'inner': 'D-Rmv',
        'label': 'dict remove'
    },
}

for i, node_info in enumerate(nodes_info.values()):
    node = gen.NodeSVG(**node_info)
    file_path, style = node.draw_node("generated/")
    print(style)
    if i + 1 != len(nodes_info.values()):
        input()
