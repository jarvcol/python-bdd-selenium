from selenium.webdriver.common.by import By
from tests.pom.base_page import BasePage
from tests.pom.ccl_view_results import CclViewResults
from tests.pom.cdc_filters import CdcFilters
from tests.pom.cdc_results_filters import CdcResultsFilter


class ItineraryPage(BasePage):

    itineraryPageUrl = 'https://www.carnival.com/itinerary/'
    itineraryDayCardsButtonsCount = (By.CSS_SELECTOR, '.itinerary-day-tile .day')
    aboutDayCardsButtons = (By.CSS_SELECTOR, '.itinerary-day-tile .departure-time + a')
    bookNowButtons = (By.XPATH, "//span[@ng-click='goToBooking(url)' and @role='button']//span[contains(text(),'Book Now')]")

    def current_page_is_itinerary(self):
        return self.check_current_url_contains(self.itineraryPageUrl)

    def cards_have_about_button(self):
        return len(self.get_element_list_by_selector(self.itineraryDayCardsButtonsCount)) == \
            len(self.get_element_list_by_selector(self.aboutDayCardsButtons))

    def itinerary_page_has_book_button(self):
        return len(self.get_element_list_by_selector(self.bookNowButtons)) >= 1


