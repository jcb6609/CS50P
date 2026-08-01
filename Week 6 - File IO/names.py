names = [] # emtpy list

for _ in range(3):
    names.append(input("What is your name? "))

for i in sorted(names): # the sorted() function goes through a sorted version of the 'names' list
    print(f"hello, {i}")