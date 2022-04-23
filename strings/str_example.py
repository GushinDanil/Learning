a = ['Eric', 'Mark', 'John']
b = '|'.join(a)
print(b)
c = b.split('|')
print(c)
S = 'spammmm'
S = 'z' + S[1:]
# S[0]='z' # Неизменяемые объекты нельзя изменить(ощшибка)
print(S)
print(S.upper())
print(S.find('s'))
print(S.find('m',4))
print(S)
