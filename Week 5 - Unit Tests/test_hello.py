# asserts --> to test arguments into functions and return values they're from, not testing side effects
# e.g. 'hello("David") == "hello, David"'

# --> We want to write nice-simple test code
from hello import hello

def test_default():
    assert hello() == "hello, world" # Not working (if) we are not returning a value back in our imported hello.py

def test_argument():
    assert hello("David") == "hello, David"