# login-tests
Python and Selenium Unit Tests for Basic Login Screen


## install dependencies

    pip install -r requirements.txt

## how to run

First set up a localhost using pythons built in command:

    python -m http.server

The test is set to use a TestSuite. Run the TestSuite by entering the following from the root directory:

    python -m unittest TestFormSuite

This TestSuite includes the following 3 individual tests:

+ TestFormFields
+ TestFormFieldsExceptions
+ TestFormSuccess

The individual tests are not able to be run directly but the code to allow this is already there and can be uncommented.


