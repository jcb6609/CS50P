# this version is more testable.

def main():
    name = input("What's your name? ")
    print(hello(name))

def hello(to="world"): # if no var is passed from the caller function hello(), then 'to=world'
    return f"hello, {to}"

if __name__ == "__main__":
    main()