print(ord('a'))
i=97
for x in range(1,5):
    for y in range(1,5):
        if x>=y:
            print(" ",end=chr(i))
            i=i+1
    print()

    
