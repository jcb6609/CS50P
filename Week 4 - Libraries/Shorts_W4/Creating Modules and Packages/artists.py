import requests

def get_artists(query, limit): # In order to use the get_artworks() function in other file, we need to put this function inside its own module
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/agents/search",
            {"q": query, "limit": limit}
            )
        response.raise_for_status()

    except requests.HTTPError:
        return []

    content = response.json()
    return [i["title"] for i in content["data"]]