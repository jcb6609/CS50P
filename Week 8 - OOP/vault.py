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


potter = Vault(100, 50, 24)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

# suppose that you want to combine the contents of two vaults, how would you do this in code?

total_g = potter.galleons + weasley.galleons
total_s = potter.sickles + weasley.sickles
total_k = potter.knuts + weasley.knuts

total = Vault(total_g, total_s, total_k)
print(total)