ls = list(map(int, input("Enter elements: ").split()))
s = 0
e = len(ls)-1
while s <= e:
    if ls[s] == ls[e]:
        flag = 1
        s = s+1
        e = e-1
    else:
        flag = 0
        break
if flag == 1:
    print("is pallindrome")
else:
    print("not pallindrome")
