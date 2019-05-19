from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.pom.base_page import BasePage

class CdcResultsFilter(BasePage):

    # By locators
    pricingFilter = (By.ID, "sfn-nav-pricing")
    lowerPricingPointer = (By.CSS_SELECTOR, ".rz-pointer.rz-pointer-min")
    higherPricingPointer = (By.CSS_SELECTOR, ".rz-pointer.rz-pointer-max")
    resetPriceSlider = (By.CSS_SELECTOR, ".sfp-reset__button")



