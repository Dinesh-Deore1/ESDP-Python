n = int(input("Enter the number: "))
flag=0
for x in range(2,n):
    if n%x == 0:
        flag=1
if flag == 1:
    print("not prime")
else:
    print("prime")
