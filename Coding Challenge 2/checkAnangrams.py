# taking first input string from user
s1 = input("Enter first string: ")
# taking secpnd input string from user
s2 = input("Enter second string: ")

# sort both strings and compare
if sorted(s1) == sorted(s2):
    print(True)
else:
    print(False)