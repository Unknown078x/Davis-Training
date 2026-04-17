age=int(input("Enter your age:"))

try:
    if age<18:
        raise Exception("Not Eligible (Age must be 18+)")
    else:
        print("Eligible for voting")
except Exception as e:
    print("Error:",e)
    
