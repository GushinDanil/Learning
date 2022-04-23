from abc import ABCMeta,abstractmethod
class Super(metaclass=ABCMeta):
    '''абстрактныe суперклассы – классы, которые предполагают
    , что часть их функциональности будет реализована
    их подклассами. Если ожидаемый метод не определен в подклассе, интерпре-
    татор возбудит исключение с сообщением о неопределенном имени, когда по-
    иск в дереве наследования завершится неудачей.'''
    def delegate(self):
        self.action()
    @abstractmethod
    def action(self):
        pass


class Sub(Super):
    def action(self):
        print('spam')

class Sub2(Super):
    pass

obj=Sub()
#obj2=Sub2() # исключение
obj.delegate()

'''Хотя при такой реализации объем программного кода
увеличивается, тем не менее она имеет свои преимущества – ошибки из-за от-
сутствующих методов будут появляться при попытке создать экземпляр клас-
са, а не позднее, при попытке вызвать отсутствующий метод. Данная возмож-
ность может использоваться для построения ожидаемого интерфейса, полнота
реализации которого будет автоматически проверяться в клиентских классах.'''