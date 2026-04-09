# taking numbers from user as input
a=int(input("Enter first Number:"))
b=int(input("Enter second Number:"))
c=int(input("Enter third Number:"))

# checking which number is greatest of three
if a >= b and a >= c:
    print(a)
elif b >= c:
    print(b)
else:
    print(c)