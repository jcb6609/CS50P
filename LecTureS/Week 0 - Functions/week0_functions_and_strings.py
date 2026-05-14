# First_Python_Program
print("Hello World!") # print() displays text/output to the console
name = input("What is your name? \n--> ") # input() displays a message inside parenthesis and waits for user input (text/string)

# Note: In Python, a method is a function attached to an object

# Remove whitespace from a str variable, from user-input (only removes spaces from the beginning and end of the string.):
name = name.strip() # here, the built-in function strip() is referenced to the variable name, producing the method name.strip()

print(f"user-input's name with no spaces (start and end only): {name}")

# capitalize user's name (just the very first letter) using capitalize()
name = name.capitalize() 

print(f"name capitalized (only first letter): {name}")

# capitalize (just the very first letter) of every word using title()
name = name.title()

print(f"full name capitalized (firts letters of multiple words): {name}")

print(f"welcome {name}") # format string f"... {...}" allows variables to be inserted inside {}, inside a print(), so that they are printed

age = input("What is your age? \n--> ") # reember that input() receives text, so that the variable age would store string data
print("You are " + age + " years old!") # "+" concatenates (joins) strings together

# but this process seems repetitive, re-applying diff methods, let's make it shorter
# directly when assigning a variable to hold the user-input, we can also implement the methods:

name = input("Please, enter your name again: \n--> ").strip().title()

print(f"here, your name variable is now using the strip() and title() methods in the same line of code as when defining user-input: {name}")

print("now, what about splitting and assigning your first and second/last name to different variables?")
# Split user's name into first and last name variables
first, last = name.split(" ") #split(" ") method with a single whitespace to indicate a separation/split on that character, returning a sequence of values, and assigning both of those values to different variables

print(f"first name: {first} and last name {last}")

# this way of using print(), with different arguments separated by comma(s), has the sep=' ', which creates an automatic space between the arguments' output
print("Great, then we have", name, "with age", age)

# build-in functions in Python:
 # https://docs.python.org/3/library/functions.html

# print() function --> check documentation:
 # print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

print("so, we have", name, age, "with a '///' which is a separator for the print() function", sep="///")
print("we also can modify jump line behavior with end", end='\n\n')

print("so that the defined behavior for print() can be modified")