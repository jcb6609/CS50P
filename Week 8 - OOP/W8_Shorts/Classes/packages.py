# Here we will see why we should create classes and the syntax we can use to do so 

# Here, we have a program called packages whose goal is to track packages we're sending between different users 

class Package:
    # by convention at least one argument 'self' which refers to the instance of the new object we would be creating
    # the other arguments are the attributes that we want our obj to have
    def __init__(self, id, sender, recipient, weight): # dunder: double undercase '__'
        # initializing the attributes for our new obj or objs
        self.id = id
        self.sender = sender
        self.recipietn = recipient
        self.weight = weight

def main():
    # lists are way too flexible
    # in this list, we are using te class's constructor to construct our obj, which are elements of the list 'packages', and also can take as arguments the attributes' data we want to pass to construct an object with those passed attributes, later initialized inside of the __init__(self, ...) method
    packages = [
        Package(id=1, sender="Alize", recipient="Bob", weight="10kg"),
        Package(id=2, sender="Bob", recipient="Charlie", weight="5kg")
    ]

    """
    for i in packages:
        print(i) # printing like this, simply will return the actual addres for our created obj(s) in our list, we have to call our objs in a different way
    """
    # so now, how to print our objs, perhaps with a __str__(self) special method? --> check next code


main()


# class --> template I can use to create various objects in our code
# we can represent each of our packages as objects
# classes allow use to encapsulate our info in a single place