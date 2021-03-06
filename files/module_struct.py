'''Сохранение и интерпретация упакованных двоичных данных в файлах
в некоторых приложениях приходится иметь дело с упако-
ванными двоичными данными, которые создаются, например, программами
на языке C. Стандартная библиотека языка Python включает инструмент, спо-
собный помочь в этом, – модуль struct, который позволяет сохранять и восста-
навливать упакованные двоичные данные. В некотором смысле, это совершен-
но другой инструмент преобразования данных, интерпретирующий строки
в файлах как двоичные данные.
'''



'''По моему мнению этот модуль позволяет нам упакавать данные в двоичном формате скопом
а затем их все вместе распакавать'''
import struct

f = open('my.bin','wb')
data=struct.pack(b'>i4sh', 7, b'spam', 8) # Создать пакет двоичных данных
print(data)
f.write(data)
f.close()

f = open('my.bin','rb')
data = f.read()
values = struct.unpack(b'>i4sh',data)
print(values)
f.close()