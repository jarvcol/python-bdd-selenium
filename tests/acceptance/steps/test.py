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

@when('I click on the Carnival Logo')
def step_imp(context):
    context.page.clik_on_home_page_logo()

@then('I should be redirected to home page')
def step_imp(context):
    assert context.page.verify_browser_is_at_homepage()




