"""Selenium WebDriver setup/cleanup fixtures. Pytest loads browser drivers from
this module for reuse with individual test cases (dependency injection).

This module can be expanded to include additional browser drivers.
"""

import pytest
import selenium.webdriver

# Chrome
@pytest.fixture
def chrome():
    """Defines setup and cleanup process for Chrome WebDriver instances.
    """
    # Setup phase (executes before the test case is run)
    # Initializes, configures, and yields Chrome WebDriver instance
    driver = selenium.webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver

    # Cleanup phase: (executes after the test case finishes)
    # Quits Chrome WebDriver instance
    driver.quit()
