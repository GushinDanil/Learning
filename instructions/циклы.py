
print('-' * 50)
for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:
    print(a, b, c)

print('-' * 50)
for (a, b), c in [((1, 2), 3), ((4, 5), 6)]:  # уровни вложенности должны быть симметричны
    print(a, b, c)

print('-' * 50)
for a, c in [((1, 2), 3), ((4, 5), 6)]:  # уровни вложенности должны быть симметричны
    print(a, c)

print('-' * 50)
for a in [((1, 2), 3), ((4, 5), 6)]:  # уровни вложенности должны быть симметричны
    print(a)
print('-' * 50)
for a, b in [((1, 2), 3), ((4, 5), 6), (1, 2)]:  # тоже интересно
    print(a, b,'тоже интересно')
'''ПРИМЕР НИЖЕ ПОЯСНЯЕТ ВСЁ '''
print('-' * 50)
for a, (b, c, d, (g, z)) in [(1, (1, 2, 3, [1, 2])), (2, (4, 5, 6, [1, 2])), (3, (4, 5, 6, [1, 2]))]:  # тоже интересно
    print(a, b, c, d, g, z)

print('-' * 50)
for a, *b in [(1, 2, 3, [1, 2]), (4, 5, 6, [1, 2]),
              (4, 5, 6, [1, 2])]:  # b становится здесь списком и забирает то что остаётся
    print(a, b)

print('-' * 50)
L = [1, 2, 3, 4, 5]
while L:
    #  front,L=L[0],L[1:] # работает точно также
    #  front,*L=L # тоже самое
    front = L.pop()
    print(front, L)

for i in range(4):
    print(1)
else:
    print('else')  # но если будет break то оно не выполнится

for ((a, b), c) in [([1, 2], 3), ['XY', 6]]:
    print(a, b, c)


print('-'*50)
print(list(range(2,5))) # start,stop,step
print(list(range(0,10,2)))
print(list(range(7,-7,-1)))


print('-'*50)

T1, T2, T3 = (1,2,3), (4,5,6), (7,8,9)
print(list(zip(T1,T2,T3)))
for i in zip(T1,T2,T3):
    print(i)

s1='abc'
s2='xyz123'
print(list(zip(s1, s2)))
print('-'*50)


word='spam'
for index,val in enumerate( word):
    print(index,val)

print(~15)
