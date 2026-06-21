students = ["Hermione", "Harry", "Ron"] # List of length 3, assigned to the var stuents (which will have datatype list)

# the symbol * next to the begining of a list name (e.g. *students) acts as a wrapper remover that unpacks the list
# when using the symbol together with a list using the print() function, it unpacks the list and feeds each item into the function as a separate argument

print("Using: print(students)")
print(students)

print("\n")

print("Using: print(*students)")
print(*students) # Python reads this as: print("hermione", "Harry", "Ron")

print("\n")

print("Using: print(*students, sep='newline char')")
print(*students, sep="\n") # recall that the print function arg sep is defined as default for sep=" "

print("\n")

# if you want to get inside of a variable (in this case 
# the var students, with datatype list, and get a specific 
# value, which means you want to index into the list, you can do:

print("accessing each object individually: print(students[0]))...")
print(students[0]) # students[0] gets the index [0] of the list students (which corresponds to the first object of the list)
print(students[1])
print(students[2])

print("\n")

# we can use a loop automatically without having to manually type out 0, and then 1, and then 2, and then ...
# You can use a loop not just to count from 0 to 1 to 2, but also to iterate over anything, not just numbers but strings

print("accessing each object using a for loop with a an interable variable, directly defined in the for loop:")
for student in students: # this for loop prints all of the students (objects from students list) one by one
    print(student) # remember that for the function print() we have a default end="\n"
# here above, Python can initialize the iterative var 'student' for our loop

print("\n")

# for i in range(students) --> students is not an integer, therefore the range() function does not work (the range() function expect an integer as an argument)
# we can use instead a len() function to pass a number to range() using the students list as an argument
print("Using an iterable variable, already defined in the for loop, together with the length() function for the students list nested inside of a range() function: ")
for i in range(len(students)): # students = ["Hermione", "Harry", "Ron"] --> len(students) = 3 --> access each index of our list --> therefore we gotta print list[i] instead of just i since the function len(studnets) access the indexes of our list rather than its actual objects 
    print(students[i])

print("\n")

print("Printing both i and students[i] in the same print function print(i, students[i]) using the aboves loop: ")
for i in range(len(students)):
    print(i, students[i])

print("\n")

print("Similarly, using above's loop, if we don't want the index 0 to appear, we can simply add a + 1 for the i argument: ")
for i in range(len(students)):
    print(i + 1, students[i])

# range(len(students)) --> dynamically wayt to know how many students (objects) are in the students list