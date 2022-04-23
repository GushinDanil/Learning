def func():
    print(func.attr)
    return 'Hello World'


func.attr='value'
other_name = func
print(other_name())



def new_func(a : int = 1, b: str = ' ') -> int:
    # Аргументы со значениями по умолчанию идут после аргументов без значений по умолчанию
    """It's just returns Hello World"""
    return False, 2, 4
    return 2
    return 'Hello World', 1

def empty_func():
    pass#означает что наша функция пустая
new_func(2, ' ')

a, b, c = new_func(a=7, b='Hello') # позиционные аргументы идут только перед именованными
_, b, c = new_func(b='Hello', a=7)
_, _, c = new_func(b='Hello')
print(a, b, c)




def func(a,b,c):
    print(a,b,c)
'''вместо 2 должен быть именнованный аргумент
иначе они оба притендуют на то чтобы быть в переменной а'''
# func(2,3,a=3) #func() got multiple values for argument 'a'