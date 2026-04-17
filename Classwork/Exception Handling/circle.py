# question: program to find the area and perimeter of circle using exception handling
import math

try:
    radius = float(input("Enter radius: "))

    if radius < 0:
        raise ValueError("Radius cannot be negative")

    area = math.pi * radius * radius
    perimeter = 2 * math.pi * radius

    print("Area of Circle:", area)
    print("Perimeter of Circle:", perimeter)

except ValueError as e:
    print("Invalid input:", e)

except Exception as e:
    print("Something went wrong:", e)