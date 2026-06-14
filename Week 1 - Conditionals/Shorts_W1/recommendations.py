# Conditionals - short W1
# Goal: be able to recommend some card games to a user based on their preferences for difficulty and the number of players they want to play with 
def main():
    difficulty = input("Difficult or Casual?: ")
    players = input("Multiplayer or Single-player?: ")

# possible games we could recommend:
    if(difficulty == "Difficult"):
        if (players == "Multiplayer"):
            recommend("Poker") # recall we can use "..." as part of a function's body when we only want to design infrastructure rather than content
        elif(players == "Single-player"):
            recommend("Klondike")
        else:
            print("Enter a valid number of players")

    elif (difficulty == "Casual"):
        if(players == "Multiplayer"):
            recommend("Hearts")
        elif(players == "Single-player"):
            recommend("Clock")
        else:
            print("Enter a valid number of players")
    else:
        print("Enter a valid difficulty")

def recommend(game):
    print("You might like", game)

main()