C=1
D=2
A,B=C,D # Присваивание кортежей
print(A,B) # Что равносильно A = C; B = D
[T,F]=[A,B] # Присваивание списков
print(T,F)

a,b,c=[1,2,3] # 1,2,3
print(a,b,c)

a,b,c='ABC' # A,B,C
print(a,b,c)

a,*b='ABC' # A, ['B','C']
print(a,b)

*a,b='ABC' # ['A','B'],C
print(a,b)

a,*b,c='spam' # s ,['p','a'], m
print(a,b,c)

a,b,*c='abc' # a,b,['c']
print(a,b,c)

a,b,c,*d='abc' # a,b,c,[]
print(a,b,c,d)

a,b,*e,c,d='abcd'
print(a,b,e,c,d)

*e,='abcd'
print(e)



string='spam'  # s pa m
a,b,c=string[0],string[1:3],string[string.__len__()-1] # а забирает вс' кроме последнего элемента
print(a,b,c)




string='spam' # s p am
a,b,c=string[0],string[1],string[2:] # срез исключение в єтом случае
print(a,b,c)


a,b=('sp','am') # sp am
print(a,b)


a,(b,c)=('sp'),'am' # sp a m
print(a,b,c)

print('-' * 50)
a,b,c=range(3)
print(a,b,c)


