import re
# There is still one problem:
# What if the user types something like 'https://ww.google.com' for the 'url', then nothing is gonna happen since there is no match to replace to (re.sub() doesn't hold)
# re.sub() is useful to cleaning up data, but why don't we instead go back to re.search() and use it to solve the same problem but in a way it's conditional, where I can confidently say, yes or no, to our program.

url = input("URL: ").strip()

# recall re.search() will return to you the matches you've captured' in this case, what we want to capture --> everything to the right of the twitter.com URL, which in this case will be '.+'; to prepare for capturing, apply parenthesis as '(.+)'
matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE) # use re.IGNORECASE to apply case-insentivity
if matches:
    username = matches.group(2) # we use the argument/int '2' since the grouping '1' is (www\.)
    print(f"Username: {username}")

# Now, if the user types something like 'https://ww.google.com', then nothing gets printed

# we can also use the walrus operator here:

if matches := re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE): # use re.IGNORECASE to apply case-insentivity
    username = matches.group(2) # we use the argument/int '2' since the grouping '1' is (www\.)
    print(f"Username: {username}")

# to avoid catching while also using parenthesis, we can use the non-capturing version of a group '(?:...)'; for example, in our regex line of code for (?:www\.); therefore, now we will only have one group '(.+)' instead of two ('(www\.)' and '(.+)'), so our .group() method would receive an int 1 as an argument, instead of 2

url = input("URL: ").strip()

# Twitter only supports [a-zA-Z0-9_]
if matches := re.search(r"^https?://(www\.)?twitter\.com/([a-zA-z0-9_]+)", url, re.IGNORECASE):
    username = matches.group(2) 
    print(f"Username: {username}")