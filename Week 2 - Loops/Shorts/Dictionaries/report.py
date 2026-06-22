# Dictionaries are useful when you want to store similar kinds of information in terms of these key-value pairs
# --> Dictionaries ar very good for storing collections of related information

# program where the goal is to write a report on some given spacecrafts out there in the universe
def main():
    spacecraft = { # A key is simply some name, which access some particular value inside of this dictionary 
        "name": "Voyager 1",
        "distance": 163,
    } # Dictionaries begin with curly braces
    
    print(create_report(spacecraft))

def create_report(spacecraft): # returning a multiple line f string 
    return f""" 
    ========= REPORT =========

    Name: {spacecraft["name"]}
    Distance: {spacecraft["distance"]} AU (Astronomic Units)

    ==========================
    """

main()

# access the value of a key in a dict --> dict["key"] --> return the value if the key "key" for dictionary dict