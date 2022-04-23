# Подкласс встроенного типа/класса list.
# Отображает диапазон 1..N на 0..N-1; вызывает встроенную версию.
class MyList(list):
    """В этом файле подкласс MyList расширяет метод __getitem__ встроенных списков
    простым отображением диапазона значений от 1 до N на необходимый спискам
    диапазон от 0 до N-1. Уменьшение индекса на единицу и вызов версии метода
    из суперкласса – вот все, что в действительности делается, но этого вполне до-
    статочно для достижения поставленной цели:"""

    def __getitem__(self, item):
        return list.__getitem__(self, item - 1)


if __name__ == "__main__":
    print(list("abc"))
    x = MyList("abc")  # __init__ наследуется из списка
    print(x)  # __repr__ наследуется из списка
    print(x[1])  # MyList.__getitem__
    print(x[3])  # Изменяет поведение метода суперкласса
    x.append("spam");
    print(x)  # Атрибуты, унаследованные от суперкласса list
    x.reverse();
    print(x)

"""
Следующий пример реализации класса в файле setsubclass.py адаптирует спи-
ски, добавляя методы и операторы, используемые для работы с множествами.
Все остальное поведение наследуется от встроенного суперкласса list, поэтому
альтернатива получилась более короткой и простой:
"""


class Set(list):
    def __init__(self, value=[]):  # Конструктор
        list.__init__([])  # Адаптирует список
        self.concat(value)  # Копировать изменяемый аргумент по умолчанию

    def intersect(self, other):  # other – любая последовательность
        res = []  # self – подразумеваемый объект
        for x in self:
            if x in other:  # Выбрать общие элементы
                res.append(x)
        return Set(res)  # Вернуть новый экземпляр Set

    def union(self, other):  # other – любая последовательность
        res = Set(self)  # Копировать меня и мой список
        res.concat(other)
        return res

    def concat(self, value):  # аргумент value: list, Set...
        for x in value:  # Удалить дубликаты
            if not x in self:
                self.append(x)

    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return "Set: " + list.__repr__(self)

print("-"*50)
if __name__ == "__main__":
    x = Set([1, 3, 5, 7])
    y = Set([2, 1, 4, 5, 6])
    print(x, y, len(x))
    print(x.intersect(y), y.union(x))
    print(x & y, x | y)
    x.reverse();
    print(x)

"""Существуют более эффективные способы реализации множеств – с помощью
словарей, которые позволяют заменить последовательное сканирование, ис-
пользуемое в данной реализации, на операцию обращения по ключу (хеши-
рование) и тем самым повысить скорость работы."""
