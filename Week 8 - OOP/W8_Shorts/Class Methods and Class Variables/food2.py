
class Food:

    # A class variable is some variable that is shared accross all instances
    base_hearts = 0
    # how do we access this (standard) class variable inside of a class method? Use 'cls', then dot '.' notation, and then the name of the actual class variable --> e.g. 'cls.base_hearts'

    def __init__(self, ingredients):

        self.ingredients = ingredients 
        self.hearts = Food.calculate_hearts(ingredients)

    # Often, a class method is useful if we try to access or change something about the class within it, let's try to do it while introducing the idea of a class variable
    @classmethod
    def calculate_hearts(cls, ingredients): 
        # hearts = 0 ## notice here that in our method, we are starting with a standard/base number of hearts equal to 1, but, in fact, if we want this base number of hearts to be something we could change accross all instances of our class, then it might be a good candidate to be a class variable.
        hearts = cls.base_hearts # 'hearts' is assigned to the class variable 'base_hearts', access through the 'cls.' notation 
        for i in ingredients: 
            if "Hearty" in i:
                hearts += 2
            else:
                hearts += 1 
        return hearts


def main():
    mushroom_skewer = Food(ingredients=["Mushroom", "Hearty Mushroom"])
    print(f"this skewart heals {mushroom_skewer.hearts} hearts!")



main()