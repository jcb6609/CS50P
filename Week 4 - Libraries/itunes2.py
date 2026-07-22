# write a code that pretends to be a browser to grab data (use the iTunes API)
import json
import requests
import sys

if(len(sys.argv) != 2):
    sys.exit()

response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=1&term=weezer {sys.argv[1]}") # requests.get() is a function that will get some response from a server
print(json.dumps(response.json(), indent=2)) # json.dumps() another function from the json module that will allow us to print our 'response.json()' argument more cleanly while indenting everything at least two spaces thanks to the second argument 'indent=2'
