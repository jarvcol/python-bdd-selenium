from selenium.webdriver.common.by import By
from tests.pom.base_page import BasePage
from tests.pom.ccl_view_results import CclViewResults
from tests.pom.cdc_filters import CdcFilters
from tests.pom.cdc_results_filters import CdcResultsFilter


class HomePage(BasePage):

    homePageUrl = 'https://www.carnival.com/'
    homePageLogo = (By.CSS_SELECTOR, ".logo.pull-left")

    def __init__(self, driver):
        super().__init__(driver)
        self.cdc_filter = CdcFilters(driver)

    def open_home_page(self):
        self.go_to_url(self.homePageUrl)

    def clik_on_home_page_logo(self):
        self.get_clickable_element_by_selector(self.homePageLogo).click()

    def verify_browser_is_at_homepage(self):
        return self.get_current_page_url() == self.homePageUrl

    def click_sail_to(self):
        self.cdc_filter.click_sail_to()

    def click_duration(self):
        self.cdc_filter.click_duration()

    def select_sail_to(self, optionName):
        self.cdc_filter.click_sail_to_option(optionName)
        self.cdc_results_filter = CdcResultsFilter(self.driver)
        self.ccl_view_results = CclViewResults(self.driver)

    def select_duration(self, optionName):
        self.cdc_filter.click_duration_option(optionName)

    def check_results_view_format(self, viewType):
        if(viewType == 'grid'):
            return self.ccl_view_results.are_results_grid()
        elif(viewType == 'list'):
            return self.ccl_view_results.are_results_list()

    def click_on_pricing_filter(self):
        self.cdc_results_filter.click_on_price_filter()

    def click_on_reset_filter(self):
        self.cdc_results_filter.click_on_rest_filter()

    def move_lower_price_filter(self, value):
        self.cdc_results_filter.move_lower_pricing_pointer_right(value)

    def move_higher_price_filter(self, value):
        self.cdc_results_filter.move_higher_pricing_pointer_right(value)

    def results_in_price_range(self, minValue, maxValue):
        return self.ccl_view_results.results_is_in_price_range(minValue, maxValue)

    def click_on_learn_option_by_index(self, index):
        self.ccl_view_results.click_on_learn_option_by_index(index)

    def current_page_is_home(self):
        return self.check_current_url_contains(self.homePageUrl)
