class Students: 
    def __init__(self, name, house): 
        self.house = house # triggerring Setter method for attribute 'house'
        self.name = name # triggering Getter method for attribute 'name'

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter for 'house':
    @property 
    def house(self):
        return self._house # refereing to the actual obj's attribute rather than to the Setter method
     # instance variable is now called '_house'

    # Setter for 'house':
    @house.setter
    def house(self, house): 
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house # attribute 'house' updated successfully  
        # instance variable is now called '_house'

    # Getter for 'name':
    @property
    def name(self):
        return self._name
    # instance variable is now called '_name'

    # Setter for 'name':
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name # attribute 'name' updated successfully
        # instance variable is now called '_name'



def main():
    student = get_student()
    # student.house = "Number Four, Privet Drive" # data not supported when calling the 'house' Setter --> ValueError raised

    # student._house = "Number Four, Privet Drive" ## The underscore '_' is meant to signify a convention that this is meant to be "private", but it really just means 'please do not touch this', sometimes programmer even trying to do two underscore as the convention to emphasize on the 'do not touch'
    # the instance variable is '_house'
    # the property is called '.house' no underscore
    # the underline attribute '_' implemented as an instance variable is still called '_house'
    # So yeah, in conclusion, fo not touch/call/update/work with the instance variable from your class' obj attributes 


    print(student) # '__str__(self):' method is called
    print(student.house) # Getter is called --> retuns the property attribute 'obj.attribute'
    print(student.name)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Students(name, house) # the Constructor invokes automatically the 'Students' class method __init__()
   

if __name__ == "__main__":
    main()