# Equilateral, Isosceles, Scalene

a=int(input("Enter first side:"))
b=int(input("Enter second side:"))
c=int(input("Enter third side:"))

if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")