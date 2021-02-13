---
layout: default_no_header
title: Control
return_page: /docs/nodes
return_title: К узлам
---
## Узлы работающие с сигналом

Кроме узлов, которые обрабатывают данные, существуют узлы позволяющие взаимодействовать с сигналом.

### Run

**Run** - узел, являющийся начальным для любой программы, он позволяет запустить работу всей программы. 
До запуска обработки данный узел уже является активным. 

<img class="img-small" src="{{site.baseurl}}/resources/docs/nodes/control/01_run.png"/>

### Stop

**Stop** - узел, являющийся финальным для программы, он позволяет прекратить работу программы по получению сигнала. 

<img class="img-small" src="{{site.baseurl}}/resources/docs/nodes/control/02_stop.png"/>

### Wait

**Wait** - узел ожидания сигнала. До тех пор, пока со всех подключенных входов не будет получен сигнал, узел не отдаст 
выходной сигнал, что позволяет подождать выполнения всех параллельных цепочек. Ожидание всех входов можно сменить
на ожидание хотя бы одного - написав в описании `$any`, по умолчанию стоит значение `$all`. 

<img class="img-small" src="{{site.baseurl}}/resources/docs/nodes/control/03_wait.png"/>

### Merge Control

**Merge Control** - узел, объединяющий сигнал и значение с разных узлов. Узел возвращает значение с сигналом только в том
случае, если подан сигнал на управляющий вход, иначе сигнала не будет. Информация с управляющего сигнала не забирается. 

<img class="img-small" src="{{site.baseurl}}/resources/docs/nodes/control/04_merge_ctrl.png"/>

### To Control

**To Control** - узел возвращает сигнал без значения. 

<img class="img-small" src="{{site.baseurl}}/resources/docs/nodes/control/05_to_ctrl.png"/>

### Delay

**Delay** - узел для задержки входящего сигнала на целое количество тактов программы. При подаче нуля отправляет сигнал на 
следующую итерацию. 

<img class="img-small" src="{{site.baseurl}}/resources/docs/nodes/control/06_delay.png"/>

### Timer

**Timer** - узел, который позволяет замерить количество пройденных тактов между запускающим и останавливающим сигналами.

<img class="img-small" src="{{site.baseurl}}/resources/docs/nodes/control/07_timer.png"/>

### Warning Message

**Warning Message** - узел, возвращающий ошибку в консоль программы при получении сигнала. Можно настроить название ошибки
изменив описание узла.

<img class="img-small" src="{{site.baseurl}}/resources/docs/nodes/control/08_warning_message.png"/>

### Error Message

**Error Message** - узел, возвращающий ошибку в консоль программы при получении сигнала. Можно настроить название ошибки
изменив описание узла. Узел завершает программу.

<img class="img-small" src="{{site.baseurl}}/resources/docs/nodes/control/09_error_message.png"/>

[index]: {{site.baseurl}}/index
[tutorials]: {{site.baseurl}}/tutorials#content
[docs]: {{site.baseurl}}/docs#content
[drawio]: https://app.diagrams.net/?splash=0&libs=0&clibs=Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/base.drawio;Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/structure.drawio
[replit]: https://repl.it/github/octo-gone/sync-execution