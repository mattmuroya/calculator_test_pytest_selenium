"""This module defines the page object and interaction methods for the Basic
Calculator page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class BasicCalculatorPage:
    """Page object for the Basic Calculator web page.
    """
    url = "https://testsheepnz.github.io/BasicCalculator.html"

    # Initializer

    def __init__(self, driver):
        """Initializes the page object with the provided browser driver.
        """
        self._driver = driver

    # Page interaction methods

    def load(self):
        """
        """
        self._driver.get(self.url)

    def execute_calculation(self, arg_1, arg_2, operation):
        """Takes two arguments and an operation type (Add, Subtract, Multiply,
        Divide, or Concatenate), inputs those values on the page, and executes
        the calculation.
        """
        # Identify page elements
        input_1 = self._driver.find_element(By.ID, "number1Field")
        input_2 = self._driver.find_element(By.ID, "number2Field")
        operation_dropdown = Select(self._driver.find_element(By.ID, "selectOperationDropdown"))
        calculate_button = self._driver.find_element(By.ID, "calculateButton")

        # Execute WebDriver calls
        input_1.send_keys(arg_1)
        input_2.send_keys(arg_2)
        operation_dropdown.select_by_visible_text(operation)
        calculate_button.click()

    def get_result(self):
        """
        """
        # Identify page elements
        answer = self._driver.find_element(By.ID, "numberAnswerField")
        return answer.get_attribute('value')
