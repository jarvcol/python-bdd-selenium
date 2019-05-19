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

    def select_sail_to(self, optionName):
        self.cdc_filter.click_sail_to_option(optionName)
        self.cdc_results_filter = CdcResultsFilter(self.driver)
        self.ccl_view_results = CclViewResults(self.driver)

    def check_results_view_format(self, viewType):
        if(viewType == 'grid'):
            return self.ccl_view_results.are_results_grid()
        elif(viewType == 'list'):
            return self.ccl_view_results.are_results_list()


