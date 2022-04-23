# open('text.txt', 'a')  # открыть файл для записи в конец
# open('text.txt', 'w')  # открыть файл записи.Если данніе уже есть они удалятся
# open('text.txt', 'r')  # открыть файл для чтения. Если вторым аргументом ничего нету сработает этот вариант
# open('text.txt', 'x')  # создать открыть новый файл для записи а если такой уже существует то будет ошибка
# open('image.png', 'wb')  # для  нетекстовых файлов нужно ещё добавить b(открыть в двоичном виде,binary)
# open('image2.png', 'x+b')  # означает читать и записывать в новый двоичный файл(который эта функция и создаст)
# второй параметр называется строка режима доступа к файлу


file = open('text.txt')  # создаём файловый дескриптор на чтение
for row in file:
    print(row, end='\n')
file.close()

'''Ниже вариант без функции сlose : конструкция with(контекстный менеджер)'''
print('---------------------------------------------')
with open('text.txt') as file:
    for row in file:
        print(row)

'''два варианта 1(открытие файла с отключением экранирования символов слешём)
    2(открытие файла с экранированием самого слеша)'''
# myfile = open(r'C:\new\text.dat', 'w')
# myfile = open('C:\\new\\text.dat', 'w')
print(50 * '-')
my_file = open('text.txt', )
print(my_file.readlines())  # записывает файл в список строк построчно
my_file.close()
print('-' * 50)
my_file = open('text.txt', )
print(my_file.read())  # записывает файл в одну строку каждая строка будет заканчиваться символом \n
my_file.close()
print('-' * 50)
my_file = open('text.txt', )
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
print(my_file.readline(), 'last symbol is \\n')
print(my_file.writable())  # проверка можно ли писать в него(открыт ли он на запись)
print(my_file.closed)  # проверка на то закрыт ли он
print(my_file.readable())  # проверка на чтение
print(my_file.name)  # имя файла

my_file.close()

'''если необходимо просмотреть содержимое файла строку за строкой, лучшим
выбором будет итератор файла(цикл или with/as)'''
print(1,5, 10, 15, sep='...', file=open('text.txt', 'a'))

