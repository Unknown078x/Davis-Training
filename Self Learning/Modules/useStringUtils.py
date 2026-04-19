# Using string_utils module

import string_utils

text = "Hello World"

print("Original:", text)

# Using multiple functions
print("Reversed:", string_utils.reverse_string(text))
print("Vowels:", string_utils.count_vowels(text))
print("Consonants:", string_utils.count_consonants(text))
print("No spaces:", string_utils.remove_spaces(text))
print("Capitalized:", string_utils.capitalize_words(text))
print("Frequency:", string_utils.frequency(text))

# Palindrome check
word = "madam"
print("Is Palindrome:", string_utils.is_palindrome(word))