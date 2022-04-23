a = 5
print(a + 2)
b = 4  # вот зачем может понадобиться точка с запятой но так делать ненадо

if (3 > a > 2 or
        b > 2):  # доступно только с круглыми скобками
    print('cool')

print('-' * 50)
res=0
while True:
    num = input('Enter number : ')
    if num == 'stop':
        break
    elif not num.isdigit():
        print('Bad reply')
    else:
        res+=int(num) ** 2
print(res)
''' или '''
while True:
    reply = input('Enter number : ')
    if reply == 'stop':
        break
try:
    num = int(reply)
except:
    print('Bad reply')
else:
    num = num ** 2
