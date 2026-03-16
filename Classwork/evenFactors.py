#taking input from user
num=int(input("Enter a number:"))
#converting negative number to positive
num=abs(num)

if num==0:
    print("Even Factor: 0")
else:
    for i in range(1,(num//2+1)):
        if num%i==0 and i%2==0:
            print(i,end=", ")

