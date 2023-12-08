# calculator_test_pytest_selenium

This repository contains a basic Python/Pytest/Selenium WebDriver UI test
automation framework for a
[basic online calculator application](https://testsheepnz.github.io/BasicCalculator.html).
This document includes a quick start guide as well as a brief technical
description of the main framework components.

## Quick Start Guide

You must have Python installed to execute this test suite. To run the suite on
your local machine:

1. Clone (or download) this repository to your local machine.

   ```console
   $ git clone https://github.com/mattmuroya/calculator_test_pytest_selenium.git
   ```

2. Change directory into the repository.

   ```console
   $ cd calculator_test_pytest_selenium
   ```

3. Optionally, create and activate a virtual environment.

   ```console
   $ python -m venv venv
   ```

   Activate on Windows:

   ```console
   $ .\venv\Scripts\activate
   ```

   Activate on MacOS/Linux:

   ```console
   $ source venv/bin/activate
   ```

4. Install the required dependencies.

   ```console
   $ pip -r requirements.txt
   ```

5. Execute the test suite:

   ```console
   $ python -m pytest
   ```

The test suite and included base test cases should execute. You should see the
name of the test file `tests/test_calculator.py` along with two green dots
indicating successful test case executions.

## Framework Design Documentation

This framework consists of two major components - pages and tests - loosely
following the Page Object Model (POM) design pattern.

### Pages

Each file in the `pages` directory contains at least one class that represents a
specific web page to be tested. The class contains all of the element locators,
WebDriver calls, and interaction methods for that page.

For example, the `calculator.py` file contains a class called
`BasicCalculatorPage` that contains a `url` class variable
(https://testsheepnz.github.io/BasicCalculator.html) and various methods for
interacting with and retrieving data from the elements on that page, such as
loading the url, entering/executing a basic calculation, and checking the
results or error message fields.

As your application/test suite grows, you can add new pages/classes and
WebDriver calls/page interaction methods. These pages and their interaction
methods will be called by individual test cases at execution time.

### Tests

The `tests` directory contains two types of files - your fixture configuration
file `conftest.py`; and any number of test suite files such
`test_calculator.py`, prefixed with `test_`.

#### conftest.py

Pytest supports a feature called _fixtures_ which are reusable functions used to
feed objects, data, or some other resource dependencies into your tests cases.
`conftest.py` contains a special fixture called `browser` that works in two
phases:

1. Setup phase: prior to test case execution, the fixture creates a new
   WebDriver instance (the particular browser - Chrome, Firefox, etc. - is
   defined in your test cases), and then temporarily feeds the driver instance
   to your test case.
2. Cleanup phase: after the test has finished executing, the fixture quits the
   driver and so your system is ready for the next test execution.

Additional fixtures can be added to `conftest.py` as needed for further test
cases/suites.

#### test\<feature>.py

The rest of the files in the `test` directory are your test suites that contain
all your individual test cases. They must be prefixed with `test_` in order for
Pytest to correctly identify and execute them.

Each function in a file, for example `test_calculator_basic_operation` in the
`test_calculator.py` file, represents a test case. As described in the
`conftest.py` section above, a WebDriver instance is fed to each test case at
execution time. The test case should then create an instance of the page it
intends to test using the appropriate class imported from the pages module, pass
the driver to the page object, and then call that object's page interaction
methods.

Test case functions can make use of Pytest's _parametrization_ feature, which
allows you to feed multiple sets of test data into a single function and have it
execute and assert the results for each set of data.

In the case of `test_calculator_basic_operation`, a set of test data can be
entered as a tuple in the `test_data` list, and the test function will execute
using each set of data sequentially. This allows you to test multiple calculator
operations (addition, subtraction, multiplication, division, and concatenation)
as well as error handling using a single function, and the results for each
execution will be recorded individually. This reduces duplicate code and makes
it easier to adjust test data as necessary.
