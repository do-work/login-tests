import unittest
from selenium import webdriver


class TestFormFields(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        # todo add explicit waits

        # todo create function to pass in any page
        local_path_form = "/loginForm.html"
        cls.driver.get("localhost:8000//{}".format(local_path_form))

    def test_username_field_exists(self):
        username_field = self.driver.find_element_by_name("username")
        self.assertTrue(username_field)

    def test_password_field_exists(self):
        password_field = self.driver.find_element_by_name("password")
        self.assertTrue(password_field)

    def test_submit_button_exists(self):
        submit_button = self.driver.find_element_by_xpath("//input[@type='submit']")
        self.assertTrue(submit_button)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # only allow test from the testSuite
    # if __name__ == '__main__':
    #     unittest.main(verbosity=2)
