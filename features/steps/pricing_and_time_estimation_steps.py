from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from faker import Faker
import random


@given('user is on the homepage')
def step_start_page(context):
    context.driver.get('https://turbotlumaczenia.pl/')
    context.driver.implicitly_wait(2)
    try:
        context.driver.find_element(By.CLASS_NAME, 'cp-callback-widget cp-callpage__widget cp-js-widget')
        context.driver.find_element(By.CLASS_NAME, 'cp-close-btn__path').click()
    except NoSuchElementException:
        pass


@when('user clicks \'Wyceń i zamów tłumaczenie\' button to choose the service')
def step_choose_service(context):
    context.driver.find_element(By.XPATH, '//a[@class="btn btn-red btn-block-xs btn-lg disable_on_click"]').click()


@when('user chooses to translate from Polish to German')
def step_choose_polish_to_german(context):
    els = context.driver.find_elements(By.CLASS_NAME, 'content__input')
    els[1].click()
    context.driver.find_element(By.ID, 'Row_1en').click()
    context.driver.find_element(By.ID, 'Row_16de').click()
    els[1].click()


@when('user checks box \'dodatkowa korekta native speakera\'')
def step_choose_proofreading(context):
    context.driver.find_element(By.ID, 'proofreading').click()


@when('user fills in 250-400 words to translate into the text field')
def step_fill_in_text_to_translate(context):
    faker = Faker(['pl_PL'])
    text_to_translate = faker.sentence(random.randint(250, 400), False)
    context.driver.find_element(By.ID, 'content').send_keys(text_to_translate)


@when('e-mail field stays empty')
def step_check_if_email_is_empty(context):
    context.driver.find_element(By.ID, 'email').clear()


@then('pricing and time estimation should be present')
def step_check_if_pricing_and_time_estimation_present(context):
    pricing = context.driver.find_element(By.XPATH, '//span[@data-bind-expected-realisation-time]')
    time_estimation = context.driver.find_element(By.XPATH, '//span[@data-bind-expected-price]')
    assert pricing, time_estimation
