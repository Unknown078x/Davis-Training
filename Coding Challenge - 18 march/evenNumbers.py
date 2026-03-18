# taking input from user 
nth_term=int(input("Enter the Nth term:"))

#loop to iterate until the Nth term
for i in range(1,nth_term+1):
    if i%2==0:
        print(i,end=" ")