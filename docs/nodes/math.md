---
layout: default_no_header
title: Math
return_page: /docs/nodes
return_title: К узлам
---
## Узлы для математических операций

Большая часть программ используется для обработки математических данных, поэтому требуется знать возможный функционал.

### Add

**Add** - узел-сумматор, складывает все значения с множественного входа. Выполнение
происходит только когда значения со всех входных узлов были получены. 

<img class="img-small" src="{{site.baseurl}}/resources/docs/nodes/math/01_add_number.png"/>

### Sub

**Sub** - узел вычитания, уменьшает значение из первого входа на значение второго. 

<img class="img-small" src="{{site.baseurl}}/resources/docs/nodes/math/02_sub_number.png"/>

### Division

**Division** - узел деления, делит делимое на делитель. 

<img class="img-small" src="{{site.baseurl}}/resources/docs/nodes/math/03_div_number.png"/>

### Multiplication

**Mult** - узел умножения, умножает друг на друга все значения с множественного входа.
Выполнение происходит только когда значения со всех входных узлов были получены.

<img class="img-small" src="{{site.baseurl}}/resources/docs/nodes/math/04_mult_number.png"/>

### Increment

**Inc** - узел, который увеличивает входное значение на один.

<img class="img-small" src="{{site.baseurl}}/resources/docs/nodes/math/05_increment.png"/>

### Decrement

**Dec** - узел, который уменьшает входное значение на один.

<img class="img-small" src="{{site.baseurl}}/resources/docs/nodes/math/06_decrement.png"/>

### Abs

**Abs** - узел-модуль, возвращает число без знака.

<img class="img-small" src="{{site.baseurl}}/resources/docs/nodes/math/07_abs.png"/>

### Inversion

**Inv** - узел-инвертор, изменяет знак числа на противоположный.

<img class="img-small" src="{{site.baseurl}}/resources/docs/nodes/math/08_inversion.png"/>

### Round

**Round** - узел округления, округляет число до указанной точности. Точность - количество символов после запятой. 
При подаче отрицательного числа или нуля округление происходит в разрядах целых.

<img class="img-small" src="{{site.baseurl}}/resources/docs/nodes/math/09_round.png"/>

### Div

**Div** - узел целочисленного деления, возвращает целую часть от деления чисел.

<img class="img-small" src="{{site.baseurl}}/resources/docs/nodes/math/10_div.png"/>

### Mod

**Mod** - узел остатка от деления, возвращает остаток от деления чисел.

<img class="img-small" src="{{site.baseurl}}/resources/docs/nodes/math/11_mod.png"/>

[index]: {{site.baseurl}}/index
[tutorials]: {{site.baseurl}}/tutorials#content
[docs]: {{site.baseurl}}/docs#content
[drawio]: https://app.diagrams.net/?splash=0&libs=0&clibs=Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/base.drawio;Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/structure.drawio
[replit]: https://repl.it/github/octo-gone/sync-execution