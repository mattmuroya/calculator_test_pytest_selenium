"""Selenium WebDriver setup/cleanup fixtures. Pytest loads browser drivers from
this module for reuse with individual test cases (dependency injection).
"""

import pytest
import selenium.webdriver

# Chrome
@pytest.fixture
def browser(request):
    """Defines setup and cleanup process for Chrome WebDriver instances.
    """
    # Setup phase (executes before the test case is run)
    # Browser selected based on test case input parameters
    if request.param == "Firefox":
        driver = selenium.webdriver.Firefox()
    elif request.param == "Edge":
        driver = selenium.webdriver.Edge()
    else: # Default to Chrome
        driver = selenium.webdriver.Chrome()

    # Configure driver options
    driver.implicitly_wait(10)
    driver.maximize_window()

    # Return Generator
    yield driver

    # Cleanup phase: (executes after the test case finishes)
    # Quit WebDriver instance
    driver.quit()
