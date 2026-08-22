class Food:

    base_hearts = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients 
        self.hearts = Food.calculate_hearts(ingredients)

    @classmethod
    def calculate_hearts(cls, ingredients): 
        hearts = cls.base_hearts
        for i in ingredients: 
            if "Hearty" in i:
                hearts += 2
            else:
                hearts += 1 
        return hearts

    # class method to cover the scenario of finding the food obj instead of cooking it with some 'ingredients' (without passing an 'ingredients' list to our obj when constructing it)
    @classmethod
    # this function should return an instance/obj of our class
    def from_nothing(cls, hearts): # in this case, we can simply specify (instead of calculating our 'hearts') the number of 'hearts' we want this food to have, therefore no worrying about the 'ingredients'
        # here, cls() (with 'cls' being the class itself) is working as a method class constructor, which calls to our __init__(self, ...) method to initialize the arguments of this instance/obj with no 'ingredients' (which means passing an empty list 'ingredients=[]' as the argument of the constructor call for this special method as in: 'cls(ingredients=[])'), storing this implementation into a 'food' var
        food = cls(ingredients=[]) # the 'food' var is assigned to a new instance of our food class (but with the 'cls' keyword) containging an empty ingredients list as argument --> 'food = cls(ingredients=[])', 
        # at the same time, we want to overwrite that instance variable 'hearts' to be whatever the programmer gave as input to this class method from_nothing()
        food.hearts = hearts # we initialize here the atribute 'hearts' for our new obj 'food' constructed inside this from_nothing() class method
        return food
# so previously, in this method class from_nothing(self, hearts) we have now created a new instance of our class (instance obj Food that is received instead of cooked)

def main():
    mushroom_skewer = Food(ingredients=["Mushroom", "Hearty Mushroom"])
    print(f"this skewart we cooked heals {mushroom_skewer.hearts} hearts!")

    # Another good candidate for a class method, is to give the user some new way of making an insatnce of our class
    # Maybe we want to allow the user to simply find some food, they didn't make it from ingrdients they imply find it elsewhere
    # What we can provide to the programmer, in this case, is to try another way to make an instance/obj of this class without the necessity of providing such 'ingredients' list as an argument for/when calling the class's constructor 
    # the other way to make an instance/obj for this scenario is making a new class method for it
    big_mushroom = Food.from_nothing(hearts=4) # this object is received, not cooked, it has to be defined, with our imlementation, not by using a constructor but by calling a class method from_nothing() inside of our 'Food' class (being 'hearts=4' as the argument we are gonna pass to this for_nothing() class method, representing the number of hearts get when buying this object instead of cooking it) --> e.g. 'object_bought = Food.from_nothing(hearts=5)'
    print(f"this big m we bought heals {big_mushroom.hearts} hearts")


"""
This code right here shows us more about class methods and class variables.

Class methods are good for functionality, we ought to be shared across all instances/objs of of our class
They are good for giving a programmer other ways to make instances of our class

And, class variables, are good at embedding information about the class itself and accessing that through the name of the class, not tied to any particular instance/obj (of our class)
"""


main()