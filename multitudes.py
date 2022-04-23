vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = {}
found['1']={'Name':'Boris'}
found[1]={'Name':{}}
print(found[1])
found= (set(vowels).intersection( set(word)))
print(type(found))
print(type(vowels))
print(found)
