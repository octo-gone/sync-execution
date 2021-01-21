---
layout: default_no_header
title: I/O
return_page: /docs/nodes
return_title: К узлам
---
## Узлы для ввода и вывода данных

Большинство программ взаимодействуют с внешней средой через вывод или ввод данных с консоли. Для этого в Sync 
были созданы следующие узлы.

### Input

**Input** - узел для ввода данных в программу. После получение сигнала узел заблокирует выполнение программы, пока не получит значение.
Если изменить описание узла, то можно персонализировать вывод подсказки (приглашение консоли). Узел автоматически добавит пробел в конце
приглашения. Если использовать конструкцию `{<var name>$<type>}`, то можно отобразить значение переменной внутри подсказки. Например,
если записать `Введите число от {min} до {max$real} >>>`, то узел попытается найти две указанные переменные, а вторую переменную дополнительно
переведет в тип **real**. Если подсказка не была изменена, то она будет `>>>`.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/inout/01_input.png"/>

### Print

**Print** - узел вывода данных в программу. После получение сигнала узел забирает данные из входа, если их там нет, 
то пытается взять данные из описания. В описании узел понимает использование констант, а также при использовании конструкции
`<var name>$var` узел попытается взять значение из переменной. После завершения узел вернет сигнал.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/inout/02_print_with_ctrl.png"/>

Существует аналогичный узел, но без выходного сигнала.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/inout/03_print.png"/>

[index]: {{site.baseurl}}/index
[tutorials]: {{site.baseurl}}/tutorials#content
[docs]: {{site.baseurl}}/docs#content
[drawio]: https://app.diagrams.net/?splash=0&libs=0&clibs=Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/base.drawio;Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/structure.drawio
[replit]: https://repl.it/github/octo-gone/sync-execution