ls = list(map(int,input("Enter elements: ").split()))
ls.sort()
print("list = "+str(ls))
num = int(input("Enter element you want to search: "))
s=0
e=len(ls)-1
while s<=e:
    mid = (s+e)//2
    if ls[mid]==num:
        print(f"Element is found at index: {mid}")
        break
    elif ls[mid]<num:
        s = mid+1
    else:
        e=mid-1
else:
    print("Element not found")
