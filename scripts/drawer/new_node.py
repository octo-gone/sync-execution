import gen


nodes_info = {
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
    },
}

style = gen.NodeSVG(nodes_info['len'])
