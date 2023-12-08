"""These test verify basic calculator functionality.
"""

import pytest
from pages.calculator import BasicCalculatorPage

# Set up test data
operations = [
    ("Chrome", "Add", "15", "30", "45"),
    # ("Chrome", "Subtract", "15", "40", "-25"),
    # ("Chrome", "Multiply", "8", "8", "64"),
    # ("Chrome", "Divide", "12", "3", "4")
]

# Test 1: Basic calculator operations
# Executes for each set of operation parameters in the list above
@pytest.mark.parametrize("driver, op, arg_1, arg_2, expected_result", operations, indirect=["driver"])
def test_calculator_basic_operation(driver, op, arg_1, arg_2, expected_result):
    """Tests calculator operations with valid inputs.
    """
    # Create page object
    calculator = BasicCalculatorPage(driver)

    # Execute test steps
    calculator.load()
    calculator.execute_calculation(arg_1, arg_2, op)

    # Assert results
    result = calculator.get_result()
    assert result == expected_result

# Set up test data
invalid_inputs = [
    ("Chrome", "Add", "5", "five", "Number 2 is not a number"),
]

# Test 2: Invalid input parameters
@pytest.mark.parametrize("driver, op, arg_1, arg_2, expected_error", invalid_inputs, indirect=["driver"])
def test_calculator_invalid_input(driver, op, arg_1, arg_2, expected_error):
    """Tests calculator error handling with invalid inputs.
    """
    # Create page object
    calculator = BasicCalculatorPage(driver)

    # Execute test steps
    calculator.load()
    calculator.execute_calculation(arg_1, arg_2, op)

    # Assert error message
    error = calculator.get_error_message()
    assert error == expected_error
