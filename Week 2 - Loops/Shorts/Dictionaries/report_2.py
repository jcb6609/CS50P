def main():
    spacecraft = {
        "name": "James Webb Space Telescope"
    }
    
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f""" 
    ========= REPORT =========

    Name: {spacecraft["name"]} 
    Distance: {spacecraft.get("distance", "Unknown")} AU (Astronomic Units)

    ==========================
    """

main()

# To access some key we don't need to always use the bracket notation
# Another method --> .get() method with our dict's name as the referenced obj and the desired key we want to acces in on the method's argument  --> access some key --> if key does not exist, then we get some other value we specified instead
# dict.get("key", '...') --> the second argument '...' is returned if "key" is not part of the dictionary dict
# It allows use to avoid the key error whenever we try to access a dict's key that is not defined