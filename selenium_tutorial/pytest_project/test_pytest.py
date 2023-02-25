import pytest

@pytest.mark.skip
def test_method():
    x = 5
    y = 2
    assert x + y == 7, "Assertion failed, Expected 7"
    assert x + y == 2, "Assertion failed, Expected 7"
@pytest.mark.skip
def test_method2():
    x = 5
    y = 2
    assert x + y == 7, "Assertion failed, Expected 7"
    assert x + y == 2, "Assertion failed, Expected 7"

def random_name():
    x = 5
    y = 2
    assert x + y == 7, "Assertion failed, Expected 7"
    assert x + y == 2, "Assertion failed, Expected 7"

def random_name_test():
    x = 5
    y = 2
    assert x + y == 7, "Assertion failed, Expected 7"
    assert x + y == 2, "Assertion failed, Expected 7"