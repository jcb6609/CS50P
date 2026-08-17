class Students: 
    def __init__(self, name, house): 
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house 

    # by using 'self' as the only method's argument, we are basically passing a reference to the current student object, which means that when we are calling our obj, let's say with the print function, with no dot notation refereing to the obj's attributes, then the method __str__() is triggered, handling the object call instead of printing its address in memory, for example, by returning a string inside of the __str__() method, and therefore, making the print function call with our object get back that alr defined returned message from inside of the __str__() method
    def __str__(self): # always one argument 'self' by convention
        # we can define returns according to the defined attriutes inside of this class for the __init__() method
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    print(student) # printing the object directly, which is handled by the __str__() special method for (and inside of) our obj's class 


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Students(name, house)
   

if __name__ == "__main__":
    main()