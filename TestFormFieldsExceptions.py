import unittest
from selenium import webdriver
from ddt import ddt, data, unpack


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
    @data("david", "test")
    def test_username_field_exceptions(self, user_value):
        self.username_field = self.driver.find_element_by_name("username")
        self.username_field.clear()

        self.username_field.send_keys(user_value)
        self.user_input_username = self.username_field.get_attribute("value")

        print(self.user_input_username)

        self.assertEqual(user_value, self.user_input_username)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    if __name__ == '__main__':
        unittest.main(verbosity=2)