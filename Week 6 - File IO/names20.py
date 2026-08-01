import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students5.csv", "a") as file:
    # with DictWriter() we need to give it a hint a to the order in which those columns are when writing it out so that, subsequently, they could b read, even if those orderings change, therefore we use a second argument wit keyword assignation 'fieldnames=' with a list of these alr established row names identifiers (in 'students5.cv' the alr established columns 'name,home' (which are the top column values of our file))
    writer = csv.DictWriter(file, fieldnames=["name", "home"]) # function DictWriter() 'csv.DictWriter()' from the csv library with 'file' argument is going to open our file but rather than writing a row as the list [name, home] for the writerow() method, we are gonna now output an actual dictionary 
    # because we passed our 'fieldnames=["name", "home"]' argument, we now ensure that the library knows exactly which column contains 'name' or 'home' (from our file as 'name,home') respectively
    writer.writerow({"name": name, "home": home})