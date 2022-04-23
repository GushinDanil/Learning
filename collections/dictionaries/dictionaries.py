"""Ключами в словарях могут быть только неизменяемые объекты"""
struct = {(1, 2, 3): 1, (4, 5, 6): 2}  # пример разрешённой структуры данных
m = {
    '3': 'a',
    '2': 'b',
    '1': 'c',
    '4': 'd',
    '5': 'd',
}
del m['5']
m.update({'6': 'y', '7': 't'})
m['8'] = 'z'

print(m.get('1', 'kiss'),  # kiss это строковый литерал который я получу по умолчанию если не будет в словаре ключа 1
      m['1'])  # различие в том что если мы будем обращаться к несуществуещему элементу(с помощью get) мы не получим
# ошибку а получим объкт None или элемент по умолчанию который можно указать вторым параметром
print(m.pop('6'))
print(m)
print('-' * 50)
for key, val in sorted(m.items()):
    print(key, val)
for key in m:
    print(key)
'''Дальше различные варианты инициализации объекта словаря'''
d = dict(name='Bob', age='40')  # Форма именованных аргументов(ключи будут строками)
print(d['name'])
d2 = dict([('name', 'mel'), ('age', 45)])  # Кортежи ключ/значение
print(d2)
d3 = dict.fromkeys(['a', 'b'], 0)  # 0 это значение по умолчанию ключей а и b
print(d3)
print(dict(zip([1, 2, 3], ['a', 'b', 'c'])))
print(list(zip([1, 2, 3], ['a', 'b', 'c'])))
print(tuple(zip([1, 2, 3], ['a', 'b', 'c'])))

'''generator of dictionaries'''
print('-' * 50)
print('generator of dictionaries')

d5 = {k: v for (k, v) in zip([1, 2, 3], ['a', 'b', 'c'])}
print(d5)

d6 = {x: x ** 2 for x in [1, 2, 3]}
d7 = {x: x * 3 for x in 'spam'}
print(d6, d7)

for (k, v) in zip([1, 2, 3], ['a', 'b', 'c']):
    print(k, v)

'''проверка наличия элемента'''
a = {1: 'Camaro', 2: 'Benz'}
if 2 in a:
    print(a[2])

print('-' * 50)
'''если хочется сравнить словари'''
D1 = {'a': 1, 'b': 2}
D2 = {'a': 1, 'b': 3}
print(D1 == D2)
D1.update(D2)  # в таком случае  поменяются просто значения ключей
print(D1)
print(sorted(D2.items()) > sorted(D1.items()))  # важное условие они должні біть отсортировані

print([1, 2, 3] is [1, 2, 3])
a = [1, 2, 3]
b = a
print(a is b)
a = 3
b = a
del b
print(a)
a=5.2
print(a)


