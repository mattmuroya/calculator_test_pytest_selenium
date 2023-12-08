"""These test verify basic calculator functionality.
"""

import pytest
from pages.calculator import BasicCalculatorPage

# Set up test data
# The test will be run for each set of values in the list;
# Arguments: browser, operation, arg_1, arg_2, expected result, inputs are valid

test_data = [
    ("Chrome", "Add", "15", "30", "45", True),
    ("Chrome", "Add", "5", "five", "Number 2 is not a number", False),
    # ("Chrome", "Subtract", "15", "40", "-25", True),
    # ("Chrome", "Multiply", "8", "8", "64", True),
    # ("Chrome", "Divide", "12", "3", "4", True),
    # ("Chrome", "Concatenate", "12", "34", "1234", True),
]

# Test function: Basic calculator operations
# Executes for each set of operation parameters in the list above

@pytest.mark.parametrize("browser, op, arg_1, arg_2, expected_result, inputs_are_valid", test_data, indirect=["browser"])
def test_calculator_basic_operation(browser, op, arg_1, arg_2, expected_result, inputs_are_valid):
    """Tests calculator operations with valid inputs.
    """
    # Create page object
    calculator = BasicCalculatorPage(browser)

    # Execute test steps
    calculator.load()
    calculator.execute_calculation(arg_1, arg_2, op)

    # Assert results
    if inputs_are_valid:
        result = calculator.get_result()
        assert result == expected_result
    else:
        error_message = calculator.get_error_message()
        assert error_message == expected_result
