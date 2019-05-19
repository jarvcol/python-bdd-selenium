from behave import *
from selenium import webdriver
from tests.pom.home_page import HomePage

use_step_matcher('re')

@given('I access Carnival Home Page')
def step_imp(context):
    context.driver = webdriver.Chrome()
    homePage = HomePage(context.driver)
    homePage.open_home_page()
    context.page = homePage

@When('I click on sail to filter')
def step_imp(context):
    context.page.click_sail_to()

@When('I select sail to "(.*)"')
def step_imp(context, optionName):
    context.page.select_sail_to(optionName)

@When('I click on the pricing filter')
def step_imp(context):
    context.page.click_on_pricing_filter()

@When('I click on reset filter button')
def step_imp(context):
    context.page.click_on_reset_filter()

@When('I move lower pricing pointer up to "(.*)"')
def step_imp(context, value):
    context.page.move_lower_price_filter(value)

@When('I move higher pricing pointer up to "(.*)"')
def step_imp(context, value):
    context.page.move_higher_price_filter(value)

@Then('I should see the results as "(.*)"')
def step_imp(context, viewType):
    assert context.page.check_results_view_format(viewType)

@Then('I should see cruise results between "(.*)" and "(.*)"')
def step_imp(context, minVal, maxVal):
    assert context.page.results_in_price_range(minVal, maxVal)



