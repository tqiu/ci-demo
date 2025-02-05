from example import add, multiply


def test_add():
    assert add(1, 2) == 3
    assert add(3, -2) == 1


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(3, -4) == -12