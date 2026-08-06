import re
# would't be nice to call:
"""
matches = re.search(r"^(.+), (.+)$", name)

if matches:
"""
# in the same line?
# --> We need to use ':=' if we want to only assign something (from right to left) and you want to ask an if or an elif question in the same line:

name = input("What's your name? ").strip()

if matches := re.search("^(.+), *(.+)$", name):
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"

print(name)




