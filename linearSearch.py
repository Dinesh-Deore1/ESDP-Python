ls = list(map(int,input("Enter elements: ").split()))
print("list = "+str(ls))
num = int(input("Enter element you want to search: "))
flag=0
for x in range(0,len(ls)):
    if num==ls[x]:
        flag=1
        break
    else:
        flag=0
if flag==1:   
    print("element found at index: "+str(x))
else:
    print("Element not")
