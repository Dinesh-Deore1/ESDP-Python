num=10
for x in range(1,num+1):
    for y in range(1,num+1):
        if (x==num or y==num or x+y>=num+1 ):
            print(" ",end="*")
        else:
            print(" ",end=" ")
    print()
