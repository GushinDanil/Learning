phrase = "Don't panic!"
plist = list(phrase)
dlist = phrase.split()
print(dlist)

word = ['a','b','c']
word.insert(0,'*')
word.insert(3,'*')
word.remove('*')
print(word.count('*'))
word.append(['f','g'])
word.append('j')
word.insert(8,'*')
print(word.__len__())
print(word)
print(word.pop(1))
print(word)

print(plist[ : :2 ])
print(plist[:2])
print(plist[5:])
print(plist[-1])
print(plist[::-1])
L = list(range(-4, 4))
L2 = list([-4, 4])
print(L,L2)

li= [12,3]
li[1]=12
li[2]=12