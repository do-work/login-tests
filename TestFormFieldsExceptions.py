import unittest
from selenium import webdriver
from ddt import ddt, data


@ddt
class TestFormFieldsExceptions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        # todo add explicit waits

        # todo create function to pass in any page
        local_path_form = "/loginForm.html"
        cls.driver.get("localhost:8000//{}".format(local_path_form))

    # todo create method that accepts various data input types
    @data("test1", "test2")
    def test_username_field_exceptions(self, user_value):
        username_field = self.driver.find_element_by_name("username")
        username_field.clear()

        # this sends the keys as listed above in the data decorator
        username_field.send_keys(user_value)
        user_input_username = username_field.get_attribute("value")

        self.assertEqual(user_value, user_input_username)

    @data("test1-pass", "test2-pass")
    def test_password_field_exceptions(self, user_value):
        password_field = self.driver.find_element_by_name("password")
        password_field.clear()

        password_field.send_keys(user_value)
        user_input_password = password_field.get_attribute("value")

        self.assertEqual(user_value, user_input_password)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # only allow test from the testSuite
    # if __name__ == '__main__':
    #     unittest.main(verbosity=2)
