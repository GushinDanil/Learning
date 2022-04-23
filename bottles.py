
word="bottles"
for i in range(99,0,-1):
    print(i,word,"of beer on the wall")
    print(i,word,"of beer")
    print("Take one down")
    print("Pass it around")
    if  i==1:
        print("Don't have bottles of beer")
    else:
        new_num = i-1
        if new_num==1:
            word="bottle"
    print(i,"of beer on the wall")
    print()

