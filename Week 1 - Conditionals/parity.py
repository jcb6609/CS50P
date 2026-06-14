# Is a number even or odd?
x = int(input("Enter a number: "))

y = x % 2

if(y == 1):
    print("The number is odd")
else:
    print("The number is even")