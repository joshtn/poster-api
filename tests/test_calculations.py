import pytest
from app.calculations import add, subtract, multiply, divide

@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5),
    (5, 5, 10),
    (1, 2, 3)
])
def test_add(num1, num2, expected):
    print("testing add function")
    assert add(num1, num2) == expected


def test_subtract():
    assert subtract(9, 4) == 5


def test_multipy():
    assert multiply(3, 3) == 9


def test_divide():
    assert divide(3, 3) == 1
