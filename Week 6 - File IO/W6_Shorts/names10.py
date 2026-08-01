with open("students.csv") as file:
    for i in sorted(file): # remember that i here is iterating over EACH LINE of our 'file', where in this case we are iterating over a sorted version of our file thanks to the sorted() function with our 'file' as its argument
        # ultimately, split() is gonna return us a list of all of the individual parts to the left and to the right of the argument "," for the complete referenced i.rstrip() line string
        name, house = i.rstrip().split(",") # we can also assign a variable to each element of our list (the method.split() returns a list); e.g. ["Hermione", "Gryffindor"] --> name = Hermione, house = Gryffindor
        print(f"hello {name} from {house}")