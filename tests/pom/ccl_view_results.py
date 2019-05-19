from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.pom.base_page import BasePage

class CclViewResults(BasePage):

    # By locators
    listOfPrices = (By.CSS_SELECTOR, ".vrgf-price-box__price")
    learnMoreButtons = (By.CSS_SELECTOR, ".vrg-search-unit .vrgf-learn-more")

    resultViewType = (By.XPATH, ".//div/*[@ng-switch-when]")

    def are_results_grid(self):
        resultView = self.get_element_by_selector(self.resultViewType).get_attribute('ng-switch-when')
        return resultView == 'grid'

    def are_results_list(self):
        resultView = self.get_element_by_selector(self.resultViewType).get_attribute('ng-switch-when')
        return resultView == 'list'