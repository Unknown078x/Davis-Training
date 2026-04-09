# taking input from user
num = int(input("Enter number: "))

# checking if the number is divisible by both 3 and 5
if num % 3 == 0 and num % 5 == 0:
    print("Yes")
else:
    print("No")