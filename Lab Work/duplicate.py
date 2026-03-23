# list with elements
a=[1,2,3,3,4,5,6,6,7,7,8]
# empty set for duplicates
duplicate=set()
# loop to iterate through the list
for i in a:
    if a.count(i)>1:
        duplicate.add(i)
        

# changing set into list
b=list(duplicate)
# printing the output
print(b)
