# read the 'alice.txt' file, separate it by chapters, and put each of those chapter info into a new file(s). 
def main():
    with open("alice.txt", "r", encoding="utf-8") as f: # if charmpa error, use the 'encoding="utf-8"' argument fot the open() function
        # contents = f.read() ## the .read() method is useful to read all our file at once
        contents = f.readlines() ## the .readlines() method will return us not just one big string but rather a list of individual lines in my (referenced) file

    # Note: If the line in your text file ends with a line break, .readline() reads and includes that \n as part of the returned string.
    # print(contents[0]) # prints the first element of our 'contents' list for each of our lines/elements in our file, where 'contents[0]' represents the first line of our file (first element of the list)

    # chapter 1 begins on line 53 and ends at line 273
    chapter1 = contents[52:272] # stores the info from the first chapter inside of a big list; the lists contains each line (each line represents an element in our list) from the first chapter, so then finally saving the list into a var named 'chapter1'

    # how could I write this 'chapter1' lines/list's elements into a new file? --> open a new file:
    # Note: Here we cannot use content from inside the previously opened impementation
    with open("chapter1.txt", "w") as w: # Recall that if the desired open file does not exist, we will create it rather than opening it
        # w.write("Chapter I.") # the .write() method is good for writing a single string to a file 

        # but our 'chapter1' list doesn't have a single string but rather a list of strings, so we could use instead the .writelines() method:
        w.writelines(chapter1) # pass into our .writelines() method the lines we want to write, in this case, the list 'chapter1' containing a list of string elements, each element being a line from our 'alice.txt' file

main()