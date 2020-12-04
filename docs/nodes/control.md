---
layout: default_no_header
title: Control
return_page: /docs/nodes
return_title: К узлам
---
## Узлы работающие с сигналом

Кроме узлов, которые обрабатывают данные, существуют узлы позволяющие взаимодействовать с сигналом.

### Run

Run - узел являющийся начальным для любой программы, он позволяет запустить работу всей программы. 
До запуска обработки данный узел уже является активным. 

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/control/01_run.png"/>

### Stop

Stop - узел являющийся финальным для программы, он позволяет прекратить работу программы по получению сигнала. 

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/control/02_stop.png"/>

### Wait

Wait - узел ожидания сигнала. До тех пор пока со всех подключенных вх/одов не будет получен сигнал, узел не отдаст 
выходной сигнал, что позволяет подождать выполнения всех параллельных цепочек. Ожидание всех входов можно сменить
на ожидание хотя бы одного - написав в описании `$any`, по умолчанию стоит значение `$all`. 

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/control/03_wait.png"/>

[index]: {{site.baseurl}}/index
[tutorials]: {{site.baseurl}}/tutorials#content
[docs]: {{site.baseurl}}/docs#content
[drawio]: https://app.diagrams.net/?splash=0&libs=0&clibs=Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/base.drawio;Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/structure.drawio
[replit]: https://repl.it/github/octo-gone/sync-execution