#function to check if the number is even or odd
def oddEven(num):
    #checking if the number is divisible by 2 or not
    if num%2==0:
        return True
    else:
        return False

#taking number from the user
num=int(input("Enter a number:"))
#checking the number is even or odd by calling the function
if (oddEven(num)):
    print(num," is Even")
else:
    print(num," is odd")
