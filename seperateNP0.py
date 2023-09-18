ls = list(map(int,input("Enter list elements: ").split()))
n=len(ls)
pos=[0]*n
neg=[0]*n
zero=[0]*n
p,n,z=0,0,0
for x in ls:
    if x==0:
        zero[z]=x
        z=z+1
    elif x>0:
        pos[p]=x
        p=p+1
    else:
        neg[n]=x
        n=n+1
print(pos[:p], neg[:n], zero[:z])
