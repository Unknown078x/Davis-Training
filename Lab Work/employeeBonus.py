# Function to calculate bonus based on salary and experience
def calculate_bonus(salary, experience):
    
    if experience >= 10:
        bonus = 0.20 * salary
    elif experience >= 5:
        bonus = 0.10 * salary
    else:
        bonus = 0.05 * salary
    
    return bonus


# getting the number of employees
n = int(input("Enter number of employees: "))

# loop to iterate thorugh multiple employees
for i in range(1, n + 1):
    print(f"\nEmployee {i}:")
    
    salary = float(input("Enter salary: "))
    experience = int(input("Enter years of experience: "))
    
    # Calculate bonus by calling the function
    bonus = calculate_bonus(salary, experience)
    
    # Display result
    print(f"Bonus: {bonus}")
    print(f"Total Salary after bonus: {salary + bonus}")