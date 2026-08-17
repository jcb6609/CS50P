class Students: 
    # --> Classes encorage you to encapsulate inside of a class all functionality(ies) related to that class
    def __init__(self, name, house):
        # use error raisers inisde if conditions to control the attributes data/content 
        if not name: # if name is blank 'if not name:' or 'name == "":'
            raise ValueError("Missing name")


        self.name = name
        self.house = house 


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    try: # try creating the object inside the 'try' block
         return Students(name, house) # just returning the constructor method, which initializes an obj and its attributes (not assigning a name to the obj, just returning it)
    except ValueError: # if an error 'ValueError' is raised, then handle it inside the except block (with custom error 'Value' in this case)
        ...
   



if __name__ == "__main__":
    main()