students_list = []

with open("students.csv") as file: 
    for i in file:
        name, house = i.rstrip().split(",")
        
        students_dict = {"name": name, "house": house} 
        students_list.append(students_dict)


def get_name(stu_dict): 
    return stu_dict["name"]


for i in sorted(students_list, key=get_name, reverse=True): # Reversing each of our sorted list dictionaries according to each dict key '"name"' vars 'name'
    print(f"hello {i['name']} from {i['house']}")