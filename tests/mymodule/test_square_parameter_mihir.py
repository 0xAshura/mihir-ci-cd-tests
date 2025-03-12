import pytest
from myapp.mymodule.funcs import *

@pytest.mark.difficult_operation
def test_calculate_square_perimeter():
    # New test case using the last two digits of the student ID as the expected output
    result = calculate_square_perimeter(21)
    print(f"Result of calculate_square_perimeter(21): {result}")
    assert result == 84