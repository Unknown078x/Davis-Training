num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if num2==0:
  print("HCF is:",num1)
else:
    while num2!=0:
        rem=num1%num2
        num1=num2
        num2=rem
    print(f"The HCF is: {num1}")