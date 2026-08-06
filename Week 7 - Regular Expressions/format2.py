# we don't really have to say 'matches.group()' since we can get specific groups back that we want:
import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)

if matches:
    last = matches.group(1) # gets the first set of parenthesis '(.+)' group for our 'matches' obj; here, we refer to the first group with the int argument 1 for .group()
    first = matches.group(2) # gets the second set of parenthesis '(.+)' group for our 'matches' obj; here, we refer to the second group with the int argument 2 for .group()
    # we can avoid writing both lines of code above and the next one underneath by saying: 'name = matches.group(2) + " " + matches.group(1)'
    name = f"{first} {last}" 

print(f"hello, {name}")

# Note: for re.search() when grouping with .group(), there is something else located in location 0, that's why we have to start counting our parenthesis groups by 1 and not from 0

# we can use the '?' symbol next to our ' ' space to hold whether we have a space or not since ? holds for either 0 or 1 repetitions, e.g. 'Bermudez,Julio'
# we can also use the '*' symbol next to the ' ' space to hold for when we have 0 or more repetitions of it, e.g. 'Bermudez,    Julio'