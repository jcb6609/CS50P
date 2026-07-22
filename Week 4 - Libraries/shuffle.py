import random

cards = ["J", "Q", "K"]

random.shuffle(cards) # It does not returns you a value that contains the shuffled cards in this case, but rather it shuffles the list it's given itself

for i in cards:
    print(i)