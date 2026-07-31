names = [] # empty list, so that we have a variable where can can accumulate of our lines in our 'file'

with open("names.txt") as file: # update, if you want to read a file, the argument "r" is by default when using the open() function
    for i in file: # iterating over each line (i) of our 'file'
        names.append(i.rstrip()) # append each line to our 'names' list using the .append() method, the 'names' list as the referenced obj, and i.rstrip() as the argument (lines of our 'file') that we want to append to our referenced list 'names'

for i in sorted(names): # we iterate over our 'names' list using the sorted() method to rather just iterate directly to a sorted 'names' list
    print(f"hello, {i}")