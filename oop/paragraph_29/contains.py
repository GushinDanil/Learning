class Iters:
    def __init__(self, value):
        self.data = value

    def __iter__(self):
        print("iter=> ", end='')
        self.ix = 0
        return self

    def __next__(self):
        print("next:", end='')
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __getitem__(self, item):
        print('get[%s]:' % len(self.data), end='')
        return self.data[item]

    def __contains__(self, item):
        print("contains: ", end='')
        return item in self.data


if __name__ == '__main__':
    obj = Iters([1, 2, 3, 4, 5])
    print(3 in obj)
    for i in obj:  # Циклы
        print(i, end=' | ')
    print()
    print([i ** 2 for i in obj])  # Другие итерационные контексты
    print(list(map(bin, obj)))
    I = iter(obj)  # Обход вручную (именно так действуют
    while True:  # другие итерационные контексты)
        try:
             print(next(I), end=' @ ')
        except StopIteration:
             break
    print()
    print(obj[1:]) # передаётся объект слайса
    print(obj[slice(1,None)])
