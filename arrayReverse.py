ls = list(map(int,input("Enter list elements: ").split()))
ls2 = [0]*len(ls)
j=len(ls)-1
for x in range(0,len(ls)):
    ls2[x]=ls[j]
    j=j-1
  print(ls2)
