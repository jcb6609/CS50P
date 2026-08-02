# we can use the pillow library to manipulate images and, for example, rotate them
from PIL import Image # from the pillow library import a particular class (template) named 'Image'

def main():
    with Image.open("in.jpeg") as img: # Use the 'Image' class imported from 'PIL' to use the open() function and open the desired image file, whcih would be the argument for the open() function, finally returning an image obj stored as the var 'img'
    # img.close() ## when we open a file, it's a good practice to close it, using the var 'img' (where we stored our opened image) referenced to the .close() method --> no need when using 'with' and 'as' from the previous code line
        # print(img.size) # inside print(), our 'img' obj is referenced to the .size property --> gives us acess to the size of our 'img' obj in pixels
        # print(img.format) # inside print(), our 'img' obj is referenced to the .format property --> will show us the format of the image, like what file type it is
        img = img.rotate(180) # rotate our image 180 degrees using our 'img' obj referenced to the .rotate() method and its argument 180 as an integer, finally save the implementation in another obj named 'img'
        img.save("out.jpeg") # saving our modified (rotated) 'img' obj (reference) by using the .save() method with the argument of the new name of the file we have to update/create (in this case '"out.jpeg"')


main()