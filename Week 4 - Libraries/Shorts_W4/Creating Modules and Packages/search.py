import requests
import json
from artwork import get_artworks
from artists import get_artists

from museum.artists import get_artists # to specify a function from our package
# import artwork ## --> if function used, need to specify as a reference (when calling the function) from what module comes from, in this case 'artwork'
# import artists ## --> if function used, need to specify as a reference (when calling the function) from what module comes from, in this case 'artists'

def main():
    artwork = input("Artwork: ")
    artworks = get_artworks(query=artwork, limit=3)
    for i in artworks:
        print(f"* {i}")

    artist = input("Artist: ")
    artists = get_artists(query=artist, limit=3)
    for i in artists:
        print(f"* {i}")

main()

# Package: Collection of multiple modules; we can create one by making a folder and putting inside of it the file '__init__.py' (check the museum folder)