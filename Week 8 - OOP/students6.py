# When we define a class in an object-oriented programming language, we are creating a user-defined data type
class Students: # create a class named 'Students'
    # instance method '__init__(self, var1, var2, ..., varn)' --> It initializes the content for the class object's attributes
    # the instance method allows us to implement the initialization of an object (an its attributes)
    def __init__(self, name, house): # we also want this method to take as arguments (after the 'self' argument) the object attributes we want to initialize
        self.name = name # installing into the empty object the 'name' attribute
        self.house = house # installing into the empty object the 'name' attribute
    # Note: Methods are basically functions inside a class block


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    # now, instead of creating student object (from our 'Students' class), and then manually putting the 'name' and 'house' attributes inside of it, let's do this:
    # assign/create the 'student_1' obj by calling the 'Students()' special method (whose name is identical to the class's name), and pass in the argument vars 'name' and 'house'
    # Note: our constructor Students() is basically going to call the instance method '__init__(self, ...)' which initializes the attributes (passed in the Students() constructor arguments) of our object; this instance method is defined inside of our 'Students' class
    student_1 = Students(name, house) # --> standardizing how we are passing data into our 'Students' class, giving us the opportunity to error check those user inputs by, again, passing our vars to the 'Students' class constructor (special method) 'Students()', while also storing this class implementation, thanks to the constructor, into our obj creation 'student_1'
    # a constructor basically construct an (assigned) obj
    # the previous line syntax (obj creation and constructor call) allows us to have more control over the correctness of our data
    return student_1


if __name__ == "__main__":
    main()