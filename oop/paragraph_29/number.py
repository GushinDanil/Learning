class Number:
    def __init__(self, start):
        self.data = start

    def __sub__(self, other):  # Выражение: экземпляр - other
        # subtraction(Вычитание)
        """метод реализации операции вычитания"""
        return Number(self.data - other)  # Результат – новый экземпляр


obj = Number(15)
obj = obj - 10
print(obj.data)

print('-'*50)

class Indexer:
    data = [1, 2, 3, 4, 5]

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):

        self.data[key] = value


ind = Indexer()
print(ind[6])  # Выражение ind[i] вызывает ind.__getitem__(i)
for i in range(5):
    print(ind[i], end=" ")
print(ind[1:4])
ind[0] = 0
ind[:2] = [1]
for i in ind:
    print(i, end=" ")
"""метод __getitem__ можно также квалифицировать как аля перегрузку метода __iter__ и
__next__  Инструкция for многократно применяет операцию индексирования 
к последовательности, используя индексы от нуля и выше, пока не будет получено исключение
выхода за границы(IndexError) в то время как перегрузка __iter__ и
__next__ заставляет инструкцию for обходить последовательность
при помощи метода __next__ а не индексирования и исключение в конце уже будет StopIteration
но различие не только в этом


в отличие от __getitem__, схема на основе метода __iter__ предназначена для
выполнения обхода элементов один раз, а не несколько. Например, элементы
класса Squares можно обойти всего один раз – для каждой последующей итера-
ции необходимо будет создавать новый объект итератора:"""
print()
i = iter(ind)
print(next(i))



