---
layout: default_no_header
return_page: /docs/nodes
return_title: К узлам
title: Memory
---
## Узлы для работы с памятью

Как известно, большинство алгоритмов не могут обходиться без использования памяти.  

### Ключевые слова типов

Работа с данными и типами немного упрощена использованием ключевых слов. Если написать после числа `$bool`, то данное число
автоматически конвертируется (если узел позволяет это делать) в логическую единицу или ноль. Для такой работы доступны следующие 
ключевые слова.

| Тип | Описание | Ключ |
| :---: | --- | --- |
| **int** | целочисленный тип | $int |
| **real** | вещественный тип | $real |
| **number** | обобщение int и real | $num, $number |
| **char** | символьный тип | $char |
| **str** | строковый тип | $string, $str |
| **bool** | логический тип | $bool |

### Constant

**Constant** - узел-константа, постоянно имеет на выходе указанное в описании значение. Если указать после значения 
через символ `$` ключевое слово типа данных, значение на выходе будет автоматически сконвертировано в соответствующий тип.

<img class="img-small" src="{{site.baseurl}}/resources/docs/nodes/mem/01_constant.png"/>

### Constant with Ctrl

**Constant with Ctrl** - узел-константа, постоянно имеет на выходе указанное в описании значение, однако позволяет 
запустить узел после себя, если сигнал был подан на вход. Если указать после значения через символ `$` ключевое слово 
типа данных, значение на выходе будет автоматически сконвертировано в соответствующий тип.

<img class="img-small" src="{{site.baseurl}}/resources/docs/nodes/mem/02_constant_with_ctrl.png"/>

### Variable

**Variable** - узел-переменная, постоянно имеет значение из переменной, указанной в описании. Узел позволяет 
изменить значение переменной при подаче активного сигнала на вход со значением. Если указать после значения через символ
`$` ключевое слово типа данных, значение на выходе будет автоматически сконвертировано в соответствующий тип.

<img class="img-small" src="{{site.baseurl}}/resources/docs/nodes/mem/03_variable.png"/>

### Variable Get

**Variable Get** - узел-переменная, постоянно имеет значение из переменной, указанной в описании. Узел **не** позволяет 
изменить значение переменной. Если указать после значения через символ `$` ключевое слово типа данных, значение на 
выходе будет автоматически сконвертировано в соответствующий тип.

<img class="img-small" src="{{site.baseurl}}/resources/docs/nodes/mem/04_variable_get.png"/>

### Variable Set

**Variable Set** - узел-переменная, постоянно имеет значение из переменной, указанной в описании. Узел **не** позволяет 
получить значение переменной, но позволяет изменить его при подаче активного значения на вход.

<img class="img-small" src="{{site.baseurl}}/resources/docs/nodes/mem/05_variable_set.png"/>


[index]: {{site.baseurl}}/index
[tutorials]: {{site.baseurl}}/tutorials#content
[docs]: {{site.baseurl}}/docs#content
[drawio]: https://app.diagrams.net/?splash=0&libs=0&clibs=Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/base.drawio;Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/structure.drawio
[replit]: https://repl.it/github/octo-gone/sync-execution