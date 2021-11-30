GitHub Actions Example
================================
This project will enable a GitHub Action pipeline which tests and lints the underlying project.


Example Project Structure
-------------------------
This project has two packages:
* `example` contains `calc.py`, which has a basic Calculator class.
* `tests` contains `test_calc.py`, which contains `unittest` test cases.

Manually Running Tests
----------------------

To run tests from the example project root directory, run one of the following commands:

* `python -m unittest discover` to discover all unit tests in a project
* `python -m unittest tests.test_calc` to run the test module by name
* `python -m unittest tests.test_calc.CalculatorTest` to run a TestCase class by name
* `python -m unittest tests/test_calc.py` to run the test module by file path

Note that unittest tests must be in a Python package from the project root,
meaning that the `tests` directory needs `__init__.py`.

To generate XML test reports, install `unittest-xml-reporting` and run:

* `python -m tests.test_calc`

XML reports will be printed to the `test-reports` directory.

GitHub Action Status
--------------------

[![Sample GitHub Action](https://github.com/awhipp/python-sample-github-action/actions/workflows/example-action.yml/badge.svg)](https://github.com/awhipp/python-sample-github-action/actions/workflows/example-action.yml)

GitHub Action Explanation
-------------------------

The workflow is defined within the YAML file under `.github/workflows/example-action.yml`

The workflow is defined as follows (in order by what is described in the file):
* The action's name is **Sample Github Action**
* The action is only executed on push
    * This only occurs in branches where this workflow yaml file exists
    * Specific branches can also be defined here (but those branches also need this workflow file already committed)
* Various jobs can be defined. In this case we only have the **Sample Code Lint and Test** job
* Various and multiple server types can be defined (linux, mac osx, and windows). In this case ubuntu is defined as the OS environment.
* A number of steps are then defined:
    * This code is checked out
        * This action is a community action. It is pulled from a common repository.
        * If you are in a GitHub Enterprise repository and cannot pull this common action then it is likely that the Organization Administrators have disabled that functionality. You can fork the community repositories into your organization and then reference that forked repository instead.
    * Python 3.8 is setup on the OS
        * This action is a community action. It is pulled from a common repository.
        * If you are in a GitHub Enterprise repository and cannot pull this common action then it is likely that the Organization Administrators have disabled that functionality. You can fork the community repositories into your organization and then reference that forked repository instead.
    * Python Dependencies are installed via a command line run command.
    * Code is Linted (if it fails then the action also fails) via a command line run command.
    * The Code Tests are run (if any of those fail then the action also fails) via a command line run command.
