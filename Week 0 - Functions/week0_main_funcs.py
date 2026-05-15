# --> Note: In Python, if you use a function, it must already exist by the time you are calling it
# --> Note: use a main() function to write a top-to-bottom logic code and def it at the top of the program for convention
def main():
    name = input("please enter your name: ").strip().title()
    helloParameterizedDefault()
    helloParameterizedDefault(name)

def mainCalc():
    x = float(input("Enter the value of x: "))
    y = float(input("Enter the value of y: "))
    print(f"the sum of {x} and {y} is {calcSum(x, y)}")

def mainElevatedTo():
    x = float(input("Enter again the value of x: "))
    print(f"x squared is: {square(x)}")
    print(f"x cubed is: {cube(x)}")
    print(f"x to the fourth power is {pow(x, 4)}")


def helloParameterizedDefault(var="world"):
    print("Hello,", var)

def calcSum(a, b):
    return a + b

def square(n):
    return n * n # n * n = n^2

def cube(n):
    return n ** 3 # n^3

main() # execute the main() function, which calls helloParameterizedDefault()
mainCalc() # execute the mainCalc() function, which calls calcSum()
mainElevatedTo() # execute the mainElevatedTo() function, which calls square()

# by calling the main function in this way, this allows the user to organize functions in any way wanted
# scope: term that refers to a variable only existing in the context in which you define it.
# Recall the usage of variables accross multiples classes in Java!
# returns: hands back a value
