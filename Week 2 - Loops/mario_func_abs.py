# If you like abstraction, when implementing print_square, we don't really care what it means to print a row (print_row),
# we just need to know that someone's taking care of printing the row, you can pass the buck to another function altogether
# and how does print_row work? It could use a for loop, it could use a string multiplication trick, etc.
# This is a way to take a larger program- and to decompose it into these smaller components, that one assembled, achieve your final idea 

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size) # by default the print() function has end="\n"

def print_row(size): 
    print("#" * size)

main()
