# the new csv treated here is 'students3.py'
import csv

students_list = []

with open("students3.csv") as file: 
    # if we instead use a dictionary reader, we can use our csv file even more flexibly
    reader = csv.DictReader(file) # the DictReader() function, from the csv library and with argument 'file', will now iterate over the file top to bottom loding in each line of text not as a list of columns but as a dictionary of columns, it returns dictionaries, here, one at a time

    for i in reader:
        # accessing dictionary's values: i["..."]
        # here, "name", and "home" are at the top of our 'students3.csv' file as 'name,house', therefore making them the keys of our iterations, which we can access by saying 'i["name"]' and 'i["home"]'
        # --> for the "name" key (top of our file's columns), store a value 'i["name"]' that enters the 'reader' dictionary for the next row (after 'name,house' which are our keys) and access the value of that row for our iteration, in this case for the first iteration in the line 'Harry,"Number Four, Privet Drive"', it stores Harry.
        # Note: If we reverse the values of 'students3.csv' (or even add another column) our code will still work
        # Also, notice that here we can simply do: 'students_list.append(i)' because DictReader() already returns a dictionary with top column info in our file as 'name,home'
        students_list.append({"name": i["name"], "home": i["home"]})
        # what is getting appended to our list: 
        # {"name": "Harry", "house": "Number Four, Privet Drive"}

# tip -> compare i and stu_dict:
for i in sorted(students_list, key=lambda stu_dict: stu_dict["name"]):
    print(f"Yes, {i['name']} is from {i['home']}")

