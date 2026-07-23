# API's get more powerful when you introduce parameters
import requests 
import json

def main():
    try: 
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": "Monet"} # parameter argument / search route; filters our get() by passing a dictionary with the key "q": as for query (indicated by the AIC's API webpage) and its value "Monet" as the filter for our query search only for that author
            )
        print(response) 
        response.raise_for_status() 

    except requests.HTTPError:
        print("Couldn't complete request!")
        return
    
    content = response.json() 
    

    for i in content["data"]: 
        print(f"* {i["title"]}") 
main()
