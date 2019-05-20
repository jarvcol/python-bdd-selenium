from behave import *
from selenium import webdriver
from tests.pom.home_page import HomePage
from tests.pom.itinerary_page import ItineraryPage

use_step_matcher('re')

@given('I access Carnival Home Page')
def step_imp(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    homePage = HomePage(context.driver)
    homePage.open_home_page()
    context.homePage = homePage

@When('I click on sail to filter')
def step_imp(context):
    context.homePage.click_sail_to()

@When('I click on duration filter')
def step_imp(context):
    context.homePage.click_duration()

@When('I select sail to "(.*)"')
def step_imp(context, optionName):
    context.homePage.select_sail_to(optionName)

@When('I select duration as "(.*)"')
def step_imp(context, optionName):
    context.homePage.select_duration(optionName)

@When('I click on the pricing filter')
def step_imp(context):
    context.homePage.click_on_pricing_filter()

@When('I click on reset filter button')
def step_imp(context):
    context.homePage.click_on_reset_filter()

@When('I move lower pricing pointer up to "(.*)"')
def step_imp(context, value):
    context.homePage.move_lower_price_filter(value)

@When('I move higher pricing pointer up to "(.*)"')
def step_imp(context, value):
    context.homePage.move_higher_price_filter(value)

@When('I click on the result option "(.*)"')
def step_imp(context, value):
    context.homePage.click_on_learn_option_by_index(value)
    context.itineraryPage = ItineraryPage(context.driver)

@Then('I should see the results as "(.*)"')
def step_imp(context, viewType):
    assert context.homePage.check_results_view_format(viewType), 'Results are not shown as expected: '+viewType

@Then('I should see cruise results between "(.*)" and "(.*)"')
def step_imp(context, minVal, maxVal):
    assert context.homePage.results_in_price_range(minVal, maxVal), 'Results are not between expected values '+minVal+' '+maxVal

@Then('I should see the itinerary page')
def step_imp(context):
    assert context.itineraryPage.current_page_is_itinerary(), 'Current page is not itinerary page'

@Then('I should be able to read about each day')
def step_imp(context):
    assert context.itineraryPage.cards_have_about_button(), 'Not every single day card has the learn more button'

@Then('I should see a book now button on itinerary page')
def step_imp(context):
    assert context.itineraryPage.itinerary_page_has_book_button(), 'Not every single day card has the learn more button'