word = ['a','b','c']
word.insert(0,'*')
word.insert(3,'*')
word.remove('*')
word.extend(['d','e'])
print(word)
word+=['1','2']
word.pop(2)
del word[0]
print(word)
word.append(['f','g'])
word.append('j')
word.insert(8,'*')
print(word.__len__())
print(word)
word.remove(['f','g'])

print(word)


print('-'*50)
L=[1,2,3]
print(L*4)
print([L]*4)


