nodes_info = {
    'array create': {
        'inputs': ('int', ),
        'inputs_label': ('len', ),
        'outputs': ('ctrl', ),
        'outputs_label': ('ctrl', ),
        'inner': 'Array',
        'label': 'array create'
    },
    'array set': {
        'inputs': ('int', 'any'),
        'inputs_label': ('index', 'value'),
        'outputs': ('ctrl', ),
        'outputs_label': ('ctrl', ),
        'inner': 'A-Set',
        'label': 'array set'
    },
    'array get': {
        'inputs': ('int', ),
        'inputs_label': ('index', ),
        'outputs': ('any', ),
        'outputs_label': ('value', ),
        'inner': 'A-Get',
        'label': 'array get'
    },
    'array get and set': {
        'inputs': ('int', 'any'),
        'inputs_label': ('index', 'value'),
        'outputs': ('any', ),
        'outputs_label': ('value', ),
        'inner': 'A-GS',
        'label': 'array get and set'
    },
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
        'inner': 'AND',
        'label': 'and'
    },
    'not and': {
        'inputs': ('mult', ),
        'inputs_label': ('values', ),
        'inputs_color': ('bool', ),
        'outputs': ('bool', ),
        'outputs_label': ('bool', ),
        'inner': 'NAND',
        'label': 'not and'
    },
    'bool': {
        'inputs': ('any', ),
        'inputs_label': ('any', ),
        'outputs': ('bool', ),
        'outputs_label': ('bool', ),
        'inner': 'Bool',
        'label': 'bool'
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
    'for ext': {
        'inputs': ('ctrl', 'number', 'number', 'number'),
        'inputs_label': ('ctrl', 'bound', 'start value', 'increment'),
        'outputs': ('ctrl', 'sep', 'number'),
        'outputs_label': ('end ctrl', 'iteration'),
        'inner': 'For',
        'label': 'for extended',
        'sync_name': 'for'
    },
    'for': {
        'inputs': ('ctrl', 'number', 'sep', 'number'),
        'inputs_label': ('ctrl', 'bound', 'increment'),
        'outputs': ('ctrl', 'sep', 'number'),
        'outputs_label': ('end ctrl', 'iteration'),
        'inner': 'For',
        'label': 'for'
    },
    'foreach': {
        'inputs': ('ctrl', 'mult_s', 'sep', 'ctrl'),
        'inputs_label': ('ctrl', 'values', 'next', ),
        'outputs': ('ctrl', 'sep', 'any'),
        'outputs_label': ('end ctrl', 'value'),
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
    'trunc': {
        'inputs': ('number', ),
        'inputs_label': ('number', ),
        'outputs': ('int', ),
        'outputs_label': ('int', ),
        'inner': 'Trunc',
        'label': 'trunc'
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
    'length': {
        'inputs': ('ctrl', ),
        'inputs_label': ('ctrl', ),
        'outputs': ('int', ),
        'outputs_label': ('int', ),
        'inner': 'Len',
        'label': 'length',
    },
    'list create': {
        'inputs': ('ctrl', ),
        'inputs_label': ('ctrl', ),
        'outputs': ('ctrl', ),
        'outputs_label': ('ctrl', ),
        'inner': 'List',
        'label': 'list create'
    },
    'list set': {
        'inputs': ('int', 'any'),
        'inputs_label': ('index', 'value'),
        'outputs': ('ctrl', ),
        'outputs_label': ('ctrl', ),
        'inner': 'L-Set',
        'label': 'list set'
    },
    'list get': {
        'inputs': ('int', ),
        'inputs_label': ('index', ),
        'outputs': ('any', ),
        'outputs_label': ('value', ),
        'inner': 'L-Get',
        'label': 'list get'
    },
    'list get and set': {
        'inputs': ('int', 'any'),
        'inputs_label': ('index', 'value'),
        'outputs': ('any', ),
        'outputs_label': ('value', ),
        'inner': 'L-GS',
        'label': 'list get and set'
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
        'inner': 'OR',
        'label': 'or'
    },
    'not or': {
        'inputs': ('mult', ),
        'inputs_label': ('values', ),
        'inputs_color': ('bool', ),
        'outputs': ('bool', ),
        'outputs_label': ('bool', ),
        'inner': 'NOR',
        'label': 'not or'
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
    'random int': {
        'inputs': ('int', 'int'),
        'inputs_label': ('bottom', 'top'),
        'outputs': ('int', ),
        'outputs_label': ('int', ),
        'inner': 'R-Int',
        'label': 'random int',
    },
    'random num': {
        'inputs': ('number', 'number'),
        'inputs_label': ('bottom', 'top'),
        'outputs': ('number', ),
        'outputs_label': ('number', ),
        'inner': 'R-Num',
        'label': 'random num',
    },
    'random': {
        'inputs': ('ctrl', ),
        'inputs_label': ('ctrl', ),
        'outputs': ('real', ),
        'outputs_label': ('real', ),
        'inner': 'Rand',
        'label': 'random',
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
    'var': {
        'inputs': ('any', ),
        'inputs_label': ('any', ),
        'outputs': ('any', ),
        'outputs_label': ('any', ),
        'inner': 'Var',
        'label': 'variable',
        'sync_name': 'var'
    },
    'var set': {
        'inputs': ('any', ),
        'inputs_label': ('any', ),
        'outputs': ('ctrl', ),
        'outputs_label': ('ctrl', ),
        'inner': 'Var',
        'label': 'variable set',
        'sync_name': 'var set'
    },
    'var get': {
        'inputs': ('ctrl', ),
        'inputs_label': ('ctrl', ),
        'outputs': ('any', ),
        'outputs_label': ('any', ),
        'inner': 'Var',
        'label': 'variable get',
        'sync_name': 'var get'
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
        'inner': 'XOR',
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
