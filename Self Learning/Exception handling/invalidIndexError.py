class InvalidIndexError(Exception):
    pass

lst = [10, 20, 30]

try:
    idx = int(input("Enter index: "))
    
    if idx < 0 or idx >= len(lst):
        raise InvalidIndexError("Index out of range")
    
    print(lst[idx])

except ValueError:
    print("Enter valid number")
except InvalidIndexError as e:
    print(e)