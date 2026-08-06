# Check that if for our 'email' var we have 'JCB6609@PSU.EDU' it will go through as Invalid since 'edu' is in lowercase, how to solve?
# --> Force the user input to e lowercase using the .lower() method:
# Option1 --> 'email = input("What's your email? ").strip().lower()'
# Option2 --> if re.search("...", email.lower())
# Option3 -->
# There is another mechanism in the re.search function:
# --> the 3rd argument, by defualt, 'flags=0'
# --> this 3rd argument also accepts built-in re variables (contstant) that have meaning to re.search():
    # re.IGNORECASE
    # re.MULTILINE
    # re.DOTALL

import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# Now, 'email' containing 'JCB6609@PSU.EDU' will be outputed as 'Valid' since it will ignore the case of the input thanks to the 're.IGNORECASE' argument 
