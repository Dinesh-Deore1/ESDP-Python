#check some of digit is greater than 10
num =2563
sum=0
while(num!=0):
    digit = num%10
    sum = sum+digit
    num=num//10
print("sum of digits of given no. is: ",sum)
