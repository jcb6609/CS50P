# How do we read the info from our 'names.txt' file?

with open("names.txt", "r") as file: # second argument in open() as "r" for read mode
    # A way to read all of the lines from the file at once will be:
    lines = file.readlines() # the .readlines() method reads all the lines from our 'file' and stores them in a variable called 'lines', which will be essentially a list

    for i in lines: # we iterate the list 'lines' that we defined before for reading/returning in a list the content(s) of our 'file' 
        # print(f"hello, {i}", end='') ## since we previously defined our writing proram to have a line separator \n, our print will basically add a new \n as default, making our final info display with two \n if not corrected
        # alternatively we can do this:
        print(f"hello, {i}", i.rstrip()) # the .rstrip() method strips off the end of the line the actual new line itself, so that print is handling the printing of everything 