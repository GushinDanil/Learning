import oop.paragraph_28.many_names as m_n
X = 66
print(X) # 66: здешняя глобальная переменная
print(m_n.x) # 11: глобальная, ставшая атрибутом в результате импорта
m_n.f() # 11: X в manynames, не здешняя глобальная!
m_n.g() # 22: локальная в функции, в другом файле
print(m_n.C.x) # 33: атрибут класса в другом модуле
I = m_n.C()
print(I.x) # 33: все еще атрибут класса
I.m()
print(I.x) # 55: а теперь атрибут экземпляра!
