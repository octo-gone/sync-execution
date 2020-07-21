nodes_info = {
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
        'inputs_label': ('number', ),
        'inputs_color': ('number', ),
        'outputs': ('number', ),
        'outputs_label': ('number', ),
        'inner': '+',
        'label': 'add number',
        'sync_name': 'add'
    },
    'and': {
        'inputs': ('mult', ),
        'inputs_label': ('values', ),
        'inputs_color': ('bool', ),
        'outputs': ('bool', ),
        'outputs_label': ('bool', ),
        'inner': '&',
        'label': 'and'
    },
    'array': {
        'inputs': ('obj', 'int'),
        'inputs_label': ('type', 'length'),
        'outputs': (),
        'outputs_label': (),
        'inner': 'Array',
        'label': 'array'
    },
    'array gs': {
        'inputs': ('int', 'any'),
        'inputs_label': ('index', 'set'),
        'outputs': ('any', ),
        'outputs_label': ('get', ),
        'inner': 'G/S',
        'label': 'array get and set',
        'sync_name': 'array gs'
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
    'concatenation': {
        'inputs': ('dir_mult_s', 'dir_mult_s',),
        'inputs_label': ('char', 'char'),
        'inputs_color': ('char', 'char'),
        'outputs': ('dir_mult_s', ),
        'outputs_label': ('string', ),
        'outputs_color': ('char', ),
        'inner': '+',
        'label': 'concatenation'
    },
    'const string': {
        'inputs': (),
        'inputs_label': (),
        'outputs': ('dir_mult_s', ),
        'outputs_label': ('string', ),
        'outputs_color': ('char', ),
        'inner': 'Const',
        'label': 'const string',
        'sync_name': 'const string'
    },
    'const string ctrl': {
        'inputs': ('ctrl', ),
        'inputs_label': ('ctrl', ),
        'outputs': ('dir_mult_s', ),
        'outputs_label': ('string', ),
        'outputs_color': ('char', ),
        'inner': 'Const',
        'label': 'const string with ctrl',
        'sync_name': 'const string ctrl'
    },
    'const char': {
        'inputs': (),
        'inputs_label': (),
        'outputs': ('char', ),
        'outputs_label': ('char', ),
        'inner': 'Const',
        'label': 'const char',
        'sync_name': 'const char'
    },
    'const char ctrl': {
        'inputs': ('ctrl', ),
        'inputs_label': ('ctrl', ),
        'outputs': ('char', ),
        'outputs_label': ('char', ),
        'inner': 'Const',
        'label': 'const char with ctrl',
        'sync_name': 'const char ctrl'
    },
    'const int': {
        'inputs': (),
        'inputs_label': (),
        'outputs': ('int', ),
        'outputs_label': ('int', ),
        'inner': 'Const',
        'label': 'const int',
        'sync_name': 'const int'
    },
    'const int ctrl': {
        'inputs': ('ctrl', ),
        'inputs_label': ('ctrl', ),
        'outputs': ('int', ),
        'outputs_label': ('int', ),
        'inner': 'Const',
        'label': 'const int with ctrl',
        'sync_name': 'const int ctrl'
    },
    'const number': {
        'inputs': (),
        'inputs_label': (),
        'outputs': ('number', ),
        'outputs_label': ('number', ),
        'inner': 'Const',
        'label': 'const number',
        'sync_name': 'const number'
    },
    'const number ctrl': {
        'inputs': ('ctrl', ),
        'inputs_label': ('ctrl', ),
        'outputs': ('number', ),
        'outputs_label': ('number', ),
        'inner': 'Const',
        'label': 'const number with ctrl',
        'sync_name': 'const number ctrl'
    },
    'const real': {
        'inputs': (),
        'inputs_label': (),
        'outputs': ('real', ),
        'outputs_label': ('real', ),
        'inner': 'Const',
        'label': 'const real',
        'sync_name': 'const real'
    },
    'const real ctrl': {
        'inputs': ('ctrl', ),
        'inputs_label': ('ctrl', ),
        'outputs': ('real', ),
        'outputs_label': ('real', ),
        'inner': 'Const',
        'label': 'const real with ctrl',
        'sync_name': 'const real ctrl'
    },
    'const': {
        'inputs': (),
        'inputs_label': (),
        'outputs': ('any', ),
        'outputs_label': ('any', ),
        'inner': 'Const',
        'label': 'constant',
        'sync_name': 'const'
    },
    'const ctrl': {
        'inputs': ('ctrl', ),
        'inputs_label': ('ctrl', ),
        'outputs': ('any', ),
        'outputs_label': ('any', ),
        'inner': 'Const',
        'label': 'constant with ctrl',
        'sync_name': 'const ctrl'
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
        'label': 'decrement',
        'sync_name': 'dec'
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
    'division': {
        'inputs': ('number', 'number'),
        'inputs_label': ('dividend', 'divider'),
        'outputs': ('number', ),
        'outputs_label': ('number', ),
        'inner': '/',
        'label': 'div number',
        'sync_name': 'division'
    },
    'equal': {
        'inputs': ('mult', ),
        'inputs_label': ('values', ),
        'outputs': ('bool', ),
        'outputs_label': ('bool', ),
        'inner': '=',
        'label': 'equal'
    },
    'error': {
        'inputs': ('ctrl', ),
        'inputs_label': ('ctrl', ),
        'outputs': (),
        'outputs_label': (),
        'inner': 'Err',
        'label': 'error message',
        'sync_name': 'error'
    },
    'exp': {
        'inputs': ('number', 'number'),
        'inputs_label': ('base', 'exponent'),
        'outputs': ('number', ),
        'outputs_label': ('number', ),
        'inner': '**',
        'label': 'exp number',
        'sync_name': 'exp'
    },
    'for int': {
        'inputs': ('ctrl', 'int', 'sep', 'int'),
        'inputs_label': ('ctrl', 'bound', 'increment'),
        'outputs': ('ctrl', 'sep', 'int'),
        'outputs_label': ('end ctrl', 'iteration'),
        'inner': 'For',
        'label': 'for',
        'sync_name': 'for int'
    },
    'for ext int': {
        'inputs': ('ctrl', 'int', 'int', 'int'),
        'inputs_label': ('ctrl', 'bound', 'start value', 'increment'),
        'outputs': ('ctrl', 'sep', 'int'),
        'outputs_label': ('end ctrl', 'iteration'),
        'inner': 'For',
        'label': 'for extended',
        'sync_name': 'for ext int'
    },
    'for ext number': {
        'inputs': ('ctrl', 'number', 'number', 'number'),
        'inputs_label': ('ctrl', 'bound', 'start value', 'increment'),
        'outputs': ('ctrl', 'sep', 'number'),
        'outputs_label': ('end ctrl', 'iteration'),
        'inner': 'For',
        'label': 'for extended number',
        'sync_name': 'for ext number'
    },
    'for number': {
        'inputs': ('ctrl', 'number', 'sep', 'number'),
        'inputs_label': ('ctrl', 'bound', 'increment'),
        'outputs': ('ctrl', 'sep', 'number'),
        'outputs_label': ('end ctrl', 'iteration'),
        'inner': 'For',
        'label': 'for number'
    },
    'foreach': {
        'inputs': ('mult', 'sep', 'ctrl'),
        'inputs_label': ('mult', 'next', ),
        'outputs': ('ctrl', 'sep', 'any', 'int'),
        'outputs_label': ('end ctrl', 'value', 'iteration'),
        'inner': 'For',
        'label': 'foreach'
    },
    'get type': {
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
        'label': 'contains',
        'sync_name': 'in'
    },
    'inc': {
        'inputs': ('number', ),
        'inputs_label': ('number', ),
        'outputs': ('number', ),
        'outputs_label': ('number', ),
        'inner': 'Inc',
        'label': 'increment',
        'sync_name': 'inc'
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
        'outputs': ('dir_mult_s', ),
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
        'label': 'inversion',
        'sync_name': 'inv'
    },
    'len': {
        'inputs': (),
        'inputs_label': (),
        'outputs': ('int', ),
        'outputs_label': ('length', ),
        'inner': 'Len',
        'label': 'len'
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
        'outputs': (),
        'outputs_label': (),
        'inner': 'Map',
        'label': 'map'
    },
    'map erase': {
        'inputs': ('any', ),
        'inputs_label': ('key', ),
        'outputs': (),
        'outputs_label': (),
        'inner': 'Erase',
        'label': 'map erase'
    },
    'map if': {
        'inputs': ('any', 'any'),
        'inputs_label': ('key', 'insert'),
        'outputs': ('any', ),
        'outputs_label': ('find', ),
        'inner': 'I/F',
        'label': 'map insert and find',
        'sync_name': 'map if'
    },
    'merge': {
        'inputs': ('ctrl', 'any'),
        'inputs_label': ('ctrl', 'any'),
        'outputs': ('any', ),
        'outputs_label': ('any', ),
        'inner': 'Merge',
        'label': 'merge ctrl',
        'sync_name': 'merge'
    },
    'mod': {
        'inputs': ('number', 'number'),
        'inputs_label': ('dividend', 'divider'),
        'outputs': ('number', ),
        'outputs_label': ('number', ),
        'inner': '%',
        'label': 'mod'
    },
    'mult': {
        'inputs': ('mult', ),
        'inputs_label': ('number', ),
        'inputs_color': ('number', ),
        'outputs': ('number', ),
        'outputs_label': ('number', ),
        'inner': '*',
        'label': 'mult number',
        'sync_name': 'mult'
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
        'inputs': ('mult', ),
        'inputs_label': ('values', ),
        'inputs_color': ('bool', ),
        'outputs': ('bool', ),
        'outputs_label': ('bool', ),
        'inner': '|',
        'label': 'or'
    },
    'print': {
        'inputs': ('any', ),
        'inputs_label': ('any', ),
        'outputs': (),
        'outputs_label': (),
        'inner': 'Print',
        'label': 'print'
    },
    'print ctrl': {
        'inputs': ('any', ),
        'inputs_label': ('any', ),
        'outputs': ('ctrl', ),
        'outputs_label': ('ctrl', ),
        'inner': 'Print',
        'label': 'print with ctrl',
        'sync_name': 'print ctrl'
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
    'sub': {
        'inputs': ('number', 'number'),
        'inputs_label': ('minuend', 'subtrahend'),
        'outputs': ('number', ),
        'outputs_label': ('number', ),
        'inner': '-',
        'label': 'sub'
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
        'label': 'to ctrl',
        'sync_name': 'ctrl'
    },
    'type': {
        'inputs': ('any', ),
        'inputs_label': ('any', ),
        'outputs': ('obj', ),
        'outputs_label': ('type', ),
        'inner': 'Type',
        'label': 'type'
    },
    'var string': {
        'inputs': ('dir_mult_s', ),
        'inputs_label': ('string', ),
        'inputs_color': ('char', ),
        'outputs': ('dir_mult_s', ),
        'outputs_label': ('string', ),
        'outputs_color': ('char', ),
        'inner': 'Var',
        'label': 'var string'
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
        'label': 'variable',
        'sync_name': 'var'
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
