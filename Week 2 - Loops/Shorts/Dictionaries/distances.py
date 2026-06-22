# make a dictionary where we have the names of our spacecraft in one column, and the distances od those spacecraft in another column

distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():
    for name in distances.keys(): # dictionaries come with a method called keys that returns all the keys in our dictionary; we could also use dict.values()
        print(f"{name} is {distances[name]} AU from Earth")

    """
    We could also do:

    for name in distances:
        print(name, distances[name], sep=", ")
    """

main() 