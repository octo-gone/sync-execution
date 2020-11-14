---
layout: tutorials
title: Запуск
---

## Выполнение программы

Главной не то как построена программа, а то как она работает. Потому кроме рисования, их нужно и запускать. 
Для запуска программы достаточно использовать [Repl.it][replit]. В данном репле находится весь проект с [Github][github].
Остается лишь немного изменить программу под себя (изменения не влияют на проект в Github и на программы других пользователей,
так как создаются только на вашем аккаунте). Однако всегда можно скачать проект и запустить его на своём устройстве.

### Что требуется для запуска

Запустить любую Sync-программу можно на чистом [Python 3.8][python3]. Однако версии выше и ниже тоже поддерживают запуск.
Поддержка версий младше 3.5 проверена.

<img src="{{site.baseurl}}/resources/tutorials/execution/01_get_python.png"/>

### Что требуется для запуска в Repl.it

Для запуска в Repl.it достаточно нажать кнопку Run. Первый запуск за сессию может быть долгим, так как Repl.it требуется 
проверить модули используемые в скриптах (часто происходит загрузка svgwrite).

<img src="{{site.baseurl}}/resources/tutorials/execution/02_run_repl.png"/>

### Инструкция запуска

Для создания программы используется [Draw.io][drawio] (все библиотеки уже установлены)

Для запуска в Repl.it или на устройстве достаточно выполнить следующий алгоритм:
1. Внутри Drawio.io в меню нужно выбрать "File" > "Export as" > "XML". 

    <img src="{{site.baseurl}}/resources/tutorials/execution/03_taking_xml_1.png"/>
2. Выбрать без флагов или с "Compressed". Если было создано несколько страниц (например, для отделения функций), 
то по необходимости выбрать флаг "All Pages"

    <img src="{{site.baseurl}}/resources/tutorials/execution/04_taking_xml_2.png"/>
3. Далее требуется получить необработанный XML. Можно нажать "Open in New Window" или сохранить файл в папку проекта (при работе на устройстве).

    <img src="{{site.baseurl}}/resources/tutorials/execution/05_taking_xml_3.png"/>
    - **Для первого варианта**: Скопировать все содержимое (`ctrl-a` (выделить все) затем `ctrl-c` (копировать)).
    
    <img src="{{site.baseurl}}/resources/tutorials/execution/06_taking_xml_4.png"/>
    - **Для второго**: Сохранить файл достаточно в корневую папку и назвать **script.drawio** для большего удобства. 
    Иначе потребуется изменять код программы (подавая правильный путь к файлу).
    
    <img src="{{site.baseurl}}/resources/tutorials/execution/07_taking_xml_5.png"/>
4. Для работы в Repl.it требуется перейти в репл sync-execution (для работы нужно быть зарегистрированным пользователем)
    - Если это первый запуск, то требуется создать репл или же перейти по [ссылке][replit_script]. Возможно то, что Repl.it
    будет долго грузить, решается перезагрузкой страницы.
    - **Если не первый, то требуется открыть уже созданный репл** (`https://repl.it/@<Никнейм>/sync-execution`). 
    Постоянно создавать новые реплы (с помощью ссылки) не стоит. 
    
    <img src="{{site.baseurl}}/resources/tutorials/execution/10_working_with_repl.png"/>
5. Дальше требуется изменить файлы для работы 
    - Сохранить данные из буфера обмена (скопированные данные) в файл **script.drawio** c заменой 
    (`ctrl-a` (выделить все) затем `ctrl-v` (вставить)). В Repl.it - если данный файл не был открыт, то требуется выбрать 
    его в боковом меню файлов.
    
    <img src="{{site.baseurl}}/resources/tutorials/execution/11_changing_project_1.png"/>
    - Если файл не находится в корневой папке и не назван **script.drawio**, то нужно перейти в файл main.py и заменить путь к файлу
    ```python
    from scripts import parser, run
    file = "<путь к файлу>"
    run.run(*parser.parse(file))
    input("Press ENTER to exit...")
    ```
    
    <img src="{{site.baseurl}}/resources/tutorials/execution/12_changing_project_2.png"/>

Финальным действием является запуск. В Repl.it достаточно нажать Run (или написать в консоли `python main.py`). 
А на устройстве потребуется запустить скрипт **main.py**.

<img src="{{site.baseurl}}/resources/tutorials/execution/13_running.png"/>

Для работы с последними обновлениями требуется зайти в репл и обновить данные из Git. Это можно сделать нажатием кнопки "Pull".

<img src="{{site.baseurl}}/resources/tutorials/execution/14_updating.png"/>

Возможно возникновение конфликтов: ваши созданные или измененные файлы не сопоставимы с файлами из Git.
Тогда требуется сохранить важные измененные данные и загрузить данные с GitHub.

<img src="{{site.baseurl}}/resources/tutorials/execution/15_conflict_solving.png"/>

[github]: https://github.com/octo-gone/sync-execution
[python3]: https://www.python.org/
[replit_script]: https://repl.it/github/octo-gone/sync-execution#script.drawio

[index]: {{site.baseurl}}/index
[tutorials]: {{site.baseurl}}/tutorials#content
[drawio]: https://app.diagrams.net/?splash=0&libs=0&clibs=Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/base.drawio;Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/structure.drawio
[replit]: https://repl.it/github/octo-gone/sync-execution
