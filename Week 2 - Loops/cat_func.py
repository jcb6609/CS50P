def main():
    n = get_number() # assign the returned value of the function get_number() to the var n
    meow(n)

def get_number():
    n = int(input("Enter a positive number: "))
    while(n < 0):
        print("Incorrect. Not a positive number")
        n = int(input("Enter a positive number: "))
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()