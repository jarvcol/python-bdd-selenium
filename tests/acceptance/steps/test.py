from behave import *
from selenium import webdriver
from tests.pom.home_page import HomePage

use_step_matcher('re')

@when('I click on the Carnival Logo')
def step_imp(context):
    context.page.clik_on_home_page_logo()

@then('I should be redirected to home page')
def step_imp(context):
    assert context.page.verify_browser_is_at_homepage()




