# Let's create our own gif
# take as input two or even more image files and then generate an animated GIF from them by essentially creating this animated GIF by toggling back and forth endlessly between those two images
# this program takes as input two command line arguments, the names of the files
import sys # to use sys.argv
# Note: If the libraries do not work, try changing the Python version to 3.13 (64-bit)
from PIL import Image # from 'PIL' library import support for 'Image' specifically 

images = [] # empty list to store images

for i in sys.argv[1:]: # iterate over the 'sys.argv' list starting from the fisrt element to the last element of the list (omitting the first element from the list) --> ignores the first element since it contains by default the name of our program when running it from the command-line
    # the 'PIL' library is essentially going to open that/those image files from 'sys.argv' in a way that gives me a lot of functionality for manipulating it, like animating
    image = Image.open(i) # setting a var 'image' equal to the function open() (which comes from the 'PIL' package) referenced to the 'Image' function (imported from the 'PIL' package), and passing each iterated list's value as 'i' (cammand lines from our command prompt, which will essentially be our images)
    images.append(image) # use the .append() method with the 'images' list as its reference, to append all the 'image' objects (the .append() method argument) from the previous line to the 'images' list

images[0].save( # save the first element from the 'images' list with the '.save()' method with the following arguments: 
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
) 

# '.save()' arguments:
"""
* "costumes.gif" --> pass the final name of the file we want to create
* save_all=True --> save all of the frames passed (the elements/files given from 'sys.argv')
* append_images=[images[1]] --> append the the second element for the second image/element 'images[1]' in our 'images' list
* duration=200 --> duration of 200 miliseconds for each of our frames passed
* loop=0 --> loop our gif an infinite number of times 
"""

# after running (and putting in the command prompt our frame files) we can now open our new gif 'costumes.gif' writing in the command prompt 'code costumes.gif'