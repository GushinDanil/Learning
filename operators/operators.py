i = 10
print(~i,'  :Битовая операция НЕ (инверсия) ')
a = i
print(i is a ,'  :укажет истинну если id(a) и id(i) совпадают(тоесть они эвивалентны тк имеют разделяемую ссылку)')
i = 5
print(i is a)
print('-------------------------------------------')
bit = 16
print(bit << 1,'на увеличение')
print(bit >> 1,'на уменьшение')

print(2&3,'  : Здесь бинарная 2 — это 10, а 3 — 11. Результатом побитового and является 10 — бинарная 2.')
print(3&4,'  : Побитовое and над 011(3) и 100(4) выдает результат 000(0).')
print('----------------------------------------------')
print(2 | 3,'  : Проводит побитовую операцию or на двух значениях. Здесь or для 10(2) и 11(3) возвращает 11(3).')
print(2^3,'XOR исключающее ИЛИ( Здесь бинарная 2 — это 10, а 3 — 11. Результатом побитового and является 01)')

#здесь представлены операции над множествами
print({'tom','ben','sue'} ^ {'jim','tom','sue'})# исключающее пересечение
print({'tom','ben','sue'} | {'jim','tom','sue'})# объединение
print({'tom','ben','sue'} & {'jim','tom','sue'})#пересечение

a=[1,2,3,4]
print(a[0::-1])