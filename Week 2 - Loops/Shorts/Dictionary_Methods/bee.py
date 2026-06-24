# Dictionary method --> FUnction you can use to manipulate your dictionary in Python 
# bee.py --> replicate the functionality of the game spelling Bee in the New York Times

WORDS = {
    "PAIR": 4,
    "HAIR": 4,
    "CHAIR": 5,
    "GRAPHIC": 0 # --> Winning word
}

def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")
    print(end='\n')
    points = 0 # We have to initilize the variable first
    winning_points = 0

    while len(WORDS) > 0: # this loop will repeat as long as we still have keys in our dictioanry
        if(len(WORDS) == 1):
            print(f"{len(WORDS)} word left ")
        else:
             print(f"{len(WORDS)} words left ")
        guess = input("Guess a word: ")
        print(end='\n')

        # To-do: check if guess is in our dictionary
        if(guess == "GRAPHIC"): # --> Winning word (if gotten, no more answers are necessary to get)
            winning_points += 1
            WORDS.clear() # .clear() method removes all of the keys of our referenced dictionary
            break
        if guess in WORDS.keys(): # .keys() method --> gives access to the referenced dictionary keys
            points += WORDS[guess]
            print(f"Godd job, You scored {WORDS[guess]} points.")
            print(f"Total points: {points}")
            print(end='\n')
            WORDS.pop(guess) # .pop(...) method with a dictionary key as the method's argument ... we want to drop out of our dictionary, which is refenced to the .pop() method
        else:
            print("Wrong word, try another.")

    print("That's game, you won!")
    print(f"Total points obtained: {points} points")
    print(f"Total winning points obtained: {winning_points} points")

main()