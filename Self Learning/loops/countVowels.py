# Count vowels in string

s = input("Enter string: ")
count = 0

for ch in s.lower():
    if ch in "aeiou":
        count += 1

print("Vowels:", count)