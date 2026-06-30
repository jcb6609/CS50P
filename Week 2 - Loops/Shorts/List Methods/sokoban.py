# Goal: To take as input an action the user might take in the game (moving up, down, left, or right),
# and storing that action inside a history (list) of actions:
def main():
    history = []

    while True:
        action = input("Action: ")
        if("Undo" in action or "undo" in action):
           history.pop() # removes the last item of our referenced list by default
           print(f"Undone: {history}")
        elif('Restart' in action or 'restart' in action):
            history.clear()  # restart the game --> use the .clear() method --> remove the entire of our list elements
            print(history)
        else:
            history.append(action)
            print(history)

main()