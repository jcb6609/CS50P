# Lists vs Dictionaries:
"""
Lists: 
    - Lists are an array of objects that are stored in sequential order.
    - They are represented using [] (square brackets).
    - Unlike many other languages, a list can contain a mixture of different data types.

Dictionaries:
    - Similar to lists in that they store an array of objects,
    - but these object are accessed using keys,
    - and the objects we are accessing is called value.
    - These are represented using {} (curly braces)

# Comprehension: 
    - Quick way to build up a list or a dictionary from data you already have

# List Comprehension:    
    - Processes data to return a list of values afterwards.

# Syntax of a List Comprehension:

    [some_function(x) for x in original_list if certain_condition]

    - The first thing that we put inside these square brackets is 
      what we want to return after processing each data item.
    - by looking at the syntax inside the square brackets, 
    - Python is able to determine that this is a list comprehension.
"""

# Exmaple 1: Square all numbers in a list
def main1():
    list = [1, 6, 4, 2, 9, 15, 5]
    squared_list = [(i * i) for i in list]

    print(squared_list)

main1()

"""
Remember we can also do 'Example 1' using a separate for loop:

list = [1, 6, 4, 2, 9, 15, 5]

# loop through a list's items
for i in list:
    print(i * i)

OR
    
list = [1, 6, 4, 2, 9, 15, 5]

# loop through a list's indexes numbers rather than its actual items.
for i in range(len(list)): 
    print(list[i] * list[i])

"""

# Exmaple 2: Return only even values
def main2():
    list = [1, 6, 4, 2, 9, 15, 5]
    even_list = [i for i in list if ((i % 2) == 0)]

    print(even_list)
    
main2()

"""
Remember we can also do 'Example 2' using a separate for loop:

list = [1, 6, 4, 2, 9, 15, 5]

# loop through a list's items
for i in list:
    if((i % 2) == 0):
        print(i)

OR
    
list = [1, 6, 4, 2, 9, 15, 5]

# loop through a list's indexes numbers rather than its actual items.
for i in range(len(list)): 
    if((list[i] % 2) == 0):
        print(list[i])

"""


# Dictionary Comprehensions:
"""
Syntax of a Dictionary Comprehension:
    
    {key: value for iterate_list_or_dict if conditional}

    - A Dictionary Comprehension is surrounded by {} (curly braces).
"""

# Example 1: Create a dictionary of numbers and their squared values
def main3():
    squared_dict = {i: (i * i) for i in range(0, 11)} # range(start, stop, step)
    print(squared_dict)

# Example 2: Dict with only even keys and values
    even_squared_dict = {i: i for i in squared_dict if ((i % 2) == 0)}
    print(even_squared_dict)
main3()