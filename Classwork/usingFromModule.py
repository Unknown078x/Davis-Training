from numericCalculations import *

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

#Adding two numbers by calling the function from numericCalculations module
print(f"sum of {a} and {b} is: ",addTwoNumbers(a,b))

#Subtracting two numbers by calling the function from numericCalculations module
print(f"Difference of {a} and {b} is: ",subtractTwoNumbers(a,b))

#Multiplying two numbers by calling the function from numericCalculations module
print(f"Multiplication of {a} and {b} is: ",multiplyTwoNumbers(a,b))

#Dividing two numbers by calling the function from numericCalculations module
print(f"Division of {a} and{b} is: ",divideTwoNumbers(a,b))

#Modulus of two numbers by calling the function from numericCalculations module
print(f"Modulus of {a} and {b} is: ",modulusTwoNumbers(a,b))