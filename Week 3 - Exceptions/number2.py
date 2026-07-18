# The while loop always keeps running until the else with break body code happens
while(True):
    try:
        x = int(input("What's x? "))
        # --> We can also use the 'break' keyword here and get rid of the else block
    except ValueError: # when the exception happens, the else block doesn't run
        print("x is not an integer")
    else: # if the ValueError is not triggered (the user prompt works), then...
        break # the keyword 'break' allows us to get out of the while loop

print(f"x is {x}")

"""
This code is basically a mix between a try-except-else block with a while loop,
which allows us to handle errors indefinitely until the user prompts a not except-block error handler!
"""