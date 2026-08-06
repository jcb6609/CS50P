import re

locations = {
    "+1": "United States and Canada",
    "+62": "Indonesia",
    "+505": "Nicaragua"
}

def main():

    number = input("Number: ").strip()

    # country codes hhave from 1 up to 3 digits
    # country codes come before the number, theparated by a space
    # country codes always start with a '+' symbol
    # numbers have 10 digits and three '-' as follows: ddd-ddd-dddd
    if match := re.search(r"^(\+\d{1,3})\s\d{3}-\d{3}-\d{4}$", number):
        # extract a portion of our regex content:
        country_code = match.group(1) # e.g. country_code = "+1" --> YES, we get back a string
        # Use the country code extracted (as our dictionary 'locations' key) to access the determinate key's value in our dictionary
        print(locations[country_code])
    else:
        print("Invalid")

# Done above:
# Let's try to show the user, from what country is the country name
# use regex to dynamically (pattern searching rather than char per char searching) capture the portion of the content we are looking for (country digit)

# We can also define our own grouped variable inside of the regex check using '?P<group_name>(group)':
    # re.search(r"^?P<country_code>(\+\d{1,3})\s\d{3}-\d{3}-\d{4}$", number):
        # country_code = match.group("country_code") ## tehn, inside the .group() method, pass as its argument the alr defined name of our grouped regex in quotation marks

main()