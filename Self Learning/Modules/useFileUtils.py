
import file_utils

file_name = "data.txt"

# Write data
print(file_utils.write_file(file_name, "Hello World\nPython is awesome"))

# Append data
print(file_utils.append_file(file_name, "\nNew line added"))

# Read file
print("\nFile Content:")
print(file_utils.read_file(file_name))

# Count lines
print("\nLines:", file_utils.count_lines(file_name))

# Count words
print("Words:", file_utils.count_words(file_name))

# Search word
print("Contains 'Python':", file_utils.search_word(file_name, "Python"))

# Copy file
print(file_utils.copy_file("data.txt", "copy.txt"))