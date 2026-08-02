import csv
import numpy as np
from PIL import Image

# We want now not just to display the values from 'views.py' but to create a new csv that has a part of it a new column with the brightness data

def main():
    # --> open 2 files at once, one for reading and one for writing
    # Note: if any file creations with extra \n, then use the argument 'newline=""':
    with open("views.csv", mode="r", encoding="utf-8") as views, open("analysis.csv", "w", newline="", encoding="utf-8") as analysis: # if coding error 'charmap' appears, remember to use 'encoding="utf-8"'
        reader = csv.DictReader(views)  
        # we need to specify the file's headers for our new csv file, which was done in te previous line of code by using the assignation keyword 'fieldnames=...', were we can specify ur own headers in the way of a list (e.g. '=["id", "english_name", ...]') or also by assignating a reader with a previosuly assigned/open file with the headers we might want to use again (e.g. 'reader.fieldnames' with .fieldnames being an attribute and 'reader' its reference obj); also, we can assign a new fieldname/header by adding at the end of 'reader.fieldnames' an additional list-like info with the element/name for the new column/header using the + symbol (e.g. '=reader.fieldanames + ["new_header"]')
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"]) # the function DcitWriter() can take as input dictionaries and write them each as their own row in our new 'analysis.csv' file; the function can also as its second argument a 'fieldanmes' input so specify some headers for our new file; here the DictWriter iplementation is saved for the 'writer' obj
        # let's write the info for the new header (column) "brightness"
        writer.writeheader() # updates first the headers of our new file thanks to the .writeheader() method and its reference the 'writer' obj, if runned only updating at this point, we will see the new file 'analysis.csv' with its respective headers

        # At this point, we alr have our headers, but we need our rows
        for i in reader:
            # we can avoid all the consquent lines back in 'views2.py' by simply assigning our calculate_brightness() function implementation directly into our alr defined new column/header 'brigthness'; recall we can also use the round() function here as an outer function for our calculate_brightness() function (the first argument of our round() function call since it returns the brightness integer)
            i["brightness"] = round(calculate_brightness(f"{i["id"]}.jpeg"), 2)
            writer.writerow(i) # just writing the whole row with our previous changes for the "brightness" header/column


def calculate_brightness(filename): 
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()