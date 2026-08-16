def main():
    # the var student, stores a tuple (returned from function get_student()) with vars 'n' and 'h'
    student = get_student() # student = (n, h) --> e.g. studnet = ("Harry", "Gryffindor") 
    print(f"{student[0]} from {student[1]}")

    
def get_student():
    n = input("Name: ")
    h = input("House: ")
    # In the next line, we are returning a tuple 
    return (n, h) # we can return either var (returning only one value, a tuple sequence)

if __name__ == "__main__":
    main()