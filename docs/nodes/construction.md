---
layout: default_no_header
return_page: /docs
return_title: К документации
title: Construction
---
## Узлы конструкции и развязки

Для задания большей гибкости программы есть возможность использовать узлы-циклы, логические развязки, счетчики и т.п.
Большинство таких узлов имеют несколько выходов между которыми переключаются в зависимости от состояния. 

### If

**If** - узел представляющий логическое ветвление. При получении сигнала на управляющий вход узел проверяет значение с 
входа условия и активирует один из соответствующих выходов.  

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/construction/01_if.png"/>

[index]: {{site.baseurl}}/index
[tutorials]: {{site.baseurl}}/tutorials#content
[docs]: {{site.baseurl}}/docs#content
[drawio]: https://app.diagrams.net/?splash=0&libs=0&clibs=Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/base.drawio;Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/structure.drawio
[replit]: https://repl.it/github/octo-gone/sync-execution