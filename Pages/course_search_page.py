from selenium.webdriver.common.by import By
from Locators.locators import Locators

class CourseSearchPage():

    def __init__(self, driver):
        self.driver = driver

        self.search_textbox_xpath = Locators.search_textbox_xpath
        self.search_button_xpath = Locators.search_button_xpath
        self.course_xpath = Locators.course_xpath

    def search_textbox_sendKeys(self, searchKeyword):
        self.driver.find_element(By.XPATH, self.search_textbox_xpath).send_keys(searchKeyword)

    def search_button_click(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()

    def select_course(self):
        self.driver.find_element(By.XPATH, self.course_xpath).click()