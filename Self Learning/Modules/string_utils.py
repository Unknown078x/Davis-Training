# String utility module (advanced)

def reverse_string(s):
    """Reverse string"""
    return s[::-1]


def is_palindrome(s):
    """Check palindrome"""
    return s == s[::-1]


def count_vowels(s):
    """Count vowels"""
    return sum(1 for ch in s.lower() if ch in "aeiou")


def count_consonants(s):
    """Count consonants"""
    return sum(1 for ch in s.lower() if ch.isalpha() and ch not in "aeiou")


def remove_spaces(s):
    """Remove spaces"""
    return s.replace(" ", "")


def capitalize_words(s):
    """Capitalize each word"""
    return s.title()


def frequency(s):
    """Character frequency"""
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq