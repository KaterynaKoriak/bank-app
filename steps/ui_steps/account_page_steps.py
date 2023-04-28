import allure
from hamcrest import equal_to
from conftest import WebDriver
from core.testlib.matchers import check_that
from selene.support.shared import browser
from core.apps.backend.user_api import user_account_api
from core.apps.frontend.pages.account_page import account_page


class AccountPageSteps:
    @allure.step('Navigate to the Open New Account page')
    def navigate_to_open_new_account(self) -> None:
        account_page.open_new_account()

    @allure.step('Create New Account')
    def create_new_account(self) -> None:
        account_page.open_account_type_dropdown()
        account_page.select_savings_account_type()
        account_page.click_open_new_account_button()

    @allure.step('Navigate to the Accounts Overview')
    def navigate_to_accounts_overview(self) -> None:
        account_page.click_accounts_overview_option()


account_page_steps = AccountPageSteps()


class AccountPageAssertSteps:
    @allure.step('Check balance on the Account overview page')
    def check_balance(self, username):
        check_that(account_page.accounts_overview_balance.text, equal_to(f'Welcome {username}'),
                   f'"Account balance = {}')

