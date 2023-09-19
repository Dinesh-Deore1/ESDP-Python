num = int(input("Enter the number: "))
lastDigit = num%10
while(num!=0):
    firstDigit = num%10
    num = num//10
print(firstDigit+lastDigit)
