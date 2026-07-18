try: 
    x = int(input("What is x? ")) # could produce a ValueError

except ValueError: # If the error ValueError happens, then we trigger the excpet keyword (trigger the exception) followed by the type of error we want to handle (we catch the ValueError)
    print("x is not an integer")

else: # if the exception is not triggered, then we simply use our else, so that we can handle the NameError right after andling our ValueError
    print(f"x is {x}") # --> not handled correctly --> producing NameError
