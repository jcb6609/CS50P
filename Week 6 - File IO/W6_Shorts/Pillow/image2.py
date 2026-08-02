from PIL import Image 
from PIL import ImageFilter # access image filter from the pillow 'PIL' library, it allows us to apply different image filters

def main():
    with Image.open("in.jpeg") as img: 
   
        img = img.rotate(180)
        # img = img.filter(ImageFilter.BLUR) ## method .filter() with our 'img' obj as its reference and as its argument the code 'ImageFilter.BLUR' to apply the filter '.BLUR' while also updating this coe implementation by saving it inside of our (repeated) 'img' obj
        img = img.filter(ImageFilter.FIND_EDGES) # another filter (.FIND_EDGES)
        img.save("out3.jpeg")


main()