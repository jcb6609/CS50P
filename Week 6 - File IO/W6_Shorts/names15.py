students_list = []

with open("students.csv") as file: 
    for i in file:
        name, house = i.rstrip().split(",")
        
        students_dict = {"name": name, "house": house} 
        students_list.append(students_dict)


def get_name(stu_dict): 
    return stu_dict["name"]

# What now if we want to sort by "house" ? -->
def get_house(stu_dict):
    return stu_dict["house"]

# when you pass a function like get_name() or get_house() to the sorted() function as the value of 'key=', that function is automatically called by the sorted function for you on each of the dictionaries in the list, and it uses the return value of 'get_name' or 'get_house' to decide what strings to actually use to compare in order to decide when sorting
# we pass our function (either 'get_name' or 'get_house') as the value of 'key='
# recall here we are using a list of dictionaries
for i in sorted(students_list, key=get_house, reverse=True):
    print(f"hello {i['name']} from {i['house']}")

# the sorted() function will use the value of key (get_house) in this case calling that function on every dictionary in the list, that it's suppose to sort, and that function 'get_house' returns the string that sorted() will actually use to decide whether things go in the order left-right or right-left, it alphabetizes these things based on that returned value
# see that we are not using parenthesis for calling 'get_house' in 'key=', we are passing it only by its name so that the sorted() function can call that 'get_house' function for us