import time

from selenium import webdriver
import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".", "."))
from Pages.course_search_page import CourseSearchPage
import HtmlTestRunner


class CourseSearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_course_search(self):
        driver = self.driver

        baseUrl = "https://www.youtube.com/"
        driver.get(baseUrl)

        csp = CourseSearchPage(driver)
        csp.search_textbox_sendKeys("selenium with python")
        csp.search_button_click()
        csp.select_course()

        time.sleep(5)

    def test_02_invalid_course_search(self):
        driver = self.driver

        baseUrl = "https://www.youtube.com/"
        driver.get(baseUrl)

        csp = CourseSearchPage(driver)
        csp.search_textbox_sendKeys("invalid test")
        csp.search_button_click()
        csp.select_course()

        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed Successfully")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='C:/Users/Bhagyashree/workspace_python/YouTubeCourseSearch/reports'))

# To run on command prompt, run as administrator
# Navigate to:
# C:\Users\Bhagyashree\workspace_python\YouTubeCourseSearch
# Command:
# python -m Tests.course_search_test
