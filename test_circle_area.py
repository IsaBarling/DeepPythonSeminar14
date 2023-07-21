import pytest
from math import pi
from circle_area import circle_area, InvalidRadiusTypeError, NegativeRadiusError

@pytest.fixture
def valid_radius():
    return 2

@pytest.fixture
def invalid_radius():
    return -2

def test_circle_area_valid(valid_radius):
    assert circle_area(valid_radius) == pi * valid_radius ** 2

def test_circle_area_zero():
    assert circle_area(0) == 0

def test_circle_area_float():
    assert circle_area(2.5) == pi * 2.5 ** 2

def test_circle_area_invalid(invalid_radius):
    with pytest.raises(NegativeRadiusError):
        circle_area(invalid_radius)

def test_circle_area_complex():
    with pytest.raises(InvalidRadiusTypeError):
        circle_area(5 + 2j)

def test_circle_area_string():
    with pytest.raises(InvalidRadiusTypeError):
        circle_area("five")

def test_circle_area_list():
    with pytest.raises(InvalidRadiusTypeError):
        circle_area([16, 22])

def test_circle_area_list_single():
    with pytest.raises(InvalidRadiusTypeError):
        circle_area([42])

def test_circle_area_bool():
    with pytest.raises(InvalidRadiusTypeError):
        circle_area(True)

