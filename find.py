vowels = ['a', 'e', 'i', 'o', 'u']
found = {}

print(type(found))
word = input("Please enter new word : ")
for letter in word:
    if letter in vowels:
        if letter in found:
            found[letter] = found[letter] + 1
        else:
            found[letter] = 0
            found[letter] = found[letter] + 1


for k, v in sorted(found.items()):

    print(k, v)

vowels = ['a', 'e', 'i', 'o', 'u']
found = {}

print(type(found))
word = input("Please enter new word : ")

for letter in word:
    if letter in vowels:
        found.setdefault(letter,0)
        found[letter] = found[letter] + 1
                                              

for k, v in sorted(found.items()):
    print(k, v)
