"""Метод __getattr__ выполняет операцию получения ссылки на атрибут. Если го-
ворить более определенно, он вызывается с именем атрибута в виде строки вся-
кий раз, когда обнаруживается попытка получить ссылку на неопределенный
(несуществующий) атрибут. Этот метод не вызывается, если интерпретатор
может обнаружить атрибут посредством выполнения процедуры поиска в дере-
ве наследования. Вследствие этого метод __getattr__ удобно использовать для
обобщенной обработки запросов к атрибутам. Например:"""


class Empty:
    def __getattr__(self, item):
        if item == 'age':
            return 40
        raise AttributeError(item)
'''В этом примере класс empty и его экземпляр X не имеют своих собственных
атрибутов, поэтому при обращении к атрибуту X.age вызывается метод __������getattr__
– в аргументе self передается экземпляр (X), а в аргументе attrname – строка
с именем неопределенного атрибута (“age”). Класс выглядит так, как если бы
он действительно имел атрибут age, возвращая результат обращения к имени
X.age (40).В результате получается атрибут, вычисляемый динамически.
Для атрибутов, обработка которых классом не предусматривается, метод __���getattr__
возбуждает встроенное исключение AttributeError, чтобы сообщить ин-
терпретатору, что это действительно неопределенные имена, – попытка обращения 
к имени X.name приводит к появлению ошибки.'''
obj = Empty()
print(obj.age)
#print(obj.name) #AttributeError: name

'''•• Метод __getattribute__ вызывается при обращениях к любым атрибутам, не
только к неизвестным; но при реализации этого метода следует быть еще
более осторожным, чем при реализации метода __getattr__, чтобы избежать
зацикливания.'''


'''Родственный ему метод перегрузки __setattr__ перехватывает все попытки при-
сваивания значений атрибутам. Если этот метод определен, выражение self.
attr = value будет преобразовано в вызов метода self.__setattr__(‘attr’, value).
Работать с этим методом немного сложнее, потому что любая попытка выпол-
нить присваивание любому атрибуту аргумента self приводит к повторному
вызову метода __setattr__, вызывая бесконечный цикл рекурсивных вызовов
(и, в конечном итоге, исключение переполнения стека!). Если вам потребуется
использовать этот метод, все присваивания в нем придется выполнять посред-
ством словаря атрибутов, как описывается в следующем разделе. Используйте
self.__dict__[‘name’] = x, а не self.name = x:'''


class accescontrol:
    def __setattr__(self, key:'attr', value):
        if key=='age':
            #self.key = value #рекурсия
            self.__dict__[key]=value # чтобы избежать рекурсии

        else:
            raise AttributeError(key+' not allowed')

obj = accescontrol()
obj.age=40
#obj.name="danil" #AttributeError: name not allowed