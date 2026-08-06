# our regular expressions allow use to express patterns, and parenthesis can also capture information --> powerful tool
import re
"""
url = input("URL: ").strip()

username = re.sub(r"https://twitter.com/", "", url) 
print(f"Username: {username}")
"""
# mistakes that we currently have:
"""
* The protocols --> http vs https
* The subdomain --> www
"""
# Let's be tolerant of all possible valid inputs for now
"""
url = input("URL: ").strip()

# Let's match the beginning of the string (regarding the use of our regex) by using '^'
username = re.sub(r"^https://twitter.com/", "", url) # we do NOT want to match the end of the string (regarding the use of our regex) by using '$' since we don't want to match the end of the string with '.com/' but rather with our user's username

# check that our regex pattern should have a 'backslash' when dealing with certain characters such as '.' rather than '.' by itself, which is a regular expression and not a simple point

print(f"Username: {username}")
"""

url = input("URL: ").strip()

# if we want to make a group optional we need (...)?, if we want to make only a character optional then we just put '?' next to it as in 'https?' --> here, only the s can be repeated 0 or more times (optional)
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

print(f"Username: {username}")