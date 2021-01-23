---
layout: default_no_header
title: Miscellaneous
return_page: /docs/nodes
return_title: К узлам
---
## Разнообразные узлы

В данной группе узлы, которые не получилось классифицировать. 

### Value Switch

**Value Switch** - узел-воронка. Используется как передатчик нескольких значений с выходов нескольких узлов на 
вход для одного узла, например, когда требуется напечатать значения с разных веток программы через один узел Print.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/misc/01_value_switch.png"/>

### Type

**Type** - узел, определяющий тип данных со входа и возвращающий тип как объект.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/misc/02_type.png"/>

### Get Type

**Get Type** - узел, возвращающий тип данных как объект указанный в описании и значение по умолчанию.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/misc/03_get_type.png"/>

### Random

**Random** - узел, возвращающий случайное значение от 0 до 1. Для изменения последовательности генерации случайных чисел
можно воспользоваться узлом Random Seed.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/misc/04_random.png"/>

### Random Int

**Random Int** - узел, возвращающий случайное целое значение от указанной нижней границы до верхней границы. Для изменения 
последовательности генерации случайных чисел можно воспользоваться узлом Random Seed.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/misc/05_random_int.png"/>

### Random Num

**Random Num** - узел, возвращающий случайное значение от указанной нижней границы до верхней границы. Для изменения 
последовательности генерации случайных чисел можно воспользоваться узлом Random Seed.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/misc/06_random_num.png"/>

### Random Seed

**Random Seed** - узел, позволяющий изменить последовательность генерации случайных чисел путем изменения начального 
состояния генератор. Для изменения нужно подать значение на вход.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/misc/07_random_seed.png"/>

### Concatenate

**Concatenate** - узел-сумматор-строк. Позволяет склеить подряд значения с входов узла.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/misc/08_concatenate.png"/>

### Format

**Format** - узел-форматер. Позволяет привести к указанному формату значение со входа. Вместо значения со входа узел
может забрать значения из списка, массива или словаря указанного в описании. Форматирование идет по следующему принципу:

1. Если указано значение со входа, то обработка структурных переменных не происходит
2. Значения из списка или массива ставятся в соответствие каждой группе последовательно
3. Значения из словаря ставятся в соответствие группе с указанным именем
4. Каждая группа представляет собой следующую последовательность (в квадратных скобках указаны не обязательные 
значения) - `{<name>[!<conversion>][:[[<fill>]<align>][<sign>][#][0][<width>][,][.<precision>][<type>]]}`
    - **name** - имя в списке значений, индекс или пусто (если требуется брать значения последовательно)
    - **conversion** - представление значения `r` или `s`
    - **fill** - символ заполнитель (все кроме `{` и `}`)
    - **align** - вариант выравнивания `<`, `>`, `=` или `^` (выравнивание по левому краю / по правому / символы будут после
    знаки и перед цифрами / выравнивание по центру)
    - **sign** - обозначение знака числа `+`, `-` или ` ` (знак будет указан для любых чисел / только для отрицательных /
    для отрицательных будет "-", а для положительных пробел)
    - **width** - ширина выравнивания
    - **precision** - точность числа
    - **type** - тип данных `c`, `d`, `e`, `f`, `g`, `o`, `s`, `x`, или `%`

Типы данных:

- `d` - десятичное число
- `s` - строка
- `c` - символ или код символа
- `o` - число в восьмеричной системе
- `x` - число в шестнадцатеричной системе
- `f` - число с плавающей точкой
- `e` - число с плавающей точкой с экспонентой
- `g` - число с плавающей точкой с автоматическим добавлением экспоненты
- `%` - представление числа от 0 до 1 в виде числа от 0 до 100 со знаком "%"

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/misc/09_format.png"/>

### Join

**Join** - узел, склеивающий значения из указанной в описании структурной переменной (список или словарь). 

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/misc/10_join.png"/>


[index]: {{site.baseurl}}/index
[tutorials]: {{site.baseurl}}/tutorials#content
[docs]: {{site.baseurl}}/docs#content
[drawio]: https://app.diagrams.net/?splash=0&libs=0&clibs=Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/base.drawio;Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/structure.drawio
[replit]: https://repl.it/github/octo-gone/sync-execution