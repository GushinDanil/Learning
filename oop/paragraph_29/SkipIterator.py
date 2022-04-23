class SkipIterator:
    def __init__(self,wrapped):
        self.wrapped=wrapped
        self.offset=0

    def __next__(self):
        """
        двигается по итерируемуму объекту
        пока в не дойдёт до конца
        в конце исключение которые перехватывает
        итерационный контекст(for,while) или ты
        :return: елемент итерируемого объекта
        """
        if self.offset>=len(self.wrapped):
            raise StopIteration
        item= self.wrapped[self.offset]
        self.offset+=1
        return item

class SkipObject:
    def __init__(self,wrapped):
        self.wrapped=wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped)


if __name__=='__main__':
    '''
    Этот пример работает подобно вложенным циклам с обычными строками –
    каждый активный цикл запоминает свое положение в строке, потому что каж-
    дый из них получает независимый объект итератора, который хранит свою
    собственную информацию о состоянии
    Наш более ранний пример класса Squares, напротив, поддерживал всего одну
    активную итерацию, нужно было во вложенных циклах вызывать Squares сно-
    ва, чтобы получить новый объект. Здесь у нас имеется единственный объект
    SkipObject, который создает множество объектов итераторов.'''
    obj = SkipObject('str object')
    it=iter(obj)
    print(next(it),next(it),next(it))

    for x in obj:
        for y in obj:
            print(x+y, end=' ')
'''Мы могли бы использовать этот механизм, например, для создания объекта
базы данных, чтобы одновременно выполнять несколько итераций в одном
и том же наборе данных, извлеченном в результате запроса к базе данных'''
