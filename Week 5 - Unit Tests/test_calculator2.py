from calculator import square

def test_square(): # Name convention --> test_functiontotest():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
    # assert square("cat") == (raise an error)