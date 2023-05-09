import allure
from hamcrest import equal_to
from core.testlib.matchers import check_that
from core.apps.frontend.pages.account_page import account_page
from core.testlib.helpers.api_helpers import format_two_digits_after_comma
from constants.variables import test_messages


class AccountPageSteps:
    @allure.step('Navigate to the Open New Account page')
    def navigate_to_open_new_account(self) -> None:
        account_page.click_open_new_account_link()

    @allure.step('Create New Account')
    def create_savings_account(self) -> None:
        account_page.open_account_type_dropdown()
        account_page.select_savings_account_type()
        account_page.click_open_new_account_button()

    @allure.step('Navigate to the Accounts Overview')
    def navigate_to_accounts_overview(self) -> None:
        account_page.click_accounts_overview_option()


account_page_steps = AccountPageSteps()


class AccountPageAssertSteps:
    @allure.step('Check total balance on the Account overview page')
    def check_total_balance(self, initial_balance):
        check_that(account_page.accounts_overview_total().text,
                   equal_to(f"${format_two_digits_after_comma(initial_balance)}"),
                   f'Account total balance =${initial_balance}')

    @allure.step('Check balance on the Account overview page')
    def check_balance(self, initial_balance):
        balance = account_page.get_accounts_overview_balance(format_two_digits_after_comma(initial_balance))
        check_that(lambda: balance().text, (f"${format_two_digits_after_comma(initial_balance)}"),
                   f'Account balance = ${initial_balance}')

    @allure.step('Check available amount on the Account overview page')
    def check_available_amount(self, initial_balance):
        available_amount = account_page.get_accounts_overview_available_amount(
            format_two_digits_after_comma(initial_balance))
        check_that(available_amount().text, equal_to(f"${format_two_digits_after_comma(initial_balance)}"),
                   f'Available amount = ${initial_balance}')

    @allure.step('Check page title')
    def check_accounts_overview_navigation(self, title):
        check_that(lambda: account_page.accounts_overview_title().get_attribute("innerHTML"), equal_to(title),
                   f'page title is "{title}"')

    @allure.step('Check the minimal amount in the message on the Open new account page')
    def check_minimal_amount_message(self, min_balance):
        check_that(account_page.minimal_amount_message().text,
                   equal_to(test_messages['minimal_amount_message'].format(min_balance)),
                   f'"${format_two_digits_after_comma(min_balance)}" is in the message on the Open new account page')

    @allure.step('Check the title "Account Opened!" is displayed')
    def check_opened_account_title(self, title):
        check_that(lambda: account_page.account_opened_title().text, equal_to(title), "the title is 'Account Opened!'")

    @allure.step('Check that the first account has "initial balance - minimal balance" amount of money')
    def check_first_account_balance(self, initial_balance, minimal_balance):
        actual_balance = initial_balance - minimal_balance
        balance_value = account_page.get_accounts_overview_balance(format_two_digits_after_comma(actual_balance))
        check_that(lambda: balance_value().text, equal_to(f'${format_two_digits_after_comma(actual_balance)}'),
                   f'${actual_balance} is the balance on the first account')

    @allure.step('Check that the second account has "minimal balance" amount of money')
    def check_second_account_balance(self, minimal_balance):
        balance_value = account_page.get_accounts_overview_balance(format_two_digits_after_comma(minimal_balance))
        check_that(balance_value().text, equal_to(f'${format_two_digits_after_comma(minimal_balance)}'),
                   f'${minimal_balance} is the balance on the second account')


account_page_assert_steps = AccountPageAssertSteps()
