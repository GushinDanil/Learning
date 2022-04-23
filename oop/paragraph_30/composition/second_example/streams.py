class Processor:
    """композиция преполагает встраивание стронних объектов в объект
    контейнер чтобы использовать их для реализации своих методов(process)
    метод converter здесь нужно просто опеределить в подклассе для реализации уникального поведения
    метода process для каждого подкласса"""
    def __init__(self,reader,writer): # это приём композиции
        self.reader=reader
        self.writer=writer

    def converter(self):
        assert False , 'method converter is not defined'

    def process(self):
        with self.reader as file:
            for row in file:
                self.writer.write( self.converter(row))


