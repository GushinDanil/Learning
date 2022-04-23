"""
Атрибуты класса совместно используются всеми его экземплярами, поэтому,
если атрибут класса ссылается на изменяемый объект, изменение этого объек-
та из любого экземпляра отразится сразу на всех экземплярах:"""


class Parent:
    p = 15


class C(Parent):
    shared = []

    def __init__(self):
        self.perobj = []


x = C()
y = C()
x.shared.append('spam')
x.perobj.append('spam')  # Изменит данные, принадлежащие только объекту x
parent = Parent()
print('Shared: x =', x.shared, ',y =', y.shared)
print('Perobj: x =', x.perobj, ',y =', y.perobj)
print('p: x =', x.p, ',y =', y.p)
