import allure
from selene import by, query
from selene.support.shared import browser

from core.apps.frontend.pages.base_page import BasePage


class AccountPage(BasePage):

    path = ''

    accounts_overview_link = browser.element(by.xpath("//a[contains(@href, '/parabank/overview.htm')]"))
    accounts_overview_balance = browser.element(by.xpath("// td[@class ='ng-binding'][1]"))
    accounts_overview_available_amount = browser.element(by.xpath("// td[@class ='ng-binding'][2]"))
    accounts_overview_total = browser.element(by.xpath("//b[@class='ng-binding']"))
    open_new_account = browser.element(by.xpath("//a[contains(@href, '/parabank/openaccount.htm')]"))
    account_type_dropdown = browser.element(by.xpath("//*[@id='type']"))
    savings_option = browser.element(by.xpath("//*[@id='type']/option[2]"))
    open_new_account_button = browser.element(by.xpath("//*[@value='Open New Account']"))
    first_name_input = browser.element(by.name("initialBalance"))
    submit_button = browser.element(by.xpath("//input[@value='Submit']"))

    def navigate(self):
        super().navigate()

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


account_page = AccountPage()
