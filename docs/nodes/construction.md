---
layout: default_no_header
return_page: /docs/nodes
return_title: К узлам
title: Construction
---
## Узлы конструкции и развязки

Для задания большей гибкости программы есть возможность использовать узлы-циклы, логические развязки, счетчики и т.п.
Большинство таких узлов имеют несколько выходов, между которыми переключаются в зависимости от состояния. 

### If

**If** - узел, представляющий логическое ветвление. При получении сигнала на управляющий вход узел проверяет значение с 
входа условия и активирует один из соответствующих выходов.  

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/construction/01_if.png"/>

### Counter

**Counter** - узел-счетчик. При получении сигнала на управляющий вход узел проверяет значение с 
входа границы и устанавливает значение текущей итерации в 0. Далее при получении сигнала на вход переключения итерации узел
увеличивает значение итерации, также значение итерации отправляется на выход. Если значение итерации больше или равно
границе, сигнал отправляется на завершающий выход.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/construction/02_counter.png"/>

### For

**For** - узел-итератор. При получении сигнала на управляющий вход узел проверяет значение с 
входа границы и устанавливает значение текущей итерации в 0. Далее при получении сигнала на вход инкремента итерации узел
увеличивает значение итерации на указанное число, также значение итерации отправляется на выход. Если значение итерации 
больше или равно границе, сигнал отправляется на завершающий выход. 

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/construction/03_for.png"/>

### While

**While** - узел-цикл. При получении сигнала на управляющий вход узел проверяет значение с 
входа условия, если условие равно логической единице, то узел отправляет сигнал на выход цикла. Далее при получении 
сигнала с логической единицей узел отправляет сигнал на выход цикла, а в ином случае отправляет на завершающий выход. 

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/construction/04_while.png"/>

### Foreach

**Foreach** - узел перебора массива. Специализированный узел, который отправляет при каждой запросе нового элемента значение
или из значений со входа или из структурной переменной указанной в описании узла. После окончания перебора узел отправляет сигнал
на завершающий выход. Если указать в описании `any`, то узел начнет перебор после получения первого значения игнорируя
активирующий сигнал.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/construction/05_foreach.png"/>

### For Extended

**For Extended** - расширенный узел-итератор. Данный узел отличается от простого узла-итератора тем, что позволяет задать 
начальное значение итерации. 

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/construction/06_for_extended.png"/>

[index]: {{site.baseurl}}/index
[tutorials]: {{site.baseurl}}/tutorials#content
[docs]: {{site.baseurl}}/docs#content
[drawio]: https://app.diagrams.net/?splash=0&libs=0&clibs=Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/base.drawio;Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/structure.drawio
[replit]: https://repl.it/github/octo-gone/sync-execution