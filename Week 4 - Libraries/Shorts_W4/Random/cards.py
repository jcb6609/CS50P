# Random: Module you can use to add an element of randomness or chance to your programs
import random

cards = ["jack", "queen", "king"]

def main():
    # random.seed(0) --> excellent for debugging programs related to randomness
    print(random.choice(cards)) # choice() function takes as input some list and returns some random element from that list
    print(random.choices(cards, k=2)) # choices() function let you choose not just one item from a list but multiple if you want to, the second argument is one called k, which stands for the number of items we want to randomly choose from this list --> (sampling with replacement)
    print(random.sample(cards, k=2)) # sample() function --> (sampling without replacement)

    print(random.choices(cards, weights=[75, 20, 5], k=2)) # we can use another argument for choices() called weights --> takes as input a list of values (numbers) the same length as the list we are selecting elements from ('cards'), then we can specify what are the weigth/probability percentages for each of our 'card' contents we want to get back

main()