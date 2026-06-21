# Assimilating a four horizontal mistery block line that mario has to jump to for getting coins 
def main():
    print_row(4)

def print_row(width):
    for _ in range(width):
        print("?", end="", sep="")

main()

"""
Our print_row() function can also have this body implementation:
    print("?" * width)
"""