---
layout: tutorials
title: Запуск
---

## Выполнение программы

Главной не то как построена программа, а то как она работает. Потому кроме рисования, их нужно и запускать. 
Для запуска программы достаточно использовать [Repl.it][replit]. В данном репле находится весь проект с [Github][github].
Остается лишь немного изменить программу под себя (изменения не влияют на проект в Github). Однако всегда
можно скачать проект и запустить его на своём устройстве

### Что требуется для запуска

Запустить любую Sync-программу можно на чистом [Python 3.8][python3]. Однако версии выше и ниже тоже поддерживают запуск.
Поддержка версий младше 3.5 проверена.

<img src="{{site.baseurl}}/resources/tutorials/execution/01_get_python.png"/>

### Что требуется для запуска в Repl.it

Для запуска в Repl.it достаточно нажать кнопку Run. Первый запуск за сессию может быть долгим, так как Repl.it требуется 
проверить модули используемые в скриптах (часто происходит загрузка svgwrite).

<img src="{{site.baseurl}}/resources/tutorials/execution/02_run_repl.png"/>

[github]: https://github.com/octo-gone/sync-execution
[python3]: https://www.python.org/

[index]: {{site.baseurl}}/index
[tutorials]: {{site.baseurl}}/tutorials#content
[drawio]: https://app.diagrams.net/?splash=0&libs=0&clibs=Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/base.drawio;Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/structure.drawio
[replit]: https://repl.it/@mr_zed/sync-execution#script.drawio