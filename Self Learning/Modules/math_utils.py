# math_utils.py
# Custom module for math operations

def is_prime(n):
    """Check if number is prime"""
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def factorial(n):
    """Return factorial"""
    if n < 0:
        raise ValueError("Negative number not allowed")
    
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def fibonacci(n):
    """Return fibonacci list"""
    a, b = 0, 1
    result = []
    
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    
    return result