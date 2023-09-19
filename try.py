#program to take numbers until 0 is encountered and print sum
sum=0
while(True):
    n = int(input("Enter the number: "))
    if n == 0:
        break
    else:
        sum = sum+n
print("sum is: "+str(sum))
