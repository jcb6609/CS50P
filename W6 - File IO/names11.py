# another way to sort:
students = [] # empty list

with open("students.csv") as file:
    for i in file:
        name, house = i.rstrip().split(",")
        students.append(f"{name} from {house}") # appending this whole string to our 'students' list

for i in sorted(students): # sorted() function applied here for our for loop iterating over our students list
    print(i)