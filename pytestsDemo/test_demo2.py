import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_third_program():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"


def test_forth_program():
    a = 4
    b = 6
    assert a+2 == b, "Addition do not match"
