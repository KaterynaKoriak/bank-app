import allure
from selene import by
from selene.support.shared import browser

from core.apps.frontend.pages.base_page import BasePage


class AccountPage(BasePage):
    @staticmethod
    def get_accounts_overview_balance(text):
        return browser.element(by.xpath(f'//td[count(//table/thead/tr/th[.="Balance*"]'
                                        f'/preceding-sibling::th)+1][text()="${text}"]'))

    @staticmethod
    def get_accounts_overview_available_amount(text):
        return browser.element(by.xpath(f'//td[count(//table/thead/tr/th[.="Available Amount"]'
                                        f'/preceding-sibling::th)+1][text()="${text}"]'))

    @staticmethod
    def get_from_account_dropdown_options(account_id):
        return browser.element(by.xpath(f"//select[@id='fromAccountId']/option[text()={account_id}]"))

    @staticmethod
    def get_to_account_dropdown_options(account_id):
        return browser.element(by.xpath(f"//select[@id='toAccountId']/option[text()={account_id}]"))

    accounts_overview_link = browser.element(by.xpath("//a[contains(@href, '/parabank/overview.htm')]"))
    accounts_overview_total = browser.element(by.xpath("//b[@class='ng-binding']"))
    page_meta_title = browser.element(by.xpath("/html/head/title"))
    minimal_amount_message = browser.element(by.xpath("//select[@id='type']/following-sibling::p/b"))
    open_new_account = browser.element(by.xpath("//a[contains(@href, '/parabank/openaccount.htm')]"))
    page_title = browser.element(by.xpath("//h1[@class='title']"))
    account_type_dropdown = browser.element(by.xpath("//*[@id='type']"))
    savings_option = browser.element(by.xpath("//*[@id='type']/option[text()='SAVINGS']"))
    open_new_account_button = browser.element(by.xpath("//*[@value='Open New Account']"))
    first_name_input = browser.element(by.name("initialBalance"))
    submit_button = browser.element(by.xpath("//input[@value='Submit']"))
    login_username_input = browser.element(by.name("username"))
    login_password_input = browser.element(by.name("password"))
    login_button = browser.element(by.xpath("//input[@value='Log In']"))
    transfer_funds_option = browser.element(by.xpath("//li/a[text() = 'Transfer Funds']"))
    transfer_amount_input = browser.element(by.xpath("//input[@id='amount']"))
    from_account_dropdown = browser.element(by.xpath("//select[@id='fromAccountId']"))
    to_account_dropdown = browser.element(by.xpath("//select[@id='toAccountId']"))
    transfer_button = browser.element(by.xpath("//input[@value='Transfer']"))

    @allure.step('Click "Open New Account" option on the navigation panel')
    def click_open_new_account_link(self):
        self.open_new_account.click()

    @allure.step('Open account type dropdown')
    def open_account_type_dropdown(self):
        self.account_type_dropdown.click()

    @allure.step('Select "Savings" account type option')
    def select_savings_account_type(self):
        self.savings_option.click()

    @allure.step('Click "Open New Account" button')
    def click_open_new_account_button(self):
        self.open_new_account_button.click()

    @allure.step('Click "Accounts Overview" option on the navigation panel')
    def click_accounts_overview_option(self):
        self.accounts_overview_link.click()

    @allure.step('Fill in username input for customer login')
    def fill_login_username_input(self, text: str):
        self.login_username_input.send_keys(text)

    @allure.step('Fill in password input for customer login')
    def fill_login_password_input(self, text: str):
        self.login_password_input.send_keys(text)

    @allure.step('Click on "Log in" button')
    def click_login_button(self):
        self.login_button.click()

    @allure.step('Click the "Transfer Funds" option on the left navigation panel')
    def click_transfer_funds(self):
        self.transfer_funds_option.click()

    @allure.step('Enter the amount to be transferred')
    def fill_transfer_amount_input(self, text: str):
        self.transfer_amount_input.send_keys(text)

    @allure.step('Click "From account #" dropdown')
    def click_from_account_dropdown(self):
        self.from_account_dropdown.click()

    @allure.step('Select "From account #" dropdown option')
    def select_from_account(self, account_id):
        self.get_from_account_dropdown_options(account_id).click()

    @allure.step('Click "to account #" dropdown')
    def click_to_account_dropdown(self):
        self.to_account_dropdown.click()

    @allure.step('Select "to account #" dropdown option')
    def select_to_account(self, account_id):
        self.get_to_account_dropdown_options(account_id).click()

    @allure.step('Click "Transfer" button')
    def click_transfer_button(self):
        self.transfer_button.click()


account_page = AccountPage()
