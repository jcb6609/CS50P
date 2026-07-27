# test to check the square() function form the file calculator.py
from calculator import square

def main():
    test_square()


def test_square():
    try:
        assert square(2) == 4 # no 'if(...)', just 'assert'
    except(AssertionError):
        print("2 squared was not 4")
    try:
        assert square(3) == 9 # error happens if 'assert' is False
    except(AssertionError):
        print("3 squared was not 9")
    try:
        assert square(-2) == 4
    except(AssertionError):
        print("-2 squared was not 4")
    try:
        assert square(-3) == 9
    except(AssertionError):
        print("-3 squared was not 9")
    try:
        assert square(0) == 0
    except(AssertionError):
        print("0 squared was not 0")


# No output --> everything went through without errors

if __name__ == "__main__":
    main()