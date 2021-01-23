base_nodes_info = {
    'abs': {
        'inputs': ('number',),
        'inputs_label': ('number',),
        'outputs': ('number',),
        'outputs_label': ('number',),
        'inner': 'Abs',
        'label': 'abs',
        'tooltip': {
            'label': 'Abs',
            'desc': 'Модуль числа',
            'inputs': [
                ('Вход', 'Число'),
            ],
            'outputs': [
                ('Выход', 'Модуль от числа'),
            ]
        }
    },
    'add': {
        'inputs': ('mult',),
        'inputs_label': ('number',),
        'inputs_color': ('number',),
        'outputs': ('number',),
        'outputs_label': ('number',),
        'inner': '+',
        'label': 'add number',
        'sync_name': 'add',
        'tooltip': {
            'label': 'Add',
            'desc': 'Сложение чисел',
            'inputs': [
                ('Вход', 'Числа'),
            ],
            'outputs': [
                ('Выход', 'Сумма чисел'),
            ]
        }
    },
    'and': {
        'inputs': ('mult',),
        'inputs_label': ('values',),
        'inputs_color': ('bool',),
        'outputs': ('bool',),
        'outputs_label': ('bool',),
        'inner': 'AND',
        'label': 'and',
        'tooltip': {
            'label': 'And',
            'desc': 'Логическая операция И',
            'inputs': [
                ('Вход', 'Логические значения'),
            ],
            'outputs': [
                ('Выход', 'Результат логического умножения'),
            ],
            'adds': 'На вход могут подаваться любые значения, которые можно привести к логическим True или False. Для числа 0, пустого символа или None приводимое логическое значение будет False',
        }
    },
    'not and': {
        'inputs': ('mult',),
        'inputs_label': ('values',),
        'inputs_color': ('bool',),
        'outputs': ('bool',),
        'outputs_label': ('bool',),
        'inner': 'NAND',
        'label': 'not and',
        'tooltip': {
            'label': 'Not And (Sheffer stroke)',
            'desc': 'Логическая операция И-НЕ',
            'inputs': [
                ('Вход', 'Логические значения'),
            ],
            'outputs': [
                ('Выход', 'Результат логического умножения с инверсией'),
            ],
            'adds': 'На вход могут подаваться любые значения, которые можно привести к логическим True или False. Для числа 0, пустого символа или None приводимое логическое значение будет False',
        }
    },
    'bool': {
        'inputs': ('any',),
        'inputs_label': ('any',),
        'outputs': ('bool',),
        'outputs_label': ('bool',),
        'inner': 'Bool',
        'label': 'bool',
        'tooltip': {
            'label': 'Boolean',
            'desc': 'Приведение к логическому типу',
            'inputs': [
                ('Вход', 'Любое значение'),
            ],
            'outputs': [
                ('Выход', 'Приведенное логическое значение'),
            ],
            'adds': 'На вход могут подаваться любое значение, которое можно привести к логическим True или False. Для числа 0, пустого символа или None приводимое логическое значение будет False',
        }
    },
    'const': {
        'inputs': (),
        'inputs_label': (),
        'outputs': ('any',),
        'outputs_label': ('any',),
        'inner': 'Const',
        'label': 'constant',
        'sync_name': 'const',
        'tooltip': {
            'label': 'Constant',
            'desc': 'Пассивное получениe константы',
            'outputs': [
                ('Выход', 'Константа указанная в описании Узла'),
            ],
            'adds': 'Кроме числовых или строковых значений, можно получить предустановленные значения ($iteration, $min, $max, $pi, $true, $false, $none, $sep). Можно установить тип получаемых данных, записав тип после значения ($int, $real, $bool, $char, $num, $str, $any)',
        }
    },
    'const ctrl': {
        'inputs': ('ctrl',),
        'inputs_label': ('ctrl',),
        'outputs': ('any',),
        'outputs_label': ('any',),
        'inner': 'Const',
        'label': 'constant with ctrl',
        'sync_name': 'const ctrl',
        'tooltip': {
            'label': 'Constant',
            'desc': 'Активное получениe константы',
            'outputs': [
                ('Выход', 'Константа указанная в описании Узла'),
            ],
            'adds': 'Позволяет активировать Узел после себя. Кроме числовых или строковых значений, можно получить предустановленные значения ($iteration, $min, $max, $pi, $true, $false, $none, $sep). Можно установить тип получаемых данных, записав тип после значения ($int, $real, $bool, $char, $num, $str, $any)',
        }
    },
    'counter': {
        'inputs': ('ctrl', 'int', 'sep', 'ctrl'),
        'inputs_label': ('ctrl', 'bound', 'next'),
        'outputs': ('ctrl', 'sep', 'int'),
        'outputs_label': ('end ctrl', 'count'),
        'inner': 'Ctr',
        'label': 'counter',
        'tooltip': {
            'label': 'Counter',
            'desc': 'Цикл отсчитывающий целые значения от нуля до указанного на входе',
            'inputs': [
                ('Вход', 'Активирующий вход'),
                ('Вход', 'Верхняя граница'),
                ('Вход', 'Итерирующий вход'),
            ],
            'outputs': [
                ('Выход', 'Завершающий выход'),
                ('Выход', 'Значение текущей итерации'),
            ],
            'adds': 'При подаче сигнала на активирующий вход Узел получит границу и начнет итерацию. При подаче сигнала на итерирующий вход Узел прибавит значение к счетчику и запустит следующую итерацию',
        }
    },
    'dec': {
        'inputs': ('number',),
        'inputs_label': ('number',),
        'outputs': ('number',),
        'outputs_label': ('number',),
        'inner': 'Dec',
        'label': 'decrement',
        'sync_name': 'dec',
        'tooltip': {
            'label': 'Decrement',
            'desc': 'Уменьшает значение на 1',
            'inputs': [
                ('Вход', 'Число'),
            ],
            'outputs': [
                ('Выход', 'Уменьшенное число'),
            ]
        }
    },
    'delay': {
        'inputs': ('ctrl', 'int'),
        'inputs_label': ('ctrl', 'time'),
        'outputs': ('ctrl',),
        'outputs_label': ('ctrl',),
        'inner': 'Delay',
        'label': 'delay',
        'tooltip': {
            'label': 'Delay',
            'desc': 'Задержка сигнала',
            'inputs': [
                ('Вход', 'Активирующий вход'),
                ('Вход', 'Количество итераций задержки'),
            ],
            'outputs': [
                ('Выход', 'Завершающий выход'),
            ]
        }
    },
    'div': {
        'inputs': ('number', 'number'),
        'inputs_label': ('dividend', 'divider'),
        'outputs': ('int',),
        'outputs_label': ('int',),
        'inner': '//',
        'label': 'div',
        'tooltip': {
            'label': 'Div',
            'desc': 'Целочисленное деление',
            'inputs': [
                ('Вход', 'Делимое'),
                ('Вход', 'Делитель'),
            ],
            'outputs': [
                ('Выход', 'Частное'),
            ]
        }
    },
    'division': {
        'inputs': ('number', 'number'),
        'inputs_label': ('dividend', 'divider'),
        'outputs': ('number',),
        'outputs_label': ('number',),
        'inner': '/',
        'label': 'div number',
        'sync_name': 'division',
        'tooltip': {
            'label': 'Division',
            'desc': 'Обыкновенное деление',
            'inputs': [
                ('Вход', 'Делимое'),
                ('Вход', 'Делитель'),
            ],
            'outputs': [
                ('Выход', 'Частное'),
            ]
        }
    },
    'equal': {
        'inputs': ('mult',),
        'inputs_label': ('values',),
        'outputs': ('bool',),
        'outputs_label': ('bool',),
        'inner': '=',
        'label': 'equal',
        'tooltip': {
            'label': 'Equal',
            'desc': 'Проверка на равенство',
            'inputs': [
                ('Вход', 'Любые значения'),
            ],
            'outputs': [
                ('Выход', 'Результат сравнения на равенство'),
            ]
        }
    },
    'error': {
        'inputs': ('ctrl',),
        'inputs_label': ('ctrl',),
        'outputs': (),
        'outputs_label': (),
        'inner': 'Err',
        'label': 'error message',
        'sync_name': 'error',
        'tooltip': {
            'label': 'Error',
            'desc': 'Вызов ошибки и выход из программы',
            'inputs': [
                ('Вход', 'Активирующий вход'),
            ],
            'adds': 'При получения сигнала показывает ошибку указанную в описании Узла',
        }
    },
    'warning': {
        'inputs': ('ctrl',),
        'inputs_label': ('ctrl',),
        'outputs': ('ctrl',),
        'outputs_label': ('ctrl',),
        'inner': 'Wrng',
        'label': 'warning message',
        'sync_name': 'warning',
        'tooltip': {
            'label': 'Warning',
            'desc': 'Сообщение об ошибке',
            'inputs': [
                ('Вход', 'Активирующий вход'),
            ],
            'outputs': [
                ('Выход', 'Завершающий выход'),
            ],
            'adds': 'При получения сигнала показывает ошибку указанную в описании Узла',
        }
    },
    'exp': {
        'inputs': ('number', 'number'),
        'inputs_label': ('base', 'exponent'),
        'outputs': ('number',),
        'outputs_label': ('number',),
        'inner': '**',
        'label': 'exp number',
        'sync_name': 'exp',
        'tooltip': {
            'label': 'Exponent',
            'desc': 'Возводит значение в указанную степень',
            'inputs': [
                ('Вход', 'Основание'),
                ('Вход', 'Степень'),
            ],
            'outputs': [
                ('Выход', 'Результат возведения'),
            ]
        }
    },
    'for ext': {
        'inputs': ('ctrl', 'number', 'number', 'number'),
        'inputs_label': ('ctrl', 'bound', 'start value', 'increment'),
        'outputs': ('ctrl', 'sep', 'number'),
        'outputs_label': ('end ctrl', 'iteration'),
        'inner': 'For',
        'label': 'for extended',
        'sync_name': 'for',
        'tooltip': {
            'label': 'For Extended',
            'desc': 'Расширенный цикл счетчик.',
            'inputs': [
                ('Вход', 'Активирующий вход'),
                ('Вход', 'Верхняя граница'),
                ('Вход', 'Начальное значение'),
                ('Вход', 'Инкремент'),
            ],
            'outputs': [
                ('Выход', 'Завершающий выход'),
                ('Выход', 'Значение текущей итерации'),
            ],
            'adds': 'При подаче сигнала на активирующий вход Узел получит границу и начнет итерацию с указанного значения. При подаче сигнала на вход инкремента Узел прибавит значение к значению текущей итерации',
        }
    },
    'for': {
        'inputs': ('ctrl', 'number', 'sep', 'number'),
        'inputs_label': ('ctrl', 'bound', 'increment'),
        'outputs': ('ctrl', 'sep', 'number'),
        'outputs_label': ('end ctrl', 'iteration'),
        'inner': 'For',
        'label': 'for',
        'tooltip': {
            'label': 'For',
            'desc': 'Цикл счетчик',
            'inputs': [
                ('Вход', 'Активирующий вход'),
                ('Вход', 'Верхняя граница'),
                ('Вход', 'Инкремент'),
            ],
            'outputs': [
                ('Выход', 'Завершающий выход'),
                ('Выход', 'Значение текущей итерации'),
            ],
            'adds': 'При подаче сигнала на активирующий вход Узел получит границу и начнет итерацию с нуля. При подаче сигнала на вход инкремента Узел прибавит значение к значению текущей итерации',
        }
    },
    'foreach': {
        'inputs': ('ctrl', 'mult_s', 'sep', 'ctrl'),
        'inputs_label': ('ctrl', 'values', 'next',),
        'outputs': ('ctrl', 'sep', 'any'),
        'outputs_label': ('end ctrl', 'value'),
        'inner': 'For',
        'label': 'foreach',
        'tooltip': {
            'label': 'For',
            'desc': 'Перебирающий цикл',
            'inputs': [
                ('Вход', 'Активирующий вход'),
                ('Вход', 'Значения для перебора (без учета порядка)'),
                ('Вход', 'Итерирующий вход'),
            ],
            'outputs': [
                ('Выход', 'Завершающий выход'),
                ('Выход', 'Значение на текущей итерации'),
            ],
            'adds': 'При подаче сигнала на активирующий вход Узел получит значения и начнет итерацию по ним. При подаче сигнала на итерирующий вход Узел переключится на следующее значение. Если в описании Узла указать имя переменной со структурой (словарь, список и т.п) цикл будет использовать значения из переменной',
        }
    },
    'get type': {
        'inputs': (),
        'inputs_label': (),
        'outputs': ('obj', 'any'),
        'outputs_label': ('type', 'default'),
        'inner': 'T',
        'label': 'get type',
        'tooltip': {
            'label': 'Get Type',
            'desc': 'Пассивное получение типа и значения по умолчанию',
            'outputs': [
                ('Выход', 'Тип как объект'),
                ('Выход', 'Значение по умолчанию'),
            ]
        }
    },
    'greater': {
        'inputs': ('any', 'any'),
        'inputs_label': ('a', 'b'),
        'outputs': ('bool',),
        'outputs_label': ('bool',),
        'inner': 'a>b',
        'label': 'greater',
        'tooltip': {
            'label': 'Greater',
            'desc': 'Разностное сравнение - больше',
            'inputs': [
                ('Вход', 'Любое значение (a)'),
                ('Вход', 'Любое значение (b)'),
            ],
            'outputs': [
                ('Выход', 'Результат сравнения'),
            ]
        }
    },
    'greater or equal': {
        'inputs': ('any', 'any'),
        'inputs_label': ('a', 'b'),
        'outputs': ('bool',),
        'outputs_label': ('bool',),
        'inner': 'a>=b',
        'label': 'greater or equal',
        'tooltip': {
            'label': 'Greater or Equal',
            'desc': 'Разностное сравнение - больше или равно',
            'inputs': [
                ('Вход', 'Любое значение (a)'),
                ('Вход', 'Любое значение (b)'),
            ],
            'outputs': [
                ('Выход', 'Результат сравнения'),
            ]
        }
    },
    'if': {
        'inputs': ('ctrl', 'bool'),
        'inputs_label': ('ctrl', 'condition'),
        'outputs': ('ctrl', 'ctrl'),
        'outputs_label': ('true', 'false'),
        'inner': 'If',
        'label': 'if',
        'tooltip': {
            'label': 'If',
            'desc': 'Условный оператор',
            'inputs': [
                ('Вход', 'Активирующий вход'),
                ('Вход', 'Логическое значение'),
            ],
            'outputs': [
                ('Выход', 'Выход True'),
                ('Выход', 'Выход False'),
            ],
            'adds': 'На вход могут подаваться любые значения, которые можно привести к логическим True или False. Для числа 0, пустого символа или None приводимое логическое значение будет False',
        }
    },
    'in': {
        'inputs': ('mult_s', 'any'),
        'inputs_label': ('mult', 'any'),
        'outputs': ('bool',),
        'outputs_label': ('bool',),
        'inner': 'In',
        'label': 'contains',
        'sync_name': 'in',
        'tooltip': {
            'label': 'Contains (In)',
            'desc': 'Проверка на принадлежность',
            'inputs': [
                ('Вход', 'Множество значений'),
                ('Вход', 'Значение на проверку'),
            ],
            'outputs': [
                ('Выход', 'Результат проверки'),
            ],
            'adds': 'Если в описании Узла указать имя переменной со структурой (словарь, список и т.п) цикл будет использовать значения из переменной как множество',
        }
    },
    'inc': {
        'inputs': ('number',),
        'inputs_label': ('number',),
        'outputs': ('number',),
        'outputs_label': ('number',),
        'inner': 'Inc',
        'label': 'increment',
        'sync_name': 'inc',
        'tooltip': {
            'label': 'Increment',
            'desc': 'Увеличение значения на 1',
            'inputs': [
                ('Вход', 'Число'),
            ],
            'outputs': [
                ('Выход', 'Увеличенное число'),
            ]
        }
    },
    'input': {
        'inputs': ('ctrl',),
        'inputs_label': ('ctrl',),
        'outputs': ('any',),
        'outputs_label': ('any',),
        'inner': 'Input',
        'label': 'input',
        'tooltip': {
            'label': 'Input',
            'desc': 'Ввод данных',
            'inputs': [
                ('Вход', 'Активирующий вход'),
            ],
            'outputs': [
                ('Выход', 'Полученные вводом значение'),
            ],
            'adds': 'Если указать в описании Узла значение, то оно будет выведено пользователю. Узел блокирует работу программы',
        }
    },
    'trunc': {
        'inputs': ('number',),
        'inputs_label': ('number',),
        'outputs': ('int',),
        'outputs_label': ('int',),
        'inner': 'Trunc',
        'label': 'trunc',
        'tooltip': {
            'label': 'Trunc',
            'desc': 'Отсечение дробной части',
            'inputs': [
                ('Вход', 'Любое число'),
            ],
            'outputs': [
                ('Выход', 'Целая часть от числа'),
            ]
        }
    },
    'inv': {
        'inputs': ('number',),
        'inputs_label': ('number',),
        'outputs': ('number',),
        'outputs_label': ('number',),
        'inner': 'Inv',
        'label': 'inversion',
        'sync_name': 'inv',
        'tooltip': {
            'label': 'Inversion',
            'desc': 'Изменение знака',
            'inputs': [
                ('Вход', 'Любое число'),
            ],
            'outputs': [
                ('Выход', 'Число с обратным знаком'),
            ]
        }
    },
    'less': {
        'inputs': ('any', 'any'),
        'inputs_label': ('a', 'b'),
        'outputs': ('bool',),
        'outputs_label': ('bool',),
        'inner': 'a<b',
        'label': 'less',
        'tooltip': {
            'label': 'Less',
            'desc': 'Разностное сравнение - меньше',
            'inputs': [
                ('Вход', 'Любое значение (a)'),
                ('Вход', 'Любое значение (b)'),
            ],
            'outputs': [
                ('Выход', 'Результат сравнения'),
            ]
        }
    },
    'less or equal': {
        'inputs': ('any', 'any'),
        'inputs_label': ('a', 'b'),
        'outputs': ('bool',),
        'outputs_label': ('bool',),
        'inner': 'a<=b',
        'label': 'less or equal',
        'tooltip': {
            'label': 'Less or Equal',
            'desc': 'Разностное сравнение - меньше или равно',
            'inputs': [
                ('Вход', 'Любое значение (a)'),
                ('Вход', 'Любое значение (b)'),
            ],
            'outputs': [
                ('Выход', 'Результат сравнения'),
            ]
        }
    },
    'merge': {
        'inputs': ('ctrl', 'any'),
        'inputs_label': ('ctrl', 'any'),
        'outputs': ('any',),
        'outputs_label': ('any',),
        'inner': 'Merge',
        'label': 'merge ctrl',
        'sync_name': 'merge',
        'tooltip': {
            'label': 'Merge',
            'desc': 'Объединение сигнала и значения',
            'inputs': [
                ('Вход', 'Активирующий выход'),
                ('Вход', 'Любое значение'),
            ],
            'outputs': [
                ('Выход', 'Значение с активным сигналом'),
            ],
            'adds': 'При получении сигнала в активирующий вход Узел значение и возвращает значение с активным сигналом',
        }
    },
    'mod': {
        'inputs': ('number', 'number'),
        'inputs_label': ('dividend', 'divider'),
        'outputs': ('number',),
        'outputs_label': ('number',),
        'inner': '%',
        'label': 'mod',
        'tooltip': {
            'label': 'Mod',
            'desc': 'Остаток от деления',
            'inputs': [
                ('Вход', 'Делимое'),
                ('Вход', 'Делитель'),
            ],
            'outputs': [
                ('Выход', 'Остаток'),
            ]
        }
    },
    'mult': {
        'inputs': ('mult',),
        'inputs_label': ('number',),
        'inputs_color': ('number',),
        'outputs': ('number',),
        'outputs_label': ('number',),
        'inner': '*',
        'label': 'mult number',
        'sync_name': 'mult',
        'tooltip': {
            'label': 'Multiplication',
            'desc': 'Произведение',
            'inputs': [
                ('Вход', 'Любые числа'),
            ],
            'outputs': [
                ('Выход', 'Результат перемножения чисел'),
            ]
        }
    },
    'not': {
        'inputs': ('bool',),
        'inputs_label': ('bool',),
        'outputs': ('bool',),
        'outputs_label': ('bool',),
        'inner': 'NOT',
        'label': 'not',
        'tooltip': {
            'label': 'Not',
            'desc': 'Логическая операция НЕ',
            'inputs': [
                ('Вход', 'Логическое значение'),
            ],
            'outputs': [
                ('Выход', 'Результат операции инверсии'),
            ],
            'adds': 'На вход могут подаваться любые значения, которые можно привести к логическим True или False. Для числа 0, пустого символа или None приводимое логическое значение будет False',
        }
    },
    'not equal': {
        'inputs': ('any', 'any'),
        'inputs_label': ('a', 'b'),
        'outputs': ('bool',),
        'outputs_label': ('bool',),
        'inner': 'a!=b',
        'label': 'not equal',
        'tooltip': {
            'label': 'Not Equal',
            'desc': 'Проверка на не равенство',
            'inputs': [
                ('Вход', 'Любое значение'),
                ('Вход', 'Любое значение'),
            ],
            'outputs': [
                ('Выход', 'Результат сравнения'),
            ]
        }
    },
    'or': {
        'inputs': ('mult',),
        'inputs_label': ('values',),
        'inputs_color': ('bool',),
        'outputs': ('bool',),
        'outputs_label': ('bool',),
        'inner': 'OR',
        'label': 'or',
        'tooltip': {
            'label': 'Or',
            'desc': 'Логическая операция ИЛИ',
            'inputs': [
                ('Вход', 'Логическое значение'),
                ('Вход', 'Логическое значение'),
            ],
            'outputs': [
                ('Выход', 'Результат логического сложения'),
            ],
            'adds': 'На вход могут подаваться любые значения, которые можно привести к логическим True или False. Для числа 0, пустого символа или None приводимое логическое значение будет False',
        }
    },
    'not or': {
        'inputs': ('mult',),
        'inputs_label': ('values',),
        'inputs_color': ('bool',),
        'outputs': ('bool',),
        'outputs_label': ('bool',),
        'inner': 'NOR',
        'label': 'not or',
        'tooltip': {
            'label': 'Not Or',
            'desc': 'Логическая операция ИЛИ-НЕ',
            'inputs': [
                ('Вход', 'Логическое значение'),
                ('Вход', 'Логическое значение'),
            ],
            'outputs': [
                ('Выход', 'Результат логического сложения с инверсией'),
            ],
            'adds': 'На вход могут подаваться любые значения, которые можно привести к логическим True или False. Для числа 0, пустого символа или None приводимое логическое значение будет False',
        }
    },
    'print': {
        'inputs': ('any',),
        'inputs_label': ('any',),
        'outputs': (),
        'outputs_label': (),
        'inner': 'Print',
        'label': 'print',
        'tooltip': {
            'label': 'Print',
            'desc': 'Вывод данных',
            'inputs': [
                ('Вход', 'Любое значение'),
            ],
            'adds': 'Если указать в описании Узла значение, то оно будет выведено пользователю. Поддерживается использование предустановленных значений ($iteration, $min, $max, $pi, $true, $false, $none, $sep) и вывод переменных (с указанием имени после $)',
        }
    },
    'print ctrl': {
        'inputs': ('any',),
        'inputs_label': ('any',),
        'outputs': ('ctrl',),
        'outputs_label': ('ctrl',),
        'inner': 'Print',
        'label': 'print with ctrl',
        'sync_name': 'print ctrl',
        'tooltip': {
            'label': 'Print',
            'desc': 'Вывод данных с последующей активацией',
            'inputs': [
                ('Вход', 'Любое значение'),
            ],
            'adds': 'Позволяет активировать Узел после себя. Если указать в описании Узла значение, то оно будет выведено пользователю. Поддерживается использование предустановленных значений ($iteration, $min, $max, $pi, $true, $false, $none, $sep) и вывод переменных (с указанием имени после $)',
        }
    },
    'random int': {
        'inputs': ('int', 'int'),
        'inputs_label': ('bottom', 'top'),
        'outputs': ('int',),
        'outputs_label': ('int',),
        'inner': 'Random\nInt',
        'label': 'random int',
        'tooltip': {
            'label': 'Random Int',
            'desc': 'Случайное целое число',
            'inputs': [
                ('Вход', 'Нижняя граница'),
                ('Вход', 'Верхняя граница'),
            ],
            'outputs': [
                ('Выход', 'Случайное целое число'),
            ]
        }
    },
    'random num': {
        'inputs': ('number', 'number'),
        'inputs_label': ('bottom', 'top'),
        'outputs': ('number',),
        'outputs_label': ('number',),
        'inner': 'Random\nNumber',
        'label': 'random num',
        'tooltip': {
            'label': 'Random Number',
            'desc': 'Случайное число',
            'inputs': [
                ('Вход', 'Нижняя граница'),
                ('Вход', 'Верхняя граница'),
            ],
            'outputs': [
                ('Выход', 'Случайное число'),
            ]
        }
    },
    'random seed': {
        'inputs': ('any',),
        'inputs_label': ('value',),
        'outputs': ('ctrl',),
        'outputs_label': ('ctrl',),
        'inner': 'Random\nSeed',
        'label': 'random seed',
        'tooltip': {
            'label': 'Random Seed',
            'desc': 'Изменение состояния генератора случайных чисел',
            'inputs': [
                ('Вход', 'Начальное условие генератора'),
            ],
            'outputs': [
                ('Выход', 'Завершающий выход'),
            ]
        }
    },
    'random': {
        'inputs': ('ctrl',),
        'inputs_label': ('ctrl',),
        'outputs': ('real',),
        'outputs_label': ('real',),
        'inner': 'Random',
        'label': 'random',
        'tooltip': {
            'label': 'Random',
            'desc': 'Случаное число от 0 до 1 не включая',
            'inputs': [
                ('Вход', 'Активирующий вход'),
            ],
            'outputs': [
                ('Выход', 'Случайное число'),
            ]
        }
    },
    'round': {
        'inputs': ('number', 'int'),
        'inputs_label': ('number', 'precision'),
        'outputs': ('number',),
        'outputs_label': ('number',),
        'inner': 'Round',
        'label': 'round',
        'tooltip': {
            'label': 'Round',
            'desc': 'Округление',
            'inputs': [
                ('Вход', 'Любое число'),
                ('Вход', 'Порядок округления'),
            ],
            'outputs': [
                ('Выход', 'Округленное значение'),
            ]
        }
    },
    'run': {
        'inputs': (),
        'inputs_label': (),
        'outputs': ('ctrl',),
        'outputs_label': ('ctrl',),
        'inner': 'Run',
        'label': 'run',
        'tooltip': {
            'label': 'Run',
            'desc': 'Начальный Узел',
            'outputs': [
                ('Выход', 'Активирующий выход'),
            ]
        }
    },
    'stop': {
        'inputs': ('ctrl',),
        'inputs_label': ('ctrl',),
        'outputs': (),
        'outputs_label': (),
        'inner': 'Stop',
        'label': 'stop',
        'tooltip': {
            'label': 'Stop',
            'desc': 'Конечный Узел',
            'inputs': [
                ('Вход', 'Завершающий вход'),
            ]
        }
    },
    'sub': {
        'inputs': ('number', 'number'),
        'inputs_label': ('minuend', 'subtrahend'),
        'outputs': ('number',),
        'outputs_label': ('number',),
        'inner': '-',
        'label': 'sub number',
        'sync_name': 'sub',
        'tooltip': {
            'label': 'Substraction',
            'desc': 'Вычитание',
            'inputs': [
                ('Вход', 'Уменьшаемое'),
                ('Вход', 'Вычитаемое'),
            ],
            'outputs': [
                ('Выход', 'Результат вычитания'),
            ]
        }
    },
    'timer': {
        'inputs': ('ctrl', 'ctrl'),
        'inputs_label': ('start ctrl', 'end ctrl'),
        'outputs': ('int',),
        'outputs_label': ('time',),
        'inner': 'Timer',
        'label': 'timer',
        'tooltip': {
            'label': 'Timer',
            'desc': 'Счетчик количества итераций между начальным сигналом и завершающим',
            'inputs': [
                ('Вход', 'Активирующий вход'),
                ('Вход', 'Завершающий вход'),
            ],
            'outputs': [
                ('Выход', 'Количество между сигналами'),
            ]
        }
    },
    'ctrl': {
        'inputs': ('any',),
        'inputs_label': ('any',),
        'outputs': ('ctrl',),
        'outputs_label': ('ctrl',),
        'inner': 'Ctrl',
        'label': 'to ctrl',
        'sync_name': 'ctrl',
        'tooltip': {
            'label': 'To Control',
            'desc': 'Сигнал без значения',
            'inputs': [
                ('Вход', 'Любое значение'),
            ],
            'outputs': [
                ('Выход', 'Завершающий выход'),
            ],
            'adds': 'Возвращает активный сигнал без значения'
        }
    },
    'type': {
        'inputs': ('any',),
        'inputs_label': ('any',),
        'outputs': ('obj',),
        'outputs_label': ('type',),
        'inner': 'Type',
        'label': 'type',
        'tooltip': {
            'label': 'Type',
            'desc': 'Тип значения',
            'inputs': [
                ('Вход', 'Любое значение'),
            ],
            'outputs': [
                ('Выход', 'Тип значения как объект'),
            ]
        }
    },
    'var': {
        'inputs': ('any',),
        'inputs_label': ('any',),
        'outputs': ('any',),
        'outputs_label': ('any',),
        'inner': 'Var',
        'label': 'variable',
        'sync_name': 'var',
        'tooltip': {
            'label': 'Variable',
            'desc': 'Создание или изменение переменной',
            'inputs': [
                ('Вход', 'Любое значение'),
            ],
            'outputs': [
                ('Выход', 'Значение из переменной'),
            ],
            'adds': 'В описании к Узлу должно быть указано название переменной',
        }
    },
    'var set': {
        'inputs': ('any',),
        'inputs_label': ('any',),
        'outputs': ('ctrl',),
        'outputs_label': ('ctrl',),
        'inner': 'Var',
        'label': 'variable set',
        'sync_name': 'var set',
        'tooltip': {
            'label': 'Variable Set',
            'desc': 'Создание или изменение переменной',
            'inputs': [
                ('Вход', 'Любое значение'),
            ],
            'outputs': [
                ('Выход', 'Завершающий выход'),
            ],
            'adds': 'В описании к Узлу должно быть указано название переменной. Узел не возвращает значение переменной',
        }
    },
    'var get': {
        'inputs': ('ctrl',),
        'inputs_label': ('ctrl',),
        'outputs': ('any',),
        'outputs_label': ('any',),
        'inner': 'Var',
        'label': 'variable get',
        'sync_name': 'var get',
        'tooltip': {
            'label': 'Variable Get',
            'desc': 'Получение переменной',
            'inputs': [
                ('Вход', 'Активирующий вход'),
            ],
            'outputs': [
                ('Выход', 'Значение из переменной'),
            ],
            'adds': 'В описании к Узлу должно быть указано название переменной. Узел не изменяет значение переменной',
        }
    },
    'wait': {
        'inputs': ('mult',),
        'inputs_label': ('ctrl',),
        'inputs_color': ('ctrl',),
        'outputs': ('ctrl',),
        'outputs_label': ('ctrl',),
        'inner': 'Wait',
        'label': 'wait',
        'tooltip': {
            'label': 'Wait',
            'desc': 'Ожидание сигналов',
            'inputs': [
                ('Вход', 'Активирующие входа'),
            ],
            'outputs': [
                ('Выход', 'Завершающий выход'),
            ],
            'adds': 'Возможно изменение режима работы на активацию после получения хотя бы одного сигнала. Для этого требуется в описании к Узлу указать "any"',
        }
    },
    'while': {
        'inputs': ('ctrl', 'sep', 'bool'),
        'inputs_label': ('ctrl', 'condition'),
        'outputs': ('ctrl', 'sep', 'ctrl'),
        'outputs_label': ('ctrl', 'while ctrl'),
        'inner': 'While',
        'label': 'while',
        'tooltip': {
            'label': 'While',
            'desc': 'Цикл с условием',
            'inputs': [
                ('Вход', 'Активирующий вход'),
                ('Вход', 'Итерирующий вход условие'),
            ],
            'outputs': [
                ('Выход', 'Завершающий выход'),
                ('Выход', 'Итерирующий выход'),
            ],
            'adds': 'При получении сигнала на активирующий вход Узел начинает итерацию. Если на итерирующий вход подается логическое значение True Узел активирует итерирующий выход, иначе завершающий',
        }
    },
    'xor': {
        'inputs': ('bool', 'bool'),
        'inputs_label': ('bool', 'bool'),
        'outputs': ('bool',),
        'outputs_label': ('bool',),
        'inner': 'XOR',
        'label': 'xor',
        'tooltip': {
            'label': 'Xor',
            'desc': 'Логическая операция Исключающее ИЛИ',
            'inputs': [
                ('Вход', 'Логическое значение'),
                ('Вход', 'Логическое значение'),
            ],
            'outputs': [
                ('Выход', 'Результат логического сложения по модулю 2'),
            ],
            'adds': 'На вход могут подаваться любые значения, которые можно привести к логическим True или False. Для числа 0, пустого символа или None приводимое логическое значение будет False',
        }
    },
    'value switch': {
        'inputs': ('mult',),
        'inputs_label': ('values',),
        'outputs': ('any',),
        'outputs_label': ('value',),
        'inner': '>-',
        'label': 'value switch',
        'tooltip': {
            'label': 'Value Switch',
            'desc': 'Переключатель значений',
            'inputs': [
                ('Вход', 'Любые значения'),
            ],
            'outputs': [
                ('Выход', 'Значение с активного входа'),
            ],
            'adds': 'Возвращает значение с активного входа',
        }
    },
    'join': {
        'inner': 'Join',
        'label': 'join',
        'sync_name': 'join',

        'inputs': ('ctrl', 'str'),
        'inputs_label': ('activation', 'join symbols'),

        'outputs': ('str',),
        'outputs_label': ('result',),

        'tooltip': {
            'label': 'Join',
            'desc': 'Объединение строк в массиве',
            'inputs': [
                ('Вход', 'Активирующий вход'),
                ('Вход', 'Объединяющая строка'),
            ],
            'outputs': [
                ('Выход', 'Строка'),
            ],
            'adds': 'Объединяет строки в структурной переменной указанной в описании Узла',
        }
    },
    'concatenate': {
        'inner': '+',
        'label': 'concatenate',
        'sync_name': 'concatenate',

        'inputs': ('str', 'str'),
        'inputs_label': ('a', 'b'),

        'outputs': ('str',),
        'outputs_label': ('result',),

        'tooltip': {
            'label': 'Concatenate',
            'desc': 'Конкатенация строк',
            'inputs': [
                ('Вход', 'Первая строка'),
                ('Вход', 'Вторая строка'),
            ],
            'outputs': [
                ('Выход', 'Строка'),
            ]
        }
    },
    'format': {
        'inner': 'Format',
        'label': 'format',
        'sync_name': 'format',

        'inputs': ('str', 'any'),
        'inputs_label': ('format', 'data'),

        'outputs': ('str',),
        'outputs_label': ('result', ),

        'tooltip': {
            'label': 'Format',
            'desc': 'Форматирование данных',
            'inputs': [
                ('Вход', 'Формат'),
                ('Вход', 'Данные'),
            ],
            'outputs': [
                ('Выход', 'Форматированная строка'),
            ],
            'adds': 'Форматирует данные из структурной переменной указанной в описании Узла. Если используется второй вход, то формат происходит по значению из него. Формат имеет следующую структуру: {индекс в массиве, ключ словаря или 0}. Возможно использование спецификации - {индекс:спецификация}. Спецификация может быть следующей: [[[символ]<|>|^]ширина][.точность][f|%|e] (квадратныые скобки обозначают необязательность, вертикальная черта - возможность выбора между указанными значениями)',
        }
    }
}
not_created_nodes_info = {
    'split string': {
        'inputs': ('any', 'sep', 'ctrl'),
        'inputs_color': ('char', 'ctrl'),
        'inputs_label': ('str', 'sep', 'ctrl',),
        'outputs': ('ctrl', 'sep', 'any',),
        'outputs_color': ('ctrl', 'char'),
        'outputs_label': ('ctrl', 'sep', 'str',),
        'inner': 'Split',
        'label': 'split string'
    },
}
structure_nodes_info = {
    'array create': {
        'inputs': ('int',),
        'inputs_label': ('len',),
        'outputs': ('ctrl',),
        'outputs_label': ('ctrl',),
        'inner': 'Array',
        'label': 'array create',
        'tooltip': {
            'label': 'Array',
            'desc': 'Создание массива',
            'inputs': [
                ('Вход', 'Количество элементов'),
            ],
            'outputs': [
                ('Выход', 'Завершающий выход'),
            ],
            'adds': 'В описании к Узлу должно быть указано имя переменной. Можно установить тип данных в массиве, записав тип после имени переменной ($int, $real, $bool, $char, $num, $str, $any)',
        }
    },
    'array set': {
        'inputs': ('int', 'any'),
        'inputs_label': ('index', 'value'),
        'outputs': ('ctrl',),
        'outputs_label': ('ctrl',),
        'inner': 'Array\nSet',
        'label': 'array set',
        'tooltip': {
            'label': 'Array Set',
            'desc': 'Изменение значения в массиве',
            'inputs': [
                ('Вход', 'Позиция элемента'),
                ('Вход', 'Значение на установку'),
            ],
            'outputs': [
                ('Выход', 'Завершающий выход'),
            ],
            'adds': 'В описании к Узлу должно быть указано имя переменной',
        }
    },
    'array get': {
        'inputs': ('int',),
        'inputs_label': ('index',),
        'outputs': ('any',),
        'outputs_label': ('value',),
        'inner': 'Array\nGet',
        'label': 'array get',
        'tooltip': {
            'label': 'Array Get',
            'desc': 'Получение значения из массива',
            'inputs': [
                ('Вход', 'Позиция элемента'),
            ],
            'outputs': [
                ('Выход', 'Значение на указанной позиции'),
            ],
            'adds': 'В описании к Узлу должно быть указано имя переменной',
        }
    },
    'array get and set': {
        'inputs': ('int', 'any'),
        'inputs_label': ('index', 'value'),
        'outputs': ('any',),
        'outputs_label': ('value',),
        'inner': 'Array\nG&S',
        'label': 'array get and set',
        'tooltip': {
            'label': 'Array Get and Set',
            'desc': 'Получение и установка значения массива',
            'inputs': [
                ('Вход', 'Позиция элемента'),
                ('Вход', 'Значение на установку'),
            ],
            'outputs': [
                ('Выход', 'Значение на указанной позиции'),
            ],
            'adds': 'В описании к Узлу должно быть указано имя переменной. Если установка не происходит, то Узел забирает значение из массива без изменения',
        }
    },
    'dict create': {
        'inputs': ('obj', 'obj'),
        'inputs_label': ('key', 'value'),
        'outputs': ('ctrl',),
        'outputs_label': ('ctrl',),
        'inner': 'Dict',
        'label': 'dict create',
        'tooltip': {
            'label': 'Dict',
            'desc': 'Создание словаря',
            'inputs': [
                ('Вход', 'Тип ключа'),
                ('Вход', 'Тип значения'),
            ],
            'outputs': [
                ('Выход', 'Завершающий выход'),
            ],
            'adds': 'В описании к Узлу должно быть указано имя переменной. Вместо типа можно подать значение, которое автоматически конвертируется в тип',
        }
    },
    'dict insert': {
        'inputs': ('any', 'any'),
        'inputs_label': ('key', 'value'),
        'outputs': ('ctrl',),
        'outputs_label': ('ctrl',),
        'inner': 'Dict\nInsert',
        'label': 'dict insert',
        'tooltip': {
            'label': 'Dict Insert',
            'desc': 'Установка значения в словаре',
            'inputs': [
                ('Вход', 'Ключ'),
                ('Вход', 'Значение'),
            ],
            'outputs': [
                ('Выход', 'Завершающий выход'),
            ],
            'adds': 'В описании к Узлу должно быть указано имя переменной. Если тип входа не совпадает с типом в словаре, то тип автоматически конвертируется в требуемый',
        }
    },
    'dict find': {
        'inputs': ('any',),
        'inputs_label': ('key',),
        'outputs': ('any',),
        'outputs_label': ('value',),
        'inner': 'Dict\nFind',
        'label': 'dict find',
        'tooltip': {
            'label': 'Dict Find',
            'desc': 'Поиск значения в словаре',
            'inputs': [
                ('Вход', 'Ключ'),
            ],
            'outputs': [
                ('Выход', 'Значение под ключем'),
            ],
            'adds': 'В описании к Узлу должно быть указано имя переменной. Если тип входа не совпадает с типом в словаре, то тип автоматически конвертируется в требуемый',
        }
    },
    'dict insert and find': {
        'inputs': ('any', 'any'),
        'inputs_label': ('key', 'value'),
        'outputs': ('any',),
        'outputs_label': ('value',),
        'inner': 'Dict\nI&F',
        'label': 'dict insert and find',
        'tooltip': {
            'label': 'Dict Insert and Find',
            'desc': 'Поиск значения в словаре и установка',
            'inputs': [
                ('Вход', 'Ключ'),
                ('Вход', 'Значение'),
            ],
            'outputs': [
                ('Выход', 'Значение под ключем'),
            ],
            'adds': 'В описании к Узлу должно быть указано имя переменной. Если установка значения не происходит, то значение под указанным ключем не будет изменено. Если тип входа не совпадает с типом в словаре, то тип автоматически конвертируется в требуемый',
        }
    },
    'dict remove': {
        'inputs': ('any',),
        'inputs_label': ('key',),
        'outputs': ('ctrl',),
        'outputs_label': ('ctrl',),
        'inner': 'Dict\nRemove',
        'label': 'dict remove',
        'tooltip': {
            'label': 'Dict Remove',
            'desc': 'Удаление значения из словаря',
            'inputs': [
                ('Вход', 'Ключ'),
            ],
            'outputs': [
                ('Выход', 'Завершающий выход'),
            ],
            'adds': 'В описании к Узлу должно быть указано имя переменной. Если тип входа не совпадает с типом в словаре, то тип автоматически конвертируется в требуемый',
        }
    },
    'length': {
        'inputs': ('ctrl',),
        'inputs_label': ('ctrl',),
        'outputs': ('int',),
        'outputs_label': ('int',),
        'inner': 'Len',
        'label': 'length',
        'tooltip': {
            'label': 'Length',
            'desc': 'Длина структурной переменной (список или словарь)',
            'inputs': [
                ('Вход', 'Активирующий вход'),
            ],
            'outputs': [
                ('Выход', 'Длина'),
            ],
            'adds': 'В описании к Узлу должно быть указано имя переменной',
        }
    },
    'list create': {
        'inputs': ('ctrl',),
        'inputs_label': ('ctrl',),
        'outputs': ('ctrl',),
        'outputs_label': ('ctrl',),
        'inner': 'List',
        'label': 'list create',
        'tooltip': {
            'label': 'List',
            'desc': 'Создание списка',
            'inputs': [
                ('Вход', 'Активирующий вход'),
            ],
            'outputs': [
                ('Выход', 'Завершающий выход'),
            ],
            'adds': 'В описании к Узлу должно быть указано имя переменной. Можно установить тип данных в списке, записав тип после имени переменной ($int, $real, $bool, $char, $num, $str, $any)',
        }
    },
    'list set': {
        'inputs': ('int', 'any'),
        'inputs_label': ('index', 'value'),
        'outputs': ('ctrl',),
        'outputs_label': ('ctrl',),
        'inner': 'List\nSet',
        'label': 'list set',
        'tooltip': {
            'label': 'List Set',
            'desc': 'Изменение и добавление элемента списка',
            'inputs': [
                ('Вход', 'Позиция элемента'),
                ('Вход', 'Значение на установку'),
            ],
            'outputs': [
                ('Выход', 'Завершающий выход'),
            ],
            'adds': 'В описании к Узлу должно быть указано имя переменной. Если не указать позицию, то Узел добавит элемент в конец списка',
        }
    },
    'list get': {
        'inputs': ('int',),
        'inputs_label': ('index',),
        'outputs': ('any',),
        'outputs_label': ('value',),
        'inner': 'List\nGet',
        'label': 'list get',
        'tooltip': {
            'label': 'List Get',
            'desc': 'Получение элемента списка',
            'inputs': [
                ('Вход', 'Позиция элемента'),
            ],
            'outputs': [
                ('Выход', 'Значение на указанной позиции'),
            ],
            'adds': 'В описании к Узлу должно быть указано имя переменной',
        }
    },
    'list get and set': {
        'inputs': ('int', 'any'),
        'inputs_label': ('index', 'value'),
        'outputs': ('any',),
        'outputs_label': ('value',),
        'inner': 'List\nG&S',
        'label': 'list get and set',
        'tooltip': {
            'label': 'List Get and Set',
            'desc': 'Получение, изменение и добавление элемента списка',
            'inputs': [
                ('Вход', 'Позиция элемента'),
                ('Вход', 'Значение на установку'),
            ],
            'outputs': [
                ('Выход', 'Значение на указанной позиции'),
            ],
            'adds': 'В описании к Узлу должно быть указано имя переменной. Если не указать значение элемента, то Узел вернет элемент без изменения. Если не указать позицию, то Узел добавит элемент в конец списка',
        }
    },
    'list remove': {
        'inputs': ('int',),
        'inputs_label': ('index',),
        'outputs': ('ctrl',),
        'outputs_label': ('ctrl',),
        'inner': 'List\nRemove',
        'label': 'list remove',
        'tooltip': {
            'label': 'List Remove',
            'desc': 'Удаление элемента списка',
            'inputs': [
                ('Вход', 'Индекс элемента'),
            ],
            'outputs': [
                ('Выход', 'Завершающий выход'),
            ],
            'adds': 'В описании к Узлу должно быть указано имя переменной',
        }
    },
    'matrix create': {
        'inputs': ('int', 'int',),
        'inputs_label': ('len y', 'len x',),
        'outputs': ('ctrl',),
        'outputs_label': ('ctrl',),
        'inner': 'Matrix',
        'label': 'matrix create',
        'tooltip': {
            'label': 'Matrix',
            'desc': 'Создание матрицы',
            'inputs': [
                ('Вход', 'Количество строк'),
                ('Вход', 'Количество столбцов'),
            ],
            'outputs': [
                ('Выход', 'Завершающий выход'),
            ],
            'adds': 'В описании к Узлу должно быть указано имя переменной. Можно установить тип данных в массиве, записав тип после имени переменной ($int, $real, $bool, $char, $num, $str, $any)',
        }
    },
    'matrix set': {
        'inputs': ('int', 'int', 'sep', 'any'),
        'inputs_label': ('index y', 'index x', 'sep', 'value'),
        'outputs': ('ctrl',),
        'outputs_label': ('ctrl',),
        'inner': 'Matrix\nSet',
        'label': 'matrix set',
        'tooltip': {
            'label': 'Matrix Set',
            'desc': 'Изменение значения матрицы',
            'inputs': [
                ('Вход', 'Номер строки'),
                ('Вход', 'Номер столбца'),
                ('Вход', 'Значение на установку'),
            ],
            'outputs': [
                ('Выход', 'Завершающий выход'),
            ],
            'adds': 'В описании к Узлу должно быть указано имя переменной',
        }
    },
    'matrix get': {
        'inputs': ('int', 'int'),
        'inputs_label': ('index y', 'index x'),
        'outputs': ('any',),
        'outputs_label': ('value',),
        'inner': 'Matrix\nGet',
        'label': 'matrix get',
        'tooltip': {
            'label': 'Matrix Get',
            'desc': 'Получение значения матрицы',
            'inputs': [
                ('Вход', 'Номер строки'),
                ('Вход', 'Номер столбца'),
            ],
            'outputs': [
                ('Выход', 'Значение на указанной позиции'),
            ],
            'adds': 'В описании к Узлу должно быть указано имя переменной',
        }
    },
    'matrix get and set': {
        'inputs': ('int', 'int', 'sep', 'any'),
        'inputs_label': ('index y', 'index x', 'sep', 'value'),
        'outputs': ('any',),
        'outputs_label': ('value',),
        'inner': 'Matrix\nG&S',
        'label': 'matrix get and set',
        'tooltip': {
            'label': 'Matrix Get',
            'desc': 'Изменение и получение значения матрицы',
            'inputs': [
                ('Вход', 'Номер строки'),
                ('Вход', 'Номер столбца'),
                ('Вход', 'Значение на установку'),
            ],
            'outputs': [
                ('Выход', 'Значение на указанной позиции'),
            ],
            'adds': 'В описании к Узлу должно быть указано имя переменной. Если не указать значение элемента, то Узел вернет элемент без изменения',
        }
    },
}

nodes_info = {}
nodes_info.update(base_nodes_info)
nodes_info.update(structure_nodes_info)

base_nodes_lib_order = ['run', 'stop', 'const', 'const ctrl', 'input', 'print', 'print ctrl', 'if', 'add', 'sub',
                        'mult', 'division', 'exp', 'var', 'var set', 'var get', 'join', 'concatenate', 'format',
                        'bool', 'and', 'or', 'not and', 'not or', 'equal', 'not', 'not equal', 'xor', 'greater',
                        'greater or equal', 'less', 'less or equal', 'inc', 'dec', 'abs', 'div', 'mod', 'inv', 'trunc',
                        'round', 'for', 'counter', 'while', 'in', 'for ext', 'foreach', 'merge', 'delay',
                        'value switch', 'ctrl', 'timer', 'wait', 'type', 'get type', 'error', 'warning', 'random',
                        'random int', 'random num', 'random seed']
structure_nodes_lib_order = ['length', 'array create', 'array set', 'array get', 'array get and set', 'list create',
                             'list set', 'list get', 'list get and set', 'list remove', 'dict create', 'dict insert',
                             'dict find', 'dict insert and find', 'dict remove', 'matrix create', 'matrix set',
                             'matrix get', 'matrix get and set']
