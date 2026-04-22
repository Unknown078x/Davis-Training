# Question: a file with name student.txt contains records in the format name,marks,city , extract and set only the students data whose marks is greater than 75 into the new file


def filter_students():
    try:
        with open("Classwork/Improved File Handling/student.txt", "r") as file, \
             open("Classwork/Improved File Handling/output.txt", "w") as new_file:

            for line in file:
                data = line.strip().split(",")

                if len(data) != 3:
                    continue  # skip invalid lines

                name = data[0]
                marks = int(data[1])
                city = data[2]

                if marks > 75:
                    new_file.write(f"{name},{marks},{city}\n")

        print("Done")

    except FileNotFoundError:
        print("Error: File not found")

    except ValueError:
        print("Error: Invalid data format in file")


filter_students()