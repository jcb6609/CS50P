# create a variable name that receives the name of the user 
# the output has no additional left/right whitespaces
# the output capitalizes the first letter of every word
name = input("What is your name? \n-->").strip().title()
print("Your name is: " + name)

print("\n")

# what if we want to create a function, so that every time called, a text "Hello, " is returned?
# let's create a function named "hello()" using the kewyword def
def hello(): # everything intended beneath this line of code is gonna be part of the function 
    return "Hello, "

print("Using the def function hello():")
print(hello() + name)

# recall the difference as in java for a method definition between "void hello()" and "String hello()"
# print for "void hello()" 
# return for String hello()" 

print("\n")
# parametrized def function
def helloParameterized(var):
    print("Hello,", var) # remember when using commas for printing more arguments a whitespaces is already added because of sep=' '

print("Calling the function helloParameterized()")
helloParameterized(name) # name (variable called through the helloParameterized()) is copied to another variable called var (argument of helloParameterized())

print("\n")
# parametrized def function (using an input argument where, if not value is called, then it sets a default one)
def helloParameterizedDefault(var = "World!"):
    print("Hello,", var)

helloParameterizedDefault() # uses the default set for the function input argument
helloParameterizedDefault(name) # uses the name var, it ignores the defualt set for the function input argument