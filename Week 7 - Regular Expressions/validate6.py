# Check that if for our 'email' var we have 'jcb6609@cmpsc360.psu.edu' it will go through as Invalid since it has two domains, and therefore, two period symbols instead of 1 (only one domain), how to solve it?
import re

email = input("What's your email? ").strip()

# we add an extra '\w+' to avoid things like 'jcb6609@.psu.edu' or 'jcb6609@ psu.edu' (thanks to the '+')
"""
if re.search(r"^\w+@\w+(\w|\.)+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
"""

# We can also use another apprach by repeatig the '\w+\.' pattern using a '?' symbols with represents 0 or more repetitions, holds if there are no repetitions or if there are 1 repetitions, or if more than 1 repetition allowed, then we could use instead '*' for 0 or more repetitions
# e.g. '^\w+@(\w+\.)*\w+\.edu$'
# e.g. '^\w+@(\w+\.)?\w+\.edu$'
# recall that since we are holding for 0 or more repetitions '*' of ur domain, we must repeat the '\w+' pattern (outside-right the parenthesis '(...)?' or '(...)*') to mantain for at least one repetition or more

if re.search(r"^\w+@(\w\.)*\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")