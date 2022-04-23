def new_func(a : int = 1, b: str = ' ') -> int:
    # Если ты делаешь значение по умолчанию то нужно делать для всех аргументов
    """It's just returns Hello World"""
    return False, 2, 4
    return 2
    return 'Hello World', 1

def empty_func():
    pass#означает что наша функция пустая
new_func(2, ' ')

a, b, c = new_func(a=7, b='Hello')
_, b, c = new_func(b='Hello', a=7)
_, _, c = new_func(b='Hello')
print(a, b, c)

print(id(a))
a=2
print(id(a))
print(a)
