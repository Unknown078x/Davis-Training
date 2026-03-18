# taking input from user 
nth_term=int(input("Enter the Nth term:"))

#loop to iterate until the Nth term
for i in range(2,nth_term+1,2):
    print(i,end=" ")