# Problem: Custom Module - Math Utility Package
# Create a module with:
# • Prime check
# • Fibonacci generator
# • Factorial

# Logic:
# 1. Prime:
#    - number > 1
#    - check divisibility from 2 to n-1
# 2. Fibonacci:
#    - start with 0, 1
#    - generate n terms using loop
# 3. Factorial:
#    - multiply numbers from 1 to n

# Code:

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq


def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result