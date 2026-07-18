def main():
    x = get_int("What's x? ") # we call (caller) the get_int() function using a prompt as an argument
    print(f"x is {x}")

def get_int(prompt): # the prompt passed from the caller argument is now passed as a 'promt' arg var fro our call-ee function.
    while(True):
        try:
            return int(input(prompt)) # the 'prompt' passed var for our call-ee function (from our caller function) is now re-used 
        except ValueError:
            pass

main()

