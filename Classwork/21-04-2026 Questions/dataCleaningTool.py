# Problem: Data Cleaning Tool
# Input file contains messy data:
# • Remove null values
# • Fix formatting issues
# • Convert types safely using exception handling

# Logic:
# 1. Read file line by line.
# 2. Skip header.
# 3. Split each row by comma.
# 4. Remove rows with empty/null values.
# 5. Clean formatting:
#    - strip spaces
#    - standardize text (capitalize names)
# 6. Convert numeric fields safely using try-except.
# 7. Store cleaned data in list.
# 8. Write cleaned data to a new file.

# Code:

input_file = "Classwork/21-04-2026 Questions/dirtyData.txt"
output_file = "Classwork/21-04-2026 Questions/cleanData.txt"

clean_data = []

with open(input_file, "r") as file:
    lines = file.readlines()
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # skip header
        if i == 0:
            clean_data.append(line)
            continue
        
        parts = line.split(",")
        
        # check for null/invalid row
        if len(parts) != 3:
            continue
        
        name, age, salary = parts
        
        # remove null values
        if name == "" or age == "" or salary == "":
            continue
        
        # fix formatting
        name = name.strip().capitalize()
        
        try:
            age = int(age.strip())
            salary = float(salary.strip())
        except:
            continue
        
        clean_data.append(f"{name},{age},{salary}")

# write cleaned data
with open(output_file, "w") as file:
    for row in clean_data:
        file.write(row + "\n")

print("Data cleaned and saved to", output_file)


# Expected Output (based on sample file below):

# clean_data.txt:
# name,age,salary
# Aman,21,25000.0
# Riya,22,30000.0
# Karan,20,20000.0