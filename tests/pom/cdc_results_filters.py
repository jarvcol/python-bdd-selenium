from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from tests.pom.base_page import BasePage

class CdcResultsFilter(BasePage):

    # By locators
    pricingFilter = (By.ID, "sfn-nav-pricing")
    lowerPricingPointer = (By.CSS_SELECTOR, ".rz-pointer.rz-pointer-min")
    higherPricingPointer = (By.CSS_SELECTOR, ".rz-pointer.rz-pointer-max")
    resetPriceSlider = (By.CSS_SELECTOR, ".sfp-reset__button")
    resetFiltersLink = (By.CSS_SELECTOR, 'div.sbsc-container a')


    def click_on_price_filter(self):
        self.get_clickable_element_by_selector(self.pricingFilter).click()

    def click_on_rest_filter(self):
        self.get_element_by_selector(self.resetPriceSlider).click()

    def move_lower_pricing_pointer_right(self, value):
        while not (self.get_element_by_selector(self.lowerPricingPointer).get_attribute('aria-valuenow') == value):
            WebDriverWait(self.driver, self.timeout).until(expected_conditions.visibility_of(
                 self.get_element_by_selector(self.lowerPricingPointer)))
            self.get_element_by_selector(self.lowerPricingPointer).send_keys(Keys.ARROW_RIGHT)
            WebDriverWait(self.driver, self.timeout).until(expected_conditions.visibility_of(
                self.get_element_by_selector(self.resetFiltersLink)))

    def move_higher_pricing_pointer_right(self, value):
        while not (self.get_element_by_selector(self.higherPricingPointer).get_attribute('aria-valuenow') == value):
            WebDriverWait(self.driver, self.timeout).until(expected_conditions.visibility_of(
                 self.get_element_by_selector(self.higherPricingPointer)))
            self.get_element_by_selector(self.higherPricingPointer).send_keys(Keys.ARROW_LEFT)
            WebDriverWait(self.driver, self.timeout).until(expected_conditions.visibility_of(
                self.get_element_by_selector(self.resetFiltersLink)))
