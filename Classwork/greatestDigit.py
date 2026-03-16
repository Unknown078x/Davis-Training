num=int(input("Enter a number:"))

greatestDigit=0

while num>0:
    digit=num%10
    if digit>greatestDigit:
        greatestDigit=digit
    num=num/10
print("Greatest digit:",greatestDigit)