# Problem: Use custom math module
# Import functions and test them

# Logic:
# 1. Import module
# 2. Call each function with sample input
# 3. Print results

# Code:

import customModule

num = 7

print("Is Prime:", customModule.is_prime(num))
print("Fibonacci (5 terms):", customModule.fibonacci(5))
print("Factorial:", customModule.factorial(num))


# Expected Output:

# Is Prime: True
# Fibonacci (5 terms): [0, 1, 1, 2, 3]
# Factorial: 5040