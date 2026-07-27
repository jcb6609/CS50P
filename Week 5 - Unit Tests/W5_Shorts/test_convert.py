import pytest
from convert import convert

def test_conversion():
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000


# does 'convert()' raise a TypeError when given an input of the wrong type (check convert.py)
def test_error():
    with pytest.raises(TypeError):
        convert("1")

def test_float_conversion():
    # We can adjust the level of tolerance:
    # Advice --> make sure that we get a value within the desired particular tolerance --> set your tolerance first and then make sure your code is giving you the right value

    assert convert(0.001) == pytest.approx(149597870.691, abs=0.1) # the approx() function from pytest allows some kind of tolerance for our result (argument); the second argument 'abs=0.1' also provides tolerance by setting a tolerable margin error of 0.1 (hight tolerance) above and below our function's output number: Lowest acceptable answer: 149597870.691 - 0.1 = 149597870.591 / Highest acceptable answer: 149597870.691 + 0.1 = 149597870.791

    # 1e-2 --> 0.01
    assert convert(0.001) == pytest.approx(149597870.691, abs=1e-2)

    # tolerance not supported --> assert convert(0.001) == pytest.approx(149597870.691, abs=1e-3)