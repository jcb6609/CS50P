from calculator import square
import pytest # the pytest library allows us to use a function raises that allows us to expect an exception to be raised

# we now instead of having a big test function, let's break down my test into different categories

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError): # exception is raised --> then all other function run (which means that yesour program runs correctly for the test check, but out original calculator program as it is it not correct)
        square("cat")

# summary: ====================== 2 failed, 1 passed in 0.30s ======================
# summary: =========================== 3 passed in 0.16s ===========================