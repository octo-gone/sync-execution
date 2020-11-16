---
layout: tutorials
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

Базовая структура любого пользовательского узла должна выглядеть следующим образом:
```python
class Node<ИмяКлассаУзла>(base.Node):
    name = "<Наименование узла>"

    def update_waiting(self):
        <Операции, когда узел обрабатывается>

    def update_active(self):
        <Операции, когда узел завершил обработку>
```  

Имя класса должно быть уникальном в скрипте **user_nodes.py**. Наименование узла должно совпадать с именем используемые 
в создании узла ("label", "sync_name"). Методы "update_waiting" и "update_active" должны присутствовать в классе в любом
случае, даже если не используются.

> **Что такое self?**  
>
> **self** - это переменная, которая хранит ссылку на экземпляр объекта, создаваемый конструктором. 
> Иначе говоря, если требуется использовать именно созданный объект, а не целиком класс, то требуется написать **self** и через
> точку метод или атрибут требуемый в вычислениях. self.<attr> - обращение к атрибуту или методу объекта класса, 
> переменной или методу класса. В Python **self** также требуется прописывать как аргумент функции, тем
> самым показывая, что данная функция работает с объектом и требует его.

#### Получение данных со входов узла <a id="working-with-input"></a>

Рассмотрим случай, когда узел был активирован одним из входов. От узла требуется получить значения с 0 и 2 входов, а 
после получения нужно переключить узел в состояние ACTIVE. Для выполнения такой задачи требуется изменить метод "update_waiting", 
использовать метод "get_value" и атрибуты "state" с "inputs". Изменять состояние узла через "set_state" нельзя, этот метод 
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

> Метод "update_active" обрабатывается когда узел был переключен в состояние ACTIVE (момент активации следующих узлов).
> В следующих примерах он будет опущен.

Данный узел выполнит свою программу, однако что делать, если ко 2 не подключен узел, а значение требуется иметь обязательно.
Исправить это можно используя "inputs", тем самым реализовывая значение по умолчанию.

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
тем же методом "get_value", такое возможно, так как при отсутствии значения в выходе узла будет сохранено значение `None`.

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

#### Работа с выходом <a id="working-with-output"></a>

Кроме получения данных, узлу требуется активировать следующие узлы и/или передать в них данные. Для сохранения данных
в порты используется метод "set_value", в него передается значение и номер выхода. Для активации следующего узла 
используется метод "set_active", он получает на вход лишь номер выхода и все подключенные к этому входу узлы будут
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
метод "update_active".

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

#### Взаимодействие с атрибутами и переменными классов <a id="working-with-attr"></a>

Так как в описании к узлу есть данные, которые могут использоваться в вычислениях, в классах предусмотрена возможность
получить значения оттуда. Атрибут "desc_value" как раз и создан для этого. Примером работы может стать упрощенный узел "Print".
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
и стоит создавать атрибуты класса. Рассмотрим узел "Var", который работает с переменными. Тип данных внутри него можно 
определить используя конструкцию "<имя переменной>$<тип данных>". А для правильной работы будет лучше забрать тип данных и
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

> "value_type" - атрибут созданный только для этого класса (хранит переводчик типа данных или конструктор требуемого класса),
> "value_types" - переменная используемая для определения типа данных по имени типа (для "num" тип данных будет "number").
> 
> "super().\_\_init\_\_(data)" - данная строка позволяет запустить инициализацию родительского класса, который как раз и создает
> все базовые переменные ("desc_value" и т.п.), а также подготавливает узел к работе с другими узлам.

Так как программа использует понятие области видимости, то для правильного управления переменными требуется использовать
атрибут "scope", который содержит в себе идентификатор области видимости. Также требуется хранить информацию о переменных
где-то. Для этого существует переменная классов (общая для всех классов) - "variables". Внутри него находится в определенной 
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

> "utils.coercion" - функция автоматически подбирающая тип для входных данных

# В процессе написания ✍(◔◡◔)

[working_with_input]: {{site.baseurl}}/tutorials/advanced-creating#working-with-input
[working_with_output]: {{site.baseurl}}/tutorials/advanced-creating#working-with-output
[working_with_attr]: {{site.baseurl}}/tutorials/advanced-creating#working-with-attr

[index]: {{site.baseurl}}/index
[tutorials]: {{site.baseurl}}/tutorials#content
[drawio]: https://app.diagrams.net/?splash=0&libs=0&clibs=Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/base.drawio;Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/structure.drawio
[replit]: https://repl.it/github/octo-gone/sync-execution