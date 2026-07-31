# the new csv treated here 'students2.py' was modified so that, for example, now one of the lines in our file looks like: 'Harry,"Number Four, Privet Drive"'; here, the quotation marks are important for the second column since if they were not there, csv would treat the other comma inside as another column, which is not the case here
import csv

students_list = []

# taking another csv, with lines such as: 'Harry,"Number Four, Privet Drive"' we need to look up for alternative solutions to run our program
with open("students2.csv") as file: 
    reader = csv.reader(file) # function reader() from the csv library 'csv.readeer()' with our 'file' as its argument, whose purpose in life is to read a csv file for you and figure out where are the commas, where are the quotes, where are all the potential corner cases and jusr eal with them for us
    for i in reader:
        students_list.append({"name": i[0], "home": i[1]}) # i[0] --> first column, i[1] --> second column (recall for our csv file, each comma separator represents a new column)
    # insted of 'for i in reader:', since we now we only have two columns in our csv file, we could also do:
    """
    for name, home in reader: # since we now we only have two columns
        students_list.append({"name": name, "home": home})
    """

for i in sorted(students_list, key=lambda students_dict: students_dict["name"]): # lambda's structure --> 'lambda students_dict: students_dict["name"]' --> 1). Keyword 'lambda', 2). passed argument 'students_dict' follewed by ':', 3). after the ':' then we set the return body of our lambda function (no 'return' keyword needed) by only typing 'students_dict["name"]'
    print(f"Yes, {i['name']} is from {i['home']}")

