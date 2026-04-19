# Question: a file with name student.txt contains records in the format name,marks,city , extract and set only the students data whose marks is greater than 75 into the new file

# Algorithm:
# Step-1: open the student file in read mode
# Step-2: open the output file in write mode
# Step-3: read the student file line by line
# Step-4: remove the extra spaces from the line and convert the line into a list by seperation of comma
# Step-5: now store all the three values into variables
# Step-6: now check if the marks are greater than 75, if yes then write the whole line into the new file
# Step-7: print done after completion of task

# LOGIC:

# Opening the student file
with open("Classwork/student.txt", "r") as file:
    # Opening new file to store results
    with open("Classwork/output.txt", "w") as new_file:
        
        for line in file:
            # strip will remove the extra spaces from front and last of line and split will convert first line string into list
            data = line.strip().split(",")

            # storing the name 
            name = data[0]
            # storing the marks and also convert them into integer type
            marks = int(data[1])
            # storing the city
            city = data[2]

            # checking if the marks are above 75, if yes then write the whole line into the new file
            if marks > 75:
                new_file.write(line)

print("Done")