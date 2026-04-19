# Count uppercase and lowercase

def count_case(s):
    upper = lower = 0
    
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    
    return upper, lower

print(count_case("HelloWorld"))