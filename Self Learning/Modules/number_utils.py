# Number utility module

def is_prime(n):
    """Check prime"""
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def factorial(n):
    """Factorial"""
    if n < 0:
        raise ValueError("Negative not allowed")
    
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def gcd(a, b):
    """Greatest Common Divisor"""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Least Common Multiple"""
    return (a * b) // gcd(a, b)


def sum_digits(n):
    """Sum of digits"""
    return sum(int(d) for d in str(n))


def is_armstrong(n):
    """Check Armstrong"""
    digits = len(str(n))
    return sum(int(d)**digits for d in str(n)) == n


def is_perfect(n):
    """Check perfect number"""
    return sum(i for i in range(1, n) if n % i == 0) == n