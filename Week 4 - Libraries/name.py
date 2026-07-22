import sys

try:

    # Check for errors
    if(len(sys.argv) < 2):
        print("Too few arguments")
    elif(len(sys.argv) > 2):
        print("Too many arguments")

    # Print name tags
    print("hello, my name is", sys.argv[1]) # output with Julio as input 'python name.py Julio': hello, my name is Julio
# --> If not input provided, then we will get back an IndexError

except(IndexError):
    print("Too few arguments")
    print(sys.argv[0]) # --> sys.argv[0] prints 'name.py'

# --> If we add single quotes for specifying our input in the command line, then it will be taken for sys.argv as a whole list element rather than different elements separated by space when written in the terminal