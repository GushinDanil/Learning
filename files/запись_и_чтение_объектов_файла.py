
objects = open('objects.txt', 'w')
#записывать в файл можно только строковые литералы
objects.write(str([1, 2, 3]) + '$' + str({1: 'a', 2: 'b', 3: 'c'}) + '\n')
x, y, z = 1, 2, 3
objects.write('{0},{1},{2}\n'.format(x, y, z))
objects.close()

S = open('objects.txt').read()
print(S)

with open('objects.txt') as objects:
    line = objects.readline()
    line.rstrip()  # Удалить символ конца строки
    collections = [eval(i) for i in line.split('$')]
    print(collections[0])
    print(collections[1])

    parts = objects.readline()
    x, y, z = [int(i) for i in parts.split(',')]
    print(x, y, z)

'''
Модуль pickle выполняет то,
что называется сериализацией объектов, – преобразование объектов в строку
байтов и обратно, не требуя от нас почти никаких действий в отличие от предыдущего примера
нужно только сохранять эти объекты в файл с соответствующим расширением'''
import pickle

data = [1, 2, 3]
file = open('data.pkl', 'wb')
pickle.dump(data, file)
file.close()
file = open('data.pkl', 'rb')
result = pickle.load(file)
print('-' * 50)
print(result)
