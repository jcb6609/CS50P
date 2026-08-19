# We expect 'Students' related data-implementation to be encapsulated, so that we do not need of extra functions to call/initialize objs and their attributes --> avoid implementing get_student() a function outside of the class that breaks with our encapsulation idea
# In this way, everything related to 'Students' now is in our 'Students' class; the only other thing in this file is main() and it's conditional (that avoids executing main when we are making a module or package or the like)
class Students: 
    def __init__(self, name, house): 
        self.house = house
        self.name = name

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Encapsulation practice: Let's just get() a 'Student' via a class method that by definition does not require us to define a 'Students' obj first  
    # let's define a method 'get(cls):' (class method)
    @classmethod # --> means that we can call this method (class method) without instantiating a 'Students' obj first
    def get(cls): # our defined class method get(cls) uses the class construcotr behind the scenes by calling 'cls(...)'!!!
        # we are gonna move the functionality from get_student() into the 'Students' class (defining our obj's attributes and then returning the Constructor with our attributes as its arguments)
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house) # 'cls' here is the convention to refer to our obj's initializator class 'Students', recall that back when using get_student(), rather tahn defining the name of pur obj when calling the class constructor, here we are directly returning the class's constructor 'Students', which, by encapsulation, we use this other method get() with argument 'cls' to refer to our class --> '@classmethod'


def main():
    student = Students.get() # assign the var holder 'student' to hold the implementation of a class method .get() from class 'Students' --> 'student = Students.get()'
    print(student)


if __name__ == "__main__":
    main()