import unittest
import requests
from selenium import webdriver


class TestFormSuccess(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        # todo add explicit waits

        # todo create function to pass in any page
        local_path_form = "/loginForm.html"
        cls.driver.get("localhost:8000//{}".format(local_path_form))

    def test_form_success(self):
        self.submit_button = self.driver.find_element_by_xpath("//input[@type='submit']").click()

        page_header = requests.get(self.driver.current_url)
        self.assertEqual(page_header.status_code, 200)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # only allow test from the testSuite
    # if __name__ == '__main__':
    #     unittest.main(verbosity=2)
