import pytest

def test_method_2():
    x = 5
    y = 2
    assert "Tom" == "Tom", "Assertion failed, Expected 7 but was" + str(x + y)
    assert x + y == 2, "Assertion failed, Expected 7"