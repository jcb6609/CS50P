def main():
    # All of the user input is relegated to our main() function
    x = input("What's x? ")
    print("x squared is", square(x))

def square(n):
    return n * n


if __name__ == "__main__": # we do this since we want to make sure as when we import the square function for another file, we don't want main() to be automatically called itself (since that would have run our all program rather than just a desired function)
    main()