# problem statement
# 6. Voting System with Duplicate Check
# Input:
# • List of votes
# Tasks:
# • Count votes
# • Prevent duplicate voting using set
# • Declare winner


# logic:
# create an empty set and add every user into it, it automatically remove duplicate users
# count the votes of every candidate
# find the winner from the countvotes using the max method
# count the max votes using the winner
# print the data 


# votes data
votes = [
    ("user1", "A"),
    ("user7", "C"),
    ("user2", "B"),
    ("user15", "A"),
    ("user3", "D"),
    ("user9", "B"),
    ("user4", "A"),
    ("user2", "C"),  
    ("user10", "D"),
    ("user5", "A"),
    ("user11", "B"),
    ("user6", "C"),
    ("user12", "A"),
    ("user7", "D"),  
    ("user13", "B"),
    ("user8", "C"),
    ("user14", "A"),
    ("user3", "B"),   
    ("user16", "D"),
    ("user17", "A"),
    ("user18", "C"),
    ("user19", "B"),
    ("user20", "A"),
    ("user9", "C"), 
    ("user21", "D"),
    ("user22", "B"),
    ("user23", "A"),
    ("user24", "C"),
    ("user25", "A"),
    ("user5", "D"),   
    ("user26", "B"),
    ("user27", "C"),
    ("user28", "A"),
    ("user29", "D"),
    ("user30", "B"),
    ("user31", "A"),
    ("user32", "C"),
    ("user33", "A"),
    ("user34", "D"),
    ("user35", "B"),
    ("user36", "C"),
    ("user37", "A"),
    ("user38", "B"),
    ("user39", "C"),
    ("user40", "D"),
    ("user41", "A"),
    ("user42", "B"),
    ("user43", "C"),
    ("user44", "A"),
    ("user45", "D"),
]


uniqueUsers = set()    
countVotes = {}        

for user, candidate in votes:
    if user not in uniqueUsers:
        uniqueUsers.add(user)

        if candidate in countVotes:
            countVotes[candidate] += 1
        else:
            countVotes[candidate] = 1
    else:
        print("Duplicate vote ignored from:", user)

# Finding winner
winner = max(countVotes, key=countVotes.get)
maxVotes = countVotes[winner]


# Output
print("\nVote count:", countVotes)
print("Winner:", winner, "with", maxVotes, "votes")






# OUTPUT:
# Duplicate vote ignored from: user2
# Duplicate vote ignored from: user7
# Duplicate vote ignored from: user3
# Duplicate vote ignored from: user9
# Duplicate vote ignored from: user5

# Vote count: {'A': 16, 'C': 10, 'B': 11, 'D': 8}
# Winner: A with 16 votes