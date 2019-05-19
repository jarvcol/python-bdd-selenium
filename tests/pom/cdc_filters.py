from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.pom.base_page import BasePage

class CdcFilters(BasePage):

    #string selector
    sail_to_option = "//button[@class='cdc-filter-button' and @aria-label='{value} ']"
    duration_option = "//button[@class='cdc-filter-button' and @aria-label='{value} ']"

    # By locators
    sailToFilter = (By.ID, "cdc-destinations")
    durationFilter = (By.ID, "cdc-durations")

    def click_duration(self):
        WebDriverWait(self.driver, self.timeout).until(
            expected_conditions.element_to_be_clickable(self.durationFilter))
        self.get_clickable_element_by_selector(self.durationFilter).click()

    def click_sail_to(self):
        WebDriverWait(self.driver, self.timeout).until(
            expected_conditions.element_to_be_clickable(self.sailToFilter))
        self.get_clickable_element_by_selector(self.sailToFilter).click()

    def click_sail_to_option(self, option_name):
        selector = self.get_element_selector_by_value(self.sail_to_option, option_name)
        WebDriverWait(self.driver, self.timeout).until(
            expected_conditions.element_to_be_clickable(selector))
        self.get_clickable_element_by_selector(selector).click()

    def click_duration_option(self, option_name):
        selector = self.get_element_selector_by_value(self.duration_option, option_name)
        WebDriverWait(self.driver, self.timeout).until(
            expected_conditions.element_to_be_clickable(selector))
        self.get_clickable_element_by_selector(selector).click()
