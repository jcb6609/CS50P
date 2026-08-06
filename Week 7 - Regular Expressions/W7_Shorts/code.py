# use regex to create some pattern we expect in some data we might have
# one other kind of data we might be able to validate, besides emails, is something called a hexadecimal code 

# Colors have a certain assigned hexadecimal color, a way of representing this color, but in a computer's memory 
# e.g. '#0076BA' --> like a type of blue
# These patterns will always begin with a '#' symbol follewed by six characters who range from 0 to 9 or A to F, upper or lower case.

# The very first two characters, after the hash symbol, define how much red is in this color on a scale of 00 (lowest) to FF (highest)
# There is also this second set of two characters, in this case '76', which corresponds to the amount of green in the color
# Then, the final two, in this case 'BA', corresponds to the amount of blue that's in this particular color above

# e.g. '#FF0000' --> all red (reddest you can get)
# e.g. '#00FF00' --> all geen (greenest you can get)
# e.g. '#0000FF' --> all blue (bluest you can get)

# e.g. '#FFFFFF' --> all white
# e.g. '#000000' -- all black

import re 

def main():
    code = input("Hexadecimal color code: ").strip()

    # Let's try to validate the user's input using some kind of pattern
    if match := re.search(r"^(#[a-fA-F0-9]{6})$", code): # include the number of repetitions inside the grouping parenthesis '()' since we want to catch more than just the first character for our group 
        color_match = match.group(1)
        print(f"Valid")
    else:
        print("Invalid")


"""
# Ww could also do the avove as:
def main():
    code = input("Hexadecimal color code: ")

    pattern = r"^#[a-fA-F0-9]{6}$"
    match = re.search(pattern, code)
    if match:
        print(f"Valid. Matched with {match.group()}") # we group our whole 'match' implementation (which is basically our regex)

    else:
        print("Invalid.")
        
main()

"""


main()