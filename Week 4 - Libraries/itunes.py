# write a code that pretends to be a browser to grab data (use the iTunes API)
import requests
import sys

if(len(sys.argv) != 2):
    sys.exit()

response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=1&term=weezer {sys.argv[1]}") # requests.get() is a function that will get some response from a server
print(response.json()) # .json() method that fromats our (referenced) data as a JSON

# what we receive as output --> is almost as the JSON we got before (even though is still a JSON) but as a standard Python dictionary thanks to the request library

# as you can see, one of our keys has a value formated as a key with other multiple key-value pairs inside of a value list,
# therefore we need another alternative to format our data a little bit more cleanly.