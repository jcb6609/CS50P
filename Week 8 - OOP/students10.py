class Students: 
    def __init__(self, name, house, patronus): 
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house 
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    # let's implement our own function/method 
    def charm(self): # the convention is having at least one argument 'self', so that we have access to our current object (called by the constructor caller)
        match self.patronus:
            case "Stag":
                return "🐴" 
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _: # case of no 'patronus' recognized (among the previous options)
                return "🌠"


def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm()) # we are using our object as a reference for getting back the return functionality of the .charm() method (which is inside the obj's class) --> 'student.charm()'

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Students(name, house, patronus)

   

if __name__ == "__main__":
    main()