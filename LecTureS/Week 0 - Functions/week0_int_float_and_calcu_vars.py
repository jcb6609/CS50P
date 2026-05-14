x = input("Insert the value of x: ") # user input always deals with text/strings
y = input("Insert the value of y: ") # user input always deals with text/strings
z = int(x) + int(y) # use the int() function to convert string numbers to int values
print(z)

# we can nest float()/int() inside the function input() such as int(input()) receives user-input and then the contained string variable is converted to an int data type
x = float(input("Insert an x float value: ")) # nested function call (in "input()" then out "int()")
y = float(input("Insert a y float value: ")) # nested function call (in "input()" then out "int()")

z = round(x + y) # the round() function rounds a numeric value to a specified number of decimal places (default to 0)
print(f"here, x + y rounded to 0 decimal places is {z}")

z = round(x + y, 1) # here, the number of decimal places to round to is 2
print(f"here, x + y rounded to 2 decimal places is {z}")

# we can also organize everything in only one line:
z = (int(input("number1 to sum: ")) + int(input("number2 to sum: ")))
print(f"{z:,}") # "print({variable:,})" formats a variable's value with comma separators (e.g. 1000 -> 1,000)

x = float(input("Another float value for x: "))
y = float(input("Another float value for y: "))

z = (x / y)
print(f"with all decimals: {z}")
print(f"with exactly 2 decimal places: {z:.2f}") #"print({variable:.2f})" formats a variable's value with exactly 2 decimal places.

# -->Note: We can ONLY concatenate strings using "+"