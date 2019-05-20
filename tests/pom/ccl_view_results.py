from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.pom.base_page import BasePage

class CclViewResults(BasePage):

    # By locators
    listOfPrices = (By.CSS_SELECTOR, ".vrgf-price-box__price")
    learnMoreButtons = (By.CSS_SELECTOR, ".vrg-search-unit .vrgf-learn-more a")
    resultViewType = (By.XPATH, ".//div/*[@ng-switch-when]")

    def click_on_learn_option_by_index(self, index):
        href = self.get_element_list_by_selector(self.learnMoreButtons)[int(index)].get_attribute('href')
        self.go_to_url(href)

    def are_results_grid(self):
        resultView = self.get_element_by_selector(self.resultViewType).get_attribute('ng-switch-when')
        return resultView == 'grid'

    def are_results_list(self):
        resultView = self.get_element_by_selector(self.resultViewType).get_attribute('ng-switch-when')
        return resultView == 'list'

    def results_is_in_price_range(self, minVal, maxVal):
        pricesList = self.get_element_list_by_selector(self.listOfPrices)
        for priceText in pricesList:
            priceValue = re.sub(r'[^\d]','',priceText.text)
            if not (priceValue >= minVal and priceValue <= maxVal):
                return False
        return True

