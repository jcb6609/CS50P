# class representing food, and tranform it as in a videogame when we as a character, as we eat food composed of various ingredients, we can get some number of hearts
# we want the ingredients to determine the number of hearts that our food obj should heal the player

# 2 case scenarios, more ingredients = more hearts, or
                 # special ingredients = more hearts
# so it seems that we need a way to calculate the number of hearts 
class Food:
    def __init__(self, ingredients):
        # initializing attributes with the instance  of a new obj 'self'
        self.ingredients = ingredients # setting an instance variable called 'ingredients' equal to some list of ingredients we passed as input
        self.hearts = Food.calculate_hearts(ingredients) # instantiating the 'hearts' attribute with no constructor data but rather with a 'Food' class method 'calculate_hearts' that accepts as input/argument our alr initialized 'ingredients' attribute 

    # our heart calculation doesn't depend on any particular instance, so therefore we can use a class method, since it does not depend on any particualr instance but rather to our class
    @classmethod # decorator that tells Python our following method is a class method
    def calculate_hearts(cls, ingredients): # default argument 'cls' (class itself) together with any passed argument, such as 'ingredients' in this case
        hearts = 0
        for i in ingredients: # e.g. ingredients=["M", "G"]; i="M" --> hearts = 0 + 1 = 1; i="G" --> hearts = 1 + 1 = 2
            if "Hearty" in i:
                hearts += 2 # "Hearty" name items give 2 hearts
            else:
                hearts += 1 # any other non-special item gives 1 heart
        return hearts # 'hearts' is returned to where it was called, in this case when initializing our attribute arguments inside __init__(self, ...), assinging 'self.hearts' to this method return (being hearts not defined as an argument in our __init__(self, ...) method since it is not defined when calling a constructor but rather in this class method calculate_hearts())


def main():
    # here, we define a container obj 'mushroom_skewer' which is assinged to our 'Food' class constructor containing as argument a list 'ingredients' with the ingredients (2 str list elements) of such container obj's name; then, this list is passed to our class's __init__(self, ingredients) method as an attribute for our new obj 
    mushroom_skewer = Food(ingredients=["Mushroom", "Hearty Mushroom"])
    # print(mushroom_skewer.ingredients) ## when passing a list for our constructor to be initialized as an attribute, we can print back this list by simply saying obj.attribute, in this case 'mushroom_skewer.ingredients', with mushroom_skewers as the new obj created which was assigned to the class's constructor Food() containing as an argument the 'ingredients' list of such obj, passing such list inside of our special method __init__() to initialize it as a new obj's attribute 'self.ingedients = ingredients'; Finally, if we now print such obj with its attribute, we will get back the whole attribute list passed for the constructor
    print(f"this skewart heals {mushroom_skewer.hearts} hearts!")



main()