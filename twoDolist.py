ls = [ [1, 2, 3, 4],
       [5, 6, 7, 8],
       [4, 5, 6, 7],
       [3, 4, 5, 6],
     ]
for x in range(4):
    if x%2 ==0:
        for y in range(4):
            print(ls[x][y],end=" ")
    else:
            for y in range(3,-1,-1):
                print(ls[x][y],end=" ")
    print()
