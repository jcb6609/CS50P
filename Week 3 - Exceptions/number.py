try: 

    x = int(input("What is x? "))

    print(f"x is {x}")

except ValueError: # If the error ValueError happens, then we trigger the excpet keyword (trigger the exception) followed by the type of error we want to handle (we catch the ValueError)
    print("x is not an integer")

# ValueError if we type something that is not an integer, e.g. 'cat'
# ValueError: invalid literal for int() with base 10: 'cat'
# What we want to do is write our code with error-handling in mind