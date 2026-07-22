import sys


if(len(sys.argv) < 2):
    sys.exit("Too few arguments") # exits the program
elif(len(sys.argv) > 2):
    sys.exit("Too many arguments") # exits the program

print("hello, my name is", sys.argv[1])