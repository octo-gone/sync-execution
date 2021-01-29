---
layout: default_no_header
title: Logic
return_page: /docs/nodes
return_title: К узлам
---
## Узлы для логических операций

Благодаря логическим функциям мы можем сделать программу более гибкой и выполнять определенные действия в зависимости от обстоятельств.

### Bool

**Bool** - ~~булочка~~ узел-конвертор, конвертирующий любое входное значение в логический эквивалент по правилу отсутствия:
при пустой строке, нуле или None будет возвращен False, при большинстве остальных случаев будет True. 

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/logic/00_bool.png"/>

### Not

**Not** - узел-инвертор, конвертирующий любое входное значение в логический эквивалент и инвертирующий его значение. Если было значение True, 
выходное значение будет False, аналогично False - True.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/logic/01_not.png"/>

### And

**And** - логический узел И, который возвращает логическое умножение между всеми входами (значения автоматически приводятся в bool). 

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/logic/02_and.png"/>

### Or

**Or** - логический узел ИЛИ, который возвращает логическое сложение между всеми входами (значения автоматически приводятся в bool). 

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/logic/03_or.png"/>

### Not And

**Not And** - логический узел И-НЕ, который возвращает инверсию логического умножения между всеми входами (значения автоматически приводятся в bool). 

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/logic/04_not_and.png"/>

### Not Or

**Not Or** - логический узел ИЛИ-НЕ, который возвращает инверсию логического сложения между всеми входами (значения автоматически приводятся в bool). 

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/logic/05_not_or.png"/>

### Xor

**Xor** - логический узел Исключающее-ИЛИ, который возвращает сложение по модулю 2 или же инвертированное 
сравнение на равенство между входами (значения автоматически приводятся в bool). 

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/logic/06_xor.png"/>

### Equal

**Equal** - логический узел Равно, который возвращает сравнение на равенство между всеми входами (значения автоматически приводятся в bool). 

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/logic/07_equal.png"/>

### Greater

**Greater** - логический узел Больше, который возвращает сравнение на больше между верхним и нижним входом (значения автоматически приводятся в bool). 

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/logic/08_greater.png"/>

### Less

**Less** - логический узел Меньше, который возвращает сравнение на меньше между верхним и нижним входом (значения автоматически приводятся в bool). 

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/logic/09_less.png"/>

### Greater or Equal

**Greater or Equal** - логический узел Больше-или-Равно, который возвращает сравнение на больше или равно между верхним и нижним входом (значения автоматически приводятся в bool). 

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/logic/10_greater_or_equal.png"/>

### Less or Equal

**Less or Equal** - логический узел Меньше-или-Равно, который возвращает сравнение на меньше или равно между верхним и нижним входом (значения автоматически приводятся в bool). 

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/logic/11_less_or_equal.png"/>

### Not Equal

**Not Equal** - логический узел Не-Равно, который возвращает сравнение на неравенство входов между друг другом (значения автоматически приводятся в bool). 

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/logic/12_not_equal.png"/>

### Contains

**Contains** - узел, который возвращает наличие указанного значения в множестве. Множество ключей словаря можно передать, написав в описании к узлу имя словаря.
Множество значений списка или массива можно передать, написав в описании имя списка или массива.

<img class="img-node" src="{{site.baseurl}}/resources/docs/nodes/logic/13_contains.png"/>


[index]: {{site.baseurl}}/index
[tutorials]: {{site.baseurl}}/tutorials#content
[docs]: {{site.baseurl}}/docs#content
[drawio]: https://app.diagrams.net/?splash=0&libs=0&clibs=Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/base.drawio;Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/structure.drawio
[replit]: https://repl.it/github/octo-gone/sync-execution