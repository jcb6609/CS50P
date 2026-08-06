import re

# goal: to reformat the user's input in the format we expect 
# it's nice to standardize or canonicalize the format in which you are storing your data so tht if you print out the user's name it's always the same format
name = input("What's your name? ").strip() # .strip() method removes leading (very beginnig) and trailing (very end) characters (like spaces, tabs, or newlines) from a string

"""
if "," in name:
    last, first = name.split(", ")
    # reformat our 'name' var
    name = f"{first} {last}" # Overwriting users input 'name'

print(f"hello, {name}")
"""

# Check that if for our 'name' var we have 'Bermudez, Julio' it will go through as 'hello, Bermudez Julio' instead of 'hello, Julio Bermudez':
# If we want to use regular expressions we need to use the re library

# search for a pattern to represent 'last_name, first_name':
# You can get back more iformation out of re.search() and assign its implementation to an obj var, and therefore,
# we can get more precise answers of what we've found when searched for
matches = re.search(r"^(.+), (.+)$", name)
# we can use parenthesis '(...)' to capture regex expressions --> allowing us to extract specific amount of information from, in this case, the user's own input (we can reverse this process too by using the non-capturing version '(?:...)')

if matches:     # if obj 'matches' is True (meaning that our whole regex function holds for the given user's input), then...
    last, first = matches.group() # the .group() method with obj reference 'matches' will catch/group the captured regex expressions inside parenthesis, then assignate those expressions to first 'last', and last 'first' variables 
    # overwrite 'name' var using previous line vars assignation for our if block
    name = f"{first} {last}" # we can then assignate a var 'name' for our already catched vars 'first' and 'last' when assignating them to our caught .group() method with obj reference 'matches' from its assignation to the re.search() implementation

# If out regex pattern does not hold, we will directly print name, therefore not entering the if block and not overwriting the 'name' var inside
print(f"hello, {name}") 

# if the user inputs 'Bermudez, Julio', then the regex pattern will hold for our if block, then gouping, and reformatting the input ('name' is overwritten), so that now printing 'hello, Julio Bermudez'