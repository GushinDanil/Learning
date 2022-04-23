"""Инструкция raise
Чтобы явно возбудить исключение, можно использовать инструкцию raise.
В общем виде она имеет очень простую форму записи – инструкция raise со-
стоит из слова raise, за которым может следовать имя класса или экземпляр
возбуждаемого исключения:
raise <instance> # Возбуждает экземпляр класса-исключения
raise <class> # Создает и возбуждает экземпляр класса-исключения
raise # Повторно возбуждает самое последнее исключение
Как уже упоминалось ранее, исключение в Python 2.6 и 3.0 – это всегда эк-
земпляр класса. Следовательно, первая форма инструкции raise является наи-
более типичной – ей непосредственно передается экземпляр класса, который
создается перед вызовом инструкции raise или внутри нее. Если инструкции
передается класс, интерпретатор вызовет конструктор класса без аргументов,
а полученный экземпляр передаст инструкции raise – если после имени класса
добавить круглые скобки, мы получим эквивалентную форму. Третья форма
инструкции raise просто повторно возбуждает текущее исключение – это удоб-
но, когда возникает необходимость передать перехваченное исключение друго-
му обработчику.
Чтобы лучше понять вышесказанное, рассмотрим несколько примеров. Сле-
дующие две формы возбуждения встроенных исключений эквивалентны – они
обе возбуждают экземпляр по имени класса, но первая из них создает экзем-
пляр неявно:
raise IndexError # Класс (экземпляр создается неявно)
raise IndexError() # Экземпляр (создается в инструкции)
Мы также можем создать экземпляр заранее – инструкция raise принимает
ссылки на объекты любых типов, поэтому следующие два примера точно так
же возбуждают исключение IndexError, как и предыдущие:
exc = IndexError() # Экземпляр создается заранее
raise exc

excs = [IndexError, TypeError]
raise excs[0]

При возбуждении исключения интерпретатор отправляет возбужденный эк-
земпляр вместе с исключением. Если инструкция try включает предложение
вида except name as X:, переменной X будет присвоен экземпляр, переданный ин-
струкцией raise:
try:
...
except IndexError as X: # Переменной X будет присвоен экземпляр исключения
..."""
