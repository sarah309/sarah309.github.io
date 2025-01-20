# Python

from calculate_circle import calculate_circle_area
import pytest
from pytest import approx

def test_calculate_circle_area():
    assert calculate_circle_area(1.0) == approx(3.14159, abs = 0.001)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])