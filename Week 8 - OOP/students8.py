class Students: 
    def __init__(self, name, house): # to make an optional var/attribute we could do e.g. 'house=None'
        if not name: # if name is blank 'if not name:' or 'name == "":'
            raise ValueError("Missing name") # error raised by the programmer
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house") # error raised by the programmer

        self.name = name
        self.house = house 


def main():
    student = get_student() # obj 'student' is assigned to the get_student() function which returns an initialized object thanks to the class' constructor and its own/called instance method to define the objts attributes, which can now be used by the initial obj 'student' from the assignation of the function call get_function() inside main(); we can refer to the obj's attributes by referencing the initial object name inside of main() and using the dot notation: e.g. 'student.name' and 'student.house'
    print(f"{student.name} from {student.house}") # calling the object by itself is gonna simply return where the object from that class is located in memory


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Students(name, house)
   



if __name__ == "__main__":
    main()