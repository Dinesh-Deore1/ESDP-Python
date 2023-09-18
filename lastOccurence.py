ls = list(map(int,input("Enter sorted list: ").split()))
print("list = "+str(ls))
num = int(input("Enter element you want to search: "))
s=0
e=len(ls)-1
while s<=e:
    mid = (s+e)//2
    if ls[mid]==num:
        pos = mid
        s=mid+1
    elif ls[mid]<num:
        s = mid+1
    else:
        e=mid-1
else:
    print("Element not found")
print("last occurence: "+str(pos))
