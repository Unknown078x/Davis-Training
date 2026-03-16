#taking input from user
num=int(input("Enter a number:"))
#converting negative value to positive
num=abs(num)

#initializing the greatest digit as 0
greatestDigit=0


while num>0:
    #extracting the last digit from the given number
    digit=num%10
    
    if digit>greatestDigit:
        greatestDigit=digit

    num=num/10
#printing the greatest digit
print("Greatest digit:",greatestDigit)

