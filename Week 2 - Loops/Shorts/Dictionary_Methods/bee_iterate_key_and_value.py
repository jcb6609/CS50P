WORDS = {
    "PAIR": 4,
    "HAIR": 4,
    "CHAIR": 5,
    "GRAPHIC": 0 # --> Winning word
}

def main():
    print("Welcome to Spelling Bee!")
    # How we could ITERATE over each KEY AND VALUE in our dictionary
    # key, value --> counter/interation variables
    for key, value in WORDS.items(): # .items() method --> returns back a set where it actually gives both the key and the value of our referenced dictionary obj
        print(f"key {key} was worth {value} points")

main()