# remember to take a look at the documentation
# e.g. if we want to append in descending order, look up for the sorted() function documentation

names = []

with open("names.txt") as file: 
    for i in file: 
        names.append(i.rstrip())

for i in sorted(names, reverse=True): # the second argument 'reverse=True' here in our sorted() function allows us to sort in descending order (from Z to A instead of A to z)
    print(f"hello, {i}")