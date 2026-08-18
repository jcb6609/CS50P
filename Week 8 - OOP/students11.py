class Students: 
    def __init__(self, name, house): 
        if not name:
            raise ValueError("Missing name")
        
        """
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")

        """
        # recall that our setter will get call anytime we access '.house' (for a setter for te 'house' attribute)
        self.house = house # --> here, since we are initializing our empty obj with the 'house attribute', if we have a setter, then the setter will also be triggered, which help us to define its validation right inside the Setter method rather than inside of the __init__() method.
        # 'self.attribute' are instance variables 
        self.name = name

    def __str__(self):
        return f"{self.name} from {self.house}"

    # We use decorators '@...' to define our Getters and Setters before their actual definition

    # Getter: function from a class (method) that gets some attributes 
    @property # keyword to define our Getter method
    def house(self):  # when we read a property attribute (e.g. print(obj.attribute)) the Getter is called
        return self._house # we do not want to get back to our Setter method when refering to the 'self/obj.attribute' syntax (which will call the attribute() method again and again), therefore, we use by convention the 'obj._attribute' notation 
    # convention '._' used

    # Setter: function from a class (method) that sets some value
    @house.setter # code to define our Setter method
    def house(self, house): # When we assign or change an obj attribute's data (e.g. obh.attriute = 10) the setter is called 
        # Setters usually have validation logic:
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
    # Both Getter and Setter methods sould have the name of the desired attribute to chnage, 'house()' in this case
        self._house = house # we do not want to get back to our Setter method when refering to the 'self/obj.attribute' syntax (whic will call the attribute() method again and again), therefore, we use by convention the 'obj._attribute' notation 
    # convention '._' used


def main():
    student = get_student()
    # we can update our obj attributes (after their initialization) using the dot notation:
    student.house = "Number Four, Privet Drive" # Setter is called --> overrides the 'house' attribute for our 'student' obj
    # The Setter will check out the previous code update for our obj's attribute, if not valid, then our Setter will simply return an error

    # --> 'student.house' will automatically call the Setter method, since its appearence after the obj's initialization basically means the update/access to the obj's attribute 'house', and therefore triggering the Setter method if defined
    # when trying to modify/update an obj's attribute after the obj's initialization, we can use setters, which will directly call the Setter method (with the same name as the attribute's name e.g. 'house(self, house):') inisde the obj's class 
    # in this way, we can check whether the user can/can't modify that exact attribute, without modifying the original attribute from obj's initialization directly
    print(student) # '__str__(self):' method is called
    print(student.house) # Getter is called --> retuns the property attribute 'obj.attribute'


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Students(name, house) # the Constructor invokes automatically the 'Students' class method __init__()
   

if __name__ == "__main__":
    main()