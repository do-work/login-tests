import unittest
from TestFormFields import TestFormFields
from TestFormFieldsExceptions import TestFormFieldsExceptions
from TestFormSuccess import TestFormSuccess

# load these tests
form_fields_test = unittest.TestLoader().loadTestsFromTestCase(TestFormFields)
form_fields_exception_test = unittest.TestLoader().loadTestsFromTestCase(TestFormFieldsExceptions)
form_success_page_test = unittest.TestLoader().loadTestsFromTestCase(TestFormSuccess)

# create the test suite
form_tests = unittest.TestSuite([form_fields_test, form_success_page_test])

# run the test suite
unittest.TextTestRunner(verbosity=2).run(form_tests)
