def main():
    student = get_student() # the 'student' var is assigned to a returned list by calling the get_student() function
    if (student[0] == "Padma"):
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

    
def get_student():
    n = input("Name: ")
    h = input("House: ")
    return [n, h] # now, we are returning a list 


if __name__ == "__main__":
    main()