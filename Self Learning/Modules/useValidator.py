# Using validator module

import validator

email = "test@gmail.com"
password = "Abc12345"
age = 21

print("Email:", email)
print("Valid Email:", validator.is_valid_email(email))

print("\nPassword:", password)
print("Strong Password:", validator.is_strong_password(password))

print("\nAge:", age)
print("Valid Age:", validator.is_valid_age(age))

# Numeric check
value = "12345"
print("\nIs Numeric:", validator.is_numeric(value))