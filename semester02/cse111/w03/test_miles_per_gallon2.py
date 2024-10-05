from miles_per_gallon import calculate_miles_per_gallon
import pytest

def test_calculate_miles_per_gallon():
    assert calculate_miles_per_gallon(4000, 6000, 40) == 50

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])