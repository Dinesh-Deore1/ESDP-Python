#check type of triagle
side1,side2,side3 = map(int,input("Enter all three sides: ").split())
if side1 == side2 == side2:
    print("Equilateral triagle")
elif side1==side2 or side2==side3 or side3==side1:
    print("Isoscales triangle")
else:
    print("scalene")
