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
может забрать значения из списка, массива или словаря указанного в описании. Форматирование аналогично форматированию из
Python с использованием фигурных скобок. 

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/misc/09_format.png"/>

### Join

**Join** - узел, склеивающий значения из указанной в описании структурной переменной (список или словарь). 

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/misc/10_join.png"/>


[index]: {{site.baseurl}}/index
[tutorials]: {{site.baseurl}}/tutorials#content
[docs]: {{site.baseurl}}/docs#content
[drawio]: https://app.diagrams.net/?splash=0&libs=0&clibs=Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/base.drawio;Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/structure.drawio
[replit]: https://repl.it/github/octo-gone/sync-execution