# list of 15 elements
a=[1,2,3,1,2,3,1,2,3,1,2,3,1,2,3]
# taking input from user
num= int(input("Enter a number:"))

# reversing the list to remove element from end only
a.reverse()
for i in a:

    if a.count(num)<1:
        print("Element doesn't exixt in the list")
        break
    elif a.count(num)==1:
        break
    else:
        a.remove(num)
# reversing the list again to get the correct list in same order as beginning
a.reverse()

# printing the list 
print("List = ",a)