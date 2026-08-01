students_list = []

with open("students.csv") as file: # by default open("students.csv", "r")
    for i in file:
        name, house = i.rstrip().split(",")
        # create a dictionary to save our values for 'name' and 'house' vars
        students_dict = {"name": name, "house": house} # saves temporarily each line of our 'file''s 'name' and 'house' vars, then we append the whole dictionary into our list, then it finishes the loop, and we continue appending each dictionary for each line 
        students_list.append(students_dict)

# after appending our list with each temporary dictionary for each of our 'file''s lines, our list ends up as:
# e.g. students = [{'name': 'Hermione', 'house': 'Gryffindor'}, {'name': 'Harry', 'house': 'Gryffindor'}, ..., {'name': 'Draco', 'house': 'Slytherin'}]

# How to sort our 'students_list' by looking at a specific key in each of our dict list element(s)?
def get_name(stu_dict): # the function get_name() returns the student's 'name' var from our dictionary with key "name"
    return stu_dict["name"]

# Python allows you to pass functions as arguments into other functions:
for i in sorted(students_list, key=get_name): # the second argument 'key=get_name' inside the sorted() functions allows us to sort our first argument 'student_list' according to the returned value for our get_name() function while pasing 'students_dict' to it --> return students_dict["name"]
    print(f"hello {i['name']} from {i['house']}")