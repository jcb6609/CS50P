name = input("What's your name? ")

# let's save this value of the person's name that's just been typed in to a file --> use the open function
# file = open("names.txt", "w") # the argument of the open() function '("name.txt", ...)' is the name of the file I would like to store my 'name' var info in; the second argument (..., "w") it's going to tell the open() function to open the file (first argument) in a way that is going to allow me change the content (if the first argument does not exist, then open it's going to create that fille for us), subsequently, we can store our open() function as a var, in this case called 'file'
file = open("names.txt", "a") #  "a" (a from append, to add/append (our info each time we run our proram and make a chnage); appending needs of a line separator (new line), otherwise the info in our txt file is gonna appear as "concatenated"
file.write(f"{name}\n") # the .write() method allows us to write our 'name' var info (as an argument of .write()) into our 'file' obj (refernced to .write()) which is contains the open() function implementation from the previous line. Here, when using the .write() method, we can use an f string to help our previous append implementation to separate each of the new lines (with a line separator \n) of info each time we run our code and add to the txt file
file.close() # the method .close() closes the referenced obj 'file'

# after writing our 'name' var into name.txt (which we created since it didn't exist before), then we can open this file in the terminal writing 'code names.txt'

"""
Unfortunately, "w" (the second argument in te open() function ) is a little dangerous,
Not only it will create the file for you, it will also recreate the file for you every time you open the file in that mode.
So, if you open the file once and write Hermione that works fine, but if you do it again for Ron or Harry, the code is working but each time is opening the file and recreating it with brand-new contents.
Ideally, we want to be appending each of those names to the file, and not just clobbering-- that is, overwriting the file each time.
How to fix this? First step, remove the previous made txt file with the command 'rm names.txt', then go back to the code, change the "w" (second argument from open() function) for an "a" (a from append, to add/append our info each time we run our proram and make a chnage) 
Since we now are appending to the file, then we need to provide space for each of our new program run, since we are gonna be adding info in a "concatenated" way
"""