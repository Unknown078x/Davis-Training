# question: area and perimeter of circle and taking input from user

# taking input from user
radius=float(input("Enter the Radius:"))
area=0
perimeter=0
if radius>0:
    # calculating area
    area=3.14*radius*radius
    # calculating perimeter
    perimeter=2*3.14*radius
    # printing area and perimeter
    print("Area of Circle:",area)
    print("Perimeter of Circle:",perimeter)
else:
    print("Radius cannot be negative")
