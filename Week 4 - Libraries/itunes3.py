import json
import requests
import sys

if(len(sys.argv) != 2):
    sys.exit() # use break to terminate only loops

# we change now the limit to 50 trackNames instead
response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=50&term=weezer {sys.argv[1]}") # requests.get() is a function that will get some response from a server

obj = response.json()

# i is going to iterate over all the keys inside of our "results" key, which contains a list with other key-value pairs
for i in obj["results"]: # obj["results"] --> accessing the '"results"' i key's value
    print(i["trackName"]) # access the i key's value(s) with name '"trackName"'