def main():
    x = get_int() # we can assign a value for x while also calling a function without argument (that performs the while loop, user input, and error handling) so that at the end, if everything went well (triggering the else block), simply return the variable of x defined in the user input
    print(f"x is {x}")

def get_int():
    
    while(True):
        try:
            x = int(input("What's x? ")) # we also can use the 'return' keyword here instead of 'x =', eliminating the else block, and any 'return var' line of code rightafter
            # --> we can also use the 'return var' line of code here too, so that eliminating the else block
        except ValueError:
            print("x is not an integer")
        else: 
            return x # we can directly return x, which will also break the loop
main()
