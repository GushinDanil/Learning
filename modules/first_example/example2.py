from modules.first_example import c

c.x=0
c.y[0]=0
c.y[1]=1



'''ОПЕРАЦИЯ ИМПОРТА ВЫПОЛНЯЕТСЯ ТОЛЬКО ОДИН РАЗ
ПОЭТОМУ СОСТОЯНИЕ X Y БУДЕТ ИЗМЕНЁННЫМ ДАЖЕ ПРИ ПОПЫТКЕ ИМПОРТИРОВАТЬ ЗАНОВО
НО ПОЛУЧИТЬ ЗАНОВО ИСХОДНЫЕ ДАННЫЕ ИЗ МОДУЛЯ ПОМОЖЕТ ФУНКЦИЯ reload
'''
from modules.first_example.c import x,y
print(x,y)

