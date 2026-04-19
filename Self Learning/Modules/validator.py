# Validation module

def is_valid_email(email):
    """Basic email validation"""
    return "@" in email and "." in email


def is_strong_password(pwd):
    """Check strong password"""
    if len(pwd) < 8:
        return False
    
    has_upper = any(ch.isupper() for ch in pwd)
    has_lower = any(ch.islower() for ch in pwd)
    has_digit = any(ch.isdigit() for ch in pwd)
    
    return has_upper and has_lower and has_digit


def is_valid_age(age):
    """Age validation"""
    return 0 <= age <= 120


def is_numeric(s):
    """Check numeric string"""
    return s.isdigit()