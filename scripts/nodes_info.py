# full node information
nodes = {
    'abs': {
        'inputs': ('number', ),
        'inputs_label': ('number', ),
        'outputs': ('number', ),
        'outputs_label': ('number', ),
        'inner': 'Abs',
        'label': 'abs'
    },
    'add': {
        'inputs': ('mult', ),
        'inputs_label': ('in', ),
        'outputs': ('any', ),
        'outputs_label': ('result', ),
        'inner': '+',
        'label': 'add'
    },
    'add int': {
        'inputs': ('mult', ),
        'inputs_label': ('int', ),
        'inputs_color': ('int', ),
        'outputs': ('int', ),
        'outputs_label': ('int', ),
        'inner': '+',
        'label': 'add int'
    },
    'add number': {
        'inputs': ('mult', ),
        'inputs_label': ('number', ),
        'inputs_color': ('number', ),
        'outputs': ('number', ),
        'outputs_label': ('number', ),
        'inner': '+',
        'label': 'add number'
    },
    'add real': {
        'inputs': ('mult', ),
        'inputs_label': ('real', ),
        'inputs_color': ('real', ),
        'outputs': ('real', ),
        'outputs_label': ('real', ),
        'inner': '+',
        'label': 'add real'
    },
    'and': {
        'inputs': ('bool', 'bool'),
        'inputs_label': ('bool', 'bool'),
        'outputs': ('bool', ),
        'outputs_label': ('bool', ),
        'inner': '&',
        'label': 'and'
    },
    'general and': {
        'inputs': ('mult', ),
        'inputs_label': ('values', ),
        'inputs_color': ('bool', ),
        'outputs': ('bool', ),
        'outputs_label': ('bool', ),
        'inner': '&',
        'label': 'and general'
    },
    'array': {
        'inputs': ('obj', 'int'),
        'inputs_label': ('type', 'length'),
        'outputs': ('dir_mult', ),
        'outputs_label': ('array', ),
        'inner': 'Array',
        'label': 'array'
    },
    'array gs': {
        'inputs': ('dir_mult', 'sep', 'int', 'any'),
        'inputs_label': ('array', 'index', 'set value'),
        'outputs': ('dir_mult', 'sep', 'any'),
        'outputs_label': ('array', 'get value'),
        'inner': 'G/S',
        'label': 'array get and set'
    },
    'array len': {
        'inputs': ('dir_mult', ),
        'inputs_label': ('array', ),
        'outputs': ('int', ),
        'outputs_label': ('length', ),
        'inner': 'Len',
        'label': 'array len'
    },
    'bool': {
        'inputs': ('any', ),
        'inputs_label': ('any', ),
        'outputs': ('bool', ),
        'outputs_label': ('bool', ),
        'inner': 'Bool',
        'label': 'bool'
    },
    'char': {
        'inputs': ('any', ),
        'inputs_label': ('any', ),
        'outputs': ('char', ),
        'outputs_label': ('char', ),
        'inner': 'Char',
        'label': 'char'
    },
    'check ctrl': {
        'inputs': ('ctrl', ),
        'inputs_label': ('ctrl', ),
        'outputs': ('bool', ),
        'outputs_label': ('bool', ),
        'inner': 'CC',
        'label': 'check ctrl'
    },
    'concatenate': {
        'inputs': ('dir_mult', ),
        'inputs_label': ('char', ),
        'inputs_color': ('char', ),
        'outputs': ('char', ),
        'outputs_label': ('char', ),
        'inner': '+',
        'label': 'concatenation'
    },
    'const char': {
        'inputs': (),
        'inputs_label': (),
        'outputs': ('char', ),
        'outputs_label': ('char', ),
        'inner': 'Const',
        'label': 'const char'
    },
    'const char ctrl': {
        'inputs': ('ctrl', ),
        'inputs_label': ('ctrl', ),
        'outputs': ('char', ),
        'outputs_label': ('char', ),
        'inner': 'Const',
        'label': 'const char with ctrl'
    },
    'const int': {
        'inputs': (),
        'inputs_label': (),
        'outputs': ('int', ),
        'outputs_label': ('int', ),
        'inner': 'Const',
        'label': 'const int'
    },
    'const int ctrl': {
        'inputs': ('ctrl', ),
        'inputs_label': ('ctrl', ),
        'outputs': ('int', ),
        'outputs_label': ('int', ),
        'inner': 'Const',
        'label': 'const int with ctrl'
    },
    'const number': {
        'inputs': (),
        'inputs_label': (),
        'outputs': ('number', ),
        'outputs_label': ('number', ),
        'inner': 'Const',
        'label': 'const number'
    },
    'const number ctrl': {
        'inputs': ('ctrl', ),
        'inputs_label': ('ctrl', ),
        'outputs': ('number', ),
        'outputs_label': ('number', ),
        'inner': 'Const',
        'label': 'const number with ctrl'
    },
    'const real': {
        'inputs': (),
        'inputs_label': (),
        'outputs': ('real', ),
        'outputs_label': ('real', ),
        'inner': 'Const',
        'label': 'const real'
    },
    'const real ctrl': {
        'inputs': ('ctrl', ),
        'inputs_label': ('ctrl', ),
        'outputs': ('real', ),
        'outputs_label': ('real', ),
        'inner': 'Const',
        'label': 'const real with ctrl'
    },
    'const': {
        'inputs': (),
        'inputs_label': (),
        'outputs': ('any', ),
        'outputs_label': ('any', ),
        'inner': 'Const',
        'label': 'constant'
    },
    'const ctrl': {
        'inputs': ('ctrl', ),
        'inputs_label': ('ctrl', ),
        'outputs': ('any', ),
        'outputs_label': ('any', ),
        'inner': 'Const',
        'label': 'constant with ctrl'
    },
    'counter': {
        'inputs': ('ctrl', 'int', 'sep', 'ctrl'),
        'inputs_label': ('ctrl', 'bound', 'next'),
        'outputs': ('ctrl', 'sep', 'int'),
        'outputs_label': ('end ctrl', 'count'),
        'inner': 'Ctr',
        'label': 'counter'
    },
    'dec': {
        'inputs': ('number', ),
        'inputs_label': ('number', ),
        'outputs': ('number', ),
        'outputs_label': ('number', ),
        'inner': 'Dec',
        'label': 'decrement'
    },
    'delay': {
        'inputs': ('ctrl', 'int'),
        'inputs_label': ('ctrl', 'time'),
        'outputs': ('ctrl', ),
        'outputs_label': ('ctrl', ),
        'inner': 'Delay',
        'label': 'delay'
    },
    'div': {
        'inputs': ('number', 'number'),
        'inputs_label': ('dividend', 'divider'),
        'outputs': ('int', ),
        'outputs_label': ('int', ),
        'inner': '//',
        'label': 'div'
    },
    'divide number': {
        'inputs': ('number', 'number'),
        'inputs_label': ('dividend', 'divider'),
        'outputs': ('number', ),
        'outputs_label': ('number', ),
        'inner': '/',
        'label': 'div number'
    },
    'divide': {
        'inputs': ('any', 'any'),
        'inputs_label': ('dividend', 'divider'),
        'outputs': ('any', ),
        'outputs_label': ('result', ),
        'inner': '/',
        'label': 'division'
    },
    'general equal': {
        'inputs': ('mult', ),
        'inputs_label': ('values', ),
        'outputs': ('bool', ),
        'outputs_label': ('bool', ),
        'inner': '=',
        'label': 'equal general'
    },
    'equal': {
        'inputs': ('any', 'any'),
        'inputs_label': ('a', 'b'),
        'outputs': ('bool', ),
        'outputs_label': ('bool', ),
        'inner': 'a=b',
        'label': 'equal'
    },
    'error': {
        'inputs': ('ctrl', ),
        'inputs_label': ('ctrl', ),
        'outputs': (),
        'outputs_label': (),
        'inner': 'Err',
        'label': 'error message'
    },
    'exp number': {
        'inputs': ('number', 'number'),
        'inputs_label': ('base', 'exponent'),
        'outputs': ('number', ),
        'outputs_label': ('number', ),
        'inner': '**',
        'label': 'exp number'
    },
    'exp': {
        'inputs': ('any', 'any'),
        'inputs_label': ('base', 'exponent'),
        'outputs': ('any', ),
        'outputs_label': ('result', ),
        'inner': '**',
        'label': 'exponentiation'
    },
    'for int': {
        'inputs': ('ctrl', 'int', 'sep', 'int'),
        'inputs_label': ('ctrl', 'bound', 'increment'),
        'outputs': ('ctrl', 'sep', 'int'),
        'outputs_label': ('end ctrl', 'iteration'),
        'inner': 'For',
        'label': 'for'
    },
    'for ext int': {
        'inputs': ('ctrl', 'int', 'int', 'int'),
        'inputs_label': ('ctrl', 'bound', 'start value', 'increment'),
        'outputs': ('ctrl', 'sep', 'int'),
        'outputs_label': ('end ctrl', 'iteration'),
        'inner': 'For',
        'label': 'for extended'
    },
    'for ext number': {
        'inputs': ('ctrl', 'number', 'number', 'number'),
        'inputs_label': ('ctrl', 'bound', 'start value', 'increment'),
        'outputs': ('ctrl', 'sep', 'number'),
        'outputs_label': ('end ctrl', 'iteration'),
        'inner': 'For',
        'label': 'for extended number'
    },
    'for ext real': {
        'inputs': ('ctrl', 'real', 'real', 'real'),
        'inputs_label': ('ctrl', 'bound', 'start value', 'increment'),
        'outputs': ('ctrl', 'sep', 'real'),
        'outputs_label': ('end ctrl', 'iteration'),
        'inner': 'For',
        'label': 'for extended real'
    },
    'for number': {
        'inputs': ('ctrl', 'number', 'sep', 'number'),
        'inputs_label': ('ctrl', 'bound', 'increment'),
        'outputs': ('ctrl', 'sep', 'number'),
        'outputs_label': ('end ctrl', 'iteration'),
        'inner': 'For',
        'label': 'for number'
    },
    'for real': {
        'inputs': ('ctrl', 'real', 'sep', 'real'),
        'inputs_label': ('ctrl', 'bound', 'increment'),
        'outputs': ('ctrl', 'sep', 'real'),
        'outputs_label': ('end ctrl', 'iteration'),
        'inner': 'For',
        'label': 'for real'
    },
    'foreach': {
        'inputs': ('dir_mult', 'sep', 'ctrl'),
        'inputs_label': ('values', 'next'),
        'outputs': ('ctrl', 'sep', 'any'),
        'outputs_label': ('end ctrl', 'value'),
        'inner': 'For',
        'label': 'foreach'
    },
    't': {
        'inputs': (),
        'inputs_label': (),
        'outputs': ('obj', 'any'),
        'outputs_label': ('type', 'default'),
        'inner': 'T',
        'label': 'get type'
    },
    'greater': {
        'inputs': ('any', 'any'),
        'inputs_label': ('a', 'b'),
        'outputs': ('bool', ),
        'outputs_label': ('bool', ),
        'inner': 'a>b',
        'label': 'greater'
    },
    'greater or equal': {
        'inputs': ('any', 'any'),
        'inputs_label': ('a', 'b'),
        'outputs': ('bool', ),
        'outputs_label': ('bool', ),
        'inner': 'a>=b',
        'label': 'greater or equal'
    },
    'if': {
        'inputs': ('ctrl', 'bool'),
        'inputs_label': ('ctrl', 'condition'),
        'outputs': ('ctrl', 'ctrl'),
        'outputs_label': ('true', 'false'),
        'inner': 'If',
        'label': 'if'
    },
    'in': {
        'inputs': ('mult_s', 'any'),
        'inputs_label': ('mult', 'any'),
        'outputs': ('bool', ),
        'outputs_label': ('bool', ),
        'inner': 'In',
        'label': 'contains'
    },
    'inc': {
        'inputs': ('number', ),
        'inputs_label': ('number', ),
        'outputs': ('number', ),
        'outputs_label': ('number', ),
        'inner': 'Inc',
        'label': 'increment'
    },
    'input': {
        'inputs': ('ctrl', ),
        'inputs_label': ('ctrl', ),
        'outputs': ('any', ),
        'outputs_label': ('any', ),
        'inner': 'Input',
        'label': 'input'
    },
    'input string': {
        'inputs': ('ctrl', ),
        'inputs_label': ('ctrl', ),
        'outputs': ('dir_mult', ),
        'outputs_label': ('string', ),
        'outputs_color': ('char', ),
        'inner': 'Input',
        'label': 'input string'
    },
    'int': {
        'inputs': ('number', ),
        'inputs_label': ('number', ),
        'outputs': ('int', ),
        'outputs_label': ('int', ),
        'inner': 'Int',
        'label': 'int'
    },
    'inv': {
        'inputs': ('number', ),
        'inputs_label': ('number', ),
        'outputs': ('number', ),
        'outputs_label': ('number', ),
        'inner': 'Inv',
        'label': 'inversion'
    },
    'less': {
        'inputs': ('any', 'any'),
        'inputs_label': ('a', 'b'),
        'outputs': ('bool', ),
        'outputs_label': ('bool', ),
        'inner': 'a<b',
        'label': 'less'
    },
    'less or equal': {
        'inputs': ('any', 'any'),
        'inputs_label': ('a', 'b'),
        'outputs': ('bool', ),
        'outputs_label': ('bool', ),
        'inner': 'a<=b',
        'label': 'less or equal'
    },
    'map': {
        'inputs': ('obj', 'obj'),
        'inputs_label': ('key type', 'value type'),
        'outputs': ('mult', ),
        'outputs_label': ('map', ),
        'inner': 'Map',
        'label': 'map'
    },
    'map erase': {
        'inputs': ('mult', 'sep', 'any'),
        'inputs_label': ('map', 'key'),
        'outputs': (),
        'outputs_label': (),
        'inner': 'Erase',
        'label': 'map erase'
    },
    'map if': {
        'inputs': ('mult', 'sep', 'any', 'any'),
        'inputs_label': ('map', 'key', 'insert'),
        'outputs': ('mult', 'sep', 'any'),
        'outputs_label': ('map', 'find'),
        'inner': 'I/F',
        'label': 'map insert and find'
    },
    'map keys': {
        'inputs': ('mult', ),
        'inputs_label': ('map', ),
        'outputs': ('dir_mult', ),
        'outputs_label': ('array', ),
        'inner': 'Keys',
        'label': 'map keys'
    },
    'len': {
        'inputs': ('mult', ),
        'inputs_label': ('map', ),
        'outputs': ('int', ),
        'outputs_label': ('length', ),
        'inner': 'Len',
        'label': 'map len'
    },
    'merge': {
        'inputs': ('ctrl', 'any'),
        'inputs_label': ('ctrl', 'any'),
        'outputs': ('any', ),
        'outputs_label': ('any', ),
        'inner': 'Merge',
        'label': 'merge ctrl'
    },
    'message': {
        'inputs': ('any', ),
        'inputs_label': ('any', ),
        'outputs': ('dir_mult', ),
        'outputs_label': ('string', ),
        'outputs_color': ('char', ),
        'inner': 'Msg',
        'label': 'message'
    },
    'mod': {
        'inputs': ('number', 'number'),
        'inputs_label': ('dividend', 'divider'),
        'outputs': ('number', ),
        'outputs_label': ('number', ),
        'inner': '%',
        'label': 'mod'
    },
    'mult char': {
        'inputs': ('char', 'int'),
        'inputs_label': ('char', 'count'),
        'outputs': ('dir_mult', ),
        'outputs_label': ('string', ),
        'outputs_color': ('char', ),
        'inner': '*',
        'label': 'mult char'
    },
    'mult int': {
        'inputs': ('mult', ),
        'inputs_label': ('int', ),
        'inputs_color': ('int', ),
        'outputs': ('int', ),
        'outputs_label': ('int', ),
        'inner': '*',
        'label': 'mult int'
    },
    'mult number': {
        'inputs': ('mult', ),
        'inputs_label': ('number', ),
        'inputs_color': ('number', ),
        'outputs': ('number', ),
        'outputs_label': ('number', ),
        'inner': '*',
        'label': 'mult number'
    },
    'mult real': {
        'inputs': ('mult', ),
        'inputs_label': ('real', ),
        'inputs_color': ('real', ),
        'outputs': ('real', ),
        'outputs_label': ('real', ),
        'inner': '*',
        'label': 'mult real'
    },
    'mult': {
        'inputs': ('any', 'any'),
        'inputs_label': ('any', 'any'),
        'outputs': ('any', ),
        'outputs_label': ('any', ),
        'inner': '*',
        'label': 'multiplication'
    },
    'not': {
        'inputs': ('bool', ),
        'inputs_label': ('bool', ),
        'outputs': ('bool', ),
        'outputs_label': ('bool', ),
        'inner': 'Not',
        'label': 'not'
    },
    'not equal': {
        'inputs': ('any', 'any'),
        'inputs_label': ('a', 'b'),
        'outputs': ('bool', ),
        'outputs_label': ('bool', ),
        'inner': 'a!=b',
        'label': 'not equal'
    },
    'or': {
        'inputs': ('bool', 'bool'),
        'inputs_label': ('bool', 'bool'),
        'outputs': ('bool', ),
        'outputs_label': ('bool', ),
        'inner': '|',
        'label': 'or'
    },
    'general or': {
        'inputs': ('mult', ),
        'inputs_label': ('values', ),
        'inputs_color': ('bool', ),
        'outputs': ('bool', ),
        'outputs_label': ('bool', ),
        'inner': '|',
        'label': 'or general'
    },
    'print': {
        'inputs': ('any', ),
        'inputs_label': ('any', ),
        'outputs': (),
        'outputs_label': (),
        'inner': 'Print',
        'label': 'print'
    },
    'print string': {
        'inputs': ('dir_mult', ),
        'inputs_label': ('string', ),
        'inputs_color': ('char', ),
        'outputs': (),
        'outputs_label': (),
        'inner': 'Print',
        'label': 'print string'
    },
    'print ctrl': {
        'inputs': ('any', ),
        'inputs_label': ('any', ),
        'outputs': ('ctrl', ),
        'outputs_label': ('ctrl', ),
        'inner': 'Print',
        'label': 'print with ctrl'
    },
    'round': {
        'inputs': ('number', 'int'),
        'inputs_label': ('number', 'precision'),
        'outputs': ('number', ),
        'outputs_label': ('number', ),
        'inner': 'Round',
        'label': 'round'
    },
    'run': {
        'inputs': (),
        'inputs_label': (),
        'outputs': ('ctrl', ),
        'outputs_label': ('ctrl', ),
        'inner': 'Run',
        'label': 'run'
    },
    'stop': {
        'inputs': ('ctrl', ),
        'inputs_label': ('ctrl', ),
        'outputs': (),
        'outputs_label': (),
        'inner': 'Stop',
        'label': 'stop'
    },
    'sub int': {
        'inputs': ('int', 'int'),
        'inputs_label': ('minuend', 'subtrahend'),
        'outputs': ('int', ),
        'outputs_label': ('int', ),
        'inner': '-',
        'label': 'sub int'
    },
    'sub number': {
        'inputs': ('number', 'number'),
        'inputs_label': ('minuend', 'subtrahend'),
        'outputs': ('number', ),
        'outputs_label': ('number', ),
        'inner': '-',
        'label': 'sub number'
    },
    'sub real': {
        'inputs': ('real', 'real'),
        'inputs_label': ('minuend', 'subtrahend'),
        'outputs': ('real', ),
        'outputs_label': ('real', ),
        'inner': '-',
        'label': 'sub real'
    },
    'sub': {
        'inputs': ('any', 'any'),
        'inputs_label': ('minuend', 'subtrahend'),
        'outputs': ('any', ),
        'outputs_label': ('result', ),
        'inner': '-',
        'label': 'subtraction'
    },
    'timer': {
        'inputs': ('ctrl', 'ctrl'),
        'inputs_label': ('start ctrl', 'end ctrl'),
        'outputs': ('int', ),
        'outputs_label': ('time', ),
        'inner': 'Timer',
        'label': 'timer'
    },
    'ctrl': {
        'inputs': ('any', ),
        'inputs_label': ('any', ),
        'outputs': ('ctrl', ),
        'outputs_label': ('ctrl', ),
        'inner': 'Ctrl',
        'label': 'to ctrl'
    },
    'type': {
        'inputs': ('any', ),
        'inputs_label': ('any', ),
        'outputs': ('obj', ),
        'outputs_label': ('type', ),
        'inner': 'Type',
        'label': 'type'
    },
    'var char': {
        'inputs': ('char', ),
        'inputs_label': ('char', ),
        'outputs': ('char', ),
        'outputs_label': ('char', ),
        'inner': 'Var',
        'label': 'var char'
    },
    'var int': {
        'inputs': ('int', ),
        'inputs_label': ('int', ),
        'outputs': ('int', ),
        'outputs_label': ('int', ),
        'inner': 'Var',
        'label': 'var int'
    },
    'var number': {
        'inputs': ('number', ),
        'inputs_label': ('number', ),
        'outputs': ('number', ),
        'outputs_label': ('number', ),
        'inner': 'Var',
        'label': 'var number'
    },
    'var real': {
        'inputs': ('real', ),
        'inputs_label': ('real', ),
        'outputs': ('real', ),
        'outputs_label': ('real', ),
        'inner': 'Var',
        'label': 'var real'
    },
    'var': {
        'inputs': ('any', ),
        'inputs_label': ('any', ),
        'outputs': ('any', ),
        'outputs_label': ('any', ),
        'inner': 'Var',
        'label': 'variable'
    },
    'wait': {
        'inputs': ('mult', ),
        'inputs_label': ('ctrl', ),
        'inputs_color': ('ctrl', ),
        'outputs': ('ctrl', ),
        'outputs_label': ('ctrl', ),
        'inner': 'Wait',
        'label': 'wait'
    },
    'while': {
        'inputs': ('ctrl', 'sep', 'bool'),
        'inputs_label': ('ctrl', 'condition'),
        'outputs': ('ctrl', 'sep', 'ctrl'),
        'outputs_label': ('ctrl', 'while ctrl'),
        'inner': 'While',
        'label': 'while'
    },
    'xor': {
        'inputs': ('bool', 'bool'),
        'inputs_label': ('bool', 'bool'),
        'outputs': ('bool', ),
        'outputs_label': ('bool', ),
        'inner': '^',
        'label': 'xor'
    },
    'value switch': {
        'inputs': ('mult', ),
        'inputs_label': ('values', ),
        'outputs': ('any', ),
        'outputs_label': ('value', ),
        'inner': '>-',
        'label': 'value switch'
    }
}

# drawio compressed svg-image data
drawio_nodes = {
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiM4OGQxYzkiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjODhkMWM5IiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPkFiczwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'abs',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2Niw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwzMy4zMzMzMzMzMzMzMzMzMyAwLDMzLjMzMzMzMzMzMzMzMzMzIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2JmYmZiZiIgcG9pbnRzPSI0MCwxMy4zMzMzMzMzMzMzMzMzMzYgMzMuMzMzMzMzMzMzMzMzMzM2LDIwLjAgNDAsMjYuNjY2NjY2NjY2NjY2NjY0IDQwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48dGV4dCBzdHlsZT0iZm9udC1zaXplOjhweDsgZm9udC1mYW1pbHk6Q291cmllcjtmb250LXdlaWdodDpib2xkOyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjAiIHk9IjIyIj4rPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'add',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiM2ZGNmZjYiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2Niw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwzMy4zMzMzMzMzMzMzMzMzMyAwLDMzLjMzMzMzMzMzMzMzMzMzIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iIzZkY2ZmNiIgcG9pbnRzPSI0MCwxMy4zMzMzMzMzMzMzMzMzMzYgMzMuMzMzMzMzMzMzMzMzMzM2LDIwLjAgNDAsMjYuNjY2NjY2NjY2NjY2NjY0IDQwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48dGV4dCBzdHlsZT0iZm9udC1zaXplOjhweDsgZm9udC1mYW1pbHk6Q291cmllcjtmb250LXdlaWdodDpib2xkOyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjAiIHk9IjIyIj4rPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'add int',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiM4OGQxYzkiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2Niw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwzMy4zMzMzMzMzMzMzMzMzMyAwLDMzLjMzMzMzMzMzMzMzMzMzIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iIzg4ZDFjOSIgcG9pbnRzPSI0MCwxMy4zMzMzMzMzMzMzMzMzMzYgMzMuMzMzMzMzMzMzMzMzMzM2LDIwLjAgNDAsMjYuNjY2NjY2NjY2NjY2NjY0IDQwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48dGV4dCBzdHlsZT0iZm9udC1zaXplOjhweDsgZm9udC1mYW1pbHk6Q291cmllcjtmb250LXdlaWdodDpib2xkOyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjAiIHk9IjIyIj4rPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'add number',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNhM2QzOWMiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2Niw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwzMy4zMzMzMzMzMzMzMzMzMyAwLDMzLjMzMzMzMzMzMzMzMzMzIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2EzZDM5YyIgcG9pbnRzPSI0MCwxMy4zMzMzMzMzMzMzMzMzMzYgMzMuMzMzMzMzMzMzMzMzMzM2LDIwLjAgNDAsMjYuNjY2NjY2NjY2NjY2NjY0IDQwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48dGV4dCBzdHlsZT0iZm9udC1zaXplOjhweDsgZm9udC1mYW1pbHk6Q291cmllcjtmb250LXdlaWdodDpib2xkOyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjAiIHk9IjIyIj4rPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'add real',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNhMTg2YmUiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2ExODZiZSIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNhMTg2YmUiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+JmFtcDs8L3RleHQ+PHJlY3QgZmlsbD0ibm9uZSIgaGVpZ2h0PSI0MCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEuNiIgd2lkdGg9IjQwIiB4PSIwIiB5PSIwIi8+PC9zdmc+': 'and',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNhMTg2YmUiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2Niw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwzMy4zMzMzMzMzMzMzMzMzMyAwLDMzLjMzMzMzMzMzMzMzMzMzIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2ExODZiZSIgcG9pbnRzPSI0MCwxMy4zMzMzMzMzMzMzMzMzMzYgMzMuMzMzMzMzMzMzMzMzMzM2LDIwLjAgNDAsMjYuNjY2NjY2NjY2NjY2NjY0IDQwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48dGV4dCBzdHlsZT0iZm9udC1zaXplOjhweDsgZm9udC1mYW1pbHk6Q291cmllcjtmb250LXdlaWdodDpib2xkOyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjAiIHk9IjIyIj4mYW1wOzwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'general and',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwYXRoIGQ9Ik0gMCA2LjY2NjY2NjY2NjY2NjY2NiBBIDYuNjY2NjY2NjY2NjY2NjY2IDYuNjY2NjY2NjY2NjY2NjY2IDAgMCAxIDAgMjAuMCIgZmlsbD0iI2Y2OTY3OSIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiM2ZGNmZjYiIHBvaW50cz0iMCwyMC4wIDYuNjY2NjY2NjY2NjY2NjY2LDI2LjY2NjY2NjY2NjY2NjY2NCAwLDMzLjMzMzMzMzMzMzMzMzMzIDAsMjAuMCIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjYmZiZmJmIiBwb2ludHM9IjQwLDYuNjY2NjY2NjY2NjY2NjY2IDMzLjMzMzMzMzMzMzMzMzMzNiwzMy4zMzMzMzMzMzMzMzMzMyA0MCwzMy4zMzMzMzMzMzMzMzMzMyA0MCw2LjY2NjY2NjY2NjY2NjY2NiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48dGV4dCBzdHlsZT0iZm9udC1zaXplOjhweDsgZm9udC1mYW1pbHk6Q291cmllcjtmb250LXdlaWdodDpib2xkOyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjAiIHk9IjIyIj5BcnJheTwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'array',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI4MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA4MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iODAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwzMy4zMzMzMzMzMzMzMzMzMyAwLDMzLjMzMzMzMzMzMzMzMzMzIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iIzZkY2ZmNiIgcG9pbnRzPSIwLDQ2LjY2NjY2NjY2NjY2NjY2IDYuNjY2NjY2NjY2NjY2NjY2LDUzLjMzMzMzMzMzMzMzMzMzIDAsNjAuMCAwLDQ2LjY2NjY2NjY2NjY2NjY2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCw1OS45OTk5OTk5OTk5OTk5OSA2LjY2NjY2NjY2NjY2NjY2Niw2Ni42NjY2NjY2NjY2NjY2NiAwLDczLjMzMzMzMzMzMzMzMzMzIDAsNTkuOTk5OTk5OTk5OTk5OTkiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2JmYmZiZiIgcG9pbnRzPSI0MCw2LjY2NjY2NjY2NjY2NjY2NiAzMy4zMzMzMzMzMzMzMzMzMzYsMzMuMzMzMzMzMzMzMzMzMzMgNDAsMzMuMzMzMzMzMzMzMzMzMzMgNDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2JmYmZiZiIgcG9pbnRzPSI0MCw1My4zMzMzMzMzMzMzMzMzMyAzMy4zMzMzMzMzMzMzMzMzMzYsNjAuMCA0MCw2Ni42NjY2NjY2NjY2NjY2NyA0MCw1My4zMzMzMzMzMzMzMzMzMyIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48dGV4dCBzdHlsZT0iZm9udC1zaXplOjhweDsgZm9udC1mYW1pbHk6Q291cmllcjtmb250LXdlaWdodDpib2xkOyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjAiIHk9IjIyIj5HL1M8L3RleHQ+PHJlY3QgZmlsbD0ibm9uZSIgaGVpZ2h0PSI4MCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEuNiIgd2lkdGg9IjQwIiB4PSIwIiB5PSIwIi8+PC9zdmc+': 'array gs',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwzMy4zMzMzMzMzMzMzMzMzMyAwLDMzLjMzMzMzMzMzMzMzMzMzIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iIzZkY2ZmNiIgcG9pbnRzPSI0MCwxMy4zMzMzMzMzMzMzMzMzMzYgMzMuMzMzMzMzMzMzMzMzMzM2LDIwLjAgNDAsMjYuNjY2NjY2NjY2NjY2NjY0IDQwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48dGV4dCBzdHlsZT0iZm9udC1zaXplOjhweDsgZm9udC1mYW1pbHk6Q291cmllcjtmb250LXdlaWdodDpib2xkOyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjAiIHk9IjIyIj5MZW48L3RleHQ+PHJlY3QgZmlsbD0ibm9uZSIgaGVpZ2h0PSI0MCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEuNiIgd2lkdGg9IjQwIiB4PSIwIiB5PSIwIi8+PC9zdmc+': 'array len',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjYTE4NmJlIiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPkJvb2w8L3RleHQ+PHJlY3QgZmlsbD0ibm9uZSIgaGVpZ2h0PSI0MCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEuNiIgd2lkdGg9IjQwIiB4PSIwIiB5PSIwIi8+PC9zdmc+': 'bool',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cGF0aCBkPSJNIDQwIDI2LjY2NjY2NjY2NjY2NjY2NCBBIDYuNjY2NjY2NjY2NjY2NjY2IDYuNjY2NjY2NjY2NjY2NjY2IDAgMCAxIDQwIDEzLjMzMzMzMzMzMzMzMzMzNCIgZmlsbD0iI2ZmZjc5OSIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPkNoYXI8L3RleHQ+PHJlY3QgZmlsbD0ibm9uZSIgaGVpZ2h0PSI0MCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEuNiIgd2lkdGg9IjQwIiB4PSIwIiB5PSIwIi8+PC9zdmc+': 'char',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjYTE4NmJlIiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPkNDPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'check ctrl',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNmZmY3OTkiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwzMy4zMzMzMzMzMzMzMzMzMyAwLDMzLjMzMzMzMzMzMzMzMzMzIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2ZmZjc5OSIgcG9pbnRzPSI0MCw2LjY2NjY2NjY2NjY2NjY2NiAzMy4zMzMzMzMzMzMzMzMzMzYsMzMuMzMzMzMzMzMzMzMzMzMgNDAsMzMuMzMzMzMzMzMzMzMzMzMgNDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+KzwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'concatenate',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwYXRoIGQ9Ik0gNDAgMjYuNjY2NjY2NjY2NjY2NjY0IEEgNi42NjY2NjY2NjY2NjY2NjYgNi42NjY2NjY2NjY2NjY2NjYgMCAwIDEgNDAgMTMuMzMzMzMzMzMzMzMzMzM0IiBmaWxsPSIjZmZmNzk5IiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+Q29uc3Q8L3RleHQ+PHJlY3QgZmlsbD0ibm9uZSIgaGVpZ2h0PSI0MCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEuNiIgd2lkdGg9IjQwIiB4PSIwIiB5PSIwIi8+PC9zdmc+': 'const char',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiM2ZGNmZjYiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+Q29uc3Q8L3RleHQ+PHJlY3QgZmlsbD0ibm9uZSIgaGVpZ2h0PSI0MCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEuNiIgd2lkdGg9IjQwIiB4PSIwIiB5PSIwIi8+PC9zdmc+': 'const int',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiM4OGQxYzkiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+Q29uc3Q8L3RleHQ+PHJlY3QgZmlsbD0ibm9uZSIgaGVpZ2h0PSI0MCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEuNiIgd2lkdGg9IjQwIiB4PSIwIiB5PSIwIi8+PC9zdmc+': 'const number',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNhM2QzOWMiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+Q29uc3Q8L3RleHQ+PHJlY3QgZmlsbD0ibm9uZSIgaGVpZ2h0PSI0MCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEuNiIgd2lkdGg9IjQwIiB4PSIwIiB5PSIwIi8+PC9zdmc+': 'const real',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+Q29uc3Q8L3RleHQ+PHJlY3QgZmlsbD0ibm9uZSIgaGVpZ2h0PSI0MCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEuNiIgd2lkdGg9IjQwIiB4PSIwIiB5PSIwIi8+PC9zdmc+': 'const',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cGF0aCBkPSJNIDQwIDI2LjY2NjY2NjY2NjY2NjY2NCBBIDYuNjY2NjY2NjY2NjY2NjY2IDYuNjY2NjY2NjY2NjY2NjY2IDAgMCAxIDQwIDEzLjMzMzMzMzMzMzMzMzMzNCIgZmlsbD0iI2ZmZjc5OSIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPkNvbnN0PC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'const char ctrl',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjNmRjZmY2IiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPkNvbnN0PC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'const int ctrl',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjODhkMWM5IiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPkNvbnN0PC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'const number ctrl',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjYTNkMzljIiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPkNvbnN0PC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'const real ctrl',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjYmZiZmJmIiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPkNvbnN0PC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'const ctrl',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI4MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA4MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iODAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iIzZkY2ZmNiIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iMCw1My4zMzMzMzMzMzMzMzMzMyA2LjY2NjY2NjY2NjY2NjY2Niw2MC4wIDAsNjYuNjY2NjY2NjY2NjY2NjcgMCw1My4zMzMzMzMzMzMzMzMzMyIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjYzQ3MTc5IiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiM2ZGNmZjYiIHBvaW50cz0iNDAsNTMuMzMzMzMzMzMzMzMzMzMgMzMuMzMzMzMzMzMzMzMzMzM2LDYwLjAgNDAsNjYuNjY2NjY2NjY2NjY2NjcgNDAsNTMuMzMzMzMzMzMzMzMzMzMiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+Q3RyPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iODAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'counter',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiM4OGQxYzkiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjODhkMWM5IiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPkRlYzwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'dec',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iIzZkY2ZmNiIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+RGVsYXk8L3RleHQ+PHJlY3QgZmlsbD0ibm9uZSIgaGVpZ2h0PSI0MCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEuNiIgd2lkdGg9IjQwIiB4PSIwIiB5PSIwIi8+PC9zdmc+': 'delay',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiM4OGQxYzkiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iIzg4ZDFjOSIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiM2ZGNmZjYiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+Ly88L3RleHQ+PHJlY3QgZmlsbD0ibm9uZSIgaGVpZ2h0PSI0MCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEuNiIgd2lkdGg9IjQwIiB4PSIwIiB5PSIwIi8+PC9zdmc+': 'div',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiM4OGQxYzkiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iIzg4ZDFjOSIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiM4OGQxYzkiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+LzwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'divide number',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2JmYmZiZiIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+LzwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'divide',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48dGV4dCBzdHlsZT0iZm9udC1zaXplOjhweDsgZm9udC1mYW1pbHk6Q291cmllcjtmb250LXdlaWdodDpib2xkOyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjAiIHk9IjIyIj5FcnI8L3RleHQ+PHJlY3QgZmlsbD0ibm9uZSIgaGVpZ2h0PSI0MCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEuNiIgd2lkdGg9IjQwIiB4PSIwIiB5PSIwIi8+PC9zdmc+': 'error',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2JmYmZiZiIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNhMTg2YmUiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+YT1iPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'equal',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2Niw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwzMy4zMzMzMzMzMzMzMzMzMyAwLDMzLjMzMzMzMzMzMzMzMzMzIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2ExODZiZSIgcG9pbnRzPSI0MCwxMy4zMzMzMzMzMzMzMzMzMzYgMzMuMzMzMzMzMzMzMzMzMzM2LDIwLjAgNDAsMjYuNjY2NjY2NjY2NjY2NjY0IDQwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48dGV4dCBzdHlsZT0iZm9udC1zaXplOjhweDsgZm9udC1mYW1pbHk6Q291cmllcjtmb250LXdlaWdodDpib2xkOyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjAiIHk9IjIyIj49PC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'general equal',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiM4OGQxYzkiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iIzg4ZDFjOSIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiM4OGQxYzkiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+Kio8L3RleHQ+PHJlY3QgZmlsbD0ibm9uZSIgaGVpZ2h0PSI0MCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEuNiIgd2lkdGg9IjQwIiB4PSIwIiB5PSIwIi8+PC9zdmc+': 'exp number',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2JmYmZiZiIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+Kio8L3RleHQ+PHJlY3QgZmlsbD0ibm9uZSIgaGVpZ2h0PSI0MCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEuNiIgd2lkdGg9IjQwIiB4PSIwIiB5PSIwIi8+PC9zdmc+': 'exp',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI4MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA4MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iODAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iIzZkY2ZmNiIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiM2ZGNmZjYiIHBvaW50cz0iMCw1My4zMzMzMzMzMzMzMzMzMyA2LjY2NjY2NjY2NjY2NjY2Niw2MC4wIDAsNjYuNjY2NjY2NjY2NjY2NjcgMCw1My4zMzMzMzMzMzMzMzMzMyIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjYzQ3MTc5IiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiM2ZGNmZjYiIHBvaW50cz0iNDAsNTMuMzMzMzMzMzMzMzMzMzMgMzMuMzMzMzMzMzMzMzMzMzM2LDYwLjAgNDAsNjYuNjY2NjY2NjY2NjY2NjcgNDAsNTMuMzMzMzMzMzMzMzMzMzMiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+Rm9yPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iODAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'for int',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI4MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA4MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iODAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjNmRjZmY2IiBwb2ludHM9IjAsMjYuNjY2NjY2NjY2NjY2NjcgNi42NjY2NjY2NjY2NjY2NjYsMzMuMzMzMzMzMzMzMzMzMzM2IDAsNDAuMCAwLDI2LjY2NjY2NjY2NjY2NjY3IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiM2ZGNmZjYiIHBvaW50cz0iMCw0MC4wIDYuNjY2NjY2NjY2NjY2NjY2LDQ2LjY2NjY2NjY2NjY2NjY3IDAsNTMuMzMzMzMzMzMzMzMzMzQgMCw0MC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiM2ZGNmZjYiIHBvaW50cz0iMCw1My4zMzMzMzMzMzMzMzMzMyA2LjY2NjY2NjY2NjY2NjY2Niw2MC4wIDAsNjYuNjY2NjY2NjY2NjY2NjcgMCw1My4zMzMzMzMzMzMzMzMzMyIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjYzQ3MTc5IiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiM2ZGNmZjYiIHBvaW50cz0iNDAsNTMuMzMzMzMzMzMzMzMzMzMgMzMuMzMzMzMzMzMzMzMzMzM2LDYwLjAgNDAsNjYuNjY2NjY2NjY2NjY2NjcgNDAsNTMuMzMzMzMzMzMzMzMzMzMiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+Rm9yPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iODAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'for ext int',
    'PHN2ZyBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI4MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6ZXY9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEveG1sLWV2ZW50cyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHZpZXdCb3g9IjAgMCA0MCA4MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iODAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iIzg4ZDFjOSIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiM4OGQxYzkiIHBvaW50cz0iMCw1My4zMzMzMzMzMzMzMzMzMyA2LjY2NjY2NjY2NjY2NjY2Niw2MC4wIDAsNjYuNjY2NjY2NjY2NjY2NjcgMCw1My4zMzMzMzMzMzMzMzMzMyIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjYzQ3MTc5IiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiM4OGQxYzkiIHBvaW50cz0iNDAsNTMuMzMzMzMzMzMzMzMzMzMgMzMuMzMzMzMzMzMzMzMzMzM2LDYwLjAgNDAsNjYuNjY2NjY2NjY2NjY2NjcgNDAsNTMuMzMzMzMzMzMzMzMzMzMiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+Rm9yPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iODAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'for number',
    'PHN2ZyBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI4MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6ZXY9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEveG1sLWV2ZW50cyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHZpZXdCb3g9IjAgMCA0MCA4MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iODAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjODhkMWM5IiBwb2ludHM9IjAsMjYuNjY2NjY2NjY2NjY2NjcgNi42NjY2NjY2NjY2NjY2NjYsMzMuMzMzMzMzMzMzMzMzMzM2IDAsNDAuMCAwLDI2LjY2NjY2NjY2NjY2NjY3IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiM4OGQxYzkiIHBvaW50cz0iMCw0MC4wIDYuNjY2NjY2NjY2NjY2NjY2LDQ2LjY2NjY2NjY2NjY2NjY3IDAsNTMuMzMzMzMzMzMzMzMzMzQgMCw0MC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiM4OGQxYzkiIHBvaW50cz0iMCw1My4zMzMzMzMzMzMzMzMzMyA2LjY2NjY2NjY2NjY2NjY2Niw2MC4wIDAsNjYuNjY2NjY2NjY2NjY2NjcgMCw1My4zMzMzMzMzMzMzMzMzMyIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjYzQ3MTc5IiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiM4OGQxYzkiIHBvaW50cz0iNDAsNTMuMzMzMzMzMzMzMzMzMzMgMzMuMzMzMzMzMzMzMzMzMzM2LDYwLjAgNDAsNjYuNjY2NjY2NjY2NjY2NjcgNDAsNTMuMzMzMzMzMzMzMzMzMzMiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+Rm9yPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iODAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'for ext number',
    'PHN2ZyBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI4MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6ZXY9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEveG1sLWV2ZW50cyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHZpZXdCb3g9IjAgMCA0MCA4MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iODAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2EzZDM5YyIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNhM2QzOWMiIHBvaW50cz0iMCw1My4zMzMzMzMzMzMzMzMzMyA2LjY2NjY2NjY2NjY2NjY2Niw2MC4wIDAsNjYuNjY2NjY2NjY2NjY2NjcgMCw1My4zMzMzMzMzMzMzMzMzMyIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjYzQ3MTc5IiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNhM2QzOWMiIHBvaW50cz0iNDAsNTMuMzMzMzMzMzMzMzMzMzMgMzMuMzMzMzMzMzMzMzMzMzM2LDYwLjAgNDAsNjYuNjY2NjY2NjY2NjY2NjcgNDAsNTMuMzMzMzMzMzMzMzMzMzMiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+Rm9yPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iODAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'for real',
    'PHN2ZyBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI4MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6ZXY9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEveG1sLWV2ZW50cyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHZpZXdCb3g9IjAgMCA0MCA4MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iODAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjYTNkMzljIiBwb2ludHM9IjAsMjYuNjY2NjY2NjY2NjY2NjcgNi42NjY2NjY2NjY2NjY2NjYsMzMuMzMzMzMzMzMzMzMzMzM2IDAsNDAuMCAwLDI2LjY2NjY2NjY2NjY2NjY3IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNhM2QzOWMiIHBvaW50cz0iMCw0MC4wIDYuNjY2NjY2NjY2NjY2NjY2LDQ2LjY2NjY2NjY2NjY2NjY3IDAsNTMuMzMzMzMzMzMzMzMzMzQgMCw0MC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNhM2QzOWMiIHBvaW50cz0iMCw1My4zMzMzMzMzMzMzMzMzMyA2LjY2NjY2NjY2NjY2NjY2Niw2MC4wIDAsNjYuNjY2NjY2NjY2NjY2NjcgMCw1My4zMzMzMzMzMzMzMzMzMyIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjYzQ3MTc5IiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNhM2QzOWMiIHBvaW50cz0iNDAsNTMuMzMzMzMzMzMzMzMzMzMgMzMuMzMzMzMzMzMzMzMzMzM2LDYwLjAgNDAsNjYuNjY2NjY2NjY2NjY2NjcgNDAsNTMuMzMzMzMzMzMzMzMzMzMiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+Rm9yPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iODAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'for ext real',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI4MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA4MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iODAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBhdGggZD0iTSAwIDIwLjAgQSA2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiAwIDAgMSAwIDMzLjMzMzMzMzMzMzMzMzMzIiBmaWxsPSIjZjY5Njc5IiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2M0NzE3OSIgcG9pbnRzPSIwLDUzLjMzMzMzMzMzMzMzMzMzIDYuNjY2NjY2NjY2NjY2NjY2LDYwLjAgMCw2Ni42NjY2NjY2NjY2NjY2NyAwLDUzLjMzMzMzMzMzMzMzMzMzIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBhdGggZD0iTSA0MCA2Ni42NjY2NjY2NjY2NjY2NyBBIDYuNjY2NjY2NjY2NjY2NjY2IDYuNjY2NjY2NjY2NjY2NjY2IDAgMCAxIDQwIDUzLjMzMzMzMzMzMzMzMzMzNiIgZmlsbD0iI2Y2OTY3OSIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPkZvcjwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjgwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'for var',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI4MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA4MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iODAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwzMy4zMzMzMzMzMzMzMzMzMyAwLDMzLjMzMzMzMzMzMzMzMzMzIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2M0NzE3OSIgcG9pbnRzPSIwLDUzLjMzMzMzMzMzMzMzMzMzIDYuNjY2NjY2NjY2NjY2NjY2LDYwLjAgMCw2Ni42NjY2NjY2NjY2NjY2NyAwLDUzLjMzMzMzMzMzMzMzMzMzIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2JmYmZiZiIgcG9pbnRzPSI0MCw1My4zMzMzMzMzMzMzMzMzMyAzMy4zMzMzMzMzMzMzMzMzMzYsNjAuMCA0MCw2Ni42NjY2NjY2NjY2NjY2NyA0MCw1My4zMzMzMzMzMzMzMzMzMyIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48dGV4dCBzdHlsZT0iZm9udC1zaXplOjhweDsgZm9udC1mYW1pbHk6Q291cmllcjtmb250LXdlaWdodDpib2xkOyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjAiIHk9IjIyIj5Gb3I8L3RleHQ+PHJlY3QgZmlsbD0ibm9uZSIgaGVpZ2h0PSI4MCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEuNiIgd2lkdGg9IjQwIiB4PSIwIiB5PSIwIi8+PC9zdmc+': 'foreach',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2JmYmZiZiIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNhMTg2YmUiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+YSZndDtiPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'greater',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2JmYmZiZiIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNhMTg2YmUiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+YSZndDs9YjwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'greater or equal',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2ExODZiZSIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iNDAsNi42NjY2NjY2NjY2NjY2NjYgMzMuMzMzMzMzMzMzMzMzMzM2LDEzLjMzMzMzMzMzMzMzMzMzMiA0MCwyMC4wIDQwLDYuNjY2NjY2NjY2NjY2NjY2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iNDAsMjAuMCAzMy4zMzMzMzMzMzMzMzMzMzYsMjYuNjY2NjY2NjY2NjY2NjY0IDQwLDMzLjMzMzMzMzMzMzMzMzMzIDQwLDIwLjAiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+SWY8L3RleHQ+PHJlY3QgZmlsbD0ibm9uZSIgaGVpZ2h0PSI0MCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEuNiIgd2lkdGg9IjQwIiB4PSIwIiB5PSIwIi8+PC9zdmc+': 'if',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2Niw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwyMC4wIDAsMjAuMCAwLDYuNjY2NjY2NjY2NjY2NjY2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCwyMC4wIDYuNjY2NjY2NjY2NjY2NjY2LDI2LjY2NjY2NjY2NjY2NjY2NCAwLDMzLjMzMzMzMzMzMzMzMzMzIDAsMjAuMCIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjYTE4NmJlIiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPkluPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'in',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiM4OGQxYzkiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjODhkMWM5IiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPkluYzwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'inc',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjYmZiZmJmIiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPklucHV0PC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'input',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjZmZmNzk5IiBwb2ludHM9IjQwLDYuNjY2NjY2NjY2NjY2NjY2IDMzLjMzMzMzMzMzMzMzMzMzNiwzMy4zMzMzMzMzMzMzMzMzMyA0MCwzMy4zMzMzMzMzMzMzMzMzMyA0MCw2LjY2NjY2NjY2NjY2NjY2NiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48dGV4dCBzdHlsZT0iZm9udC1zaXplOjhweDsgZm9udC1mYW1pbHk6Q291cmllcjtmb250LXdlaWdodDpib2xkOyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjAiIHk9IjIyIj5JbnB1dDwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'input string',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiM4OGQxYzkiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjNmRjZmY2IiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPkludDwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'int',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiM4OGQxYzkiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjODhkMWM5IiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPkludjwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'inv',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2JmYmZiZiIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNhMTg2YmUiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+YSZsdDtiPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'less',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2JmYmZiZiIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNhMTg2YmUiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+YSZsdDs9YjwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'less or equal',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwYXRoIGQ9Ik0gMCA2LjY2NjY2NjY2NjY2NjY2NiBBIDYuNjY2NjY2NjY2NjY2NjY2IDYuNjY2NjY2NjY2NjY2NjY2IDAgMCAxIDAgMjAuMCIgZmlsbD0iI2Y2OTY3OSIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwYXRoIGQ9Ik0gMCAyMC4wIEEgNi42NjY2NjY2NjY2NjY2NjYgNi42NjY2NjY2NjY2NjY2NjYgMCAwIDEgMCAzMy4zMzMzMzMzMzMzMzMzMyIgZmlsbD0iI2Y2OTY3OSIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iNDAsNi42NjY2NjY2NjY2NjY2NjYgMzMuMzMzMzMzMzMzMzMzMzM2LDYuNjY2NjY2NjY2NjY2NjY2IDMzLjMzMzMzMzMzMzMzMzMzNiwzMy4zMzMzMzMzMzMzMzMzMyA0MCwzMy4zMzMzMzMzMzMzMzMzMyA0MCw2LjY2NjY2NjY2NjY2NjY2NiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48dGV4dCBzdHlsZT0iZm9udC1zaXplOjhweDsgZm9udC1mYW1pbHk6Q291cmllcjtmb250LXdlaWdodDpib2xkOyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjAiIHk9IjIyIj5NYXA8L3RleHQ+PHJlY3QgZmlsbD0ibm9uZSIgaGVpZ2h0PSI0MCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEuNiIgd2lkdGg9IjQwIiB4PSIwIiB5PSIwIi8+PC9zdmc+': 'map',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI4MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA4MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iODAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2Niw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwzMy4zMzMzMzMzMzMzMzMzMyAwLDMzLjMzMzMzMzMzMzMzMzMzIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2JmYmZiZiIgcG9pbnRzPSIwLDUzLjMzMzMzMzMzMzMzMzMzIDYuNjY2NjY2NjY2NjY2NjY2LDYwLjAgMCw2Ni42NjY2NjY2NjY2NjY2NyAwLDUzLjMzMzMzMzMzMzMzMzMzIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPkVyYXNlPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iODAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'map erase',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI4MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA4MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iODAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2Niw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwzMy4zMzMzMzMzMzMzMzMzMyAwLDMzLjMzMzMzMzMzMzMzMzMzIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2JmYmZiZiIgcG9pbnRzPSIwLDQ2LjY2NjY2NjY2NjY2NjY2IDYuNjY2NjY2NjY2NjY2NjY2LDUzLjMzMzMzMzMzMzMzMzMzIDAsNjAuMCAwLDQ2LjY2NjY2NjY2NjY2NjY2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCw1OS45OTk5OTk5OTk5OTk5OSA2LjY2NjY2NjY2NjY2NjY2Niw2Ni42NjY2NjY2NjY2NjY2NiAwLDczLjMzMzMzMzMzMzMzMzMzIDAsNTkuOTk5OTk5OTk5OTk5OTkiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2JmYmZiZiIgcG9pbnRzPSI0MCw2LjY2NjY2NjY2NjY2NjY2NiAzMy4zMzMzMzMzMzMzMzMzMzYsNi42NjY2NjY2NjY2NjY2NjYgMzMuMzMzMzMzMzMzMzMzMzM2LDMzLjMzMzMzMzMzMzMzMzMzIDQwLDMzLjMzMzMzMzMzMzMzMzMzIDQwLDYuNjY2NjY2NjY2NjY2NjY2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iNDAsNTMuMzMzMzMzMzMzMzMzMzMgMzMuMzMzMzMzMzMzMzMzMzM2LDYwLjAgNDAsNjYuNjY2NjY2NjY2NjY2NjcgNDAsNTMuMzMzMzMzMzMzMzMzMzMiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+SS9GPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iODAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'map if',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2Niw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwzMy4zMzMzMzMzMzMzMzMzMyAwLDMzLjMzMzMzMzMzMzMzMzMzIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2JmYmZiZiIgcG9pbnRzPSI0MCw2LjY2NjY2NjY2NjY2NjY2NiAzMy4zMzMzMzMzMzMzMzMzMzYsMzMuMzMzMzMzMzMzMzMzMzMgNDAsMzMuMzMzMzMzMzMzMzMzMzMgNDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+S2V5czwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'map keys',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2Niw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwzMy4zMzMzMzMzMzMzMzMzMyAwLDMzLjMzMzMzMzMzMzMzMzMzIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iIzZkY2ZmNiIgcG9pbnRzPSI0MCwxMy4zMzMzMzMzMzMzMzMzMzYgMzMuMzMzMzMzMzMzMzMzMzM2LDIwLjAgNDAsMjYuNjY2NjY2NjY2NjY2NjY0IDQwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48dGV4dCBzdHlsZT0iZm9udC1zaXplOjhweDsgZm9udC1mYW1pbHk6Q291cmllcjtmb250LXdlaWdodDpib2xkOyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjAiIHk9IjIyIj5MZW48L3RleHQ+PHJlY3QgZmlsbD0ibm9uZSIgaGVpZ2h0PSI0MCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEuNiIgd2lkdGg9IjQwIiB4PSIwIiB5PSIwIi8+PC9zdmc+': 'len',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2JmYmZiZiIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+TWVyZ2U8L3RleHQ+PHJlY3QgZmlsbD0ibm9uZSIgaGVpZ2h0PSI0MCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEuNiIgd2lkdGg9IjQwIiB4PSIwIiB5PSIwIi8+PC9zdmc+': 'merge',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNmZmY3OTkiIHBvaW50cz0iNDAsNi42NjY2NjY2NjY2NjY2NjYgMzMuMzMzMzMzMzMzMzMzMzM2LDMzLjMzMzMzMzMzMzMzMzMzIDQwLDMzLjMzMzMzMzMzMzMzMzMzIDQwLDYuNjY2NjY2NjY2NjY2NjY2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPk1zZzwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'message',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiM4OGQxYzkiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iIzg4ZDFjOSIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiM4OGQxYzkiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+JTwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'mod',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwYXRoIGQ9Ik0gMCA2LjY2NjY2NjY2NjY2NjY2NiBBIDYuNjY2NjY2NjY2NjY2NjY2IDYuNjY2NjY2NjY2NjY2NjY2IDAgMCAxIDAgMjAuMCIgZmlsbD0iI2ZmZjc5OSIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiM2ZGNmZjYiIHBvaW50cz0iMCwyMC4wIDYuNjY2NjY2NjY2NjY2NjY2LDI2LjY2NjY2NjY2NjY2NjY2NCAwLDMzLjMzMzMzMzMzMzMzMzMzIDAsMjAuMCIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjZmZmNzk5IiBwb2ludHM9IjQwLDYuNjY2NjY2NjY2NjY2NjY2IDMzLjMzMzMzMzMzMzMzMzMzNiwzMy4zMzMzMzMzMzMzMzMzMyA0MCwzMy4zMzMzMzMzMzMzMzMzMyA0MCw2LjY2NjY2NjY2NjY2NjY2NiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48dGV4dCBzdHlsZT0iZm9udC1zaXplOjhweDsgZm9udC1mYW1pbHk6Q291cmllcjtmb250LXdlaWdodDpib2xkOyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjAiIHk9IjIyIj4qPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'mult char',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiM2ZGNmZjYiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2Niw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwzMy4zMzMzMzMzMzMzMzMzMyAwLDMzLjMzMzMzMzMzMzMzMzMzIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iIzZkY2ZmNiIgcG9pbnRzPSI0MCwxMy4zMzMzMzMzMzMzMzMzMzYgMzMuMzMzMzMzMzMzMzMzMzM2LDIwLjAgNDAsMjYuNjY2NjY2NjY2NjY2NjY0IDQwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48dGV4dCBzdHlsZT0iZm9udC1zaXplOjhweDsgZm9udC1mYW1pbHk6Q291cmllcjtmb250LXdlaWdodDpib2xkOyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjAiIHk9IjIyIj4qPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'mult int',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiM4OGQxYzkiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2Niw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwzMy4zMzMzMzMzMzMzMzMzMyAwLDMzLjMzMzMzMzMzMzMzMzMzIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iIzg4ZDFjOSIgcG9pbnRzPSI0MCwxMy4zMzMzMzMzMzMzMzMzMzYgMzMuMzMzMzMzMzMzMzMzMzM2LDIwLjAgNDAsMjYuNjY2NjY2NjY2NjY2NjY0IDQwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48dGV4dCBzdHlsZT0iZm9udC1zaXplOjhweDsgZm9udC1mYW1pbHk6Q291cmllcjtmb250LXdlaWdodDpib2xkOyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjAiIHk9IjIyIj4qPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'mult number',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNhM2QzOWMiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2Niw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwzMy4zMzMzMzMzMzMzMzMzMyAwLDMzLjMzMzMzMzMzMzMzMzMzIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2EzZDM5YyIgcG9pbnRzPSI0MCwxMy4zMzMzMzMzMzMzMzMzMzYgMzMuMzMzMzMzMzMzMzMzMzM2LDIwLjAgNDAsMjYuNjY2NjY2NjY2NjY2NjY0IDQwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48dGV4dCBzdHlsZT0iZm9udC1zaXplOjhweDsgZm9udC1mYW1pbHk6Q291cmllcjtmb250LXdlaWdodDpib2xkOyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjAiIHk9IjIyIj4qPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'mult real',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2JmYmZiZiIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+KjwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'mult',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNhMTg2YmUiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjYTE4NmJlIiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPk5vdDwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'not',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2JmYmZiZiIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNhMTg2YmUiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+YSE9YjwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'not equal',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNhMTg2YmUiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2ExODZiZSIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNhMTg2YmUiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+fDwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'or',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNhMTg2YmUiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2Niw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwzMy4zMzMzMzMzMzMzMzMzMyAwLDMzLjMzMzMzMzMzMzMzMzMzIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2ExODZiZSIgcG9pbnRzPSI0MCwxMy4zMzMzMzMzMzMzMzMzMzYgMzMuMzMzMzMzMzMzMzMzMzM2LDIwLjAgNDAsMjYuNjY2NjY2NjY2NjY2NjY0IDQwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48dGV4dCBzdHlsZT0iZm9udC1zaXplOjhweDsgZm9udC1mYW1pbHk6Q291cmllcjtmb250LXdlaWdodDpib2xkOyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjAiIHk9IjIyIj58PC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'general or',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48dGV4dCBzdHlsZT0iZm9udC1zaXplOjhweDsgZm9udC1mYW1pbHk6Q291cmllcjtmb250LXdlaWdodDpib2xkOyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjAiIHk9IjIyIj5QcmludDwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'print',
    'PHN2ZyBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6ZXY9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEveG1sLWV2ZW50cyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjYzQ3MTc5IiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPlByaW50PC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'print ctrl',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNmZmY3OTkiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwzMy4zMzMzMzMzMzMzMzMzMyAwLDMzLjMzMzMzMzMzMzMzMzMzIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+UHJpbnQ8L3RleHQ+PHJlY3QgZmlsbD0ibm9uZSIgaGVpZ2h0PSI0MCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEuNiIgd2lkdGg9IjQwIiB4PSIwIiB5PSIwIi8+PC9zdmc+': 'print string',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiM4OGQxYzkiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iIzZkY2ZmNiIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiM4OGQxYzkiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+Um91bmQ8L3RleHQ+PHJlY3QgZmlsbD0ibm9uZSIgaGVpZ2h0PSI0MCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEuNiIgd2lkdGg9IjQwIiB4PSIwIiB5PSIwIi8+PC9zdmc+': 'round',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+UnVuPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'run',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48dGV4dCBzdHlsZT0iZm9udC1zaXplOjhweDsgZm9udC1mYW1pbHk6Q291cmllcjtmb250LXdlaWdodDpib2xkOyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjAiIHk9IjIyIj5TdG9wPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'stop',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiM2ZGNmZjYiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iIzZkY2ZmNiIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiM2ZGNmZjYiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+LTwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'sub int',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiM4OGQxYzkiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iIzg4ZDFjOSIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiM4OGQxYzkiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+LTwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'sub number',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNhM2QzOWMiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2EzZDM5YyIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNhM2QzOWMiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+LTwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'sub real',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2JmYmZiZiIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+LTwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'sub',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2M0NzE3OSIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiM2ZGNmZjYiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+VGltZXI8L3RleHQ+PHJlY3QgZmlsbD0ibm9uZSIgaGVpZ2h0PSI0MCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEuNiIgd2lkdGg9IjQwIiB4PSIwIiB5PSIwIi8+PC9zdmc+': 'timer',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cGF0aCBkPSJNIDQwIDI2LjY2NjY2NjY2NjY2NjY2NCBBIDYuNjY2NjY2NjY2NjY2NjY2IDYuNjY2NjY2NjY2NjY2NjY2IDAgMCAxIDQwIDEzLjMzMzMzMzMzMzMzMzMzNCIgZmlsbD0iI2Y2OTY3OSIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPlR5cGU8L3RleHQ+PHJlY3QgZmlsbD0ibm9uZSIgaGVpZ2h0PSI0MCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEuNiIgd2lkdGg9IjQwIiB4PSIwIiB5PSIwIi8+PC9zdmc+': 'type',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwYXRoIGQ9Ik0gNDAgMjAuMCBBIDYuNjY2NjY2NjY2NjY2NjY2IDYuNjY2NjY2NjY2NjY2NjY2IDAgMCAxIDQwIDYuNjY2NjY2NjY2NjY2NjY2IiBmaWxsPSIjZjY5Njc5IiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2JmYmZiZiIgcG9pbnRzPSI0MCwyMC4wIDMzLjMzMzMzMzMzMzMzMzMzNiwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMzMuMzMzMzMzMzMzMzMzMzMgNDAsMjAuMCIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48dGV4dCBzdHlsZT0iZm9udC1zaXplOjhweDsgZm9udC1mYW1pbHk6Q291cmllcjtmb250LXdlaWdodDpib2xkOyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjAiIHk9IjIyIj5UPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 't',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwYXRoIGQ9Ik0gMCAxMy4zMzMzMzMzMzMzMzMzMzQgQSA2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiAwIDAgMSAwIDI2LjY2NjY2NjY2NjY2NjY2NCIgZmlsbD0iI2ZmZjc5OSIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwYXRoIGQ9Ik0gNDAgMjYuNjY2NjY2NjY2NjY2NjY0IEEgNi42NjY2NjY2NjY2NjY2NjYgNi42NjY2NjY2NjY2NjY2NjYgMCAwIDEgNDAgMTMuMzMzMzMzMzMzMzMzMzM0IiBmaWxsPSIjZmZmNzk5IiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+VmFyPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'var char',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiM2ZGNmZjYiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjNmRjZmY2IiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPlZhcjwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'var int',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiM4OGQxYzkiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjODhkMWM5IiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPlZhcjwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'var number',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNhM2QzOWMiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjYTNkMzljIiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPlZhcjwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'var real',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjYmZiZmJmIiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPlZhcjwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'var',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2Niw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwzMy4zMzMzMzMzMzMzMzMzMyAwLDMzLjMzMzMzMzMzMzMzMzMzIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2M0NzE3OSIgcG9pbnRzPSI0MCwxMy4zMzMzMzMzMzMzMzMzMzYgMzMuMzMzMzMzMzMzMzMzMzM2LDIwLjAgNDAsMjYuNjY2NjY2NjY2NjY2NjY0IDQwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48dGV4dCBzdHlsZT0iZm9udC1zaXplOjhweDsgZm9udC1mYW1pbHk6Q291cmllcjtmb250LXdlaWdodDpib2xkOyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjAiIHk9IjIyIj5XYWl0PC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'wait',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI4MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA4MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iODAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNjNDcxNzkiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjYTE4NmJlIiBwb2ludHM9IjAsNTMuMzMzMzMzMzMzMzMzMzMgNi42NjY2NjY2NjY2NjY2NjYsNjAuMCAwLDY2LjY2NjY2NjY2NjY2NjY3IDAsNTMuMzMzMzMzMzMzMzMzMzMiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2M0NzE3OSIgcG9pbnRzPSI0MCwxMy4zMzMzMzMzMzMzMzMzMzYgMzMuMzMzMzMzMzMzMzMzMzM2LDIwLjAgNDAsMjYuNjY2NjY2NjY2NjY2NjY0IDQwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjYzQ3MTc5IiBwb2ludHM9IjQwLDUzLjMzMzMzMzMzMzMzMzMzIDMzLjMzMzMzMzMzMzMzMzMzNiw2MC4wIDQwLDY2LjY2NjY2NjY2NjY2NjY3IDQwLDUzLjMzMzMzMzMzMzMzMzMzIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPldoaWxlPC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iODAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'while',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNhMTg2YmUiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwxMy4zMzMzMzMzMzMzMzMzMzIgMCwyMC4wIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2ExODZiZSIgcG9pbnRzPSIwLDIwLjAgNi42NjY2NjY2NjY2NjY2NjYsMjYuNjY2NjY2NjY2NjY2NjY0IDAsMzMuMzMzMzMzMzMzMzMzMzMgMCwyMC4wIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjxwb2x5Z29uIGZpbGw9IiNhMTg2YmUiIHBvaW50cz0iNDAsMTMuMzMzMzMzMzMzMzMzMzM2IDMzLjMzMzMzMzMzMzMzMzMzNiwyMC4wIDQwLDI2LjY2NjY2NjY2NjY2NjY2NCA0MCwxMy4zMzMzMzMzMzMzMzMzMzYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHRleHQgc3R5bGU9ImZvbnQtc2l6ZTo4cHg7IGZvbnQtZmFtaWx5OkNvdXJpZXI7Zm9udC13ZWlnaHQ6Ym9sZDsiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIwIiB5PSIyMiI+XjwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'xor',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNhMTg2YmUiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2Niw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwzMy4zMzMzMzMzMzMzMzMzMyAwLDMzLjMzMzMzMzMzMzMzMzMzIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2ExODZiZSIgcG9pbnRzPSI0MCwxMy4zMzMzMzMzMzMzMzMzMzYgMzMuMzMzMzMzMzMzMzMzMzM2LDIwLjAgNDAsMjYuNjY2NjY2NjY2NjY2NjY0IDQwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48dGV4dCBzdHlsZT0iZm9udC1zaXplOjhweDsgZm9udC1mYW1pbHk6Q291cmllcjtmb250LXdlaWdodDpib2xkOyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjAiIHk9IjIyIj5ePC90ZXh0PjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxLjYiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjwvc3ZnPg==': 'general xor',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCwxMy4zMzMzMzMzMzMzMzMzMzYgNi42NjY2NjY2NjY2NjY2NjYsMjAuMCAwLDI2LjY2NjY2NjY2NjY2NjY2NCAwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48cG9seWdvbiBmaWxsPSIjYzQ3MTc5IiBwb2ludHM9IjQwLDEzLjMzMzMzMzMzMzMzMzMzNiAzMy4zMzMzMzMzMzMzMzMzMzYsMjAuMCA0MCwyNi42NjY2NjY2NjY2NjY2NjQgNDAsMTMuMzMzMzMzMzMzMzMzMzM2IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjAuOCIvPjx0ZXh0IHN0eWxlPSJmb250LXNpemU6OHB4OyBmb250LWZhbWlseTpDb3VyaWVyO2ZvbnQtd2VpZ2h0OmJvbGQ7IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMCIgeT0iMjIiPkN0cmw8L3RleHQ+PHJlY3QgZmlsbD0ibm9uZSIgaGVpZ2h0PSI0MCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEuNiIgd2lkdGg9IjQwIiB4PSIwIiB5PSIwIi8+PC9zdmc+': 'ctrl',
    'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmV2PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL3htbC1ldmVudHMiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBiYXNlUHJvZmlsZT0iZnVsbCIgaGVpZ2h0PSI0MCIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PGRlZnMvPjxyZWN0IGZpbGw9IiNmZmZmZmYiIGhlaWdodD0iNDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHdpZHRoPSI0MCIgeD0iMCIgeT0iMCIvPjxwb2x5Z29uIGZpbGw9IiNiZmJmYmYiIHBvaW50cz0iMCw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2Niw2LjY2NjY2NjY2NjY2NjY2NiA2LjY2NjY2NjY2NjY2NjY2NiwzMy4zMzMzMzMzMzMzMzMzMyAwLDMzLjMzMzMzMzMzMzMzMzMzIDAsNi42NjY2NjY2NjY2NjY2NjYiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMC44Ii8+PHBvbHlnb24gZmlsbD0iI2JmYmZiZiIgcG9pbnRzPSI0MCwxMy4zMzMzMzMzMzMzMzMzMzYgMzMuMzMzMzMzMzMzMzMzMzM2LDIwLjAgNDAsMjYuNjY2NjY2NjY2NjY2NjY0IDQwLDEzLjMzMzMzMzMzMzMzMzMzNiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjgiLz48dGV4dCBzdHlsZT0iZm9udC1zaXplOjhweDsgZm9udC1mYW1pbHk6Q291cmllcjtmb250LXdlaWdodDpib2xkOyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjAiIHk9IjIyIj4mZ3Q7LTwvdGV4dD48cmVjdCBmaWxsPSJub25lIiBoZWlnaHQ9IjQwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMS42IiB3aWR0aD0iNDAiIHg9IjAiIHk9IjAiLz48L3N2Zz4=': 'value switch'
}

# only node inputs, outputs and their types
cleared_nodes = {
    'abs': {
        'inputs': ('number', ),
        'outputs': ('number', ),
    },
    'add': {
        'inputs': ('mult', ),
        'outputs': ('any', ),
    },
    'add int': {
        'inputs': ('mult', ),
        'inputs_type': ('int', ),
        'outputs': ('int', ),
    },
    'add number': {
        'inputs': ('mult', ),
        'inputs_type': ('number', ),
        'outputs': ('number', ),
    },
    'add real': {
        'inputs': ('mult', ),
        'inputs_type': ('real', ),
        'outputs': ('real', ),
    },
    'and': {
        'inputs': ('bool', 'bool'),
        'outputs': ('bool', ),
    },
    'general and': {
        'inputs': ('mult', ),
        'inputs_type': ('bool', ),
        'outputs': ('bool', ),
    },
    'array': {
        'inputs': ('obj', 'int'),
        'outputs': ('dir_mult', ),
    },
    'array gs': {
        'inputs': ('dir_mult', 'sep', 'int', 'any'),
        'outputs': ('dir_mult', 'sep', 'any'),
    },
    'array len': {
        'inputs': ('dir_mult', ),
        'outputs': ('int', ),
    },
    'bool': {
        'inputs': ('any', ),
        'outputs': ('bool', ),
    },
    'char': {
        'inputs': ('any', ),
        'outputs': ('char', ),
    },
    'check ctrl': {
        'inputs': ('ctrl', ),
        'outputs': ('bool', ),
    },
    'concatenate': {
        'inputs': ('dir_mult', ),
        'inputs_type': ('char', ),
        'outputs': ('char', ),
    },
    'const char': {
        'inputs': (),
        'outputs': ('char', ),
    },
    'const char ctrl': {
        'inputs': ('ctrl', ),
        'outputs': ('char', ),
    },
    'const int': {
        'inputs': (),
        'outputs': ('int', ),
    },
    'const int ctrl': {
        'inputs': ('ctrl', ),
        'outputs': ('int', ),
    },
    'const number': {
        'inputs': (),
        'outputs': ('number', ),
    },
    'const number ctrl': {
        'inputs': ('ctrl', ),
        'outputs': ('number', ),
    },
    'const real': {
        'inputs': (),
        'outputs': ('real', ),
    },
    'const real ctrl': {
        'inputs': ('ctrl', ),
        'outputs': ('real', ),
    },
    'const': {
        'inputs': (),
        'outputs': ('any', ),
    },
    'const ctrl': {
        'inputs': ('ctrl', ),
        'outputs': ('any', ),
    },
    'counter': {
        'inputs': ('ctrl', 'int', 'sep', 'ctrl'),
        'outputs': ('ctrl', 'sep', 'int'),
    },
    'dec': {
        'inputs': ('number', ),
        'outputs': ('number', ),
    },
    'delay': {
        'inputs': ('ctrl', 'int'),
        'outputs': ('ctrl', ),
    },
    'div': {
        'inputs': ('number', 'number'),
        'outputs': ('int', ),
    },
    'divide number': {
        'inputs': ('number', 'number'),
        'outputs': ('number', ),
    },
    'divide': {
        'inputs': ('any', 'any'),
        'outputs': ('any', ),
    },
    'general equal': {
        'inputs': ('mult', ),
        'outputs': ('bool', ),
    },
    'equal': {
        'inputs': ('any', 'any'),
        'outputs': ('bool', ),
    },
    'error': {
        'inputs': ('ctrl', ),
        'outputs': (),
    },
    'exp number': {
        'inputs': ('number', 'number'),
        'outputs': ('number', ),
    },
    'exp': {
        'inputs': ('any', 'any'),
        'outputs': ('any', ),
    },
    'for int': {
        'inputs': ('ctrl', 'int', 'sep', 'int'),
        'outputs': ('ctrl', 'sep', 'int'),
    },
    'for ext int': {
        'inputs': ('ctrl', 'int', 'int', 'int'),
        'outputs': ('ctrl', 'sep', 'int'),
    },
    'for ext number': {
        'inputs': ('ctrl', 'number', 'number', 'number'),
        'outputs': ('ctrl', 'sep', 'number'),
    },
    'for ext real': {
        'inputs': ('ctrl', 'real', 'real', 'real'),
        'outputs': ('ctrl', 'sep', 'real'),
    },
    'for number': {
        'inputs': ('ctrl', 'number', 'sep', 'number'),
        'outputs': ('ctrl', 'sep', 'number'),
    },
    'for real': {
        'inputs': ('ctrl', 'real', 'sep', 'real'),
        'outputs': ('ctrl', 'sep', 'real'),
    },
    'foreach': {
        'inputs': ('dir_mult', 'sep', 'ctrl'),
        'outputs': ('ctrl', 'sep', 'any'),
    },
    't': {
        'inputs': (),
        'outputs': ('obj', 'any'),
    },
    'greater': {
        'inputs': ('any', 'any'),
        'outputs': ('bool', ),
    },
    'greater or equal': {
        'inputs': ('any', 'any'),
        'outputs': ('bool', ),
    },
    'if': {
        'inputs': ('ctrl', 'bool'),
        'outputs': ('ctrl', 'ctrl'),
    },
    'in': {
        'inputs': ('mult_s', 'any'),
        'outputs': ('bool', ),
    },
    'inc': {
        'inputs': ('number', ),
        'outputs': ('number', ),
    },
    'input': {
        'inputs': ('ctrl', ),
        'outputs': ('any', ),
    },
    'input string': {
        'inputs': ('ctrl', ),
        'outputs': ('dir_mult', ),
        'outputs_type': ('char', ),
    },
    'int': {
        'inputs': ('number', ),
        'outputs': ('int', ),
    },
    'inv': {
        'inputs': ('number', ),
        'outputs': ('number', ),
    },
    'less': {
        'inputs': ('any', 'any'),
        'outputs': ('bool', ),
    },
    'less or equal': {
        'inputs': ('any', 'any'),
        'outputs': ('bool', ),
    },
    'map': {
        'inputs': ('obj', 'obj'),
        'outputs': ('mult', ),
    },
    'map erase': {
        'inputs': ('mult', 'sep', 'any'),
        'outputs': (),
    },
    'map if': {
        'inputs': ('mult', 'sep', 'any', 'any'),
        'outputs': ('mult', 'sep', 'any'),
    },
    'map keys': {
        'inputs': ('mult', ),
        'outputs': ('dir_mult', ),
    },
    'len': {
        'inputs': ('mult', ),
        'outputs': ('int', ),
    },
    'merge': {
        'inputs': ('ctrl', 'any'),
        'outputs': ('any', ),
    },
    'message': {
        'inputs': ('any', ),
        'outputs': ('dir_mult', ),
        'outputs_type': ('char', ),
    },
    'mod': {
        'inputs': ('number', 'number'),
        'outputs': ('number', ),
    },
    'mult char': {
        'inputs': ('char', 'int'),
        'outputs': ('dir_mult', ),
        'outputs_type': ('char', ),
    },
    'mult int': {
        'inputs': ('mult', ),
        'inputs_type': ('int', ),
        'outputs': ('int', ),
    },
    'mult number': {
        'inputs': ('mult', ),
        'inputs_type': ('number', ),
        'outputs': ('number', ),
    },
    'mult real': {
        'inputs': ('mult', ),
        'inputs_type': ('real', ),
        'outputs': ('real', ),
    },
    'mult': {
        'inputs': ('any', 'any'),
        'outputs': ('any', ),
    },
    'not': {
        'inputs': ('bool', ),
        'outputs': ('bool', ),
    },
    'not equal': {
        'inputs': ('any', 'any'),
        'outputs': ('bool', ),
    },
    'or': {
        'inputs': ('bool', 'bool'),
        'outputs': ('bool', ),
    },
    'general or': {
        'inputs': ('mult', ),
        'inputs_type': ('bool', ),
        'outputs': ('bool', ),
    },
    'print': {
        'inputs': ('any', ),
        'outputs': (),
    },
    'print string': {
        'inputs': ('dir_mult', ),
        'inputs_type': ('char', ),
        'outputs': (),
    },
    'print ctrl': {
        'inputs': ('any', ),
        'outputs': ('ctrl', ),
    },
    'round': {
        'inputs': ('number', 'int'),
        'outputs': ('number', ),
    },
    'run': {
        'inputs': (),
        'outputs': ('ctrl', ),
    },
    'stop': {
        'inputs': ('ctrl', ),
        'outputs': (),
    },
    'sub int': {
        'inputs': ('int', 'int'),
        'outputs': ('int', ),
    },
    'sub number': {
        'inputs': ('number', 'number'),
        'outputs': ('number', ),
    },
    'sub real': {
        'inputs': ('real', 'real'),
        'outputs': ('real', ),
    },
    'sub': {
        'inputs': ('any', 'any'),
        'outputs': ('any', ),
    },
    'timer': {
        'inputs': ('ctrl', 'ctrl'),
        'outputs': ('int', ),
    },
    'ctrl': {
        'inputs': ('any', ),
        'outputs': ('ctrl', ),
    },
    'type': {
        'inputs': ('any', ),
        'outputs': ('obj', ),
    },
    'var char': {
        'inputs': ('char', ),
        'outputs': ('char', ),
    },
    'var int': {
        'inputs': ('int', ),
        'outputs': ('int', ),
    },
    'var number': {
        'inputs': ('number', ),
        'outputs': ('number', ),
    },
    'var real': {
        'inputs': ('real', ),
        'outputs': ('real', ),
    },
    'var': {
        'inputs': ('any', ),
        'outputs': ('any', ),
    },
    'wait': {
        'inputs': ('mult', ),
        'inputs_type': ('ctrl', ),
        'outputs': ('ctrl', ),
    },
    'while': {
        'inputs': ('ctrl', 'sep', 'bool'),
        'outputs': ('ctrl', 'sep', 'ctrl'),
    },
    'xor': {
        'inputs': ('bool', 'bool'),
        'outputs': ('bool', ),
    },
    'value switch': {
        'inputs': ('mult', ),
        'outputs': ('any', ),
    }
}
