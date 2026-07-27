# we need to create an additional file (__init__.py) in our folder to use the function of a file from another folder, so that Python can treat that folder not just as a module but as a package (Python module organized inside of a folder)
# we can now run pytest on our folder 'test' (since we have only the two files test_hello.py and __init__.py) --> must be runned (from our terminal) outide of the test folder loc
from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David"