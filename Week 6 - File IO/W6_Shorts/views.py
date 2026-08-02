# Our goal is to read 'views.csv' and do a bit of image analysis about how bright or not each of the photos (check folder) are
import csv
import numpy as np
from PIL import Image

def main():
    # Adding encoding="utf-8" forces Windows to read the file exactly how it was written,  When you use open() without specifying an encoding on Windows, Python automatically uses an old Windows-specific standard called CP1252 (or "charmap"), generating a an error UnicodeDecodeError since CP1252 did not understand our file.
    with open("views.csv", mode="r", encoding="utf-8") as file: # argument "r" as defalt for open()
        reader = csv.DictReader(file) # DictReader() function from the 'csv' library taking as input our file named 'file' (as defined in the previous line) and saving all this implementation into a reader obj; the DictReader() function allows us to take a file and read each row of it as a dictionary
        for i in reader: # where i means row, every roe is a dictionary 
            # print(i["id"]) # prints all the "id" key's values, which are also the names of our image files (check folder)
            brightness = calculate_brightness(f"{i['id']}.jpeg") # what we are looking here is our file's names (images) for each iteration, where the id column (f"{i['id']}.jpeg") has the names of these files, which are also their id's, so that each of our images/files can be passed to the 'calculate_brightness(filename)' function to return the brightness of each iterated image/file
            print(round(brightness, 2)) # prints the returned brightness values for eah of our iterated column/key's values/images files using an inner round() function to 2 decimal places 'round(brightness, 2)'



def calculate_brightness(filename): # this function takes as an input a file name, and returns to us 0 to 1 (in a 0 to 1 scale) how bright or not bright (dark) the image is, with 1 being brightest (completely black) and 0 being darkest (completely dark)
    with Image.open(filename) as image: # we open each image/file name 
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness



main()