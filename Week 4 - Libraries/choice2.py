from random import choice # Loads the function's name 'choice' from the 'random' module

# therefore, we do not longer need to specify which choice function we need
seq = ["Heads", "Tails"]

coin = choice(seq)
print(coin)

# We needed to specify the name of the module as a reference for the choice() function since in this way we can specify what type of function are we working with, in this case, the choice() function from the 'random' module.
# Sometimes, to avoid conflict with let's say other modules with matching name for their functions, it is recommended to reference the module from where its specific function comes from.