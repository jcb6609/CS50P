import re
# Extracting information (from Strings) pin order to answer some questions
# Goal: Prompt users for the URL of their Twitter profile and extract from it what's the username's name 
# --> Extract the username only!
"""
url = input("URL: ").strip()

# strings come with multiple methods 
username = url.replace("https://twitter.com/", "") # for the .replace() method, you pass two arguments, first the thing you want to replace, and second the thing you want to replace it with
print(f"Username: {username}")
"""

# Check that if the user types something else that could not match the .replace() first arguent, then our program will broke, we need to fix that

url = input("URL: ").strip()

# A prefix is a string or a substring that comes at the start of another
username = url.removeprefix("https://twitter.com/")
print(f"Username: {username}")