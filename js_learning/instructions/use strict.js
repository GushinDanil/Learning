'use strict'
/*
"use strict" – это директива, введенная стандартом ECMAScript 5. Директивы не
являются инструкциями (но достаточно близки, чтобы включить описание "use
strict" в эту главу). Между обычными инструкциями и директивой "use strict"
существует два важных отличия:
• Она не включает никаких зарезервированных слов языка: директива – это
лишь выражение, содержащее специальный строковый литерал (в одиночных
или двойных кавычках). Интерпретаторы JavaScript, не соответствующие
стандарту ECMAScript 5, будут интерпретировать ее как простое выражение
без побочных эффектов и ничего не будут делать. В будущих версиях стандар
та ECMAScript, как ожидается, слово use будет переведено в разряд ключевых
слов, что позволит опустить кавычки.
• Она может появляться только в начале сценария или в начале тела функции,
перед любыми другими инструкциями. Однако она не обязательно должна на
ходиться в самой первой строке сценария или функции: директиве "use strict"
могут предшествовать или следовать за ней другие строковые выражения-ли
тералы, а различные реализации JavaScript могут интерпретировать эти стро
ковые литералы как директивы, определяемые этими реализациями. Строко
вые литералы, следующие за первой обычной инструкцией в сценарии или
функции, интерпретируются как обычные выражения – они могут не воспри
ниматься как директивы и не оказывать никакого эффекта.
Назначение директивы "use strict" состоит в том, чтобы показать, что следую
щий за ней программный код (в сценарии или функции) является строгим ко
дом. Строгим считается программный код верхнего уровня (не внутри функций),
если в сценарии имеется директива "use strict". Строгим считается тело функ
ции, если она определяется внутри строгого программного кода или если она со
держит директиву "use strict". Строгим считается программный код, передавае
мый методу eval(), если вызов eval() выполняется из строгого программного кода
или если строка с кодом содержит директиву "use strict".
Строгий программный код выполняется в строгом режиме. Согласно стандарту
ECMAScript 5, строгий режим определяет ограниченное подмножество языка,
благодаря чему исправляет некоторые недостатки языка, а также обеспечивает
более строгую проверку на наличие ошибок и повышенный уровень безопасно
сти. Ниже перечислены различия между строгим и нестрогим режимами (первые
три имеют особенно большое значение):

• В строгом режиме не допускается использование инструкции with.

• В строгом режиме все переменные должны объявляться: если попытаться при
    своить значение идентификатору, который не является объявленной перемен
    ной, функцией, параметром функции, параметром конструкции catch или
    свойством глобального объекта, возбуждается исключение ReferenceError. (В не
    строгом режиме такая попытка просто создаст новую глобальную переменную
    и добавит ее в виде свойства в глобальный объект.)

• В строгом режиме функции, которые вызываются как функции (а не как методы),
    получают в ссылке this значение undefined. (В нестрогом режиме функ
    ции, которые вызываются как функции, всегда получают в ссылке this гло
    бальный объект.) Это отличие можно использовать, чтобы определить, под
    держивает ли та или иная реализация строгий режим:
    var hasStrictMode = (function() { "use strict"; return this===undefined}());

    Кроме того, когда функция вызывается в строгом режиме с помощью call()
    или apply(), значение ссылки this в точности соответствует значению, передан
    ному в первом аргументе функции call() или apply(). (В нестрогом режиме зна
    чения null и undefined замещаются ссылкой на глобальный объект, а простые
    значения преобразуются в объекты.)
• В строгом режиме попытки присвоить значения свойствам, недоступным для
    записи, или создать новые свойства в нерасширяемых объектах порождают ис
    ключение TypeError. (В нестрогом режиме эти попытки просто игнорируются.)
• В строгом режиме программный код, передаваемый функции eval(), не может
    объявлять переменные или функции в области видимости вызывающего про
    граммного кода, как это возможно в нестрогом режиме. Вместо этого перемен
    ные и функции помещаются в новую область видимости, создаваемую для
    функции eval(). Эта область видимости исчезает, как только eval() вернет
    управление.
• В строгом режиме объект arguments (раздел 8.3.2) в функции хранит статиче
    скую копию значений, переданных функции. В нестрогом режиме объект
    arguments ведет себя иначе – элементы массива arguments и именованные пара
    метры функции ссылаются на одни и те же значения.
• В строгом режиме возбуждается исключение SyntaxError, если оператору delete
    передать неквалифицированный идентификатор, такой как имя переменной,
    функции или параметра функции. (В нестрогом режиме такое выражение
    delete не выполнит никаких действий и вернет false.)
• В строгом режиме попытка удалить ненастраиваемое свойство приведет к ис
    ключению TypeError. (В нестрогом режиме эта попытка просто завершится не
    удачей и выражение delete вернет false.)
• В строгом режиме попытка определить в литерале объекта два или более
    свойств с одинаковыми именами считается синтаксической ошибкой. (В не
    строгом режиме ошибка не возникает.)
• В строгом режиме определение двух или более параметров с одинаковыми
    именами в объявлении функции считается синтаксической ошибкой. (В не
    строгом режиме ошибка не возникает.)
• В строгом режиме не допускается использовать литералы восьмеричных це
    лых чисел (начинающихся с 0, за которым не следует символ x). (В нестрогом
    режиме некоторые реализации позволяют использовать восьмеричные лите
    ралы.)
• В строгом режиме идентификаторы eval и arguments интерпретируются как
    ключевые слова, и вы не можете изменить их значения. Вы сможете присво
    ить значения этим идентификаторам, объявив их как переменные, использо
    вав их в качестве имен функций, имен параметров функций или идентифика
    торов блока catch.
• В строгом режиме ограничивается возможность просмотра стека вызовов. По
    пытки обратиться к свойствам arguments.caller и arguments.callee в строгом ре
    жиме возбуждают исключение TypeError. Попытки прочитать свойства caller
    и arguments функций в строгом режиме также возбуждают исключение Type
    Error. (Некоторые реализации определяют эти свойства в нестрогих функциях.)
 */

var obj = {
    '':12,
}
