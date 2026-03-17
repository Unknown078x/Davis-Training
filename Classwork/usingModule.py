import numericCalculations as mod

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

#Adding two numbers by calling the function from numericCalculations module
print(f"sum of {a} and {b} is: ",mod.addTwoNumbers(a,b))

#Subtracting two numbers by calling the function from numericCalculations module
print(f"Difference of {a} and {b} is: ",mod.subtractTwoNumbers(a,b))

#Multiplying two numbers by calling the function from numericCalculations module
print(f"Multiplication of {a} and {b} is: ",mod.multiplyTwoNumbers(a,b))

#Dividing two numbers by calling the function from numericCalculations module
print(f"Division of {a} and{b} is: ",mod.divideTwoNumbers(a,b))

#Modulus of two numbers by calling the function from numericCalculations module
print(f"Modulus of {a} and {b} is: ",mod.modulusTwoNumbers(a,b))