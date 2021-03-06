"""В версии Python 2.6 и 3.0 появилась новая инструкция, имеющая отношение
к исключениям – with, с необязательным предложением as. Эта инструкция
предназначена для работы с объектами контекстных менеджеров, которые
поддерживают новый протокол взаимодействия, основанный на использова-
нии методов. Данная особенность доступна также в Python 2.5 в виде необяза-
тельного расширения, которое можно активировать инструкцией:
from __future__ import with_statement
В двух словах, инструкция with/as может использоваться как альтернатива
известной идиомы try/finally; подобно этой инструкции она предназначена
для выполнения заключительных операций независимо от того, возникло ли
исключение на этапе выполнения основного действия. Однако, в отличие от
инструкции try/finally, инструкция with поддерживает более богатый возмож-
ностями протокол, позволяющий определять как предварительные, так и за-
ключительные действия для заданного блока программного кода.
Язык ������������������������������������������������������������������Python������������������������������������������������������������ дополняет некоторые встроенные средства контекстными менед-
жерами, например файлы, которые закрываются автоматически, или блоки-
ровки потоков выполнения, которые автоматически запираются и отпирают-
ся. Однако программист также может создавать с классами и свои контекст-
ные менеджеры.

Основная форма инструкции with выглядит, как показано ниже:
with выражение [as переменная]:
блок with
Здесь предполагается, что выражение возвращает объект, поддерживающий
протокол контекстного менеджера (вскоре я расскажу об этом протоколе под-
робнее). Этот объект может возвращать значение, которое будет присвоено
переменной, если присутствует необязательное предложение as.
Обратите внимание, что переменной необязательно будет присвоен результат
выражения – результатом выражения является объект, который поддерживает кон-
текстный протокол, а переменной может быть присвоено некоторое другое значе-
ние, предназначенное для использования внутри инструкции. Объект, возвра-
щаемый выражением, может затем выполнять предварительные действия перед
тем, как будет запущен блок with, а также завершающие действия после того,
как этот блок будет выполнен, независимо от того, было ли возбуждено исклю-
чение при его выполнении.
Некоторые встроенные объекты языка Python были дополнены поддержкой
протокола управления контекстом и потому могут использоваться в инструк-
ции with. Например, объекты файлов снабжены менеджером контекста, кото-
рый автоматически закрывает файл после выполнения блока with независимо
от того, было ли возбуждено исключение при его выполнении:"""

with open('data.txt', 'r') as myfile:
    for row in myfile:
        print(row)

"""Здесь вызываемая функция open возвращает объект файла, который присваива-
ется имени myfile. Применительно к переменной myfile мы можем использовать
обычные средства, предназначенные для работы с файлами, – в данном случае
с помощью итератора выполняется чтение строки за строкой в цикле for.
Однако данный объект поддерживает протокол управления контекстом, ис-
пользуемый инструкцией with. После того как инструкция with начнет выпол-
нение, механизм управления контекстом гарантирует, что объект файла, на
который ссылается переменная myfile, будет закрыт автоматически, даже если
в цикле for во время обработки файла произойдет исключение.
Объекты файлов закрываются автоматически в момент их утилизации сбор-
щиком мусора, однако нет никакой возможности узнать заранее, когда это
произойдет. Инструкция with, используемая в таком качестве, представляет
альтернативное решение, позволяющее гарантировать, что файл будет закрыт
сразу после выполнения определенного блока программного кода. Как мы уже
видели выше, аналогичного эффекта можно добиться с помощью более универ-
сальной и более явной инструкции try/finally, но в данном случае для этого
потребуется написать четыре строки программного кода вместо одного:"""
print('-'*50)
try:
    myfile = open('data.txt', 'r')
    for i in myfile:
        print(i)
finally:
    myfile.close()

print('-'*50)
with open('data.txt','r') as data,open('data2.txt') as data2:
    for i in data:
        print(i)
    print()
    for i in data2:
        print(i)


