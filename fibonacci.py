num = int(input("Enter the number upto you want to print series: "))
a=0
b=1
for x in range(1,num+1):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
