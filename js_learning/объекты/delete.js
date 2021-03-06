/*
Выражение delete возвращает значение true в случае успешного удаления свойст
ва или когда операция удаления не привела к изменению объекта (например, при
попытке удалить несуществующее свойство). Выражение delete также возвраща
ет true, когда этому оператору передается выражение, не являющееся выражени
ем обращения к свойству:

o = {x:1};         //o имеет собственное свойство x и наследует toString

delete o.x;        //Удалит x и вернет true

delete o.x;        //Ничего не сделает (x не существует) и вернет true

delete o.toString; //Ничего не сделает (toString не собственное свойство) и вернет true

delete 1;          //Бессмысленно, но вернет true




Оператор delete не удаляет ненастраиваемые свойства, атрибут configurable кото
рых имеет значение false. (Однако он может удалять настраиваемые свойства не
расширяемых объектов.) Ненастраиваемыми являются свойства встроенных объ
ектов, а также свойства глобального объекта, созданные с помощью инструкций
объявления переменных и функций. Попытка удалить ненастраиваемое свойство
в строгом режиме вызывает исключение TypeError. В нестрогом режиме (и в реа
лизациях ECMAScript 3) в таких случаях оператор delete просто возвращает
false:

При удалении настраиваемых свойств глобального объекта в нестрогом режиме
допускается опускать ссылку на глобальный объект и передавать оператору
delete только имя свойства:
this.x = 1;    // Создать настраиваемое глобальное свойство (без var)
delete x;      // И удалить его
Однако в строгом режиме оператор delete возбуждает исключение SyntaxError, ес
ли его операндом является неквалифицированный идентификатор, такой как x,
поэтому необходимо указывать явное выражение обращения к свойству:
delete x;      // В строгом режиме возбудит исключение SyntaxError
delete this.x; // Такой способ работает
 */

