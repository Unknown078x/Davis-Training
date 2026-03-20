# Function to check numbers
def check_number(num):
    
    # Positive / Negative / Zero
    if num > 0:
        sign = "Positive"
        
        # Nested if for even/odd
        if num % 2 == 0:
            nature = "Even"
        else:
            nature = "Odd"
    
    elif num < 0:
        sign = "Negative"
        
        # Nested if for even/odd
        if num % 2 == 0:
            nature = "Even"
        else:
            nature = "Odd"
    
    else:
        # Special case for zero
        sign = "Zero"
        nature = "Even"   
    
    return sign, nature


# list of mixed numbers
numbers=[2,-5,0,24,6,7,8,9,9,999,-21,90]

# Loop to process all numbers
for num in numbers:
    sign, nature = check_number(num)
    print(f"{num} : {sign}, {nature}")