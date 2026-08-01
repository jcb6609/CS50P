students_list = []

with open("students.csv") as file: 
    for i in file:
        name, house = i.rstrip().split(",")
        students_dict = {"name": name, "house": house} 
        students_list.append(students_dict)

# alternatively, we can use lambda functions, which are anonymous functions, functions that have no name
# why? Because we do not need to give it a name if we are only going to call it in one place

for i in sorted(students_list, key=lambda stu_dict: stu_dict["name"]): # lambda's structure --> 'lambda students_dict: students_dict["name"]' --> 1). Keyword 'lambda', 2). passed argument 'students_dict' follewed by ':', 3). after the ':' then we set the return body of our lambda function (no 'return' keyword needed) by only typing 'students_dict["name"]'
    print(f"hello {i['name']} from {i['house']}")

# lambda can take more passed parameters; e.g. 'lambda students_dict, x, y: ...'