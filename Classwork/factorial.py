#taking input from user
num=int(input("Enter any number:"))
fact=1

#checking if number is negative
if num<0:
    print("Factorial not possible for negative number")

#if number is 0, factorial will be 1
elif num==0:
    print("Factorial: 1")
else:
    # loop to calculate the factorial
    for i in range(1,num+1):
        fact*=i
    #printing the factorial
    print("Factorial:",fact)