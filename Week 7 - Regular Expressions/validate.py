# Solve problems using simple syntax:
# Validate a user's email address

 # .strip() has the effect of stripping off any leading whitespace to te left or any trailing whitespace to the right
email = input("What's your email? ").strip() # e.g. email = "jcb6609@psu.edu"

"""
# deficient code:
if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")
"""

# split our referenced 'email' str (by the .split() method with "@" argument), then splitting the str into two parts, the part on the left "@" side and the part on the right "@" side
username, domain = email.split("@") # e.g. email = ["jcb6609", "psu.edu"] --> username = "jcb6609", domain = "psu.edu

"""
lacks consistency when passing, for example, jcb6609@.edu (no domain)
if (username and domain.endswith(".edu")): # "if 'username'" --> True if at least a char found, False if empty; we can use the method .endswith() to check the last chars (function's argument, in this case ".edu") of a referenced string
    print("Valid")
else:
    print("Invalid")
"""