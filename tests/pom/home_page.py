from selenium.webdriver.common.by import By
from tests.pom.base_page import BasePage

class HomePage(BasePage):

    homePageUrl = 'https://www.carnival.com/'
    homePageLogo = (By.CSS_SELECTOR, ".logo.pull-left")

    def open_home_page(self):
        self.go_to_url(self.homePageUrl)

    def clik_on_home_page_logo(self):
        self.get_clickable_element_by_selector(self.homePageLogo).click()

    def verify_browser_is_at_homepage(self):
        return self.get_current_page_url() == self.homePageUrl


