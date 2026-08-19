# Implement the idea of a valut at Gringotts, keeping on theme wherein there's a bank in the wolrd of Harry Potter, and within this bank, families and individuals have vaults containing all sorts of money in the wizarding world 
# Money system: gelleons, sickles, and knuts --> in descending order respectively

# Implementing first the idea of a vault
class Vault: # meant to represent a bank vault
    # we initialize our attributes with a value of 0, since they cannot go any lower (for now), taking into account this is a savings vault
    def __init__(self, galleons=0, sickles=0, knuts=0): # initialize our vault with some number of galleons, sickles, and knuts
        # for now, we just trust that these values were passed-in ad we are going to immediately assign them to these instance variables
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        # now, let's print out what is in someone's vault
    
    def __str__(self): # if the obj is called by itself with no attribute, the method __str__(self) is triggered, returning some implementation
        return f"{self.galleons} Galleons, {self.sickles} sickles, and {self.knuts} knuts"

    def __add__(self, other): # we better return a value from this add special method (usually returning the class's constructor with the special method's functionality(ies) as the constructor's arguments, so that initializing an obj assigned to an operator overloading expression)
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        # return the constructor for the class Vault 'Vault()' which is going to initialize the obj assigned to our overloading operator expression which triggers the __add__(self, other) special method, so that using for the constructor's arguments, the body functionality of this special method, therefore initializing/creating the object
        return Vault(galleons, sickles, knuts)

potter = Vault(100, 50, 24)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

# suppose that you want to combine the contents of two vaults, how would you do this in code?
# wouldn't it be nice if we could simply do 'total = potter + weasley' --> overloading the '+' operator to allow us to add two Vaults obj together on the left and the right
total = potter + weasley # triggering the __add__(self, other) special method --> trying to 'sum' out objects --> operator overloading for '+'
# When we overload an operator like '+' what's going to happen automatically as soon as Python sees (obj + obj), it is going to call our __add__(self, other) special method, which will take 'potter' as 'self' (left to '+') and 'other' as 'weasley' (right to '+')
print(total)