# When we define a class in an object-oriented programming language, we are creating a user-defined data type
class Students: # create a class named 'Students'
    ...


def main():
    student = get_student() # the 'student' var is assigned to a returned dict by calling the get_student() function
    # getting the content of our class's obj and its attributes
    print(f"{student.name} from {student.house}") # use single quotes for entering a dict key when also printing their values!

# use the class's previously defined implementation inside this function to define an object
def get_student():
    # creating an object 'student_1' instance by using a constructor (a special method used to initialize the state/attributes of an object when it is created from a class):
    student_1 = Students() # obj 'student_1' stores the constructor special method Students() (which has the same name as the 'Students' class previously defined) so then also initializing the state/attributes (from class 'Students') of the assigned object 'student_1'
    # initializing attributes (instance variables) to our 'student_1' obj by using a dot followed by the desired attribute and the desired functionality assignment (in this case user's input) for the object's attribute
    student_1.name = input("Name: ")
    student_1.house = input("House: ")
    # '.name' and '.house' are really just variables (instance variables) inside of an object (in this case 'student_1') whose date type is, in this case, 'Students'

    return student_1

if __name__ == "__main__":
    main()