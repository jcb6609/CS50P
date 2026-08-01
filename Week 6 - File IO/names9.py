# What if we wanted to keep track of other information (in our 'file') as well?
# Suppose that we wanted to STORE information including a student's name and their house at Howarts, where do we go about putting that? --> well, we can change our file convention to .csv (Comma-Separated Values)
# (the professor changes the 'names.txt' file convencion for 'names.csv', then he manually modifies the information in the file so that we have: Hermione,Gryffindor '\n' Harry,Gryffindor '\n' ... Draco,Slytherin)
# You could think of these commas as representing a column 

# the professor creates a new csv filed named 'students.csv', and copy-pastes the info from 'names.csv' to this new csv file

with open("students.csv") as file:
    for i in file: # remember that i here is iterating over EACH LINE of our 'file'
        # ultimately, split() is gonna return us a list of all of the individual parts to the left and to the right of the argument "," for the complete referenced i.rstrip() line string
        row = i.rstrip().split(",") # we can use the .split() method with a "," str as its argument to split the total string into 2 pieces, the piece to the left of the comma and the piece to the right of the comma (we can split multiple times, not necesarrily just once, but we have to adjust the default .split() method arguments); e.g. row = ["Harry", "Gryffindor"] (next line) row = ["Hermione", "Gryffindor"] (next line) ... row = ["Draco", "Slytherin"]; since we are iterating over each line, our row list is gonna get updated each time i goes to the next line of our file!
        print(f"hello {row[0]} from {row[1]}")