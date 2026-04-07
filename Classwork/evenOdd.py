# function to calculate if a number is odd or even
def checkOddEven(num):
    if num%2==0: return True
    else: return False

# taking number from user:
num=int(input("Enter any number:"))

# calling the function to calculate if the number is even or odd
if checkOddEven:
    print(num," is Even number")
else:
    print(num," is Odd number")