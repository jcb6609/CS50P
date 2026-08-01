# let's take a pic on how we might write a csv too, 
# how can we keep adding to this file? 
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students4.csv", "a") as file: # opening our file in opne() with argument append as "a" (which avoids overwriting our file everytime we make a change)
    writer = csv.writer(file) # writer() function 'csv.writer()' from the csv module, and it takes as its sole argument our 'file' variable there 
    writer.writerow([name, home]) # function writerow() with obj 'writer' referenced --> we are going to pass into writerow() the line that we want to write to our file, in this case a list [] with elements previosuly user-defined 'name' and 'home' 
    # Note: a comma would help us (and the user) while writing the var info we are going to write in our file, since when using commas as for example 'home = cota, Colombia', our csv file will automatically help with the comma separation and will add quotation marks in our info '"cota, Colombia"' inside of our csv file
    # Note: Each time we run, we hae to place our cursor into the next (empty) line, were we want to write our info, besides not having any other empty line underneath the empty line to fill with info.
    # Here, the library took care of not only writing each of those rows, per the function's name, it also handled the escaping of any strings that themselves contained a comma like Harry's home