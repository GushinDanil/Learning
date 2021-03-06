import oop.second.second as second

print('''module mod-----------------------------''')
my_obj = second.FirstClass
my_obj.data = 222
my_obj().display()  # вот как нужно вызывать методы класса используя объект класса а не экземпляра


my_obj().data=333 # атрибуту объекта экземпляра присвоили значение но оно не сохранилось
my_obj().display() # потому что не привязали ссылку на этот объект экземпляр(по умолчанию возьмёт атрибут класса)


class ThridClass(second.SecondClass):
    def __init__(self, value):
        self.data = value


    def __add__(self, other ) :
        '''эта запись создаёт новый объект экземпляр с вызовом конструктора
        __init()__ (видно же что это создание нового экземляря)'''
        return ThridClass(self.data + other)

    def __str__(self):
        return '[ThridClass : {0}]'.format(self.data)

    def mul(self, other):
        self.data *= other


'''Методы со специальными именами, такими как __init__, __add__ и __str__, на-
следуются подклассами и экземплярами, как любые другие имена, которым
выполняется присваивание в инструкции class'''

a = ThridClass('abc')
a.display()
print(a)
b = a + 'de'  # создание нового экземпляра
b.display()
a.mul(3)  # умножение

print(a.__class__)  # ссылка на наследуемый класс
print(ThridClass.__bases__) # кортеж суперклассов этого класса



def upper_name(self):
    return self.data.upper()

print(upper_name(a))
ThridClass.method=upper_name
print(a.method)


'''Обычно заполнение классов производится внутри инструкции class, а атри-
буты экземпляров создаются в результате присваивания значений атрибутам
аргумента self в методах. Однако отметим снова, что все это не является обяза-
тельным, поскольку ООП в языке Python – это в основном поиск атрибутов во
взаимосвязанных объектах пространств имен.'''



'''Чисто формулировка которая и так понятна'''
'''Экземпляры класса действительно являются 
разными пространствами имен: каждый из них имеет
свой словарь атрибутов(имеется ввиду что имеют свой индивидуальный
 набор атрибутов а доступ к ним обеспечивается как по ключу в словаре(object.attribute)).
Обычно экземпляры единообразно наполняются атрибутами
в методах класса, тем не менее они обладают большей гибкостью, чем
можно было бы ожидать.'''



'''Наконец, несмотря на всю гибкость таких типов, как словари, классы позволя-
ют наделять объекты поведением таким способом, который встроенными типа-
ми и простыми функциями напрямую не поддерживается. Хотя мы и можем
сохранять функции в словарях, тем не менее использование их для обработки
данных в словарях не выглядит столь же естественным, как такое их исполь-
зование в классах.'''



'''Перегрузка операторов в языке Python выполняется с помощью методов со
специальными именами – они начинаются и заканчиваются двумя симво-
лами подчеркивания. Эти имена не являются встроенными или зарезер-
вированными именами – интерпретатор Python просто автоматически вы-
зывает методы с этими именами, когда экземпляр появляется в составе со-
ответствующей операции. Язык Python определяет порядок отображения
операций на специальные имена методов

Перегрузка операторов может использоваться для реализации объектов, ко-
торые имитируют поведение встроенных типов (например, последователь-
ностей или числовых объектов, таких как матрицы), и для реализации ин-
терфейсов встроенных типов, которые ожидают получить те или иные части
программного кода. Кроме того, имитация интерфейсов встроенных типов
позволяет передавать в экземплярах классов информацию о состоянии – то
есть атрибуты, в которых сохраняются данные между вызовами операций.
Однако не следует использовать перегрузку операторов, когда достаточно ис-
пользовать простые методы'''

