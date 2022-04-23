'''switch alternative'''
choice = 'spam'
d = {
    'ham': 1,
    'spam': 2
}[choice]

print(d)

branch = {1: 'a', 2: 'b', 3: 'c'}
print(branch.get(4, 'didn\'t find '))

empty = ...
print(empty)
