def main():
    x = int(input("Enter a number: "))
    print(even_or_odd(x)) # need to print our returned value (strings on this case)

def even_or_odd(x):
    if ((x % 2) == 0):
        return "The number is even"
    else:
        return "The number is odd"

main()