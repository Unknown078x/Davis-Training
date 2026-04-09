# function to check if a number is prime or not
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True

print("Prime" if is_prime(7) else "Not Prime")