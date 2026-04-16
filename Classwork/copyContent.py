try:
    # opening the file in read mode
    with open("source.txt", "r") as file:
        # reading the content of file
        content = file.read()

    # creating new file and writing data into it
    with open("destination.txt", "w") as file:
        # writing the data into the file
        file.write(content)

    print("File copied successfully.")

except FileNotFoundError:
    print("Error: source.txt file does not exist.")

except IOError:
    print("Error: Problem while opening or reading the file.")