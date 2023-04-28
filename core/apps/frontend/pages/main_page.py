import allure
from selene import by, query
from selene.support.shared import browser

from core.apps.frontend.pages.base_page import BasePage


class MainPage(BasePage):
    """
    Every action method in a page module should have allure.step annotation. This steps will be displayed in allure
    report as actions and it will be clear, what happened on the page. That's why it's better to interact with items
    only via wrapped methods.
    Please note, that business steps shouldn't be implemented here
    """

    path = ''

    register_link = browser.element(by.xpath("//a[contains(@href, 'register.htm')]"))
    first_name_input = browser.element(by.name("customer.firstName"))
    last_name_input = browser.element(by.name("customer.lastName"))
    address_input = browser.element(by.name("customer.address.street"))
    city_input = browser.element(by.name("customer.address.city"))
    state_input = browser.element(by.name("customer.address.state"))
    zip_code_input = browser.element(by.name("customer.address.zipCode"))
    phone_input = browser.element(by.name("customer.phoneNumber"))
    ssn_input = browser.element(by.name("customer.ssn"))
    username_input = browser.element(by.name("customer.username"))
    password_input = browser.element(by.name("customer.password"))
    confirm_input = browser.element(by.name("repeatedPassword"))
    register_button = browser.element(by.xpath("//input[@value='Register']"))
    welcome_page_title = browser.element(by.xpath("/html/head/title"))
    welcome_username = browser.element(by.xpath("//h1[@class ='title']"))
    welcome_user = browser.element(by.xpath("//p[@class='smallText']"))
    error_existing_username = browser.element(by.xpath("//span[@id='customer.username.errors']"))
    required_password_error = browser.element(by.xpath("//span[@id='customer.password.errors']"))
    password_confirmation_error = browser.element(by.xpath("//span[@id='repeatedPassword.errors']"))
    login_username_input = browser.element(by.name("username"))
    login_password_input = browser.element(by.name("password"))
    login_button = browser.element(by.xpath("//input[@value='Log In']"))

    def navigate(self):
        super().navigate()

    @allure.step('Click "Register" link')
    def click_register_link(self):
        self.register_link.click()

    @allure.step('Fill first name input')
    def fill_first_name_input(self, text: str):
        self.first_name_input.send_keys(text)

    @allure.step('Fill last name input')
    def fill_last_name_input(self, text: str):
        self.last_name_input.send_keys(text)

    @allure.step('Fill address input')
    def fill_address_input(self, text: str):
        self.address_input.send_keys(text)

    @allure.step('Fill city input')
    def fill_city_input(self, text: str):
        self.city_input.send_keys(text)

    @allure.step('Fill state input')
    def fill_state_input(self, text: str):
        self.state_input.send_keys(text)

    @allure.step('Fill zip code input')
    def fill_zip_code_input(self, text: str):
        self.zip_code_input.send_keys(text)

    @allure.step('Fill phone input')
    def fill_phone_input(self, text: str):
        self.phone_input.send_keys(text)

    @allure.step('Fill SSN input')
    def fill_ssn_input(self, text: str):
        self.ssn_input.send_keys(text)

    @allure.step('Fill username input')
    def fill_username_input(self, text: str):
        self.username_input.send_keys(text)

    @allure.step('Fill password input')
    def fill_password_input(self, text: str):
        self.password_input.send_keys(text)

    @allure.step('Fill confirm input')
    def fill_confirm_input(self, text: str):
        self.confirm_input.send_keys(text)

    @allure.step('Click "Register" button')
    def click_register_button(self):
        self.register_button.click()

    def fill_login_username_input(self, text: str):
        self.login_username_input.send_keys(text)

    def fill_login_password_input(self, text: str):
        self.login_password_input.send_keys(text)

    def click_login_button(self):
        self.login_button.click()


main_page = MainPage()
