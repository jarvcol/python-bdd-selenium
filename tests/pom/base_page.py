from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 60

    def go_to_url(self, url):
        self.driver.get(url)

    def get_current_page_url(self):
        WebDriverWait(self.driver, self.timeout).until(lambda s: self.driver.title)
        return self.driver.current_url

    def refresh_current_page(self):
        self.driver.refresh()

    def navigate_back(self):
        self.driver.back()

    def navigate_forward(self):
        self.driver.forward()

    def check_current_url_contains(self, urlSegment):
        return urlSegment in self.get_current_page_url()

    def get_current_page_title(self):
        WebDriverWait(self.driver, self.timeout).until(lambda s: self.driver.title)
        return self.driver.title

    def get_clickable_element_by_selector(self, selector):
        WebDriverWait(self.driver, self.timeout,
                      ignored_exceptions=[ElementNotVisibleException,
                                          ElementNotSelectableException,
                                          StaleElementReferenceException]) \
            .until(expected_conditions.element_to_be_clickable(selector))
        return self.driver.find_element(*selector)

    def get_element_selector_by_value(self, stringLocator, value):
        return (By.XPATH, stringLocator.replace("{value}", value))

    def get_element_by_selector(self, selector):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                expected_conditions.visibility_of_element_located(selector))
            return self.driver.find_element(*selector)
        except TimeoutException:
            return None

    def get_element_list_by_selector(self, selector):
        try:
            WebDriverWait(self.driver, self.timeout,
                          ignored_exceptions=[ElementNotVisibleException,
                                              ElementNotSelectableException,
                                              StaleElementReferenceException]) \
                .until(expected_conditions.presence_of_element_located(selector))
            return self.driver.find_elements(*selector)
        except TimeoutException:
            return []