# we can realize that both of our classes Student and Professor are both just simply wizards, so maybe what we should really define is a third class for instance called Wizard that has any of the common attributes for Students and Professors alike

# Single inheritance example code:

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name


class Student(Wizard): # Student' class inherits (all of the implementations and characteristics) from 'Wizard' class
    def __init__(self, name, house):
        # we can now remove impementation for the 'name' attribute and the if block checker since now this implementation is in the 'Wizard' class
        
        # since we have linked classes by inheritance, now we need to access their functionalities by calling 'super()'
        super().__init__(name) # calling the super class (parent class) 'Wizard' of this class (child class) 'Student'; and then, specifying with the dot notation '.' the method (of the parent class) we want to access, in this case __init__(), and finally, specifying as an argument of the inteded method to access, the variable/attribute initialized (its final name) that we want to work with in this child class 'Student' --> 'super().__init__(name)' --> Note: This value/attribute also needs to be specified as an attribute for our own child class __init__() method!!!
        self.house = house

class Professor(Wizard): 
    def __init__(self, name, subject):
        # we can now remove impementation for the 'name' attribute and the if block checker since now this implementation is in the 'Wizard' class
        
        super().__init__(name)
        self.subject = subject


wizard = Wizard("Albus") # recall that our <<standard>> 'Wizard' parent class defines inside for its __init__() method, one required argument/attribute (not counting 'self' ofc)
print(f"{wizard.name} is the headmaster wizard of Howarts")


student = Student("Harry", "Gryffindor") # recall that our <<standard>> 'Student' child class defines inside for its __init__() method, two required arguments/attributes (not counting 'self' ofc)
print(f"{student.name} is a student at Howarts from the {student.house} house")

professor = Professor("Snape", "Defense Magic") # recall that our <<standard>> 'Professor' child class defines inside for its __init__() method, two required arguments/attributes (not counting 'self' ofc)
print(f"{professor.name} is a professor at Howarts that specializes on {professor.subject}")

