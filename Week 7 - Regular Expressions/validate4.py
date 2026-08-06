import re

email = input("What's your email? ").strip()

# Now, 'email' containing '.edu@something.edu' will be outputed as 'Invalid', which is correct

# The fact is, we can reduce syntax:
# alphanumeric --> [a-zA-Z0-9_] = \w
# '\w' --> word character  --> alphanumeric symbol or underscore as well
"""
if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
"""


# We can introduce parenthesis '()' and or '|' symbols to specify more possible (correlated) cases:
if re.search(r"^\w+@\w+\.(edu|com|gov|net|org)$", email):
    print("Valid")
else:
    print("Invalid")

# If we want to allow a whitespace '\s' together with our alphanumeric bracket set '[a-zA-Z0-9_]' we can do:
# --> [a-zA-Z0-9_ ] = (\w|\s)

