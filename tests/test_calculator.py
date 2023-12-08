"""These test verify basic calculator functionality.
"""

import pytest
from pages.calculator import BasicCalculatorPage

# Set up test data
test_parameters = [
    ("Chrome", "Add", "15", "30", "45"),
    # ("Chrome", "Subtract", "15", "40", "-25"),
    # ("Chrome", "Multiply", "8", "8", "64"),
    # ("Chrome", "Divide", "12", "3", "4")
]

# Test: Basic calculator operations
# Executes for each set of test parameters in the list above
@pytest.mark.parametrize("driver, op, arg_1, arg_2, expected_result", test_parameters, indirect=["driver"])
def test_calculator_basic_operation(driver, op, arg_1, arg_2, expected_result):
    """Tests calculator addition with invalid inputs.
    """
    # Create page object
    calculator = BasicCalculatorPage(driver)

    # Execute test steps
    calculator.load()
    calculator.execute_calculation(arg_1, arg_2, op)

    # Assert results
    result = calculator.get_result()
    assert result == expected_result
