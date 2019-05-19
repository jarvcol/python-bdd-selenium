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

@Then('I should see the results as "(.*)"')
def step_imp(context, viewType):
    assert context.page.check_results_view_format(viewType)


