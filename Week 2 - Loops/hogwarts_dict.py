# Dict: Keys on the left (column names), values on the right (column vertical values)
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

print("print each value case individually, from each key, using print(students['key'])...")
print(students["Hermione"]) # Access and prints the value(s) of the key "Hermione" for the students dict
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

print("\n")

# when you use a for loop in Python to iterate over a dictionary, by design, it iterates over of all the keys

for student in students:
    print(student, students[student], sep=", ") # prints all of the keys with the first argument (student), and print it's respective values with the second argument (students[student])

print("\n")

# Dictionary of lists: 
dict_lists= {
    "name": ["Hermione", "Harry", "Ron", "Draco"],
    "house": ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"],
    "patronus": ["Otter", "Stag", "Jack Rusell terrier", None] # None --> Python's version of null
}

# first column then row (index)
for student in range(len(dict_lists["name"])):
    print(dict_lists["name"][student], dict_lists["house"][student], dict_lists["patronus"][student], sep=", ") # dict_lists["name"][student] --> access the "name" key first, then chooses the student iterator var index to choose the specific value, and so on with the other key values

"A dictionary is inside curly braces!"
print("\n")

# List of dictionaries:
list_dicts = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"}, # one dictionry, three keys, 3 values (one value per key in this case)
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Rusell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

# first row (index) then column
for student in list_dicts:
    print(student["name"], student["house"], student["patronus"], sep=", ") # open the value of the "name" key for the student interator index var, then the value of the "house" key for the student iterator var index var, then the value of the "patronus" key for the student iterator var index