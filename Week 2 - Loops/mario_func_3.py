def main():
    print_square(3)

def print_square(size):
    # For each row in square
    for i in range(size):
        # For each block in row
        for j in range(size):
            # print block
            print("#", end="")
        # Create a new line after ###
        print() # by default the print() function has end="\n"

main()    

"""
We can also implement:

def print_3x3_block(line):
    for _ in range(line): # _ --> range(line) --> line = 3 --> 0, 1, 2 (stop at 3) --> loop works 3 times (0, 1, and 2)
        print("#" * line) # print ### (one brick line)
"""