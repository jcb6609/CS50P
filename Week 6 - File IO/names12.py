# We need to sort properly, since we want to sort by our srudents' names, then we cannot simply rely on the fact that our sorted functionality starts from left to right and that we set our students to be always on the left-most part of our iterable elements
# it would be better, really, to come up with a technique for sorting by the students' names and not by some English sentence line
# we will need to collect the information about each student before we bother assembling that sentence.

students = []

with open("students.csv") as file:
    for i in file:
        name, house = i.rstrip().split(",")
        # we can implement the next three lines by doing: student = {"name": name, "house": house}
        student = {} # let's temporarily create a dictionary name 'student' that stores this association of 'name' with 'house'
        student["name"] = name # the key '"name"' is set for our 'students' dictionary as 'students["name"]', which stores our 'name' var as 'students["name"] = name'; key --> "name", value --> name
        student["house"] = house # the key '"house"' is set for our 'students' dictionary as 'students["house"]', which stores our 'house' var as 'students["ouse"] = house' as its value; key --> "house", value --> house
        # print(student) ## e.g. student = {"name": "Hermione", "house": "Gryffindor"}
        students.append(student) # here, we are appending our temporary dictionary 'student' to our list 'students'
        # print(students) ## e.g. students = [{'name': Hermione, 'house': 'Gryffindor'}] --> A list containing a dictionary

# after appending our list with each temporary dictionary for each of our 'file''s lines, our list ends up as:
# e.g. students = [{'name': 'Hermione', 'house': 'Gryffindor'}, {'name': 'Harry', 'house': 'Gryffindor'}, ..., {'name': 'Draco', 'house': 'Slytherin'}]

for i in students: # iterating over the 'students' list with our appended temporary dictionaries named 'student'
    print(f"hello {i['name']} from {i['house']}") # recall that here i is entering directly into our 'students' elements, therefore, we can enter the values of the dictionary keys by 'i['name']' and 'i['house']' 
    # why do we use single quotes to surround 'house' and 'name'? --> because we are already using quotes for our f-string, so we need single quotes to don't mix them up