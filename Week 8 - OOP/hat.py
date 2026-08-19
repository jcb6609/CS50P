import random

# Let's implement a sorting hat such that when we pass to the sorting hat the name of the student, like "Harry", this sorting hat, implemented in code, will tell use what house that student should be in
class Hat:
    # Strategy, define class, implement code, then come back to implement the class's code (use '...')
    def __init__(self):
        # create a 'houses' instance variable 'self.houses' that is assigned to a list of the HP houses
        self.houses = ["Gryffidnor", "Hufflepuff", "Ravenclaw", "Slytherin"] 
        # we might want to use multiple times this list of houses, defined as one of our obj instance variable, so that we simply keep it's info in the object itself by simply storing such list in the obj's ('hat') instance variable 'houses' nside of the __init__() method --> 'self.houses = [...]'

    # By default, any standard function we create inside of a class becomes an instance method
    # Python automatically passes the object instance 'self' as the first argument when we call that method, 
    def sort(self, name): # recall 'self' is set by default as our object instance therefore, when using .sort() and passing into it a str, we can define as a second argument in our instance method an argument to name that passing value, in this case 'name' (second argument after 'self' for our sort() instance method) 
        house = random.choice(self.houses) # var 'house' is assigned to the choice() function which returns a random element from its argument (a list for instance), here that argument being the created instance variable from the __init__() method, which stores a list of HP houses
        print(name, "is in", house)


def main():
    hat = Hat() # constructor 'Hat()' initializing obj 'hat' ## Recall that the constructor calls by defualt the __new__ and __init__ methods; in this code, we defined the __init__() method to simply define a new instance variable that holds a list with str elements
    hat.sort("Harry") # we want to sort, so we can implement a sort() method inside class, that works for our 'referenced' obj; therefore, when using the method .sort() we will be calling the class's function sort()
    # harry is oassed as the second argument ofr the instance method inside of our class def for the referenced obj 'hat', which uses the .sort() method designed by us inside of the obj's class


if __name__ == "__main__":
    main()