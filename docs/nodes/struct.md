---
layout: default_no_header
return_page: /docs/nodes
return_title: К узлам
title: Struct
---
## Узлы для работы со структурным переменными

Для упрощения работы с множеством данных можно использовать структурные переменные.

### Ключевые слова типов

Работа с данными и типами немного упрощена использованием ключевых слов. Если написать после числа `$bool`, то данное число
автоматически конвертируется (если узел позволяет это делать) в логическую единицу или ноль. Для такой работы доступны следующие 
ключевые слова. **Данные ключевые слова могут указать тип при создании структурной переменной.**

| Тип | Описание | Ключ | Значение |
| :---: | --- | --- | --- |
| **int** | целочисленный тип | $int | 0 |
| **real** | вещественный тип | $real | 0.0 |
| **number** | обобщение int и real | $num, $number | 0 |
| **char** | символьный тип | $char | Пустая строка |
| **str** | строковый тип | $string, $str | Пустая строка |
| **bool** | логический тип | $bool | False |

### Length

**Length** - узел, определяющий длину структурной переменной. Узел возвращает длину списка или словаря (количество пар) 
с указанным в описании именем.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/struct/19_length.png"/>

## Array

Массив - структура данных, которая представляет собой последовательность значений, где длина данной последовательности фиксирована.

### Create

**Array Create** - узел создания массива. Для создания требуется указать имя в описании и передать длину массива. 
При указании типа данных массив заполняется значениями по умолчанию.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/struct/01_array_create.png"/>

### Get and Set

**Array Get and Set** - узел установки и получения значения из массива. Для получения или изменения требуется указать имя в 
описании и индекс значения. Для установки значения требуется передать значение на вход. Узел автоматически возвращает
на выходе значение по указанному индексу.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/struct/02_array_get_and_set.png"/>

### Get

**Array Get** - узел получения значения из массива. Для получения требуется указать имя в 
описании и индекс значения.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/struct/03_array_get.png"/>

### Set

**Array Set** - узел установки значения в массив. Для установки требуется указать имя в 
описании, индекс значения и передать значение на вход.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/struct/04_array_set.png"/>

## Dict

Словарь - структура данных, которая состоит из пары ключ-значение. Ключи уникальны. Значения могут повторятся.

### Create

**Dict Create** - узел создания словаря. Для создания требуется указать имя в описании, передать тип ключа и тип данных. 

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/struct/05_dict_create.png"/>

### Insert and Find

**Dict Insert and Find** - узел установки и получения значения из словаря. Для получения или изменения требуется указать имя в 
описании и значение ключа. Для установки значения требуется передать значение на вход. Узел автоматически возвращает
на выходе значение по указанному ключу.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/struct/06_dict_insert_and_find.png"/>

### Find

**Dict Find** - узел получения значения из словаря. Для получения требуется указать имя в 
описании и значение ключа.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/struct/07_dict_find.png"/>

### Insert

**Dict Insert** - узел установки значения в словарь. Для установки требуется указать имя в 
описании, значение ключа и передать значение на вход.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/struct/08_dict_insert.png"/>

### Remove

**Dict Remove** - узел удаления значения из словаря. Для удаления требуется указать имя в 
описании и значение ключа.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/struct/09_dict_remove.png"/>

## List

Список - структура данных, которая представляет собой последовательность значений, длина данной последовательности изменяема.

### Create

**List Create** - узел создания списка. Для создания требуется указать имя в описании. 

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/struct/10_list_create.png"/>

### Get and Set

**List Get and Set** - узел установки и получения значения из списка. Для получения, изменения или установки требуется указать имя в 
описании. Для изменения значения требуется передать значение на вход и индекс. Для добавления значения требуется передать 
только значение на вход. Узел автоматически возвращает на выходе значение по указанному индексу или только что введенное.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/struct/11_list_get_and_set.png"/>

### Get

**List Get** - узел получения значения из списка. Для получения требуется указать имя в 
описании и индекс значения.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/struct/12_list_get.png"/>

### Set

**List Set** - узел установки значения в список. Для установки или изменения требуется указать имя в 
описании. Для изменения значения требуется передать значение на вход и индекс. Для добавления значения требуется передать 
только значение на вход.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/struct/13_list_set.png"/>

### Remove

**List Remove** - узел удаления значения из списка. Для удаления требуется указать имя в описании и индекс. 

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/struct/14_list_remove.png"/>

## Matrix

Матрица - структура данных, которая представляет собой массивы вложенные в массивы или последовательность значений, 
где каждое значение расположено под двумя индексами - строками и столбцами. Длина строк и столбцов фиксирована.

### Create

**Matrix Create** - узел создания матрицы. Для создания требуется указать имя в описании и передать длину строк и столбцов. 
При указании типа данных матрицы заполняется значениями по умолчанию.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/struct/15_matrix_create.png"/>

### Get and Set

**Matrix Get and Set** - узел установки и получения значения из матрицы. Для получения или изменения требуется указать имя в 
описании и индексы строки и столбца. Для установки значения требуется передать значение на вход. Узел автоматически возвращает
на выходе значение по указанным индексам.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/struct/16_matrix_get_and_set.png"/>

### Get

**Matrix Get** - узел получения значения из матрицы. Для получения требуется указать имя в 
описании и индексы строки и столбца.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/struct/17_matrix_get.png"/>

### Set

**Matrix Set** - узел установки значения в массив. Для изменения требуется указать имя в описании, индексы 
строки и столбца и передать значение на вход.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/struct/18_matrix_set.png"/>

[index]: {{site.baseurl}}/index
[tutorials]: {{site.baseurl}}/tutorials#content
[docs]: {{site.baseurl}}/docs#content
[drawio]: https://app.diagrams.net/?splash=0&libs=0&clibs=Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/base.drawio;Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/structure.drawio
[replit]: https://repl.it/github/octo-gone/sync-execution