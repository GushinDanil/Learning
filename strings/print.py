# print(str(x,y,z) )# str как и его коллеги принимает только
# один объект поэтому ниже показано как это можно обойти
print('{0} vam {1} world'.format('xyz','hello'),end=' end\n')
print('%s vam %s world' % ('xyz','hello'),end=' end\n')
print(len('\0'))
s='Hello' ' World' # выражение неявной конкатенации
print(s)
print('-'*80)
s='a\nb\tc'
print(s)
print(len(s)) #выводит количество байт


