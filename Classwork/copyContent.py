try:
    # opening the file in read mode
    with open("Classwork/hcf.py", "r") as file:
        # reading the content of file
        content = file.read()

    # creating new file and writing data into it
    with open("Classwork/destination.txt", "w") as file:
        # writing the data into the file
        file.write(content)

    print("File copied successfully.")

except FileNotFoundError:
    print("Error: file does not exist.")

except IOError:
    print("Error: Problem while opening or reading the file.")