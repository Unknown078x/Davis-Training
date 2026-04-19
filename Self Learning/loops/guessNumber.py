# Simple guessing game
secret = 7
tries=0
while True:
    guess = int(input("Guess number: "))
    
    if guess == secret:
        tries+=1
        print("Correct...you guessed the number in ",tries," tries")
        break
    elif guess>secret:
        tries+=1
        print("guess lower number")
    elif guess<secret:
        tries+=1
        print("guess greater number")