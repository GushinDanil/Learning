/** 3.6. Объекты-обертки
Объекты в языке JavaScript являются составными значениями: они представля
ют собой коллекции свойств, или именованных значений. Обращение к свойст
вам мы будем выполнять с использованием точечной нотации. Свойства, значе
ниями которых являются функции, мы будем называть методами. Чтобы вы
звать метод m объекта o, следует использовать инструкцию o.m().
     Мы уже видели, что строки обладают свойствами и методами: */
var s = "hello world!";                              // Строка
var word = s.substring(s.indexOf(" ")+1, s.length);  // Использование свойств строки
/** Однако строки не являются объектами, так почему же они обладают свойствами?
Всякий раз когда в программе предпринимается попытка обратиться к свойству
строки s, интерпретатор JavaScript преобразует строковое значение в объект, как
если бы был выполнен вызов new String(s). Этот объект наследует (раздел 6.2.2)
строковые методы и используется интерпретатором для доступа к свойствам. По
сле обращения к свойству вновь созданный объект уничтожается. (От реализа
ций не требуется фактически создавать и уничтожать этот промежуточный объ
ект, но они должны вести себя так, как если бы объект действительно создавался
и уничтожался.)
Наличие методов у числовых и логических значений объясняется теми же при
чинами: при обращении к какому-либо методу создается временный объект вызо
вом конструктора Number() или Boolean(), после чего производится вызов метода
этого объекта. Значения null и undefined не имеют объектов-оберток: любые по
пытки обратиться к свойствам этих значений будет вызывать ошибку TypeError.
     Рассмотрим следующий фрагмент и подумаем, что происходит при его выполнении:  */
var s = "test"; // Начальное строковое значение.
s.len = 4;      // Установить его свойство.
var t = s.len;  // Теперь запросить значение свойства.
/**
В начале этого фрагмента переменная t имеет значение undefined. Вторая строка
создает временный объект String, устанавливает его свойство len равным 4 и за
тем уничтожает этот объект. Третья строка создает из оригинальной (неизменен
ной) строки новый объект String и пытается прочитать значение свойства len.
    Строки не имеют данного свойства, поэтому выражение возвращает значение
undefined. Данный фрагмент показывает, что при попытке прочитать значение
какого-либо свойства (или вызвать метод) строки числа и логические значения
ведут себя подобно объектам. Но если попытаться установить значение свойства,
    эта попытка будет просто проигнорирована: изменение затронет только времен
ный объект и не будет сохранено.
    Временные объекты, которые создаются при обращении к свойству строки, числа
или логического значения, называются объектами-обертками, и иногда может
потребоваться отличать строки от объектов String или числа и логические значе
ния от объектов Number и Boolean. Однако обычно объекты-обертки можно рассмат
ривать просто как особенность реализации и вообще не думать о них. Вам доста
точно будет знать, что строки, числа и логические значения отличаются от объек
тов тем, что их свойства доступны только для чтения и что вы не можете опреде
лять для них новые свойства.
    Обратите внимание, что существует возможность (но в этом почти никогда нет не
обходимости или смысла) явно создавать объекты-обертки вызовом конструктора

Строка, число и логическое значение.
При необходимости интерпретатор JavaScript обычно автоматически преобразу
ет объекты-обертки, т. е. объекты S, N и B в примере выше, в обертываемые ими
простые значения, но они не всегда ведут себя точно так же, как значения s, n и b.
Оператор равенства == считает равными значения и соответствующие им объекты-обертки, но оператор идентичности === отличает их. Оператор typeof также
обнаруживает отличия между простыми значениями и их объектами-обертками.*/
console.log(undefined==false)
var i
var i
i
console.log(i)