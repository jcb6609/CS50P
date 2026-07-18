def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while(True):
        try:
            return int(input("What's x? "))
        except ValueError:
            pass # handle an exception in Python, but you want to 'pass' on doing anything with it

main()