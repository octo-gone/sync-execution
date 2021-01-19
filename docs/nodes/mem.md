---
layout: default_no_header
return_page: /docs/nodes
return_title: К узлам
title: Memory
---
## Узлы для работы с памятью

Как известно, что большинство алгоритмов не могут обходиться без использования памяти.  

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


[index]: {{site.baseurl}}/index
[tutorials]: {{site.baseurl}}/tutorials#content
[docs]: {{site.baseurl}}/docs#content
[drawio]: https://app.diagrams.net/?splash=0&libs=0&clibs=Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/base.drawio;Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/structure.drawio
[replit]: https://repl.it/github/octo-gone/sync-execution