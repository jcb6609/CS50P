def main():
    x = int(input("Enter a number: "))
    if is_even(x): # if the funciton is_even() with argument x returns True, then our if function holds
        print("The number is even")
    else: # if the funciton is_even() with argument x returns False, then it holds for our else
        print("The number is odd")
    
def is_even(x):
    if ((x % 2) == 0):
        return True
    else:
        return False

# alternative for is_even() body: return True if n % 2 == 0 else False
# alternative for is_even() body: return n % 2 == 0

main()