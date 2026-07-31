# If we just want to sort our 'file', we can actually do this even more simply:

with open("names.txt") as file:
    for i in sorted(file): # We directly use the sorted() function in our for loop for the 'file' obj
        print("hello,", i.rstrip())

# REMEMEBER that if we want to make further chnage to our info in 'file' this is not a good approach