# If you find yourself in this kinda of copy-pasting situation, you might think of using a loop (e.g. for loop)
# Let's make a guest list and write a for loop to write a letter for each person on that guestlist

def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi", "Bowser"]
    # 'for name in names:', where name is the iterative variable, also works , where the iterative variable represents each list's obj rather than eahch list's index obj
    for i in range(len(names)): # range() funciton will give us a list of numbers from 0 up to but not including the value we pass in as input to range (range's argument)
        print(write_letter(names[i], "Princess Peach")) # the argument 'names[i]' can also only 'name' if we use the 'for name in names:' for loop declaration instead 

def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {receiver}, 

        You are cordially invited to a ball at
        Peach's Castle this evening, 7:00 PM.

        Sincerely,
        {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+ 
    """

main()

