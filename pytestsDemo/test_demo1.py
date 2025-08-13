# Any pytest file should start with test_ or end with _test
# pytest method name should start with test_
# Any code should be wrapped in method only
# Method name should be descriptive
# -k stands for method name execution
# -s logs output
# -v gives more info about the test result
# Can run specific file with py.test <filename>
# Can mark (tag) tests @pytest.mark.smoke and then run with -m
# Can skip tests with @pytest.mark.skip
# @pytest.mark.xfail will run, but not log in the report
# fixtures are used as setup and tear down methods for test cases
# conftest file to generalize fixture and make it to availale in all test cases
# datadriven and parameterization can be done with return statements in tuple format
# when defining fixture scope to class only, it will run once before class is initiated and at the end

import pytest


@pytest.mark.smoke
def test_first_program(setup):
    print("Hello")


@pytest.mark.xfail
def test_second_program():
    print("hi")


def test_cross_browser(cross_browser):
    print(cross_browser[1])


