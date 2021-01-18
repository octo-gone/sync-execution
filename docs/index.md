---
layout: default_no_header
title: Документация
---
## Информация о языке

Язык дает возможность представлять не только линейные алгоритмы, но и визуализировать сложные асинхронные моменты.
А благодаря тому, что это графический язык, анализ программ упрощается. Конечно, это возможно, только если программа
создана с учетом стиля и выстроена визуально в правильном порядке - про это можно прочитать в статье про [стилизацию
программ][style_tutorial]. Но, как и многие языки программирования, Sync имеет свои минусы, главный из которых - сложность
учета механики работы программ в Sync. Для большего понимания были созданы следующие статьи:

- [Соединение узлов и работа программы][program_construction]
    - [Виды коннекторов и виды подключения][pc_connectors]
    - [Порядок запуска узлов][pc_running]
    - [Обратный запрос][pc_callback]

### Узлы

Главной составляющей программы являются узлы, многие имеет свою особенность при запуске, обработке или выводе
данных или сигнала. В статьях ниже можно прочитать про это. Больше про узлы можно узнать [здесь][nodes].

#### Узлы делятся на следующе типы:

- [Control][n_control]
- [Math][n_mathematic]
- [Logic][n_logic]
- [Input and Output][n_inout]
- [Memory][n_mem]
- [Construction][n_construction]
- misc
- struct
- user_nodes
- functions

[style_tutorial]: {{site.baseurl}}/tutorials/style#content

[program_construction]: {{site.baseurl}}/docs/program-construction#content
[pc_connectors]: {{site.baseurl}}/docs/program-construction#connectors
[pc_running]: {{site.baseurl}}/docs/program-construction#running
[pc_callback]: {{site.baseurl}}/docs/program-construction#callback

[nodes]: {{site.baseurl}}/docs/nodes#content
[n_control]: {{site.baseurl}}/docs/nodes/control#content
[n_mathematic]: {{site.baseurl}}/docs/nodes/math#content
[n_logic]: {{site.baseurl}}/docs/nodes/logic#content
[n_inout]: {{site.baseurl}}/docs/nodes/inout#content
[n_mem]: {{site.baseurl}}/docs/nodes/mem#content
[n_construction]: {{site.baseurl}}/docs/nodes/construction#content

[index]: {{site.baseurl}}/index
[tutorials]: {{site.baseurl}}/tutorials#content
[docs]: {{site.baseurl}}/docs#content
[drawio]: https://app.diagrams.net/?splash=0&libs=0&clibs=Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/base.drawio;Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/structure.drawio
[replit]: https://repl.it/github/octo-gone/sync-execution