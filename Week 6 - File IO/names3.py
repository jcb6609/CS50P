name = input("What's your name? ")

# we can use the keyword 'with' to close our program in a more pythonic way

with open("names.txt", "a") as file: # 'file' is the var/obj that is assigned for our open() function implementation, then we intend the line underneath
    file.write(f"{name}\n") # after this line, since we used the 'with' keyword in the previous line, our file will close

