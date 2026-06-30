SHOWS = [
    " Avatar: the last airbender",
    "Ben 10",
    "Arthur",
    " Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy Neutron ",
    "the Proud family"
]

def main():
    cleaned_shows = []
    for i in SHOWS:
        # print(i.capitalize()) # use the .capitalize() method to capitalize ONLY the first letter of our referenced/iterated item(s)/show(s)
        # print(i.title()) # .title() method titlecase our referenced/iterated item(s)/show(s)
        # print(i.strip()) # .strip() method get rids of the spaces on either end of our referenced/iterated item(s)/show(s)

        # Recall we can refer multiple methods for the same obj (chain String methods together):
        # --> print(i.title().strip())
        cleaned_shows.append(i.title().strip()) # append each new String to the empty list 'cleaned_shows'
    print(f"{cleaned_shows}\n") # print outside the for loop to avoid printing every iteration!
    print("We can also print using the .join() method:", end='\n\n')
    print(', '.join(cleaned_shows))
main()