#function to check if the number is even or odd
def oddEven(num):
    #changing negative number to positive number
    num=abs(num)
    if num%2==0:
        print(num," is an Even Number")
    else:
        print(num," is an Odd Number")

#taking number from the user
num=int(input("Enter a number:"))
#calling the function
oddEven(num)