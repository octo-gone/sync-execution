---
layout: default_no_header
return_page: /tutorials
return_title: К обучению
title: Продвинутое создание узлов
---

## Создание узлов с функционалом  

Главное отличие узлов с функционалом и функций в том, что первые выполняются внутри одного узла, а функции 
выполняются соответственно описанной подпрограммы из узлов внутри. Если поиск максимума в функции может 
занимать 30 операций для  сравнения трех чисел, то поиск максимума в запрограммированном узле может 
выполнятся за 1 операцию.

### Какие знания требуются

Первоначально требуется знание Python и того, как работает в нем ООП. Если есть знание объектно-ориентированного 
программирования (независимого от языка), то второй пункт можно опустить. Если ООП вовсе не известно, но хочется 
создавать узлы самому, то тогда требуется понимание того, как каждый узел взаимодействует с окружением и что для этого
нужно (какие функции, переменные и т.п.).

### Быстрый переход

В данной статье описаны следующие возможности в работе с узлом:

- [Получение данных с входов узла][working_with_input]
- [Работа с выходом][working_with_output]
- [Взаимодействие с атрибутами и переменными][working_with_attr]
- [Изменение состояния][working_with_attr]
- [Взаимодействие со входным сигналом][working_with_set_state]
- [Пример создания узла][new_node]

## Что используется в работе узла

Общие переменные для всех узлов: 

- **variables** - список всех переменные
- **struct_variables** - список всех структурных переменных
- **nodes** - список всех узлов

Базовые методы класса узла:

- **get_actual_state()** - получение реального состояния
- **update_connections()** - обновление соединений
- **set_state(state, input_index, \*\*kwargs)** - изменение состояния узла
- **update(state)** - обновление узла

Часто **изменяемые** базовые методы класса узла при написании функционала:

- **\_\_init\_\_(data)** - создание экземпляра класса (узла)
- **set_active(output_index)** - активация следующих узлов
- **update_active()** - обновление узла в активном состоянии
- **update_waiting()** - обновление узла в ожидании
- **update_inactive()** - обновление узла в деактивированном состоянии

Часто **используемые** методы класса узла при написании функционала:

- **get_actual_input(input_index)** - получение входного номера коннектора по номеру подключения
- **get_actual_output(output_index)** - получение выходного номера коннектора по номеру подключения
- **get_value(input_index, mult=False)** - получение значения из узла по указанному индексу
- **set_value(value, index)** - сохранение значение по указанному номеру

Атрибуты класса используемые в вычислениях:

- **id** - идентификатор узла на диаграмме
- **raw_data** - необработанная информацию об узле
- **input_values** - список значений входов
- **output_values** - список значений выходов
- **input_connectors** - список входов
- **output_connectors** - список выходов
- **actual_inputs** - словарь соответствий входов и коннекторов
- **actual_outputs** - словарь соответствий выходов и коннекторов
- **sub_state** - дополнительное состояние
- **scope** - область видимости
- **pos** - позиция на диаграмме
- **size** - размер в диаграмме

Часто используемые атрибуты класса:

- **name** - имя узла
- **desc_value** - описание узла на диаграмме
- **inputs** - список узлов подключенных ко входам
- **outputs** - список узлов подключенных к выходам
- **state** - состояние

### Структура класса узла

Для работы узла требуется класс, который будет обрабатывать все его действия. Для этого нужно перейти в скрипт
**user_nodes.py**. Внутри него нужно положить класс узла с определенной структурой, а после программа сама поймет что делать.
Создание узла основывается на свойствах ООП - полиморфизме и наследовании. Наследование позволяет получать все требуемые
для работы функции не расписывая их заново для каждого класса, а полиморфизм позволяет настроить класс под определенный
функционал. Все измененные методы класса существовали в родительском в неком общем виде.

Базовая структура любого пользовательского узла должна выглядеть следующим образом:
```python
class Node<ИмяКлассаУзла>(base.Node):
    name = "..."  # Наименование узла
    desc = {...}  # Описание узла

    def update_waiting(self):
        <Операции, когда узел обрабатывается>

    def update_active(self):
        <Операции, когда узел завершил обработку>
```  

Имя класса должно быть уникальном в скрипте **user_nodes.py**. Наименование узла должно совпадать с именем используемые 
в создании узла (**label**, **sync_name**). Методы **update_waiting** и **update_active** должны присутствовать в классе в любом
случае, даже если не используются. **Описание узла должно быть в формате указанном в данной [статье][creating_tutorial_desc].**
Иначе программа не поймет как связывать узел с другими. 

> **Что такое self?**  
>
> **self** - это переменная, которая хранит ссылку на экземпляр объекта, создаваемый конструктором. 
> Иначе говоря, если требуется использовать именно созданный объект, а не целиком класс, то требуется написать **self** и через
> точку метод или атрибут требуемый в вычислениях. **self.attr** - обращение к атрибуту или методу объекта класса, 
> переменной или методу класса. В Python ссылку на объект или **self** также требуется прописывать как аргумент функции, тем
> самым показывая, что данная функция работает с объектом и требует его.

#### Получение данных со входов узла <a id="input"></a>

Рассмотрим случай, когда узел был активирован одним из входов. От узла требуется получить значения с 0 и 2 входов, а 
после получения нужно переключить узел в состояние ACTIVE. Для выполнения такой задачи требуется изменить метод **update_waiting**, 
использовать метод **get_value** и атрибуты **state** с **inputs**. Изменять состояние узла через **set_state** нельзя, этот метод 
используется только извне класса.

```python
class NodeExample1(base.Node):
    name = "example_1"

    def update_waiting(self):
        # получение значений
        value_0 = self.get_value(0)
        value_2 = self.get_value(2)
        # переключение
        self.state = ACTIVE

    def update_active(self):
        self.state = INACTIVE
```

> Метод **update_active** обрабатывается когда узел был переключен в состояние ACTIVE (момент активации следующих узлов).
> В следующих примерах он будет опущен.

Данный узел выполнит свою программу, однако что делать, если ко 2 не подключен узел, а значение требуется иметь обязательно.
Исправить это можно используя **inputs**, тем самым реализовывая значение по умолчанию.

```python
class NodeExample1(base.Node):
    name = "example_1"

    def update_waiting(self):
        value_0 = self.get_value(0)
        # если ни один узел не подключен,
        # то self.inputs[2] будет пустым списком
        if not self.inputs[2]:
            value_2 = 0
        else:
            value_2 = self.get_value(2)
        self.state = ACTIVE

    ...
```

Иногда входные узлы не могут отдать данные, потому требуется проверять, есть ли значение на входе. Это можно сделать
тем же методом **get_value**, такое возможно, так как при отсутствии значения в выходе узла будет сохранено значение `None`.

```python
class NodeExample1(base.Node):
    name = "example_1"

    def update_waiting(self):
        value_0 = self.get_value(0)
        if not self.inputs[2]:
            value_2 = 0
        else:
            value_2 = self.get_value(2)
        # проверка значений
        if value_0 is not None and value_2 is not None:        
            self.state = ACTIVE
    
    ...
```

> Проверять на равенство None желательно через конструкцию `<v> is None` или `<v> is not None`

#### Работа с выходом <a id="output"></a>

Кроме получения данных, узлу требуется активировать следующие узлы и/или передать в них данные. Для сохранения данных
в порты используется метод **set_value**, в него передается значение и номер выхода. Для активации следующего узла 
используется метод **set_active**, он получает на вход лишь номер выхода и все подключенные к этому входу узлы будут
активированы (переключены в состояние WAITING).

Попробуем создать инвертирующий узел, на вход подается значение, на выходе значение с минусом.

```python
class NodeExample2(base.Node):
    name = "example_2"

    def update_waiting(self):
        value_0 = self.get_value(0)
        self.set_value(-value_0, 0)
        self.state = ACTIVE

    def update_active(self):
        self.state = INACTIVE
```

Данный класс будет сохранять значение в выходе узла, однако последующей активации не будет, для этого требуется изменить 
метод **update_active**.

```python
class NodeExample2(base.Node):
    name = "example_2"

    def update_waiting(self):
        value_0 = self.get_value(0)
        self.set_value(-value_0, 0)
        self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE
```

Если посмотреть на реализацию инвертора в проекте, то можно увидеть сходство. В стандартной реализации дополнительно есть
проверка на наличие значения.

```python
class NodeInv(base.Node):
    """
    Class for node 'inv' (inverse). Node that returns number with different number sign.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If node has input value then function sets to output inverse number value.
        """
        if self.get_value(0) is not None:
            self.set_value(-self.get_value(0), 0)
            self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE
```

> Хорошим улучшением было бы добавление проверки на то, что входное значение является значением с возможностью инвертирования.

#### Взаимодействие с атрибутами и переменными классов <a id="attr"></a>

Много информации для вычислений можно получить из атрибутов и переменных классов. Например в описании к узлу есть данные, 
которые могут использоваться в вычислениях, в Sync предусмотрена возможность
получить значения оттуда через атрибут **desc_value**. Примером работы может стать упрощенный узел **Print**.
Если данные на вход узла не подаются, то узел постарается забрать данные из описания.

```python
class NodePrint(base.Node):
    def update_waiting(self):
        value = self.get_value(0)
        value = value if value is not None else self.desc_value
        print(f"{utils.iteration}:", value)
        self.state = INACTIVE

    ...
```

Некоторые данные требуется вводить до того, как узел будет даже впервые обработан. Для этого существует конструктор, в котором
и стоит создавать атрибуты класса. Рассмотрим узел **Var**, который работает с переменными. Тип данных внутри него можно 
определить используя конструкцию "имя-переменной$тип-данных". А для правильной работы будет лучше забрать тип данных и
оставить в описании лишь имя переменной (тем самым упростив дальнейшее взаимодействие с описанием).

```python
class NodeVar(base.Node):
    def __init__(self, data):
        super().__init__(data)
        self.value_type = None
        for value_type in value_types.keys():
            if self.desc_value.endswith(value_type):
                self.value_type = value_types[value_type]
                self.desc_value = self.desc_value[:self.desc_value.index("$")]
                break

    ...
```

> **value_type** - атрибут созданный для этого класса (хранит переводчик типа данных или конструктор требуемого класса),
> **value_types** - переменная используемая для определения типа данных по имени типа (для "num" тип данных будет "number").
> 
> **super().\_\_init\_\_(data)** - данная строка позволяет запустить инициализацию родительского класса, который как раз и создает
> все базовые переменные ("desc_value" и т.п.), а также подготавливает узел к работе с другими узлам.

Так как программа использует понятие области видимости, то для правильного управления переменными требуется использовать
атрибут **scope**, который содержит в себе идентификатор области видимости. Также требуется хранить информацию о переменных
где-то. Для этого существует переменная классов (общая для всех классов) - **variables**. Внутри него находится в определенной 
структуре имена и данные переменных.

```python
class NodeVar(base.Node):
    ...

    def update_inactive(self):
        var_name = f"{self.scope}$" + self.desc_value
        if var_name in self.variables:
            value = self.variables[var_name]
            if self.value_type is not None:
                self.set_value(self.value_type(value), 0)
            else:
                self.set_value(utils.coercion(value), 0)
    ...
```

> **utils.coercion** - функция автоматически подбирающая тип для входных данных

#### Взаимодействие со входным сигналом <a id="set-state"></a>

Самым полезным методом для комплексных функций, например для циклов или счетчиков, является метод **set_state**. Он 
исполняется автоматически для узлов при использовании функции **set_active**. Базовая структура (неизменная) описана ниже.
Вне зависимости от значений аргументов функция изменит состояние узла.

```python
class NodeExample3(base.Node):
    ...

    def set_state(self, state, input_index, **kwargs):
        """
        Change state function, runs when other nodes are trying to activate the current node. Can be redefined.

        :param str state: new state
        :param int input_index: index of input from which the state change has been requested
        :param kwargs: additional arguments if needed (obj and output_index)
        """
        self.state = state
    
    ...
``` 

Однако в некоторых случаях так не должно быть, например в циклах, где при подаче только на определенный вход программа должна
обработать сигнал и вывести значение, а при подаче на любой другой - проигнорировать. Специально для таких случаев добавлен
аргумент **input_index**, который показывает по какому именно входу подается сигнал. 

Попробуем реализовать проверку того, что только на первый вход может подаваться сигнал, а на все остальные нет.

```python
class NodeExample3(base.Node):
    ...

    def set_state(self, state, input_index, **kwargs):
        if input_index == 0:
            self.state = state
    ...
``` 

Сделаем аналогичную проверку, но узел должен проверить, что входное значение равно значению из описания (как ключ к шкатулке).

```python
class NodeExample3(base.Node):
    ...

    def set_state(self, state, input_index, **kwargs):
        if input_index == 0 and self.get_value(0) == self.desc_value:
            self.state = state
    ...
``` 

## Пример создания узла <a id="new-node"></a>

Финальной частью статьи будет создание узла: счетчик с минимальным значением 0 и максимальным 15, где один входной порт 
увеличивает значение, а другой уменьшает, переход за минимум и максимум цикличен (-1=15 и 16=0).
Реализовать данный узел можно несколькими способами. Однако первоначально нужно описать узел и создать его с помощью
скрипта *new_nodes.py*

Изменим переменную **node** следующим образом

```python
node = {
    'inner': 'C16',
    'label': 'count 16',
    'inputs': ('ctrl', 'ctrl'),
    'outputs': ('int',),
    'tooltip': {
        'label': 'Count 16 (+/-)',
        'desc': 'Счетчик 16',
        'input': [
            ('Вход', 'Увеличивающий вход'),
            ('Вход', 'Уменьшающий вход'),
        ],
        'outputs': [
            ('Выход', 'Значение'),
        ],
        'adds': 'Счетчик с пересчетом 16, где один входной порт увеличивает, а другой уменьшает',
    }
}
```

Воспользуемся созданием библиотеки, для получения уже готового узла.

```python
svg_save_folder = "resources/generated/svg/"
lib_save_folder = "resources/libraries/"
library_name = "c16"
nodes_info = [
    node
]
generate_library(library_name, nodes_info, svg_save_folder, lib_save_folder)
```

Проверим результат выполнения программы, импортировав полученную библиотеку в [Draw.io][drawio].

<img src="{{site.baseurl}}/resources/tutorials/advanced-creating/01_c16_node.png"/>

Проведем аналогичные операции, но теперь вместо библиотеки создадим функцию, и попробуем реализовать программу
через доступные узлы.

<img src="{{site.baseurl}}/resources/tutorials/advanced-creating/02_c16_func.png"/>

Составленная программа немного сложна, так как требуется при первом запуске создавать переменную, если она была создана, то
достаточно будет складывать или вычитать.

<img src="{{site.baseurl}}/resources/tutorials/advanced-creating/03_c16_func_prog.png"/>

Тестовая программа будет выглядеть просто, на один из входов подается значение из цикла, подача на другой вход была
проверена и работает. 

<img src="{{site.baseurl}}/resources/tutorials/advanced-creating/04_c16_test.png"/>

После запуска функции видно, что на такую программу тратится огромное количество шагов, но результат правильный.

<img src="{{site.baseurl}}/resources/tutorials/advanced-creating/05_c16_func_work.png"/>

Теперь реализуем класс и его функционал. Если сразу запустить программу, то можно увидеть, что программа вернет сообщение
об ошибке `0: no built-in nodes found with name 'count 16'`. Это значит, что узел не был найден, исправим это.

Первым делом требуется ввести описание узла

```python
class NodeCount16(base.Node):
    name = "count 16"
    desc = {
        'inner': 'C16',
        'label': 'count 16',
        'inputs': ('ctrl', 'ctrl'),
        'outputs': ('int',),
        'tooltip': {
            'label': 'Count 16 (+/-)',
            'desc': 'Счетчик 16',
            'input': [
                ('Вход', 'Увеличивающий вход'),
                ('Вход', 'Уменьшающий вход'),
            ],
            'outputs': [
                ('Выход', 'Значение'),
            ],
            'adds': 'Счетчик с пересчетом 16, где один входной порт увеличивает, а другой уменьшает',
        }
    }
    ...
```

Введем 2 переменные, одна будет счетчиком, а вторая определять что нужно сделать со значением. Видно, что переменную мы ввели сразу,
потому дой большой проверки не будет.

```python
class NodeCount16(base.Node):
    ...
    def __init__(self, data):
        super().__init__(data)
        self.count = 0
        self.operation = None
    ...
```

Сделаем изменение счетчика.

```python
class NodeCount16(base.Node):
    ...
    def update_waiting(self):
        if self.operation == "+":
            new_value = (self.count + 1) % 16
            self.set_value(new_value, 0)
            self.count = new_value
        elif self.count == 0:
            new_value = 15
            self.set_value(new_value, 0)
            self.count = new_value
        else:
            new_value = self.count - 1
            self.set_value(new_value, 0)
            self.count = new_value
        self.state = ACTIVE
    ...
```

Остается сделать переключение из состояния ACTIVE и обработку входных сигналов.

```python
class NodeCount16(base.Node):
    ...
    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE

    def set_state(self, state, input_index, **kwargs):
        if input_index == 0:
            self.operation = "+"
        else:
            self.operation = "-"
        self.state = state
```

Программирование закончилось, осталось лишь запустить программу и увидеть разницу в результатах. Узел будет работать намного
быстрее функции, и в то же время выполнять все тот же функционал.

<img src="{{site.baseurl}}/resources/tutorials/advanced-creating/06_c16_node_work.png"/>

Класс целиком:

```python
class NodeCount16(base.Node):
    name = "count 16"
    desc = {
        'inner': 'C16',
        'label': 'count 16',
        'inputs': ('ctrl', 'ctrl'),
        'outputs': ('int',),
        'tooltip': {
            'label': 'Count 16 (+/-)',
            'desc': 'Счетчик 16',
            'input': [
                ('Вход', 'Увеличивающий вход'),
                ('Вход', 'Уменьшающий вход'),
            ],
            'outputs': [
                ('Выход', 'Значение'),
            ],
            'adds': 'Счетчик с пересчетом 16, где один входной порт увеличивает, а другой уменьшает',
        }
    }

    def __init__(self, data):
        super().__init__(data)
        self.count = 0
        self.operation = None

    def update_waiting(self):
        if self.operation == "+":
            new_value = (self.count + 1) % 16
            self.set_value(new_value, 0)
            self.count = new_value
        elif self.count == 0:
            new_value = 15
            self.set_value(new_value, 0)
            self.count = new_value
        else:
            new_value = self.count - 1
            self.set_value(new_value, 0)
            self.count = new_value
        self.state = ACTIVE

    def update_active(self):
        self.set_active(0)
        self.state = INACTIVE

    def set_state(self, state, input_index, **kwargs):
        if input_index == 0:
            self.operation = "+"
        else:
            self.operation = "-"
        self.state = state
```

[working_with_input]: {{site.baseurl}}/tutorials/advanced-creating#input
[working_with_output]: {{site.baseurl}}/tutorials/advanced-creating#output
[working_with_attr]: {{site.baseurl}}/tutorials/advanced-creating#attr
[working_with_set_state]: {{site.baseurl}}/tutorials/advanced-creating#set-state
[new_node]: {{site.baseurl}}/tutorials/advanced-creating#new-node

[creating_tutorial]: {{site.baseurl}}/tutorials/creating#content
[creating_tutorial_desc]: {{site.baseurl}}/tutorials/creating#description
[functions_tutorial]: {{site.baseurl}}/tutorials/functions#content

[index]: {{site.baseurl}}/index
[tutorials]: {{site.baseurl}}/tutorials#content
[drawio]: https://app.diagrams.net/?splash=0&libs=0&clibs=Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/base.drawio;Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/structure.drawio
[replit]: https://repl.it/github/octo-gone/sync-execution