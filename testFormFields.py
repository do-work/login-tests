import unittest
import os
from selenium import webdriver


class SearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()

        # todo create function to pass in any page
        local_path_form = os.getcwd() + "/loginForm.html"
        cls.driver.get("file:// {}".format(local_path_form))

    def test_login_is_true(self):
        self.search_login = self.driver.find_element_by_name("username")
        self.assertTrue(self.search_login)

    def test_password_is_true(self):
        self.search_password = self.driver.find_element_by_name("password")
        self.assertTrue(self.search_password)

    def test_submit_exists(self):
        self.search_submit = self.driver.find_element_by_xpath("//input[@type='submit']")
        self.assertTrue(self.search_submit)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    if __name__ == '__main__':
        unittest.main(verbosity=2)
