#function to calculate simple interest
def calculateSI(p,r,t):
    return (p*r*t)/100

# taking values from the user:
principle=float(input("Enter the principle amount:"))
rate=float(input("Enter the rate of interest:"))
time=float(input("Enter the time(in years):"))

# calling the function to calculate the simple interest
simpleInterest=calculateSI(principle,rate,time)

# printing the result
print(f"Simple Interest:Rs.{simpleInterest}")