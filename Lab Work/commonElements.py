# first list
list1=[1,2,3,4]
# second list
list2=[2,4,5,6]
# empty set for duplicates
dup=set()
# loop to iterate through the list
for i in list1:
    for j in list2:
        if i==j:
            dup.add(j)

# chanhing the set into list
duplicate=list(dup)
print(duplicate)