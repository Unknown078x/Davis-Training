class EmptyFileError(Exception):
    pass

try:
    with open("data.txt") as f:
        content = f.read()
        
        if not content:
            raise EmptyFileError("File is empty")
        
        print(content)

except FileNotFoundError:
    print("File not found")
except EmptyFileError as e:
    print(e)