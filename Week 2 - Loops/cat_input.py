n = int(input("Enter a positive value: "))

while(n < 0): # while loop to check user input
    print("Error. Not a positive value.")
    n = int(input("Enter a positive value: "))

for _ in range(n):
    print("meow")

"""
We can also code the while loop as:

while True:
    n = int(input("..."))
    if(n > 0):
        break
"""