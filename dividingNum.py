#print all the numbers that completely divides given numbers
num = int(input("Enter the number: "))
for x in range(2,num+1):
    if num%x == 0:
        print(x)
