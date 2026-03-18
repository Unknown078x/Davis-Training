 #function to calculate the simple interest
def simpleInterest(p,r,t):
    temp = p * r
    temp = temp * t
    si = temp / 100
    return si

# taking the value of principle amount from user
principle=int(input("Enter the Principle Amount:"))
# taking the rate from user
rate=int(input("Enter the Rate(in %):"))
# taking the time from user
time=int(input("Enter the Time(in Years):"))

# Calling the function to calculate the Simple Interest
print(f"Simple interest of principle Amount Rs.{principle} at rate of {rate}% in time {time} years is Rs.{simpleInterest(principle,rate,time)}")