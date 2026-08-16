def main():
    student = get_student() # the 'student' var is assigned to a returned dict by calling the get_student() function
    if (student["name"] == "Padma"):
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}") # use single quotes for entering a dict key when also printing their values!


def get_student():
    student = {} # create an empty dict assigned to 'student'

    # creating and accessing a dict key and its respective value:
    student["name"] = input("Name: ") # the value of a key "name" for the 'student' dict (student["name"]) is assigned to an input() return, therefore taking the "name" key a value assigned from the user's input
    student["house"] = input("House: ")
    return student


if __name__ == "__main__":
    main()