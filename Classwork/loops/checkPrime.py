# Check whether a number is prime or not
num = int(input("Enter number: "))
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, num):   # check from 2 to num-1
        if num % i == 0:
            is_prime = False
            break   # no need to check further

if is_prime:
    print("Prime")
else:
    print("Not Prime")