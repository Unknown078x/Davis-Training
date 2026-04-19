# Using list_utils module

import list_utils

lst = [1, 5, 3, 9, 7, 5, 3]

print("Original List:", lst)

# Multiple functions usage
print("Max:", list_utils.find_max(lst))
print("Min:", list_utils.find_min(lst))
print("No duplicates:", list_utils.remove_duplicates(lst))
print("Second largest:", list_utils.second_largest(lst))
print("Sum:", list_utils.sum_list(lst))
print("Even numbers:", list_utils.even_numbers(lst))
print("Sorted:", list_utils.sort_list(lst))