# we can read our 'file' info actually not iterating and printing but combining everything into one thing:

with open("names.txt", "r") as file:
    for i in file: # iterating over our 'file' obj allows us to iterate over every line in our 'file', one at a time, and on each iteration, updating the value of this variable to be Harmione, then Harry, then Ron, then Draco, etc
        print("hello,", i.strip()) # notice that here we do not need our f-string since we are directly reading/printing from our 'file''s obj info, instead  we can simply use the .rstrip() method and use the iterable variable as its reference to display each of our 'file''s lines while helping on the append/display/line format 

        # *this approach is not recommendable* since now, if let's say we want to sort our info, then we will have to step back and get some o=ideas from our prebious codes