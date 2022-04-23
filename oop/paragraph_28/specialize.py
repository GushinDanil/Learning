class Super:
    def method(self):
        print('in Super')

    def delegate(self):
        self.action()

    def action(self):
        assert False, 'action must be defined'


class Inheritor(Super):  # наследник перевод
    pass


class Replacer(Super):
    def method(self):  # полностью замещает
        print('in Replacer')


class Extender(Super):
    def method(self):  # частично замещает
        print('In Extender')
        Super.method(self)
        print('End Extender')


class Provider(Super):
    def action(self):
        print('in Provider.action')


if __name__ == '__main__':
    for obj in (Inheritor, Replacer, Extender):
        print('\n' + obj.__name__ + '...')
        obj().method()
    print()
    x = Provider()
    x.delegate()


