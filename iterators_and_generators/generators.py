'''Генераторы списков собирают результаты применения произвольного выраже-
ния к элементам последовательности и возвращают их в виде нового списка.


В действительности, генераторы списков обладают еще большей гибкостью.
Они дают возможность запрограммировать любое число вложенных циклов
for, каждый из которых может сопровождаться собственным оператором if
с условным выражением. В общем виде генераторы списков выглядят следую-
щим образом:
[ expression for target1 in sequence1 [if condition]
for target2 in sequence2 [if condition] ...
for targetN in sequenceN [if condition] ]'''
l = [i.rstrip().upper() for i in open('text.txt')]
print(l)

l2 = [('is' in line, line[0],list(open('text.txt'))[key].rstrip()) for key, line in enumerate( open('text.txt'))]  # гибкость бешанная
print(l2)

l3 = [('is' in line, line[0]) for line in open('text.txt')
      if line[line.rstrip().__len__() - 1] == 's' or
      line[line.rstrip().__len__() - 1] == 'S']
print(l3)
l4 = {x: y for x in [1, 2, 3] for y in [4, 5, 6]}  # в словаре будет 3 элемента
# а не 6 потому что только 3 уникальных ключа
# дальще будет переприсваивание по ключу
print(l4)
l4 = [x + y for x in [1, 2, 3]  if x<4
            for y in [4, 5, 6]  if y>3]
print(l4)

l4 = list(map(str.upper, open('text.txt')))
print(l4)

d1 = {k: str.rstrip(v) for k, v in enumerate(open('text.txt'))}
print(d1)

