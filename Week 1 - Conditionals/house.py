name = input("What is your name?: ")

match name:
    case "Harry" | "Hermione" | "Ron": # previosuly: if (name == "Harry" or name == "Hermione" or name == "Ron")
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: # 'case _' refers to whatever case has not yet been handle.
        print("Who?")