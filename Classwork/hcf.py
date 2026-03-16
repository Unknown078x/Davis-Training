#taking the first and second number from the user
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

#checking if the second number is 0
if num2==0:
  print("HCF is:",num1)
else:
    while num2!=0:
        rem=num1%num2
        num1=num2
        num2=rem
    #printing the hcf
    print(f"The HCF is: {num1}")
