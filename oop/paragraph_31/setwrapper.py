class Set:
    """По большей части этот класс
    просто обертывает список, добавляя дополнительные операции."""
    def __init__(self,value=[]):
        self.data=value

    def concat(self,conq): # Аргумент conq: список, Set...
        for i in conq:
            if not i in self.data: # Отфильтровать дубликаты
                self.data.append(i)

    def union(self,conq):   # conq – любая последовательность
        res=self.data.copy()    # Копировать список
        for i in conq:
            if not i in res:
                res.append(i)   # Добавить уникальные элементы из conq
        return Set(res)

    def intersect(self,conq):
        res=[]
        for i in self.data:
            if i in conq:
                res.append(i)
        return Set(res)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        return self.data[item]

    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return "Set : "+repr( self.data)


x = Set([1, 3, 5, 7])
print(x.union(Set([1, 4, 7]))) # Выведет: Set:[1, 3, 5, 7, 4]
print(x & Set([1, 4, 6])) # Выведет: Set:[1]
