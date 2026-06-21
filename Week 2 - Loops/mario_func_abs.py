# If you like abstraction, when implementing print_square, we don't really care what it means to print a row (print_row),
# we just need to know that someone's taking care of printing the row, you can pass the buck to another function altogether

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size) # by default the print() function has end="\n"

def print_row(size): 
    print("#" * size)

main()