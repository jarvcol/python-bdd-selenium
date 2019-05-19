from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions

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
        self.drive.forward()

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