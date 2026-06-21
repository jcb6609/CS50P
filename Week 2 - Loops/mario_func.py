# Assimilating a three vertical block obstacle that mario has to jump over
def main():
    print_column(3)

# we now have a function, an abstraction, print_column() that is going to allow us to think about printing some chunk of blocks in the Mario world at a time
def print_column(block_height):
    for _ in range(block_height):
        print("#")

main() # for abstraaction what matter is that te main() function does not need to know that the underlying implementation of print_column() has changed

"""
Our print_column() function can also have this body implementation:
    print("#\n" * block_height, end="")
"""