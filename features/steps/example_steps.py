from behave import *
from behave.api.async_step import async_run_until_complete

from models.main_page import MainPage
from models.elements_page import ElementsPage


@given('the main page is open')
@async_run_until_complete
async def open_login_url(context):
    main_page = MainPage(context.page)
    await main_page.navigate()
    await main_page.verify_main_page()

@when("I click Elements in the main page")
@async_run_until_complete
async def open_login_url(context):
    main_page = MainPage(context.page)
    await main_page.click_elements()

@then("I am at the Elements Page")
@async_run_until_complete
async def verify_element_page(context):
    elements_page = ElementsPage(context.page)
    await elements_page.verify_text_box_page()


@when("I Click Text Box")
@async_run_until_complete
async def click_text_box(context):
    elements_page = ElementsPage(context.page)
    await elements_page.go_to_tex_box()

@when('I fill Name Box with "{value}"')
@async_run_until_complete
async def step_impl(context, value: str):
    elements_page = ElementsPage(context.page)
    await elements_page.fill_name(value)

@when('I fill Email with "{value}"')
@async_run_until_complete
async def step_impl(context, value: str):
    elements_page = ElementsPage(context.page)
    await elements_page.fill_email(value)

@when('I fill Current Address with "{value}"')
@async_run_until_complete
async def step_impl(context, value: str):
    elements_page = ElementsPage(context.page)
    await elements_page.fill_address_curr(value)

@when('I fill Permanent Address with "{value}"')
@async_run_until_complete
async def step_impl(context, value: str):
    elements_page = ElementsPage(context.page)
    await elements_page.fill_address_new(value)


@when("I click Submit")
@async_run_until_complete
async def click_submit(context):
    elements_page = ElementsPage(context.page)
    await elements_page.click_button()