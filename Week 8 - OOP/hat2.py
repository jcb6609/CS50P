# Let's improve the design of our code so that we do not have to count with the possibility of instantiating different objects for the same class again and again, let's say that we are only suppose to have a 'singleton' --> a single object
# here is where '@classmethod' is applied

import random

# In addition to class methods, there are also class variables, which exist within the class itself and there is just one copy of that variable for all of the objects there are (They all share the same variable, in this case a variable 'houses' containing a list)
class Hat:
    # if we are not gonna initialize multiple objects (let's say we only have/want a singleton) then we do not need the __init__() method, since it's purpose is basically initializing specific objects from our class/blueprint, then we avoid using __init__() since, first, we will be working with a singleton, and that singleton has no specific attributes
    houses = ["Gryffidnor", "Hufflepuff", "Ravenclaw", "Slytherin"] 
    # What we have done here is defining inside of our hat class, in a class variable 'houses'; and because it is inside of our hat class, we can use that list in any of our methods (in this case only for sort() since the only method defined)
    # this class variable (as any other class variable) exist within the class itself and ther is just one copy of that variable for all of the objects thereof, they all share the same variable

 # We use the @classmethod decorator in Python to define a method that belongs to the class itself rather than a specific object instance
    @classmethod # --> defines a class method
    def sort(cls, name): # therefore, the first argument we pass is not an obj convention 'self' but rather a class convention 'cls' (reference to the class itself convention wich basically means 'class')
        # 'house' is just a variable used to store the choice function from the 'random' library, which takes as argument the class variable 'cls.houses' (with 'cls' and '@classmethod' specifying that we are working inside of a class method sort(cls, ...))
        house = random.choice(cls.houses) # 'cls.houses' means we want to return/use the variable called 'houses' (a class variable) that is associated with this current class 'Hat' (wherein our sort(cls, ...) method is defined)
        print(name, "is in", house) # printin, not returning (not reusable for main())


def main():
    # hat = Hat() # now with the previous class body implementation, we do not need to instantiate any class object(s) as in this line
    Hat.sort("Harry") # Now we only passed a capitalized name of the class 'Hat' as our reference for calling up the .sort() method, which is defined inside of our class using a class variable working for the sort() method which is a class method (defined by the '@classmethod' decorator)
    # so now we are basically, not botherin in instantiating an object of type Hat (e.g. hat = Hat()), but rather accessing a class method sort(cls, ...) inside of the 'Hat' class that you know what, is just gonna work

if __name__ == "__main__":
    main()