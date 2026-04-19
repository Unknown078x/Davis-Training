# Question: copy the content of one file to another using with statement

# opening the file in read mode
with open("Classwork/article.txt", "r") as file:
    # reading the content of file
    content = file.read()

    # creating new file and writing data into it
with open("Classwork/destination.txt", "w") as file:
    # writing the data into the file
    file.write(content)

print("File copied successfully.")