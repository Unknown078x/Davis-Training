# copy the content of one file to another----improved version


src = "Classwork/Improved File Handling/content.txt"
dest = "Classwork/Improved File Handling/copiedContent.txt"

def copy_file(src,dest):
    try:

        with open(src, "r") as file1, open(dest, "w") as file2:
            for line in file1:
                file2.write(line)

        print("File copied successfully.")

    except FileNotFoundError:
        print("Error: Source file does not exist.")

    except IOError:
        print("Error: Problem while handling the file.")


copy_file(src,dest)