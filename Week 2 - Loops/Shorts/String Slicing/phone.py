# Store a phone number as a string
def main():
    # first xxx --> area code, last xxxx --> security
    phone = "814-384-1568"
    print(phone[:3]) # print the first three digits of our 'phone' string
    print(phone[8:]) # print the last four digits of our 'phone' string

    # If the characters you want are always at the end of our string, we can get them using a special indexing:
    print(phone[-4:])

main()