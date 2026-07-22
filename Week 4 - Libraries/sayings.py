def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello {name}")

def goodbye(name):
    print(f"goodbye {name}")

if __name__ == "__main__":
    main() # If any function from this file is gonna be used in another file, we have to handle our main() function caller with the previous line technique