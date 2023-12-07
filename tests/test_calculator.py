"""These test verify basic calculator functionality.
"""

# Import page object
from pages.calculator import BasicCalculatorPage

# Test: Basic calculator addition
def test_calculator_basic_addition(chrome):
    """Tests calculator addition with invalid inputs.
    """
    # Create page object
    calculator = BasicCalculatorPage(chrome)

    # Set up test data
    arg_1 = "15"
    arg_2 = "30"
    expected_result = "45"

    # Execute test steps
    calculator.load()
    calculator.execute_calculation(arg_1, arg_2, "Add")

    # Assert results
    result = calculator.get_result()
    assert result == expected_result

# Test: Invalid input
def test_calculator_invalid_input(chrome):
    """Tests calculator addition with invalid inputs.
    """
    # Create page object
    calculator = BasicCalculatorPage(chrome)

    # Set up test data
    arg_1 = "5"
    arg_2 = "five"
    expected_result = ""

    # Execute test steps
    calculator.load()
    calculator.execute_calculation(arg_1, arg_2, "Add")

    # Assert results
    result = calculator.get_result()
    assert result == expected_result
