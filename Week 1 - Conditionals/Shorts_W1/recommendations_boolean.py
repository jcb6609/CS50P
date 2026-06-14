# Boolean Expressions- short W1
def main():
    difficulty = input("Difficult or Casual?: ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid difficulty")
        return # the end of our program, we don't want the user to keep interacting 

    players = input("Multiplayer or Single-player?: ")
    if not (players == "Multiplayer" or players == "Single-player"):
        print("Enter valid number of players")
        return # the end of our program, we don't want the user to keep interacting 

# The above code allows us to request the user for a correct input right after the input is entered

# 4 possible games we could recommend:
    if (difficulty == "Difficult" and players == "Multiplayer"):
        recommend("Poker") # recall we can use "..." as part of a function's body when we only want to design infrastructure rather than content
    elif (difficulty == "Difficult" and players == "Single-player"):
        recommend("Klondike")
    elif (difficulty == "Casual" and players == "Multiplayer"):
        recommend("Hearts")
    else:
        recommend("Clock")

def recommend(game):
    print("You might like", game)

main()