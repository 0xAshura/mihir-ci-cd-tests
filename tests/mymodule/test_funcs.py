import pytest

from myapp.mymodule.funcs import *


@pytest.mark.easy_operation
def test_add():
    # This test will fail.
    assert add(4, 8) == 12

@pytest.mark.easy_operation
def test_subtract():
    assert subtract(3, 6) == -3

@pytest.mark.difficult_operation
def test_multiply():
    assert multiply(4, 5) == 20

@pytest.mark.difficult_operation
def test_divide():
    assert divide(56, 8) == 7

@pytest.mark.easy_operation
def test_add_student_id():
    # New test case using the last two digits of the student ID as the expected output
    assert add(42, 42) == 84  # Replace 42, 42 with appropriate values if needed
