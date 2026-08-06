# Let's now not only check for a username and domain but to check that our string ends in .edu as well
import re

email = input("What's your email? ").strip()

# Check the mistake we committed here:
"""
if re.search(".+@.+.edu", email): #'.edu' in this case is not '.edu' at all but 'any character, then, edu', therefore, 'email' var content such as 'jcb6609@psu?edu' will go through as Valid
    print("Valid")
else:
    print("Invalid")
"""

# How to solve it? --> Specify that we want a normal dot instead of a regex symbol usingt the backslash '\' character and the char we want to use with it, int this case the '.' --> '\.'
# Also, since bakclashes usually are related to a new line, we need to specify our string as a raw string by using an 'r' character before the string content --> r"..."
# Note: backslash '\' --> scape sequence

"""
if re.search(r".+@.+'backslash'.edu", email): # backslash throws some kind of syntax warning when displaced in comments, gotta replace it for 'backsash' meanwhile,
    print("Valid")
else:
    print("Invalid")
"""

# Check that if for our 'email' var we have 'jcb6609@@@psu.edu' it will still go through as Valid, we need to solve that
# Check that if for our 'email' var we have 'My email is jcb6609@psu.edu.' it will still go through as Valid, we need to solve that

"""
* '^' --> matches the start of the string:
    
    - caret symbol: '^'
    - used to represent that you want a regex pattern to match the start of the string specifically, not anywhere but the start.

* '$' --> matches the end of the string, or, matches just before the newline at the end of the string 
"""
# Using '^' and '$' in our pattern '^...$' will basically require of our user's input to:
 # --> start and end with the same pattern
 # --> re.search() will now evaluate for an exact match of our patter in 'email'

"""
if re.search(r"^.+@.+'backslash'.edu$", email):
    print("Valid")
else:
    print("Invalid")
"""

# Check that if for our 'email' var we have 'jcb6609@@@psu.edu' it will still go through as Valid, we need to solve that
"""
if re.search(r"^[^@]+@[^@]+\.edu$", email): # this will unallows things like 'jcb6609@@@psu.edu'
    print("Valid")
else:
    print("Invalid")
"""
# e.g. [^@]+ --> any character on the keyboard except for a @ sign with 1 or more repetitions --> unallows things like '@@@...'


# Check that if for our 'email' var we have '.edu@something.edu' it will still go through as Valid, we need to solve that
# alphanumeric: [a-zA-Z0-9_] (and underscore)
# [a-zA-Z0-9_] --> any character between a and z or any character between A and Z or any digit etween 0 and 9 or underscore '_' (meaning we can ONLY accept this character), so that we do not need [^@] as in the previous file's code

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
# Now, 'email' containing '.edu@something.edu' will be outputed as 'Invalid', which is correct