# API:
    # - An API (Application Programming Interface) is a way to talk to some other application, perhaps over the internet or in your own code.
    # We will focus on a particular API, the API for the Art Institute of Chicago (Museum based on Chicago) --> it has an API, a way to access all of the artwork in their collection and display it in our programs as long as we make the right requests.
    # If we want to write a program here to access the previous mentioned API, let's create a program called api.py

import requests # allows me to send requests over the internet to the Art Institute of Chicago (AIC)
import json

# How? -->  Remember to take a look at the AIC'S API documentation 
def main():
    try: 
        response = requests.get("https://api.artic.edu/api/v1/artworks/search") # use the 'requests' library together with its get() function to access the AIC's API
        print(response) # <Response [200]> --> means everything went ok with our request
        response.raise_for_status() # the .raise_for_status() method checks if the referenced obj response actually worked as intended, if it doesn't then we will raise the requests.HTTPError

    except requests.HTTPError:
        print("Couldn't complete request!")
        return # exits the program

    # So, how do we access to the data inside of our 'response' obj
    # It turns out that according to the Art Institute, they are gonna send us back this data in the form of JSON
    # So, if we want to read that JSON, thankfully our 'response' obj comes with a way to do that, we can simply type 'response.json()' and that will convert our 'response' obj into a JSON obj that we could actually read.
    
    content = response.json() # creathing a 'content' obj that stores the 'response' JSON obj (use the .json() method referenced with our 'response' obj)

    # print(json.dumps(content, indent=2)) ## --> prints a more cleanly and indented json info

    for i in content["data"]: # Here, we iterate over the value of our json info for the obj content, specifically, we are iterating over the inside of the key 'data', which contains a value storing a list with multiple key-value pairs
        print(f"* {i["title"]}") # Here, we print the values of our iterated ["title"] keys

main()
