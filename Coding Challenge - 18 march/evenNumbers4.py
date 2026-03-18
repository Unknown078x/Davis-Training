# taking input from user 
nth_term=int(input("Enter the Nth term:"))

i=1
while(i<=nth_term):
    if i%2==0:
        print(i,end=" ")
    i+=1