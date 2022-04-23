"""Рекурсивными называются функции, которые сами вызывают себя прямо
или косвенно. Они могут использоваться для обхода структур данных про-
извольной формы, но они также могут использоваться и для реализации
итераций (хотя итерации зачастую более просто и эффективно реализуются
с помощью инструкций циклов)."""
def mysum1(L):
    print(L)
    if not L:  # вернётся True если пустая
        return 0
    return L[0] + mysum1(L[1:])


print(mysum1([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5]))  # альтернатива


def mysum2(L):
    return 0 if not L else L[0] + mysum2(L[1:])  # Трехместный оператор


print(mysum2([1, 2, 3, 4, 5]))


def mysum3(L):
    if not L:
        return False
    first, *rest = L
    return first if not rest else first + mysum3(rest)


print(mysum3([1, 2, 3]))
print(mysum3(['a', 'b', 'c']))

print('-' * 50)


def mysum4(L):
    if not L:
        return 0
    return none_empty(L)


def none_empty(L):
    return L[0] + mysum4(L[1:])  # косвенная рекурсия


print(mysum4([1, 2, 3, 4, 5]))

'''С другой стороны, рекурсия  может оказаться востре-
бованной для реализации обхода структур данных с произвольной организа-
цией.'''


def sum_tree(L):
    res = 0
    for x in L:
        if isinstance(x, list):
            res += sum_tree(x)
        else:
            res += x
    return res


print(sum_tree([1, 2, [3, [4, 5], 6]]))


